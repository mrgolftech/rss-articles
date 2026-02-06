# How to License and Distribute a Private Node Module

**来源:** https://keygen.sh
**链接:** https://keygen.sh/blog/how-to-license-and-distribute-commercial-node-modules/
**日期:** Wed, 04 Aug 2021 05:00:00 GMT

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
    * [_support_ Get Support ](/cdn-cgi/l/email-protection#b6c5c3c6c6d9c4c2f6ddd3cfd1d3d898c5de)
  * [Pricing ](/pricing/)
  * [Log in ](https://app.keygen.sh/login)
  * [Sign Up](https://app.keygen.sh/register?plan=984180df-07b3-4dc1-b138-ca68a0f913ed)



# How to License and Distribute a Private Node Module

Wednesday, August 4th 2021

**This blog post is outdated.** We now offer an official npm engine for distributing private packages. Please see [the docs](/docs/api/engines/#engines-npm) to get started. We're leaving this blog post up for posterity, because it may still be helpful for those wanting to use an S3-compatible service for distributing packages.

_Last month, we quietly launched "version 2" of our distribution API. While version 1 will continue to see maintenance, we made the decision to build a better version from the ground up â one that is [fully integrated into our flagship software licensing API](/docs/api/releases/). This has been a goal of ours since, really, early 2018 when we first launched Keygen Dist. We're excited to get this new version into the hands of our customers!_

_Over the next few months, we 'll be showcasing how to license and distribute various types of commercial software using our API, including Node modules, PHP packages, RubyGems, cross-platform [Electron apps](/blog/how-to-license-and-distribute-an-electron-app/), and Docker images._

_Today, we 'll start with distributing a private npm package._

* * *

Have you ever built an awesome set of React components, or a slick Tailwind theme, and wondered how you could sell it? Or perhaps you maintain an open source Node module and you want to dual-license it to businesses and enterprises, Ã la [Sidekiq](https://sidekiq.org/)?

Well, today we're going to cover how to license and distribute a private Node module that can be installed via npm through a private package registry, Keygen.

## Creating a private module

The module that we'll be creating today will be a simple `@demo/hello-world` package. Using npm **package scopes** , e.g. `@scope/package`, we'll be able to configure npm to use a private registry for specific packages under that scope.

To get things kicked off, let's create a new directory for our module:
    
    
    mkdir hello-world
    
    cd hello-world
    
    mkdir hello-world
    cd hello-world
    _content_copy_

Then we'll create a new `package.json` for our private module:
    
    
    touch package.json
    
    touch package.json
    _content_copy_

And we'll populate it with the following JSON:
    
    
    {
    
      "private": true,
    
      "name": "@demo/hello-world",
    
      "version": "1.0.0",
    
      "main": "index.js",
    
      "files": []
    
    }
    
    {
      "private": true,
      "name": "@demo/hello-world",
      "version": "1.0.0",
      "main": "index.js",
      "files": []
    }
    _content_copy_

**Note that the package name is scoped to`@demo`. We'll get into this more a bit later on, but this is very important.** Without that scope, npm will attempt to install our module from `registry.npmjs.org`, instead of installing from our private registry. 

Next, let's create our module's `index.js` file:
    
    
    touch index.js
    
    touch index.js
    _content_copy_

Finally, we'll add our package's logic:
    
    
    module.exports = () => 'hello world'
    
    module.exports = () => 'hello world'
    _content_copy_

## Publishing a private module

We'll be using our `demo` Keygen account and product, but feel free to pass in your own identifiers if you're following along. You'll also need to [generate a secret product token](https://app.keygen.sh/tokens/product/new) in order to have permission to create and upload release artifacts.

### Packaging the module

The first step in publishing our Node module is to `pack` it up into a gzipped tarball, the format that npm expects from a registry. Let's go ahead and do that:
    
    
    mkdir dist
    
    npm pack --pack-destination dist
    
    mkdir dist
    npm pack --pack-destination dist
    _content_copy_

This should create a new tarball `dist/demo-hello-world-1.0.0.tgz`. If not, you may need to upgrade npm to v7. At time of writing, I'm on Node v16.6.1, npm v7.20.3.

### Publishing the module

Next, let's publish our tarball. We'll create a new release using `curl` with the filename `@demo/hello-world/1.0.0.tgz`, which is again, what npm expects when requesting a specific version tarball from a registry:

_(If you 're not a fan of `curl`, we'll link to a GitHub repo at the bottom of this article that codifies all these steps, written in Node.)_
    
    
    curl -v -X PUT 'https://api.keygen.sh/v1/accounts/demo/releases' \
    
      -u token:prod-1d2dedc2b12a376cfc5ee0622e9c0803ef1755d29baff43e8a8b0e790413f645v3 \
    
      -H 'content-type: application/json' \
    
      -d '{
    
            "data": {
    
              "type": "release",
    
              "attributes": {
    
                "status": "PUBLISHED",
    
                "channel": "stable",
    
                "version": "1.0.0"
    
              },
    
              "relationships": {
    
                "product": {
    
                  "data": {
    
                    "type": "product",
    
                    "id": "855ef427-6f68-4153-ab88-e63c631014c3"
    
                  }
    
                }
    
              }
    
            }
    
          }'
    
    # => {
    
    #      "data": {
    
    #        "id": "5b4c27ab-8b1e-4257-b056-1db82a4ce8cf",
    
    #        "type": "releases",
    
    #        ...
    
    #      }
    
    #    }
    
    curl -v -X PUT 'https://api.keygen.sh/v1/accounts/demo/releases' \
      -u token:prod-1d2dedc2b12a376cfc5ee0622e9c0803ef1755d29baff43e8a8b0e790413f645v3 \
      -H 'content-type: application/json' \
      -d '{
            "data": {
              "type": "release",
              "attributes": {
                "status": "PUBLISHED",
                "channel": "stable",
                "version": "1.0.0"
              },
              "relationships": {
                "product": {
                  "data": {
                    "type": "product",
                    "id": "855ef427-6f68-4153-ab88-e63c631014c3"
                  }
                }
              }
            }
          }'
    # => {
    #      "data": {
    #        "id": "5b4c27ab-8b1e-4257-b056-1db82a4ce8cf",
    #        "type": "releases",
    #        ...
    #      }
    #    }
    _content_copy_

We'll want to note our new release's ID so that we can create and upload our first artifact: our packed `demo-hello-world-1.0.0.tgz` tarball:
    
    
    curl -v -X POST 'https://api.keygen.sh/v1/accounts/demo/artifacts' \
    
      -u token:prod-1d2dedc2b12a376cfc5ee0622e9c0803ef1755d29baff43e8a8b0e790413f645v3 \
    
      -H 'content-type: application/json' \
    
      -d '{
    
            "data": {
    
              "type": "artifact",
    
              "attributes": {
    
                "filename": "@demo/hello-world/1.0.0.tgz",
    
                "filetype": "tgz",
    
                "platform": "npm"
    
              },
    
              "relationships": {
    
                "release": {
    
                  "data": {
    
                    "type": "release",
    
                    "id": "5b4c27ab-8b1e-4257-b056-1db82a4ce8cf"
    
                  }
    
                }
    
              }
    
            }
    
          }'
    
    # => {
    
    #      "data": {
    
    #        "id": "9053969d-7615-417b-887b-342ef143b926",
    
    #        "type": "artifacts",
    
    #        ...
    
    #        "links": {
    
    #          "redirect": "https://bucket.s3.us-east-2.amazonaws.com/artifacts/%40demo/hello-world/1.0.0.tgz...",
    
    #        }
    
    #      }
    
    #    }
    
    curl -v -X POST 'https://api.keygen.sh/v1/accounts/demo/artifacts' \
      -u token:prod-1d2dedc2b12a376cfc5ee0622e9c0803ef1755d29baff43e8a8b0e790413f645v3 \
      -H 'content-type: application/json' \
      -d '{
            "data": {
              "type": "artifact",
              "attributes": {
                "filename": "@demo/hello-world/1.0.0.tgz",
                "filetype": "tgz",
                "platform": "npm"
              },
              "relationships": {
                "release": {
                  "data": {
                    "type": "release",
                    "id": "5b4c27ab-8b1e-4257-b056-1db82a4ce8cf"
                  }
                }
              }
            }
          }'
    # => {
    #      "data": {
    #        "id": "9053969d-7615-417b-887b-342ef143b926",
    #        "type": "artifacts",
    #        ...
    #        "links": {
    #          "redirect": "https://bucket.s3.us-east-2.amazonaws.com/artifacts/%40demo/hello-world/1.0.0.tgz...",
    #        }
    #      }
    #    }
    _content_copy_

Next, follow the redirect to upload the file:
    
    
    curl -vL -X PUT 'https://bucket.s3.us-east-2.amazonaws.com/artifacts/%40demo/hello-world/1.0.0.tgz...'
    
      -H 'content-type: application/tar+gzip' \
    
      -T dist/demo-hello-world-1.0.0.tgz
    
    curl -vL -X PUT 'https://bucket.s3.us-east-2.amazonaws.com/artifacts/%40demo/hello-world/1.0.0.tgz...'
      -H 'content-type: application/tar+gzip' \
      -T dist/demo-hello-world-1.0.0.tgz
    _content_copy_

Given that succeeded, we've now uploaded a **tarball** of our module! But we still need to publish a **manifest** so that npm can know the available versions of our module.

## Publishing an npm manifest

In order for npm to be able to use our module, we need to define a manifest that npm can use to determine the available versions of our module. A manifest is simply a JSON file, kind of similar to `package.json`.

An abbreviated manifest looks like this:
    
    
    {
    
      "name": "@demo/hello-world",
    
      "dist-tags": {
    
        "latest": "1.0.0"
    
      },
    
      "versions": {
    
        "1.0.0": {
    
          "dist": {
    
            "tarball": "https://api.keygen.sh/v1/accounts/demo/artifacts/@demo/hello-world/1.0.0.tgz"
    
          }
    
        }
    
      }
    
    }
    
    {
      "name": "@demo/hello-world",
      "dist-tags": {
        "latest": "1.0.0"
      },
      "versions": {
        "1.0.0": {
          "dist": {
            "tarball": "https://api.keygen.sh/v1/accounts/demo/artifacts/@demo/hello-world/1.0.0.tgz"
          }
        }
      }
    }
    _content_copy_

The manifest can include additional information, such as an `integrity` digest for each version, [among other metadata properties](https://github.com/npm/registry/blob/master/docs/responses/package-metadata.md). But this is the bare-minimum metadata needed for npm to be able to install a private module.

Let's go ahead and create our **manifest** release:
    
    
    curl -v -X PUT 'https://api.keygen.sh/v1/accounts/demo/releases' \
    
      -u prod-1d2dedc2b12a376cfc5ee0622e9c0803ef1755d29baff43e8a8b0e790413f645v3: \
    
      -H 'content-type: application/json' \
    
      -d '{
    
            "data": {
    
              "type": "release",
    
              "attributes": {
    
                "status": "PUBLISHED",
    
                "channel": "stable",
    
                "version": "1.0.0"
    
              },
    
              "relationships": {
    
                "product": {
    
                  "data": {
    
                    "type": "product",
    
                    "id": "855ef427-6f68-4153-ab88-e63c631014c3"
    
                  }
    
                }
    
              }
    
            }
    
          }'
    
    # => {
    
    #      "data": {
    
    #        "id": "c07c9f7c-37f1-4401-96c7-1c6e4cde2705",
    
    #        "type": "releases",
    
    #        ...
    
    #      }
    
    #    }
    
    curl -v -X PUT 'https://api.keygen.sh/v1/accounts/demo/releases' \
      -u prod-1d2dedc2b12a376cfc5ee0622e9c0803ef1755d29baff43e8a8b0e790413f645v3: \
      -H 'content-type: application/json' \
      -d '{
            "data": {
              "type": "release",
              "attributes": {
                "status": "PUBLISHED",
                "channel": "stable",
                "version": "1.0.0"
              },
              "relationships": {
                "product": {
                  "data": {
                    "type": "product",
                    "id": "855ef427-6f68-4153-ab88-e63c631014c3"
                  }
                }
              }
            }
          }'
    # => {
    #      "data": {
    #        "id": "c07c9f7c-37f1-4401-96c7-1c6e4cde2705",
    #        "type": "releases",
    #        ...
    #      }
    #    }
    _content_copy_

