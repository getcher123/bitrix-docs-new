#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для удаления ВСЕХ внешних ссылок и замены на локальные
"""

import re
import json
from pathlib import Path
from urllib.parse import urlparse, urljoin

class LinksFixer:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.docs_dir = self.base_dir / "docs"
        self.url_to_file = {}
        self.fixed_count = 0
        self.removed_count = 0
        
        # Загрузить маппинг URL -> файл
        self.load_url_mapping()
    
    def load_url_mapping(self):
        """Загрузить маппинг URL к файлам"""
        mapping_file = self.base_dir / "url_mapping.json"
        if mapping_file.exists():
            self.url_to_file = json.loads(mapping_file.read_text(encoding='utf-8'))
            print(f"Загружен маппинг для {len(self.url_to_file)} URL")
        
        # Также построить маппинг из файлов
        for md_file in self.docs_dir.rglob("*.md"):
            content = md_file.read_text(encoding='utf-8')
            match = re.search(r'\*\*Источник:\*\*\s+(https?://[^\s\n]+)', content)
            if match:
                url = match.group(1)
                rel_path = md_file.relative_to(self.docs_dir)
                self.url_to_file[url] = str(rel_path)
                
                # Также без параметров и якорей
                base_url = url.split('?')[0].split('#')[0]
                if base_url != url:
                    self.url_to_file[base_url] = str(rel_path)
        
        print(f"Всего в маппинге: {len(self.url_to_file)} URL")
    
    def url_to_relative_path(self, url, current_file):
        """Конвертировать URL в относительный путь"""
        # Убрать якорь
        anchor = ""
        if '#' in url:
            url, anchor_part = url.split('#', 1)
            anchor = f"#{anchor_part}"
        
        # Убрать параметры print
        url = url.replace('?print=Y', '').replace('&print=Y', '')
        url = url.rstrip('?&')
        
        # Проверить в маппинге
        if url in self.url_to_file:
            target_file = self.docs_dir / self.url_to_file[url]
            current_dir = current_file.parent
            
            try:
                # Вычислить относительный путь
                rel_path = target_file.relative_to(current_dir)
                return f"{rel_path}{anchor}"
            except ValueError:
                # Если не получается, использовать путь от корня docs
                parts_count = len(current_file.relative_to(self.docs_dir).parts) - 1
                prefix = "../" * parts_count
                return f"{prefix}{self.url_to_file[url]}{anchor}"
        
        return None
    
    def fix_links_in_file(self, md_file):
        """Исправить ссылки в одном файле"""
        content = md_file.read_text(encoding='utf-8')
        original_content = content
        
        file_fixed = 0
        file_removed = 0
        
        def replace_link(match):
            nonlocal file_fixed, file_removed
            
            text = match.group(1)
            url = match.group(2)
            
            # Пропустить якоря и mailto
            if url.startswith('#') or url.startswith('mailto:'):
                return match.group(0)
            
            # Пропустить уже локальные ссылки
            if not url.startswith('http'):
                # Но проверить, не указывает ли на несуществующий файл
                return match.group(0)
            
            # Обработать ссылки на dev.1c-bitrix.ru
            if 'dev.1c-bitrix.ru' in url or '1c-bitrix.ru' in url:
                # Попробовать конвертировать в локальную
                local_path = self.url_to_relative_path(url, md_file)
                
                if local_path:
                    file_fixed += 1
                    return f"[{text}]({local_path})"
                else:
                    # Если не нашли локальный файл - удалить ссылку, оставить текст
                    file_removed += 1
                    return f"**{text}**"
            
            # Внешние ссылки на другие сайты - оставить как есть
            return match.group(0)
        
        # Заменить все ссылки
        content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, content)
        
        # Сохранить если изменилось
        if content != original_content:
            md_file.write_text(content, encoding='utf-8')
            self.fixed_count += file_fixed
            self.removed_count += file_removed
            return True
        
        return False
    
    def run(self):
        """Исправить ссылки во всех файлах"""
        print("\n" + "=" * 70)
        print("ИСПРАВЛЕНИЕ ССЫЛОК")
        print("=" * 70)
        
        files_processed = 0
        files_changed = 0
        
        all_files = list(self.docs_dir.rglob("*.md"))
        total = len(all_files)
        
        for i, md_file in enumerate(all_files, 1):
            if i % 50 == 0:
                print(f"Обработано {i}/{total} файлов...")
            
            files_processed += 1
            if self.fix_links_in_file(md_file):
                files_changed += 1
        
        print("\n" + "=" * 70)
        print(f"✓ ИСПРАВЛЕНИЕ ЗАВЕРШЕНО!")
        print(f"  Обработано файлов: {files_processed}")
        print(f"  Изменено файлов: {files_changed}")
        print(f"  Ссылок конвертировано: {self.fixed_count}")
        print(f"  Ссылок удалено: {self.removed_count}")
        print("=" * 70)

if __name__ == "__main__":
    fixer = LinksFixer("/home/ubuntu/bitrix-docs-new")
    fixer.run()
