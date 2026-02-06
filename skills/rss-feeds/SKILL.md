---
name: rss-feeds
description: 定期抓取技术博客RSS源，聚合最新文章信息并保存为markdown文件
---

# RSS Feeds 技能

定期抓取技术博客RSS源，聚合最新文章信息并保存为markdown文件。

## 概述

此技能用于：
- 定期抓取技术博客RSS源
- 聚合最新文章信息
- 生成摘要和推荐
- 将文章保存为markdown文件，按博客来源组织

## 配置

### OPML源文件
- 默认源：从GitHub Gist获取的技术博客OPML文件
- 可配置自定义OPML文件路径

### 抓取频率
- 默认：每6小时抓取一次
- 可配置抓取间隔

### 输出目录
- 默认：`/root/openclaw/gw/docs/rss/`
- 按博客来源创建子文件夹
- 每篇文章保存为独立的markdown文件

## 博客源列表

以下是当前聚合的所有92个技术博客的完整列表（按分类组织）：

### 技术与开发（21个）

| 博客名称 | RSS URL | HTML URL | 描述 |
|---------|---------|----------|------|
| simonwillison.net | https://simonwillison.net/atom/everything/ | https://simonwillison.net | Python/Django专家，分享Web开发、AI应用、数据科学等内容 |
| paulgraham.com | http://www.aaronsw.com/2002/feeds/pgessays.rss | https://paulgraham.com | YC创始人，分享创业、编程、思考等深度文章 |
| jeffgeerling.com | https://www.jeffgeerling.com/blog.xml | https://jeffgeerling.com | 硬件和嵌入式系统专家，专注于Linux、网络、硬件项目 |
| antirez.com | http://antirez.com/rss | http://antirez.com | Redis作者，分享编程、系统设计、开源项目经验 |
| michael.stapelberg.ch | https://michael.stapelberg.ch/feed.xml | https://michael.stapelberg.ch | Go开发者，开源项目 |
| miguelgrinberg.com | https://blog.miguelgrinberg.com/feed | https://blog.miguelgrinberg.com | Python开发者，Flask教程 |
| seangoedecke.com | https://www.seangoedecke.com/rss.xml | https://www.seangoedecke.com | Staff软件工程师，工程管理 |
| martinalderson.com | https://martinalderson.com/feed.xml | https://martinalderson.com | 软件开发思考 |
| nesbitt.io | https://nesbitt.io/feed.xml | https://nesbitt.io | Zig语言，包管理 |
| johndcook.com | https://www.johndcook.com/blog/feed/ | https://www.johndcook.com | 数学和编程 |
| evanhahn.com | https://evanhahn.com/feed.xml | https://evanhahn.com | Web开发，技术写作 |
| grantslatton.com | https://grantslatton.com/rss.xml | https://grantslatton.com | 系统设计 |
| xania.org | https://xania.org/feed | https://xania.org | C++开发，编译器 |
| lucumr.pocoo.org | https://lucumr.pocoo.org/feed.atom | https://lucumr.pocoo.org | Python核心开发者 |
| borretti.me | https://borretti.me/feed.xml | https://borretti.me | 系统编程 |
| matklad.github.io | https://matklad.github.io/feed.xml | https://matklad.github.io | Rust和系统编程 |
| maurycyz.com | https://maurycyz.com/index.xml | https://maurycyz.com | 静态网站生成 |
| skyfall.dev | https://skyfall.dev/rss.xml | https://skyfall.dev | Rails开发 |
| ericmigi.com | https://ericmigi.com/rss.xml | https://ericmigi.com | Pebble智能手表开发 |
| rachelbythebay.com | https://rachelbythebay.com/w/atom.xml | https://rachelbythebay.com | 嵌入式系统 |
| overreacted.io | https://overreacted.io/rss.xml | https://overreacted.io | React开发 |
| timsh.org | https://timsh.org/rss/ | https://timsh.org | Web开发 |
| gilesthomas.com | https://gilesthomas.com/feed/rss.xml | https://gilesthomas.com | Git专家 |
| rakhim.exotext.com | https://rakhim.exotext.com/rss.xml | https://rakhim.exotext.com | 代码质量 |
| beej.us | https://beej.us/blog/rss.xml | https://beej.us | 编程教程 |
| hugotunius.se | https://hugotunius.se/feed.xml | https://hugotunius.se | Rust编程 |
| bernsteinbear.com | https://bernsteinbear.com/feed.xml | https://bernsteinbear.com | Rust和编程语言设计 |
| danieldelaney.net | https://danieldelaney.net/feed | https://danieldelaney.net | 软件和哲学 |

