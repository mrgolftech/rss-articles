#!/usr/bin/env python3
import os
import re
import time
import random
import json
import urllib.parse
from pathlib import Path
import xml.etree.ElementTree as ET
import html

# User agents to rotate through
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0',
]

# Known problematic blogs to skip
SKIP_BLOGS = ['xeiaso.net']

def sanitize_filename(name):
    """Sanitize blog name for use as directory name."""
    # Remove special characters, keep alphanumeric, dash, underscore
    name = re.sub(r'[^\w\-\.]', '_', name)
    return name

def fetch_rss(url, name):
    """Fetch RSS feed with retry logic."""
    import subprocess

    user_agent = random.choice(USER_AGENTS)
    cmd = [
        'curl', '-s', '-L',
        '-A', user_agent,
        '--connect-timeout', '15',
        '--max-time', '30',
        url
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=35)
        if result.returncode != 0:
            return None, f"curl failed with code {result.returncode}"
        if not result.stdout or len(result.stdout) < 100:
            return None, "Empty or too short response"
        return result.stdout, None
    except subprocess.TimeoutExpired:
        return None, "Timeout"
    except Exception as e:
        return None, str(e)

def parse_rss(xml_content, max_articles=5):
    """Parse RSS/Atom feed and extract articles."""
    try:
        root = ET.fromstring(xml_content)
        articles = []

        # Try RSS format first
        items = root.findall('.//item') or root.findall('.//{http://www.w3.org/2005/Atom}entry')

        for item in items[:max_articles]:
            title = ''
            link = ''
            desc = ''
            pub_date = ''

            # RSS
            title_elem = item.find('title')
            if title_elem is not None:
                title = html.unescape(title_elem.text or '')

            link_elem = item.find('link')
            if link_elem is not None:
                link = link_elem.text or ''
            else:
                # Atom format
                link_elem = item.find('{http://www.w3.org/2005/Atom}link')
                if link_elem is not None:
                    link = link_elem.get('href', '')

            desc_elem = item.find('description')
            if desc_elem is not None:
                desc = html.unescape(desc_elem.text or '')
            else:
                # Atom content
                desc_elem = item.find('{http://www.w3.org/2005/Atom}content')
                if desc_elem is not None:
                    desc = html.unescape(desc_elem.text or '')

            date_elem = item.find('pubDate')
            if date_elem is not None:
                pub_date = date_elem.text or ''
            else:
                date_elem = item.find('{http://www.w3.org/2005/Atom}published')
                if date_elem is not None:
                    pub_date = date_elem.text or ''

            if title and link:
                # Strip HTML from description
                desc = re.sub(r'<[^>]+>', ' ', desc)
                desc = ' '.join(desc.split())
                if len(desc) > 200:
                    desc = desc[:200] + '...'

                articles.append({
                    'title': title,
                    'link': link,
                    'description': desc,
                    'date': pub_date
                })

        return articles
    except ET.ParseError as e:
        print(f"  XML parse error: {e}")
        return []
    except Exception as e:
        print(f"  Parse error: {e}")
        return []

def create_blog_directory(name, rss_url, html_url, articles):
    """Create blog directory and markdown files."""
    base_dir = Path('/root/openclaw/gw/docs/rss/docs')
    blog_dir = base_dir / sanitize_filename(name)

    try:
        blog_dir.mkdir(exist_ok=True)

        # Create index.md
        index_content = f"""# {name}

[访问博客]({html_url})

## 最新文章

"""
        for i, article in enumerate(articles, 1):
            index_content += f"### {i}. {article['title']}\n\n"
            index_content += f"**链接**: {article['link']}\n\n"
            if article['date']:
                index_content += f"**日期**: {article['date']}\n\n"
            if article['description']:
                index_content += f"**摘要**: {article['description']}\n\n"
            index_content += "---\n\n"

        index_file = blog_dir / 'index.md'
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(index_content)

        # Create article markdown files
        for i, article in enumerate(articles[:5], 1):
            filename = f"{i:02d}_{sanitize_filename(article['title'][:50])}.md"
            article_file = blog_dir / filename

            article_content = f"""# {article['title']}

**原文链接**: {article['link']}
**发布日期**: {article['date'] or '未知'}

---

{article['description'] or '暂无摘要'}

---

*本文内容版权归原作者所有，仅供学习交流使用。*
"""
            with open(article_file, 'w', encoding='utf-8') as f:
                f.write(article_content)

        return True, None
    except Exception as e:
        return False, str(e)

