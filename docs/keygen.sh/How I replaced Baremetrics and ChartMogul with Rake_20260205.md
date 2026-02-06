# How I replaced Baremetrics and ChartMogul with Rake

**来源:** https://keygen.sh
**链接:** https://keygen.sh/blog/how-i-replaced-baremetrics-and-chartmogul-with-rake/
**日期:** Tue, 05 Jan 2021 06:00:00 GMT

---

[Keygen is Fair SourceStar us on GitHub _arrow_right_alt_](https://github.com/keygen-sh/keygen-api)

[ Keygen](/)

 _menu_

  * Use Cases _expand_more_
    * [ _lock_open_ Software Application Licensing](/software-licensing-api/)Use Keygen's flagship software licensing API to add license key validation, device activation and entitlements to any software product. 
    * [_cloud_download_ Software Artifact Distribution](/software-distribution-api/)Use Keygen's supplementary software distribution API to securely deliver artifacts and offer automatic updates to licensed users. 
    * [_bolt_ No-code Licensing Automation](/integrate/zapier/)Use Zapier to integrate Keygen with your favorite tools, such as Stripe for payments, and Postmark for transactional emails. No code required. 
    * [__For On-Premise/Multi-Prem](/for-on-prem-software/)
    * [ __For Go Programs](/for-go-programs/)
    * [ __For iOS Apps](/for-ios-apps/)
    * [ __For Mac Applications](/for-mac-apps/)
    * [ __For Android Apps](/for-android-apps/)
    * [ __For Windows Programs](/for-windows-programs/)
    * [ __For Container Images](/for-docker-images/)
    * [ __For Electron Apps](/for-electron-apps/)
    * [ __For WordPress Plugins](/for-wordpress-plugins/)
    * [ For Tauri Apps](/for-tauri-apps/)
    * [ __For Python Packages](/for-python-packages/)
    * [ __For PHP Packages](/for-composer-packages/)
    * [ __For Node Packages](/for-npm-packages/)
    * [ __For RubyGems](/for-rubygems/)
  * Demos _expand_more_
    * [ _phonelink_lock_ License Activation Portal Demo](/demo/license-activation-portal/)
    * [ _vpn_key_ License Key Validation Demo](/demo/license-key-validation/)
    * [Try Dashboard Demo ](https://app.keygen.sh/demo)
  * Developers _expand_more_
    * [ _dns_ Self-Host Keygen](/docs/self-hosting/)Learn how to self-host Keygen's Community Edition for free, or self-host our Enterprise Edition for your business. 
    * [_lan_ Keygen Relay NEW](/docs/relay/)Use Keygen Relay to securely distribute node-locked licenses in offline and air-gapped environments. 
    * [_terminal_ Developer CLI](/docs/cli/)Use Keygen's official CLI to sign and publish software releases. Integrate with our SDKs for secure automatic upgrades. 
    * [_import_contacts_ Documentation ](/docs/)
    * [_data_object_ API Reference ](/docs/api/)
    * [_update_ Changelog ](/changelog/)
    * [_security_ Security ](/security/)
    * [_code_ Source Code ](https://github.com/keygen-sh/keygen-api)
  * Company _expand_more_
    * [ __Read the Source Code](https://github.com/keygen-sh/keygen-api) Keygen is an Fair Source software licensing and distribution API. View the source code on GitHub to learn more. [_compare_arrows_ Build vs Buy](/build-vs-buy/)Businesses of all sizes face the question of whether to build or buy a licensing solution. 
    * [_volunteer_activism_ Open Source ](/open-source/)
    * [_description_ Fair Source ](/license/)
    * [_business_ About ](/about/)
    * [_badge_ Careers ](/jobs/)
    * [_article_ Blog ](/blog/)
    * [_support_ Get Support ](/cdn-cgi/l/email-protection#d7a4a2a7a7b8a5a397bcb2aeb0b2b9f9a4bf)
  * [Pricing ](/pricing/)
  * [Log in ](https://app.keygen.sh/login)
  * [Sign Up](https://app.keygen.sh/register?plan=984180df-07b3-4dc1-b138-ca68a0f913ed)



# How I replaced Baremetrics and ChartMogul with Rake

Tuesday, January 5th 2021

In the early days of my business, I was a happy Baremetrics user. I was new to running a Software-as-a-Service (SaaS) business, I only had a handful of Stripe plans, and all I really wanted to know was my monthly recurring revenue (MRR). But fast-forward to 2020 and I was starting to transition into running Keygen full-time, and my needs as a solo-founder had changed quite a bit.

It wasn't too far into 2020 when I realized I wasn't getting the insights I needed from Baremetrics. I eventually tried switching to ChartMogul, both to see if I could get better visibility into my business, but also to save a few bucks, since I was also in the process of cutting out unnecessary costs after going full-time.

Instead of simply peeking MRR every single day, sometimes obsessively, I also wanted to get a better pulse on my conversion rate, and most of all, I wanted to get visibility into how long it actually takes customers to convert, and what types of customers convert. I figured, since I was already unhappy with Baremetrics and ChartMogul, I'd try my hand at calculating the metrics myself using a Rake task. I had just wrapped up the launch of a few new features, so I was looking for a change of pace anyways.

Scripting in Ruby is always a nice change of pace.

I'll walk you through the basics of using Rake to calculate some common business metrics. (Most of Keygen is a typical Ruby on Rails app, so this post will assume a Rails folder structure.)

Let's begin by creating a file for our Rake task,
    
    
    $ touch lib/tasks/money.rake
    
    $ touch lib/tasks/money.rake
    _content_copy_

The Rake task we'll be working on makes a few assumptions, for the sake of brevity, such as assuming all subscriptions are billed monthly, as well as a lack of discounts (which I'd personally avoid anyways for B2B, but that's a blog post for another day.)

Feel free to adjust accordingly.

Next, let's add the Rake task boilerplate,
    
    
    require 'stripe'
    
     
    
    desc 'get revenue report'
    
    task money: :environment do
    
      puts 'Hello, world!'
    
    end
    
    require 'stripe'
    
    desc 'get revenue report'
    task money: :environment do
      puts 'Hello, world!'
    end
    _content_copy_

And we can run it by using this command,
    
    
    $ rake money
    
    > Hello, world!
    
    $ rake money
    > Hello, world!
    _content_copy_

Har har. (Credit to [@geetfun](https://twitter.com/geetfun/status/1337220581087981568) for that one.)

## Retrieving subscription data

So first thing's first â we'll need to get an array of all of our Stripe subscriptions. This is the main dataset that we'll be using for our calculations.
    
    
    Stripe.api_key = ENV.fetch('STRIPE_SECRET_KEY')
    
     
    
    subscriptions =
    
      Stripe::Subscription.list(status: 'all', limit: 100, expand: ['data.customer'])
    
        # Retrieve all subscriptions, following pagination until complete.
    
        .auto_paging_each
    
        .to_a
    
        # Filter out deleted customers.
    
        .filter { |s| !s.customer.deleted? }
    
        # Remove duplicate subscriptions per-customer. Keep the latest.
    
        .sort_by { |s| [s.customer.id, -s.created] }
    
        .uniq { |s| s.customer.id }
    
    Stripe.api_key = ENV.fetch('STRIPE_SECRET_KEY')
    
    subscriptions =
      Stripe::Subscription.list(status: 'all', limit: 100, expand: ['data.customer'])
        # Retrieve all subscriptions, following pagination until complete.
        .auto_paging_each
        .to_a
        # Filter out deleted customers.
        .filter { |s| !s.customer.deleted? }
        # Remove duplicate subscriptions per-customer. Keep the latest.
        .sort_by { |s| [s.customer.id, -s.created] }
        .uniq { |s| s.customer.id }
    _content_copy_

(You may want to cache the data if you're planning on running this task a few times during development, or multiple times a day, as it can be a bit long running if you have a large number of subscriptions.)

## Calculating MRR

And now for the big show! Let's calculate that ubiquitous SaaS metric: Monthly Recurring Revenue (MRR). To start, we'll get an array of our paid subscriptions,
    
    
    paid_subscriptions = subscriptions.filter { |s| s.status == 'active' }
    
    paid_subscriptions = subscriptions.filter { |s| s.status == 'active' }
    _content_copy_

(One quirk here is that we're not including subscriptions with an `over_due` status. This status is used when a subscription is still "active", but has 1 or more invoice that hasn't been paid and is overdue. We may still want to consider these users a "paid user" until their subscription is fully canceled, given they also have at least 1 paid invoice. More on invoices later, though.)

Next, we'll need to create an array of our monthly revenue per-user,
    
    
    revenue_per_user = paid_subscriptions.map { |s| s.plan.amount.to_f * s.quantity / 100 }
    
    revenue_per_user = paid_subscriptions.map { |s| s.plan.amount.to_f * s.quantity / 100 }
    _content_copy_

(If you have annual plans, you'll need to adjust `revenue_per_user` to account for that. This is also where you'd want to apply any discounts.)

Finally, we can sum that up to get our MRR,
    
    
    monthly_recurring_revenue = revenue_per_user.sum(0.0)
    
    monthly_recurring_revenue = revenue_per_user.sum(0.0)
    _content_copy_

## Calculating ARR

Now that we have our MRR, it's super simple to calculate our Annual Run Rate (ARR),
    
    
    annual_run_rate = monthly_recurring_revenue * 12
    
    annual_run_rate = monthly_recurring_revenue * 12
    _content_copy_

## Calculating ARPU

Our MRR calculation used our `revenue_per_user` variable, which is also useful to calculate Average Revenue Per-User (ARPU),
    
    
    average_revenue_per_user =
    
      revenue_per_user.sum(0.0) / revenue_per_user.size
    
    average_revenue_per_user =
      revenue_per_user.sum(0.0) / revenue_per_user.size
    _content_copy_

## Calculating conversion rate

One of the most important metrics for my business is conversion rate. This tells me how many of the new sign ups coming in actually turn into paying customers ("new" sign ups, meaning those within the last 30 days). If I was going to optimize anything, it would be this metric right here. You can stuff more leads into the funnel, but if they aren't converting in the first place, it's all for naught.

Calculating our conversion rate is relatively simple,
    
    
    new_paid_subscriptions = paid_subscriptions.filter { |s| s.created >= 1.month.ago.to_i }
    
    new_subscriptions = subscriptions.filter { |s| s.created >= 1.month.ago.to_i }
    
    new_paid_subscriptions = paid_subscriptions.filter { |s| s.created >= 1.month.ago.to_i }
    new_subscriptions = subscriptions.filter { |s| s.created >= 1.month.ago.to_i }
    _content_copy_

We get an array of our new paid customers and an array of all new subscriptions, for the past 30 days, then we divide the size of `new_paid_subscriptions` by the size of `new_subscriptions`,
    
    
    conversion_rate = new_paid_subscriptions.size.to_f / new_subscriptions.size * 100
    
    conversion_rate = new_paid_subscriptions.size.to_f / new_subscriptions.size * 100
    _content_copy_

This gives us the percentage of new sign ups that convert. (More on this later.)

## Calculating churn rate

Another very useful metric is churn rate. This tells us how many of our customers cancel their subscription in a given time period.

Calculating our churn rate require a few things up front,
    
    
    canceled_subscriptions = subscriptions.filter { |s| s.status == 'canceled' }
    
    churned_subscriptions =
    
      canceled_subscriptions
    
        # Select only recent cancellations.
    
        .filter { |s| s.canceled_at >= 1.month.ago.to_i || s.ended_at >= 1.month.ago.to_i }
    
        # Filter out customers who never added a payment method, i.e. an unconverted trial.
    
        .filter { |s| s.customer.default_source.present? }
    
    canceled_subscriptions = subscriptions.filter { |s| s.status == 'canceled' }
    churned_subscriptions =
      canceled_subscriptions
        # Select only recent cancellations.
        .filter { |s| s.canceled_at >= 1.month.ago.to_i || s.ended_at >= 1.month.ago.to_i }
        # Filter out customers who never added a payment method, i.e. an unconverted trial.
        .filter { |s| s.customer.default_source.present? }
    _content_copy_

Here, we get an array of all canceled subscriptions, and then filter that down into our final churned subscriptions array, containing canceled subscriptions in the past month that have a payment method added. (We could improve this by scanning for paid invoices instead of looking at whether or not the customer has a payment method, but once again, we'll dive more into invoices later.)

Next, we'll need to get a count of our subscribers at the start of the month,
    
    
    paid_subscriptions_count_at_period_start =
    
      (paid_subscriptions.size - new_paid_subscriptions.size) + churned_subscriptions.size
    
    paid_subscriptions_count_at_period_start =
      (paid_subscriptions.size - new_paid_subscriptions.size) + churned_subscriptions.size
    _content_copy_

Getting that number, even though we aren't storing historical data to look back in time 30 days, actually isn't as hard as you'd think.

We can subtract our `new_paid_subscriptions` count from our current `paid_subscriptions` count, and then add our `churned_subscriptions` count to that (since they were paying subscribers in the previous period). That should get us the number we're looking for, given you don't do anything weird with your customer/subscription objects, e.g. delete them.

Finally, we can calculate our churn rate,
    
    
    churn_rate =
    
      churned_subscriptions.size.to_f / paid_subscriptions_count_at_period_start * 100
    
    churn_rate =
      churned_subscriptions.size.to_f / paid_subscriptions_count_at_period_start * 100
    _content_copy_

## Calculating LTV

Another useful metric is a user's life-time value, or rather, the average of all users' life-time values, also referred to as LTV.

To calculate our LTV, we'll need to retrieve an array of all of our "converted" subscribers,
    
    
    converted_subscriptions =
    
      (paid_subscriptions + canceled_subscriptions)
    
        # Filter out canceled customers who never added a payment method.
    
        .filter { |s| s.customer.default_source.present? }
    
    converted_subscriptions =
      (paid_subscriptions + canceled_subscriptions)
        # Filter out canceled customers who never added a payment method.
        .filter { |s| s.customer.default_source.present? }
    _content_copy_

We may only want to pay attention to subscriptions within a certain timeframe, e.g. 1 year, but I'll leave that as-is for now, which will give us our overall LTV.

Next, we'll get the subscription duration, in months, of all converted subscribers,
    
    
    subscription_durations =
    
      converted_subscriptions
    
        .map { |s| ((s.ended_at || Time.now) - s.created) / 1.month }
    
    subscription_durations =
      converted_subscriptions
        .map { |s| ((s.ended_at || Time.now) - s.created) / 1.month }
    _content_copy_

Then we'll get the average subscription duration,
    
    
    average_subscription_duration =
    
      subscription_durations.sum(0.0) / subscription_durations.size
    
    average_subscription_duration =
      subscription_durations.sum(0.0) / subscription_durations.size
    _content_copy_

Finally, we'll multiply our ARPU by our average subscription duration,
    
    
    life_time_value =
    
      average_revenue_per_user * average_subscription_duration
    
    life_time_value =
      average_revenue_per_user * average_subscription_duration
    _content_copy_

The resulting number is our LTV.

## Calculating revenue growth rate

The last metric we'll calculate is our Revenue Growth Rate. This will give us a percent change for our MRR, compared to the previous month.

First, we'll want to get our current MRR, which we already have from our previous calculations. Then, we'll want to get our previous month's MRR.

But how?

We'll do a few things:

  1. We'll need to take our current MRR, `monthly_recurring_revenue`.
  2. Subtract our "new" revenue from it (think: `new_paid_subscriptions`).
  3. Add our "lost" revenue back in (think: `churned_subscriptions`).



This total should give us our MRR for the previous period, i.e. 30 days ago.

Where's the code? Well, I'll leave this one up to the reader.

But here's the gist of it,
    
    
    next_mrr = monthly_recurring_revenue
    
    prev_mrr = (next_mrr - new_revenue) + lost_revenue
    
    revenue_growth_rate =
    
      (next_mrr - prev_mrr) / prev_mrr * 100
    
    next_mrr = monthly_recurring_revenue
    prev_mrr = (next_mrr - new_revenue) + lost_revenue
    revenue_growth_rate =
      (next_mrr - prev_mrr) / prev_mrr * 100
    _content_copy_

## Improving our dataset

Our base subscription dataset is relatively simple, being an array of subscription objects, and we could actually improve it a bit to garner more insights. One way to do that would be to scan a subscription's (or customer's) invoices to determine if they've "converted" vs. simply looking at the subscription's `status` attribute.

You can retrieve a subscription's invoices like so,
    
    
    invoices =
    
      Stripe::Invoice.list(subscription: subscription.id, limit: 100)
    
        .auto_paging_each
    
        .to_a
    
    invoices =
      Stripe::Invoice.list(subscription: subscription.id, limit: 100)
        .auto_paging_each
        .to_a
    _content_copy_

But do keep in mind that this type of operation is very expensive â retrieving all invoices for all subscriptions is going to result in an N+1 query, meaning lot of Stripe API requests, and a long time spent staring at a seemingly frozen terminal. When I request invoices for a set of subscriptions, I try to keep my dataset as small as possible, and only request what I absolutely need. I also cache the data, especially data that is unlikely to change, e.g. a canceled subscriber's invoices from a year ago.

Once we start pulling invoices per-subscription, it's much easier to calculate other interesting metrics, such as how long it takes a user to convert into a paying customer, or more commonly referred to as "time-to-convert."

All we need to do to get a subscription's time-to-convert is grab the date of their first paid invoice, and from that, subtract the date at which the customer was created,
    
    
    # Sort invoices in ASC order, to make sure we can select their
    
    # first paid invoice, not the most recent paid invoice.
    
    sorted_invoices = invoices.sort_by { |i| i.created }
    
     
    
    # Find their first paid invoice with an amount > 0.
    
    first_paid_invoice = sorted_invoices.find { |i| i.amount_paid > 0 }
    
     
    
    # Calculate the subscription's time-to-convert
    
    time_to_convert =
    
      first_paid_invoice.status_transitions.paid_at - subscription.customer.created
    
    # Sort invoices in ASC order, to make sure we can select their
    # first paid invoice, not the most recent paid invoice.
    sorted_invoices = invoices.sort_by { |i| i.created }
    
    # Find their first paid invoice with an amount > 0.
    first_paid_invoice = sorted_invoices.find { |i| i.amount_paid > 0 }
    
    # Calculate the subscription's time-to-convert
    time_to_convert =
      first_paid_invoice.status_transitions.paid_at - subscription.customer.created
    _content_copy_

And this was where things started to get interesting for me, now that I could see my average time-to-convert.

Why?

Because I discovered that my average time-to-convert was about 45 days.

A lot longer than I thought!

I had my guesses as to what my time-to-convert was, based on normal day-to-day conversations with leads and new customers, but I was never really sure. The aforementioned SaaS metric/analytics services didn't tell me what it was, and they kind of made me too lazy to calculate it myself.

But honestly, when I really think about it, it makes a lot of sense, given that Keygen is integrated pre-revenue for a lot of businesses. And a lot of the time businesses will evaluate Keygen in the early stages of product dev, but the actual licensing integration won't be until much later on in the timeline, usually more towards the end as they inch towards release. That disconnect would almost always result in a manual trial extension, which was becoming cumbersome to manage.

## Making some changes

This discovery informed me of a few things that needed to change,

First â my free trial length. I originally had a 14-day free trial, and what I had seen was that a lot of leads would see the short trial and actually wait to sign up, until they were ready to evaluate and integrate within that arbitrary 14-day period.

To me, that puts unneeded pressure on the evaluation and integration process, and also increases the chance that the lead won't come back later on.

To alleviate the perceived pressure there, I've opted to try an "unlimited trial," which is essentially just a limited free tier. (Gasp! I always told myself I would never do a free plan.) Having a free tier gives new customers ample time to evaluate Keygen, and then fit the integration into their unique product development timeline. And it allows them to sign up right away, reducing the chance of losing a lead.

Second â my conversion rate calculation. If it takes a user, on average, over 40 days to convert, then calculating conversion rate over the past 30 days makes little sense (see `new_paid_subscriptions` and `new_sign_ups`), because users actually take longer than that to convert. Instead, I've opted to calculate conversion rate over the past 90 days, since my 90th percentile time-to-convert is pretty close to that number at around 100 days. (An overall conversion rate, or at least for the past 12 months, may also be a good metric to have on-hand.)

I may adjust my 90 day time-to-convert calculation window further out as time moves on, or better yet, retrieve all "first paid invoices" in the past 30 days and then calculate the time-to-convert from that. That's the cool thing about using Rake for this type of thing â you're in control of how you calculate your metrics, and you get to see the metrics that matter to you and nothing else.

It's specifically tailored to you and your business.

## Final thoughts

I've since expanded my Rake task to include metrics such as forecasted revenue based on current growth rate, more in-depth conversion metrics, and I've also recently started tying in account data to gain better visibility into what types of customers convert, how fast they convert, how many licenses they have, average admin user count, etc. All of this helps me in making decisions.

You get a lot more freedom when it comes to exploring data when you're a technical founder and can do this type of stuff through scripting. And it's especially nice when you use a great programming language like Ruby.

(ââ _â )

Small tangentâ

I've mentioned this before, on various places like Twitter or Reddit, but I find myself running this Rake task maybe once or twice a week. Usually on Monday morning, at the least. But I've noticed a lot less anxiety about numbers going up and down when I limit the amount of times I check my stats. I also hard-coded a 2-day cache TTL for all of the Stripe data, and made it so clearing the cache and rerunning the Rake task is a chore.

Purposefully.

Constantly having the anxious itch to "check my stats" was becoming a problem. I'd need that dopamine hit from seeing green numbers. And I'd feel depressed if I saw red. Nobody talks about it, but sometimes I would find myself in a Spotify-induced coma mindlessly reloading ChartMogul/Baremetrics hoping to see a change, even though I knew there would be no change. Everything nowadays is about instant gratification and constant dopamine hits. It's really easy to become addicted to stupid things, like checking your stats, so putting up some boundaries is helpful.

Anywaysâ

Hope you enjoyed the blog post. Follow me on Twitter, [@keygen_sh](https://twitter.com/keygen_sh), where I occasionally post tidbits on Ruby, Rails and what it's like running a SaaS as a solo founder.

In the end, I knew neither Baremetrics nor ChartMogul were going to work for me.

So, I chose to drop them in favor of Rake.

* * *

If you find any errors in my code, or if you can think of ways to improve things, [ping me via Twitter](https://x.com/_m27e). 

Â© 2016â2026 Keygen LLC â All Rights Reserved â Reach out <[[email protected]](/cdn-cgi/l/email-protection)>  
The Keygen name, logo, and mark are trademarks of Keygen LLC in the United States

  * [Status](https://status.keygen.sh)
  * [About](/about/)
  * [Security](/security/)
  * [Changelog](/changelog/)
  * [Privacy](/privacy/)
  * [Terms](/terms/)
  * [SLA](/terms/sla/)
  * [Blog](/blog/)
  * [Jobs](/jobs/)
  * [Press](/press/)
  * [License](/license/)
  * [CLA](/cla/)
  * [ __](https://github.com/keygen-sh)
  * [__](https://hub.docker.com/u/keygen)
  * [](https://discord.gg/TRrhSaWSsN)
  * [__](https://twitter.com/keygen_sh)


