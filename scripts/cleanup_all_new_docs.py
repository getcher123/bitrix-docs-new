#!/usr/bin/env python3
"""
Очистка всей новой документации от мусора и внешних ссылок
"""

import os
import re

DOCS_DIRS = [
    "/home/ubuntu/bitrix-docs-new/docs/d7",
    "/home/ubuntu/bitrix-docs-new/docs/user_help",
    "/home/ubuntu/bitrix-docs-new/docs/courses",
    "/home/ubuntu/bitrix-docs-new/docs/bitrix24_api",
]

def clean_file(file_path):
    """Очистка одного файла"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 1. Удаляем дублирующиеся заголовки
        lines = content.split('\n')
        cleaned_lines = []
        i = 0
        while i < len(lines):
            line = lines[i]
            # Проверяем дубли заголовков
            if line.startswith('#') and i + 2 < len(lines):
                if lines[i+1] == '---' and lines[i+2] == line:
                    # Пропускаем первый заголовок и разделитель
                    i += 2
                    continue
            cleaned_lines.append(line)
            i += 1
        
        content = '\n'.join(cleaned_lines)
        
        # 2. Удаляем футеры
        footers_patterns = [
            r'Новинки документации в соцсетях:.*?(?=\n\n|\Z)',
            r'Пользовательские комментарии.*?(?=\n\n|\Z)',
            r'©.*?Битрикс.*?(?=\n\n|\Z)',
            r'Курсы разработаны в компании.*?(?=\n\n|\Z)',
        ]
        
        for pattern in footers_patterns:
            content = re.sub(pattern, '', content, flags=re.DOTALL | re.IGNORECASE)
        
        # 3. Удаляем строки "Источник:"
        content = re.sub(r'\*\*Источник:\*\*.*?\n', '', content)
        
        # 4. Удаляем навигационные блоки
        nav_patterns = [
            r'Документация для разработчиков.*?(?=\n#|\Z)',
            r'Разделы документации:.*?(?=\n#|\Z)',
        ]
        
        for pattern in nav_patterns:
            content = re.sub(pattern, '', content, flags=re.DOTALL | re.IGNORECASE)
        
        # 5. Удаляем внешние ссылки на dev.1c-bitrix.ru (кроме справочных)
        # Заменяем ссылки вида [текст](https://dev.1c-bitrix.ru/...) на просто текст
        content = re.sub(
            r'\[([^\]]+)\]\(https?://dev\.1c-bitrix\.ru/(?:docs|api_help|api_d7|user_help|learning)/[^\)]*\)',
            r'\1',
            content
        )
        
        # 6. Удаляем пустые ссылки
        content = re.sub(r'\[([^\]]+)\]\(\)', r'\1', content)
        
        # 7. Очищаем множественные пустые строки
        content = re.sub(r'\n{4,}', '\n\n\n', content)
        
        # 8. Удаляем trailing whitespace
        lines = [line.rstrip() for line in content.split('\n')]
        content = '\n'.join(lines)
        
        # 9. Добавляем trailing newline
        if content and not content.endswith('\n'):
            content += '\n'
        
        # Сохраняем только если были изменения
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
    
    except Exception as e:
        print(f"Ошибка при обработке {file_path}: {e}")
        return False

def main():
    print("="*60)
    print("ОЧИСТКА НОВОЙ ДОКУМЕНТАЦИИ")
    print("="*60)
    
    total_files = 0
    modified_files = 0
    
    for docs_dir in DOCS_DIRS:
        if not os.path.exists(docs_dir):
            print(f"\n⚠️  Директория не найдена: {docs_dir}")
            continue
        
        print(f"\n📁 Обработка: {os.path.basename(docs_dir)}")
        dir_files = 0
        dir_modified = 0
        
        for root, dirs, files in os.walk(docs_dir):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    dir_files += 1
                    total_files += 1
                    
                    if clean_file(file_path):
                        dir_modified += 1
                        modified_files += 1
        
        print(f"   Обработано: {dir_files} файлов")
        print(f"   Изменено: {dir_modified} файлов")
    
    print("\n" + "="*60)
    print("ОЧИСТКА ЗАВЕРШЕНА")
    print("="*60)
    print(f"Всего обработано: {total_files} файлов")
    print(f"Изменено: {modified_files} файлов")

if __name__ == "__main__":
    main()
