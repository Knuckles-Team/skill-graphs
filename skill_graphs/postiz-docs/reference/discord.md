[Skip to main content](https://docs.postiz.com/public-api/providers/youtube#content-area)
[Postiz Documentation home page![light logo](https://mintcdn.com/postiz/SZ3zBABjhg7UQcI8/logo/light.png?fit=max&auto=format&n=SZ3zBABjhg7UQcI8&q=85&s=ab950a1a5aa687eb0de8156022f7c7c9)![dark logo](https://mintcdn.com/postiz/SZ3zBABjhg7UQcI8/logo/dark.png?fit=max&auto=format&n=SZ3zBABjhg7UQcI8&q=85&s=4134d88b8fc8339a26775f8e48e95f7e)](https://docs.postiz.com/)
Search...
Ctrl K
  * [Discord](https://discord.postiz.com)


##### Overview
  * [API Overview](https://docs.postiz.com/public-api/introduction)


##### Integrations
  * [GET List Integrations](https://docs.postiz.com/public-api/integrations/list)
  * [GET Connect Channel (OAuth)](https://docs.postiz.com/public-api/integrations/connect)
  * [DEL Delete Channel](https://docs.postiz.com/public-api/integrations/delete)
  * [GET Check Connection](https://docs.postiz.com/public-api/integrations/is-connected)
  * [GET Find Available Slot](https://docs.postiz.com/public-api/integrations/find-slot)


##### Posts
  * [GET List Posts](https://docs.postiz.com/public-api/posts/list)
  * [POST Create Post](https://docs.postiz.com/public-api/posts/create)
  * [DEL Delete Post](https://docs.postiz.com/public-api/posts/delete)
  * [DEL Delete Post by Group](https://docs.postiz.com/public-api/posts/delete-by-group)
  * [GET Get Missing Content](https://docs.postiz.com/public-api/posts/missing-content)
  * [PUT Update Release ID](https://docs.postiz.com/public-api/posts/update-release-id)


##### Analytics
  * [GET Platform Analytics](https://docs.postiz.com/public-api/analytics/platform)
  * [GET Post Analytics](https://docs.postiz.com/public-api/analytics/post)


##### Notifications
  * [GET List Notifications](https://docs.postiz.com/public-api/notifications/list)


##### Uploads
  * [POST Upload File](https://docs.postiz.com/public-api/uploads/upload-file)
  * [POST Upload from URL](https://docs.postiz.com/public-api/uploads/upload-from-url)


##### Video Generation
  * [POST Generate Video](https://docs.postiz.com/public-api/video/generate)
  * [POST Video Function](https://docs.postiz.com/public-api/video/function)


##### Provider Settings (25 with custom settings)
  * [X (Twitter) Settings](https://docs.postiz.com/public-api/providers/x)
  * [LinkedIn Settings](https://docs.postiz.com/public-api/providers/linkedin)
  * [Facebook Settings](https://docs.postiz.com/public-api/providers/facebook)
  * [Instagram Settings](https://docs.postiz.com/public-api/providers/instagram)
  * [Warpcast (Farcaster) Settings](https://docs.postiz.com/public-api/providers/warpcast)
  * [YouTube Settings](https://docs.postiz.com/public-api/providers/youtube)
  * [TikTok Settings](https://docs.postiz.com/public-api/providers/tiktok)
  * [Reddit Settings](https://docs.postiz.com/public-api/providers/reddit)
  * [Lemmy Settings](https://docs.postiz.com/public-api/providers/lemmy)
  * [Pinterest Settings](https://docs.postiz.com/public-api/providers/pinterest)
  * [Discord Settings](https://docs.postiz.com/public-api/providers/discord)
  * [Slack Settings](https://docs.postiz.com/public-api/providers/slack)
  * [Dribbble Settings](https://docs.postiz.com/public-api/providers/dribbble)
  * [Medium Settings](https://docs.postiz.com/public-api/providers/medium)
  * [Dev.to Settings](https://docs.postiz.com/public-api/providers/devto)
  * [Hashnode Settings](https://docs.postiz.com/public-api/providers/hashnode)
  * [WordPress Settings](https://docs.postiz.com/public-api/providers/wordpress)
  * [Listmonk Settings](https://docs.postiz.com/public-api/providers/listmonk)
  * [Google My Business Settings](https://docs.postiz.com/public-api/providers/gmb)
  * [Whop Settings](https://docs.postiz.com/public-api/providers/whop)
  * [Skool Settings](https://docs.postiz.com/public-api/providers/skool)
  * [Kick Settings](https://docs.postiz.com/public-api/providers/kick)
  * [Twitch Settings](https://docs.postiz.com/public-api/providers/twitch)
  * [Moltbook Settings](https://docs.postiz.com/public-api/providers/moltbook)


  * [Discord](https://discord.postiz.com)
  * [Register to the cloud](https://postiz.com)


[Postiz Documentation home page![light logo](https://mintcdn.com/postiz/SZ3zBABjhg7UQcI8/logo/light.png?fit=max&auto=format&n=SZ3zBABjhg7UQcI8&q=85&s=ab950a1a5aa687eb0de8156022f7c7c9)![dark logo](https://mintcdn.com/postiz/SZ3zBABjhg7UQcI8/logo/dark.png?fit=max&auto=format&n=SZ3zBABjhg7UQcI8&q=85&s=4134d88b8fc8339a26775f8e48e95f7e)](https://docs.postiz.com/)
Search...
Ctrl K
  * [](https://discord.postiz.com)
  * [Register to the cloud](https://postiz.com)
  * [Register to the cloud](https://postiz.com)


Search...
Navigation
Provider Settings (25 with custom settings)
YouTube Settings
[Documentation](https://docs.postiz.com/introduction)[Public API](https://docs.postiz.com/public-api/introduction)[CLI](https://docs.postiz.com/cli/introduction)[MCP](https://docs.postiz.com/mcp/introduction)[Developer App (oAuth2)](https://docs.postiz.com/public-api/oauth)[Contributing](https://docs.postiz.com/developer-guide)
[Documentation](https://docs.postiz.com/introduction)[Public API](https://docs.postiz.com/public-api/introduction)[CLI](https://docs.postiz.com/cli/introduction)[MCP](https://docs.postiz.com/mcp/introduction)[Developer App (oAuth2)](https://docs.postiz.com/public-api/oauth)[Contributing](https://docs.postiz.com/developer-guide)
Provider Settings (25 with custom settings)
# YouTube Settings
Copy page
API settings for posting to YouTube
Copy page
## 
[​](https://docs.postiz.com/public-api/providers/youtube#settings-schema)
Settings Schema
When uploading a video to YouTube, use the following settings schema:
```
{
  "settings": {
    "__type": "youtube",
    "title": "My Video Title",
    "type": "public",
    "selfDeclaredMadeForKids": "no",
    "thumbnail": null,
    "tags": []
  }
}

```

## 
[​](https://docs.postiz.com/public-api/providers/youtube#fields)
Fields
Field | Type | Required | Description  
---|---|---|---  
`__type` | `string` | Yes | Must be `youtube`  
`title` | `string` | Yes | Video title (2-100 characters)  
`type` | `string` | Yes | Video visibility  
`selfDeclaredMadeForKids` | `string` | No | Made for kids declaration  
`thumbnail` | `object` | No | Custom thumbnail  
`tags` | `array` | No | Video tags  
### 
[​](https://docs.postiz.com/public-api/providers/youtube#title)
`title`
Video title with the following constraints:
  * Minimum: 2 characters
  * Maximum: 100 characters


### 
[​](https://docs.postiz.com/public-api/providers/youtube#type-visibility)
`type` (visibility)
Value | Description  
---|---  
`public` | Anyone can search for and view  
`unlisted` | Anyone with the link can view  
`private` | Only you can view  
### 
[​](https://docs.postiz.com/public-api/providers/youtube#selfdeclaredmadeforkids)
`selfDeclaredMadeForKids`
Value | Description  
---|---  
`yes` | Content is made for kids  
`no` | Content is not made for kids  
### 
[​](https://docs.postiz.com/public-api/providers/youtube#thumbnail)
`thumbnail`
Custom thumbnail object (uploaded via the uploads endpoint):
```
{
  "thumbnail": {
    "id": "thumbnail-id",
    "path": "https://uploads.postiz.com/thumbnail.jpg"
  }
}

```

### 
[​](https://docs.postiz.com/public-api/providers/youtube#tags)
`tags`
Array of tag objects for video SEO:
```
{
  "tags": [
    { "value": "tech", "label": "tech" },
    { "value": "tutorial", "label": "tutorial" }
  ]
}

```

* * *
## 
[​](https://docs.postiz.com/public-api/providers/youtube#complete-example)
Complete Example
### 
[​](https://docs.postiz.com/public-api/providers/youtube#public-video-with-tags)
Public Video with Tags
```
{
  "type": "schedule",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-youtube-integration-id"
      },
      "value": [
        {
          "content": "In this video, I'll show you how to use the Postiz API to automate your social media workflow.\n\nTimestamps:\n0:00 Introduction\n1:30 Setup\n5:00 First API call\n10:00 Conclusion",
          "image": [
            {
              "id": "video-id",
              "path": "https://uploads.postiz.com/tutorial.mp4"
            }
          ]
        }
      ],
      "settings": {
        "__type": "youtube",
        "title": "How to Use Postiz API - Complete Tutorial",
        "type": "public",
        "selfDeclaredMadeForKids": "no",
        "tags": [
          { "value": "postiz", "label": "postiz" },
          { "value": "api", "label": "api" },
          { "value": "tutorial", "label": "tutorial" },
          { "value": "social media automation", "label": "social media automation" }
        ]
      }
    }
  ]
}

```

### 
[​](https://docs.postiz.com/public-api/providers/youtube#video-with-custom-thumbnail)
Video with Custom Thumbnail
```
{
  "type": "schedule",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-youtube-integration-id"
      },
      "value": [
        {
          "content": "Full video description here...",
          "image": [
            {
              "id": "video-id",
              "path": "https://uploads.postiz.com/video.mp4"
            }
          ]
        }
      ],
      "settings": {
        "__type": "youtube",
        "title": "My Awesome Video",
        "type": "public",
        "selfDeclaredMadeForKids": "no",
        "thumbnail": {
          "id": "thumb-id",
          "path": "https://uploads.postiz.com/thumbnail.jpg"
        },
        "tags": []
      }
    }
  ]
}

```

### 
[​](https://docs.postiz.com/public-api/providers/youtube#private/unlisted-video)
Private/Unlisted Video
```
{
  "settings": {
    "__type": "youtube",
    "title": "Private Team Update",
    "type": "unlisted",
    "selfDeclaredMadeForKids": "no",
    "tags": []
  }
}

```

Was this page helpful?
YesNo
[Previous](https://docs.postiz.com/public-api/providers/warpcast)[ TikTok SettingsAPI settings for posting to TikTok Next ](https://docs.postiz.com/public-api/providers/tiktok)
Ctrl+I
[discord](https://discord.postiz.com)
On this page
  * [Settings Schema](https://docs.postiz.com/public-api/providers/youtube#settings-schema)
  * [Fields](https://docs.postiz.com/public-api/providers/youtube#fields)
  * [title](https://docs.postiz.com/public-api/providers/youtube#title)
  * [type (visibility)](https://docs.postiz.com/public-api/providers/youtube#type-visibility)
  * [selfDeclaredMadeForKids](https://docs.postiz.com/public-api/providers/youtube#selfdeclaredmadeforkids)
  * [thumbnail](https://docs.postiz.com/public-api/providers/youtube#thumbnail)
  * [tags](https://docs.postiz.com/public-api/providers/youtube#tags)
  * [Complete Example](https://docs.postiz.com/public-api/providers/youtube#complete-example)
  * [Public Video with Tags](https://docs.postiz.com/public-api/providers/youtube#public-video-with-tags)
  * [Video with Custom Thumbnail](https://docs.postiz.com/public-api/providers/youtube#video-with-custom-thumbnail)
  * [Private/Unlisted Video](https://docs.postiz.com/public-api/providers/youtube#private%2Funlisted-video)


![Logo](https://postiz.com/favicon.ico)
Postiz
Hi! Im the Postiz AI Chatbot, ask me any question you'd like, and I will answer it the best to my abilities!
QUICK QUESTIONS
Discord Settings - Postiz Documentation
← Asking about this page
Made by 
Chat