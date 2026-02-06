# How to Implement API Key Authentication in Rails Without Devise

**来源:** https://keygen.sh
**链接:** https://keygen.sh/blog/how-to-implement-api-key-authentication-in-rails-without-devise/
**日期:** Fri, 16 Apr 2021 05:00:00 GMT

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
    * [_support_ Get Support ](/cdn-cgi/l/email-protection#91e2e4e1e1fee3e5d1faf4e8f6f4ffbfe2f9)
  * [Pricing ](/pricing/)
  * [Log in ](https://app.keygen.sh/login)
  * [Sign Up](https://app.keygen.sh/register?plan=984180df-07b3-4dc1-b138-ca68a0f913ed)



# How to Implement API Key Authentication in Rails Without Devise

Friday, April 16th 2021

It's gotta be at least once a week that I see somebody on /r/rails or Stack Overflow asking how to implement API key authentication using Ruby on Rails. Most of the time they ask how to do it with the ubiquitous Devise gem, or the accepted answer points them in that direction. And everytime I think to myself, "why is everybody using Devise for something as simple as API key authentication?"

Devise was created to handle browser-based authentication via cookies for run-of-the-mill, non-API, Rails applications. Devise really shines in its simple and secure session management, ready-to-go view and mailer templates, and support for things like SSO and OAuth using OmniAuth.

But API's don't utilize sessions, or views. (Or at least they shouldn't!)

To make matters even more confusing â the Devise repo kind of seems like they don't even recommend using Devise for API-mode apps. Concerning Rails' API-mode, their README states "we still don't know the full extent of [API-mode] compatibility."

So why are people using and recommending Devise for APIs?

I think they're using Devise simply because they are unaware of how easy it is to implement API key authentication without Devise. When it comes to authentication, Ruby on Rails is a batteries-included framework.

Devise is over-kill for an API.

## Generating a new Rails API

To kick things off, let's create a new Rails API app:
    
    
    $ rails new . --api --database postgresql \
    
        --skip-active-storage \
    
        --skip-action-cable
    
    $ rails new . --api --database postgresql \
        --skip-active-storage \
        --skip-action-cable
    _content_copy_

Now that we have a new Rails app in API-mode, excluding a little bit of cruft that we don't need like Active Storage and Action Cable, let's move onto our models.

## Creating a user model

First up, we have our `User`. For that, we'll need a `users` table. Pretty standard stuff. Let's generate a migration:
    
    
    $ rails g migration CreateUsers
    
    $ rails g migration CreateUsers
    _content_copy_

We'll populate the migration with the following:
    
    
    class CreateUsers < ActiveRecord::Migration[5.2]
    
      def change
    
        create_table :users do |t|
    
          t.string :email, null: false
    
          t.string :password_digest, null: false
    
          t.timestamps null: false
    
        end
    
     
    
        add_index :users, :email, unique: true
    
      end
    
    end
    
    class CreateUsers < ActiveRecord::Migration[5.2]
      def change
        create_table :users do |t|
          t.string :email, null: false
          t.string :password_digest, null: false
          t.timestamps null: false
        end
    
        add_index :users, :email, unique: true
      end
    end
    _content_copy_

Then we'll apply it:
    
    
    $ rails db:migrate
    
    $ rails db:migrate
    _content_copy_

Lastly, we'll create the actual `User` model:
    
    
    class User < ApplicationRecord
    
      has_secure_password
    
    end
    
    class User < ApplicationRecord
      has_secure_password
    end
    _content_copy_

Simple enough. Rails has out-of-the-box support for user password authentication using the `has_secure_password` concern. I run across Rails devs all the time who don't know that, so I figured I'd mention it. Again, You Don't Need Deviseâ¢.

## Creating an API key model

Moving on, we'll need another model. An `ApiKey`. So let's go ahead and create the `api_keys` table as well as the model class.
    
    
    $ rails g migration CreateApiKeys
    
    $ rails g migration CreateApiKeys
    _content_copy_

Then fill it with the following:
    
    
    class CreateApiKeys < ActiveRecord::Migration[5.2]
    
      def change
    
        create_table :api_keys do |t|
    
          t.integer :bearer_id, null: false
    
          t.string :bearer_type, null: false
    
          t.string :token, null: false
    
          t.timestamps null: false
    
        end
    
     
    
        add_index :api_keys, [:bearer_id, :bearer_type]
    
        add_index :api_keys, :token, unique: true
    
      end
    
    end
    
    class CreateApiKeys < ActiveRecord::Migration[5.2]
      def change
        create_table :api_keys do |t|
          t.integer :bearer_id, null: false
          t.string :bearer_type, null: false
          t.string :token, null: false
          t.timestamps null: false
        end
    
        add_index :api_keys, [:bearer_id, :bearer_type]
        add_index :api_keys, :token, unique: true
      end
    end
    _content_copy_

Note the `bearer_id` and `bearer_type` columns, instead of a `user_id` column. We're going to be defining a polymorphic API key model, meaning not just a `User` can have an API key. We can get more into multiple "bearers" later, though.

Then we'll apply the migration:
    
    
    $ rails db:migrate
    
    $ rails db:migrate
    _content_copy_

Next, in the same vein as our user, we'll create the `ApiKey` model:
    
    
    class ApiKey < ApplicationRecord
    
      belongs_to :bearer, polymorphic: true
    
    end
    
    class ApiKey < ApplicationRecord
      belongs_to :bearer, polymorphic: true
    end
    _content_copy_

Lastly, we'll want to add the API key association to the user model.
    
    
     class User < ApplicationRecord
    
    +  has_many :api_keys, as: :bearer 
    
    + 
    
       has_secure_password
    
     end
    
    class User < ApplicationRecord
      has_many :api_keys, as: :bearer # [tl! ++]
      # [tl! ++]
      has_secure_password
    end
    _content_copy_

Again, note the `as: :bearer` option. This ensures that the user, at least from the API key's perspective, is referred to as the API key "bearer."

## Verifying our work

Alright â so we have our tables, a `User` model, and an `ApiKey` model. What's next? Well, I always like to test things as I go using the Rails console, so let's do that real quick before we dive too deep into things.
    
    
    $ rails c
    
    > User.create! email: '[[email protected]](/cdn-cgi/l/email-protection)', password: 'secret'
    
    # You don't have bcrypt installed in your application. Please add it to your Gemfile and run bundle install
    
    # Traceback (most recent call last):
    
    #         3: from (irb):3
    
    #         2: from app/models/user.rb:1:in `<main>'
    
    #         1: from app/models/user.rb:4:in `<class:User>'
    
    # LoadError (cannot load such file -- bcrypt)
    
    $ rails c
    > User.create! email: 'zeke@keygen.example', password: 'secret'
    # You don't have bcrypt installed in your application. Please add it to your Gemfile and run bundle install
    # Traceback (most recent call last):
    #         3: from (irb):3
    #         2: from app/models/user.rb:1:in `<main>'
    #         1: from app/models/user.rb:4:in `<class:User>'
    # LoadError (cannot load such file -- bcrypt)
    _content_copy_

Oops. It's been awhile since I created a new Rails app, so let's uncomment `bcrypt` from our Gemfile real quick, run Bundler, then try again.
    
    
    -# gem 'bcrypt', '~> 3.1.7' # 
    
    +gem 'bcrypt', '~> 3.1.7' 
    
    # gem 'bcrypt', '~> 3.1.7' # [tl! --]
    gem 'bcrypt', '~> 3.1.7' # [tl! ++]
    _content_copy_

Then run Bundler:
    
    
    $ bundle
    
    $ bundle
    _content_copy_

Now let's try that again:
    
    
    $ rails c
    
    > User.create! email: '[[email protected]](/cdn-cgi/l/email-protection)', password: 'secret'
    
    # => #<User id: 1, email: "[[email protected]](/cdn-cgi/l/email-protection)", password_digest: "$2a$10$RAR1bk.3VlusLgAg.tvEbOOI3govZfQg/Xibj0E/GYN...", created_at: "2021-04-16 13:45:30", updated_at: "2021-04-16 13:45:30">
    
    $ rails c
    > User.create! email: 'zeke@keygen.example', password: 'secret'
    # => #<User id: 1, email: "zeke@keygen.example", password_digest: "$2a$10$RAR1bk.3VlusLgAg.tvEbOOI3govZfQg/Xibj0E/GYN...", created_at: "2021-04-16 13:45:30", updated_at: "2021-04-16 13:45:30">
    _content_copy_

Perfection.

Let's go ahead and test a few more things, like user password authentication, and maybe we can even create a couple API keys, just for kicks.
    
    
    $ rails c
    
    > zeke = User.first
    
    > zeke.authenticate('secret')
    
    # => #<User id: 1, email: "[[email protected]](/cdn-cgi/l/email-protection)", password_digest: "$2a$10$RAR1bk.3VlusLgAg.tvEbOOI3govZfQg/Xibj0E/GYN...", created_at: "2021-04-16 13:45:30", updated_at: "2021-04-16 13:45:30">
    
    > zeke.authenticate('foo')
    
    # => false
    
    > zeke.api_keys
    
    # => #<ActiveRecord::Associations::CollectionProxy []>
    
    > zeke.api_keys.create! token: SecureRandom.hex
    
    # => #<ApiKey id: 1, bearer_id: 1, bearer_type: "User", token: "5c8e4327fd8b2bf3118f82b13890d89d", created_at: "2021-04-16 13:56:42", updated_at: "2021-04-16 13:56:42">
    
    > zeke.api_keys
    
    # => #<ActiveRecord::Associations::CollectionProxy [#<ApiKey id: 1, bearer_id: 1, bearer_type: "User", token: "5c8e4327fd8b2bf3118f82b13890d89d", created_at: "2021-04-16 13:56:42", updated_at: "2021-04-16 13:56:42">]>
    
    $ rails c
    > zeke = User.first
    > zeke.authenticate('secret')
    # => #<User id: 1, email: "zeke@keygen.example", password_digest: "$2a$10$RAR1bk.3VlusLgAg.tvEbOOI3govZfQg/Xibj0E/GYN...", created_at: "2021-04-16 13:45:30", updated_at: "2021-04-16 13:45:30">
    > zeke.authenticate('foo')
    # => false
    > zeke.api_keys
    # => #<ActiveRecord::Associations::CollectionProxy []>
    > zeke.api_keys.create! token: SecureRandom.hex
    # => #<ApiKey id: 1, bearer_id: 1, bearer_type: "User", token: "5c8e4327fd8b2bf3118f82b13890d89d", created_at: "2021-04-16 13:56:42", updated_at: "2021-04-16 13:56:42">
    > zeke.api_keys
    # => #<ActiveRecord::Associations::CollectionProxy [#<ApiKey id: 1, bearer_id: 1, bearer_type: "User", token: "5c8e4327fd8b2bf3118f82b13890d89d", created_at: "2021-04-16 13:56:42", updated_at: "2021-04-16 13:56:42">]>
    _content_copy_

Everything looks solid. What's next?

## The route to API key authentication

In this example, we're going to be defining 3 routes:

  1. `POST /api-keys`: to create a new API key i.e. a standard 'login'
  2. `DELETE /api-keys`: to revoke the current API key i.e. 'logout'
  3. `GET /api-keys`: to list a user's API keys



Let's open up our `config/routes.rb` file and plop this in there:
    
    
    Rails.application.routes.draw do
    
      post '/api-keys', to: 'api_keys#create'
    
      delete '/api-keys', to: 'api_keys#destroy'
    
      get '/api-keys', to: 'api_keys#index'
    
    end
    
    Rails.application.routes.draw do
      post '/api-keys', to: 'api_keys#create'
      delete '/api-keys', to: 'api_keys#destroy'
      get '/api-keys', to: 'api_keys#index'
    end
    _content_copy_

You could probably make this more RESTful by following the standard Rails `resources` route conventions, but I figured managing API key IDs for the purpose of revocation would be a bit too much for this post.

## A concern about API key authentication

What's the concern? ~~Nothing, really.~~ (_Update: April 17th, 2021_ â well, that was a lie â there are a couple concerns, but we'll touch on them later.)

For now, we're going to be creating a typical Rails concern that allows controllers to require API key authentication:
    
    
    module ApiKeyAuthenticatable
    
      extend ActiveSupport::Concern
    
     
    
      include ActionController::HttpAuthentication::Basic::ControllerMethods
    
      include ActionController::HttpAuthentication::Token::ControllerMethods
    
     
    
      attr_reader :current_api_key
    
      attr_reader :current_bearer
    
     
    
      # Use this to raise an error and automatically respond with a 401 HTTP status
    
      # code when API key authentication fails
    
      def authenticate_with_api_key!
    
        @current_bearer = authenticate_or_request_with_http_token &method(:authenticator)
    
      end
    
     
    
      # Use this for optional API key authentication
    
      def authenticate_with_api_key
    
        @current_bearer = authenticate_with_http_token &method(:authenticator)
    
      end
    
     
    
      private
    
     
    
      attr_writer :current_api_key
    
      attr_writer :current_bearer
    
     
    
      def authenticator(http_token, options)
    
        @current_api_key = ApiKey.find_by token: http_token
    
     
    
        current_api_key&.bearer
    
      end
    
    end
    
    module ApiKeyAuthenticatable
      extend ActiveSupport::Concern
    
      include ActionController::HttpAuthentication::Basic::ControllerMethods
      include ActionController::HttpAuthentication::Token::ControllerMethods
    
      attr_reader :current_api_key
      attr_reader :current_bearer
    
      # Use this to raise an error and automatically respond with a 401 HTTP status
      # code when API key authentication fails
      def authenticate_with_api_key!
        @current_bearer = authenticate_or_request_with_http_token &method(:authenticator)
      end
    
      # Use this for optional API key authentication
      def authenticate_with_api_key
        @current_bearer = authenticate_with_http_token &method(:authenticator)
      end
    
      private
    
      attr_writer :current_api_key
      attr_writer :current_bearer
    
      def authenticator(http_token, options)
        @current_api_key = ApiKey.find_by token: http_token
    
        current_api_key&.bearer
      end
    end
    _content_copy_

Like I said, Rails comes batteries-included. By including just a couple core classes, we can take advantage of some useful methods:

  * `#authenticate_or_request_with_http_token`: authenticate with an HTTP token, otherwise automatically request authentication, i.e. Rails will respond with a `401 Unauthenticated` HTTP status code.
  * `#authenticate_with_http_token`: attempt to authenticate with an HTTP token, but don't raise an error if the token ends up being `nil`.



In both cases, we're going to be passing in our `#authenticator` method to handle the API key lookup. Rails will handle the rest. We'll be storing the current API key bearer and the current API key into controller-level instance variables, `current_bearer` and `current_api_key`, respectively.

These methods will handle parsing of the `Authorization` HTTP header. There are multiple HTTP authorization schemes, but these 2 methods will only care about the `Bearer` scheme. We'll get into others in a second.

An `Authorization` header for an API key will look something like this:
    
    
    Authorization: Bearer 5c8e4327fd8b2bf3118f82b13890d89d
    
    Authorization: Bearer 5c8e4327fd8b2bf3118f82b13890d89d
    _content_copy_

This is how your users will likely be interacting with your API.

Real quick, let's verify that our routes are correct:
    
    
    $ rails routes
    
    # Verb    URI Pattern          Controller#Action
    
    # POST    /api-keys(.:format)  api_keys#create
    
    # DELETE  /api-keys(.:format)  api_keys#destroy
    
    # GET     /api-keys(.:format)  api_keys#index
    
    $ rails routes
    # Verb    URI Pattern          Controller#Action
    # POST    /api-keys(.:format)  api_keys#create
    # DELETE  /api-keys(.:format)  api_keys#destroy
    # GET     /api-keys(.:format)  api_keys#index
    _content_copy_

Looks good. Onward!

## Controlling API key authentication

I know, I know â we've written a lot of code and haven't tested anything in awhile. Let's define an empty controller so that we can start testing our API using `curl`.
    
    
    class ApiKeysController < ApplicationController
    
      def index
    
      end
    
     
    
      def create
    
      end
    
     
    
      def destroy
    
      end
    
    end
    
    class ApiKeysController < ApplicationController
      def index
      end
    
      def create
      end
    
      def destroy
      end
    end
    _content_copy_

Okay, let's do a quick smoke test of our endpoints using `curl`:
    
    
    $ curl -v -X POST http://localhost:3000/api-keys
    
    # < HTTP/1.1 204 No Content
    
    $ curl -v -X DELETE http://localhost:3000/api-keys
    
    # < HTTP/1.1 204 No Content
    
    $ curl -v -X GET http://localhost:3000/api-keys
    
    # < HTTP/1.1 204 No Content
    
    $ curl -v -X POST http://localhost:3000/api-keys
    # < HTTP/1.1 204 No Content
    $ curl -v -X DELETE http://localhost:3000/api-keys
    # < HTTP/1.1 204 No Content
    $ curl -v -X GET http://localhost:3000/api-keys
    # < HTTP/1.1 204 No Content
    _content_copy_

Good â no `404` or `5xx` errors. Now let's add our authenticatable concern to our controller, and define a route that requires an API key and one where an API key is optional:
    
    
     class ApiKeysController < ApplicationController
    
    +  include ApiKeyAuthenticatable 
    
    + 
    
    +  # Require token authentication for index                             
    
    +  prepend_before_action :authenticate_with_api_key!, only: [:index] 
    
    + 
    
    +  # Optional token authentication for logout                           
    
    +  prepend_before_action :authenticate_with_api_key, only: [:destroy] 
    
      
    
       def index
    
       end
    
      
    
       def create
    
       end
    
      
    
       def destroy
    
       end
    
     end
    
    class ApiKeysController < ApplicationController
      include ApiKeyAuthenticatable # [tl! ++]
      # [tl! ++]
      # Require token authentication for index                             [tl! ++]
      prepend_before_action :authenticate_with_api_key!, only: [:index] # [tl! ++]
      # [tl! ++]
      # Optional token authentication for logout                           [tl! ++]
      prepend_before_action :authenticate_with_api_key, only: [:destroy] # [tl! ++]
    
      def index
      end
    
      def create
      end
    
      def destroy
      end
    end
    _content_copy_

Let's re-run our smoke test:
    
    
    $ curl -v -X POST http://localhost:3000/api-keys
    
    # < HTTP/1.1 204 No Content
    
    $ curl -v -X DELETE http://localhost:3000/api-keys
    
    # < HTTP/1.1 204 No Content
    
    $ curl -v -X GET http://localhost:3000/api-keys
    
    # < HTTP/1.1 401 Unauthorized
    
    $ curl -v -X POST http://localhost:3000/api-keys
    # < HTTP/1.1 204 No Content
    $ curl -v -X DELETE http://localhost:3000/api-keys
    # < HTTP/1.1 204 No Content
    $ curl -v -X GET http://localhost:3000/api-keys
    # < HTTP/1.1 401 Unauthorized
    _content_copy_

Notice anything different? Our `GET` request now responds with a `401` HTTP status code, as intended. Remember â our `POST` endpoint doesn't require authentication, and authentication is optional for the `DELETE` endpoint.

## Creating our first API key

Everything looks good, so let's go ahead and work on the `#create` action. As touched on earlier, this is going to be our login endpoint.
    
    
     class ApiKeysController < ApplicationController
    
       include ApiKeyAuthenticatable
    
      
    
       # Require API key authentication for index
    
       prepend_before_action :authenticate_with_api_key!, only: [:index]
    
      
    
       # Optional API key authentication for logout
    
       prepend_before_action :authenticate_with_api_key, only: [:destroy]
    
      
    
       def index
    
       end
    
      
    
       def create
    
    +    authenticate_with_http_basic do |email, password| 
    
    +      user = User.find_by email: email 
    
    + 
    
    +      if user&.authenticate(password) 
    
    +        api_key = user.api_keys.create! token: SecureRandom.hex 
    
    + 
    
    +        render json: api_key, status: :created and return 
    
    +      end 
    
         end
    
      
    
         render status: :unauthorized
    
       end
    
      
    
       def destroy
    
       end
    
     end
    
    class ApiKeysController < ApplicationController
      include ApiKeyAuthenticatable
    
      # Require API key authentication for index
      prepend_before_action :authenticate_with_api_key!, only: [:index]
    
      # Optional API key authentication for logout
      prepend_before_action :authenticate_with_api_key, only: [:destroy]
    
      def index
      end
    
      def create
        authenticate_with_http_basic do |email, password| # [tl! ++]
          user = User.find_by email: email # [tl! ++]
          # [tl! ++]
          if user&.authenticate(password) # [tl! ++]
            api_key = user.api_keys.create! token: SecureRandom.hex # [tl! ++]
            # [tl! ++]
            render json: api_key, status: :created and return # [tl! ++]
          end # [tl! ++]
        end
    
        render status: :unauthorized
      end
    
      def destroy
      end
    end
    _content_copy_

Once again, we're going to be utilizing another method provided by Rails to handle the grunt-work of HTTP authentication. Like the previously used method `authenticate_with_http_token`, the `authenticate_with_http_basic` will parse the `Authorization` header. Unlike the token method variant caring about the `Bearer` scheme, the basic variant only cares about the `Basic` scheme.

A basic `Authorization` header will look something like this:
    
    
    Authorization: Basic [[email protected]](/cdn-cgi/l/email-protection):secret
    
    Authorization: Basic zeke@keygen.example:secret
    _content_copy_

The actual email and password values will be base64 encoded, but for example purposes we're omitting that detail. Rails will automatically handle parsing and decoding these values. You Don't Need Deviseâ¢.

Now that we've written hundreds of lines of code, let's errâ¦ wait. We've only written about 60 lines of application code. A lot of people will make API key authentication sound harder and more complicated than it really is. It's really not that hard, and it's not complicated, because Rails does most of the heavy lifting for us.

Anyways â let's create our first API key:
    
    
    $ curl -v -X POST http://localhost:3000/api-keys \
    
        -u [[email protected]](/cdn-cgi/l/email-protection):secret
    
    # < HTTP/1.1 201 Created
    
    # {
    
    #   "id": 2,
    
    #   "bearer_id": 1,
    
    #   "bearer_type": "User",
    
    #   "token": "5d1524c7e2486f98e1b65cbe1cdeb258",
    
    #   "created_at": "2021-04-16T15:18:01.709Z",
    
    #   "updated_at": "2021-04-16T15:18:01.709Z"
    
    # }
    
    $ curl -v -X POST http://localhost:3000/api-keys \
        -u zeke@keygen.example:secret
    # < HTTP/1.1 201 Created
    # {
    #   "id": 2,
    #   "bearer_id": 1,
    #   "bearer_type": "User",
    #   "token": "5d1524c7e2486f98e1b65cbe1cdeb258",
    #   "created_at": "2021-04-16T15:18:01.709Z",
    #   "updated_at": "2021-04-16T15:18:01.709Z"
    # }
    _content_copy_

Nice, but before we celebrate, let's make sure a bad password and a bad email are properly rejected with a `401` response, respectively:
    
    
    $ curl -v -X POST http://localhost:3000/api-keys \
    
        -u [[email protected]](/cdn-cgi/l/email-protection):foo
    
    # < HTTP/1.1 401 Unauthorized
    
    $ curl -v -X POST http://localhost:3000/api-keys \
    
        -u [[email protected]](/cdn-cgi/l/email-protection):secret
    
    # < HTTP/1.1 401 Unauthorized
    
    $ curl -v -X POST http://localhost:3000/api-keys \
        -u zeke@keygen.example:foo
    # < HTTP/1.1 401 Unauthorized
    $ curl -v -X POST http://localhost:3000/api-keys \
        -u foo@keygen.example:secret
    # < HTTP/1.1 401 Unauthorized
    _content_copy_

## Listing our API keys

Up next, let's work on our `#index` action. Go ahead and open that controller up again and let's list the API keys of the `current_bearer`.
    
    
     class ApiKeysController < ApplicationController
    
       include ApiKeyAuthenticatable
    
      
    
       # Require API key authentication for index
    
       prepend_before_action :authenticate_with_api_key!, only: [:index]
    
      
    
       # Optional API key authentication for logout
    
       prepend_before_action :authenticate_with_api_key, only: [:destroy]
    
      
    
       def index
    
    +    render json: current_bearer.api_keys 
    
       end
    
      
    
       def create
    
         authenticate_with_http_basic do |email, password|
    
           user = User.find_by email: email
    
      
    
           if user&.authenticate(password)
    
             api_key = user.api_keys.create! token: SecureRandom.hex
    
      
    
             render json: api_key, status: :created and return
    
           end
    
         end
    
      
    
         render status: :unauthorized
    
       end
    
      
    
       def destroy
    
       end
    
     end
    
    class ApiKeysController < ApplicationController
      include ApiKeyAuthenticatable
    
      # Require API key authentication for index
      prepend_before_action :authenticate_with_api_key!, only: [:index]
    
      # Optional API key authentication for logout
      prepend_before_action :authenticate_with_api_key, only: [:destroy]
    
      def index
        render json: current_bearer.api_keys # [tl! ++]
      end
    
      def create
        authenticate_with_http_basic do |email, password|
          user = User.find_by email: email
    
          if user&.authenticate(password)
            api_key = user.api_keys.create! token: SecureRandom.hex
    
            render json: api_key, status: :created and return
          end
        end
    
        render status: :unauthorized
      end
    
      def destroy
      end
    end
    _content_copy_

Let's try it out:
    
    
    $ curl -v -X GET http://localhost:3000/api-keys \
    
        -H 'Authorization: Bearer 5d1524c7e2486f98e1b65cbe1cdeb258'
    
    # < HTTP/1.1 200 OK
    
    # [
    
    #   {
    
    #     "id": 1,
    
    #     "bearer_id": 1,
    
    #     "bearer_type": "User",
    
    #     "token": "5c8e4327fd8b2bf3118f82b13890d89d",
    
    #     "created_at": "2021-04-16T13:56:42.181Z",
    
    #     "updated_at": "2021-04-16T13:56:42.181Z"
    
    #   },
    
    #   {
    
    #     "id": 2,
    
    #     "bearer_id": 1,
    
    #     "bearer_type": "User",
    
    #     "token": "5d1524c7e2486f98e1b65cbe1cdeb258",
    
    #     "created_at": "2021-04-16T15:18:01.709Z",
    
    #     "updated_at": "2021-04-16T15:18:01.709Z"
    
    #   }
    
    # ]
    
    $ curl -v -X GET http://localhost:3000/api-keys \
        -H 'Authorization: Bearer 5d1524c7e2486f98e1b65cbe1cdeb258'
    # < HTTP/1.1 200 OK
    # [
    #   {
    #     "id": 1,
    #     "bearer_id": 1,
    #     "bearer_type": "User",
    #     "token": "5c8e4327fd8b2bf3118f82b13890d89d",
    #     "created_at": "2021-04-16T13:56:42.181Z",
    #     "updated_at": "2021-04-16T13:56:42.181Z"
    #   },
    #   {
    #     "id": 2,
    #     "bearer_id": 1,
    #     "bearer_type": "User",
    #     "token": "5d1524c7e2486f98e1b65cbe1cdeb258",
    #     "created_at": "2021-04-16T15:18:01.709Z",
    #     "updated_at": "2021-04-16T15:18:01.709Z"
    #   }
    # ]
    _content_copy_

There they are! Looks good.

## Revoking our first API key

So we've got our 2 API keys. Let's revoke 1 of them. To do that, we'll need to work on the `#destroy` action of our controller. It's gonna be as complicated as the last action we wrote, so prepare yourself:
    
    
     class ApiKeysController < ApplicationController
    
       include ApiKeyAuthenticatable
    
      
    
       # Require API key authentication for index
    
       prepend_before_action :authenticate_with_api_key!, only: [:index]
    
      
    
       # Optional API key authentication for logout
    
       prepend_before_action :authenticate_with_api_key, only: [:destroy]
    
      
    
       def index
    
         render json: current_bearer.api_keys
    
       end
    
      
    
       def create
    
         authenticate_with_http_basic do |email, password|
    
           user = User.find_by email: email
    
      
    
           if user&.authenticate(password)
    
             api_key = user.api_keys.create! token: SecureRandom.hex
    
      
    
             render json: api_key, status: :created and return
    
           end
    
         end
    
      
    
         render status: :unauthorized
    
       end
    
      
    
       def destroy
    
    +    current_api_key&.destroy 
    
       end
    
     end
    
    class ApiKeysController < ApplicationController
      include ApiKeyAuthenticatable
    
      # Require API key authentication for index
      prepend_before_action :authenticate_with_api_key!, only: [:index]
    
      # Optional API key authentication for logout
      prepend_before_action :authenticate_with_api_key, only: [:destroy]
    
      def index
        render json: current_bearer.api_keys
      end
    
      def create
        authenticate_with_http_basic do |email, password|
          user = User.find_by email: email
    
          if user&.authenticate(password)
            api_key = user.api_keys.create! token: SecureRandom.hex
    
            render json: api_key, status: :created and return
          end
        end
    
        render status: :unauthorized
      end
    
      def destroy
        current_api_key&.destroy # [tl! ++]
      end
    end
    _content_copy_

That's all it takes, folks. Now let's test it out by revoking our original API key, the one that we created in the Rails console:
    
    
    $ curl -v -X DELETE http://localhost:3000/api-keys \
    
        -H 'Authorization: Bearer 5c8e4327fd8b2bf3118f82b13890d89d'
    
    # < HTTP/1.1 204 No Content
    
    $ curl -v -X DELETE http://localhost:3000/api-keys \
        -H 'Authorization: Bearer 5c8e4327fd8b2bf3118f82b13890d89d'
    # < HTTP/1.1 204 No Content
    _content_copy_

We got a `No Content` status code, but did it actually work? Remember, our `DELETE` endpoint has optional API key authentication, unlike the list endpoint which requires authentication, so even if an invalid API key was provided, it would still return a `204 No Content` status code. Is this ideal? Probably not, but it works to expemlify the 2 different authentication actions.

Let's assert that the API key was revoked, using the Rails console:
    
    
    $ rails c
    
    > ApiKey.count
    
    # => 1
    
    > ApiKey.find_by token: '5c8e4327fd8b2bf3118f82b13890d89d'
    
    # => nil
    
    $ rails c
    > ApiKey.count
    # => 1
    > ApiKey.find_by token: '5c8e4327fd8b2bf3118f82b13890d89d'
    # => nil
    _content_copy_

Looks like it worked!

## To bear or not to bear

Since our API keys are polymorphic, we can have multiple authenticatable models, such as an `Admin` model, or a `SpaceInvader`. The sky's the limit, and as long as your code is flexible enough, i.e. it's not expecting a `User` everywhere a bearer is, you shouldn't have any issues making some obscure model an API key bearer.

Pair this with an authorization gem like Pundit and you'll be golden. I've been running a variant of this for Keygen's API â allowing users, admins, products and licenses to all be authenticatable, each with different permission sets.

(I won't get too deep into the weeds here, but I thought it'd be worth mentioning.)

## Wrapping up

That's it. We've implemented a login endpoint where we can generate new API keys, a logout endpoint where we can revoke existing API keys, as well as an endpoint allowing us to list the current user's API keys. From here, adding API key authentication to other controller actions is as simple as adding one of the 2 `before_action` callbacks.

Some people may raise concern that we're "rolling our own auth" here, but that's actually not true. We're using tools that Rails provides for us out-of-the-box. API key authentication doesn't have to be complex, and you most certainly don't have to use a third-party gem like Devise to implement it.

Also, you certainly don't need JWTs either. But that's an entire other blog post in and of itself. But I digressâ¦ for another day, for another day.

You can harden your authentication token scheme by utilizing HMAC digests to protect against timing-attacks and to prevent tokens from being stored in plaintext, but I'll leave that as an exercise to the reader. (Edit: I made a mistake not including the HMAC solution in the original post. Please see update below.)

We've manged to do everything here in under 100 lines of code â 96 to be exact â and that's including the migrations! That's pretty cool if you ask me.

Looking for more? Next, [learn how to implement TOTP 2FA using ROTP](/blog/how-to-implement-totp-2fa-in-rails-using-rotp/).

* * *

#### Update: April 17th, 2021

It was brought to my attention shortly after publishing this post that the original code is storing API keys as plaintext in the database, which is true. That fact was (briefly) mentioned at the end of the post, and I originally thought including the solution would complicate the post, but I think I made a mistake excluding it. We should always strive to reflect best security practices when writing technical "how-to" posts, even if that results in more complex code or a longer blog post.

Because the original code stores tokens in plaintext, the code [could also be vulnerable to timing attacks](https://en.wikipedia.org/wiki/Timing_attack). We're going to utilize a secure HMAC function to resolve both of these vulnerabilities.

To sum up, the 2 vulnerabilities are:

  1. Storing API keys as plaintext (a big no-no â these tokens should be treated like passwords.)
  2. Tokens could be vulnerable to timing attacks (yes, [even with a database index](https://soatok.blog/2021/08/20/lobste-rs-password-reset-vulnerability/)!)



I'm leaving the original blog post unchanged for transparency.

## Patching the vulnerabilities

To start our patch, let's rollback our last migration which created the `tokens` table. We're going to slightly modify the schema. In a production environment, we'd want to add a new column, populate it, and then remove the old column, but this will suffice for our toy example application.
    
    
    $ rails db:rollback
    
    $ rails db:rollback
    _content_copy_

Open up our last migration and change the `token` column to `token_digest`:
    
    
     class CreateApiKeys < ActiveRecord::Migration[5.2]
    
       def change
    
         create_table :api_keys do |t|
    
           t.integer :bearer_id, null: false
    
           t.string :bearer_type, null: false
    
    -      t.string :token, null: false 
    
    +      t.string :token_digest, null: false 
    
           t.timestamps null: false
    
         end
    
      
    
         add_index :api_keys, [:bearer_id, :bearer_type]
    
    -    add_index :api_keys, :token, unique: true 
    
    +    add_index :api_keys, :token_digest, unique: true 
    
       end
    
     end
    
    class CreateApiKeys < ActiveRecord::Migration[5.2]
      def change
        create_table :api_keys do |t|
          t.integer :bearer_id, null: false
          t.string :bearer_type, null: false
          t.string :token, null: false # [tl! --]
          t.string :token_digest, null: false # [tl! ++]
          t.timestamps null: false
        end
    
        add_index :api_keys, [:bearer_id, :bearer_type]
        add_index :api_keys, :token, unique: true # [tl! --]
        add_index :api_keys, :token_digest, unique: true # [tl! ++]
      end
    end
    _content_copy_

Then we'll want to re-run the migration:
    
    
    $ rails db:migrate
    
    $ rails db:migrate
    _content_copy_

Next, we're going to update the `ApiKey` model to utilize a SHA-256 HMAC function, and also provide a method for authenticating an API key by token.
    
    
     class ApiKey < ApplicationRecord
    
    +  HMAC_SECRET_KEY = ENV.fetch('API_KEY_HMAC_SECRET_KEY') 
    
    + 
    
       belongs_to :bearer, polymorphic: true
    
    + 
    
    +  before_create :generate_token_hmac_digest
    
    + 
    
    +  # Virtual attribute for raw token value, allowing us to respond with the
    
    +  # API key's non-hashed token value. but only directly after creation.
    
    +  attr_accessor :token
    
    + 
    
    +  def self.authenticate_by_token!(token)
    
    +    digest = OpenSSL::HMAC.hexdigest 'SHA256', HMAC_SECRET_KEY, token
    
    + 
    
    +    find_by! token_digest: digest
    
    +  end
    
    + 
    
    +  def self.authenticate_by_token(token)
    
    +    authenticate_by_token! token
    
    +  rescue ActiveRecord::RecordNotFound
    
    +    nil
    
    +  end
    
    + 
    
    +  # Add virtual token attribute to serializable attributes, and exclude
    
    +  # the token's HMAC digest
    
    +  def serializable_hash(options = nil)
    
    +    h = super options.merge(except: 'token_digest')
    
    +    h.merge! 'token' => token if token.present?
    
    +    h
    
    +  end
    
    + 
    
    +  private
    
    + 
    
    +  def generate_token_hmac_digest
    
    +    raise ActiveRecord::RecordInvalid, 'token is required' unless
    
    +      token.present?
    
    + 
    
    +    digest = OpenSSL::HMAC.hexdigest 'SHA256', HMAC_SECRET_KEY, token
    
    + 
    
    +    self.token_digest = digest
    
    +  end 
    
     end
    
    class ApiKey < ApplicationRecord
      HMAC_SECRET_KEY = ENV.fetch('API_KEY_HMAC_SECRET_KEY') # [tl! ++]
      # [tl! ++]
      belongs_to :bearer, polymorphic: true
      # [tl! ++:start]
      before_create :generate_token_hmac_digest
    
      # Virtual attribute for raw token value, allowing us to respond with the
      # API key's non-hashed token value. but only directly after creation.
      attr_accessor :token
    
      def self.authenticate_by_token!(token)
        digest = OpenSSL::HMAC.hexdigest 'SHA256', HMAC_SECRET_KEY, token
    
        find_by! token_digest: digest
      end
    
      def self.authenticate_by_token(token)
        authenticate_by_token! token
      rescue ActiveRecord::RecordNotFound
        nil
      end
    
      # Add virtual token attribute to serializable attributes, and exclude
      # the token's HMAC digest
      def serializable_hash(options = nil)
        h = super options.merge(except: 'token_digest')
        h.merge! 'token' => token if token.present?
        h
      end
    
      private
    
      def generate_token_hmac_digest
        raise ActiveRecord::RecordInvalid, 'token is required' unless
          token.present?
    
        digest = OpenSSL::HMAC.hexdigest 'SHA256', HMAC_SECRET_KEY, token
    
        self.token_digest = digest
      end # [tl! ++:end]
    end
    _content_copy_

Here we've defined a few new methods for the `ApiKey` model:

  * A new virtual attribute called `token` which holds the plaintext value of our API key's token. This virtual attribute is only available after the model is created.
  * Redefining an API key's `serializable_hash` attributes, to include the `token` virtual attribute when present, and to always exclude `token_digest`.
  * A `before_create` callback which handles generating an HMAC of the current token before the API key is persisted to the database.
  * Bang and non-bang variants of `authenticate_by_token` which handles securely looking up an API key by token.



Our HMAC function requires a secret key to be able to compute digests, defined in a new `API_KEY_HMAC_SECRET_KEY` environment variable. Let's generate a random string with 32 bytes of entropy that we can use for the HMAC secret key:
    
    
    $ rails c
    
    > SecureRandom.hex(32)
    
    # => febf2568e5f151dc979ebdb84f05633417beeef06b9fb4e32e6c4eea6b121afc
    
    $ rails c
    > SecureRandom.hex(32)
    # => febf2568e5f151dc979ebdb84f05633417beeef06b9fb4e32e6c4eea6b121afc
    _content_copy_

And let's go ahead and set the required environment variable:
    
    
    $ export API_KEY_HMAC_SECRET_KEY=febf2568e5f151dc979ebdb84f05633417beeef06b9fb4e32e6c4eea6b121afc
    
    $ export API_KEY_HMAC_SECRET_KEY=febf2568e5f151dc979ebdb84f05633417beeef06b9fb4e32e6c4eea6b121afc
    _content_copy_

Do note that the HMAC secret key should never change. Changing the secret key will invalidate all existing API keys, since we'd no longer be able to authenticate them.

Lastly, we'll want to update the `ApiKeyAuthenticatable` concern to use our new API key authentication method:
    
    
     module ApiKeyAuthenticatable
    
       extend ActiveSupport::Concern
    
      
    
       include ActionController::HttpAuthentication::Basic::ControllerMethods
    
       include ActionController::HttpAuthentication::Token::ControllerMethods
    
      
    
       attr_reader :current_api_key
    
       attr_reader :current_bearer
    
      
    
       # Use this to raise an error and automatically respond with a 401 HTTP status
    
       # code when API key authentication fails
    
       def authenticate_with_api_key!
    
         @current_bearer = authenticate_or_request_with_http_token &method(:authenticator)
    
       end
    
      
    
       # Use this for optional API key authentication
    
       def authenticate_with_api_key
    
         @current_bearer = authenticate_with_http_token &method(:authenticator)
    
       end
    
      
    
       private
    
      
    
       attr_writer :current_api_key
    
       attr_writer :current_bearer
    
      
    
       def authenticator(http_token, options)
    
    -    @current_api_key = ApiKey.find_by token: http_token 
    
    +    @current_api_key = ApiKey.authenticate_by_token http_token 
    
      
    
         current_api_key&.bearer
    
       end
    
     end
    
    module ApiKeyAuthenticatable
      extend ActiveSupport::Concern
    
      include ActionController::HttpAuthentication::Basic::ControllerMethods
      include ActionController::HttpAuthentication::Token::ControllerMethods
    
      attr_reader :current_api_key
      attr_reader :current_bearer
    
      # Use this to raise an error and automatically respond with a 401 HTTP status
      # code when API key authentication fails
      def authenticate_with_api_key!
        @current_bearer = authenticate_or_request_with_http_token &method(:authenticator)
      end
    
      # Use this for optional API key authentication
      def authenticate_with_api_key
        @current_bearer = authenticate_with_http_token &method(:authenticator)
      end
    
      private
    
      attr_writer :current_api_key
      attr_writer :current_bearer
    
      def authenticator(http_token, options)
        @current_api_key = ApiKey.find_by token: http_token # [tl! --]
        @current_api_key = ApiKey.authenticate_by_token http_token # [tl! ++]
    
        current_api_key&.bearer
      end
    end
    _content_copy_

## Verifying our patch

First up â let's generate a new API key:
    
    
    $ curl -v -X POST http://localhost:3000/api-keys \
    
        -u [[email protected]](/cdn-cgi/l/email-protection):secret
    
    # < HTTP/1.1 201 Created
    
    # {
    
    #   "id": 3,
    
    #   "bearer_id": 1,
    
    #   "bearer_type": "User",
    
    #   "created_at": "2021-04-17T19:44:28.975Z",
    
    #   "updated_at": "2021-04-17T19:44:28.975Z",
    
    #   "token": "4ff169e0c3e42fd0b60af4f12abae086"
    
    # }
    
    $ curl -v -X POST http://localhost:3000/api-keys \
        -u zeke@keygen.example:secret
    # < HTTP/1.1 201 Created
    # {
    #   "id": 3,
    #   "bearer_id": 1,
    #   "bearer_type": "User",
    #   "created_at": "2021-04-17T19:44:28.975Z",
    #   "updated_at": "2021-04-17T19:44:28.975Z",
    #   "token": "4ff169e0c3e42fd0b60af4f12abae086"
    # }
    _content_copy_

Looks good. The API key's token is correctly being generated, and the raw token value is still being serialized in the JSON response. But let's assert that the token is no longer being stored in plaintext:
    
    
    $ rails c
    
    > ApiKey.last
    
    # => #<ApiKey id: 3, bearer_id: 1, bearer_type: "User", token_digest: "f2f00166929739413ebe7848306d4be04b57447ad92a386d27...", created_at: "2021-04-17 19:44:28", updated_at: "2021-04-17 19:44:28">
    
    $ rails c
    > ApiKey.last
    # => #<ApiKey id: 3, bearer_id: 1, bearer_type: "User", token_digest: "f2f00166929739413ebe7848306d4be04b57447ad92a386d27...", created_at: "2021-04-17 19:44:28", updated_at: "2021-04-17 19:44:28">
    _content_copy_

Looks correct. Now let's also make sure we can still authenticate with our API key's token, and we also want to assert that we're not leaking our `token_digest` in the list of serialized API keys.
    
    
    $ curl -v -X GET http://localhost:3000/api-keys \
    
        -H 'Authorization: Bearer 4ff169e0c3e42fd0b60af4f12abae086'
    
    # < HTTP/1.1 200 OK
    
    # [
    
    #   {
    
    #     "id": 3,
    
    #     "bearer_id": 1,
    
    #     "bearer_type": "User",
    
    #     "created_at": "2021-04-17T19:44:28.975Z",
    
    #     "updated_at": "2021-04-17T19:44:28.975Z"
    
    #   }
    
    # ]
    
    $ curl -v -X GET http://localhost:3000/api-keys \
        -H 'Authorization: Bearer 4ff169e0c3e42fd0b60af4f12abae086'
    # < HTTP/1.1 200 OK
    # [
    #   {
    #     "id": 3,
    #     "bearer_id": 1,
    #     "bearer_type": "User",
    #     "created_at": "2021-04-17T19:44:28.975Z",
    #     "updated_at": "2021-04-17T19:44:28.975Z"
    #   }
    # ]
    _content_copy_

And once again, things look good. But we have a new problem. Since we can no longer read the tokens of other API keys, we're unable to delete them using our existing API key deletion endpoint. To fix this issue, let's rework our "logout" endpoint.

Let's open up our `routes.rb` file and make a quick edit (and in the process, we get to make our endpoints more Rails-y with `resources`):
    
    
     Rails.application.routes.draw do
    
    -  post '/api-keys', to: 'api_keys#create' 
    
    -  delete '/api-keys', to: 'api_keys#destroy' 
    
    -  get '/api-keys', to: 'api_keys#index' 
    
    +  resources :api_keys, path: 'api-keys', only: %i[index create destroy] 
    
     end
    
    Rails.application.routes.draw do
      post '/api-keys', to: 'api_keys#create' # [tl! --]
      delete '/api-keys', to: 'api_keys#destroy' # [tl! --]
      get '/api-keys', to: 'api_keys#index' # [tl! --]
      resources :api_keys, path: 'api-keys', only: %i[index create destroy] # [tl! ++]
    end
    _content_copy_

And we'll also want to update our controller to revoke API keys by ID, rather than simply revoking the `current_api_key`:
    
    
     class ApiKeysController < ApplicationController
    
       include ApiKeyAuthenticatable
    
      
    
    -  # Require API key authentication for index                                   
    
    -  prepend_before_action :authenticate_with_api_key!, only: [:index] 
    
    +  # Require API key authentication                                             
    
    +  prepend_before_action :authenticate_with_api_key!, only: %i[index destroy] 
    
    - 
    
    -  # Optional API key authentication for logout                                 
    
    -  prepend_before_action :authenticate_with_api_key, only: [:destroy] 
    
      
    
       def index
    
         render json: current_bearer.api_keys
    
       end
    
      
    
       def create
    
         authenticate_with_http_basic do |email, password|
    
           user = User.find_by email: email
    
      
    
           if user&.authenticate(password)
    
             api_key = user.api_keys.create! token: SecureRandom.hex
    
      
    
             render json: api_key, status: :created and return
    
           end
    
         end
    
      
    
         render status: :unauthorized
    
       end
    
      
    
       def destroy
    
    +    api_key = current_bearer.api_keys.find(params[:id]) 
    
    + 
    
    -    current_api_key&.destroy 
    
    +    api_key.destroy 
    
       end
    
     end
    
    class ApiKeysController < ApplicationController
      include ApiKeyAuthenticatable
    
      # Require API key authentication for index                                   [tl! --]
      prepend_before_action :authenticate_with_api_key!, only: [:index] # [tl! --]
      # Require API key authentication                                             [tl! ++]
      prepend_before_action :authenticate_with_api_key!, only: %i[index destroy] # [tl! ++]
      # [tl! --]
      # Optional API key authentication for logout                                 [tl! --]
      prepend_before_action :authenticate_with_api_key, only: [:destroy] # [tl! --]
    
      def index
        render json: current_bearer.api_keys
      end
    
      def create
        authenticate_with_http_basic do |email, password|
          user = User.find_by email: email
    
          if user&.authenticate(password)
            api_key = user.api_keys.create! token: SecureRandom.hex
    
            render json: api_key, status: :created and return
          end
        end
    
        render status: :unauthorized
      end
    
      def destroy
        api_key = current_bearer.api_keys.find(params[:id]) # [tl! ++]
        # [tl! ++]
        current_api_key&.destroy # [tl! --]
        api_key.destroy # [tl! ++]
      end
    end
    _content_copy_

And voila! This patch does add a bit of complexity to the API key model, but it resolves critical vulnerabilities in the original implementation. You can view [the full example app on GitHub](https://github.com/ezekg/example-rails-api-key-authentication).

Thanks to /u/stouset for the report.

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