Once we've done that, we'll want to again note our new release's ID, and then create and upload an artifact for our manifest JSON:
    
    
    curl -v -X POST 'https://api.keygen.sh/v1/accounts/demo/artifacts' \
    
      -u token:prod-1d2dedc2b12a376cfc5ee0622e9c0803ef1755d29baff43e8a8b0e790413f645v3 \
    
      -H 'content-type: application/json' \
    
      -d '{
    
            "data": {
    
              "type": "artifact",
    
              "attributes": {
    
                "filename": "@demo/hello-world",
    
                "filetype": "json",
    
                "platform": "npm",
    
              },
    
              "relationships": {
    
                "release": {
    
                  "data": {
    
                    "type": "release",
    
                    "id": "c07c9f7c-37f1-4401-96c7-1c6e4cde2705"
    
                  }
    
                }
    
              }
    
            }
    
          }'
    
    # => {
    
    #      "data": {
    
    #        "id": "ea27199f-2aa7-4851-a78c-e3a4346d3977",
    
    #        "type": "artifacts",
    
    #        ...
    
    #        "links": {
    
    #          "redirect": "https://bucket.s3.us-east-2.amazonaws.com/artifacts/%40demo/hello-world...",
    
    #        }
    
    #      }
    
    #    }
    
    curl -v -X POST 'https://api.keygen.sh/v1/accounts/demo/artifacts' \
      -u token:prod-1d2dedc2b12a376cfc5ee0622e9c0803ef1755d29baff43e8a8b0e790413f645v3 \
      -H 'content-type: application/json' \
      -d '{
            "data": {
              "type": "artifact",
              "attributes": {
                "filename": "@demo/hello-world",
                "filetype": "json",
                "platform": "npm",
              },
              "relationships": {
                "release": {
                  "data": {
                    "type": "release",
                    "id": "c07c9f7c-37f1-4401-96c7-1c6e4cde2705"
                  }
                }
              }
            }
          }'
    # => {
    #      "data": {
    #        "id": "ea27199f-2aa7-4851-a78c-e3a4346d3977",
    #        "type": "artifacts",
    #        ...
    #        "links": {
    #          "redirect": "https://bucket.s3.us-east-2.amazonaws.com/artifacts/%40demo/hello-world...",
    #        }
    #      }
    #    }
    _content_copy_

