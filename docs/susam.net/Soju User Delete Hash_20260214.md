# Soju User Delete Hash

**来源:** [susam.net](https://susam.net)
**发布时间:** Sat, 14 Feb 2026 00:00:00 +0000
**链接:** https://susam.net/soju-user-delete-hash.html

---

<p>
  In <a href="https://susam.net/from-znc-to-soju.html">my last post</a>, I talked about
  switching from ZNC to Soju as my IRC bouncer.  One thing that caught
  my attention while creating and deleting Soju users was that the
  delete command asks for a confirmation, like so:
</p>
<pre><samp>$ <kbd>sudo sojuctl user delete soju</kbd>
To confirm user deletion, send "user delete soju 4664cd"
$ <kbd>sudo sojuctl user delete soju 4664cd</kbd>
deleted user "soju"</samp></pre>
<p>
  That confirmation token for a specific user never changes, no matter
  how many times we create or delete it.  The confirmation token is
  not saved in the Soju database, as can be confirmed here:
</p>
<pre><samp>$ <kbd>sudo sqlite3 -table /var/lib/soju/main.db 'SELECT * FROM User'</kbd>
+----+----------+--------------------------------------------------------------+-------+----------+------+--------------------------+---------+--------------------------+--------------+
| id | username |                           password                           | admin | realname | nick |        created_at        | enabled | downstream_interacted_at | max_networks |
+----+----------+--------------------------------------------------------------+-------+----------+------+--------------------------+---------+--------------------------+--------------+
| 1  | soju     | $2a$10$yRj/oYlR2Zwd8YQxZPuAQuNo2j7FVJWeNdIAHF2MinYkKLmBjtf0y | 0     |          |      | 2026-02-16T13:49:46.119Z | 1       |                          | -1           |
+----+----------+--------------------------------------------------------------+-------+----------+------+--------------------------+---------+--------------------------+--------------+</samp></pre>
<p>
  Surely, then, the confirmation token is derived from the user
  definition?  Yes, indeed it is.  This can be confirmed at the
  <a href="https://codeberg.org/emersion/soju/src/commit/v0.10.1/service.go#L1185-L1203">source
  code here</a>.  Quoting the most relevant part from the source code:
</p>
<pre><code>hashBytes := sha1.Sum([]byte(username))
hash := fmt.Sprintf("%x", hashBytes[0:3])</code></pre>
<p>
  Indeed if we compute the same hash ourselves, we get the same token:
</p>
<pre><samp>$ <kbd>printf soju | sha1sum | head -c6</kbd>
4664cd</samp></pre>
<p>
  This allows us to automate the two step Soju user deletion process
  in a single command:
</p>
<pre><code>sudo sojuctl user delete soju "$(printf soju | sha1sum | head -c6)"</code></pre>
<p>
  But of course, the implementation of the confirmation token may
  change in future and Soju helpfully outputs the deletion command
  with the confirmation token when we first invoke it without the
  token, so it is perhaps more prudent to just take that output and
  feed it back to Soju, like so:
</p>
<pre><code>sudo sojuctl $(sudo sojuctl user delete soju | sed 's/.*"\(.*\)"/\1/')</code></pre>
<!-- ### -->
<p>
  <a href="https://susam.net/soju-user-delete-hash.html">Read on website</a> |
  <a href="https://susam.net/tag/shell.html">#shell</a> |
  <a href="https://susam.net/tag/irc.html">#irc</a> |
  <a href="https://susam.net/tag/technology.html">#technology</a> |
  <a href="https://susam.net/tag/how-to.html">#how-to</a>
</p>

---

*抓取时间: 2026-02-18 18:04:21*
