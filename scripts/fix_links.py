#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для исправления внутренних ссылок в документации
"""

import re
from pathlib import Path
from urllib.parse import urlparse, unquote

class LinkFixer:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.docs_dir = self.base_dir / "docs"
        self.url_to_file = {}
        
        # Построить карту URL -> файл
        self.build_url_map()
    
    def build_url_map(self):
        """Построить карту соответствия URL к локальным файлам"""
        for md_file in self.docs_dir.rglob("*.md"):
            content = md_file.read_text(encoding='utf-8')
            
            # Извлечь исходный URL из файла
            match = re.search(r'\*\*Источник:\*\*\s+(https?://[^\s\n]+)', content)
            if match:
                url = match.group(1)
                # Относительный путь от docs
                rel_path = md_file.relative_to(self.docs_dir)
                self.url_to_file[url] = str(rel_path)
                
                # Также добавить без параметров
                base_url = url.split('?')[0].split('#')[0]
                if base_url != url:
                    self.url_to_file[base_url] = str(rel_path)
        
        print(f"Построена карта для {len(self.url_to_file)} URL")
    
    def convert_link(self, url, current_file):
        """Конвертировать URL в относительную ссылку"""
        # Удалить якорь
        anchor = ""
        if '#' in url:
            url, anchor = url.split('#', 1)
            anchor = f"#{anchor}"
        
        # Проверить в карте
        if url in self.url_to_file:
            target_file = self.url_to_file[url]
            # Вычислить относительный путь
            current_dir = current_file.parent
            target_path = self.docs_dir / target_file
            
            try:
                rel_path = target_path.relative_to(current_dir)
                return f"{rel_path}{anchor}"
            except ValueError:
                # Если не получается относительный путь, использовать абсолютный от docs
                return f"../{target_file}{anchor}"
        
        return url + anchor
    
    def fix_file_links(self, md_file):
        """Исправить ссылки в одном файле"""
        content = md_file.read_text(encoding='utf-8')
        original_content = content
        
        # Найти все ссылки вида [текст](url)
        def replace_link(match):
            text = match.group(1)
            url = match.group(2)
            
            # Пропустить якоря и внешние ссылки
            if url.startswith('#') or not ('1c-bitrix.ru' in url or url.startswith('/')):
                return match.group(0)
            
            # Конвертировать внутренние ссылки
            if '1c-bitrix.ru' in url or url.startswith('/api_help'):
                if not url.startswith('http'):
                    url = f"https://dev.1c-bitrix.ru{url}"
                
                new_url = self.convert_link(url, md_file)
                return f"[{text}]({new_url})"
            
            return match.group(0)
        
        content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, content)
        
        # Сохранить если изменилось
        if content != original_content:
            md_file.write_text(content, encoding='utf-8')
            return True
        return False
    
    def run(self):
        """Исправить ссылки во всех файлах"""
        print("Исправление внутренних ссылок...")
        
        fixed_count = 0
        for md_file in self.docs_dir.rglob("*.md"):
            if self.fix_file_links(md_file):
                fixed_count += 1
                print(f"  Исправлено: {md_file.name}")
        
        print(f"\n✓ Обработано файлов: {fixed_count}")

if __name__ == "__main__":
    fixer = LinkFixer("/home/ubuntu/bitrix-docs-storage")
    fixer.run()
