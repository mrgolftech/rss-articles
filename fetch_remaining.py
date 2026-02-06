#!/usr/bin/env python3
"""
Fetch remaining RSS feeds
"""
import os
import re
import time
import random
import requests
import feedparser
import html2text

# Configuration
WORK_DIR = "/root/openclaw/gw/docs/rss"
DOCS_DIR = os.path.join(WORK_DIR, "docs")

# Only the missing blogs
MISSING_BLOGS = [
    ("utcc.utoronto.ca/~cks", "https://utcc.utoronto.ca/~cks/space/blog/?atom", "https://utcc.utoronto.ca/~cks"),
    ("geohot.github.io", "https://geohot.github.io/blog/feed.xml", "https://geohot.github.io"),
    ("jyn.dev", "https://jyn.dev/atom.xml", "https://jyn.dev"),
    ("geoffreylitt.com", "https://www.geoffreylitt.com/feed.xml", "https://geoffreylitt.com"),
    ("downtowndougbrown.com", "https://www.downtowndougbrown.com/feed/", "https://www.downtowndougbrown.com"),
    ("brutecat.com", "https://brutecat.com/rss.xml", "https://brutecat.com"),
    ("eli.thegreenplace.net", "https://eli.thegreenplace.net/feeds/all.atom.xml", "https://eli.thegreenplace.net"),
    ("abortretry.fail", "https://www.abortretry.fail/feed", "https://abortretry.fail"),
    ("fabiensanglard.net", "https://fabiensanglard.net/rss.xml", "https://fabiensanglard.net"),
    ("oldvcr.blogspot.com", "https://oldvcr.blogspot.com/feeds/posts/default", "https://oldvcr.blogspot.com"),
    ("bogdanthegeek.github.io", "https://bogdanthegeek.github.io/blog/index.xml", "https://bogdanthegeek.github.io"),
    ("hugotunius.se", "https://hugotunius.se/feed.xml", "https://hugotunius.se"),
    ("gwern.net", "https://gwern.substack.com/feed", "https://gwern.net"),
    ("simone.org", "https://simone.org/feed/", "https://simone.org"),
    ("it-notes.dragas.net", "https://it-notes.dragas.net/feed/", "https://it-notes.dragas.net"),
    ("beej.us", "https://beej.us/blog/rss.xml", "https://beej.us"),
    ("hey.paris", "https://hey.paris/index.xml", "https://hey.paris"),
    ("danielwirtz.com", "https://danielwirtz.com/rss.xml", "https://danielwirtz.com"),
    ("matduggan.com", "https://matduggan.com/rss/", "https://matduggan.com"),
    ("refactoringenglish.com", "https://refactoringenglish.com/index.xml", "https://refactoringenglish.com"),
    ("philiplaine.com", "https://philiplaine.com/index.xml", "https://philiplaine.com"),
    ("bernsteinbear.com", "https://bernsteinbear.com/feed.xml", "https://bernsteinbear.com"),
    ("danieldelaney.net", "https://danieldelaney.net/feed", "https://danieldelaney.net"),
    ("herman.bearblog.dev", "https://herman.bearblog.dev/feed/", "https://herman.bearblog.dev"),
    ("tomrenner.com", "https://tomrenner.com/index.xml", "https://tomrenner.com"),
    ("blog.pixelmelt.dev", "https://blog.pixelmelt.dev/rss/", "https://blog.pixelmelt.dev"),
    ("danielchasehooper.com", "https://danielchasehooper.com/feed.xml", "https://danielchasehooper.com"),
    ("chiark.greenend.org.uk/~sgtatham", "https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/feed.xml", "https://chiark.greenend.org.uk/~sgtatham"),
    ("keygen.sh", "https://keygen.sh/blog/feed.xml", "https://keygen.sh"),
    ("mjg59.dreamwidth.org", "https://mjg59.dreamwidth.org/data/rss", "https://mjg59.dreamwidth.org"),
    ("computer.rip", "https://computer.rip/rss.xml", "https://computer.rip"),
    ("tedunangst.com", "https://www.tedunangst.com/flak/rss", "https://tedunangst.com"),
]

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
    name = re.sub(r'[<>:"/\\|?*]', '-', name)
    name = name.strip('. ')
    if len(name) > 200:
        name = name[:200]
    return name

def extract_date(link):
    """Extract date from link or use current date"""
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
    """Clean RSS content"""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    h.body_width = 0
    
    text = h.handle(content)
    
    if len(text) < 200 and link:
        try:
            print(f"    内容太短，尝试抓取完整内容...")
            headers = {'User-Agent': get_random_user_agent()}
            response = requests.get(link, headers=headers, timeout=10)
            if response.status_code == 200:
                full_text = h.handle(response.text)
                if len(full_text) > len(text):
                    print(f"    ✓ 成功抓取完整内容")
                    return full_text
        except Exception as e:
            print(f"    ✗ 抓取完整内容失败: {e}")
    
    return text

def process_blog(blog_name, rss_url, html_url):
    """Process a single blog"""
    print(f"\n[{blog_name}]")
    
    # Normalize blog name for directory
    dir_name = blog_name.replace('/', '_').replace('~', '_').replace(':', '_')
    blog_dir = os.path.join(DOCS_DIR, dir_name)
    
    # Skip if already exists
    if os.path.exists(blog_dir):
        print(f"  ✓ 已存在，跳过")
        return True
    
    os.makedirs(blog_dir, exist_ok=True)
    
    # Fetch RSS feed
    headers = {'User-Agent': get_random_user_agent()}
    try:
        feed = feedparser.parse(rss_url, request_headers=headers)
    except Exception as e:
        print(f"  ✗ 解析RSS失败: {e}")
        return False
    
    if not feed or not feed.entries:
        print(f"  ✗ 未能获取RSS feed或没有文章")
        return False
    
    print(f"  ✓ 找到 {len(feed.entries)} 篇文章")
    
    # Get blog description
    blog_description = feed.feed.get('description', '')
    if blog_description:
        h = html2text.HTML2Text()
        h.body_width = 0
        blog_description = h.handle(blog_description).split('\n')[0]
    
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
    print(f"开始抓取 {len(MISSING_BLOGS)} 个缺失的博客...")
    print("=" * 60)
    
    success_count = 0
    failed_blogs = []
    
    for i, (blog_name, rss_url, html_url) in enumerate(MISSING_BLOGS):
        print(f"\n[{i+1}/{len(MISSING_BLOGS)}] 处理: {blog_name}")
        
        try:
            success = process_blog(blog_name, rss_url, html_url)
            if success:
                success_count += 1
            else:
                failed_blogs.append(blog_name)
        except Exception as e:
            print(f"  ✗ 处理失败: {e}")
            failed_blogs.append(blog_name)
        
        # Add delay between blogs
        if i < len(MISSING_BLOGS) - 1:
            delay = random.uniform(2, 4)
            print(f"  等待 {delay:.1f} 秒...")
            time.sleep(delay)
    
    print("\n" + "=" * 60)
    print(f"抓取完成！")
    print(f"成功: {success_count}/{len(MISSING_BLOGS)}")
    print(f"失败: {len(failed_blogs)}")
    
    if failed_blogs:
        print(f"\n失败的博客:")
        for blog in failed_blogs:
            print(f"  - {blog}")
    
    print("=" * 60)

if __name__ == "__main__":
    from datetime import datetime
    main()