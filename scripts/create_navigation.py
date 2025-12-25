#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Создание навигационной системы для хранилища
"""

import re
from pathlib import Path
from collections import defaultdict

class NavigationBuilder:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.docs_dir = self.base_dir / "docs"
        self.modules = defaultdict(list)
    
    def extract_title(self, md_file):
        """Извлечь заголовок из MD файла"""
        try:
            content = md_file.read_text(encoding='utf-8')
            match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if match:
                title = match.group(1).strip()
                # Убрать markdown форматирование
                title = re.sub(r'\*\*(.+?)\*\*', r'\1', title)
                title = re.sub(r'\*(.+?)\*', r'\1', title)
                return title
            return md_file.stem
        except:
            return md_file.stem
    
    def build_tree(self):
        """Построить дерево файлов"""
        tree = defaultdict(list)
        
        for md_file in self.docs_dir.rglob("*.md"):
            rel_path = md_file.relative_to(self.docs_dir)
            parts = rel_path.parts
            
            if len(parts) == 1:
                # Корневой файл
                tree['_root'].append({
                    'file': md_file,
                    'path': rel_path,
                    'title': self.extract_title(md_file)
                })
            else:
                # Файл в модуле
                module = parts[0]
                tree[module].append({
                    'file': md_file,
                    'path': rel_path,
                    'title': self.extract_title(md_file)
                })
        
        return tree
    
    def create_main_index(self, tree):
        """Создать главный индекс"""
        content = "# Полный индекс документации 1C-Bitrix\n\n"
        content += "Полное хранилище документации API 1C-Bitrix для локального использования.\n\n"
        content += "---\n\n"
        
        # Корневые файлы
        if '_root' in tree:
            content += "## Главные страницы\n\n"
            for item in sorted(tree['_root'], key=lambda x: x['title']):
                content += f"- [{item['title']}](./{item['path']})\n"
            content += "\n"
        
        # Модули
        content += "## Модули и разделы\n\n"
        
        for module in sorted(tree.keys()):
            if module == '_root':
                continue
            
            files = tree[module]
            content += f"### {module}\n\n"
            
            # Сначала index.md
            index_files = [f for f in files if f['path'].name == 'index.md']
            other_files = [f for f in files if f['path'].name != 'index.md']
            
            for item in index_files:
                content += f"- **[{item['title']}](./{item['path']})** *(главная страница модуля)*\n"
            
            for item in sorted(other_files, key=lambda x: x['title']):
                content += f"- [{item['title']}](./{item['path']})\n"
            
            content += "\n"
        
        # Статистика
        total_files = sum(len(files) for files in tree.values())
        total_modules = len([k for k in tree.keys() if k != '_root'])
        
        content += "---\n\n"
        content += "## Статистика\n\n"
        content += f"- **Модулей:** {total_modules}\n"
        content += f"- **Страниц:** {total_files}\n"
        content += f"- **Изображений:** {len(list((self.base_dir / 'images').glob('*')))}\n\n"
        
        # Сохранить
        index_file = self.docs_dir / "INDEX.md"
        index_file.write_text(content, encoding='utf-8')
        
        print(f"✓ Создан главный индекс: INDEX.md")
        print(f"  Модулей: {total_modules}")
        print(f"  Страниц: {total_files}")
    
    def create_readme(self):
        """Создать README для docs"""
        content = """# Хранилище документации 1C-Bitrix

Локальное хранилище документации по API 1C-Bitrix в формате Markdown.

## Навигация

- **[INDEX.md](./INDEX.md)** - Полный алфавитный указатель всех страниц
- **[index.md](./index.md)** - Главная страница документации API

## Структура

Документация организована по модулям:
- Каждый модуль находится в отдельной папке
- Файл `index.md` - главная страница модуля
- Остальные файлы - подразделы и классы

## Использование

1. Откройте файл `index.md` для начала работы
2. Используйте ссылки для навигации между документами
3. Все ссылки локальные и работают без интернета
4. Изображения находятся в папке `../images/`

## Поиск

### Visual Studio Code
- `Ctrl+Shift+F` - поиск по всем файлам

### Командная строка
```bash
grep -r "искомый_текст" .
```

---

**Источник:** https://dev.1c-bitrix.ru/api_help/  
**Версия:** 2.0 (полная)  
**Дата:** 23.12.2025
"""
        
        readme_file = self.docs_dir / "README.md"
        readme_file.write_text(content, encoding='utf-8')
        
        print(f"✓ Создан README.md для docs/")
    
    def run(self):
        """Создать всю навигацию"""
        print("\n" + "=" * 70)
        print("СОЗДАНИЕ НАВИГАЦИИ")
        print("=" * 70)
        
        tree = self.build_tree()
        self.create_main_index(tree)
        self.create_readme()
        
        print("=" * 70)

if __name__ == "__main__":
    builder = NavigationBuilder("/home/ubuntu/bitrix-docs-new")
    builder.run()
