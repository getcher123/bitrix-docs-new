#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Парсер документации 1C-Bitrix
Скачивает документацию с dev.1c-bitrix.ru и конвертирует в Markdown
"""

import os
import re
import time
import json
import hashlib
from urllib.parse import urljoin, urlparse, unquote
from pathlib import Path
import requests
from bs4 import BeautifulSoup

class BitrixDocsParser:
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
        self.modules = []
        
    def sanitize_filename(self, name):
        """Очистить имя файла от недопустимых символов"""
        name = re.sub(r'[<>:"/\\|?*]', '_', name)
        name = re.sub(r'\s+', '_', name)
        return name.strip('_')
    
    def download_image(self, img_url):
        """Скачать изображение и вернуть локальный путь"""
        try:
            if not img_url.startswith('http'):
                img_url = urljoin(self.base_url, img_url)
            
            # Создать имя файла на основе URL
            img_hash = hashlib.md5(img_url.encode()).hexdigest()[:10]
            img_ext = os.path.splitext(urlparse(img_url).path)[1] or '.png'
            img_filename = f"{img_hash}{img_ext}"
            img_path = self.images_dir / img_filename
            
            if not img_path.exists():
                response = self.session.get(img_url, timeout=30)
                if response.status_code == 200:
                    img_path.write_bytes(response.content)
                    print(f"  Скачано изображение: {img_filename}")
            
            return f"../images/{img_filename}"
        except Exception as e:
            print(f"  Ошибка скачивания изображения {img_url}: {e}")
            return img_url
    
    def html_to_markdown(self, element, base_url):
        """Конвертировать HTML элемент в Markdown"""
        if element.name is None:
            return str(element).strip()
        
        text = ""
        
        # Обработка различных тегов
        if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(element.name[1])
            text = f"\n{'#' * level} {element.get_text().strip()}\n\n"
        
        elif element.name == 'p':
            text = f"{self.process_inline(element, base_url)}\n\n"
        
        elif element.name == 'a':
            href = element.get('href', '')
            link_text = element.get_text().strip()
            if href:
                # Конвертировать внутренние ссылки
                if href.startswith(self.base_url) or href.startswith('/'):
                    href = self.convert_internal_link(href)
                text = f"[{link_text}]({href})"
            else:
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
                text += f"{prefix} {self.process_inline(li, base_url)}\n"
            text += "\n"
        
        elif element.name == 'code':
            text = f"`{element.get_text()}`"
        
        elif element.name == 'pre':
            code = element.get_text().strip()
            text = f"\n```\n{code}\n```\n\n"
        
        elif element.name == 'table':
            text = self.table_to_markdown(element, base_url)
        
        elif element.name == 'br':
            text = "\n"
        
        elif element.name in ['strong', 'b']:
            text = f"**{element.get_text().strip()}**"
        
        elif element.name in ['em', 'i']:
            text = f"*{element.get_text().strip()}*"
        
        elif element.name == 'blockquote':
            lines = element.get_text().strip().split('\n')
            text = "\n".join([f"> {line}" for line in lines]) + "\n\n"
        
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
                result += child
            else:
                result += self.html_to_markdown(child, base_url)
        return result.strip()
    
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
        """Конвертировать HTML таблицу в Markdown"""
        rows = []
        for tr in table.find_all('tr'):
            cells = []
            for td in tr.find_all(['td', 'th']):
                cell_text = self.process_inline(td, base_url).replace('|', '\\|')
                cells.append(cell_text)
            if cells:
                rows.append(cells)
        
        if not rows:
            return ""
        
        # Создать Markdown таблицу
        md = "\n"
        # Заголовок
        if rows:
            md += "| " + " | ".join(rows[0]) + " |\n"
            md += "| " + " | ".join(["---"] * len(rows[0])) + " |\n"
            # Остальные строки
            for row in rows[1:]:
                # Дополнить строку если не хватает ячеек
                while len(row) < len(rows[0]):
                    row.append("")
                md += "| " + " | ".join(row) + " |\n"
        md += "\n"
        return md
    
    def convert_internal_link(self, url):
        """Конвертировать внутреннюю ссылку в относительную"""
        if url in self.url_to_file:
            return self.url_to_file[url]
        return url
    
    def parse_page(self, url, output_file):
        """Парсить одну страницу документации"""
        try:
            if url in self.visited_urls:
                return
            
            self.visited_urls.add(url)
            print(f"Парсинг: {url}")
            
            response = self.session.get(url, timeout=30)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Найти основной контент
            content = soup.find('div', class_='content') or soup.find('article') or soup.find('main')
            if not content:
                content = soup.find('body')
            
            # Получить заголовок
            title = soup.find('h1')
            if title:
                title_text = title.get_text().strip()
            else:
                title_text = soup.title.get_text().strip() if soup.title else "Документация"
            
            # Конвертировать в Markdown
            markdown = f"# {title_text}\n\n"
            markdown += f"**Источник:** {url}\n\n---\n\n"
            
            if content:
                # Удалить навигацию и лишние элементы
                for elem in content.find_all(['nav', 'script', 'style']):
                    elem.decompose()
                
                # Обработать контент
                for child in content.children:
                    if child.name:
                        markdown += self.html_to_markdown(child, url)
            
            # Сохранить в файл
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(markdown, encoding='utf-8')
            print(f"  Сохранено: {output_file}")
            
            time.sleep(0.5)  # Пауза между запросами
            
        except Exception as e:
            print(f"Ошибка парсинга {url}: {e}")
    
    def get_module_links(self):
        """Получить список всех модулей из главной страницы API"""
        try:
            response = self.session.get(self.api_help_url, timeout=30)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')
            
            modules = []
            # Найти все ссылки на модули в боковой панели
            for link in soup.find_all('a'):
                href = link.get('href', '')
                text = link.get_text().strip()
                
                if href and text and not href.startswith('#'):
                    full_url = urljoin(self.api_help_url, href)
                    if 'api_help' in full_url and full_url not in [self.api_help_url]:
                        modules.append({
                            'name': text,
                            'url': full_url
                        })
            
            return modules
        except Exception as e:
            print(f"Ошибка получения списка модулей: {e}")
            return []
    
    def parse_module(self, module_name, module_url):
        """Парсить модуль документации"""
        print(f"\n=== Модуль: {module_name} ===")
        
        # Создать директорию для модуля
        safe_name = self.sanitize_filename(module_name)
        module_dir = self.docs_dir / safe_name
        module_dir.mkdir(parents=True, exist_ok=True)
        
        # Парсить главную страницу модуля
        output_file = module_dir / "index.md"
        self.url_to_file[module_url] = f"./{safe_name}/index.md"
        self.parse_page(module_url, output_file)
        
        return safe_name
    
    def run(self):
        """Запустить парсинг всей документации"""
        print("Начало парсинга документации 1C-Bitrix...")
        
        # Создать директории
        self.docs_dir.mkdir(parents=True, exist_ok=True)
        self.images_dir.mkdir(parents=True, exist_ok=True)
        
        # Парсить главную страницу
        print("\n=== Главная страница ===")
        main_page = self.docs_dir / "index.md"
        self.parse_page(self.api_help_url, main_page)
        
        # Получить список модулей
        print("\nПолучение списка модулей...")
        modules = self.get_module_links()
        print(f"Найдено модулей: {len(modules)}")
        
        # Парсить каждый модуль
        parsed_modules = []
        for i, module in enumerate(modules[:10], 1):  # Начнем с первых 10 модулей
            try:
                safe_name = self.parse_module(module['name'], module['url'])
                parsed_modules.append({
                    'name': module['name'],
                    'dir': safe_name
                })
            except Exception as e:
                print(f"Ошибка парсинга модуля {module['name']}: {e}")
        
        # Сохранить метаданные
        metadata = {
            'modules': parsed_modules,
            'total_pages': len(self.visited_urls)
        }
        
        metadata_file = self.base_dir / "metadata.json"
        metadata_file.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding='utf-8')
        
        print(f"\n✓ Парсинг завершен!")
        print(f"  Обработано страниц: {len(self.visited_urls)}")
        print(f"  Модулей: {len(parsed_modules)}")

if __name__ == "__main__":
    parser = BitrixDocsParser("/home/ubuntu/bitrix-docs-storage")
    parser.run()
