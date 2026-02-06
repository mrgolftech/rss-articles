#!/usr/bin/env python3
"""
重新抓取所有博客的完整内容
"""
import os
import re
import time
import random
import json
from datetime import datetime
import feedparser
import html2text
import requests

# Configuration
WORK_DIR = "/root/openclaw/gw/docs/rss"
DOCS_DIR = os.path.join(WORK_DIR, "docs")

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

def fetch_full_content(link):
    """Fetch full article content from link"""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    h.body_width = 0
    
    try:
        print(f"    正在抓取完整内容...")
        headers = {'User-Agent': get_random_user_agent()}
        response = requests.get(link, headers=headers, timeout=15)
        
        if response.status_code == 200:
            # Remove script and style tags
            import re
            clean_html = re.sub(r'<script[^>]*>.*?</script>', '', response.text, flags=re.DOTALL | re.IGNORECASE)
            clean_html = re.sub(r'<style[^>]*>.*?</style>', '', clean_html, flags=re.DOTALL | re.IGNORECASE)
            
            full_text = h.handle(clean_html)
            print(f"    ✓ 成功抓取完整内容 ({len(full_text)} 字符)")
            return full_text
        else:
            print(f"    ⚠️  HTTP {response.status_code}，无法抓取完整内容")
            return None
    except Exception as e:
        print(f"    ✗ 抓取完整内容失败: {e}")
        return None

def process_blog(blog_name, rss_url, html_url):
    """Process a single blog and fetch full content"""
    print(f"\n[{blog_name}]")
    print(f"  RSS: {rss_url}")
    
    blog_dir = os.path.join(DOCS_DIR, blog_name)
    
    if not os.path.exists(blog_dir):
        print(f"  ⚠️  博客目录不存在，跳过")
        return False
    
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
    
    # Process up to 5 most recent articles
    updated_count = 0
    article_list = []
    
    for i, entry in enumerate(feed.entries[:5]):
        title = entry.get('title', 'Untitled')
        link = entry.get('link', '')
        published = entry.get('published', '')
        
        print(f"  [{i+1}/5] {title[:50]}...")
        
        # Generate filename
        date_str = extract_date(link)
        safe_title = sanitize_filename(title)
        filename = f"{safe_title}_{date_str}.md"
        filepath = os.path.join(blog_dir, filename)
        
        # Check if article already exists
        if os.path.exists(filepath):
            print(f"      ⊙ 已存在，跳过: {filename}")
            article_list.append(filename)
            continue
        
        # Fetch full content
        full_content = fetch_full_content(link)
        
        if not full_content:
            print(f"      ✗ 无法获取完整内容，跳过")
            continue
        
        # Write article with full content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            f.write(f"**来源:** {html_url}\n")
            f.write(f"**链接:** {link}\n")
            f.write(f"**日期:** {published}\n\n")
            f.write("---\n\n")
            f.write(full_content)
        
        article_list.append(filename)
        print(f"      ✓ 新增: {filename} ({len(full_content)} 字符)")
        updated_count += 1
        
        # Add delay between articles
        time.sleep(random.uniform(1, 2))
    
    # Update index.md
    if article_list:
        index_file = os.path.join(blog_dir, "index.md")
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(f"# {blog_name}\n\n")
            f.write(f"**网站:** {html_url}\n")
            f.write(f"**RSS:** {rss_url}\n\n")
            f.write("---\n\n")
            f.write("## 最新文章\n\n")
            for article in article_list:
                f.write(f"- [{article.replace('.md', '')}]({article})\n")
        
        print(f"  ✓ 已更新 index.md ({updated_count} 篇文章)")
    
    return updated_count > 0

