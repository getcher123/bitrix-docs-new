#!/usr/bin/env python3
"""
Парсер Bitrix24 REST API документации
"""

import requests
from bs4 import BeautifulSoup
import os
import time
import re
from urllib.parse import urljoin, urlparse
import json

BASE_URL = "https://apidocs.bitrix24.ru"
START_URL = "https://apidocs.bitrix24.ru/"
OUTPUT_DIR = "/home/ubuntu/bitrix-docs-new/docs/bitrix24_api"
IMAGES_DIR = "/home/ubuntu/bitrix-docs-new/images/bitrix24_api"

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

visited_urls = set()
url_to_path = {}

def clean_filename(name):
    name = re.sub(r'[<>:"/\\|?*]', '_', name)
    name = re.sub(r'\s+', '_', name)
    name = name.strip('._')
    return name[:200]

def download_image(img_url, base_path):
    try:
        if not img_url.startswith('http'):
            img_url = urljoin(BASE_URL, img_url)
        
        # Пропускаем SVG и data: URL
        if 'data:' in img_url or img_url.endswith('.svg'):
            return None
        
        response = requests.get(img_url, timeout=30)
        if response.status_code == 200:
            img_name = os.path.basename(urlparse(img_url).path)
            if not img_name:
                img_name = f"image_{hash(img_url)}.png"
            
            img_path = os.path.join(IMAGES_DIR, clean_filename(img_name))
            
            with open(img_path, 'wb') as f:
                f.write(response.content)
            
            return os.path.relpath(img_path, base_path)
    except Exception as e:
        print(f"Ошибка загрузки изображения {img_url}: {e}")
    
    return None

def clean_content(soup):
    # Удаляем навигацию, футеры
    for elem in soup.find_all(['nav', 'header', 'footer']):
        elem.decompose()
    
    for elem in soup.find_all(class_=re.compile(r'(nav|menu|breadcrumb|sidebar|footer|header|banner)', re.I)):
        elem.decompose()
    
    for elem in soup.find_all(['script', 'style', 'noscript']):
        elem.decompose()
    
    # Удаляем кнопки и интерактивные элементы
    for elem in soup.find_all('button'):
        elem.decompose()
    
    return soup

def html_to_markdown(html_content, base_path):
    soup = BeautifulSoup(html_content, 'html.parser')
    soup = clean_content(soup)
    
    markdown_lines = []
    
    def process_element(elem, level=0):
        if elem.name is None:
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
            if href and text and not href.startswith('#'):
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
                lang = code.get('class', [''])[0].replace('language-', '')
                return f'```{lang}\n{code.get_text()}\n```'
            return f'```\n{elem.get_text()}\n```'
        
        elif elem.name in ['strong', 'b']:
            return f'**{elem.get_text().strip()}**'
        
        elif elem.name in ['em', 'i']:
            return f'*{elem.get_text().strip()}*'
        
        elif elem.name == 'table':
            rows = []
            for tr in elem.find_all('tr'):
                cells = [td.get_text().strip() for td in tr.find_all(['td', 'th'])]
                if cells:
                    rows.append('| ' + ' | '.join(cells) + ' |')
            if len(rows) > 1:
                header_sep = '| ' + ' | '.join(['---'] * len(rows[0].split('|')[1:-1])) + ' |'
                rows.insert(1, header_sep)
            return '\n'.join(rows)
        
        elif elem.name == 'br':
            return '\n'
        
        elif elem.name in ['div', 'section', 'article', 'main']:
            content = []
            for child in elem.children:
                result = process_element(child, level)
                if result:
                    content.append(result)
            return '\n\n'.join(content)
        
        else:
            return elem.get_text().strip()
    
    for child in soup.children:
        result = process_element(child)
        if result:
            markdown_lines.append(result)
    
    markdown = '\n\n'.join(markdown_lines)
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)
    
    return markdown

def parse_page(url, depth=0, max_depth=4):
    if depth > max_depth or url in visited_urls:
        return
    
    # Парсим только apidocs.bitrix24.ru
    if not url.startswith(BASE_URL):
        return
    
    # Пропускаем якоря
    url = url.split('#')[0]
    
    if url in visited_urls:
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
        url_path = urlparse(url).path.strip('/')
        
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
        
        url_to_path[url] = file_path
        
        # Извлекаем основной контент
        content_div = soup.find('main') or soup.find('article')
        if not content_div:
            content_div = soup.find('div', class_=re.compile(r'content|main|article', re.I))
        if not content_div:
            content_div = soup.body
        
        if content_div:
            markdown = html_to_markdown(str(content_div), os.path.dirname(file_path))
            full_content = f"# {title_text}\n\n{markdown}"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(full_content)
            
            print(f"{'  ' * depth}Сохранено: {file_path}")
        
        # Находим все ссылки
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(url, href)
            
            if full_url.startswith(BASE_URL) and full_url not in visited_urls:
                time.sleep(0.3)
                parse_page(full_url, depth + 1, max_depth)
    
    except Exception as e:
        print(f"Ошибка при парсинге {url}: {e}")

def fix_internal_links():
    print("\nИсправление внутренних ссылок...")
    
    for root, dirs, files in os.walk(OUTPUT_DIR):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                for url, local_path in url_to_path.items():
                    rel_path = os.path.relpath(local_path, os.path.dirname(file_path))
                    content = content.replace(url, rel_path)
                
                # Удаляем оставшиеся внешние ссылки на apidocs.bitrix24.ru
                content = re.sub(r'\[([^\]]+)\]\(https?://apidocs\.bitrix24\.ru/[^\)]*\)', r'\1', content)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)

if __name__ == "__main__":
    print("Начало парсинга Bitrix24 REST API...")
    print(f"Стартовый URL: {START_URL}")
    print(f"Директория вывода: {OUTPUT_DIR}\n")
    
    parse_page(START_URL, max_depth=5)
    fix_internal_links()
    
    print(f"\nПарсинг завершен!")
    print(f"Обработано страниц: {len(visited_urls)}")
    print(f"Создано файлов: {len(url_to_path)}")