### AI与科技（6个）

| 博客名称 | RSS URL | HTML URL | 描述 |
|---------|---------|----------|------|
| garymarcus.substack.com | https://garymarcus.substack.com/feed | https://garymarcus.substack.com | AI研究者，批判性思考 |
| pluralistic.net | https://pluralistic.net/feed/ | https://pluralistic.net | Cory Doctorow，数字权利 |
| terriblesoftware.org | https://terriblesoftware.org/feed/ | https://terriblesoftware.org | 软件工程批判 |
| worksonmymachine.substack.com | https://worksonmymachine.substack.com/feed | https://worksonmymachine.substack.com | AI提示工程 |
| herman.bearblog.dev | https://herman.bearblog.dev/feed/ | https://herman.bearblog.dev | AI和工具思考 |
| tomrenner.com | https://tomrenner.com/index.xml | https://tomrenner.com | AI和思考 |

### 硬件与工程（2个）

| 博客名称 | RSS URL | HTML URL | 描述 |
|---------|---------|----------|------|
| construction-physics.com | https://www.construction-physics.com/feed | https://www.construction-physics.com | 建筑技术 |
| idiallo.com | https://idiallo.com/feed.rss | https://idiallo.com | 软件工程思考 |

### 安全（2个）

| 博客名称 | RSS URL | HTML URL | 描述 |
|---------|---------|----------|------|
| krebsonsecurity.com | https://krebsonsecurity.com/feed/ | https://krebsonsecurity.com | 网络安全专家 |
| troyhunt.com | https://www.troyhunt.com/rss/ | https://www.troyhunt.com | 安全新闻和分析 |

### 创业与商业（3个）

| 博客名称 | RSS URL | HTML URL | 描述 |
|---------|---------|----------|------|
| steveblank.com | https://steveblank.com/feed/ | https://steveblank.com | 创业方法论 |
| wheresyoured.at | https://www.wheresyoured.at/rss/ | https://wheresyoured.at | 科技行业分析 |
| joanwestenberg.com | https://joanwestenberg.com/rss | https://joanwestenberg.com | 创业文化 |

### 系统与历史（5个）

| 博客名称 | RSS URL | HTML URL | 说明 |
|---------|---------|----------|------|
| dfarq.homeip.net | https://dfarq.homeip.net/feed/ | https://dfarq.homeip.net | 计算机历史 |
| devblogs.microsoft.com/oldnewthing | https://devblogs.microsoft.com/oldnewthing/feed | https://devblogs.microsoft.com/oldnewthing | Windows历史 |
| entropicthoughts.com | https://entropicthoughts.com/feed.xml | https://entropicthoughts.com | 系统思考 |
| righto.com | https://www.righto.com/feeds/posts/default | https://righto.com | 电子学和逆向工程 |
| oldvcr.blogspot.com | https://oldvcr.blogspot.com/feeds/posts/default | https://oldvcr.blogspot.com | 复古计算机 |
| bogdanthegeek.github.io | https://bogdanthegeek.github.io/blog/index.xml | https://bogdanthegeek.github.io | RISC-V和嵌入式 |

### 文化与生活（13个）

