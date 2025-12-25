#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Удаление футеров и лент сообщений из документации
"""

import re
from pathlib import Path

class FooterRemover:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.docs_dir = self.base_dir / "docs"
        self.removed_count = 0
    
    def clean_file(self, md_file):
        """Удалить футеры из файла"""
        content = md_file.read_text(encoding='utf-8')
        original_content = content
        
        # Паттерны для удаления
        patterns = [
            # Новинки документации в соцсетях
            r'Новинки документации в соцсетях:.*?(?=\n\n|\Z)',
            r'---\s*Новинки документации в соцсетях:.*?(?=\n\n|\Z)',
            
            # Пользовательские комментарии
            r'####\s*Пользовательские комментарии.*?(?=\n\n|\Z)',
            r'Пользовательские комментарии.*?обращайтесь на форумы\.',
            
            # Копирайт Битрикс
            r'©\s*«Битрикс».*?Наверх.*?(?=\n|\Z)',
            r'©\s*«Битрикс».*?\d{4}.*?(?=\n|\Z)',
            
            # Лента сообщений
            r'\*\*Лента сообщений\*\*.*?(?=\n\n|\Z)',
            
            # Соцсети (VK, Twitter и т.д.)
            r'\[VK\].*?\[Twitter\].*?\[Telegram\].*?(?=\n|\Z)',
            r'VK\s*\|\s*Twitter\s*\|\s*Facebook.*?(?=\n|\Z)',
        ]
        
        # Применить все паттерны
        for pattern in patterns:
            content = re.sub(pattern, '', content, flags=re.DOTALL | re.IGNORECASE)
        
        # Удалить множественные пустые строки в конце
        content = re.sub(r'\n{3,}\Z', '\n\n', content)
        
        # Удалить пробелы в конце строк
        lines = content.split('\n')
        lines = [line.rstrip() for line in lines]
        content = '\n'.join(lines)
        
        # Убедиться, что файл заканчивается одной пустой строкой
        content = content.rstrip() + '\n'
        
        # Сохранить если изменилось
        if content != original_content:
            md_file.write_text(content, encoding='utf-8')
            self.removed_count += 1
            return True
        
        return False
    
    def run(self):
        """Обработать все файлы"""
        print("\n" + "=" * 70)
        print("УДАЛЕНИЕ ФУТЕРОВ И ЛЕНТ СООБЩЕНИЙ")
        print("=" * 70)
        
        all_files = list(self.docs_dir.rglob("*.md"))
        # Исключить навигационные файлы
        exclude_files = ['AGENT.md', 'MODULES.md', 'QUICK_REFERENCE.md', 'README.md', 'INDEX.md']
        all_files = [f for f in all_files if f.name not in exclude_files]
        
        total = len(all_files)
        changed = 0
        
        for i, md_file in enumerate(all_files, 1):
            if i % 50 == 0:
                print(f"Обработано {i}/{total} файлов...")
            
            if self.clean_file(md_file):
                changed += 1
        
        print("\n" + "=" * 70)
        print(f"✓ УДАЛЕНИЕ ЗАВЕРШЕНО!")
        print(f"  Обработано файлов: {total}")
        print(f"  Изменено файлов: {changed}")
        print(f"  Удалено футеров: {self.removed_count}")
        print("=" * 70)

if __name__ == "__main__":
    remover = FooterRemover("/home/ubuntu/bitrix-docs-new")
    remover.run()
