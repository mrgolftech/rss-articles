# Eigenvalue homework problems are backward

**来源:** [johndcook.com](https://johndcook.com)
**发布时间:** Fri, 06 Feb 2026 23:31:11 +0000
**链接:** https://www.johndcook.com/blog/2026/02/06/eigenvalue-roots/

---

{'type': 'text/html', 'language': None, 'base': 'https://www.johndcook.com/blog/feed/', 'value': '<h2>Classroom</h2>\n<p>When you take a linear algebra course and get to the chapter on eigenvalues, your homework problems will include a small matrix <em>A</em> and you will be asked to find the eigenvalues. You do this by computing the determinant</p>\n<p style="padding-left: 40px;">det(<em>A</em> − λ<em>I</em>) = <em>P</em>(λ)</p>\n<p>and getting <em>P</em>(λ), a polynomial in λ. The roots of <em>P</em> are the eigenvalues of\xa0<em>A</em>.</p>\n<p>Either <em>A</em> will be a 2 × 2 matrix, in which case you can find the roots using the quadratic formula, or the matrix will have been carefully selected so that <em>P</em>(λ) will be easy to factor. Otherwise, finding the roots of a polynomial is hard.</p>\n<h2>Real world</h2>\n<p>Numerical algorithms to find eigenvalues have gotten really good. In practice, you don&#8217;t compute determinants or find roots of polynomials. Instead you do something like the <em>QR</em> algorithm.</p>\n<p>Finding all the roots of a polynomial is a challenging problem, and so what you might do in practice is find the roots by constructing a matrix, called the <strong>companion matrix</strong>, whose eigenvalues correspond to the roots you&#8217;re after.</p>\n<h2>Summary</h2>\n<p>As a classroom exercise, you calculate roots of polynomials to find eigenvalues.</p>\n<p>In the real world, you might use an eigenvalue solver to find the roots of polynomials.</p>\n<p>I wrote a <a href="https://www.johndcook.com/blog/2020/08/03/conceptual-vs-numerical/">similar post</a> a few years ago. It explains that textbooks definite hyperbolic functions using\xa0<em>e</em><sup><em>x</em></sup>, but you might want to compute <em>e</em><sup><em>x</em></sup> using hyperbolic functions.</p>The post <a href="https://www.johndcook.com/blog/2026/02/06/eigenvalue-roots/">Eigenvalue homework problems are backward</a> first appeared on <a href="https://www.johndcook.com/blog">John D. Cook</a>.'}

---

*抓取时间: 2026-02-07 09:36:38*
