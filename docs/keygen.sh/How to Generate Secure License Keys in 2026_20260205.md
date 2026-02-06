# How to Generate Secure License Keys in 2026

**来源:** https://keygen.sh
**链接:** https://keygen.sh/blog/how-to-generate-license-keys/
**日期:** Wed, 02 Jun 2021 05:00:00 GMT

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
    * [_support_ Get Support ](/cdn-cgi/l/email-protection#f685838686998482b69d938f919398d8859e)
  * [Pricing ](/pricing/)
  * [Log in ](https://app.keygen.sh/login)
  * [Sign Up](https://app.keygen.sh/register?plan=984180df-07b3-4dc1-b138-ca68a0f913ed)



# How to Generate Cryptographically Secure License Keys in 2026

Wednesday, June 2nd 2021

Generating and verifying license keys is a common requirement for a lot commercial software these days. From desktop applications such as those built on frameworks like [Electron](/blog/how-to-license-and-distribute-an-electron-app/) or [Qt](https://www.qt.io/), to dual-licensed open source packages and libraries like [Sidekiq](https://sidekiq.org/), to a variety of other on-premise software applications and dependencies.

They all have one common denominator: _the need for secure licensing._

But as an independent software vendor (ISV), you may be asking yourself â **" what technology should I choose for software licensing in 2021?"**

Well, before we get to the answer, we need to understand a bit of history.

## The 2 big attack vectors for licensing

When it comes to software licensing, the key generation and verification algorithms vendors choose can make or break a licensing system. After an algorithm has been compromised, a vendor can no longer trust _any_ previously generated license keys, including those belonging to legit end-users.

When this happens, there are a couple things we can do:

  1. Move to an online licensing server, where we can check keys against a list of valid keys. If you choose to build an in-house licensing system, this can be [incredibly expensive](/build-vs-buy/), both up-front and in the long-term. This can also limit our application's license checks to online-only, which may be less than ideal.
  2. Move to a modern license key algorithm. This resolution has the rather unfortunate side-effect of invalidating all previously generated license keys, including those belonging to legit end-users, requiring a migration plan.



Both of these solutions can come at a huge cost, both in terms of end-user trust, support costs, as well as engineering resources. Suffice it to say, it's a bad situation. And ideally, what we want to do is avoid the situation entirely, by choosing a modern, secure license key algorithm from the get-go.

But before we cover how, let's take a quick look at a couple of the largest attack vectors for licensing, which may help us understand how to defend against them.

### Software cracking

Software "cracking" is the act of directly modifying the source code of a software application to bypass its licensing system entirely. As much as vendors hate to hear it: _all applications installed on an end-users device are susceptible to cracking._

(After all, an application is simply made up of bits and bytes, ones and zeroes, stored locally, and those can always be modified no matter how hard a vendor may try.)

**But doesn 't that mean licensing is a fool's errand?** Not at all. Licensing can be a powerful deterrent against casual piracy, especially for applications that utilize a modern licensing system. More importantly, a good licensing system can help you get visibility into application usage, it can provide distribution and update services, and a great system can help you maximize your software's revenue potential by highlighting natural up-sell opportunities, such as when an end-user attempts to utilize more [device seats](/docs/activating-machines/) than they've been allotted. 

Software cracks usually only work for a single version of a particular application, since the application code itself is modified to bypass any license checks (meaning a software update often requires an updated crack for the new application code.) Distributing a cracked version of an application falls on the bad actor.

Cracks are one of the more common attack vectors for software applications.

### Software keygens

The other major attack vector is known as a software "keygen", which is much more ominous. As its name may imply, a keygen is a form of software, often a separate program or webpage, that generates _valid_ license keys, i.e. a key-generator, or "keygen."

Most software vendors have some type of license keygen, which they keep secret. For example, after a user submits a successful purchase order, part of the order process calls a key generator, which generates a valid, legitimate license key for the new customer.

But when it comes to vulnerable, legacy license key algorithms, a bad actor may _also_ be able to accomplish a similar feat â generating valid, albeit _illegitimate_ , license keys, granted they put in some effort to reverse-engineer the algorithm.

Depending on your key generation algorithm, a keygen like this may only be able to generate valid key for a single version of an application. But in the worst case, a bad actor can create a keygen that generates valid license keys that work across all versions of an application, requiring a complete upheaval of the product's licensing system.

**Fun fact: we chose the name "Keygen" for it's true meaning â a license key generator.** We don't use proprietary algorithms that can be reverse-engineered, like the olden days. Rather, we lean on modern cryptography â the same algorithms used for the Internet's security and used by government agencies such as the NSA â to generate secure license keys. 

_It 's also worth mentioning that keygens are much more valuable to bad actors than cracks, because a keygen can be used on the **real** application, vs the bad actor having to distribute a **modified** , cracked version of the application._

## The legacy license key algorithm

Now, we've alluded to this legacy algorithm, which is actually still in use to this day by a number of software vendors. It's called Partial Key Verification, and although it may seem like a good-enough system, it is _security through obscurity._

Why? Let's dive in and find out.

### Partial key verification

These days, writing a partial key verification (PKV) algorithm is actually _more work_ than simply doing it the right way. But for the sake of understanding, let's write our own partial key verification system. And then we're going to break it.

#### A quick definition of PKV

[Partial Key Verification](https://www.brandonstaggs.com/2007/07/26/implementing-a-partial-serial-number-verification-system-in-delphi/) is a software license key algorithm that partitions a product key into multiple "subkeys." With each new version of your product, your license key verification algorithm will check a different subset of a license's subkeys.

It's called _partial_ key verification because the verification algorithm never tests the full license key, it only tests a subset of subkeys. (Or so they say.)

_I 'd recommend reading the above blog post by Brandon from 2007, with his partial serial number verification system being written in Delphi. But if you're not into Delphi, we'll be porting the partial key verification algorithm to Node._

#### An implementation of PKV

The main components of a PKV key are the **seed** value and its **subkeys** (together referred to as the **serial**), and then a **checksum**. The subkeys are derived from the unique seed value, accomplished using [bit twiddling](https://en.wikipedia.org/wiki/Bit_manipulation), and the checksum is to ensure that the serial (seed + subkeys) does not contain a typo. (Yesâ¦ in the olden days, a person actually had to input license keys by-hand.)

_We 're not going to get into the specifics on each of these components, e.g. how the checksum works, since Brandon's post covers all of that in detail._

With that said, let's assume the role of a business that is about to release a new application. We're going to write a _keygen_ that we, the business, can use to generate legitimate keys for our end-users after they purchase our product.

Our PKV keygen should be a tightly kept trade secret, because with it comes the power to craft license keys at-will. But we'll soon realize, much to our demise, keeping a PKV keygen secret is actually not possible.

So, without further ado â let's begin.

Here's what a PKV keygen looks like:
    
    
    const crypto = require('crypto')
    
     
    
    // Format a number to a fixed-length hexadecimal string
    
    function toFixedHex(num, len) {
    
      return num.toString(16).toUpperCase().padStart(len, '0').substring(0, len)
    
    }
    
     
    
    // Derive a subkey from the seed (a, b, c being params for bit twiddling)
    
    function getSubkeyFromSeed(seed, a, b, c) {
    
      if (typeof seed === 'string') {
    
        seed = parseInt(seed, 16)
    
      }
    
     
    
      a = a % 25
    
      b = b % 3
    
     
    
      let subkey
    
      if (a % 2 === 0) {
    
        subkey = ((seed >> a) & 0x000000ff) ^ ((seed >> b) | c) & 0xff
    
      } else {
    
        subkey = ((seed >> a) & 0x000000ff) ^ ((seed >> b) & c) & 0xff
    
      }
    
     
    
      return toFixedHex(subkey, 2)
    
    }
    
     
    
    // Get the checksum for a given serial string
    
    function getChecksumForSerial(serial) {
    
      let right = 0x00af // 175
    
      let left = 0x0056 // 101
    
     
    
      for (var i = 0; i < serial.length; i++) {
    
        right += serial.charCodeAt(i)
    
        if (right > 0x00ff) {
    
          right -= 0x00ff
    
        }
    
     
    
        left += right
    
        if (left > 0x00ff) {
    
          left -= 0x00ff
    
        }
    
      }
    
     
    
      return toFixedHex((left << 8) + right, 4)
    
    }
    
     
    
    // Format the key (XXXX-XXXX-XXXX-XXXX-XXXX)
    
    function formatKey(key) {
    
      return key.match(/.{4}/g).join('-')
    
    }
    
     
    
    // Generate a 4-byte hexadecimal seed value
    
    function generateSeed(n) {
    
      const seed = crypto.randomBytes(4).toString('hex')
    
     
    
      return seed.toUpperCase()
    
    }
    
     
    
    // Generate a (legitimate) license key
    
    function generateKey(seed) {
    
      // Build a list of subkeys (bit twiddling params are arbitrary but can never change)
    
      const subkeys = [
    
        getSubkeyFromSeed(seed, 24, 3, 200),
    
        getSubkeyFromSeed(seed, 10, 0, 56),
    
        getSubkeyFromSeed(seed, 1, 2, 91),
    
        getSubkeyFromSeed(seed, 7, 1, 100),
    
      ]
    
     
    
      // Build the serial (seed + subkeys)
    
      const serial = seed + subkeys.join('')
    
     
    
      // Build the key (serial + checksum)
    
      const key = serial + getChecksumForSerial(serial)
    
     
    
      return formatKey(key)
    
    }
    
    const crypto = require('crypto')
    
    // Format a number to a fixed-length hexadecimal string
    function toFixedHex(num, len) {
      return num.toString(16).toUpperCase().padStart(len, '0').substring(0, len)
    }
    
    // Derive a subkey from the seed (a, b, c being params for bit twiddling)
    function getSubkeyFromSeed(seed, a, b, c) {
      if (typeof seed === 'string') {
        seed = parseInt(seed, 16)
      }
    
      a = a % 25
      b = b % 3
    
      let subkey
      if (a % 2 === 0) {
        subkey = ((seed >> a) & 0x000000ff) ^ ((seed >> b) | c) & 0xff
      } else {
        subkey = ((seed >> a) & 0x000000ff) ^ ((seed >> b) & c) & 0xff
      }
    
      return toFixedHex(subkey, 2)
    }
    
    // Get the checksum for a given serial string
    function getChecksumForSerial(serial) {
      let right = 0x00af // 175
      let left = 0x0056 // 101
    
      for (var i = 0; i < serial.length; i++) {
        right += serial.charCodeAt(i)
        if (right > 0x00ff) {
          right -= 0x00ff
        }
    
        left += right
        if (left > 0x00ff) {
          left -= 0x00ff
        }
      }
    
      return toFixedHex((left << 8) + right, 4)
    }
    
    // Format the key (XXXX-XXXX-XXXX-XXXX-XXXX)
    function formatKey(key) {
      return key.match(/.{4}/g).join('-')
    }
    
    // Generate a 4-byte hexadecimal seed value
    function generateSeed(n) {
      const seed = crypto.randomBytes(4).toString('hex')
    
      return seed.toUpperCase()
    }
    
    // Generate a (legitimate) license key
    function generateKey(seed) {
      // Build a list of subkeys (bit twiddling params are arbitrary but can never change)
      const subkeys = [
        getSubkeyFromSeed(seed, 24, 3, 200),
        getSubkeyFromSeed(seed, 10, 0, 56),
        getSubkeyFromSeed(seed, 1, 2, 91),
        getSubkeyFromSeed(seed, 7, 1, 100),
      ]
    
      // Build the serial (seed + subkeys)
      const serial = seed + subkeys.join('')
    
      // Build the key (serial + checksum)
      const key = serial + getChecksumForSerial(serial)
    
      return formatKey(key)
    }
    _content_copy_

Yeah â it's a lot to take in. Most readers won't be comfortable with all of those magic numbers and the nifty bit-twiddling. (And rightly so â it _is_ confusing, even to me, as I port over the Delphi code and write this post.)

But with that, let's generate our first license key:
    
    
    const seed = generateSeed()
    
    const key = generateKey(seed)
    
     
    
    console.log({ key })
    
    // => { key: 'ECE4-4EDB-37E8-7FF9-BC96' }
    
    const seed = generateSeed()
    const key = generateKey(seed)
    
    console.log({ key })
    // => { key: 'ECE4-4EDB-37E8-7FF9-BC96' }
    _content_copy_

Next, let's break down this new key, `ECE4-4EDB-37E8-7FF9-BC96`. Let's recall the components of a key: the **seed** , its **subkeys** , and the **checksum**.

In this case, we can strip away the dashes and see our components:
    
    
    Seed:     'ECE44EDB'
    
    Subkeys:  '37', 'E8', '7F', 'F9'
    
    Checksum: 'BC96'
    
    Seed:     'ECE44EDB'
    Subkeys:  '37', 'E8', '7F', 'F9'
    Checksum: 'BC96'
    _content_copy_

Now, a keygen for production-use may have more subkeys, or the subkeys may be arranged or intermingled differently, but the algorithm is still going to be more or less the same. As will the algorithm's vulnerabilities.

So, how do we verify these license keys?

Well, let's remember, the "P" in "PKV" stands for "partial" â Partial Key Verification. Our license key verification algorithm should only verify one subkey at a time, which we can rotate as-needed, or per version of our app.

Here's what the verification algorithm looks like:
    
    
    function isKeyFormatValid(key) {
    
      return key.length === 24 && key.replace(/-/g, '').length === 20
    
    }
    
     
    
    function isSeedFormatValid(seed) {
    
      return seed.match(/[A-F0-9]{8}/) != null
    
    }
    
     
    
    function isSerialChecksumValid(serial, checksum) {
    
      const c = getChecksumForSerial(serial)
    
     
    
      return c === checksum
    
    }
    
     
    
    function isKeyValid(key) {
    
      if (!isKeyFormatValid(key)) {
    
        return false
    
      }
    
     
    
      const [, serial, checksum] = key.replace(/-/g, '').match(/(.{16})(.{4})/)
    
      if (!isSerialChecksumValid(serial, checksum)) {
    
        return false
    
      }
    
     
    
      const seed = serial.substring(0, 8)
    
      if (!isSeedFormatValid(seed)) {
    
        return false
    
      }
    
     
    
      // Verify 0th subkey
    
      const expected = getSubkeyFromSeed(seed, 24, 3, 200)
    
      const actual = serial.substring(8, 10)
    
      if (actual !== expected) {
    
        return false
    
      }
    
     
    
      return true
    
    }
    
    function isKeyFormatValid(key) {
      return key.length === 24 && key.replace(/-/g, '').length === 20
    }
    
    function isSeedFormatValid(seed) {
      return seed.match(/[A-F0-9]{8}/) != null
    }
    
    function isSerialChecksumValid(serial, checksum) {
      const c = getChecksumForSerial(serial)
    
      return c === checksum
    }
    
    function isKeyValid(key) {
      if (!isKeyFormatValid(key)) {
        return false
      }
    
      const [, serial, checksum] = key.replace(/-/g, '').match(/(.{16})(.{4})/)
      if (!isSerialChecksumValid(serial, checksum)) {
        return false
      }
    
      const seed = serial.substring(0, 8)
      if (!isSeedFormatValid(seed)) {
        return false
      }
    
      // Verify 0th subkey
      const expected = getSubkeyFromSeed(seed, 24, 3, 200)
      const actual = serial.substring(8, 10)
      if (actual !== expected) {
        return false
      }
    
      return true
    }
    _content_copy_

The gist of the verification algorithm is that we firstly check key formatting, then we'll verify the checksum is valid. Next, we'll verify the format of the seed value, which if we recall is the first 8 characters of the serial.

And then we hit the meat and potatoes of PKV: verifying the _nth_ subkey.
    
    
    // Verify 0th subkey
    
    const expected = getSubkeyFromSeed(seed, 24, 3, 200)
    
    const actual = serial.substring(8, 10)
    
    if (actual !== expected) {
    
      return false
    
    }
    
    // Verify 0th subkey
    const expected = getSubkeyFromSeed(seed, 24, 3, 200)
    const actual = serial.substring(8, 10)
    if (actual !== expected) {
      return false
    }
    _content_copy_

If you notice, `getSubkeyFromSeed(seed, 24, 3, 200)` is deriving an expected 0th subkey from the seed value. We then compare the expected 0th subkey to our license key's actual 0th subkey. If the subkeys don't match, the license key is not valid.

But if we're including the exact 0th subkey parameters, which are used by our secret keygen, in our application code, isn't that bad? Absolutely! This is how we break PKV. And thus comes the moment we've all been waiting for â _let 's write an 'illegal' keygen._

#### Writing a keygen

Let's assume the role of a bad actor. And let's review what we know so far:

  1. The current version of the application verifies the 0th subkey.
  2. The 0th subkey is located at indices 8 and 9: `0000-0000-XX00-0000-0000`.
  3. We possess the parameters to generate a valid 0th subkey: `24, 3, 200`.



Let's write a keygen, using only the operations contained within the verification code, that generates a license key with a valid 0th subkey.
    
    
    const seed = '00000000'
    
    const subkey = getSubkeyFromSeed(seed, 24, 3, 200)
    
    const serial = `${seed}${subkey}000000`
    
    const checksum = getChecksumForSerial(serial)
    
    const key = `${serial}${checksum}`.match(/.{4}/g).join('-')
    
     
    
    console.log({ key })
    
    // => { key: '0000-0000-C800-0000-BBCD' }
    
    const seed = '00000000'
    const subkey = getSubkeyFromSeed(seed, 24, 3, 200)
    const serial = `${seed}${subkey}000000`
    const checksum = getChecksumForSerial(serial)
    const key = `${serial}${checksum}`.match(/.{4}/g).join('-')
    
    console.log({ key })
    // => { key: '0000-0000-C800-0000-BBCD' }
    _content_copy_

That's a lot of zeroes. Further, the only components that are _not_ zeroed out are the 0th subkey, and the checksum. But this can't possibly be a valid key, right?
    
    
    isKeyValid('0000-0000-C800-0000-BBCD')
    
    // => true
    
    isKeyValid('0000-0000-C800-0000-BBCD')
    // => true
    _content_copy_

Shoot â that's not good.

Well, actuallyâ¦ it's good for 'us', the bad actor; bad for the business whose application we just wrote a working keygen for. We need only increment the hexadecimal seed value to generate more valid license keys:
    
    
    -const seed = '00000000' 
    
    +const seed = '00000001' 
    
     const subkey = getSubkeyFromSeed(seed, 24, 3, 200)
    
     const serial = `${seed}${subkey}000000`
    
     const checksum = getChecksumForSerial(serial)
    
     const key = formatKey(`${serial}${checksum}`)
    
    const seed = '00000000' // [tl! --]
    const seed = '00000001' // [tl! ++]
    const subkey = getSubkeyFromSeed(seed, 24, 3, 200)
    const serial = `${seed}${subkey}000000`
    const checksum = getChecksumForSerial(serial)
    const key = formatKey(`${serial}${checksum}`)
    _content_copy_

Which we can then inspect,
    
    
    console.log({ key })
    
    // => { key: '0000-0001-C900-0000-CBCF' }
    
    console.log({ key })
    // => { key: '0000-0001-C900-0000-CBCF' }
    _content_copy_

And as expected,
    
    
    isKeyValid('0000-0001-C900-0000-CBCF')
    
    // => true
    
    isKeyValid('0000-0001-C900-0000-CBCF')
    // => true
    _content_copy_

Well, that's _doubly_ not good, for them. And as Murphy's Law would predict, this keygen has just been submitted to a popular online message board that the business has no control over. The keygen grows in popularity, sales dip, stakeholders are unhappy.

What can be done?

#### Verifying the next subkey

Let's assume the role of the business once again. We need to fix this. Luckily, our chosen key algorithm lets us go from verifying the 0th subkey, to verifying the 1st subkey. All we have to do is adjust the subkey parameters:
    
    
    -// Verify 0th subkey                                    
    
    -const expected = getSubkeyFromSeed(seed, 24, 3, 200) 
    
    -const actual = serial.substring(8, 10)               
    
    +// Verify 1st subkey                                    
    
    +const expected = getSubkeyFromSeed(seed, 10, 0, 56)  
    
    +const actual = serial.substring(10, 12)              
    
     if (actual !== expected) {
    
       return false
    
     }
    
    // Verify 0th subkey                                    [tl! --]
    const expected = getSubkeyFromSeed(seed, 24, 3, 200) // [tl! --]
    const actual = serial.substring(8, 10)               // [tl! --]
    // Verify 1st subkey                                    [tl! ++]
    const expected = getSubkeyFromSeed(seed, 10, 0, 56)  // [tl! ++]
    const actual = serial.substring(10, 12)              // [tl! ++]
    if (actual !== expected) {
      return false
    }
    _content_copy_

Let's quickly make this change and push out a silent update to limit any further damage this bad actor can inflict. Luckily, our app auto-updates so this should be a fast fix.

Problem solved, right?

Not quite.

#### Writing another keygen

Let's reclaim our role as bad actor. Users of our keygen are claiming that it no longer works, which is weird because it was most definitely working before. They're paying us in cryptocurrency, and even though we're a bad guy, we like to keep our customers happy.

We note: the first variable that has changed is that the application seems to have updated itself. After poking around the new version, we reassess the situation.

And these are the facts:

  1. The new version of the application no longer verifies the 0th subkey.
  2. The new version of the application now verifies the 1st subkey.
  3. The 1st subkey is located at indices 10 and 11: `0000-0000-00XX-0000-0000`.
  4. We possess the parameters to generate a valid 1st subkey: `10, 0, 56`.



See a pattern?

All 'they' did was move from verifying the 0th subkey to the 1st subkey. Let's adjust our keygen program so that it generates valid product keys once again:
    
    
     const seed = '00000000'
    
    -const subkey = getSubkeyFromSeed(seed, 24, 3, 200) 
    
    -const serial = `${seed}${subkey}000000`            
    
    +const subkey = getSubkeyFromSeed(seed, 10, 0, 56)  
    
    +const serial = `${seed}00${subkey}0000`            
    
     const checksum = getChecksumForSerial(serial)
    
     const key = `${serial}${checksum}`.match(/.{4}/g).join('-')
    
    const seed = '00000000'
    const subkey = getSubkeyFromSeed(seed, 24, 3, 200) // [tl! --]
    const serial = `${seed}${subkey}000000`            // [tl! --]
    const subkey = getSubkeyFromSeed(seed, 10, 0, 56)  // [tl! ++]
    const serial = `${seed}00${subkey}0000`            // [tl! ++]
    const checksum = getChecksumForSerial(serial)
    const key = `${serial}${checksum}`.match(/.{4}/g).join('-')
    _content_copy_

Which produces a new license key,
    
    
    console.log({ key })
    
    // => { key: '0000-0000-0038-0000-25BD' }
    
    console.log({ key })
    // => { key: '0000-0000-0038-0000-25BD' }
    _content_copy_

And, once again, as expected,
    
    
    isKeyValid('0000-0000-0038-0000-25BD')
    
    // => true
    
    isKeyValid('0000-0000-0038-0000-25BD')
    // => true
    _content_copy_

We can do this all day. All we need is some 90s KeyGen music.

* * *

As the business using PKV, we can continue adjusting our _nth_ subkey verification as-needed to combat these keygens as they pop up. We have alerts set up for various indicator keywords and everything.

But there's a major problem. (It may not be a problem _now_ , but it will be _soon_.)

Do you see it?

It's simple: once we start verifying the 2nd subkey, which the bad actor will once again write a keygen for, and then the 3rd subkey, _we 'll eventually run out of subkeys._ Even if we use 100 subkeys, running out is inevitable.

What does that mean, to "run out"?

It means that after we've rotated through verifying each of our subkeys, in our clever attempt at combatting the keygens, we'll soon have no more recourse. Sure, we can start blacklisting seed values directly in our application code, but that's a fool's errand when there's something _worse_ than running out of subkeys.

What's "worse"?

Well, at the end of this scenario, once all subkey parameters have been leaked, _the bad actor can fully replicate our secret keygen!_ (After all, _we 've literally given them the keys to our castle._ It was a slow trickle, but they were patient.)
    
    
    P0: 24, 3, 200
    
    P1: 10, 0, 56
    
    P2: 1, 2, 91
    
    P3: 7, 1, 100
    
    P0: 24, 3, 200
    P1: 10, 0, 56
    P2: 1, 2, 91
    P3: 7, 1, 100
    _content_copy_

It's game over after they get those.

#### So, what's the point?

To be frank, Partial Key Verification is _a lot_ of work, especially for a key algorithm that _we will eventually leak in its entirety._ PKV is flawed by its very nature. Sure, the more subkeys there are, the longer it will take to leak the entire algorithm. Maybe that's awhile. Or maybe the bad actor isn't sophisticated enough to keep a record of subkey parameters.

_But at the end of the day, we 're still leaking our secrets!_

Things that are wrong with PKV:

  1. You leak the license key generation algorithm over time. (I can't stress this enough!)
  2. You eventually have to maintain a blacklist of leaked/illegitimate keys.
  3. Given enough legitimate keys, your algorithm can be deduced.
  4. It's hard to embed data into a key (e.g. max app version).
  5. It's incredibly complex.



* * *

A quick tangent â

Most application licensing boils down to code that looks like this:
    
    
    if (isKeyValid(key)) {
    
      // â¦ do something
    
    } else {
    
      // â¦ do something else
    
    }
    
    if (isKeyValid(key)) {
      // â¦ do something
    } else {
      // â¦ do something else
    }
    _content_copy_

Some applications will have a central point in the bytecode where this check happens, but others harden their system by inlining the license key checks, making the work of a bad actor wanting to _crack_ the software much, much harder. But licensing is all essentially the same: _it 's a series of conditionals._

With that in mind, there's no benefit to using PKV, a licensing scheme that will eventually leak its secrets to any bad actor that is looking, vs. modern cryptography. It's not more secure, it's not easier to distribute, and it doesn't protect you from keygens. PKV is, by design, security through obscurity. And it should no longer be used.

* * *

So what's the alternative?

## Modern license key algorithms

When choosing a modern license key algorithm, we have a quite a few solid options. For example, our API supports a variety of cryptographic schemes for license keys, from elliptic-curve signatures, to RSA signatures and even encryption. Today, we'll be covering elliptic-curve and RSA-2048 signatures.

Cryptography is a wide space, but we're going to focus on asymmetric, or [public-key](https://en.wikipedia.org/wiki/Public-key_cryptography), cryptography. The way these asymmetric cryptographic schemes work is that they have a **private key** , and a **public key**. You take some data and create a **signature** of it using the private key, which can be **verified** using the public key. Verification is essentially an authenticity check, _" was this data signed by the private key?"_

As the names imply, the private key is our secret (i.e. it's never shared), the public key is public. In our case, we're going to embed the public key into our application code.

_There are symmetric schemes, such as AES-128, which forego public and private keys, and instead use a shared secret key. But those aren 't useful for license keys because we'd have to embed our secret key into our code to verify license keys, which would give a bad actor the ability to write a keygen (which was the end result of our PKV implementation)._

At the end of today, our cryptographic license keys are going to end up looking like this:
    
    
    ${ENCODED_DATA}.${ENCODED_SIGNATURE}
    
    ${ENCODED_DATA}.${ENCODED_SIGNATURE}
    _content_copy_

The license keys we generate may differ in length, depending on the cryptographic scheme we use, but the format is going to stay the same: some **encoded data** , a **delimiter** ".", and a cryptographic **signature** of the data. (This is more or less the same format our API uses for cryptographic keys.)

Let's start with asymmetric elliptic-curves.

### Elliptic-curve cryptography

We aren't going to be doing a deep-dive into [elliptic-curve cryptography](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography) (ECC) today, but that link should curb the curious. Within the ECC category, there are a myriad of different algorithms. Today, we'll be exploring **Ed25519** , a modern implementation of a Schnorr signature system using elliptic-curve groups.

_Ed25519 provides a 128-bit security level, the same security level as AES-128, NIST P-256, and RSA-3072. (Meaning, yes, it 's good.)_

#### An implementation of ECC

Now, rather than write our own crypto, we're going to be using Node's standard `crypto` module, which as of Node 12, supports Ed25519.

Let's generate our private and public keys, or more succinctly, our _keypair_.
    
    
    const crypto = require('crypto')
    
     
    
    const { privateKey, publicKey } = crypto.generateKeyPairSync('ed25519')
    
    const signingKey =
    
      privateKey.export({ type: 'pkcs8', format: 'der' }).toString('hex')
    
    const verifyKey =
    
      publicKey.export({ type: 'spki', format: 'der' }).toString('hex')
    
     
    
    console.log({ signingKey, verifyKey })
    
    // => {
    
    //      signingKey: '302e020100300506032b657004220420a9466527e2b4dd30f202742abe38e8d75c9756a4f3d22daf1e37a317c22e2197',
    
    //      verifyKey: '302a300506032b657003210092f97e92cf06959a8b469d9da95609a4419fa2cc4f03a7009cd3a7c6bc1423e9'
    
    //    }
    
    const crypto = require('crypto')
    
    const { privateKey, publicKey } = crypto.generateKeyPairSync('ed25519')
    const signingKey =
      privateKey.export({ type: 'pkcs8', format: 'der' }).toString('hex')
    const verifyKey =
      publicKey.export({ type: 'spki', format: 'der' }).toString('hex')
    
    console.log({ signingKey, verifyKey })
    // => {
    //      signingKey: '302e020100300506032b657004220420a9466527e2b4dd30f202742abe38e8d75c9756a4f3d22daf1e37a317c22e2197',
    //      verifyKey: '302a300506032b657003210092f97e92cf06959a8b469d9da95609a4419fa2cc4f03a7009cd3a7c6bc1423e9'
    //    }
    _content_copy_

After generating our keypair, we're going to want to keep those encoded keys in a safe place. We'll use the private **signing key** for our keygen, and we'll use the public **verify key** to verify authenticity of license keys within our application.

Let's write our license keygen. Thankfully, it's a lot simpler than our PKV code:
    
    
    // Some data we're going to embed into the license key
    
    const data = '[[email protected]](/cdn-cgi/l/email-protection)'
    
     
    
    // Generate a signature of the data
    
    const signature = crypto.sign(null, Buffer.from(data), privateKey)
    
     
    
    // Encode the signature and the dataset using our signing key
    
    const encodedSignature = signature.toString('base64')
    
    const encodedData = Buffer.from(data).toString('base64')
    
     
    
    // Combine the encoded data and signature to create a license key
    
    const licenseKey = `${encodedData}.${encodedSignature}`
    
     
    
    console.log({ licenseKey })
    
    // => { licenseKey: 'dXNlckBjdXN0b21lci5leGFtcGxl.kANuXAhc8b7rDNgbFBpoSUsmfkM7msQC0tNkeUed4b5W15xF6zxmoV3AYF54zaWFMHznSNY7M9bLloInknvlDw==' }
    
    // Some data we're going to embed into the license key
    const data = 'user@customer.example'
    
    // Generate a signature of the data
    const signature = crypto.sign(null, Buffer.from(data), privateKey)
    
    // Encode the signature and the dataset using our signing key
    const encodedSignature = signature.toString('base64')
    const encodedData = Buffer.from(data).toString('base64')
    
    // Combine the encoded data and signature to create a license key
    const licenseKey = `${encodedData}.${encodedSignature}`
    
    console.log({ licenseKey })
    // => { licenseKey: 'dXNlckBjdXN0b21lci5leGFtcGxl.kANuXAhc8b7rDNgbFBpoSUsmfkM7msQC0tNkeUed4b5W15xF6zxmoV3AYF54zaWFMHznSNY7M9bLloInknvlDw==' }
    _content_copy_

Once again, we can strip away any delimiters and see our components:
    
    
    Dataset: dXNlckBjdXN0b21lci5leGFtcGxl
    
    Signature: kANuXAhc8b7rDNgbFBpoSUsmfkM7msQC0tNkeUed4b5W15xF6zxmoV3AYF54zaWF
    
               MHznSNY7M9bLloInknvlDw==
    
    Dataset: dXNlckBjdXN0b21lci5leGFtcGxl
    Signature: kANuXAhc8b7rDNgbFBpoSUsmfkM7msQC0tNkeUed4b5W15xF6zxmoV3AYF54zaWF
               MHznSNY7M9bLloInknvlDw==
    _content_copy_

What's great about this license key format is that we can embed _any_ dataset into it that we need. Right now, we're embedding the customer's email, but we could include other information as well, such as order ID, key expiration date, entitlements, and more. (It could even be a JSON object, which is actually the default for our API.)

One downside is that the more data you embed, the larger the license keys will become. But in the real world, this isn't _really_ an issue, since the majority of users will copy-and-paste their license keys, as opposed to typing them in by hand.

So, what about verifying the keys? Again, it's pretty simple:
    
    
    // Split the license key by delimiter
    
    const [encodedData, encodedSignature] = licenseKey.split('.')
    
     
    
    // Decode the embedded data and its signature
    
    const signature = Buffer.from(encodedSignature, 'base64')
    
    const data = Buffer.from(encodedData, 'base64').toString()
    
     
    
    // Verify the data and its signature using our verify key
    
    const valid = crypto.verify(null, Buffer.from(data), publicKey, signature)
    
     
    
    console.log({ valid, data })
    
    // => { valid: true, data: '[[email protected]](/cdn-cgi/l/email-protection)' }
    
    // Split the license key by delimiter
    const [encodedData, encodedSignature] = licenseKey.split('.')
    
    // Decode the embedded data and its signature
    const signature = Buffer.from(encodedSignature, 'base64')
    const data = Buffer.from(encodedData, 'base64').toString()
    
    // Verify the data and its signature using our verify key
    const valid = crypto.verify(null, Buffer.from(data), publicKey, signature)
    
    console.log({ valid, data })
    // => { valid: true, data: 'user@customer.example' }
    _content_copy_

That's all the code you would need to add to your application to verify license keys (minus implementation details like prompting the user for their license key, etc.)

Another major downside is that Ed25519 may not be supported in many programming languages, outside of third-party dependencies. Most modern programming languages, given the version is up-to-date _should_ support it. For example, Node introduced support in Node 12; but Ruby, however, still lacks support in the standard library.

So, what's another alternative?

### RSA cryptography

[RSA](https://en.wikipedia.org/wiki/RSA_%28cryptosystem%29) (RivestâShamirâAdleman), is a widely supported cryptography system, and it's one of the oldest systems still in use. Like ECC, it's an asymmetric cryptography system, meaning it uses public-private keypairs to verify and sign data, respectively.

Due to its age, you may find outdated advice online recommending 512-bit keys, or even smaller. A modern use of RSA should utilize 2048-, 3072- or 4096-bit keys. The higher the bit size, the higher the security level. (Though, we should also keep in mind: the higher the bit size, the longer the signatures will be.)

For our implementation, we're going to use **RSA-2048**.

#### An implementation of RSA

We're going to be returning to our old friend, Node's `crypto` module. It has full support for RSA, like most programming languages do. Our RSA license keygen will be very similar to its ECC counterpart.

So, let's generate an RSA keypair: (Brace yourself.)
    
    
    const crypto = require('crypto')
    
     
    
    // Generate a new keypair
    
    const { privateKey, publicKey } = crypto.generateKeyPairSync('rsa', {
    
      modulusLength: 2048,
    
      privateKeyEncoding: { type: 'pkcs1', format: 'pem' },
    
      publicKeyEncoding: { type: 'pkcs1', format: 'pem' },
    
    })
    
     
    
    console.log({ privateKey, publicKey })
    
    // => {
    
    //      privateKey: '-----BEGIN RSA PRIVATE KEY-----\n' +
    
    //        'MIIEpAIBAAKCAQEAqYYo2aSU3EPASo3vAb1pXyU3vdAP1V73qGKcPvWJ1+DlCZJh\n' +
    
    //        'BTlY/IyBYJCoaHiized1ynjiUNOvC5zbEGUOjRJBnUzX8ep53BeoCyWRfA1wRo5S\n' +
    
    //        'easxpNyNE9yJKT/Cyv91jCxH4aOpt8jjTTbvZLh1YnqWI1Bc4YCUKVTA1wV63qzp\n' +
    
    //        'A/ghBCsB6Hhq7Phlngcs+gQYMH4WRkGxwMAeqOJ/UmaK1cMCSZ1yMgN/+Svp1B8a\n' +
    
    //        'iBZ5FAm/0uqh89TWr6ABihIRu9Q6Lan7nr33vB0Fl36KOlPSpJyonWUlFx4crAdR\n' +
    
    //        'NnOO+vfmhMCjQnqNLEzltqrmY7sAZNT2gkmTdwIDAQABAoIBAGCKYHUhfwy5IKbU\n' +
    
    //        'kYoCHiHrBgV4mau/e3ZPQf+wwSFJl+WNkObys7SPJ5agiueD2+M6rx/xG6FAC+2n\n' +
    
    //        'FDIP+utnvCoies/v4hnu9unyKRnmZUwo/NsBHTJvz3/CFfKBtyL3vC9pgD4FgD+D\n' +
    
    //        'jb6JTGeljGPav+m4eEyLdtTayT8pmE2ZQ6qelGW1M+Jd9JN7XYNKzmR8kI4rhug0\n' +
    
    //        'cFf87FGZ7PI8uEXeTWIysS/ZMkxk+dDifaFIpBEFKPdinaotl9raE+pcgeV/+ktQ\n' +
    
    //        'T7RsjEYstRH1VFA9z8Lf1w7RLwdGNMRzv6y69eac/N+FpUsDgRyfXS+JD+KnS6xV\n' +
    
    //        'bW9hAeECgYEA2I8VcZDwPu2qRnyrU4ZWH7Dskv05KFTmxw8/E2oUVnhSnYOaBzAY\n' +
    
    //        'O6DLUNObY3QPFaKzsQv+i5yDL5HHqIDuPEapiZ0g0DDbRQ5+mzxJy92jgP/qouXn\n' +
    
    //        'yCWIun62VjoZqHU4PKWorPoSYrZRzDUtdiNSB+ulmhlt4sbWvB9fXt8CgYEAyGYb\n' +
    
    //        'Ss9vxBjvC4MqLaf2J5cWSEkFA4LjEaz+TqGluuSWbAim4Yu/vjEV7l+jguPNZcm0\n' +
    
    //        'u8+KeyrGtggEDz3z4eTQOtkWwrA0icQaKqT1iBRaoREpYMS4bOFjEoYsVTuAaeEs\n' +
    
    //        'v8E94VkSmONdH7pQEObtb/T71hSO1qr6FjELlmkCgYBaaGGrZ7bkjpPnmWRtGkga\n' +
    
    //        'MuKQ+uZB0DAIKnVKxZ53+wOCfs5u8cUsH5TByZW1j148yg/6eedqoYyi71lLH4hV\n' +
    
    //        '4aolqVNplvvzeHmilSi5023PDQgHubNp+0F5mizFErxjd4xixUYF8OB8FWFQv2Kb\n' +
    
    //        'T2OPqvEXxEX7xscfAnnuQQKBgQDCI7kY9nDuZsFeQ8mexXMA06vwh1zmE+zq+M69\n' +
    
    //        'Wnh14HGhY5hYNMyi8mausdR0P0CC9a+zqtIblEtBme5k3b3g/4yDFkCoh4++T06S\n' +
    
    //        'NZDwLdfG5htR9gI86PTTw0w7nhM/f7ecZRcPsv0DRHC5BgP++9jWd11p/iyK5sS0\n' +
    
    //        'rvrs0QKBgQC8I8nSwZIMu+jIMoMbL22hrwrghQ7g48MeDcxBBxAlnLbBdDl3bDeD\n' +
    
    //        'FkDlFFTu8EqMz7MslbHH44iHU/WG1HBe7tGZqVEraKKlsQB3ULHkhi/m1pjKmFek\n' +
    
    //        'QtiGtNPLB5zZk434moQb2/n772N+2OayxGbULkWhVqlw1OGXWVOnkw==\n' +
    
    //        '-----END RSA PRIVATE KEY-----\n',
    
    //      publicKey: '-----BEGIN RSA PUBLIC KEY-----\n' +
    
    //        'MIIBCgKCAQEAqYYo2aSU3EPASo3vAb1pXyU3vdAP1V73qGKcPvWJ1+DlCZJhBTlY\n' +
    
    //        '/IyBYJCoaHiized1ynjiUNOvC5zbEGUOjRJBnUzX8ep53BeoCyWRfA1wRo5Seasx\n' +
    
    //        'pNyNE9yJKT/Cyv91jCxH4aOpt8jjTTbvZLh1YnqWI1Bc4YCUKVTA1wV63qzpA/gh\n' +
    
    //        'BCsB6Hhq7Phlngcs+gQYMH4WRkGxwMAeqOJ/UmaK1cMCSZ1yMgN/+Svp1B8aiBZ5\n' +
    
    //        'FAm/0uqh89TWr6ABihIRu9Q6Lan7nr33vB0Fl36KOlPSpJyonWUlFx4crAdRNnOO\n' +
    
    //        '+vfmhMCjQnqNLEzltqrmY7sAZNT2gkmTdwIDAQAB\n' +
    
    //        '-----END RSA PUBLIC KEY-----\n'
    
    //    }
    
    const crypto = require('crypto')
    
    // Generate a new keypair
    const { privateKey, publicKey } = crypto.generateKeyPairSync('rsa', {
      modulusLength: 2048,
      privateKeyEncoding: { type: 'pkcs1', format: 'pem' },
      publicKeyEncoding: { type: 'pkcs1', format: 'pem' },
    })
    
    console.log({ privateKey, publicKey })
    // => {
    //      privateKey: '-----BEGIN RSA PRIVATE KEY-----\n' +
    //        'MIIEpAIBAAKCAQEAqYYo2aSU3EPASo3vAb1pXyU3vdAP1V73qGKcPvWJ1+DlCZJh\n' +
    //        'BTlY/IyBYJCoaHiized1ynjiUNOvC5zbEGUOjRJBnUzX8ep53BeoCyWRfA1wRo5S\n' +
    //        'easxpNyNE9yJKT/Cyv91jCxH4aOpt8jjTTbvZLh1YnqWI1Bc4YCUKVTA1wV63qzp\n' +
    //        'A/ghBCsB6Hhq7Phlngcs+gQYMH4WRkGxwMAeqOJ/UmaK1cMCSZ1yMgN/+Svp1B8a\n' +
    //        'iBZ5FAm/0uqh89TWr6ABihIRu9Q6Lan7nr33vB0Fl36KOlPSpJyonWUlFx4crAdR\n' +
    //        'NnOO+vfmhMCjQnqNLEzltqrmY7sAZNT2gkmTdwIDAQABAoIBAGCKYHUhfwy5IKbU\n' +
    //        'kYoCHiHrBgV4mau/e3ZPQf+wwSFJl+WNkObys7SPJ5agiueD2+M6rx/xG6FAC+2n\n' +
    //        'FDIP+utnvCoies/v4hnu9unyKRnmZUwo/NsBHTJvz3/CFfKBtyL3vC9pgD4FgD+D\n' +
    //        'jb6JTGeljGPav+m4eEyLdtTayT8pmE2ZQ6qelGW1M+Jd9JN7XYNKzmR8kI4rhug0\n' +
    //        'cFf87FGZ7PI8uEXeTWIysS/ZMkxk+dDifaFIpBEFKPdinaotl9raE+pcgeV/+ktQ\n' +
    //        'T7RsjEYstRH1VFA9z8Lf1w7RLwdGNMRzv6y69eac/N+FpUsDgRyfXS+JD+KnS6xV\n' +
    //        'bW9hAeECgYEA2I8VcZDwPu2qRnyrU4ZWH7Dskv05KFTmxw8/E2oUVnhSnYOaBzAY\n' +
    //        'O6DLUNObY3QPFaKzsQv+i5yDL5HHqIDuPEapiZ0g0DDbRQ5+mzxJy92jgP/qouXn\n' +
    //        'yCWIun62VjoZqHU4PKWorPoSYrZRzDUtdiNSB+ulmhlt4sbWvB9fXt8CgYEAyGYb\n' +
    //        'Ss9vxBjvC4MqLaf2J5cWSEkFA4LjEaz+TqGluuSWbAim4Yu/vjEV7l+jguPNZcm0\n' +
    //        'u8+KeyrGtggEDz3z4eTQOtkWwrA0icQaKqT1iBRaoREpYMS4bOFjEoYsVTuAaeEs\n' +
    //        'v8E94VkSmONdH7pQEObtb/T71hSO1qr6FjELlmkCgYBaaGGrZ7bkjpPnmWRtGkga\n' +
    //        'MuKQ+uZB0DAIKnVKxZ53+wOCfs5u8cUsH5TByZW1j148yg/6eedqoYyi71lLH4hV\n' +
    //        '4aolqVNplvvzeHmilSi5023PDQgHubNp+0F5mizFErxjd4xixUYF8OB8FWFQv2Kb\n' +
    //        'T2OPqvEXxEX7xscfAnnuQQKBgQDCI7kY9nDuZsFeQ8mexXMA06vwh1zmE+zq+M69\n' +
    //        'Wnh14HGhY5hYNMyi8mausdR0P0CC9a+zqtIblEtBme5k3b3g/4yDFkCoh4++T06S\n' +
    //        'NZDwLdfG5htR9gI86PTTw0w7nhM/f7ecZRcPsv0DRHC5BgP++9jWd11p/iyK5sS0\n' +
    //        'rvrs0QKBgQC8I8nSwZIMu+jIMoMbL22hrwrghQ7g48MeDcxBBxAlnLbBdDl3bDeD\n' +
    //        'FkDlFFTu8EqMz7MslbHH44iHU/WG1HBe7tGZqVEraKKlsQB3ULHkhi/m1pjKmFek\n' +
    //        'QtiGtNPLB5zZk434moQb2/n772N+2OayxGbULkWhVqlw1OGXWVOnkw==\n' +
    //        '-----END RSA PRIVATE KEY-----\n',
    //      publicKey: '-----BEGIN RSA PUBLIC KEY-----\n' +
    //        'MIIBCgKCAQEAqYYo2aSU3EPASo3vAb1pXyU3vdAP1V73qGKcPvWJ1+DlCZJhBTlY\n' +
    //        '/IyBYJCoaHiized1ynjiUNOvC5zbEGUOjRJBnUzX8ep53BeoCyWRfA1wRo5Seasx\n' +
    //        'pNyNE9yJKT/Cyv91jCxH4aOpt8jjTTbvZLh1YnqWI1Bc4YCUKVTA1wV63qzpA/gh\n' +
    //        'BCsB6Hhq7Phlngcs+gQYMH4WRkGxwMAeqOJ/UmaK1cMCSZ1yMgN/+Svp1B8aiBZ5\n' +
    //        'FAm/0uqh89TWr6ABihIRu9Q6Lan7nr33vB0Fl36KOlPSpJyonWUlFx4crAdRNnOO\n' +
    //        '+vfmhMCjQnqNLEzltqrmY7sAZNT2gkmTdwIDAQAB\n' +
    //        '-----END RSA PUBLIC KEY-----\n'
    //    }
    _content_copy_

Right off the bat, we can see that RSA's keys are much, much larger the Ed25519's. But that's okay, they both get us to our end goal: a cryptographically secure licensing system. Again, you'll want to store these keys in a safe place. As before, and as the names imply, the private key is private, and the public key can be public.
    
    
    // Some data we're going to embed into the license key
    
    const data = '[[email protected]](/cdn-cgi/l/email-protection)'
    
     
    
    // Create an RSA signer
    
    const signer = crypto.createSign('rsa-sha256')
    
    signer.update(data)
    
     
    
    // Encode the original data
    
    const encoded = Buffer.from(data).toString('base64')
    
     
    
    // Generate a signature for the data using our private key
    
    const signature = signer.sign(privateKey, 'base64')
    
     
    
    // Combine the encoded data and signature to create a license key
    
    const licenseKey = `${encoded}.${signature}`
    
     
    
    console.log({ licenseKey })
    
    // => {
    
    //      licenseKey: 'dXNlckBjdXN0b21lci5leGFtcGxl.mEuxvjm1wlrv02ujafM63shjrjZ3edR07adIvR4vQoaJlQ0PSgiCX6DlLFeP6Qzaz1YZDLHvh3hALEujKZCutJlFhrxhuHJ+H2cAGyMHLoxeCNJHrGBwcW4IP3sGeSVxgWFwUl1twEw5Xb9jdEbxadszCP34YQrKrf/NlmHCDLIP/5eEla02nUGnHOkZ0b3HJAM20sJbulZFfrqqKakkYziJDBiQ0DFjvpTp4xwHEDHsNORle128CMrnpN1PcPuteoKoiMFBha3+hLo9zkUyYBa34KaIZ2RKttF+cOj6MqK1zbC1SVQz2znwEletZdC4a9MMGd0UWNEL9jNzdhMAGw=='
    
    //    }
    
    // Some data we're going to embed into the license key
    const data = 'user@customer.example'
    
    // Create an RSA signer
    const signer = crypto.createSign('rsa-sha256')
    signer.update(data)
    
    // Encode the original data
    const encoded = Buffer.from(data).toString('base64')
    
    // Generate a signature for the data using our private key
    const signature = signer.sign(privateKey, 'base64')
    
    // Combine the encoded data and signature to create a license key
    const licenseKey = `${encoded}.${signature}`
    
    console.log({ licenseKey })
    // => {
    //      licenseKey: 'dXNlckBjdXN0b21lci5leGFtcGxl.mEuxvjm1wlrv02ujafM63shjrjZ3edR07adIvR4vQoaJlQ0PSgiCX6DlLFeP6Qzaz1YZDLHvh3hALEujKZCutJlFhrxhuHJ+H2cAGyMHLoxeCNJHrGBwcW4IP3sGeSVxgWFwUl1twEw5Xb9jdEbxadszCP34YQrKrf/NlmHCDLIP/5eEla02nUGnHOkZ0b3HJAM20sJbulZFfrqqKakkYziJDBiQ0DFjvpTp4xwHEDHsNORle128CMrnpN1PcPuteoKoiMFBha3+hLo9zkUyYBa34KaIZ2RKttF+cOj6MqK1zbC1SVQz2znwEletZdC4a9MMGd0UWNEL9jNzdhMAGw=='
    //    }
    _content_copy_

And as expected, like our keypair, our license keys are also much larger. But they're secure. And remember, most users copy-and-paste, so length doesn't really matter. (You could even wrap license keys in a `license.dat` file, which makes distribution a breeze. But that's just an implementation detail.)

Let's break down the license key into its **dataset** and **signature** components:
    
    
    Dataset: dXNlckBjdXN0b21lci5leGFtcGxl
    
    Signature: mEuxvjm1wlrv02ujafM63shjrjZ3edR07adIvR4vQoaJlQ0PSgiCX6DlLFeP6Qza
    
               z1YZDLHvh3hALEujKZCutJlFhrxhuHJ+H2cAGyMHLoxeCNJHrGBwcW4IP3sGeSVx
    
               gWFwUl1twEw5Xb9jdEbxadszCP34YQrKrf/NlmHCDLIP/5eEla02nUGnHOkZ0b3H
    
               JAM20sJbulZFfrqqKakkYziJDBiQ0DFjvpTp4xwHEDHsNORle128CMrnpN1PcPut
    
               eoKoiMFBha3+hLo9zkUyYBa34KaIZ2RKttF+cOj6MqK1zbC1SVQz2znwEletZdC4
    
               a9MMGd0UWNEL9jNzdhMAGw==
    
    Dataset: dXNlckBjdXN0b21lci5leGFtcGxl
    Signature: mEuxvjm1wlrv02ujafM63shjrjZ3edR07adIvR4vQoaJlQ0PSgiCX6DlLFeP6Qza
               z1YZDLHvh3hALEujKZCutJlFhrxhuHJ+H2cAGyMHLoxeCNJHrGBwcW4IP3sGeSVx
               gWFwUl1twEw5Xb9jdEbxadszCP34YQrKrf/NlmHCDLIP/5eEla02nUGnHOkZ0b3H
               JAM20sJbulZFfrqqKakkYziJDBiQ0DFjvpTp4xwHEDHsNORle128CMrnpN1PcPut
               eoKoiMFBha3+hLo9zkUyYBa34KaIZ2RKttF+cOj6MqK1zbC1SVQz2znwEletZdC4
               a9MMGd0UWNEL9jNzdhMAGw==
    _content_copy_

_That signature_ , aye? If we were to use a smaller key size, the signature size could be reduced, but we shouldn't sacrifice security for such a thing. RSA-512 can be broken within _days_ , for less than $100 in compute-power. Similarly, even RSA-1024 can be broken, though for a much larger sum. RSA-2048 would take around a billion years to break on modern systems (quantum computing aside.)

Suffice it to say â RSA-2048 is a safe choice in 2021. RSA-3072, even moreso.

But I digress â

Similarly to ECC, verifying an RSA license key is a rather painless process:
    
    
    // Split the license key's data and the signature by delimiter
    
    const [encoded, signature] = licenseKey.split('.')
    
     
    
    // Decode the embedded data
    
    const data = Buffer.from(encoded, 'base64').toString()
    
     
    
    // Create an RSA verifier
    
    const verifier = crypto.createVerify('rsa-sha256')
    
    verifier.update(data)
    
     
    
    // Verify the signature for the data using our public key
    
    const valid = verifier.verify(publicKey, signature, 'base64')
    
     
    
    console.log({ valid, data })
    
    // => { valid: true, data: '[[email protected]](/cdn-cgi/l/email-protection)' }
    
    // Split the license key's data and the signature by delimiter
    const [encoded, signature] = licenseKey.split('.')
    
    // Decode the embedded data
    const data = Buffer.from(encoded, 'base64').toString()
    
    // Create an RSA verifier
    const verifier = crypto.createVerify('rsa-sha256')
    verifier.update(data)
    
    // Verify the signature for the data using our public key
    const valid = verifier.verify(publicKey, signature, 'base64')
    
    console.log({ valid, data })
    // => { valid: true, data: 'user@customer.example' }
    _content_copy_

Once again, it takes less than 10 lines of code to verify license keys within your application. Our RSA implementation can be improved by using a more modern non-deterministic padding scheme, PKCS1-PSS (which our API also supports.)

* * *

## Caveats and summary

We've learned how legacy licensing systems, such as Partial Key Verification, can be compromised by a bad actor, and how PKV is insecure by-design. We even wrote a PKV keygen ourselves. We then wrote a couple secure licensing systems using modern cryptography, implementing Ed25519 and RSA-2048 signature verification.

* * *

Okay, okay â after all we've been through with PKVâ¦

You may be asking yourself â

**" What about keygens?"**

The good news is that unless a bad actor can break Ed25519 or RSA-2048, writing a keygen is effectively impossible. Besides, if a bad actor can break Ed25519 or RSA-2048 in 2021, we'll have much bigger things to worry about, anyways.

But remember, a crack != a keygen, so your application's licensing always runs the risk of being circumvented via code modification. But license keys cannot be _forged_ when you utilize a licensing system built on modern cryptography.

(When it comes to cracking, we _can_ defend against some low-hanging-fruit, but we'll leave that topic for another day.)

* * *

Now, where does a licensing **server** fit in?

Generating and verifying the authenticity of cryptographically signed license keys like we've covered will work great for a lot of licensing needs. The implementation is straight forward, it's secure, and these types of license keys work especially great for offline-first perpetual licenses (or a timed license with an embedded, immutable expiry).

But coupled with a modern licensing server, cryptographic keys can be used to implement [more complex licensing models](/docs/choosing-a-licensing-model), such as these popular ones:

  * An entitlement-based model that gates access to certain features or versions of an application by a license's entitlements. For example, [Sublime Text 4](https://www.sublimetext.com/blog/articles/sublime-text-4) allows for a few years of updates, but after a license expires, only the versions within that 3 year window can be accessed, according to the license's entitlements.
  * A node-locked or floating model where a license is limited to the number of devices it can be used on at one time. For example, [Sketch](https://www.sketch.com/pricing/) allows you to purchase licenses by seat-count, where a user can activate and deactivate device "seats."
  * Device-locked timed trials where a device can sign up for a single trial, without risk of the user signing up for a second, third or fourth trial.



But rather than [build a licensing server in-house](/build-vs-buy/), that's where our software licensing API can come in and save your team time and money.

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