| 博客名称 | RSS URL | HTML URL | 描述 |
|---------|---------|----------|------|
| daringfireball.net | https://daringfireball.net/feeds/main | https://daringfireball.net | Apple和科技评论 |
| shkspr.mobi | https://shkspr.mobi/blog/feed/ | https://shkspr.mobi | 技术文化，书籍评论 |
| filfre.net | https://www.filfre.net/feed/ | https://www.filfre.net | 游戏历史 |
| aresluna.org | https://aresluna.org/main.rss | https://aresluna.org | 技术文化 |
| chadnauseam.com | https://chadnauseam.com/rss.xml | https://chadnauseam.com | 技术思考 |
| experimental-history.com | https://www.experimental-history.com/feed | https://www.experimental-history.com | 历史思考 |
| berthub.eu | https://berthub.eu/articles/index.xml | https://berthub.eu | 技术政策（荷兰） |
| blog.jim-nielsen.com | https://blog.jim-nielsen.com/feed.xml | https://blog.jim-nielsen.com | 设计与思考 |
| tedium.co | https://feed.tedium.co/ | https://tedium.co | 深度探索 |
| micahflee.com | https://micahflee.com/feed/ | https://micahflee.com | 隐私和安全 |
| anildash.com | https://anildash.com/feed.xml | https://anildash.com | 技术伦理 |
| simone.org | https://simone.org/feed/ | https://simone.org | 艺术和创意思考 |
| it-notes.dragas.net | https://it-notes.dragas.net/feed/ | https://it-notes.dragas.net | FreeBSD和系统管理 |
| danielwirtz.com | https://danielwirtz.com/rss.xml | https://danielwirtz.com | 生产力工具 |
| matduggan.com | https://matduggan.com/rss/ | https://matduggan.com | 3D打印和开源 |
| refactoringenglish.com | https://refactoringenglish.com/index.xml | https://refactoringenglish.com | 重构和代码质量 |
| philiplaine.com | https://philiplaine.com/index.xml | https://philiplaine.com | Kubernetes和云原生 |

### 其他（40个）

| 博客名称 | RSS URL | HTML URL | 描述 |
|---------|---------|----------|------|
| derekthompson.org | https://www.theatlantic.com/feed/author/derek-thompson/ | https://derekthompson.org | 经济和技术 |
| dwarkesh.com | https://www.dwarkeshpatel.com/feed | https://dwarkesh.com | 经济和技术 |
| jayd.ml | https://jayd.ml/feed.xml | https://jayd.ml | Web开发 |
| minimaxir.com | https://minimaxir.com/index.xml | https://minimaxir.com | 数据科学 |
| geohot.github.io | https://geohot.github.io/blog/feed.xml | https://geohot.github.io | 黑客和AI |
| jyn.dev | https://jyn.dev/atom.xml | https://jyn.dev | 编程语言 |
| geoffreylitt.com | https://www.geoffreylitt.com/feed.xml | https://www.geoffreylitt.com | 分布式系统 |
| downtowndougbrown.com | https://www.downtowndougbrown.com/feed/ | https://www.downtowndougbrown.com | Web开发 |
| brutecat.com | https://brutecat.com/rss.xml | https://brutecat.com | 编程 |
| eli.thegreenplace.net | https://eli.thegreenplace.net/feeds/all.atom.xml | https://eli.thegreenplace.net | C++教程 |
| abortretry.fail | https://www.abortretry.fail/feed | https://www.abortretry.fail | 编程 |
| fabiensanglard.net | https://fabiensanglard.net/rss.xml | https://fabiensanglard.net | 图形编程 |
| hey.paris | https://hey.paris/index.xml | https://hey.paris | 技术和思考 |
| danielchasehooper.com | https://danielchasehooper.com/feed.xml | https://danielchasehooper.com | C语言编程 |
| chiark.greenend.org.uk/~sgtatham | https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/feed.xml | https://www.chiark.greenend.org.uk/~sgtatham | PuTTY作者 Simon Tatham的博客 |
| keygen.sh | https://keygen.sh/blog/feed.xml | https://keygen.sh | 软件授权和分发 |
| mjg59.dreamwidth.org | https://mjg59.dreamwidth.org/data/rss | https://mjg59.dreamwidth.org | 安全研究 |
| computer.rip | https://computer.rip/rss.xml | https://computer.rip | 计算机历史 |
| tedunangst.com | https://www.tedunangst.com/flak/rss | https://www.tedunangst.com | 编程 |
| buttondown.com/hillelwayne | https://buttondown.com/hillelwayne/rss | https://buttondown.com/hillelwayne | 编程逻辑 |
| utcc.utoronto.ca/~cks | https://utcc.utoronto.ca/~cks/space/blog/?atom | https://utcc.utoronto.ca/~cks | OpenSSH开发 |
| lcamtuf.substack.com | https://lcamtuf.substack.com/feed | https://lcamtuf.substack.com | 安全研究 |
| mitchellh.com | https://mitchellh.com/feed.xml | https://mitchellh.com | Terraform和云基础设施 |
| dynomight.net | https://dynomight.net/feed.xml | https://dynomight.net | 数学和科学 |
| susam.net | https://susam.net/feed.xml | https://susam.net | Git和版本控制 |
| gwern.net | https://gwern.substack.com/feed | https://gwern.net | 深度思考者，AI、心理学等领域 |

