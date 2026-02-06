#!/usr/bin/env python3
import os
import re
import time
import random
import json
import subprocess
from pathlib import Path
import xml.etree.ElementTree as ET
import html

def fetch_rss_with_curl(url):
    """Fetch RSS feed using curl with proper headers."""
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    ]
    
    user_agent = random.choice(user_agents)
    cmd = [
        'curl', '-s', '-L',
        '-A', user_agent,
        '--connect-timeout', '10',
        '--max-time', '20',
        url
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=25)
        if result.returncode == 0 and result.stdout:
            return result.stdout
        return None
    except:
        return None

def parse_rss_articles(xml_content, max_items=3):
    """Parse RSS and return recent articles."""
    try:
        root = ET.fromstring(xml_content)
        articles = []
        
        # Handle both RSS and Atom formats
        items = root.findall('.//item') or root.findall('.//{http://www.w3.org/2005/Atom}entry')
        
        for item in items[:max_items]:
            title = ''
            link = ''
            desc = ''
            pub_date = ''
            
            # Get title
            title_elem = item.find('title')
            if title_elem is not None and title_elem.text:
                title = html.unescape(title_elem.text)
            else:
                title_elem = item.find('{http://www.w3.org/2005/Atom}title')
                if title_elem is not None and title_elem.text:
                    title = html.unescape(title_elem.text)
            
            # Get link
            link_elem = item.find('link')
            if link_elem is not None and link_elem.text:
                link = link_elem.text
            else:
                link_elem = item.find('{http://www.w3.org/2005/Atom}link')
                if link_elem is not None:
                    link = link_elem.get('href', '')
            
            # Get description/content
            desc_elem = item.find('description')
            if desc_elem is not None and desc_elem.text:
                desc = html.unescape(desc_elem.text)
            else:
                desc_elem = item.find('{http://www.w3.org/2005/Atom}content')
                if desc_elem is not None and desc_elem.text:
                    desc = html.unescape(desc_elem.text)
                else:
                    desc_elem = item.find('{http://www.w3.org/2005/Atom}summary')
                    if desc_elem is not None and desc_elem.text:
                        desc = html.unescape(desc_elem.text)
            
            # Get publication date
            date_elem = item.find('pubDate')
            if date_elem is not None and date_elem.text:
                pub_date = date_elem.text
            else:
                date_elem = item.find('{http://www.w3.org/2005/Atom}published')
                if date_elem is not None and date_elem.text:
                    pub_date = date_elem.text
            
            if title and link:
                # Clean up description
                desc = re.sub(r'<[^>]+>', ' ', desc)
                desc = ' '.join(desc.split())
                if len(desc) > 150:
                    desc = desc[:150] + '...'
                elif not desc:
                    desc = '暂无摘要'
                
                articles.append({
                    'title': title,
                    'link': link,
                    'description': desc,
                    'date': pub_date
                })
        
        return articles
    except Exception as e:
        print(f"解析错误: {e}")
        return []

def main():
    # Popular tech blogs to check
    blogs = [
        ('simonwillison.net', 'https://simonwillison.net/atom/everything/', 'Python/Django专家'),
        ('paulgraham.com', 'http://www.aaronsw.com/2002/feeds/pgessays.rss', 'YC创始人'),
        ('antirez.com', 'http://antirez.com/rss', 'Redis作者'),
        ('jeffgeerling.com', 'https://www.jeffgeerling.com/blog.xml', '硬件和嵌入式专家'),
        ('overreacted.io', 'https://overreacted.io/rss.xml', 'React核心开发者'),
        ('krebsonsecurity.com', 'https://krebsonsecurity.com/feed/', '网络安全专家'),
        ('fabiensanglard.net', 'https://fabiensanglard.net/rss.xml', '图形编程专家'),
        ('gwern.net', 'https://gwern.substack.com/feed', '深度思考者'),
    ]
    
    all_articles = []
    
    print("🚀 开始抓取RSS Feeds...")
    print("=" * 50)
    
    for name, rss_url, description in blogs:
        print(f"\n📡 抓取: {name}")
        print(f"   {description}")
        
        xml_content = fetch_rss_with_curl(rss_url)
        if not xml_content:
            print(f"   ❌ 无法获取RSS")
            continue
        
        articles = parse_rss_articles(xml_content)
        if not articles:
            print(f"   ❌ 无文章")
            continue
        
        print(f"   ✅ 找到 {len(articles)} 篇文章")
        
        for article in articles:
            article['blog'] = name
            article['blog_desc'] = description
            all_articles.append(article)
        
        time.sleep(random.uniform(1, 2))
    
    # Sort by date (newest first)
    def extract_date(article):
        date_str = article.get('date', '')
        if not date_str:
            return ''
        # Simple date extraction - just use the string as-is for sorting
        return date_str
    
    all_articles.sort(key=extract_date, reverse=True)
    
    # Generate summary
    summary = f"""📝 RSS Feeds 更新报告 ({time.strftime('%Y-%m-%d %H:%M')})

📊 统计:
• 成功抓取: {len([a for a in all_articles if a.get('title')])} 篇文章
• 来源博客: {len(blogs)} 个

🔥 最新文章:

"""
    
    for i, article in enumerate(all_articles[:15], 1):
        summary += f"""{i}. **{article['title']}**
   🏷️ 来源: {article['blog']} ({article['blog_desc']})
   🔗 链接: {article['link']}
   📅 {article.get('date', '未知日期')}
   📝 {article['description']}

"""
    
    if len(all_articles) > 15:
        summary += f"\n📚 还有 {len(all_articles) - 15} 篇文章...\n"
    
    summary += """
💡 提示: 访问 https://mrgolftech.github.io/rss-articles/ 查看完整内容
"""
    
    print("\n" + "=" * 50)
    print("📋 摘要报告已生成")
    print("=" * 50)
    
    # Save summary
    with open('/root/openclaw/gw/docs/rss/latest_summary.md', 'w', encoding='utf-8') as f:
        f.write(summary)
    
    return summary

if __name__ == '__main__':
    summary = main()
    print(summary)