def main():
    """Main function"""
    print("=" * 60)
    print("重新抓取所有博客的完整内容...")
    print("=" * 60)
    
    # Get all blog directories
    blogs = []
    for item in os.listdir(DOCS_DIR):
        item_path = os.path.join(DOCS_DIR, item)
        if os.path.isdir(item_path) and item not in ['blogs.md', 'index.md']:
            blogs.append(item)
    
    print(f"\n找到 {len(blogs)} 个博客目录\n")
    print("=" * 60)
    
    # Blog RSS mappings (from OPML)
    blog_rss_map = {
        'simonwillison.net': 'https://simonwillison.net/atom/everything/',
        'jeffgeerling.com': 'https://www.jeffgeerling.com/blog.xml',
        'seangoedecke.com': 'https://www.seangoedecke.com/rss.xml',
        'krebsonsecurity.com': 'https://krebsonsecurity.com/feed/',
        'daringfireball.net': 'https://daringfireball.net/feeds/main',
        'ericmigi.com': 'https://ericmigi.com/rss.xml',
        'antirez.com': 'http://antirez.com/rss',
        'idiallo.com': 'https://idiallo.com/feed.rss',
        'maurycyz.com': 'https://maurycyz.com/index.xml',
        'pluralistic.net': 'https://pluralistic.net/feed/',
        'shkspr.mobi': 'https://shkspr.mobi/blog/feed/',
        'lcamtuf.substack.com': 'https://lcamtuf.substack.com/feed',
        'mitchellh.com': 'https://mitchellh.com/feed.xml',
        'dynomight.net': 'https://dynomight.net/feed.xml',
        'devblogs.microsoft.com/oldnewthing': 'https://devblogs.microsoft.com/oldnewthing/feed',
        'righto.com': 'https://www.righto.com/feeds/posts/default',
        'lucumr.pocoo.org': 'https://lucumr.pocoo.org/feed.atom',
        'skyfall.dev': 'https://skyfall.dev/rss.xml',
        'garymarcus.substack.com': 'https://garymarcus.substack.com/feed',
        'rachelbythebay.com': 'https://rachelbythebay.com/w/atom.xml',
        'overreacted.io': 'https://overreacted.io/rss.xml',
        'timsh.org': 'https://timsh.org/rss/',
        'johndcook.com': 'https://www.johndcook.com/blog/feed/',
        'gilesthomas.com': 'https://gilesthomas.com/feed/rss.xml',
        'matklad.github.io': 'https://matklad.github.io/feed.xml',
        'derekthompson.org': 'https://www.theatlantic.com/feed/author/derek-thompson/',
        'evanhahn.com': 'https://evanhahn.com/feed.xml',
        'terriblesoftware.org': 'https://terriblesoftware.org/feed/',
        'rakhim.exotext.com': 'https://rakhim.exotext.com/rss.xml',
        'joanwestenberg.com': 'https://joanwestenberg.com/rss',
        'xania.org': 'https://xania.org/feed',
        'micahflee.com': 'https://micahflee.com/feed/',
        'nesbitt.io': 'https://nesbitt.io/feed.xml',
        'construction-physics.com': 'https://www.construction-physics.com/feed',
        'tedium.co': 'https://feed.tedium.co/',
        'susam.net': 'https://susam.net/feed.xml',
        'entropicthoughts.com': 'https://entropicthoughts.com/feed.xml',
        'buttondown.com/hillelwayne': 'https://buttondown.com/hillelwayne/rss',
        'dwarkesh.com': 'https://www.dwarkeshpatel.com/feed',
        'borretti.me': 'https://borretti.me/feed.xml',
        'wheresyoured.at': 'https://www.wheresyoured.at/rss/',
        'jayd.ml': 'https://jayd.ml/feed.xml',
        'minimaxir.com': 'https://minimaxir.com/index.xml',
        'geohot.github.io': 'https://geohot.github.io/blog/feed.xml',
        'paulgraham.com': 'http://www.aaronsw.com/2002/feeds/pgessays.rss',
        'filfre.net': 'https://www.filfre.net/feed/',
        'blog.jim-nielsen.com': 'https://blog.jim-nielsen.com/feed.xml',
        'dfarq.homeip.net': 'https://dfarq.homeip.net/feed/',
        'jyn.dev': 'https://jyn.dev/atom.xml',
        'geoffreylitt.com': 'https://www.geoffreylitt.com/feed.xml',
        'downtowndougbrown.com': 'https://www.downtowndougbrown.com/feed/',
        'brutecat.com': 'https://brutecat.com/rss.xml',
        'eli.thegreenplace.net': 'https://eli.thegreenplace.net/feeds/all.atom.xml',
        'abortretry.fail': 'https://www.abortretry.fail/feed',
        'fabiensanglard.net': 'https://fabiensanglard.net/rss.xml',
        'oldvcr.blogspot.com': 'https://oldvcr.blogspot.com/feeds/posts/default',
        'bogdanthegeek.github.io': 'https://bogdanthegeek.github.io/blog/index.xml',
        'hugotunius.se': 'https://hugotunius.se/feed.xml',
        'gwern.net': 'https://gwern.substack.com/feed',
        'berthub.eu': 'https://berthub.eu/articles/index.xml',
        'chadnauseam.com': 'https://chadnauseam.com/rss.xml',
        'simone.org': 'https://simone.org/feed/',
        'it-notes.dragas.net': 'https://it-notes.dragas.net/feed/',
        'beej.us': 'https://beej.us/blog/rss.xml',
        'hey.paris': 'https://hey.paris/index.xml',
        'danielwirtz.com': 'https://danielwirtz.com/rss.xml',
        'matduggan.com': 'https://matduggan.com/rss/',
        'refactoringenglish.com': 'https://refactoringenglish.com/index.xml',
        'worksonmymachine.substack.com': 'https://worksonmymachine.substack.com/feed',
        'philiplaine.com': 'https://philiplaine.com/index.xml',
        'steveblank.com': 'https://steveblank.com/feed/',
        'bernsteinbear.com': 'https://bernsteinbear.com/feed.xml',
        'danieldelaney.net': 'https://danieldelaney.net/feed',
        'troyhunt.com': 'https://www.troyhunt.com/rss/',
        'herman.bearblog.dev': 'https://herman.bearblog.dev/feed/',
        'tomrenner.com': 'https://tomrenner.com/index.xml',
        'blog.pixelmelt.dev': 'https://blog.pixelmelt.dev/rss/',
        'martinalderson.com': 'https://martinalderson.com/feed.xml',
        'danielchasehooper.com': 'https://danielchasehooper.com/feed.xml',
        'chiark.greenend.org.uk/~sgtatham': 'https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/feed.xml',
        'grantslatton.com': 'https://grantslatton.com/rss.xml',
        'experimental-history.com': 'https://www.experimental-history.com/feed',
        'anildash.com': 'https://anildash.com/feed.xml',
        'aresluna.org': 'https://aresluna.org/main.rss',
        'michael.stapelberg.ch': 'https://michael.stapelberg.ch/feed.xml',
        'miguelgrinberg.com': 'https://blog.miguelgrinberg.com/feed',
        'keygen.sh': 'https://keygen.sh/blog/feed.xml',
        'mjg59.dreamwidth.org': 'https://mjg59.dreamwidth.org/data/rss',
        'computer.rip': 'https://computer.rip/rss.xml',
        'tedunangst.com': 'https://www.tedunangst.com/flak/rss',
        'buttondown.com_hillelwayne': 'https://buttondown.com/hillelwayne/rss',
        'devblogs.microsoft.com_oldnewthing': 'https://devblogs.microsoft.com/oldnewthing/feed',
    }
    
    # Process each blog
    success_count = 0
    failed_blogs = []
    total_articles = 0
    
    for i, blog_name in enumerate(blogs):
        print(f"\n[{i+1}/{len(blogs)}] 处理: {blog_name}")
        
        rss_url = blog_rss_map.get(blog_name)
        html_url = f"https://{blog_name}"
        
        if not rss_url:
            print(f"  ⚠️  未找到RSS配置，跳过")
            failed_blogs.append(blog_name)
            continue
        
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
        if i < len(blogs) - 1:
            delay = random.uniform(2, 4)
            print(f"  等待 {delay:.1f} 秒...")
            time.sleep(delay)
    
    print("\n" + "=" * 60)
    print(f"抓取完成！")
    print(f"成功: {success_count}/{len(blogs)}")
    print(f"失败: {len(failed_blogs)}")
    
    if failed_blogs:
        print(f"\n失败的博客:")
        for blog in failed_blogs:
            print(f"  - {blog}")
    
    print("=" * 60)

if __name__ == "__main__":
    main()