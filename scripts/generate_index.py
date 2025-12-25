#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Генератор навигационного индекса для документации
"""

import re
from pathlib import Path
from collections import defaultdict

class IndexGenerator:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.docs_dir = self.base_dir / "docs"
        self.modules = defaultdict(list)
    
    def extract_title(self, md_file):
        """Извлечь заголовок из MD файла"""
        try:
            content = md_file.read_text(encoding='utf-8')
            # Найти первый заголовок H1
            match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if match:
                return match.group(1).strip()
            return md_file.stem
        except:
            return md_file.stem
    
    def scan_modules(self):
        """Сканировать все модули и файлы"""
        for module_dir in sorted(self.docs_dir.iterdir()):
            if module_dir.is_dir():
                module_name = module_dir.name
                files = []
                
                for md_file in sorted(module_dir.glob("*.md")):
                    title = self.extract_title(md_file)
                    rel_path = md_file.relative_to(self.docs_dir)
                    files.append({
                        'title': title,
                        'path': str(rel_path),
                        'filename': md_file.name
                    })
                
                if files:
                    self.modules[module_name] = files
    
    def generate_index(self):
        """Сгенерировать файл индекса"""
        self.scan_modules()
        
        index_content = "# Полный индекс документации 1C-Bitrix\n\n"
        index_content += "Алфавитный указатель всех разделов и страниц документации.\n\n"
        index_content += "---\n\n"
        
        # Главная страница
        main_index = self.docs_dir / "index.md"
        if main_index.exists():
            index_content += "## Главная страница\n\n"
            index_content += f"- [Документация 1C-Bitrix API](./index.md)\n\n"
            index_content += "---\n\n"
        
        # Модули
        index_content += "## Модули документации\n\n"
        
        for module_name in sorted(self.modules.keys()):
            files = self.modules[module_name]
            index_content += f"### {module_name}\n\n"
            
            for file_info in files:
                title = file_info['title']
                path = file_info['path']
                
                # Отметить главную страницу модуля
                if file_info['filename'] == 'index.md':
                    index_content += f"- **[{title}](./{path})** *(главная страница модуля)*\n"
                else:
                    index_content += f"- [{title}](./{path})\n"
            
            index_content += "\n"
        
        # Статистика
        total_files = sum(len(files) for files in self.modules.values())
        index_content += "---\n\n"
        index_content += "## Статистика\n\n"
        index_content += f"- **Модулей:** {len(self.modules)}\n"
        index_content += f"- **Страниц:** {total_files}\n"
        index_content += f"- **Изображений:** {len(list((self.base_dir / 'images').glob('*')))}\n\n"
        
        # Сохранить индекс
        index_file = self.docs_dir / "INDEX.md"
        index_file.write_text(index_content, encoding='utf-8')
        
        print(f"✓ Создан индекс: {index_file}")
        print(f"  Модулей: {len(self.modules)}")
        print(f"  Страниц: {total_files}")
    
    def generate_module_navigation(self):
        """Добавить навигацию в каждый модуль"""
        for module_name, files in self.modules.items():
            if len(files) <= 1:
                continue
            
            module_dir = self.docs_dir / module_name
            
            # Создать навигационный файл для модуля
            nav_content = f"# Навигация: {module_name}\n\n"
            nav_content += "## Страницы модуля\n\n"
            
            for file_info in files:
                title = file_info['title']
                filename = file_info['filename']
                nav_content += f"- [{title}](./{filename})\n"
            
            nav_content += f"\n[← Вернуться к главной](./../index.md)\n"
            
            nav_file = module_dir / "NAVIGATION.md"
            nav_file.write_text(nav_content, encoding='utf-8')
        
        print(f"✓ Создана навигация для {len(self.modules)} модулей")

if __name__ == "__main__":
    generator = IndexGenerator("/home/ubuntu/bitrix-docs-storage")
    generator.generate_index()
    generator.generate_module_navigation()
