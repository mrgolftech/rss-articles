# How can I prevent the user from changing the widths of ListView columns?

**来源:** https://devblogs.microsoft.com/oldnewthing
**链接:** https://devblogs.microsoft.com/oldnewthing/20260204-00/?p=112037
**日期:** Wed, 04 Feb 2026 15:00:00 +0000

---

Suppose you are using a Win32 ListView control in report mode, and you've got all your columns set up perfectly, and you don't want the user to resize them. How do you do that?

There is no ListView style for preventing column resize, but there _is_ a header control style to prevent sizing: `HDS_NOSIZING`. This style requires Common Controls version 6, but I'm sure you're all using that version already, right?
    
    
    auto hdr = ListView_GetHeader(hwndLV);
    SetWindowLong(hdr, GWL_STYLE,
                  GetWindowLong(hdr, GWL_STYLE) | HDS_NOSIZING);
    

Whether the columns can be resized is independent of whether the columns can be rearranged, which you specify by setting the `LVS_EX_HEADER­DRAG­DROP` ListView extended style.
    
    
    ListView_SetExtendedListViewStyleEx(hwndLV,
                                        LVS_EX_HEADERDRAGDROP,
                                        LVS_EX_HEADERDRAGDROP);
    

Okay, but what if you're stuck in the dark ages with version 5 of the Common Controls? We'll look at that next time.

The post [How can I prevent the user from changing the widths of ListView columns?](https://devblogs.microsoft.com/oldnewthing/20260204-00/?p=112037) appeared first on [The Old New Thing](https://devblogs.microsoft.com/oldnewthing).
