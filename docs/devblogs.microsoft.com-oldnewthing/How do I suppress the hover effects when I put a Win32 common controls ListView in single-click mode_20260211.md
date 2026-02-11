# How do I suppress the hover effects when I put a Win32 common controls ListView in single-click mode?

**来源:** [devblogs.microsoft.com/oldnewthing](https://devblogs.microsoft.com/oldnewthing)
**发布时间:** Wed, 11 Feb 2026 15:00:00 +0000
**链接:** https://devblogs.microsoft.com/oldnewthing/20260211-00/?p=112057

---

{'type': 'text/html', 'language': None, 'base': 'https://devblogs.microsoft.com/oldnewthing/feed', 'value': '<p>A customer had a Win32 common controls ListView in single-click mode. This has a side effect of enabling hover effects: When the mouse hovers over an item, the cursor changes to a hand, and the item gets highlighted in the hot-track color. How can they suppress these hover effects while still having single-click activation?</p>\n<p>When the user hovers over an item, the ListView sends a <code>LVN_HOT\xadTRACK</code> notification, and you can suppress all hot-tracking effects by returning 1.</p>\n<pre>    // WndProc\n    case WM_NOTIFY:\n    {\n        auto nm = (NMLISTVIEW*)lParam;\n        if (nm-&gt;hdr.code == LVN_HOTTRACK)\n        {\n            return 1;\n        }\n    }\n    break;\n</pre>\n<p>If you are doing this from a dialog box, you need to set the <code>DWLP_MSG\xadRESULT</code> to the desired return value, which is 1 in this case, and then return <code>TRUE</code> to say &#8220;I handled the message; use the value I put into <code>DWLP_MSG\xadRESULT</code>.&#8221;</p>\n<pre>    // DlgProc\n    case WM_NOTIFY:\n    {\n        auto nm = (NMLISTVIEW*)lParam;\n        if (nm-&gt;hdr.code == LVN_HOTTRACK)\n        {\n            SetWindowLongPtr(hDlg, DWLP_MSGRESULT, 1);\n            return TRUE;\n        }\n    }\n    break;\n</pre>\n<p>The post <a href="https://devblogs.microsoft.com/oldnewthing/20260211-00/?p=112057">How do I suppress the hover effects when I put a Win32 common controls ListView in single-click mode?</a> appeared first on <a href="https://devblogs.microsoft.com/oldnewthing">The Old New Thing</a>.</p>'}

---

*抓取时间: 2026-02-12 06:02:37*
