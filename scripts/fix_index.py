#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Исправление INDEX.md - удаление "Источник:" из заголовков ссылок
"""

import re
from pathlib import Path

def fix_index():
    index_file = Path("/home/ubuntu/bitrix-docs-new/docs/INDEX.md")
    content = index_file.read_text(encoding='utf-8')
    
    # Удалить "Источник: URL" из заголовков ссылок
    # Было: [Источник: https://...](./path.md)
    # Станет: просто извлечь заголовок из файла или использовать имя файла
    
    # Простое решение - удалить "Источник: URL" и оставить путь
    content = re.sub(r'\[Источник:\s*https?://[^\]]+\]', '[Документация]', content)
    
    index_file.write_text(content, encoding='utf-8')
    print("✓ INDEX.md исправлен")

if __name__ == "__main__":
    fix_index()