Lastly, you'll want to upload the artifact payload:
    
    
    curl -vL -X PUT 'https://bucket.s3.us-east-2.amazonaws.com/artifacts/%40demo/hello-world...'
    
      -H 'content-type: application/json' \
    
      -d '{
    
            "name": "@demo/hello-world",
    
            "dist-tags": {
    
              "latest": "1.0.0"
    
            },
    
            "versions": {
    
              "1.0.0": {
    
                "dist": {
    
                  "tarball": "https://api.keygen.sh/v1/accounts/demo/artifacts/@demo/hello-world/1.0.0.tgz"
    
                }
    
              }
    
            }
    
          }'
    
    curl -vL -X PUT 'https://bucket.s3.us-east-2.amazonaws.com/artifacts/%40demo/hello-world...'
      -H 'content-type: application/json' \
      -d '{
            "name": "@demo/hello-world",
            "dist-tags": {
              "latest": "1.0.0"
            },
            "versions": {
              "1.0.0": {
                "dist": {
                  "tarball": "https://api.keygen.sh/v1/accounts/demo/artifacts/@demo/hello-world/1.0.0.tgz"
                }
              }
            }
          }'
    _content_copy_

Simple as that â we've successfully uploaded the first tarball of our module, and we have a manifest available for npm to read. To make things even easier next time, we could use [Keygen's CLI](/docs/cli/) to publish releases and to upload artifacts, or [we could use Node to script everything](https://github.com/keygen-sh/example-private-npm-package/blob/master/scripts/publish.js) as part of our build or release process.

So, how do we use it?

## Using a private registry

In order for npm to install our private module, we need to tell it about our registry. For our `demo` account, we can add a registry with the following configuration:
    
    
    npm config set @demo:registry \
    
      'https://api.keygen.sh/v1/accounts/demo/artifacts/'
    
    npm config set @demo:registry \
      'https://api.keygen.sh/v1/accounts/demo/artifacts/'
    _content_copy_

This will configure npm to install all packages with the `@demo` scope from our **private artifact registry**. Pretty cool, huh?

## Installing our module

Let's try it out by installing our npm package! You can install it like any other npm package â just remember the `@demo` package scope:
    
    
    npm install -g @demo/hello-world
    
    # => npm ERR! code E401
    
    # => npm ERR! Unable to authenticate, your authentication
    
    #             token seems to be invalid.
    
    npm install -g @demo/hello-world
    # => npm ERR! code E401
    # => npm ERR! Unable to authenticate, your authentication
    #             token seems to be invalid.
    _content_copy_

Butâ¦ that didn't work, did it? Well, _that 's good!_ Our distribution API only allows **licensed users** to access release artifacts. So, we'll need to [create a new license](https://app.keygen.sh/licenses/new) for the product and then create [a license token](https://app.keygen.sh/tokens/activation/new) for that license. Alternatively, you can use a license key here, given [license key authentication](/docs/api/authentication/) is enabled on the policy.

A license token will look something like this:
    
    
    activ-b04db8523196a234f52748ef61cba077v3
    
    activ-b04db8523196a234f52748ef61cba077v3
    _content_copy_

**A license token allows an API consumer permission to read and manage a very small subset of resources they are entitled to.** In this case, that's downloading release artifacts. But a license token also grants permission to do other actions via the API, such as [activate machines for the specific license](/docs/api/machines/#machines-create). 

To resolve the authentication issue, let's also configure npm to use our license's license token when accessing our private npm registry:
    
    
    npm config set '//api.keygen.sh/v1/accounts/demo/artifacts/:_authToken' \
    
      'activ-b04db8523196a234f52748ef61cba077v3'
    
    npm config set '//api.keygen.sh/v1/accounts/demo/artifacts/:_authToken' \
      'activ-b04db8523196a234f52748ef61cba077v3'
    _content_copy_

The syntax is a bit â¦ odd, but that's how you configure npm to use an API token for authentication. Let's give installation another try:
    
    
    npm install -g @demo/hello-world
    
    # => + @demo/[[email protected]](/cdn-cgi/l/email-protection)
    
    # => added 1 package in 0.413s
    
    npm install -g @demo/hello-world
    # => + @demo/hello-world@1.0.0
    # => added 1 package in 0.413s
    _content_copy_

Eureka! We've successfully published our Node module to Keygen's distribution API, and then we configured npm to use Keygen as a private npm registry for packages scoped under the `@demo` package scope. Finally, we masqueraded as a licensed user and installed our package using a license token.

## Publishing updates

Publishing updates for the package is as simple as creating a new release, uploading the new tarball artifact, and then updating the manifest JSON to include the new version.

One thing to note â

When updating the manifest, we'll want to make sure that our changes are **additive** so that we retain a correct `versions` history â we don't want to overwrite the manifest with a single version every time, otherwise npm won't be able to install previous versions, breaking builds for any licensed users not on latest.

For example, updating the manifest to include version `2.0.0` of our module should also include version `1.0.0`. We'll also want to tag `2.0.0` as latest:
    
    
    curl -vL -X PUT 'https://bucket.s3.us-east-2.amazonaws.com/artifacts/%40demo/hello-world...'
    
      -H 'content-type: application/json' \
    
      -d '{
    
            "name": "@demo/hello-world",
    
            "dist-tags": {
    
              "latest": "2.0.0"
    
            },
    
            "versions": {
    
              "2.0.0": {
    
                "dist": {
    
                  "tarball": "https://api.keygen.sh/v1/accounts/demo/artifacts/@demo/hello-world/2.0.0.tgz"
    
                }
    
              },
    
              "1.0.0": {
    
                "dist": {
    
                  "tarball": "https://api.keygen.sh/v1/accounts/demo/artifacts/@demo/hello-world/1.0.0.tgz"
    
                }
    
              }
    
            }
    
          }'
    
    curl -vL -X PUT 'https://bucket.s3.us-east-2.amazonaws.com/artifacts/%40demo/hello-world...'
      -H 'content-type: application/json' \
      -d '{
            "name": "@demo/hello-world",
            "dist-tags": {
              "latest": "2.0.0"
            },
            "versions": {
              "2.0.0": {
                "dist": {
                  "tarball": "https://api.keygen.sh/v1/accounts/demo/artifacts/@demo/hello-world/2.0.0.tgz"
                }
              },
              "1.0.0": {
                "dist": {
                  "tarball": "https://api.keygen.sh/v1/accounts/demo/artifacts/@demo/hello-world/1.0.0.tgz"
                }
              }
            }
          }'
    _content_copy_

## In conclusion

I hope you enjoyed the read. It look quite a bit of reverse-engineering of the npm API to figure out how all of this works. _:grin:_ I hadn't ever come across an article on how to distribute a private npm package using static files and no database, so I hope this was helpful to some folks!

Although we're using Keygen to distribute our private npm package, a similar approach can be used to host a private registry on AWS S3 or similar. All you need to do is host a collection of static tarballs and a JSON manifest pointing to those tarballs.

If you're interested in a "codified" publishing workflow, [we've set up a Node.js repo on our GitHub](https://github.com/keygen-sh/example-private-npm-package) with a codified example. Check it out if that sounds interesting!

Some other things to explore next:

  * Add entitlement constraints to specific releases. For example, you could attach an `INSTALL_V2` entitlement constraint to v2, ensuring that only customers who "upgraded" their license can access v2 (while still allowing them to access v1.)
  * Add additional licensing logic into your module, such as for example, [device activation](/docs/api/machines/#machines-create), where you can set an upper limit on how many unique devices, or running instances of your module, can be used at a given time.
  * Use a CI/CD pipeline, such as GitHub actions, to automate publishing new versions from a `master` branch.



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


