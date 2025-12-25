#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Полный парсер документации 1C-Bitrix с рекурсивным обходом
"""

import os
import re
import time
import json
import hashlib
from urllib.parse import urljoin, urlparse, unquote, parse_qs
from pathlib import Path
import requests
from bs4 import BeautifulSoup

class BitrixDocsFullParser:
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
        self.modules_structure = {}
        self.max_depth = 3  # Максимальная глубина рекурсии
        
    def sanitize_filename(self, name):
        """Очистить имя файла от недопустимых символов"""
        name = re.sub(r'[<>:"/\\|?*]', '_', name)
        name = re.sub(r'\s+', '_', name)
        name = name.strip('_.')
        if not name:
            name = "page"
        return name[:100]  # Ограничить длину
    
    def url_to_filename(self, url):
        """Конвертировать URL в имя файла"""
        parsed = urlparse(url)
        path = parsed.path.strip('/')
        
        # Извлечь параметры
        params = parse_qs(parsed.query)
        
        # Создать имя на основе пути
        if path.endswith('.php'):
            name = path.split('/')[-1].replace('.php', '')
        else:
            name = path.split('/')[-1] or 'index'
        
        # Добавить параметры для уникальности
        if params:
            param_str = '_'.join([f"{k}_{v[0]}" for k, v in params.items() if k not in ['print']])
            if param_str:
                name = f"{name}_{param_str}"
        
        return self.sanitize_filename(name)
    
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
            
            return f"../images/{img_filename}"
        except Exception as e:
            return img_url
    
    def clean_text(self, text):
        """Очистить текст от лишних пробелов"""
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    def html_to_markdown(self, element, base_url):
        """Конвертировать HTML элемент в Markdown"""
        if element.name is None:
            text = str(element).strip()
            return text if text else ""
        
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
                if href.startswith(self.base_url) or href.startswith('/'):
                    href = self.convert_internal_link(href)
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
        """Конвертировать HTML таблицу в Markdown"""
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
    
    def convert_internal_link(self, url):
        """Конвертировать внутреннюю ссылку в относительную"""
        # Удалить параметр print
        if '?print=Y' in url or '&print=Y' in url:
            url = url.replace('?print=Y', '').replace('&print=Y', '')
        
        if url in self.url_to_file:
            return self.url_to_file[url]
        
        # Если ссылка на api_help, попробовать создать относительную ссылку
        if 'api_help' in url:
            return url.replace(self.base_url, '')
        
        return url
    
    def extract_links(self, soup, base_url):
        """Извлечь все ссылки на документацию со страницы"""
        links = []
        for link in soup.find_all('a'):
            href = link.get('href', '')
            if href and not href.startswith('#'):
                full_url = urljoin(base_url, href)
                # Фильтровать только ссылки на документацию
                if 'api_help' in full_url and '?print=Y' not in full_url:
                    links.append(full_url)
        return list(set(links))
    
    def parse_page(self, url, output_file, depth=0):
        """Парсить одну страницу документации"""
        try:
            if url in self.visited_urls or depth > self.max_depth:
                return []
            
            self.visited_urls.add(url)
            print(f"{'  ' * depth}[{len(self.visited_urls)}] {url}")
            
            response = self.session.get(url, timeout=30)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Найти основной контент
            content = soup.find('div', class_='content')
            if not content:
                content = soup.find('article') or soup.find('main') or soup.find('body')
            
            # Получить заголовок
            title = soup.find('h1')
            title_text = title.get_text().strip() if title else (soup.title.get_text().strip() if soup.title else "Документация")
            
            # Конвертировать в Markdown
            markdown = f"# {title_text}\n\n"
            markdown += f"**Источник:** {url}\n\n"
            markdown += "---\n\n"
            
            if content:
                # Удалить навигацию и лишние элементы
                for elem in content.find_all(['nav', 'script', 'style', 'noscript']):
                    elem.decompose()
                
                # Обработать контент
                for child in content.children:
                    if child.name:
                        markdown += self.html_to_markdown(child, url)
            
            # Сохранить в файл
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(markdown, encoding='utf-8')
            
            # Извлечь ссылки для дальнейшего парсинга
            links = self.extract_links(soup, url)
            
            time.sleep(0.3)
            
            return links
            
        except Exception as e:
            print(f"{'  ' * depth}Ошибка: {e}")
            return []
    
    def parse_module_recursive(self, module_name, module_url, depth=0):
        """Рекурсивно парсить модуль и все его подстраницы"""
        if depth > self.max_depth:
            return
        
        safe_name = self.sanitize_filename(module_name)
        module_dir = self.docs_dir / safe_name
        module_dir.mkdir(parents=True, exist_ok=True)
        
        # Парсить главную страницу
        output_file = module_dir / "index.md"
        self.url_to_file[module_url] = f"./{safe_name}/index.md"
        
        links = self.parse_page(module_url, output_file, depth)
        
        # Парсить подстраницы
        for link in links[:20]:  # Ограничить количество подстраниц
            if link not in self.visited_urls:
                filename = self.url_to_filename(link)
                sub_file = module_dir / f"{filename}.md"
                self.url_to_file[link] = f"./{safe_name}/{filename}.md"
                self.parse_page(link, sub_file, depth + 1)
    
    def run(self):
        """Запустить полный парсинг документации"""
        print("=" * 60)
        print("Полный парсинг документации 1C-Bitrix")
        print("=" * 60)
        
        self.docs_dir.mkdir(parents=True, exist_ok=True)
        self.images_dir.mkdir(parents=True, exist_ok=True)
        
        # Парсить главную страницу
        print("\n[ГЛАВНАЯ СТРАНИЦА]")
        main_page = self.docs_dir / "index.md"
        self.parse_page(self.api_help_url, main_page)
        
        # Список основных модулей
        modules = [
            ("Основные сведения", f"{self.api_help_url}index.php"),
            ("Главный модуль", f"{self.api_help_url}main/index.php"),
            ("Информационные блоки", f"{self.api_help_url}iblock/index.php"),
            ("Интернет-магазин", f"{self.api_help_url}sale/index.php"),
            ("CRM", f"{self.api_help_url}crm/index.php"),
            ("Бизнес-процессы", f"{self.api_help_url}bizproc/index.php"),
            ("Веб-формы", f"{self.api_help_url}form/index.php"),
            ("Управление структурой", f"{self.api_help_url}fileman/index.php"),
            ("Торговый каталог", f"{self.api_help_url}catalog/index.php"),
            ("Highload-блоки", f"{self.api_help_url}hlblock/index.php"),
        ]
        
        for i, (name, url) in enumerate(modules, 1):
            print(f"\n[МОДУЛЬ {i}/{len(modules)}] {name}")
            print("-" * 60)
            try:
                self.parse_module_recursive(name, url, depth=0)
            except Exception as e:
                print(f"Ошибка модуля {name}: {e}")
        
        # Сохранить метаданные
        metadata = {
            'total_pages': len(self.visited_urls),
            'modules': list(self.modules_structure.keys()),
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        (self.base_dir / "metadata.json").write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2), 
            encoding='utf-8'
        )
        
        print("\n" + "=" * 60)
        print(f"✓ Парсинг завершен!")
        print(f"  Всего страниц: {len(self.visited_urls)}")
        print(f"  Изображений: {len(list(self.images_dir.glob('*')))}")
        print("=" * 60)

if __name__ == "__main__":
    parser = BitrixDocsFullParser("/home/ubuntu/bitrix-docs-storage")
    parser.run()
