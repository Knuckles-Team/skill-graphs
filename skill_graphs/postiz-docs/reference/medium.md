[Skip to main content](https://docs.postiz.com/public-api/providers/lemmy#content-area)
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
Lemmy Settings
[Documentation](https://docs.postiz.com/introduction)[Public API](https://docs.postiz.com/public-api/introduction)[CLI](https://docs.postiz.com/cli/introduction)[MCP](https://docs.postiz.com/mcp/introduction)[Developer App (oAuth2)](https://docs.postiz.com/public-api/oauth)[Contributing](https://docs.postiz.com/developer-guide)
[Documentation](https://docs.postiz.com/introduction)[Public API](https://docs.postiz.com/public-api/introduction)[CLI](https://docs.postiz.com/cli/introduction)[MCP](https://docs.postiz.com/mcp/introduction)[Developer App (oAuth2)](https://docs.postiz.com/public-api/oauth)[Contributing](https://docs.postiz.com/developer-guide)
Provider Settings (25 with custom settings)
# Lemmy Settings
Copy page
Provider settings for Lemmy posts
Copy page
## 
[​](https://docs.postiz.com/public-api/providers/lemmy#overview)
Overview
Lemmy is a decentralized Reddit alternative. When posting to Lemmy, you need to specify the community and post details.
The settings use `subreddit` as the field name for historical reasons, but it refers to Lemmy communities.
## 
[​](https://docs.postiz.com/public-api/providers/lemmy#settings-schema)
Settings Schema
```
{
  "__type": "lemmy",
  "subreddit": [
    {
      "value": {
        "subreddit": "community_name",
        "id": "community-id",
        "title": "Post Title",
        "url": "https://optional-link.com"
      }
    }
  ]
}

```

## 
[​](https://docs.postiz.com/public-api/providers/lemmy#properties)
Properties
Property | Type | Required | Description  
---|---|---|---  
`__type` | string | ✅ | Must be `"lemmy"`  
`subreddit` | array | ✅ | Array of community targets  
`subreddit[].value.subreddit` | string | ✅ | Community name (min 2 chars)  
`subreddit[].value.id` | string | ✅ | Community ID  
`subreddit[].value.title` | string | ✅ | Post title (min 2 chars)  
`subreddit[].value.url` | string | ❌ | Optional link URL  
## 
[​](https://docs.postiz.com/public-api/providers/lemmy#example)
Example
```
{
  "type": "schedule",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-lemmy-integration-id"
      },
      "value": [
        {
          "content": "Check out this interesting article about open-source software!",
          "image": []
        }
      ],
      "settings": {
        "__type": "lemmy",
        "subreddit": [
          {
            "value": {
              "subreddit": "opensource",
              "id": "123456",
              "title": "Why Open Source Matters",
              "url": ""
            }
          }
        ]
      }
    }
  ]
}

```

## 
[​](https://docs.postiz.com/public-api/providers/lemmy#notes)
Notes
  * You can post to multiple communities by adding more items to the `subreddit` array
  * Each community requires a unique title for the post
  * The `url` field is optional and used for link-type posts


Was this page helpful?
YesNo
[Previous](https://docs.postiz.com/public-api/providers/reddit)[ Pinterest SettingsAPI settings for posting to Pinterest Next ](https://docs.postiz.com/public-api/providers/pinterest)
Ctrl+I
[discord](https://discord.postiz.com)
On this page
  * [Overview](https://docs.postiz.com/public-api/providers/lemmy#overview)
  * [Settings Schema](https://docs.postiz.com/public-api/providers/lemmy#settings-schema)
  * [Properties](https://docs.postiz.com/public-api/providers/lemmy#properties)
  * [Example](https://docs.postiz.com/public-api/providers/lemmy#example)
  * [Notes](https://docs.postiz.com/public-api/providers/lemmy#notes)


![Logo](https://postiz.com/favicon.ico)
Postiz
Hi! Im the Postiz AI Chatbot, ask me any question you'd like, and I will answer it the best to my abilities!
QUICK QUESTIONS
Medium Settings - Postiz Documentation
← Asking about this page
Made by 
Chat