**注意：**
- 所有博客的RSS URL都已验证可访问
- 包含斜杠的博客名（如 `buttondown.com/hillelwayne`）会自动创建对应的子目录
- 目录名与博客名完全一致，保持原始格式
- 如果某个博客的RSS无法访问，会在抓取时跳过并记录日志

## 使用方法

### 初始化RSS源
```
rss-feeds init
```

### 手动抓取并保存
```
rss-feeds fetch
```

### 查看最新文章
```
rss-feeds latest
```

### 生成摘要
```
rss-feeds summary
```

## 输出格式

抓取完成后会：
1. 生成最新文章摘要
2. 按博客来源创建文件夹
3. 将每篇文章保存为markdown文件，包含：
   - 文章标题
   - 来源博客名称和链接
   - 发布时间
   - 文章链接
   - 文章摘要
   - 抓取时间

## 文件结构

### RSS Feeds 技能目录
- `/root/openclaw/gw/skills/rss-feeds/config.json` - 配置文件
- `/root/openclaw/gw/skills/rss-feeds/feeds.opml` - RSS源文件
- `/root/openclaw/gw/skills/rss-feeds/cache/` - 抓取缓存
- `/root/openclaw/gw/skills/rss-feeds/logs/` - 日志文件

### 文章输出目录（MkDocs 仓库）
- `/root/openclaw/gw/docs/rss/` - 文章输出目录
  - `docs/` - Markdown 源文件目录
    - `index.md` - 首页
    - `blogs.md` - 所有博客列表页（重要：超链接配置见下方）
    - `[博客名称]/` - 各博客的目录（如 `simonwillison.net/`）
      - `index.md` - 博客索引页（自动生成，列出该博客所有文章）
      - `[文章标题].md` - 文章的markdown文件
  - `mkdocs.yml` - MkDocs 配置文件
  - `.github/workflows/deploy.yml` - GitHub Actions 部署配置

## MkDocs 网站配置

### site_url 配置
在 `mkdocs.yml` 中设置：
```yaml
site_url: https://mrgolftech.github.io/rss-articles/
```

### 重要：超链接配置要求

#### blogs.md 中的博客链接格式
在 `docs/blogs.md` 中列出所有博客时，必须使用以下格式：

```markdown
- **[simonwillison.net](/rss-articles/simonwillison.net/)** - Python/Django专家，分享Web开发、AI应用、数据科学等内容
- **[paulgraham.com](/rss-articles/paulgraham.com/)** - YC创始人，分享创业、编程、思考等深度文章
```

**关键规则：**
1. ✅ 使用完整的相对路径：`/rss-articles/[博客名称]/`
2. ✅ 必须包含末尾斜杠：`/`（指向目录，不是文件）
3. ✅ 正确闭合 Markdown 链接：`**[名称](链接)** - 描述`
4. ❌ 错误格式：`**[名称](链接]`（缺少闭合括号）
5. ❌ 错误格式：`**[名称](链接)*`（缺少第二个星号）

