#!/usr/bin/env python3
"""
Fetch RSS feeds from OPML and save articles
"""
import os
import re
import time
import random
import json
import hashlib
from datetime import datetime
from urllib.parse import urlparse, urljoin
import feedparser
import html2text

# Configuration
WORK_DIR = "/root/openclaw/gw/docs/rss"
DOCS_DIR = os.path.join(WORK_DIR, "docs")
OPML_URL = "https://gist.githubusercontent.com/emschwartz/e6d2bf860ccc367fe37ff953ba6de66b/raw/426957f043dc0054f95aae6c19de1d0b4ecc2bb2/hn-popular-blogs-2025.opml"

# User agents for rotation
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
]

def get_random_user_agent():
    """Get a random user agent"""
    return random.choice(USER_AGENTS)

def sanitize_filename(name):
    """Sanitize filename to be filesystem-safe"""
    # Replace invalid characters
    name = re.sub(r'[<>:"/\\|?*]', '-', name)
    # Remove leading/trailing dots and spaces
    name = name.strip('. ')
    # Limit length
    if len(name) > 200:
        name = name[:200]
    return name

def extract_date(link):
    """Extract date from link or use current date"""
    # Try to extract date from URL
    date_patterns = [
        r'/(\d{4})/(\d{2})/(\d{2})/',
        r'/(\d{4})-(\d{2})-(\d{2})/',
        r'/(\d{4})(\d{2})(\d{2})/',
    ]
    
    for pattern in date_patterns:
        match = re.search(pattern, link)
        if match:
            year, month, day = match.groups()
            return f"{year}{month}{day}"
    
    return datetime.now().strftime("%Y%m%d")

def clean_rss_content(content, link):
    """Clean RSS content, removing HTML tags and formatting"""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    h.body_width = 0  # Don't wrap lines
    
    text = h.handle(content)
    
    # Always try to fetch the full page for complete content
    if link:
        try:
            print(f"    正在抓取完整内容...")
            import requests
            headers = {'User-Agent': get_random_user_agent()}
            response = requests.get(link, headers=headers, timeout=15)
            if response.status_code == 200:
                full_text = h.handle(response.text)
                if len(full_text) > len(text):
                    print(f"    ✓ 成功抓取完整内容 ({len(full_text)} 字符)")
                    return full_text
                else:
                    print(f"    ✓ 使用RSS内容 ({len(text)} 字符)")
            else:
                print(f"    ⚠️  无法访问页面，使用RSS内容 ({len(text)} 字符)")
        except Exception as e:
            print(f"    ✗ 抓取完整内容失败: {e}，使用RSS内容")
    
    return text

def fetch_rss_feed(rss_url):
    """Fetch and parse RSS feed"""
    headers = {'User-Agent': get_random_user_agent()}
    
    try:
        feed = feedparser.parse(rss_url, request_headers=headers)
        return feed
    except Exception as e:
        print(f"    ✗ 解析RSS失败: {e}")
        return None

