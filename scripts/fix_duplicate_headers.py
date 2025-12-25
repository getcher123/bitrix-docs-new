#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Исправление дублирующихся заголовков и разделителей
"""

import re
from pathlib import Path

class HeaderFixer:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.docs_dir = self.base_dir / "docs"
        self.fixed_count = 0
    
    def fix_file(self, md_file):
        """Исправить дублирующиеся заголовки в файле"""
        content = md_file.read_text(encoding='utf-8')
        original_content = content
        lines = content.split('\n')
        
        # Удалить дублирующиеся заголовки в начале файла
        # Паттерн: # Заголовок\n---\n# Заголовок
        if len(lines) >= 5:
            # Проверить первые 5 строк
            if (lines[0].startswith('#') and 
                lines[1].strip() == '' and
                lines[2].strip() == '---' and
                lines[3].strip() == '' and
                lines[4].startswith('#')):
                
                # Проверить, одинаковые ли заголовки
                h1 = lines[0].strip()
                h2 = lines[4].strip()
                
                if h1 == h2:
                    # Удалить первый заголовок и разделитель
                    lines = lines[4:]
                    self.fixed_count += 1
        
        # Удалить разделители сразу после заголовков
        cleaned_lines = []
        i = 0
        while i < len(lines):
            line = lines[i]
            cleaned_lines.append(line)
            
            # Если это заголовок
            if line.strip().startswith('#'):
                # Пропустить пустую строку
                if i + 1 < len(lines) and lines[i + 1].strip() == '':
                    i += 1
                    cleaned_lines.append(lines[i])
                    
                    # Пропустить разделитель
                    if i + 1 < len(lines) and lines[i + 1].strip() == '---':
                        i += 1  # Пропустить разделитель
                        # Пропустить пустую строку после разделителя
                        if i + 1 < len(lines) and lines[i + 1].strip() == '':
                            i += 1
            
            i += 1
        
        content = '\n'.join(cleaned_lines)
        
        # Удалить множественные пустые строки
        content = re.sub(r'\n{4,}', '\n\n\n', content)
        
        # Сохранить если изменилось
        if content != original_content:
            md_file.write_text(content, encoding='utf-8')
            return True
        
        return False
    
    def run(self):
        """Исправить все файлы"""
        print("\n" + "=" * 70)
        print("ИСПРАВЛЕНИЕ ДУБЛИРУЮЩИХСЯ ЗАГОЛОВКОВ")
        print("=" * 70)
        
        all_files = list(self.docs_dir.rglob("*.md"))
        total = len(all_files)
        changed = 0
        
        for i, md_file in enumerate(all_files, 1):
            if i % 50 == 0:
                print(f"Обработано {i}/{total} файлов...")
            
            if self.fix_file(md_file):
                changed += 1
        
        print("\n" + "=" * 70)
        print(f"✓ ИСПРАВЛЕНИЕ ЗАВЕРШЕНО!")
        print(f"  Обработано файлов: {total}")
        print(f"  Изменено файлов: {changed}")
        print(f"  Исправлено дублей: {self.fixed_count}")
        print("=" * 70)

if __name__ == "__main__":
    fixer = HeaderFixer("/home/ubuntu/bitrix-docs-new")
    fixer.run()