#### 为什么需要这些规则？

1. **`/rss-articles/` 前缀**：
   - MkDocs 会将 `site_url` 与相对路径拼接
   - 最终生成的完整 URL：`https://mrgolftech.github.io/rss-articles/simonwillison.net/`

2. **末尾斜杠 `/`**：
   - 博客名称是目录，不是文件
   - 没有 `/` 会导致 404 错误
   - 有 `/` 才能正确访问目录的 `index.md`

3. **正确的 Markdown 语法**：
   - `**` 开启加粗，需要 `**` 关闭
   - `[text](url)` 是标准 Markdown 链接语法
   - 任何语法错误都会导致链接无法渲染

#### 验证链接格式

生成 blogs.md 后，使用以下 Python 脚本验证：

```python
import re

with open('docs/blogs.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 检查链接格式
pattern = r'\]\((/rss-articles/[^)]+)\)\*\*'
matches = re.findall(pattern, content)

if len(matches) == 35:
    print(f"✅ 所有 {len(matches)} 个链接格式正确")
else:
    print(f"❌ 发现 {len(matches)} 个正确链接，预期 35 个")

# 检查是否有末尾斜杠
no_slash = [m for m in matches if not m.endswith('/')]
if no_slash:
    print(f"❌ 以下链接缺少末尾斜杠：{no_slash}")
else:
    print("✅ 所有链接都有末尾斜杠")
```

### 博客索引页 (index.md)

每个博客目录下应该有一个 `index.md` 文件，格式如下：

```markdown
# simonwillison.net

以下是本博客的所有文章：

- [文章标题 1](文章标题1_20260205/)
- [文章标题 2](文章标题2_20260204/)
- [文章标题 3](文章标题3_20260203/)

---

*本博客文章由 OpenClaw 自动抓取*
```

**注意：**
- 文章链接使用相对路径，不需要 `/rss-articles/` 前缀
- 文章链接也需要末尾斜杠（指向目录）

## 常见问题和解决方案

### 反爬虫保护

某些博客平台（如 Substack、Medium 等）有反爬虫保护，直接使用 `requests` 抓取文章页面时可能会遇到以下错误：

#### 常见错误

1. **403 Forbidden**
   - **原因**：网站检测到自动化请求，拒绝访问
   - **影响**：无法获取完整文章内容，文章文件缺失导致 404 错误
   - **典型案例**：`worksonmymachine.substack.com`

2. **429 Too Many Requests**
   - **原因**：请求频率过高，触发限流
   - **影响**：暂时无法访问该网站

3. **空内容或内容过短**
   - **原因**：网站返回了错误页面或验证页面
   - **影响**：文章内容不完整

#### 解决方案

##### 方案1：检查 RSS Feed 是否提供完整内容

在 `rss_feeds.py` 中，脚本会优先使用 RSS feed 提供的内容：

```python
# 检查是否有 content 字段（有些 RSS feed 提供完整内容）
if hasattr(entry, 'content') and len(entry.content) > 0:
    content = entry.content[0].value
```

**建议**：优先使用 RSS feed 中的完整内容，避免直接访问文章页面。

##### 方案2：使用 web_fetch 工具

如果直接请求失败，可以使用 OpenClaw 的 `web_fetch` 工具：

```python
# 使用 web_fetch 提取内容
from openclaw import web_fetch

result = web_fetch(
    url=article_url,
    extractMode="markdown",  # 或 "text"
    maxChars=10000
)

if result['status'] == 200:
    content = result['text']
```

**优点**：
- `web_fetch` 使用不同的 User-Agent 和请求头
- 可能绕过某些反爬虫检测
- 自动提取主要内容

##### 方案3：添加请求延迟和随机 User-Agent

在 `rss_feeds.py` 的 `fetch_full_content` 方法中：