def process_blog(blog_name, rss_url, html_url):
    """Process a single blog and save its articles"""
    print(f"\n[{blog_name}]")
    print(f"  RSS: {rss_url}")
    
    # Create blog directory
    blog_dir = os.path.join(DOCS_DIR, blog_name)
    os.makedirs(blog_dir, exist_ok=True)
    
    # Fetch RSS feed
    feed = fetch_rss_feed(rss_url)
    if not feed or not feed.entries:
        print(f"  ✗ 未能获取RSS feed或没有文章")
        return False
    
    print(f"  ✓ 找到 {len(feed.entries)} 篇文章")
    
    # Get blog description
    blog_description = feed.feed.get('description', '')
    if blog_description:
        blog_description = clean_rss_content(blog_description, '')
        blog_description = blog_description.split('\n')[0]  # Just first line
    
    # Save blog description
    desc_file = os.path.join(blog_dir, "description.txt")
    with open(desc_file, 'w', encoding='utf-8') as f:
        f.write(blog_description)
    
    # Save up to 5 most recent articles
    saved_count = 0
    article_list = []
    
    for i, entry in enumerate(feed.entries[:5]):
        title = entry.get('title', 'Untitled')
        link = entry.get('link', '')
        published = entry.get('published', '')
        content = entry.get('content', [{}])[0].get('value', '') if entry.get('content') else entry.get('description', '')
        
        if not content:
            content = entry.get('summary', '')
        
        print(f"  [{i+1}/5] {title[:50]}...")
        
        # Clean content
        clean_content = clean_rss_content(content, link)
        
        # Generate filename
        date_str = extract_date(link)
        safe_title = sanitize_filename(title)
        filename = f"{safe_title}_{date_str}.md"
        filepath = os.path.join(blog_dir, filename)
        
        # Write article
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            f.write(f"**来源:** {html_url}\n")
            f.write(f"**链接:** {link}\n")
            f.write(f"**日期:** {published}\n\n")
            f.write("---\n\n")
            f.write(clean_content)
        
        article_list.append(filename)
        print(f"      ✓ 保存: {filename}")
        saved_count += 1
        
        # Add delay between articles
        time.sleep(random.uniform(1, 2))
    
    # Update or create index.md
    index_file = os.path.join(blog_dir, "index.md")
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(f"# {blog_name}\n\n")
        if blog_description:
            f.write(f"{blog_description}\n\n")
        f.write(f"**网站:** {html_url}\n")
        f.write(f"**RSS:** {rss_url}\n\n")
        f.write("---\n\n")
        f.write("## 最新文章\n\n")
        for article in article_list:
            f.write(f"- [{article.replace('.md', '')}]({article})\n")
    
    print(f"  ✓ 已更新 index.md ({saved_count} 篇文章)")
    return True

def main():
    """Main function"""
    print("=" * 60)
    print("开始抓取缺失的博客...")
    print("=" * 60)
    
    # Fetch OPML
    import requests
    headers = {'User-Agent': get_random_user_agent()}
    response = requests.get(OPML_URL, headers=headers)
    opml_content = response.text
    
    # Parse OPML to extract blogs
    blog_list = []
    
    # Find all outline elements
    pattern = r'<outline[^>]*type="rss"[^>]*text="([^"]+)"[^>]*xmlUrl="([^"]+)"[^>]*htmlUrl="([^"]+)"[^>]*?>'
    matches = re.findall(pattern, opml_content)
    
    for blog_name, rss_url, html_url in matches:
        blog_list.append({
            'name': blog_name,
            'rss_url': rss_url,
            'html_url': html_url
        })
    
    print(f"\n从OPML中找到 {len(blog_list)} 个博客\n")
    
    # Get existing blogs
    existing_blogs = set()
    for item in os.listdir(DOCS_DIR):
        item_path = os.path.join(DOCS_DIR, item)
        if os.path.isdir(item_path) and item not in ['blogs.md', 'index.md']:
            existing_blogs.add(item)
    
    print(f"已存在的博客: {len(existing_blogs)}\n")
    
    # Filter to only missing blogs
    missing_blogs = []
    for blog in blog_list:
        if blog['name'] not in existing_blogs:
            missing_blogs.append(blog)
    
    print(f"需要抓取的博客: {len(missing_blogs)}\n")
    print("=" * 60)
    
    # Process each missing blog
    success_count = 0
    failed_blogs = []
    
    for i, blog in enumerate(missing_blogs):
        print(f"\n[{i+1}/{len(missing_blogs)}] 处理: {blog['name']}")
        
        try:
            success = process_blog(blog['name'], blog['rss_url'], blog['html_url'])
            if success:
                success_count += 1
            else:
                failed_blogs.append(blog['name'])
        except Exception as e:
            print(f"  ✗ 处理失败: {e}")
            failed_blogs.append(blog['name'])
        
        # Add delay between blogs
        if i < len(missing_blogs) - 1:
            delay = random.uniform(2, 4)
            print(f"  等待 {delay:.1f} 秒...")
            time.sleep(delay)
    
    print("\n" + "=" * 60)
    print(f"抓取完成！")
    print(f"成功: {success_count}/{len(missing_blogs)}")
    print(f"失败: {len(failed_blogs)}")
    
    if failed_blogs:
        print(f"\n失败的博客:")
        for blog in failed_blogs:
            print(f"  - {blog}")
    
    print("=" * 60)

if __name__ == "__main__":
    main()