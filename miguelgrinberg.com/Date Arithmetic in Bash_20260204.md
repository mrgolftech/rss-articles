# Date Arithmetic in Bash

**来源:** [miguelgrinberg.com](https://miguelgrinberg.com)
**发布时间:** Wed, 04 Feb 2026 11:09:06 GMT
**链接:** https://blog.miguelgrinberg.com/post/date-arithmetic-in-bash

---

<p>Date and time management libraries in many programming languages are famously bad. <a href="https://dev.arie.bovenberg.net/blog/python-datetime-pitfalls/">Python's datetime module</a> comes to mind as one of the best (worst?) examples, and so does <a href="https://fjolt.com/article/javascript-date-is-weird/">JavaScript's Date class</a>. It feels like these libraries could not have been made worse on purpose, or so I thought until today, when I needed to implement some date calculations in a backup rotation script written in bash.</p>
<p>So, if you wanted to learn how to perform date and time arithmetic in your bash scripts, you've come to the right place. Just don't blame me for the nightmares.</p>

---

*抓取时间: 2026-02-06 16:29:18*