```python
import time
import random

# 添加随机延迟
time.sleep(random.uniform(1, 3))

# 使用随机 User-Agent
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36...',
    # 更多 User-Agent...
]
headers = {
    'User-Agent': random.choice(user_agents),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,...',
    'Accept-Language': 'en-US,en;q=0.5',
}
```

##### 方案4：跳过受保护的网站

如果某些网站无法抓取，可以在配置文件中添加黑名单：

```json
{
  "skip_domains": [
    "substack.com",
    "medium.com"
  ]
}
```

### 调试缺失的文章

#### 发现问题

当用户报告某个博客的 404 错误时：

1. 检查博客目录是否存在：
   ```bash
   ls -la docs/[博客名称]/
   ```

2. 检查 `index.md` 列出的文章文件是否存在：
   ```bash
   cat docs/[博客名称]/index.md
   ```

3. 统计目录中的文件数量：
   ```bash
   find docs/[博客名称]/ -name "*.md" -type f | wc -l
   ```

#### 修复步骤

1. **获取文章内容**：
   ```python
   # 使用 web_fetch
   from openclaw import web_fetch
   result = web_fetch(url="文章链接", extractMode="markdown")
   content = result['text']
   ```

2. **创建文章文件**：
   ```python
   from datetime import datetime

   md_content = f"""# 文章标题

   **来源:** [博客名称](博客链接)
   **发布时间:** 发布时间
   **链接:** 文章链接

   ---

   {content}

   ---

   *抓取时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
   """

   with open('docs/[博客名称]/文章标题_20260128.md', 'w') as f:
       f.write(md_content)
   ```

3. **提交并推送**：
   ```bash
   git add docs/[博客名称]/
   git commit -m "Add missing article for [博客名称]"
   git push origin main
   ```

### 预防措施

1. **定期检查缺失的文章**：
   ```bash
   # 查找只有 index.md 的目录
   for dir in docs/*/; do
       count=$(find "$dir" -name "*.md" -type f | wc -l)
       if [ $count -eq 1 ]; then
           echo "$dir: 只有 index.md"
       fi
   done
   ```

2. **更新 RSS 抓取脚本**：
   - 添加错误处理和日志记录
   - 记录哪些文章抓取失败
   - 生成缺失文章的报告

3. **使用 cron 定期验证**：
   创建 cron 任务检查 404 错误：
   ```python
   # scripts/check_missing_articles.py
   import os

   output_dir = "docs"
   missing = []

   for blog_dir in os.listdir(output_dir):
       index_path = os.path.join(output_dir, blog_dir, "index.md")
       if not os.path.exists(index_path):
           continue

       # 读取 index.md 中列出的文章
       with open(index_path) as f:
           for line in f:
               if line.startswith('- ['):
                   # 提取文件名
                   import re
                   match = re.search(r'\]\(([^)]+)\)', line)
                   if match:
                       article_path = os.path.join(output_dir, blog_dir, match.group(1))
                       if not os.path.exists(article_path):
                           missing.append(article_path)

   print(f"发现 {len(missing)} 个缺失的文章")
   for path in missing:
       print(f"  - {path}")
   ```

### 已知问题平台

| 平台 | 问题 | 解决方案 |
|------|------|----------|
| Substack | 403 Forbidden | 使用 web_fetch 或检查 RSS feed |
| Medium | 403/内容不完整 | 使用 web_fetch |
| 某些 WordPress 博客 | 需要登录 | 跳过或手动处理 |
| Ghost 博客 | 有时返回空内容 | 检查 RSS feed 是否有完整内容 |

## 维护建议

1. **每周检查一次**：运行 `check_missing_articles.py` 查找缺失的文章
2. **监控 GitHub Actions**：查看部署日志，及时发现 404 错误
3. **更新黑名单**：将无法抓取的网站添加到配置文件
4. **备份 RSS feeds**：定期备份 OPML 文件和抓取的数据
- 文章链接也需要末尾斜杠（指向目录）