[Skip to main content](https://docs.postiz.com/public-api/providers/facebook#content-area)
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
Facebook Settings
[Documentation](https://docs.postiz.com/introduction)[Public API](https://docs.postiz.com/public-api/introduction)[CLI](https://docs.postiz.com/cli/introduction)[MCP](https://docs.postiz.com/mcp/introduction)[Developer App (oAuth2)](https://docs.postiz.com/public-api/oauth)[Contributing](https://docs.postiz.com/developer-guide)
[Documentation](https://docs.postiz.com/introduction)[Public API](https://docs.postiz.com/public-api/introduction)[CLI](https://docs.postiz.com/cli/introduction)[MCP](https://docs.postiz.com/mcp/introduction)[Developer App (oAuth2)](https://docs.postiz.com/public-api/oauth)[Contributing](https://docs.postiz.com/developer-guide)
Provider Settings (25 with custom settings)
# Facebook Settings
Copy page
Provider settings for Facebook posts
Copy page
## 
[​](https://docs.postiz.com/public-api/providers/facebook#overview)
Overview
Facebook integration allows you to post to Facebook pages. You can optionally include a link URL in your posts.
## 
[​](https://docs.postiz.com/public-api/providers/facebook#settings-schema)
Settings Schema
```
{
  "__type": "facebook",
  "url": "https://example.com/my-article"
}

```

## 
[​](https://docs.postiz.com/public-api/providers/facebook#properties)
Properties
Property | Type | Required | Description  
---|---|---|---  
`__type` | string | ✅ | Must be `"facebook"`  
`url` | string | ❌ | Optional link URL to include in the post  
## 
[​](https://docs.postiz.com/public-api/providers/facebook#examples)
Examples
### 
[​](https://docs.postiz.com/public-api/providers/facebook#simple-text-post)
Simple text post
```
{
  "type": "now",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-facebook-integration-id"
      },
      "value": [
        {
          "content": "Check out our latest updates! 🎉",
          "image": []
        }
      ],
      "settings": {
        "__type": "facebook"
      }
    }
  ]
}

```

### 
[​](https://docs.postiz.com/public-api/providers/facebook#post-with-link)
Post with link
```
{
  "type": "schedule",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-facebook-integration-id"
      },
      "value": [
        {
          "content": "We just published a new blog post about social media automation!",
          "image": []
        }
      ],
      "settings": {
        "__type": "facebook",
        "url": "https://example.com/blog/social-media-automation"
      }
    }
  ]
}

```

### 
[​](https://docs.postiz.com/public-api/providers/facebook#post-with-image)
Post with image
```
{
  "type": "schedule",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-facebook-integration-id"
      },
      "value": [
        {
          "content": "Beautiful sunset from our office! 🌅",
          "image": [
            {
              "id": "img-123",
              "path": "https://uploads.postiz.com/sunset.jpg"
            }
          ]
        }
      ],
      "settings": {
        "__type": "facebook"
      }
    }
  ]
}

```

## 
[​](https://docs.postiz.com/public-api/providers/facebook#notes)
Notes
  * The `url` field is optional and creates a link preview in the post
  * If posting with images, Facebook will display them as attachments
  * Video uploads are also supported


Was this page helpful?
YesNo
[Previous](https://docs.postiz.com/public-api/providers/linkedin)[ Instagram SettingsAPI settings for posting to Instagram Next ](https://docs.postiz.com/public-api/providers/instagram)
Ctrl+I
[discord](https://discord.postiz.com)
On this page
  * [Overview](https://docs.postiz.com/public-api/providers/facebook#overview)
  * [Settings Schema](https://docs.postiz.com/public-api/providers/facebook#settings-schema)
  * [Properties](https://docs.postiz.com/public-api/providers/facebook#properties)
  * [Examples](https://docs.postiz.com/public-api/providers/facebook#examples)
  * [Simple text post](https://docs.postiz.com/public-api/providers/facebook#simple-text-post)
  * [Post with link](https://docs.postiz.com/public-api/providers/facebook#post-with-link)
  * [Post with image](https://docs.postiz.com/public-api/providers/facebook#post-with-image)
  * [Notes](https://docs.postiz.com/public-api/providers/facebook#notes)


![Logo](https://postiz.com/favicon.ico)
Postiz
Hi! Im the Postiz AI Chatbot, ask me any question you'd like, and I will answer it the best to my abilities!
QUICK QUESTIONS
Made by 
Chat