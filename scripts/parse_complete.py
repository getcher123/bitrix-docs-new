#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Полный парсер документации 1C-Bitrix с глубоким рекурсивным обходом
Собирает ВСЕ страницы документации со всеми уровнями вложенности
"""

import os
import re
import time
import json
import hashlib
from urllib.parse import urljoin, urlparse, unquote, parse_qs
from pathlib import Path
from collections import deque
import requests
from bs4 import BeautifulSoup

class CompleteBitrixParser:
    def __init__(self, base_dir):
        self.base_url = "https://dev.1c-bitrix.ru"
        self.api_help_url = f"{self.base_url}/api_help/"
        self.base_dir = Path(base_dir)
        self.docs_dir = self.base_dir / "docs"
        self.images_dir = self.base_dir / "images"
        
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        self.visited_urls = set()
        self.url_to_file = {}
        self.queue = deque()
        self.max_pages = 500  # Ограничение для безопасности
        
    def sanitize_filename(self, name):
        """Очистить имя файла"""
        name = re.sub(r'[<>:"/\\|?*]', '_', name)
        name = re.sub(r'\s+', '_', name)
        name = name.strip('_.')
        return name[:100] if name else "page"
    
    def url_to_path(self, url):
        """Конвертировать URL в путь к файлу"""
        parsed = urlparse(url)
        path_parts = [p for p in parsed.path.split('/') if p and p != 'api_help']
        
        # Извлечь параметры
        params = parse_qs(parsed.query)
        
        # Создать путь
        if not path_parts:
            return "index"
        
        # Последний элемент - имя файла
        filename = path_parts[-1].replace('.php', '')
        
        # Директории
        dirs = path_parts[:-1] if len(path_parts) > 1 else []
        
        # Добавить параметры для уникальности
        if params:
            param_str = '_'.join([f"{k}_{v[0]}" for k, v in params.items() 
                                 if k not in ['print']])
            if param_str:
                filename = f"{filename}_{param_str}"
        
        return '/'.join(dirs + [filename]) if dirs else filename
    
    def download_image(self, img_url):
        """Скачать изображение"""
        try:
            if not img_url.startswith('http'):
                img_url = urljoin(self.base_url, img_url)
            
            img_hash = hashlib.md5(img_url.encode()).hexdigest()[:10]
            img_ext = os.path.splitext(urlparse(img_url).path)[1] or '.png'
            img_filename = f"{img_hash}{img_ext}"
            img_path = self.images_dir / img_filename
            
            if not img_path.exists():
                response = self.session.get(img_url, timeout=30)
                if response.status_code == 200:
                    img_path.write_bytes(response.content)
            
            return f"../images/{img_filename}"
        except:
            return img_url
    
    def clean_text(self, text):
        """Очистить текст"""
        return re.sub(r'\s+', ' ', text).strip()
    
    def html_to_markdown(self, element, base_url):
        """Конвертировать HTML в Markdown"""
        if element.name is None:
            return str(element).strip()
        
        text = ""
        
        if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(element.name[1])
            content = self.clean_text(element.get_text())
            if content:
                text = f"\n{'#' * level} {content}\n\n"
        
        elif element.name == 'p':
            content = self.process_inline(element, base_url)
            if content:
                text = f"{content}\n\n"
        
        elif element.name == 'a':
            href = element.get('href', '')
            link_text = self.clean_text(element.get_text())
            if href and link_text:
                # НЕ конвертируем ссылки здесь - сделаем это позже
                text = f"[{link_text}]({href})"
            elif link_text:
                text = link_text
        
        elif element.name == 'img':
            src = element.get('src', '')
            alt = element.get('alt', 'image')
            if src:
                local_path = self.download_image(src)
                text = f"![{alt}]({local_path})\n\n"
        
        elif element.name in ['ul', 'ol']:
            text = "\n"
            for i, li in enumerate(element.find_all('li', recursive=False)):
                prefix = f"{i+1}." if element.name == 'ol' else "-"
                content = self.process_inline(li, base_url)
                if content:
                    text += f"{prefix} {content}\n"
            text += "\n"
        
        elif element.name == 'code':
            text = f"`{element.get_text()}`"
        
        elif element.name == 'pre':
            code = element.get_text().strip()
            if code:
                text = f"\n```\n{code}\n```\n\n"
        
        elif element.name == 'table':
            text = self.table_to_markdown(element, base_url)
        
        elif element.name == 'br':
            text = "  \n"
        
        elif element.name in ['strong', 'b']:
            content = self.clean_text(element.get_text())
            if content:
                text = f"**{content}**"
        
        elif element.name in ['em', 'i']:
            content = self.clean_text(element.get_text())
            if content:
                text = f"*{content}*"
        
        elif element.name == 'blockquote':
            lines = element.get_text().strip().split('\n')
            text = "\n".join([f"> {line.strip()}" for line in lines if line.strip()]) + "\n\n"
        
        elif element.name in ['div', 'span', 'section', 'article']:
            text = self.process_children(element, base_url)
        
        else:
            text = self.process_children(element, base_url)
        
        return text
    
    def process_inline(self, element, base_url):
        """Обработать inline элементы"""
        result = ""
        for child in element.children:
            if isinstance(child, str):
                result += str(child)
            else:
                result += self.html_to_markdown(child, base_url)
        return self.clean_text(result)
    
    def process_children(self, element, base_url):
        """Обработать дочерние элементы"""
        result = ""
        for child in element.children:
            if isinstance(child, str):
                text = str(child).strip()
                if text:
                    result += text + " "
            else:
                result += self.html_to_markdown(child, base_url)
        return result
    
    def table_to_markdown(self, table, base_url):
        """Конвертировать таблицу в Markdown"""
        rows = []
        for tr in table.find_all('tr'):
            cells = []
            for td in tr.find_all(['td', 'th']):
                cell_text = self.process_inline(td, base_url).replace('|', '\\|').replace('\n', ' ')
                cells.append(cell_text)
            if cells:
                rows.append(cells)
        
        if not rows:
            return ""
        
        md = "\n"
        if rows:
            max_cols = max(len(row) for row in rows)
            md += "| " + " | ".join(rows[0] + [""] * (max_cols - len(rows[0]))) + " |\n"
            md += "| " + " | ".join(["---"] * max_cols) + " |\n"
            for row in rows[1:]:
                md += "| " + " | ".join(row + [""] * (max_cols - len(row))) + " |\n"
        md += "\n"
        return md
    
    def extract_api_links(self, soup, base_url):
        """Извлечь все ссылки на API документацию"""
        links = set()
        for link in soup.find_all('a'):
            href = link.get('href', '')
            if href and not href.startswith('#'):
                full_url = urljoin(base_url, href)
                # Только ссылки на api_help
                if 'api_help' in full_url and '?print=Y' not in full_url:
                    # Убрать якоря
                    full_url = full_url.split('#')[0]
                    links.add(full_url)
        return links
    
    def parse_page(self, url):
        """Парсить одну страницу"""
        try:
            if url in self.visited_urls:
                return []
            
            self.visited_urls.add(url)
            print(f"[{len(self.visited_urls)}/{self.max_pages}] {url}")
            
            response = self.session.get(url, timeout=30)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Найти контент
            content = soup.find('div', class_='content')
            if not content:
                content = soup.find('article') or soup.find('main') or soup.find('body')
            
            # Заголовок
            title = soup.find('h1')
            title_text = title.get_text().strip() if title else (
                soup.title.get_text().strip() if soup.title else "Документация"
            )
            
            # Конвертировать в Markdown
            markdown = f"# {title_text}\n\n"
            markdown += f"**Источник:** {url}\n\n"
            markdown += "---\n\n"
            
            if content:
                # Удалить лишнее
                for elem in content.find_all(['nav', 'script', 'style', 'noscript']):
                    elem.decompose()
                
                # Конвертировать
                for child in content.children:
                    if child.name:
                        markdown += self.html_to_markdown(child, url)
            
            # Определить путь к файлу
            file_path = self.url_to_path(url)
            safe_path = '/'.join([self.sanitize_filename(p) for p in file_path.split('/')])
            output_file = self.docs_dir / f"{safe_path}.md"
            
            # Сохранить
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(markdown, encoding='utf-8')
            
            # Сохранить маппинг
            self.url_to_file[url] = str(output_file.relative_to(self.docs_dir))
            
            # Извлечь новые ссылки
            new_links = self.extract_api_links(soup, url)
            
            time.sleep(0.2)
            
            return list(new_links)
            
        except Exception as e:
            print(f"  Ошибка: {e}")
            return []
    
    def run(self):
        """Запустить полный парсинг"""
        print("=" * 70)
        print("ПОЛНЫЙ ПАРСИНГ ДОКУМЕНТАЦИИ 1C-BITRIX")
        print("=" * 70)
        
        self.docs_dir.mkdir(parents=True, exist_ok=True)
        self.images_dir.mkdir(parents=True, exist_ok=True)
        
        # Начать с главной страницы
        self.queue.append(self.api_help_url)
        
        # BFS обход всех страниц
        while self.queue and len(self.visited_urls) < self.max_pages:
            url = self.queue.popleft()
            
            if url not in self.visited_urls:
                new_links = self.parse_page(url)
                
                # Добавить новые ссылки в очередь
                for link in new_links:
                    if link not in self.visited_urls:
                        self.queue.append(link)
        
        # Сохранить маппинг
        mapping_file = self.base_dir / "url_mapping.json"
        mapping_file.write_text(
            json.dumps(self.url_to_file, ensure_ascii=False, indent=2),
            encoding='utf-8'
        )
        
        # Метаданные
        metadata = {
            'total_pages': len(self.visited_urls),
            'total_images': len(list(self.images_dir.glob('*'))),
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        (self.base_dir / "metadata.json").write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2),
            encoding='utf-8'
        )
        
        print("\n" + "=" * 70)
        print(f"✓ ПАРСИНГ ЗАВЕРШЕН!")
        print(f"  Страниц: {len(self.visited_urls)}")
        print(f"  Изображений: {len(list(self.images_dir.glob('*')))}")
        print("=" * 70)

if __name__ == "__main__":
    parser = CompleteBitrixParser("/home/ubuntu/bitrix-docs-new")
    parser.run()
