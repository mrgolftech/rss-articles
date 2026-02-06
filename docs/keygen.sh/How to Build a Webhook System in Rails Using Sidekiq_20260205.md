# How to Build a Webhook System in Rails Using Sidekiq

**来源:** https://keygen.sh
**链接:** https://keygen.sh/blog/how-to-build-a-webhook-system-in-rails-using-sidekiq/
**日期:** Wed, 16 Jun 2021 05:00:00 GMT

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
    * [_support_ Get Support ](/cdn-cgi/l/email-protection#8cfff9fcfce3fef8cce7e9f5ebe9e2a2ffe4)
  * [Pricing ](/pricing/)
  * [Log in ](https://app.keygen.sh/login)
  * [Sign Up](https://app.keygen.sh/register?plan=984180df-07b3-4dc1-b138-ca68a0f913ed)



# How to Build a Webhook System in Rails Using Sidekiq

Wednesday, Jun 16th 2021

It's 2021, and we're in the heyday of SaaS. As the SaaS economy has grown, so has the need for these services to communicate events to each other asynchronously. Complex business logic can often span across both internal and external services, and one way external communication is accomplished is with a design pattern called "webhooks."

If you've ever integrated with an API service such as [Stripe](https://stripe.com), you're probably well aware of what a webhook is. For Stripe, events like `customer.created` and `invoice.*` are _table-stakes_ for many businesses. (At least they are for ours.)

Many other services, and even our own API, send webhooks for important events. There are even [entire businesses built on the concept of webhooks](https://zapier.com).

Suffice it to say â webhooks are here to stay. They've gone from nice-to-have to must-have for any sort of API-based SaaS.

Speaking of SaaS â

There are a number of webhooks-as-a-service options out there, such as [HostedHooks](https://hostedhooks.com/) and YC-backed [Svix](https://www.svix.com/). But much to my dismay, none of these existed back when I started Keygen, so I figured I'd share the knowledge on how I've built mine over the years.

* * *

It's actually kind of funny â back in 2017, I had a similar idea scribbled down in my "notebook of start up ideas", but never got around to building it as I've been too busy with Keygen over the past 5 years. But I'm glad others have ran with the idea.

* * *

But running a webhook system yourself has its, ehmâ¦ quirks? The quirks are usually due to misbehaved webhook endpoints, but we'll touch more on that later. It seems like every month I'm adjusting things to handle new quirks.

Another thing that can take some time to get right is a retry cadence that works for both you and your users, which we'll also cover in a bit more detail later on.

Anyways â

These days, you may want to spend some time and ask yourself the build-vs-buy question. Using a third-party for webhooks may save you time (and money.)

But today, we're going to build. And we can move fast when we're on Rails.

## Defining our webhook resources

In its simplest form, a webhook system is built on top of the [pub/sub design pattern](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern):

> Some event **_e_** happens in our service, and we want to notify all subscribers **_s_**.

In the context of a webhook, an event **_e_** will consist of the following information:

  * An `event` â this will be an event name, for example `payment.successful`, `license.expired`, or `user.updated`.
  * A `payload` â this will be the data we'll be sending to subscribers. Typically, it's a snapshot of the affected resource. For example, the `user.updated` event may send a snapshot of the user after it was updated.



And a subscriber **_s_** will consist of the following information:

  * A `url` â this will be the URL that the webhook is delivered to.



Since we don't know how big the set of **_s_** is, we don't want to run these notifications inline with our normal application code. Why? Because the bigger **_s_** is, the slower our app will be, and we also have no control over deliveribility speed, other than through setting an upper bound on webhook execution time with a timeout.

So rather than run inline, we'll need some sort of queueing and background job system so that we can asynchronously process notifications to each subscriber.

If you've ever used Rails, you're probably familiar with the ubiquitous [Sidekiq](https://sidekiq.org) gem.

Sidekiq is powerful background job library that we'll be using to queue up webhook events and process them asynchronously. And we'll also be leaning on Sidekiq to handle the bulk of our retry logic (more on this later.)

**Have an open-source library you 'd like to dual-license like Sidekiq?** Dual-licensing open-source is all the rage these days, and we can help with that. By using our licensing and distribution APIs, you can easily distribute commercial license keys and allow license-gated downloads of your "premium" gems or libraries. 

The webhook system we're going to build today is actually modeled after Keygen's webhook system. As of writing, Keygen has processed nearly **250 million** webhook events using Sidekiq. (Thanks for your work, Mike!)

## Building out our models

To kick things off, let's create a new Rails 6 API application:
    
    
    $ rails new . --api --database postgresql \
    
        --skip-active-storage \
    
        --skip-action-cable
    
    $ rails new . --api --database postgresql \
        --skip-active-storage \
        --skip-action-cable
    _content_copy_

Then we'll want to create our first table, a **webhook endpoint**. These are going to represent the subscribers **_s_** in our webhook system.

Let's generate a new migration:
    
    
    $ rails g migration CreateWebhookEndpoints
    
    $ rails g migration CreateWebhookEndpoints
    _content_copy_

Next, we'll want to define the schema, which only consists of a `url`:
    
    
    class CreateWebhookEndpoints < ActiveRecord::Migration[5.2]
    
      def change
    
        create_table :webhook_endpoints do |t|
    
          t.string :url, null: false
    
     
    
          t.timestamps null: false
    
        end
    
      end
    
    end
    
    class CreateWebhookEndpoints < ActiveRecord::Migration[5.2]
      def change
        create_table :webhook_endpoints do |t|
          t.string :url, null: false
    
          t.timestamps null: false
        end
      end
    end
    _content_copy_

Now before we run our migration, let's also go ahead and define the other table in our system, the **webhook event**. As the name implies, these will represent the events **_e_** in our webhook system. Let's generate another migration:
    
    
    $ rails g migration CreateWebhookEvents
    
    $ rails g migration CreateWebhookEvents
    _content_copy_

Then let's define the schema, which consists of a reference to a webhook endpoint, as well as the `event` and `payload` attributes we discussed earlier:
    
    
    class CreateWebhookEvents < ActiveRecord::Migration[5.2]
    
      def change
    
        create_table :webhook_events do |t|
    
          t.integer :webhook_endpoint_id, null: false, index: true
    
     
    
          t.string :event, null: false
    
          t.text :payload, null: false
    
     
    
          t.timestamps null: false
    
        end
    
      end
    
    end
    
    class CreateWebhookEvents < ActiveRecord::Migration[5.2]
      def change
        create_table :webhook_events do |t|
          t.integer :webhook_endpoint_id, null: false, index: true
    
          t.string :event, null: false
          t.text :payload, null: false
    
          t.timestamps null: false
        end
      end
    end
    _content_copy_

Now let's go ahead and run those migrations:
    
    
    $ rails db:migrate
    
    $ rails db:migrate
    _content_copy_

Next, we'll want to define the 2 models. We'll start with the webhook endpoint:
    
    
    class WebhookEndpoint < ApplicationRecord
    
      has_many :webhook_events, inverse_of: :webhook_endpoint
    
     
    
      validates :url, presence: true
    
    end
    
    class WebhookEndpoint < ApplicationRecord
      has_many :webhook_events, inverse_of: :webhook_endpoint
    
      validates :url, presence: true
    end
    _content_copy_

Lastly, we'll define the webhook event model:
    
    
    class WebhookEvent < ApplicationRecord
    
      belongs_to :webhook_endpoint, inverse_of: :webhook_events
    
     
    
      validates :event, presence: true
    
      validates :payload, presence: true
    
    end
    
    class WebhookEvent < ApplicationRecord
      belongs_to :webhook_endpoint, inverse_of: :webhook_events
    
      validates :event, presence: true
      validates :payload, presence: true
    end
    _content_copy_

Okay, phew â

Let's go ahead and test out what we've got in the console:
    
    
    $ rails c
    
    > WebhookEndpoint.create!(url: 'https://functions.ecorp.example/webhooks')
    
    # => #<WebhookEndpoint
    
    #       id: 1,
    
    #       url: "https://functions.ecorp.example/webhooks",
    
    #       created_at: "2021-06-14 22:14:53.587473000 +0000",
    
    #       updated_at: "2021-06-14 22:14:53.587473000 +0000"
    
    #     >
    
    > WebhookEvent.create!(
    
        webhook_endpoint: _,
    
        event: 'events.test',
    
        payload: { test: 1 }
    
      )
    
    # => #<WebhookEvent
    
    #       id: 1,
    
    #       webhook_endpoint_id: 1,
    
    #       event: "events.test",
    
    #       payload: { "test" => 1 },
    
    #       created_at: "2021-06-14 22:17:06.908392000 +0000",
    
    #       updated_at: "2021-06-14 22:17:06.908392000 +0000"
    
    #     >
    
    $ rails c
    > WebhookEndpoint.create!(url: 'https://functions.ecorp.example/webhooks')
    # => #<WebhookEndpoint
    #       id: 1,
    #       url: "https://functions.ecorp.example/webhooks",
    #       created_at: "2021-06-14 22:14:53.587473000 +0000",
    #       updated_at: "2021-06-14 22:14:53.587473000 +0000"
    #     >
    > WebhookEvent.create!(
        webhook_endpoint: _,
        event: 'events.test',
        payload: { test: 1 }
      )
    # => #<WebhookEvent
    #       id: 1,
    #       webhook_endpoint_id: 1,
    #       event: "events.test",
    #       payload: { "test" => 1 },
    #       created_at: "2021-06-14 22:17:06.908392000 +0000",
    #       updated_at: "2021-06-14 22:17:06.908392000 +0000"
    #     >
    _content_copy_

## Building our webhook worker

Now that we have an event queued up, we need to process it. We've talked a lot about Sidekiq, so let's write our webhook worker.

### Installing dependencies

To start, let's go ahead and add Sidekiq and Redis to our `Gemfile`:
    
    
    +gem 'sidekiq' 
    
    +gem 'redis' 
    
    gem 'sidekiq' # [tl! ++]
    gem 'redis' # [tl! ++]
    _content_copy_

We're also going to need an HTTP library so that we can send webhook events to webhook endpoints. Let's add the popular [`http.rb`](https://github.com/httprb/http) gem.
    
    
    +gem 'http' 
    
    gem 'http' # [tl! ++]
    _content_copy_

And we'll run Bundler to install everything:
    
    
    $ bundle
    
    $ bundle
    _content_copy_

### Defining our webhook worker

Next up we'll want to create a new `app/workers` directory for our worker classes to live in, to keep our Sidekiq workers distinct from any ActiveJobs.
    
    
    $ mkdir app/workers
    
    $ touch app/workers/webhook_worker.rb
    
    $ mkdir app/workers
    $ touch app/workers/webhook_worker.rb
    _content_copy_

Now, let's define the base logic for our webhook worker. It's going to accept a webhook ID as an input parameter, use that to query the endpoint, then `POST` the event payload to the endpoint's URL. If it fails, it'll retry.
    
    
    require 'http.rb'
    
     
    
    class WebhookWorker
    
      include Sidekiq::Worker
    
     
    
      def perform(webhook_event_id)
    
        webhook_event = WebhookEvent.find_by(id: webhook_event_id)
    
        return if
    
          webhook_event.nil?
    
     
    
        webhook_endpoint = webhook_event.webhook_endpoint
    
        return if
    
          webhook_endpoint.nil?
    
     
    
        # Send the webhook request with a 30 second timeout.
    
        response = HTTP.timeout(30)
    
                       .headers(
    
                         'User-Agent' => 'rails_webhook_system/1.0',
    
                         'Content-Type' => 'application/json',
    
                       )
    
                       .post(
    
                         webhook_endpoint.url,
    
                         body: {
    
                           event: webhook_event.event,
    
                           payload: webhook_event.payload,
    
                         }.to_json
    
                       )
    
     
    
        # Raise a failed request error and let Sidekiq handle retrying.
    
        raise FailedRequestError unless
    
          response.status.success?
    
      end
    
     
    
      private
    
     
    
      # General failed request error that we're going to use to signal
    
      # Sidekiq to retry our webhook worker.
    
      class FailedRequestError < StandardError; end
    
    end
    
    require 'http.rb'
    
    class WebhookWorker
      include Sidekiq::Worker
    
      def perform(webhook_event_id)
        webhook_event = WebhookEvent.find_by(id: webhook_event_id)
        return if
          webhook_event.nil?
    
        webhook_endpoint = webhook_event.webhook_endpoint
        return if
          webhook_endpoint.nil?
    
        # Send the webhook request with a 30 second timeout.
        response = HTTP.timeout(30)
                       .headers(
                         'User-Agent' => 'rails_webhook_system/1.0',
                         'Content-Type' => 'application/json',
                       )
                       .post(
                         webhook_endpoint.url,
                         body: {
                           event: webhook_event.event,
                           payload: webhook_event.payload,
                         }.to_json
                       )
    
        # Raise a failed request error and let Sidekiq handle retrying.
        raise FailedRequestError unless
          response.status.success?
      end
    
      private
    
      # General failed request error that we're going to use to signal
      # Sidekiq to retry our webhook worker.
      class FailedRequestError < StandardError; end
    end
    _content_copy_

As you can see, our webhook system is actually relatively simple. And it's going to stay that way apart from a little subscription management and some special-case error handling. But overall, you may be surprised at how "simple" this system is.

Since we're leaning on Sidekiq to handle queueing, processing and retries, all we _really_ have to do is handle delivery. We're attempting delivery by sending an HTTP `POST` request to the endpoint's URL with a JSON-encoded payload:
    
    
    {
    
      "event": "events.test",
    
      "payload": {
    
        "test": 1
    
      }
    
    }
    
    {
      "event": "events.test",
      "payload": {
        "test": 1
      }
    }
    _content_copy_

**A quick note:** since we're raising an exception here, this is going to get a bitâ¦ _noisy._ I have some log line filters in place to ignore the verbose stack traces from `FailedRequestError`, so keep that idea tucked away. You can also silence the stack trace by overriding `FailedRequestError#backtrace`, e.g. `def backtrace = nil`. 

This whole thing could probably be done without relying on errors for control flow, but I can't be bothered. It works as-is, and ignoring noisy log lines is cheap. 

### Delivering our first webhook

Let's go ahead and attempt to deliver our first webhook event. For now, we'll run jobs inline from the console, rather than queue them:
    
    
    $ rails c
    
    > WebhookWorker.new.perform(WebhookEvent.last.id)
    
    # => Traceback (most recent call last):
    
    #      2: from (irb):1
    
    #      1: from app/workers/webhook_worker.rb:24:in `perform'
    
    #    HTTP::TimeoutError (execution expired)
    
    $ rails c
    > WebhookWorker.new.perform(WebhookEvent.last.id)
    # => Traceback (most recent call last):
    #      2: from (irb):1
    #      1: from app/workers/webhook_worker.rb:24:in `perform'
    #    HTTP::TimeoutError (execution expired)
    _content_copy_

Unless you happen to have a server running at the endpoint you entered, you're probably going to get a timeout error after about 30 seconds.

Which brings us to our first error case: **timeouts**.

### Handing delivery timeouts

First thing's first â let's go ahead and update our worker class to rescue from that error class so that we can handle it more gracefully:
    
    
     def perform(webhook_event_id)
    
       ...
    
    +rescue HTTP::TimeoutError 
    
    + 
    
     end
    
    def perform(webhook_event_id)
      ...
    rescue HTTP::TimeoutError # [tl! ++]
      # [tl! ++]
    end
    _content_copy_

But what does "gracefully" mean here? Well, let's think about this from a developer's perspective â what do they want to know? They probably want to know their webhook endpoint just timed out, right?

Ideally, we'd send them an alert. But we won't go that deep today. At the very least, we need a way to store an error on the webhook event model.

But rather than just store errors, why don't we go ahead and store the entire `response`? Providing visibility into what response the endpoint actually sent will offer a nice developer experience when they're tasked with debugging a webhook integration.

Rather than dig through logs, they can look at their recent failed webhook events.

Let's go ahead and generate a new migration for that:
    
    
    $ rails g migration AddResponseToWebhookEvents
    
    $ rails g migration AddResponseToWebhookEvents
    _content_copy_

And we'll add a new `jsonb` column to our webhook events called `response`:
    
    
    class AddResponseToWebhookEvents < ActiveRecord::Migration[5.2]
    
      def change
    
        add_column :webhook_events, :response, :jsonb, default: {}
    
      end
    
    end
    
    class AddResponseToWebhookEvents < ActiveRecord::Migration[5.2]
      def change
        add_column :webhook_events, :response, :jsonb, default: {}
      end
    end
    _content_copy_

Now let's adjust our worker to store the response object, both for typical responses as well as for newly discovered timeout errors:
    
    
    def perform(webhook_event_id)
    
      webhook_event = WebhookEvent.find_by(id: webhook_event_id)
    
      return if
    
        webhook_event.nil?
    
     
    
      webhook_endpoint = webhook_event.webhook_endpoint
    
      return if
    
        webhook_endpoint.nil?
    
     
    
      # Send the webhook request with a 30 second timeout.
    
      response = HTTP.timeout(30)
    
                     .headers(
    
                       'User-Agent' => 'rails_webhook_system/1.0',
    
                       'Content-Type' => 'application/json',
    
                     )
    
                     .post(
    
                       webhook_endpoint.url,
    
                       body: {
    
                         event: webhook_event.event,
    
                         payload: webhook_event.payload,
    
                       }.to_json
    
                     )
    
     
    
      # Store the webhook response.
    
      webhook_event.update(response: {
    
        headers: response.headers.to_h,
    
        code: response.code.to_i,
    
        body: response.body.to_s,
    
      })
    
     
    
      # Raise a failed request error and let Sidekiq handle retrying.
    
      raise FailedRequestError unless
    
        response.status.success?
    
    rescue HTTP::TimeoutError
    
      # This error means the webhook endpoint timed out. We can either
    
      # raise a failed request error to trigger a retry, or leave it
    
      # as-is and consider timeouts terminal. We'll do the latter.
    
      webhook_event.update(response: { error: 'TIMEOUT_ERROR' })
    
    end
    
    def perform(webhook_event_id)
      webhook_event = WebhookEvent.find_by(id: webhook_event_id)
      return if
        webhook_event.nil?
    
      webhook_endpoint = webhook_event.webhook_endpoint
      return if
        webhook_endpoint.nil?
    
      # Send the webhook request with a 30 second timeout.
      response = HTTP.timeout(30)
                     .headers(
                       'User-Agent' => 'rails_webhook_system/1.0',
                       'Content-Type' => 'application/json',
                     )
                     .post(
                       webhook_endpoint.url,
                       body: {
                         event: webhook_event.event,
                         payload: webhook_event.payload,
                       }.to_json
                     )
    
      # Store the webhook response.
      webhook_event.update(response: {
        headers: response.headers.to_h,
        code: response.code.to_i,
        body: response.body.to_s,
      })
    
      # Raise a failed request error and let Sidekiq handle retrying.
      raise FailedRequestError unless
        response.status.success?
    rescue HTTP::TimeoutError
      # This error means the webhook endpoint timed out. We can either
      # raise a failed request error to trigger a retry, or leave it
      # as-is and consider timeouts terminal. We'll do the latter.
      webhook_event.update(response: { error: 'TIMEOUT_ERROR' })
    end
    _content_copy_

Okay, now that we've (hopefully) handled timeouts, let's try delivering the event again:
    
    
    $ rails c
    
    > WebhookWorker.new.perform(WebhookEvent.last.id)
    
    # => true
    
    > WebhookEvent.last.response
    
    # => { "error" => "TIMEOUT_ERROR" }
    
    $ rails c
    > WebhookWorker.new.perform(WebhookEvent.last.id)
    # => true
    > WebhookEvent.last.response
    # => { "error" => "TIMEOUT_ERROR" }
    _content_copy_

Nice! As you can see, our `response` column now says there was a timeout error. We obviously don't want to continue using `ecorp.example` as our test server, so let's update our endpoint to something else, say, a Rails server on port `3000`.

In a new terminal pane, let's start up our Rails server:
    
    
    rails s
    
    rails s
    _content_copy_

Then let's update our endpoint:
    
    
    $ rails c
    
    > WebhookEndpoint.last.update!(url: 'http://localhost:3000/webhooks')
    
    # => true
    
    $ rails c
    > WebhookEndpoint.last.update!(url: 'http://localhost:3000/webhooks')
    # => true
    _content_copy_

Lastly, let's kick off a new webhook worker:
    
    
    $ rails c
    
    > WebhookWorker.new.perform(WebhookEvent.last.id)
    
    # => Traceback (most recent call last):
    
    #      2: from (irb):17
    
    #      1: from app/workers/webhook_worker.rb:76:in `perform'
    
    #    WebhookWorker::FailedRequestError (WebhookWorker::FailedRequestError)
    
    > WebhookEvent.last.response
    
    # => { "body" => "...", "code" => 404, "headers" => { ... } }
    
    $ rails c
    > WebhookWorker.new.perform(WebhookEvent.last.id)
    # => Traceback (most recent call last):
    #      2: from (irb):17
    #      1: from app/workers/webhook_worker.rb:76:in `perform'
    #    WebhookWorker::FailedRequestError (WebhookWorker::FailedRequestError)
    > WebhookEvent.last.response
    # => { "body" => "...", "code" => 404, "headers" => { ... } }
    _content_copy_

As we can see, the worker is (correctly) raising the failed request error for the `404` response, which will signal Sidekiq to automatically retry the job. And you should also see a line in your server logs indicating the `404`:
    
    
    ActionController::RoutingError (No route matches [POST] "/webhooks"):
    
    ActionController::RoutingError (No route matches [POST] "/webhooks"):
    _content_copy_

Now before we go any further, we need to adjust our webhook server to return a `204` response for the `/webhooks` route. To keep things simple, we'll add an inline `proc` handler that returns a basic Rack response.

Let's edit our `config/routes.rb` file with a new route:
    
    
     Rails.application.routes.draw do
    
    -  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html 
    
    +  post '/webhooks', to: proc { [204, {}, []] } 
    
     end
    
    Rails.application.routes.draw do
      # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html [tl! --]
      post '/webhooks', to: proc { [204, {}, []] } # [tl! ++]
    end
    _content_copy_

And then let's attempt to deliver the webhook one more time again:
    
    
    $ rails c
    
    > WebhookWorker.new.perform(WebhookEvent.last.id)
    
    # => nil
    
    > WebhookEvent.last.response
    
    # => { "body" => "", "code" => 204, "headers" => { ... } }
    
    $ rails c
    > WebhookWorker.new.perform(WebhookEvent.last.id)
    # => nil
    > WebhookEvent.last.response
    # => { "body" => "", "code" => 204, "headers" => { ... } }
    _content_copy_

Note the lack of a failed request error, and our status code is `204`. We should also see a log line in our Rails server logs indicating the request was sent:
    
    
    Started POST "/webhooks" for ::1 at 2021-06-15 10:04:34 -0500
    
    Started POST "/webhooks" for ::1 at 2021-06-15 10:04:34 -0500
    _content_copy_

## Broadcasting our webhook events

Now, creating webhook events and delivering them inline from the console is kind of cumbersome. We've also been sending the same event every time. Let's write a service object that helps streamline the process of broadcasting new events to our webhook endpoints.

Let's create a new `services` directory, and a file for our new service object:
    
    
    $ mkdir app/services
    
    $ touch app/services/broadcast_webhook_service.rb
    
    $ mkdir app/services
    $ touch app/services/broadcast_webhook_service.rb
    _content_copy_

Our service object is going to accept an `event` and a `payload`, and it will create a new webhook event for each endpoint and queue it up for delivery:
    
    
    class BroadcastWebhookService
    
      def self.call(event:, payload:)
    
        new(event: event, payload: payload).call
    
      end
    
     
    
      def call
    
        WebhookEndpoint.find_each do |webhook_endpoint|
    
          webhook_event = WebhookEvent.create!(
    
            webhook_endpoint: webhook_endpoint,
    
            event: event,
    
            payload: payload,
    
          )
    
     
    
          WebhookWorker.perform_async(webhook_event.id)
    
        end
    
      end
    
     
    
      private
    
     
    
      attr_reader :event, :payload
    
     
    
      def initialize(event:, payload:)
    
        @event   = event
    
        @payload = payload
    
      end
    
    end
    
    class BroadcastWebhookService
      def self.call(event:, payload:)
        new(event: event, payload: payload).call
      end
    
      def call
        WebhookEndpoint.find_each do |webhook_endpoint|
          webhook_event = WebhookEvent.create!(
            webhook_endpoint: webhook_endpoint,
            event: event,
            payload: payload,
          )
    
          WebhookWorker.perform_async(webhook_event.id)
        end
      end
    
      private
    
      attr_reader :event, :payload
    
      def initialize(event:, payload:)
        @event   = event
        @payload = payload
      end
    end
    _content_copy_

In the real world, this service may only want to broadcast events to endpoints belonging to specific users, for example if your app is multi-tenant. But right now, we aren't going to worry about that sort of detail.

Let's test the service out in our console:
    
    
    $ rails c
    
    > WebhookEvent.delete_all
    
    # => 1
    
    > BroadcastWebhookService.call(event: 'events.test', payload: { test: 2 })
    
    # => nil
    
    > WebhookEvent.last
    
    # => #<WebhookEvent
    
    #       id: 2,
    
    #       webhook_endpoint_id: 1,
    
    #       event: "events.test",
    
    #       payload: { "test" => 2 },
    
    #       created_at: "2021-06-15 15:43:21.767801000 +0000",
    
    #       updated_at: "2021-06-15 15:43:21.767801000 +0000",
    
    #       response: {}
    
    #     >
    
    $ rails c
    > WebhookEvent.delete_all
    # => 1
    > BroadcastWebhookService.call(event: 'events.test', payload: { test: 2 })
    # => nil
    > WebhookEvent.last
    # => #<WebhookEvent
    #       id: 2,
    #       webhook_endpoint_id: 1,
    #       event: "events.test",
    #       payload: { "test" => 2 },
    #       created_at: "2021-06-15 15:43:21.767801000 +0000",
    #       updated_at: "2021-06-15 15:43:21.767801000 +0000",
    #       response: {}
    #     >
    _content_copy_

Curious â `response` is empty, and we don't see any request logs for our Rails server. What gives? Well, we queued up the webhook worker, but we're no longer processing it inline. We'll need to boot up a Sidekiq process and let our workers work.

In a new terminal pane:
    
    
    $ sidekiq
    
    $ sidekiq
    _content_copy_

Then we can go back to our console session and check the last event:
    
    
    $ rails c
    
    > WebhookEvent.last
    
    # => #<WebhookEvent
    
    #       id: 2,
    
    #       webhook_endpoint_id: 2,
    
    #       event: "events.test",
    
    #       payload: { "test" => 2 },
    
    #       created_at: "2021-06-15 15:48:32.801960000 +0000",
    
    #       updated_at: "2021-06-15 15:48:32.810783000 +0000",
    
    #       response: {
    
    #         "body" => "",
    
    #         "code" => 204,
    
    #         "headers" => { ... }
    
    #       }
    
    #     >
    
    $ rails c
    > WebhookEvent.last
    # => #<WebhookEvent
    #       id: 2,
    #       webhook_endpoint_id: 2,
    #       event: "events.test",
    #       payload: { "test" => 2 },
    #       created_at: "2021-06-15 15:48:32.801960000 +0000",
    #       updated_at: "2021-06-15 15:48:32.810783000 +0000",
    #       response: {
    #         "body" => "",
    #         "code" => 204,
    #         "headers" => { ... }
    #       }
    #     >
    _content_copy_

The event was delivered successfully, as indicated by the `204` response.

## Subscribing to certain events

As your list of event types grows, your users are likely to only care about a handful of them. For example, our API service sends over 60 different event types, but we've found that each customer on average only listens to about 5 of them (which 5 depends on the licensing and billing model for the given business).

Allowing users to subscribe to only the events they need lets us:

  1. Reduces our costs by not queueing up and delivering superfluous webhooks.
  2. Reduces their costs by not spamming webhooks they don't need.



It's a win-win.

Let's update our webhook endpoints to be able to subscribe to certain events. To start, let's add a new `subscriptions` column to our webhook endpoints:
    
    
    $ rails g migration AddSubscriptionsToWebhookEndpoints
    
    $ rails g migration AddSubscriptionsToWebhookEndpoints
    _content_copy_

Then we'll throw this into the migration file:
    
    
    class AddSubscriptionsToWebhookEndpoints < ActiveRecord::Migration[5.2]
    
      def change
    
        add_column :webhook_endpoints, :subscriptions, :jsonb, default: ['*']
    
      end
    
    end
    
    class AddSubscriptionsToWebhookEndpoints < ActiveRecord::Migration[5.2]
      def change
        add_column :webhook_endpoints, :subscriptions, :jsonb, default: ['*']
      end
    end
    _content_copy_

Note the default `*` wildcard value. We're going to use that to signal that the endpoint will subscribe to all event types. Rare for production, useful for development.

Let's run the migration:
    
    
    $ rails db:migrate
    
    $ rails db:migrate
    _content_copy_

And then let's update our webhook endpoint model to require at least 1 subscription, and also add a helper method to the model for checking if a given endpoint is subscribed to an event type. We'll use this throughout our webhook system.
    
    
     class WebhookEndpoint < ApplicationRecord
    
       has_many :webhook_events, inverse_of: :webhook_endpoint
    
      
    
    +  validates :subscriptions, length: { minimum: 1 }, presence: true 
    
       validates :url, presence: true
    
    + 
    
    +  def subscribed?(event) 
    
    +    (subscriptions & ['*', event]).any? 
    
    +  end 
    
     end
    
    class WebhookEndpoint < ApplicationRecord
      has_many :webhook_events, inverse_of: :webhook_endpoint
    
      validates :subscriptions, length: { minimum: 1 }, presence: true # [tl! ++]
      validates :url, presence: true
      # [tl! ++]
      def subscribed?(event) # [tl! ++]
        (subscriptions & ['*', event]).any? # [tl! ++]
      end # [tl! ++]
    end
    _content_copy_

We can test this out by updating our endpoint's subscriptions:
    
    
    $ rails c
    
    > WebhookEndpoint.last.subscriptions
    
    # => ["*"]
    
    > WebhookEndpoint.last.subscribed?('events.noop')
    
    # => true
    
    > WebhookEndpoint.last.subscribed?('events.test')
    
    # => true
    
    > WebhookEndpoint.last.update!(subscriptions: ['events.test'])
    
    # => true
    
    > WebhookEndpoint.last.subscribed?('events.noop')
    
    # => false
    
    > WebhookEndpoint.last.subscribed?('events.test')
    
    # => true
    
    $ rails c
    > WebhookEndpoint.last.subscriptions
    # => ["*"]
    > WebhookEndpoint.last.subscribed?('events.noop')
    # => true
    > WebhookEndpoint.last.subscribed?('events.test')
    # => true
    > WebhookEndpoint.last.update!(subscriptions: ['events.test'])
    # => true
    > WebhookEndpoint.last.subscribed?('events.noop')
    # => false
    > WebhookEndpoint.last.subscribed?('events.test')
    # => true
    _content_copy_

Next, we'll adjust our service object to skip over endpoints that are not subscribed to the current event being broadcast:
    
    
     def call
    
       WebhookEndpoint.find_each do |webhook_endpoint|
    
    +    next unless 
    
    +      webhook_endpoint.subscribed?(event) 
    
    + 
    
         webhook_event = WebhookEvent.create!(
    
           webhook_endpoint: webhook_endpoint,
    
           event: event,
    
           payload: payload,
    
         )
    
      
    
         WebhookWorker.perform_async(webhook_event.id)
    
       end
    
     end
    
    def call
      WebhookEndpoint.find_each do |webhook_endpoint|
        next unless # [tl! ++]
          webhook_endpoint.subscribed?(event) # [tl! ++]
        # [tl! ++]
        webhook_event = WebhookEvent.create!(
          webhook_endpoint: webhook_endpoint,
          event: event,
          payload: payload,
        )
    
        WebhookWorker.perform_async(webhook_event.id)
      end
    end
    _content_copy_

Lastly, we'll also want to update our worker to do the same, just in case a webhook is in the process of being delivered but the user has since unsubscribed to that event.

For example, if a given event is particularly noisy, it may cause performance issues for the end-user's webhook server and they may want to retroactively unsubscribe from the noisy event. (For instance, our `license.validation.*` events can get pretty noisy depending on the licensing integration.)

Let's adjust our webhook worker to skip over event types that the webhook endpoint is no longer subscribed to:
    
    
     def perform(webhook_event_id)
    
       webhook_event = WebhookEvent.find_by(id: webhook_event_id)
    
       return if
    
         webhook_event.nil?
    
      
    
       webhook_endpoint = webhook_event.webhook_endpoint
    
       return if
    
         webhook_endpoint.nil?
    
    + 
    
    +  return unless 
    
    +    webhook_endpoint.subscribed?(webhook_event.event) 
    
      
    
       # Send the webhook request with a 30 second timeout.
    
       response = HTTP.timeout(30)
    
                      .headers(
    
                        'User-Agent' => 'rails_webhook_system/1.0',
    
                        'Content-Type' => 'application/json',
    
                      )
    
                      .post(
    
                        webhook_endpoint.url,
    
                        body: {
    
                          event: webhook_event.event,
    
                          payload: webhook_event.payload,
    
                        }.to_json
    
                      )
    
      
    
       # Store the webhook response.
    
       webhook_event.update(response: {
    
         headers: response.headers.to_h,
    
         code: response.code.to_i,
    
         body: response.body.to_s,
    
       })
    
      
    
       # Raise a failed request error and let Sidekiq handle retrying.
    
       raise FailedRequestError unless
    
         response.status.success?
    
     rescue HTTP::TimeoutError
    
     # This error means the webhook endpoint timed out. We can either
    
       # raise a failed request error to trigger a retry, or leave it
    
       # as-is and consider timeouts terminal. We'll do the latter.
    
       webhook_event.update(response: { error: 'TIMEOUT_ERROR' })
    
     end
    
    def perform(webhook_event_id)
      webhook_event = WebhookEvent.find_by(id: webhook_event_id)
      return if
        webhook_event.nil?
    
      webhook_endpoint = webhook_event.webhook_endpoint
      return if
        webhook_endpoint.nil?
      # [tl! ++]
      return unless # [tl! ++]
        webhook_endpoint.subscribed?(webhook_event.event) # [tl! ++]
    
      # Send the webhook request with a 30 second timeout.
      response = HTTP.timeout(30)
                     .headers(
                       'User-Agent' => 'rails_webhook_system/1.0',
                       'Content-Type' => 'application/json',
                     )
                     .post(
                       webhook_endpoint.url,
                       body: {
                         event: webhook_event.event,
                         payload: webhook_event.payload,
                       }.to_json
                     )
    
      # Store the webhook response.
      webhook_event.update(response: {
        headers: response.headers.to_h,
        code: response.code.to_i,
        body: response.body.to_s,
      })
    
      # Raise a failed request error and let Sidekiq handle retrying.
      raise FailedRequestError unless
        response.status.success?
    rescue HTTP::TimeoutError
    # This error means the webhook endpoint timed out. We can either
      # raise a failed request error to trigger a retry, or leave it
      # as-is and consider timeouts terminal. We'll do the latter.
      webhook_event.update(response: { error: 'TIMEOUT_ERROR' })
    end
    _content_copy_

We can once again test this out by queueing up a new event that our endpoint isn't subscribed to. Let's do this from the console:
    
    
    $ rails c
    
    > WebhookEvent.count
    
    # => 2
    
    > BroadcastWebhookService.call(event: 'events.noop', payload: { test: 3 })
    
    # => nil
    
    > WebhookEvent.count
    
    # => 2
    
    $ rails c
    > WebhookEvent.count
    # => 2
    > BroadcastWebhookService.call(event: 'events.noop', payload: { test: 3 })
    # => nil
    > WebhookEvent.count
    # => 2
    _content_copy_

## Improving our retry cadence

Right now, we're using Sidekiq's default retry cadence, which is an exponential backoff. This is great for normal background jobs, but in our case, potentially retrying seconds after a failed webhook usually just exacerbates the problem. Sidekiq's default retry cadence is `retry_count ** 4`, which starts small and _eventually_ gets large.

For example, if a webhook server is timing out because of too many requests, retrying all of them in quick succession until the backoff grows large enough isn't going to help the situation. We can alleviate that risk by adding in a little bit of "jitter" into the retry cadence and increasing the exponent from `4` to `5`:
    
    
     class WebhookWorker
    
       include Sidekiq::Worker
    
    + 
    
    +  sidekiq_retry_in do |retry_count| 
    
    +    # Exponential backoff, with a random 30-second to 10-minute "jitter"   
    
    +    # added in to help spread out any webhook "bursts."                    
    
    +    jitter = rand(30.seconds..10.minutes).to_i 
    
    + 
    
    +    (retry_count ** 5) + jitter 
    
    +  end 
    
      
    
       def perform(webhook_event_id)
    
         ...
    
       end
    
     end
    
    class WebhookWorker
      include Sidekiq::Worker
      # [tl! ++]
      sidekiq_retry_in do |retry_count| # [tl! ++]
        # Exponential backoff, with a random 30-second to 10-minute "jitter"   [tl! ++]
        # added in to help spread out any webhook "bursts."                    [tl! ++]
        jitter = rand(30.seconds..10.minutes).to_i # [tl! ++]
        # [tl! ++]
        (retry_count ** 5) + jitter # [tl! ++]
      end # [tl! ++]
    
      def perform(webhook_event_id)
        ...
      end
    end
    _content_copy_

This should do a couple things:

  1. Reduce occurrences of instantaneous retries, reducing the chance of us exacerbating any issues with the webhook server.
  2. Help space out sudden large bursts of failing webhooks by using a random jitter between 30 seconds and 10 minutes.



One other thing we can also do is limit the amount of times a webhook will retry:
    
    
     class WebhookWorker
    
       include Sidekiq::Worker
    
      
    
    +  sidekiq_options retry: 10, dead: false 
    
       sidekiq_retry_in do |retry_count|
    
         # Exponential backoff, with a random 30-second to 10-minute "jitter"
    
         # added in to help spread out any webhook "bursts."
    
         jitter = rand(30.seconds..10.minutes).to_i
    
      
    
         (retry_count ** 5) + jitter
    
       end
    
      
    
       def perform(webhook_event_id)
    
         ...
    
       end
    
     end
    
    class WebhookWorker
      include Sidekiq::Worker
    
      sidekiq_options retry: 10, dead: false # [tl! ++]
      sidekiq_retry_in do |retry_count|
        # Exponential backoff, with a random 30-second to 10-minute "jitter"
        # added in to help spread out any webhook "bursts."
        jitter = rand(30.seconds..10.minutes).to_i
    
        (retry_count ** 5) + jitter
      end
    
      def perform(webhook_event_id)
        ...
      end
    end
    _content_copy_

Here we've set the maximum number of retries to `10`, and we've also told Sidekiq to not store these failed webhooks in its set of "dead" jobs. We don't care about dead webhook jobs. With our retry exponent of `5` and a maximum retry limit of `10`, retries should occur over approximately 3 days:
    
    
    $ rails c
    
    > include ActionView::Helpers::DateHelper
    
    > total = 0.0
    
    > 10.times { |i| total += ((i + 1) ** 5) + rand(30.seconds..10.minutes) }
    
    > distance_of_time_in_words(total)
    
    # => "3 days"
    
    $ rails c
    > include ActionView::Helpers::DateHelper
    > total = 0.0
    > 10.times { |i| total += ((i + 1) ** 5) + rand(30.seconds..10.minutes) }
    > distance_of_time_in_words(total)
    # => "3 days"
    _content_copy_

The exponent and retry limit can be increased to spread the retries out over a longer duration. (The values can also be decreased, of course.)

## Disabling our webhook endpoints

Another great feature to have is being able to disable webhook endpoints. This could come in handy for us when we want to disable a problem endpoint, but not delete it (so that the problem can be resolved by the endpoint owner.) This feature can also come in handy for our users, by allowing them to keep certain webhook endpoints on-hand, but only have them enabled when they need them.

To accomplish this, we'll want to add a new `enabled` column to our webhook endpoints:

(There's a relatively wide changeset here â we're touching a lot of files.)
    
    
    $ rails g migration AddEnabledToWebhookEndpoints
    
    $ rails g migration AddEnabledToWebhookEndpoints
    _content_copy_

And then within the migration, we'll want to have this:
    
    
    class AddEnabledToWebhookEndpoints < ActiveRecord::Migration[5.2]
    
      def change
    
        add_column :webhook_endpoints, :enabled, :boolean,
    
          default: true,
    
          index: true
    
      end
    
    end
    
    class AddEnabledToWebhookEndpoints < ActiveRecord::Migration[5.2]
      def change
        add_column :webhook_endpoints, :enabled, :boolean,
          default: true,
          index: true
      end
    end
    _content_copy_

And we'll want to run the migration:
    
    
    $ rails db:migrate
    
    $ rails db:migrate
    _content_copy_

Next, we'll want to update the webhook endpoint model to have an `enabled` scope, and we'll also add a bang-method to `disable!` a webhook endpoint:
    
    
     class WebhookEndpoint < ApplicationRecord
    
       has_many :webhook_events, inverse_of: :webhook_endpoint
    
      
    
       validates :subscriptions, length: { minimum: 1 }, presence: true
    
       validates :url, presence: true
    
    + 
    
    +  scope :enabled, -> { where(enabled: true) } 
    
      
    
       def subscribed?(event)
    
        (subscriptions & ['*', event]).any?
    
       end
    
    + 
    
    +  def disable! 
    
    +    update!(enabled: false) 
    
    +  end 
    
     end
    
    class WebhookEndpoint < ApplicationRecord
      has_many :webhook_events, inverse_of: :webhook_endpoint
    
      validates :subscriptions, length: { minimum: 1 }, presence: true
      validates :url, presence: true
      # [tl! ++]
      scope :enabled, -> { where(enabled: true) } # [tl! ++]
    
      def subscribed?(event)
       (subscriptions & ['*', event]).any?
      end
      # [tl! ++]
      def disable! # [tl! ++]
        update!(enabled: false) # [tl! ++]
      end # [tl! ++]
    end
    _content_copy_

Next, the broadcast webhook service needs to utilize the new `enabled` scope so that we only broadcast events to endpoints that are enabled:
    
    
     def call
    
    -  WebhookEndpoint.find_each do |webhook_endpoint| 
    
    +  WebhookEndpoint.enabled.find_each do |webhook_endpoint| 
    
         ...
    
       end
    
     end
    
    def call
      WebhookEndpoint.find_each do |webhook_endpoint| # [tl! --]
      WebhookEndpoint.enabled.find_each do |webhook_endpoint| # [tl! ++]
        ...
      end
    end
    _content_copy_

Finally, we'll update the webhook worker to bail early if the endpoint is disabled:
    
    
     def perform(webhook_event_id)
    
       ...
    
       return unless
    
    -    webhook_endpoint.subscribed?(webhook_event.event) 
    
    +    webhook_endpoint.subscribed?(webhook_event.event) && 
    
    +    webhook_endpoint.enabled? 
    
       ...
    
     end
    
    def perform(webhook_event_id)
      ...
      return unless
        webhook_endpoint.subscribed?(webhook_event.event) # [tl! --]
        webhook_endpoint.subscribed?(webhook_event.event) && # [tl! ++]
        webhook_endpoint.enabled? # [tl! ++]
      ...
    end
    _content_copy_

If we go ahead and disable our endpoint and then broadcast a new event, we shouldn't see a webhook delivery occur:
    
    
    $ rails c
    
    > WebhookEndpoint.last.update!(enabled: false)
    
    # => true
    
    > WebhookEvent.count
    
    # => 2
    
    > BroadcastWebhookService.call(event: 'events.test', payload: { test: 4 })
    
    # => nil
    
    > WebhookEvent.count
    
    # => 2
    
    $ rails c
    > WebhookEndpoint.last.update!(enabled: false)
    # => true
    > WebhookEvent.count
    # => 2
    > BroadcastWebhookService.call(event: 'events.test', payload: { test: 4 })
    # => nil
    > WebhookEvent.count
    # => 2
    _content_copy_

If we had a failed webhook event being retried, and then we disabled the event's endpoint, the worker should stop attempting to retry. We aren't going to test that scenario, but it should be covered by the changeset here.

## Improving our error handling

When it comes to sending webhooks, there are a plethora of errors that can occur. From DNS issues, to TLS issues, to an [ngrok](https://ngrok.com) tunnel no longer being active, to various type of timeouts and connection errors.

For now, we're going to handle the first 2: DNS and TLS issues.

Let's adjust our worker to rescue from a couple error classes:

  1. `OpenSSL::SSL::SSLError` â this means the TLS connection failed, often due to an expired cert. In my experience, these are often short-lived and resolve within the 3 day delivery window that we've configured for retries.
  2. `HTTP::ConnectionError` â this is a general "catch-all" from `http.rb`. From my experience it usually means DNS, but it's kind of nuanced.


    
    
    def perform(webhook_event_id)
    
      ...
    
    rescue OpenSSL::SSL::SSLError
    
      # Since TLS issues may be due to an expired cert, we'll continue retrying
    
      # since the issue may get resolved within the 3 day retry window. This
    
      # may be a good place to send an alert to the endpoint owner.
    
      webhook_event.update(response: { error: 'TLS_ERROR' })
    
     
    
      # Signal the webhook for retry.
    
      raise FailedRequestError
    
    rescue HTTP::ConnectionError
    
      # This error usually means DNS issues. To save us the bandwidth,
    
      # we're going to disable the endpoint. This would also be a good
    
      # location to send an alert to the endpoint owner.
    
      webhook_event.update(response: { error: 'CONNECTION_ERROR' })
    
     
    
      # Disable the problem endpoint.
    
      webhook_endpoint.disable!
    
    rescue HTTP::TimeoutError
    
      # This error means the webhook endpoint timed out. We can either
    
      # raise a failed request error to trigger a retry, or leave it
    
      # as-is and consider timeouts terminal. We'll do the latter.
    
      webhook_event.update(response: { error: 'TIMEOUT_ERROR' })
    
    end
    
    def perform(webhook_event_id)
      ...
    rescue OpenSSL::SSL::SSLError
      # Since TLS issues may be due to an expired cert, we'll continue retrying
      # since the issue may get resolved within the 3 day retry window. This
      # may be a good place to send an alert to the endpoint owner.
      webhook_event.update(response: { error: 'TLS_ERROR' })
    
      # Signal the webhook for retry.
      raise FailedRequestError
    rescue HTTP::ConnectionError
      # This error usually means DNS issues. To save us the bandwidth,
      # we're going to disable the endpoint. This would also be a good
      # location to send an alert to the endpoint owner.
      webhook_event.update(response: { error: 'CONNECTION_ERROR' })
    
      # Disable the problem endpoint.
      webhook_endpoint.disable!
    rescue HTTP::TimeoutError
      # This error means the webhook endpoint timed out. We can either
      # raise a failed request error to trigger a retry, or leave it
      # as-is and consider timeouts terminal. We'll do the latter.
      webhook_event.update(response: { error: 'TIMEOUT_ERROR' })
    end
    _content_copy_

How we handle each of these errors ends up being pretty arbitrary. I just chose these to exemplify how to handle a few different scenarios:

  1. Retrying the webhook after an error occurs
  2. Disabling an endpoint after a fatal error
  3. Not retrying after an error



## Using pattern matching for special cases

I mentioned [ngrok](https://ngrok.com) earlier and I wanted to share some information on how you could use Ruby's new [pattern matching](https://docs.ruby-lang.org/en/3.0.0/doc/syntax/pattern_matching_rdoc.html) to handle certain response patterns differently. We'll be applying this to ngrok specifically, but you could use the same logic to match against other types of responses as well.

Take an example â when an ngrok user creates a tunnel to a local server, and then adds that URL as a webhook endpoint, often times the tunnel session will be killed at the end of the day, but the webhook endpoint will still be enabled. I've found this to be a common occurrence with various localhost tunnel services.

One way we can handle these ngrok tunnels is by using pattern matching to match against certain response codes and response bodies from ngrok endpoints.

There are 3 scenarios for ngrok endpoints that we're going to cover today:

  1. When an ngrok URL no longer exists. This will return a `404` response code. We'll handle this by completely deleting the endpoint, since non-stable URLs are randomly generated and cannot be recreated.
  2. When an ngrok URL is active, but the server being tunneled to is no longer running. This will return a `502` and usually occurs when the developer kills their local server at the end of a work day, but forgets to kill the ngrok session. We'll keep retrying this one, since the ngrok process records the events which can be replayed later on.
  3. When a ["stable" ngrok URL](https://ngrok.com/docs#getting-started-stable) is valid but there is no active tunnel session. This will return a `504`. We'll automatically disable this endpoint.



Let's modify our webhook worker to be able to handle these scenarios:
    
    
    def perform(webhook_event_id)
    
      ...
    
     
    
      # Exit early if the webhook was successful.
    
      return if
    
        response.status.success?
    
     
    
      # Handle response errors.
    
      case webhook_event
    
      in webhook_endpoint: { url: /\.ngrok\.io/ },
    
         response: { code: 404, body: /tunnel .+?\.ngrok\.io not found/i }
    
        # Automatically delete dead ngrok tunnel endpoints. This error likely
    
        # means that the developer forgot to remove their temporary ngrok
    
        # webhook endpoint, seeing as it no longer exists.
    
        webhook_endpoint.destroy!
    
      in webhook_endpoint: { url: /\.ngrok\.io/ },
    
         response: { code: 502 }
    
        # The bad gateway error usually means that the tunnel is still open
    
        # but the local server is no longer responding for any number of
    
        # reasons. We're going to automatically retry.
    
        raise FailedRequestError
    
      in webhook_endpoint: { url: /\.ngrok\.io/ },
    
         response: { code: 504 }
    
        # Automatically disable these since the endpoint is likely an ngrok
    
        # "stable" URL, but it's not currently running. To save bandwidth,
    
        # we do not want to automatically retry.
    
        webhook_endpoint.disable!
    
      else
    
        # Raise a failed request error and let Sidekiq handle retrying.
    
        raise FailedRequestError
    
      end
    
     
    
      ...
    
    end
    
    def perform(webhook_event_id)
      ...
    
      # Exit early if the webhook was successful.
      return if
        response.status.success?
    
      # Handle response errors.
      case webhook_event
      in webhook_endpoint: { url: /\.ngrok\.io/ },
         response: { code: 404, body: /tunnel .+?\.ngrok\.io not found/i }
        # Automatically delete dead ngrok tunnel endpoints. This error likely
        # means that the developer forgot to remove their temporary ngrok
        # webhook endpoint, seeing as it no longer exists.
        webhook_endpoint.destroy!
      in webhook_endpoint: { url: /\.ngrok\.io/ },
         response: { code: 502 }
        # The bad gateway error usually means that the tunnel is still open
        # but the local server is no longer responding for any number of
        # reasons. We're going to automatically retry.
        raise FailedRequestError
      in webhook_endpoint: { url: /\.ngrok\.io/ },
         response: { code: 504 }
        # Automatically disable these since the endpoint is likely an ngrok
        # "stable" URL, but it's not currently running. To save bandwidth,
        # we do not want to automatically retry.
        webhook_endpoint.disable!
      else
        # Raise a failed request error and let Sidekiq handle retrying.
        raise FailedRequestError
      end
    
      ...
    end
    _content_copy_

Now to actually be able to pattern match against our webhook event model, we'll need to add a `deconstruct_keys` method:
    
    
     class WebhookEvent < ApplicationRecord
    
       belongs_to :webhook_endpoint, inverse_of: :webhook_events
    
      
    
       validates :event, presence: true
    
       validates :payload, presence: true
    
      
    
    +  def deconstruct_keys(keys) 
    
    +    { 
    
    +      webhook_endpoint: { url: webhook_endpoint.url }, 
    
    +      event: event, 
    
    +      payload: payload, 
    
    +      response: response.symbolize_keys, 
    
    +    } 
    
    +  end 
    
     end
    
    class WebhookEvent < ApplicationRecord
      belongs_to :webhook_endpoint, inverse_of: :webhook_events
    
      validates :event, presence: true
      validates :payload, presence: true
    
      def deconstruct_keys(keys) # [tl! ++]
        { # [tl! ++]
          webhook_endpoint: { url: webhook_endpoint.url }, # [tl! ++]
          event: event, # [tl! ++]
          payload: payload, # [tl! ++]
          response: response.symbolize_keys, # [tl! ++]
        } # [tl! ++]
      end # [tl! ++]
    end
    _content_copy_

This will allow us to match against the hash pattern we define. In our case, we're surfacing the `webhook_endpoint`, `event`, `payload` and the `response` object.

We can test these scenarios by creating an ngrok tunnel to our local Rails server:
    
    
    $ ngrok http 3000
    
    $ ngrok http 3000
    _content_copy_

Then we can update our webhook endpoint to use the generated ngrok URL:
    
    
    $ rails c
    
    > WebhookEndpoint.last.update!(
    
        url: 'https://349df8f512ea.ngrok.io/webhooks'
    
      )
    
    # => true
    
    $ rails c
    > WebhookEndpoint.last.update!(
        url: 'https://349df8f512ea.ngrok.io/webhooks'
      )
    # => true
    _content_copy_

Next, we can queue up a new webhook event to send:
    
    
    $ rails c
    
    > BroadcastWebhookService.call(event: 'events.test', payload: { test: 5 })
    
    # => nil
    
    > WebhookEvent.last.response
    
    # => { "body" => "", "code" => 204, "headers" => { ... } }
    
    $ rails c
    > BroadcastWebhookService.call(event: 'events.test', payload: { test: 5 })
    # => nil
    > WebhookEvent.last.response
    # => { "body" => "", "code" => 204, "headers" => { ... } }
    _content_copy_

Looking at our ngrok logs, we see a `204` status code for that webhook. Now, let's kill our ngrok process and send another event:
    
    
    $ rails c
    
    > WebhookEndpoint.count
    
    # => 1
    
    > BroadcastWebhookService.call(event: 'events.test', payload: { test: 6 })
    
    # => nil
    
    > WebhookEndpoint.count
    
    # => 0
    
    $ rails c
    > WebhookEndpoint.count
    # => 1
    > BroadcastWebhookService.call(event: 'events.test', payload: { test: 6 })
    # => nil
    > WebhookEndpoint.count
    # => 0
    _content_copy_

Using pattern matching, our worker (correctly) determined that the bad ngrok webhook endpoint should be deleted, since it's now returning a `404`.

Similarly, we can test the other scenarios, for example by keeping the ngrok session active but killing the local Rails server process. But I'll leave that as an exercise for the curious reader.

## Caveats and summary

Today, we've covered how to build a webhook system using Rails and Sidekiq. We've learned how we can rely on Sidekiq to do the heavy-lifting for us, and then we broke out Ruby's new pattern matching syntax for some special-case response handling.

So what's next? Here are things to try and look out for:

  * Assert that webhook endpoints are non-malicious (one big thing to assert is that they are not pointing to the system itself!)
  * Assert that webhook endpoints use TLS.
  * Assert that webhook jobs are unique (see [Sidekiq Pro](https://sidekiq.org/products/pro.html)'s unique jobs feature, or the `sidekiq-unique-jobs` gem.)
  * Assert that the webhook event `response` is not too large. (Some endpoints will try to send you the entire Internet to store.)
  * Add the ability to manually retry events.
  * Add better error handling.
  * Add logging (!)



You can view [the full example app](https://github.com/ezekg/example-rails-webhook-system) on GitHub.

Until next time.

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


