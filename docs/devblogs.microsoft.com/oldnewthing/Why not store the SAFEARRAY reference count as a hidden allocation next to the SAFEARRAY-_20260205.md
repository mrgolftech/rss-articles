# Why not store the SAFEARRAY reference count as a hidden allocation next to the SAFEARRAY?

**来源:** https://devblogs.microsoft.com/oldnewthing
**链接:** https://devblogs.microsoft.com/oldnewthing/20260130-00/?p=112025
**日期:** Fri, 30 Jan 2026 15:00:00 +0000

---

When I described [ how `Safe­Array­Add­Ref` keeps its reference count in a side table](https://devblogs.microsoft.com/oldnewthing/20260127-00/?p=112018 "A digression on the design and implementation of SafeArrayAddRef and extending APIs in general"), commenter Koro Unhallowed wondered [ why we couldn't store the reference count either before or after the formal `SAFEARRAY` structure](https://devblogs.microsoft.com/oldnewthing/20260127-00/?p=112018&commentid=143776#comment-143776). Commenter Peter Cooper Jr. suspected that [ there might be cases where applications assumed how much memory a `SAFEARRAY` occupied](https://devblogs.microsoft.com/oldnewthing/20260127-00/?p=112018&commentid=143779#comment-143779).

And indeed that is the case.

Not all `SAFEARRAY`s are created by the `Safe­Array­Create` function. I've seen code that declared and filled out their own `SAFEARRAY` structure. In those cases, the code allocates exactly `sizeof(SAFEARRAY)` bytes and doesn't allocate any bonus data for the reference count.

Indeed, there three flags [ in the `fFeatures` member](https://learn.microsoft.com/windows/win32/api/oaidl/ns-oaidl-safearray) for these "bring your own `SAFEARRAY`" structures.

`FADF_AUTO` | An array that is allocated on the stack.  
---|---  
`FADF_STATIC` | An array that is statically allocated.  
`FADF_EMBEDDED` | An array that is embedded in a structure.  
  
These flag indicate that the array was not created by `Safe­Array­Create` but rather was constructed manually by the caller in various ways.¹

Note that if you pass a `SAFEARRAY` with one these flags to `Safe­Array­Add­Ref`, it will still increment the reference count, but you don't get a data pointer back because the caller does not control the lifetime of the `SAFEARRAY`. The lifetime of the `SAFEARRAY` is controlled by the lifetime of the `SAFEARRAY` variable on the stack (`FADF_AUTO`), in the DLL's global data segment (`FADF_STATIC`), or in the enclosing object (`FADF_EMBEDDED`).

This means that our earlier suggestion to wrap the `SAFEARRAY` inside an in/out `VARIANT` runs into trouble if the `SAFEARRAY` is one of these types of arrays with externally-controlled lifetime. For those, you have no choice but to copy the data.

¹ The documentation is, however, ambiguous about what "the array" refers to. Is it referring to the `SAFEARRAY` structure itself? Or is it referring to the data pointed to by the `pvData` member?

The post [Why not store the <CODE>SAFEARRAY</CODE> reference count as a hidden allocation next to the <CODE>SAFEARRAY</CODE>?](https://devblogs.microsoft.com/oldnewthing/20260130-00/?p=112025) appeared first on [The Old New Thing](https://devblogs.microsoft.com/oldnewthing).
