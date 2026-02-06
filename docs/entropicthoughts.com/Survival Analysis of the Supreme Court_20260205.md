# Survival Analysis of the Supreme Court

**来源:** https://entropicthoughts.com
**链接:** https://entropicthoughts.com/survival-analysis-of-the-supreme-court
**日期:** Tue, 27 Jan 2026 00:00:00 +0100

---

# [Entropic Thoughts](/)

## Survival Analysis of the Supreme Court

  * [Home](/)
  * [Archive](/archive)
  * [Tags](/tags)
  * [About](/about)
  * [xkqr.org](https://xkqr.org/)



# Survival Analysis of the Supreme Court

by kqr, scheduled 2026-01-27

Tags: 

  * [forecasting](tags.html#forecasting)



![survival-analysis-of-the-supreme-court.jpg](../image/banner/survival-analysis-of-the-supreme-court.jpg)

[The 2026 acx prediction contest](https://www.metaculus.com/notebooks/41230/the-acx-2026-prediction-contest-is-live-10000-prize-pool/) asks [whether any justice of the Supreme Court (scotus) will leave during the year](https://www.metaculus.com/questions/41072/scotus-composition-change-in-2026/). Well, actually it asks whether one of two things will happen: 

  * Congress enacts a bill that changes the number of seats in the scotus; or
  * a sitting justice officially leaves office.



The first condition seems extremely unlikely. All actual changes to the size of the scotus happened in the years 1801–1869. At the time, representatives of the scotus had to regularly travel across the us. Asking six people to cover all that country when horseback was the most efficient mode of transport was unrealistic so the scotus was gradually expanded when the size of the us expanded.11 It was also briefly decreased in the 1860s for political reasons, but that appears more difficult to do these days. Not for lack of trying – there have been recent proposals to change the size of the scotus but they've so far been shot down fairly easily.

The – by far – most likely reason for the scotus composition to change is that one of its current justices leave. What's the probability of that? 

At the time of writing, the community aggregate indicates 28 %. I think the correct forecast is 18 %. 

# The base rate is 35 %

In the following plot, each point represents a year with a vacancy in the scotus. 

![survival-scotus-01.svg](./image/survival-scotus-01.svg)

There have been … hang on, I'm counting … eighteen, nineteen, twenty, twenty-one! vacancies in the past sixty years. Through [Laplace's law of succession](laws-of-succession.html), we get a base rate of \\(\frac{21+1}{60+2}\\) = 35 % that any given year sees a vacancy. This is slightly higher than the community aggregate. Is this an appropriate base rate? 

## Verifying base rate assumptions

This base rate assumes vacancies happen randomly and independently, i.e. that 

  * a vacancy does not increase the probability of another vacancy, and
  * a long time with no vacancies does not increase the probability of a vacancy.



But the dots look a little lumpy. If that's the case, then the independence assumption is invalid. [Some lumpiness is expected from randomness](https://empiricalzeal.com/2012/12/21/what-does-randomness-look-like/), but how much is too much? 

If the vacancy times are random and independent, the average time between vacancies should match the standard deviation, because that's what happens with exponential time between events. That's indeed what we find: the average time between vacancies is 2.8 years, and the standard deviation is 2.6. 

We can also plot the quantiles of our data against the quantiles of the exponential distribution. This results in a so-called _q-q plot_. If the points fall on a straight line, then the distribution of the data is a decent match for the theoretical distribution, which in this case would be the exponential distribution. 

![survival-scotus-02.svg](./image/survival-scotus-02.svg)

Great! It seems the assumptions for the base rate to hold are fulfilled. So 35 % is a good base rate. 

## Driving a forecast from actuarial tables

Plenty of community members are not satisfied with the naïve base rate. Justices sit for life, and some of them are quite old! We can look up their ages in an [actuarial table online](https://www.ssa.gov/oact/STATS/table4c6.html) to find out how likely each justice is to survive the coming year.22 By the way, I will exclusively be using actuarial tables for men in this section. Four of the nine currently sitting justices are women, and women live longer, but historically justices have been men. To keep the maths and data entry simple, I will stick to the majority gender.

Age | Death rate  
---|---  
53 | 0.7 %  
55 | 0.8 %  
58 | 1.1 %  
60 | 1.2 %  
65 | 1.8 %  
70 | 2.5 %  
71 | 2.7 %  
75 | 3.7 %  
77 | 4.5 %  
  
If we flip the death rate we get the probability of surviving another year. If we multiply all of those together we get the probability that all nine survive the coming year. The number is 82 %. The inverse of that – 18 % – is the probability that any of the justices die next year. 

## Intermission: a note on mortality

The previous paragraph is one of those bizarre things I never thought I would write, but when I'm wearing my forecasting hat I end up writing anyway. 

Imagine, for a moment, being a justice of the scotus. Maybe you're Neil Gorsuch, the oldest sibling of three children, both your parents attorneys. You grew up in a household that encouraged debate, and you have participated in many clubs in your youth, and other professional organisations throughout your life. You met your partner at Oxford, you've been married for 30 years, and together you have two children. In your spare time, you enjoy being outdoors. 

I – an arbitrary person online – come along and speculate there's a 1/5 chance you or one of your closest colleagues die in the next year because you're all an old bunch. I don't even do it with kindness; I make it look like maths homework. 

I know not everyone cares, but that's an ethical dilemma I keep having every time I write articles like these. I really don't want to compress people's life experiences down to their probability of survival for another year. But that is _exactly_ what makes for good forecasting. And I hope that by writing these articles – even if I'm blunt – I can teach someone else how to forecast better, and that they get opportunities to use it to improve the world. 

## Back to actuarial tables

Maybe that 18 % probability that someone in the scotus dies next year is the reason the community goes lower than the base rate? 

Not so fast: scotus justices are probably more healthy than the average us citizen. To capture some of this effect, we can look at life tables used for computing _individual annuities_ , in contrast to e.g. census data or group-level annuities. This helps us because people who live longer self-select into individual annuities, so the data underlying their caculations are biased toward people who live longer. If we do the same exercise there, we get a probability of 14 % that any justice dies this year. 

Maybe there's a connection between this probability and the probability that there are vacancies? Here's a time series of the survival probability of the entire scotus, with vertical lines indicating vacancies. 

![survival-scotus-03.svg](./image/survival-scotus-03.svg)

If we take just the death probabilities that intersect with the vacancy lines, and order them by size, we get the distribution of the probability that any scotus justice dies during the vacancy years. It looks like this. 

![survival-scotus-04.svg](./image/survival-scotus-04.svg)

The probability we computed for the current scotus – 14 % – is definitely toward the lower half of this distribution, making it seem like the scotus is in a comparatively low-risk-of-death phase, and maybe this is an argument we can use the lower the base rate of 35 % to 28 %. 

But there's a better way to do it! 

# Treating retirement as the event of interest

In the previous section, we looked at actual death at various ages. But these days, justices rarely die on the bench. In the past sixty years, three justices have died while still serving the scotus. The other eighteen retired, and some lived for much longer after that. 

What we can do is try to model at which age justices leave the scotus for any reason – including retirement, resignation, and death. It's probably a good idea to stick to data produced in the past 60 years, because both health and work norms are different now to what they were a hundred years ago. 

The following plot is the survival function of scotus tenures at any given age. It shows the probability that justices serve to any specific age as it would be estimated at the moment they are confirmed. 

![survival-scotus-06.svg](./image/survival-scotus-06.svg)

The crosses over the curve indicate the ages of the currently serving justices. They help improve the shape of the curve by telling us that they have _not_ retired yet by their current age. (A common mistake is to treat them like the other data points, but that leads to biasing the curve downward.) 

We can extract from this curve the probability that the currently serving justices stay on for another year. The _hazard function_ 33 This function has many names. One of the best is _force of mortality_. But you may also see _hazard rate_ or _failure rate_. of time is the probability that a justice retires at a particular age. We extract it from the survival function by dividing the negative derivative with the value.44 This should be quite intuitive: it's the proportion of justices that have left at a specific age to those that stayed for another year.

\\[h(t) = -\frac{S'(t)}{S(t)}\\] 

In this case we want the inverse of the hazard function to get the probability that a justice stays on. We'll use a second order numerical approximation for the derivative, meaning the function we end up computing is 

\\[1-h(t) = 1+\frac{S(t+1) - S(t-1)}{2S(t)}\\] 

When we do, we get the following curve, which indicates the probability that justices of various ages serve another year. 

![survival-scotus-07.svg](./image/survival-scotus-07.svg)

This curve is a little choppy due to the low amount of data we have. For example, it estimates the probability of retiring at age 72 as 3 %, but then at age 73 it's impossible.55 And perhaps more visibly, there's a brief respite at age 88 where justices are guaranteed to go on another year, whereas they are highly likely to retire at ages 87 and 89. To smooth things out, we paint in a Weibull distribution over the survival function. The Weibull distribution tends to fit this kind of data fairly well using only two parameters, so it's often used for the purpose. 

![survival-scotus-08.svg](./image/survival-scotus-08.svg)

Because the Weibull distribution has a relatively simple mathematical expression, we can practice our differentiation skills and get its derivative analytically.66 The ingredients for this recipe is 2× chain rule, 1× polynomial rule, 1× differentiation of the exponential function, 2× product rule. We could also look it up because the survival function is the inverse distribution function, and the derivative of the distribution function is the density function. Thus the hazard function is effectively the negative density function. We construct the inverse hazard function from that, and plot the resulting curve with crosses indicating the ages of current justices. 

![survival-scotus-09.svg](./image/survival-scotus-09.svg)

From this curve, we read off the probabilities that the current justices serve another year. 

99.9 % | 99.9 % | 99.8 % | 99.6 % | 99.0 %  
---|---|---|---|---  
97.3 % | 96.8 % | 93.5 % | 90.8 % |   
  
The product of these probabilities is 79 %. The inverse of that – 21 % – is the probability that any justice retires in the next year. 

## Confirming against history

To find out how good this forecast is, we can verify against the historic data we have. To be clear, this is not a proper test of accuracy, because we've used the same historic data to fit the curve. Our method will perform worse in the real world compared to what it looks like here. But it's still useful to perform this check, because if it looks crappy when we are testing it with data that's in its favour, then we know it really sucks. 

The [Brier score](brier-score.html) of the base rate of 35 % is 0.218.77 Fun fact: the Brier score of a constant probability is optimised at 31.67 % because that's the _number of years_ there have been vacancies in the past data, even though the appropriate base rate is 35 %. Talk about overfitting! The Brier score of the above probabilities applied to the ages of past Supreme Courts is 0.174. 

We can also see how well calibrated the forecast is, by splitting the forecast into bins and comparing the mean predicted probability to the actual probability of a vacancy in the same year. 

Bin (observations) | Our model predicted | Actual probability  
---|---|---  
0–20 % (17) | 15 % | 6 %  
20–40 % (24) | 30 % | 25 %  
40–100 % (25) | 52 % | 56 %  
  
Here it looks like the model overestimates low probabilities and underestimates high probabilities. Since the model outputs 21 % as the forecast for the question, we should maybe consider adjusting that _downward_ to something like 18 % or so for our final forecast. 

There's a couple more concerns, though! 

  * Justices are no longer dying on the bench. This could reflect a trend of retiring earlier. If that's the case, our full 60-year data might be overestimating the retirement age slightly. However, it seems that if anything, justices retire later these days. The reason they don't die in service anymore has more to do with good health and modern medicine.
  * Someone claimed scotus vacancies tend to happen near election transitions, rather than mid-term. This is patently false. Mid-term is the most popular year for scotus vacancies. Ten out of the past 26 vacancies have happened mid-term. The most _infrequent_ year for scotus vacancies are actually election years.



These two concerns argue for adjusting the forecast in opposite directions (justices serve longer means we should lower the forecast, but this being a mid-term year suggests we should increase the forecast), which means sticking at 18 % is probably the right thing to do. 

# Where I went wrong

Now this would all be great, except I did something _very_ embarrassing. 

I had a long-lived brain fart and treated the fitted Weibull survival function (the accumulated hazard) as the probability that a justice would sit another year. This lead to an incredibly high forecast of 65 % that we will see a change in the next year. 

Let that sink in: the contest has a question where 18 % is the appropriate forecast, and I entered 65 %. Oh boy. 

It's too late to change it, so if the most likely thing happens, I'm screwed in terms of my competition placement. All I can do is hope that the 18 % chance strikes and any justice – against odds – retire this year. Maybe Clarence Thomas? You deserve a long retirement with your wife. Please? 

# Sidenotes

1

It was also briefly decreased in the 1860s for political reasons, but that appears more difficult to do these days. Not for lack of trying – there have been recent proposals to change the size of the scotus but they've so far been shot down fairly easily.

2

By the way, I will exclusively be using actuarial tables for men in this section. Four of the nine currently sitting justices are women, and women live longer, but historically justices have been men. To keep the maths and data entry simple, I will stick to the majority gender.

3

This function has many names. One of the best is _force of mortality_. But you may also see _hazard rate_ or _failure rate_.

4

This should be quite intuitive: it's the proportion of justices that have left at a specific age to those that stayed for another year.

5

And perhaps more visibly, there's a brief respite at age 88 where justices are guaranteed to go on another year, whereas they are highly likely to retire at ages 87 and 89.

6

The ingredients for this recipe is 2× chain rule, 1× polynomial rule, 1× differentiation of the exponential function, 2× product rule. We could also look it up because the survival function is the inverse distribution function, and the derivative of the distribution function is the density function. Thus the hazard function is effectively the negative density function.

7

Fun fact: the Brier score of a constant probability is optimised at 31.67 % because that's the _number of years_ there have been vacancies in the past data, even though the appropriate base rate is 35 %. Talk about overfitting!

If you liked this and want more you should [buy me a coffee](https://buymeacoff.ee/kqr). That helps me turn my 170+ ideas backlog into articles. 

Shoutout to my amazing wife    without whose support I would never make it past the first sentence. ♥ 

S = k log W.  
   
Comments? [Send me an email](/about).  
You can also [subscribe for new articles](https://buttondown.email/entropicthoughts). 