def main():
    # List of missing blogs
    blogs = [
        ('ericmigi.com', 'https://ericmigi.com/rss.xml', 'https://ericmigi.com'),
        ('maurycyz.com', 'https://maurycyz.com/index.xml', 'https://maurycyz.com'),
        ('lcamtuf.substack.com', 'https://lcamtuf.substack.com/feed', 'https://lcamtuf.substack.com'),
        ('mitchellh.com', 'https://mitchellh.com/feed.xml', 'https://mitchellh.com'),
        ('dynomight.net', 'https://dynomight.net/feed.xml', 'https://dynomight.net'),
        ('utcc.utoronto.ca/~cks', 'https://utcc.utoronto.ca/~cks/space/blog/?atom', 'https://utcc.utoronto.ca/~cks'),
        ('xeiaso.net', 'https://xeiaso.net/blog.rss', 'https://xeiaso.net'),
        ('devblogs.microsoft.com/oldnewthing', 'https://devblogs.microsoft.com/oldnewthing/feed', 'https://devblogs.microsoft.com/oldnewthing'),
        ('skyfall.dev', 'https://skyfall.dev/rss.xml', 'https://skyfall.dev'),
        ('rachelbythebay.com', 'https://rachelbythebay.com/w/atom.xml', 'https://rachelbythebay.com'),
        ('overreacted.io', 'https://overreacted.io/rss.xml', 'https://overreacted.io'),
        ('timsh.org', 'https://timsh.org/rss/', 'https://timsh.org'),
        ('gilesthomas.com', 'https://gilesthomas.com/feed/rss.xml', 'https://gilesthomas.com'),
        ('matklad.github.io', 'https://matklad.github.io/feed.xml', 'https://matklad.github.io'),
        ('derekthompson.org', 'https://www.theatlantic.com/feed/author/derek-thompson/', 'https://derekthompson.org'),
        ('rakhim.exotext.com', 'https://rakhim.exotext.com/rss.xml', 'https://rakhim.exotext.com'),
        ('susam.net', 'https://susam.net/feed.xml', 'https://susam.net'),
        ('buttondown.com/hillelwayne', 'https://buttondown.com/hillelwayne/rss', 'https://buttondown.com/hillelwayne'),
        ('dwarkesh.com', 'https://www.dwarkeshpatel.com/feed', 'https://dwarkesh.com'),
        ('jayd.ml', 'https://jayd.ml/feed.xml', 'https://jayd.ml'),
        ('minimaxir.com', 'https://minimaxir.com/index.xml', 'https://minimaxir.com'),
        ('geohot.github.io', 'https://geohot.github.io/blog/feed.xml', 'https://geohot.github.io'),
        ('jyn.dev', 'https://jyn.dev/atom.xml', 'https://jyn.dev'),
        ('geoffreylitt.com', 'https://www.geoffreylitt.com/feed.xml', 'https://geoffreylitt.com'),
        ('downtowndougbrown.com', 'https://www.downtowndougbrown.com/feed/', 'https://www.downtowndougbrown.com'),
        ('brutecat.com', 'https://brutecat.com/rss.xml', 'https://brutecat.com'),
        ('eli.thegreenplace.net', 'https://eli.thegreenplace.net/feeds/all.atom.xml', 'https://eli.thegreenplace.net'),
        ('abortretry.fail', 'https://www.abortretry.fail/feed', 'https://www.abortretry.fail'),
        ('fabiensanglard.net', 'https://fabiensanglard.net/rss.xml', 'https://fabiensanglard.net'),
        ('oldvcr.blogspot.com', 'https://oldvcr.blogspot.com/feeds/posts/default', 'https://oldvcr.blogspot.com'),
        ('bogdanthegeek.github.io', 'https://bogdanthegeek.github.io/blog/index.xml', 'https://bogdanthegeek.github.io'),
        ('hugotunius.se', 'https://hugotunius.se/feed.xml', 'https://hugotunius.se'),
        ('gwern.net', 'https://gwern.substack.com/feed', 'https://gwern.net'),
        ('simone.org', 'https://simone.org/feed/', 'https://simone.org'),
        ('it-notes.dragas.net', 'https://it-notes.dragas.net/feed/', 'https://it-notes.dragas.net'),
        ('beej.us', 'https://beej.us/blog/rss.xml', 'https://beej.us'),
        ('hey.paris', 'https://hey.paris/index.xml', 'https://hey.paris'),
        ('danielwirtz.com', 'https://danielwirtz.com/rss.xml', 'https://danielwirtz.com'),
        ('matduggan.com', 'https://matduggan.com/rss/', 'https://matduggan.com'),
        ('refactoringenglish.com', 'https://refactoringenglish.com/index.xml', 'https://refactoringenglish.com'),
        ('philiplaine.com', 'https://philiplaine.com/index.xml', 'https://philiplaine.com'),
        ('bernsteinbear.com', 'https://bernsteinbear.com/feed.xml', 'https://bernsteinbear.com'),
        ('danieldelaney.net', 'https://danieldelaney.net/feed', 'https://danieldelaney.net'),
        ('herman.bearblog.dev', 'https://herman.bearblog.dev/feed/', 'https://herman.bearblog.dev'),
        ('tomrenner.com', 'https://tomrenner.com/index.xml', 'https://tomrenner.com'),
        ('blog.pixelmelt.dev', 'https://blog.pixelmelt.dev/rss/', 'https://blog.pixelmelt.dev'),
        ('danielchasehooper.com', 'https://danielchasehooper.com/feed.xml', 'https://danielchasehooper.com'),
        ('chiark.greenend.org.uk/~sgtatham', 'https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/feed.xml', 'https://www.chiark.greenend.org.uk/~sgtatham'),
        ('keygen.sh', 'https://keygen.sh/blog/feed.xml', 'https://keygen.sh'),
        ('mjg59.dreamwidth.org', 'https://mjg59.dreamwidth.org/data/rss', 'https://mjg59.dreamwidth.org'),
        ('computer.rip', 'https://computer.rip/rss.xml', 'https://computer.rip'),
        ('tedunangst.com', 'https://www.tedunangst.com/flak/rss', 'https://tedunangst.com'),
    ]

    results = {
        'success': [],
        'failed': [],
        'skipped': []
    }

    total = len(blogs)
    for i, (name, rss_url, html_url) in enumerate(blogs, 1):
        print(f"\n[{i}/{total}] Fetching: {name}")
        print(f"  RSS: {rss_url}")

        # Skip known problematic blogs
        if name in SKIP_BLOGS:
            print(f"  ⚠️  SKIPPED (known issue)")
            results['skipped'].append(name)
            time.sleep(random.uniform(0.5, 1.5))
            continue

        # Fetch RSS
        xml_content, error = fetch_rss(rss_url, name)

        if error:
            print(f"  ❌ FAILED: {error}")
            results['failed'].append((name, error))
            time.sleep(random.uniform(1, 2))
            continue

        # Parse RSS
        articles = parse_rss(xml_content, max_articles=5)

        if not articles:
            print(f"  ❌ FAILED: No articles found")
            results['failed'].append((name, "No articles found"))
            time.sleep(random.uniform(1, 2))
            continue

        print(f"  ✓ Found {len(articles)} articles")

        # Create files
        success, error = create_blog_directory(name, rss_url, html_url, articles)

        if success:
            print(f"  ✓ Created files")
            results['success'].append(name)
        else:
            print(f"  ❌ FAILED to create files: {error}")
            results['failed'].append((name, error))

        # Random delay to avoid being blocked
        delay = random.uniform(1, 3)
        print(f"  Waiting {delay:.1f}s...")
        time.sleep(delay)

        # Report progress every 10 blogs
        if i % 10 == 0:
            print(f"\n=== Progress: {i}/{total} ===")
            print(f"  Success: {len(results['success'])}")
            print(f"  Failed: {len(results['failed'])}")
            print(f"  Skipped: {len(results['skipped'])}")

    # Final report
    print("\n" + "="*60)
    print("FINAL REPORT")
    print("="*60)
    print(f"Total: {total}")
    print(f"✓ Success: {len(results['success'])}")
    print(f"✗ Failed: {len(results['failed'])}")
    print(f"⚠ Skipped: {len(results['skipped'])}")

    if results['failed']:
        print("\nFailed blogs:")
        for name, error in results['failed']:
            print(f"  - {name}: {error}")

    if results['skipped']:
        print("\nSkipped blogs:")
        for name in results['skipped']:
            print(f"  - {name}")

    # Save results to JSON
    with open('/root/openclaw/gw/docs/rss/fetch_results.json', 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to fetch_results.json")

if __name__ == '__main__':
    main()