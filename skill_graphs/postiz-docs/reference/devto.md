[Skip to main content](https://docs.postiz.com/public-api/providers/pinterest#content-area)
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
Pinterest Settings
[Documentation](https://docs.postiz.com/introduction)[Public API](https://docs.postiz.com/public-api/introduction)[CLI](https://docs.postiz.com/cli/introduction)[MCP](https://docs.postiz.com/mcp/introduction)[Developer App (oAuth2)](https://docs.postiz.com/public-api/oauth)[Contributing](https://docs.postiz.com/developer-guide)
[Documentation](https://docs.postiz.com/introduction)[Public API](https://docs.postiz.com/public-api/introduction)[CLI](https://docs.postiz.com/cli/introduction)[MCP](https://docs.postiz.com/mcp/introduction)[Developer App (oAuth2)](https://docs.postiz.com/public-api/oauth)[Contributing](https://docs.postiz.com/developer-guide)
Provider Settings (25 with custom settings)
# Pinterest Settings
Copy page
API settings for posting to Pinterest
Copy page
## 
[​](https://docs.postiz.com/public-api/providers/pinterest#settings-schema)
Settings Schema
When creating a Pin on Pinterest, use the following settings schema:
```
{
  "settings": {
    "__type": "pinterest",
    "board": "board-id",
    "title": "My Pin Title",
    "link": "https://example.com",
    "dominant_color": "#FF5733"
  }
}

```

## 
[​](https://docs.postiz.com/public-api/providers/pinterest#fields)
Fields
Field | Type | Required | Description  
---|---|---|---  
`__type` | `string` | Yes | Must be `pinterest`  
`board` | `string` | Yes | Board ID to pin to  
`title` | `string` | No | Pin title (max 100 characters)  
`link` | `string` | No | Destination URL  
`dominant_color` | `string` | No | Dominant color for the pin  
### 
[​](https://docs.postiz.com/public-api/providers/pinterest#board)
`board`
The board ID where the pin will be saved. This is required and must be a valid board ID from your Pinterest account.
Get board IDs by using Postiz’s UI to view your boards, or by using Pinterest’s API directly.
### 
[​](https://docs.postiz.com/public-api/providers/pinterest#title)
`title`
Optional pin title with a maximum of 100 characters.
### 
[​](https://docs.postiz.com/public-api/providers/pinterest#link)
`link`
Optional destination URL. When users click “Visit” on your pin, they’ll be taken to this URL.
### 
[​](https://docs.postiz.com/public-api/providers/pinterest#dominant-color)
`dominant_color`
Optional hex color code that represents the dominant color of your pin. Pinterest may use this for visual presentation.
* * *
## 
[​](https://docs.postiz.com/public-api/providers/pinterest#complete-example)
Complete Example
### 
[​](https://docs.postiz.com/public-api/providers/pinterest#basic-pin)
Basic Pin
```
{
  "type": "schedule",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-pinterest-integration-id"
      },
      "value": [
        {
          "content": "Beautiful home decor inspiration for your living room! 🏠✨",
          "image": [
            {
              "id": "pin-image-id",
              "path": "https://uploads.postiz.com/decor.jpg"
            }
          ]
        }
      ],
      "settings": {
        "__type": "pinterest",
        "board": "1234567890123456789",
        "title": "Living Room Decor Ideas",
        "link": "https://myblog.com/living-room-decor",
        "dominant_color": ""
      }
    }
  ]
}

```

### 
[​](https://docs.postiz.com/public-api/providers/pinterest#pin-with-all-options)
Pin with All Options
```
{
  "type": "schedule",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-pinterest-integration-id"
      },
      "value": [
        {
          "content": "Try this delicious recipe! Perfect for summer dinners. Full recipe on my blog 👇",
          "image": [
            {
              "id": "recipe-image-id",
              "path": "https://uploads.postiz.com/recipe.jpg"
            }
          ]
        }
      ],
      "settings": {
        "__type": "pinterest",
        "board": "9876543210987654321",
        "title": "Easy Summer Pasta Recipe",
        "link": "https://myrecipes.com/summer-pasta",
        "dominant_color": "#E8B4B8"
      }
    }
  ]
}

```

### 
[​](https://docs.postiz.com/public-api/providers/pinterest#simple-pin-minimal-settings)
Simple Pin (Minimal Settings)
```
{
  "settings": {
    "__type": "pinterest",
    "board": "1234567890123456789",
    "title": "",
    "link": "",
    "dominant_color": ""
  }
}

```

Was this page helpful?
YesNo
[Previous](https://docs.postiz.com/public-api/providers/lemmy)[ Discord SettingsAPI settings for posting to Discord Next ](https://docs.postiz.com/public-api/providers/discord)
Ctrl+I
[discord](https://discord.postiz.com)
On this page
  * [Settings Schema](https://docs.postiz.com/public-api/providers/pinterest#settings-schema)
  * [Fields](https://docs.postiz.com/public-api/providers/pinterest#fields)
  * [board](https://docs.postiz.com/public-api/providers/pinterest#board)
  * [title](https://docs.postiz.com/public-api/providers/pinterest#title)
  * [link](https://docs.postiz.com/public-api/providers/pinterest#link)
  * [dominant_color](https://docs.postiz.com/public-api/providers/pinterest#dominant-color)
  * [Complete Example](https://docs.postiz.com/public-api/providers/pinterest#complete-example)
  * [Basic Pin](https://docs.postiz.com/public-api/providers/pinterest#basic-pin)
  * [Pin with All Options](https://docs.postiz.com/public-api/providers/pinterest#pin-with-all-options)
  * [Simple Pin (Minimal Settings)](https://docs.postiz.com/public-api/providers/pinterest#simple-pin-minimal-settings)


![Logo](https://postiz.com/favicon.ico)
Postiz
Hi! Im the Postiz AI Chatbot, ask me any question you'd like, and I will answer it the best to my abilities!
QUICK QUESTIONS
Dev.to Settings - Postiz Documentation
← Asking about this page
Made by 
Chat