#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Очистка документации от избыточных элементов
"""

import re
from pathlib import Path

class DocsCleanup:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.docs_dir = self.base_dir / "docs"
        self.cleaned_count = 0
    
    def clean_file(self, md_file):
        """Очистить один файл от избыточных элементов"""
        content = md_file.read_text(encoding='utf-8')
        original_content = content
        
        # 1. Удалить блок "Документация для разработчиков"
        # Ищем от "Документация для разработчиков" до первого заголовка или ---
        pattern1 = r'\*\*Документация для разработчиков\*\*.*?(?=\n#|\n---|\Z)'
        content = re.sub(pattern1, '', content, flags=re.DOTALL)
        
        # 2. Удалить альтернативный вариант навигационного блока
        pattern2 = r'\[Документация для разработчиков\].*?(?=\n#|\n---|\Z)'
        content = re.sub(pattern2, '', content, flags=re.DOTALL)
        
        # 3. Удалить футер "Новинки документации в соцсетях"
        pattern3 = r'\*\*Новинки документации в соцсетях:.*?(?=\n#|\Z)'
        content = re.sub(pattern3, '', content, flags=re.DOTALL)
        
        # 4. Удалить строку "**Источник:**"
        pattern4 = r'\*\*Источник:\*\*\s+https?://[^\n]+\n*'
        content = re.sub(pattern4, '', content)
        
        # 5. Удалить множественные пустые строки (больше 2 подряд)
        content = re.sub(r'\n{4,}', '\n\n\n', content)
        
        # 6. Удалить пустые строки в начале файла
        content = content.lstrip('\n')
        
        # 7. Убедиться что после заголовка есть пустая строка
        content = re.sub(r'(^#[^\n]+)\n([^#\n-])', r'\1\n\n\2', content, flags=re.MULTILINE)
        
        # Сохранить если изменилось
        if content != original_content:
            md_file.write_text(content, encoding='utf-8')
            return True
        
        return False
    
    def run(self):
        """Очистить все файлы"""
        print("\n" + "=" * 70)
        print("ОЧИСТКА ДОКУМЕНТАЦИИ")
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
    cleanup = DocsCleanup("/home/ubuntu/bitrix-docs-new")
    cleanup.run()
