#!/usr/bin/env python3
"""
Парсер документации API D7 для 1C-Bitrix
"""

import requests
from bs4 import BeautifulSoup
import os
import time
import re
from urllib.parse import urljoin, urlparse
# import html2text - не используется

BASE_URL = "https://dev.1c-bitrix.ru"
START_URL = "https://dev.1c-bitrix.ru/api_d7/"
OUTPUT_DIR = "/home/ubuntu/bitrix-docs-new/docs/d7"
IMAGES_DIR = "/home/ubuntu/bitrix-docs-new/images/d7"

# Создаем директории
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

# Множество для отслеживания посещенных URL
visited_urls = set()
# Словарь для маппинга URL -> локальный путь
url_to_path = {}

def clean_filename(name):
    """Очистка имени файла от недопустимых символов"""
    name = re.sub(r'[<>:"/\\|?*]', '_', name)
    name = re.sub(r'\s+', '_', name)
    name = name.strip('._')
    return name[:200]  # Ограничение длины

def download_image(img_url, base_path):
    """Скачивание изображения"""
    try:
        if not img_url.startswith('http'):
            img_url = urljoin(BASE_URL, img_url)
        
        response = requests.get(img_url, timeout=30)
        if response.status_code == 200:
            # Определяем имя файла
            img_name = os.path.basename(urlparse(img_url).path)
            if not img_name:
                img_name = f"image_{hash(img_url)}.png"
            
            img_path = os.path.join(IMAGES_DIR, clean_filename(img_name))
            
            with open(img_path, 'wb') as f:
                f.write(response.content)
            
            # Возвращаем относительный путь
            return os.path.relpath(img_path, base_path)
    except Exception as e:
        print(f"Ошибка загрузки изображения {img_url}: {e}")
    
    return None

def clean_content(soup):
    """Удаление навигации, футеров и прочего мусора"""
    # Удаляем навигационные элементы
    for elem in soup.find_all(['nav', 'header', 'footer']):
        elem.decompose()
    
    # Удаляем элементы с классами навигации
    for elem in soup.find_all(class_=re.compile(r'(nav|menu|breadcrumb|sidebar|footer|header)', re.I)):
        elem.decompose()
    
    # Удаляем скрипты и стили
    for elem in soup.find_all(['script', 'style', 'noscript']):
        elem.decompose()
    
    # Удаляем комментарии
    for elem in soup.find_all(string=lambda text: isinstance(text, str) and text.strip().startswith('<!--')):
        elem.extract()
    
    return soup

def html_to_markdown(html_content, base_path):
    """Конвертация HTML в Markdown"""
    soup = BeautifulSoup(html_content, 'html.parser')
    soup = clean_content(soup)
    
    markdown_lines = []
    
    def process_element(elem, level=0):
        if elem.name is None:
            # Текстовый узел
            text = str(elem).strip()
            if text:
                return text
            return ''
        
        if elem.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level_num = int(elem.name[1])
            return '#' * level_num + ' ' + elem.get_text().strip()
        
        elif elem.name == 'p':
            return elem.get_text().strip()
        
        elif elem.name == 'a':
            text = elem.get_text().strip()
            href = elem.get('href', '')
            if href and text:
                return f'[{text}]({href})'
            return text
        
        elif elem.name == 'img':
            src = elem.get('src', '')
            alt = elem.get('alt', 'image')
            if src:
                local_img_path = download_image(src, base_path)
                if local_img_path:
                    return f'![{alt}]({local_img_path})'
            return ''
        
        elif elem.name in ['ul', 'ol']:
            items = []
            for i, li in enumerate(elem.find_all('li', recursive=False)):
                prefix = '-' if elem.name == 'ul' else f'{i+1}.'
                items.append(f'{prefix} {li.get_text().strip()}')
            return '\n'.join(items)
        
        elif elem.name == 'code':
            return f'`{elem.get_text()}`'
        
        elif elem.name == 'pre':
            code = elem.find('code')
            if code:
                return f'```\n{code.get_text()}\n```'
            return f'```\n{elem.get_text()}\n```'
        
        elif elem.name in ['strong', 'b']:
            return f'**{elem.get_text().strip()}**'
        
        elif elem.name in ['em', 'i']:
            return f'*{elem.get_text().strip()}*'
        
        elif elem.name == 'table':
            # Простая обработка таблиц
            rows = []
            for tr in elem.find_all('tr'):
                cells = [td.get_text().strip() for td in tr.find_all(['td', 'th'])]
                if cells:
                    rows.append('| ' + ' | '.join(cells) + ' |')
            if len(rows) > 1:
                # Добавляем разделитель после заголовка
                header_sep = '| ' + ' | '.join(['---'] * len(rows[0].split('|')[1:-1])) + ' |'
                rows.insert(1, header_sep)
            return '\n'.join(rows)
        
        elif elem.name == 'br':
            return '\n'
        
        elif elem.name in ['div', 'section', 'article']:
            # Рекурсивно обрабатываем содержимое
            content = []
            for child in elem.children:
                result = process_element(child, level)
                if result:
                    content.append(result)
            return '\n\n'.join(content)
        
        else:
            # Для остальных элементов просто извлекаем текст
            return elem.get_text().strip()
    
    # Обрабатываем все дочерние элементы
    for child in soup.children:
        result = process_element(child)
        if result:
            markdown_lines.append(result)
    
    markdown = '\n\n'.join(markdown_lines)
    
    # Очистка от лишних пустых строк
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)
    
    return markdown

