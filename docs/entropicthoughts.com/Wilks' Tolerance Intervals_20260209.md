# Wilks' Tolerance Intervals

**来源:** [entropicthoughts.com](https://entropicthoughts.com)
**发布时间:** Tue, 10 Feb 2026 00:00:00 +0100
**链接:** https://entropicthoughts.com/wilks-tolerance-intervals

---

Imagine we want to figure out what round-trip times we can expect between Sweden
and New Zealand. We ping a server belonging to the University of Waikato from
Stockholm, and record the following round-trip times in milliseconds.
290
388
299
290
462
292
291
293
293
308
292
292
290
294
292
333
348
292
292
293
293
292
460
408
290
350
475
290
We want to tell our friend about our experience, but we don’t want to send over
this entire table. A decent way to summarise a distribution is by a
tolerance
interval
, which means the central portion in which some fraction of the values
end up. For our case, we might pick the fraction 90 %, meaning only 5 % of the
data will be smaller, and 5 % will be greater than the interval.
What many people then do is compute a mean and a standard deviation and give a
range that is 1.645 standard deviations on either side of the mean – this
corresponds to a 90 % tolerance interval
on the normal distribution when
parameters are fully known
. With mean and standard deviation computed from the
above, we get 226–421 ms.
1
1
324 ± 1.645 × 59 ms.
If we’re careless, we might tell our friend that 90 % of the time, we get
round-trip times of 226–421 ms.
But that’s ridiculous. I’m fairly sure 226 ms never happens, since 290 ms is
consistently the floor in the sample above. And well over 5 % of values in our
sample are greater than 406 ms; almost 11 % of them are.
A perhaps more intuitive solution would be to use the 5 % and 95 % quantiles in
the sample data. For that, we first need to sort the data by size.
290
290
290
290
290
291
292
292
292
292
292
292
292
293
293
293
293
294
299
308
333
348
350
388
408
460
462
475
Since this is 28 sample values, we compute the fifth percentile to be the
28×0.05 = 1.4th value from the start, and the 95th percentile to be the 1.4th
value from the end. This means we will interpolate the lower bound between the
first two numbers (290 and 290, yielding, well, 290 ms), and the upper bound
between the two last values (462 and 475, yielding 470 ms).
Maybe, then, we can say the 90 % tolerance interval is 290–470 ms? This is much
better.
But there’s something that feels wrong about both of the above methods: they do
not account for the size of our sample. We have collected 28 values, but what if
there were only 10? Would that be enough to determine a tolerance interval we
could rely on? Intuition says no – we’re running the risk of having only
collected central values, and underestimating the tolerance interval
significantly.
Wilks’ method
is a way to compute how confident we can be in a tolerance
interval derived this way.
2
2
I will not give an intuition for the theory this
is based on today, but it is very neat and I wish I could take time to do it.
It’s one of those things where you could have invented it.
Above, we chose the
1.4th and 26.6th value from 28 samples to construct a 90 % tolerance interval.
The confidence level \(\alpha\) of that interval is given by the
incomplete beta
function
\(I_p\), evaluated with three arguments
3
3
Wilks’ Formula Applied to
Computational Tools: A Practical Discussion
; Porter; Annals of Nuclear Energy;
2019.
:
The size of the tolerance interval we made (0.9 in this case);
The number of values from our sample we have based this on (26.6−1.4 = 25.2); and
One more than the number of values from our sample we have kept outside of the
interval (26−25.2 = 2.8, then add 1).
Mathematically, we write this as
\[\alpha = I_{0.9}\left(25.2,\; 2.8 + 1\right)\]
To illustrate graphically what happens, we represent the 28 samples as sticks
and show which of them we have captured in the range we use for estimating the
tolerance interval.
||||||||||||||||||||||||||||
|`----------v-------------´|
|    25.2 values inside    |
v                          v
1.4          +           1.4
= 2.8 values outside
R implements the incomplete beta function as
pbeta
, so we can evaluate the
confidence level of our proposed 90 % tolerance interval using R.
In[1]:
$ R -s -e
'pbeta(0.9, 25.2, 2.8+1)'
[1] 0.6521653
This is not good enough by any standard. A common confidence level to use is
\(\alpha\) = 0.05, and 0.65 is far from that.
The skeptic reader may have suspected the problem already: is 28 samples enough
to determine a 90 % tolerance interval? If we use
all
values gathered to build
the 90 % tolerance interval, i.e. say that the interval is the minimum to the
maximum (290–475 ms), what’s the confidence of that?
In[2]:
$ R -s -e
'pbeta(0.9, 28, 1)'
[1] 0.05233476
Hah! Just outside the traditional \(\alpha\) = 0.05 confidence level. We might be
happy with that still – call it close enough – but if we wanted to exceed that
\(\alpha\) level, we would have to collect more samples. So we run the ping for a
little longer, and collect more data, and sort it from smallest to largest
again.
290
290
290
290
290
290
290
290
290
291
291
291
292
292
292
292
292
292
292
292
292
292
292
292
293
293
293
293
293
294
294
295
295
296
299
301
303
306
308
310
320
329
333
337
338
342
344
347
348
349
350
368
372
378
381
382
388
408
439
439
460
462
475
There are 63 measurements here, so the 5 % and 95 % quantiles would be the
3.15th and the 59.85th value, i.e. a tolerance interval of 290–439 ms. To
compute the confidence level of that, we compute the span inside the range, 56.7
values, and outside the range, 6.3 values. Then we plug in:
In[3]:
$ R -s -e
'pbeta(0.9, 56.7, 6.3+1)'
[1] 0.6039901
Slightly better than before, but almost as bad. What we can do is use more
values from the sample. If we use all 63 values, i.e. say that the tolerance
interval is 290–475, we achieve a confidence level of
In[4]:
$ R -s -e
'pbeta(0.9, 63, 1)'
[1] 0.001310021
which is well beyond the conventional level of significance. However, by
choosing such a wide interval, we’re trading precision for lowered risk of
error. What if we want the error rate to be in that \(\alpha\) = 0.05 spot? We
need to use more than 59 values, but fewer than 63. We can ask R to figure out
for us how many.
In[5]:
$ R -s -e
'which(pbeta(0.9, 1:63, 63:1) < 0.05)[1]'
[1] 61
In other words, for a confidence level of \(\alpha\) = 0.05, we need to use 61 out
of the 63 sample values. That means we exclude the greatest and the smallest,
and use the rest. Our tolerance interval, now at the desired confidence level of
\(\alpha\) = 0.05, spans 290–462 ms.
That, finally, is how to construct a tolerance interval using Wilks’ method.
Compute the incomplete beta function \(I_p\) for various combinations of sample
values inside the range and outside the range.
Pick the smallest number of values inside the range that satisfies the
desired confidence level.
Done!
Given that R has the incomplete beta function as
pbeta
this becomes easy with
R. If we have \(N\) samples, and we want a 90 % tolerance interval at an \(\alpha\) =
0.05 confidence level, we run
In[6]:
which(pbeta(0.9, 1:N, N:1) < 0.05)[1]
and this tells us how many sample values we need to have inside the interval to
get the desired confidence level.
If we plug in \(N=28\), this would have returned
NA
, indicating it is not
possible to construct the desired tolerance interval using so few samples. On
the other hand, if we plug in a ridiculous sample size like \(N\) = 10,000, this
will return 9050, i.e. it will indicate that the naïve guess of 5 % and 95 %
quantiles fairly represent the underlying distribution. This is what we’d expect.
Since this process never involves any of the actual sample values, we can also
pre-compute tables for the number of sample values to include inside the range.
The following table indicates how many sample values to keep outside the range
of sample values that make up a 90 % tolerance interval at a confidence level of
\(\alpha\) = 0.05.
Sample size
Samples outside
Comment
0–29
—
Impossible
30–46
0
Use full range
47–60
1
Throw away maximum
61–75
2
Throw away min and max
76–88
3
Keep roughly central 96.6 %
89–102
4
ʺ     96.1 %
150
8
ʺ     94.7 %
250
16
ʺ     93.6 %
500
38
ʺ     92.4 %
1000
84
ʺ     91.8 %
5000
464
ʺ     90.1 %
This goes on, of course, but by this point we’re rather close to just using the
5 % and 95 % quantiles of the sample, so we’ll stop here. But it might surprise
you (it sure did me) that we need a whopping 5000 samples or more before the
naïve limits start being reliable!
But, hey, the above table hints at an optimisation. If we want a 90 % tolerance
interval at \(\alpha\) = 0.05, we didn’t need the full 63 sample values. We could
have opted to collect fewer and still get it. In fact, we could have collected
as few as 30 and then taken the smallest and largest as our tolerance interval
bounds.
That
was in fact the problem Wilks’ was actually interested in
solving: what’s the fewest number of samples we can collect and still produce
the tolerance interval we’re interested in at a confidence level we feel good
about?
Since this is independent of the actual sample values, it is easy to construct a
constant-memory streaming algorithm that produces a tolerance interval for an
incoming distribution in the shortest time possible: we read values and keep
track of the largest and the smallest
4
4
Aside from largest and smallest, we
throw away all other sample values – that’s what makes the algorithm
constant-memory.
, then we stop as soon as the pre-computed number of samples
are consumed.
In the case of a 90 % tolerance interval at 95 % confidence we run this process
for 30 samples. Here’s an
awk
snippet
5
5
If you haven’t yet, read through
the
posix
specification of
awk
. It’s tiny and teaches you the entire language.
that does that to any stream of numbers in the terminal:
In[7]:
awk
'
{
min = $0 < min || min == "" ? $0 : min;
max = $0 > max || max == "" ? $0 : max;
printf "%.0f %%\n", 100*NR/30;
}
NR == 30 { print (min "-" max); exit; };'
If we want our 90 % tolerance interval at greater or lower confidence, we’ll have
to compute the minimum number of samples to read to produce it for any given
level of confidence:
Confidence level (\(\a

... (内容已截断)

---

*抓取时间: 2026-02-11 00:02:55*
