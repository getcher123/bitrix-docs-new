#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Улучшенная очистка документации от избыточных элементов
"""

import re
from pathlib import Path

class DocsCleanupV2:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.docs_dir = self.base_dir / "docs"
        self.cleaned_count = 0
    
    def clean_file(self, md_file):
        """Очистить один файл от избыточных элементов"""
        content = md_file.read_text(encoding='utf-8')
        original_content = content
        
        # 1. Удалить строку "Документация для разработчиков" (без ссылок)
        content = re.sub(r'^Документация для разработчиков\s*\n', '', content, flags=re.MULTILINE)
        
        # 2. Удалить блок с множественными ссылками на модули (обычно в начале)
        # Ищем блоки где много ссылок подряд (больше 5)
        lines = content.split('\n')
        cleaned_lines = []
        link_count = 0
        skip_mode = False
        
        for i, line in enumerate(lines):
            # Подсчитать количество ссылок в строке
            links_in_line = len(re.findall(r'\[.*?\]\(.*?\)', line))
            
            if links_in_line > 3:  # Строка с множественными ссылками
                link_count += 1
                if link_count > 2:  # Если больше 2 строк подряд с множественными ссылками
                    skip_mode = True
                    continue
            else:
                if skip_mode and line.strip() == '':
                    continue  # Пропустить пустые строки после блока ссылок
                skip_mode = False
                link_count = 0
            
            cleaned_lines.append(line)
        
        content = '\n'.join(cleaned_lines)
        
        # 3. Удалить футер "Новинки документации в соцсетях"
        content = re.sub(r'\*\*Новинки документации в соцсетях:.*', '', content, flags=re.DOTALL)
        
        # 4. Удалить строку "**Источник:**"
        content = re.sub(r'\*\*Источник:\*\*\s+https?://[^\n]+\n*', '', content)
        
        # 5. Удалить разделитель --- если он идет сразу после заголовка
        content = re.sub(r'(^#[^\n]+)\n---\n', r'\1\n\n', content, flags=re.MULTILINE)
        
        # 6. Удалить множественные пустые строки (больше 2 подряд)
        content = re.sub(r'\n{4,}', '\n\n\n', content)
        
        # 7. Удалить пустые строки в начале файла
        content = content.lstrip('\n')
        
        # 8. Добавить пустую строку после заголовка если её нет
        content = re.sub(r'(^#[^\n]+)\n([^#\n\s])', r'\1\n\n\2', content, flags=re.MULTILINE)
        
        # Сохранить если изменилось
        if content != original_content:
            md_file.write_text(content, encoding='utf-8')
            return True
        
        return False
    
    def run(self):
        """Очистить все файлы"""
        print("\n" + "=" * 70)
        print("УЛУЧШЕННАЯ ОЧИСТКА ДОКУМЕНТАЦИИ")
        print("=" * 70)
        
        all_files = list(self.docs_dir.rglob("*.md"))
        total = len(all_files)
        
        for i, md_file in enumerate(all_files, 1):
            if i % 50 == 0:
                print(f"Обработано {i}/{total} файлов...")
            
            if self.clean_file(md_file):
                self.cleaned_count += 1
        
        print("\n" + "=" * 70)
        print(f"✓ ОЧИСТКА ЗАВЕРШЕНА!")
        print(f"  Обработано файлов: {total}")
        print(f"  Очищено файлов: {self.cleaned_count}")
        print("=" * 70)

if __name__ == "__main__":
    cleanup = DocsCleanupV2("/home/ubuntu/bitrix-docs-new")
    cleanup.run()