def parse_page(url, depth=0, max_depth=5):
    """Рекурсивный парсинг страницы"""
    if depth > max_depth or url in visited_urls:
        return
    
    # Проверяем, что URL относится к API D7
    if not url.startswith(START_URL):
        return
    
    visited_urls.add(url)
    print(f"{'  ' * depth}Парсинг: {url}")
    
    try:
        response = requests.get(url, timeout=30)
        if response.status_code != 200:
            print(f"Ошибка {response.status_code}: {url}")
            return
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Извлекаем заголовок
        title = soup.find('h1')
        if title:
            title_text = title.get_text().strip()
        else:
            title_text = "Без названия"
        
        # Определяем путь для сохранения
        url_path = urlparse(url).path
        url_path = url_path.replace('/api_d7/', '').strip('/')
        
        if not url_path or url_path == '':
            file_path = os.path.join(OUTPUT_DIR, "index.md")
        else:
            # Создаем структуру папок
            parts = url_path.split('/')
            if len(parts) > 1:
                dir_path = os.path.join(OUTPUT_DIR, *parts[:-1])
                os.makedirs(dir_path, exist_ok=True)
                file_path = os.path.join(dir_path, clean_filename(parts[-1]) + ".md")
            else:
                file_path = os.path.join(OUTPUT_DIR, clean_filename(url_path) + ".md")
        
        # Сохраняем маппинг
        url_to_path[url] = file_path
        
        # Извлекаем основной контент
        content_div = soup.find('div', class_=re.compile(r'content|main|article', re.I))
        if not content_div:
            content_div = soup.find('main') or soup.find('article') or soup.body
        
        if content_div:
            # Конвертируем в Markdown
            markdown = html_to_markdown(str(content_div), os.path.dirname(file_path))
            
            # Добавляем заголовок
            full_content = f"# {title_text}\n\n{markdown}"
            
            # Сохраняем файл
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(full_content)
            
            print(f"{'  ' * depth}Сохранено: {file_path}")
        
        # Находим все ссылки на подстраницы
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(url, href)
            
            # Парсим только ссылки внутри API D7
            if full_url.startswith(START_URL) and full_url not in visited_urls:
                time.sleep(0.5)  # Задержка между запросами
                parse_page(full_url, depth + 1, max_depth)
    
    except Exception as e:
        print(f"Ошибка при парсинге {url}: {e}")

def fix_internal_links():
    """Исправление внутренних ссылок"""
    print("\nИсправление внутренних ссылок...")
    
    for root, dirs, files in os.walk(OUTPUT_DIR):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Заменяем ссылки на dev.1c-bitrix.ru/api_d7/ на локальные
                for url, local_path in url_to_path.items():
                    rel_path = os.path.relpath(local_path, os.path.dirname(file_path))
                    content = content.replace(url, rel_path)
                
                # Удаляем оставшиеся ссылки на dev.1c-bitrix.ru
                content = re.sub(r'\[([^\]]+)\]\(https?://dev\.1c-bitrix\.ru/api_d7/[^\)]*\)', r'\1', content)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)

if __name__ == "__main__":
    print("Начало парсинга API D7...")
    print(f"Стартовый URL: {START_URL}")
    print(f"Директория вывода: {OUTPUT_DIR}\n")
    
    # Парсим документацию
    parse_page(START_URL, max_depth=6)
    
    # Исправляем ссылки
    fix_internal_links()
    
    print(f"\nПарсинг завершен!")
    print(f"Обработано страниц: {len(visited_urls)}")
    print(f"Создано файлов: {len(url_to_path)}")
