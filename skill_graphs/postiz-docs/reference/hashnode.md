[Skip to main content](https://docs.postiz.com/public-api/providers/discord#content-area)
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
Discord Settings
[Documentation](https://docs.postiz.com/introduction)[Public API](https://docs.postiz.com/public-api/introduction)[CLI](https://docs.postiz.com/cli/introduction)[MCP](https://docs.postiz.com/mcp/introduction)[Developer App (oAuth2)](https://docs.postiz.com/public-api/oauth)[Contributing](https://docs.postiz.com/developer-guide)
[Documentation](https://docs.postiz.com/introduction)[Public API](https://docs.postiz.com/public-api/introduction)[CLI](https://docs.postiz.com/cli/introduction)[MCP](https://docs.postiz.com/mcp/introduction)[Developer App (oAuth2)](https://docs.postiz.com/public-api/oauth)[Contributing](https://docs.postiz.com/developer-guide)
Provider Settings (25 with custom settings)
# Discord Settings
Copy page
API settings for posting to Discord
Copy page
## 
[​](https://docs.postiz.com/public-api/providers/discord#settings-schema)
Settings Schema
When posting a message to Discord, use the following settings schema:
```
{
  "settings": {
    "__type": "discord",
    "channel": "channel-id"
  }
}

```

## 
[​](https://docs.postiz.com/public-api/providers/discord#fields)
Fields
Field | Type | Required | Description  
---|---|---|---  
`__type` | `string` | Yes | Must be `discord`  
`channel` | `string` | Yes | Discord channel ID  
### 
[​](https://docs.postiz.com/public-api/providers/discord#channel)
`channel`
The Discord channel ID where the message will be posted. This is required.
**How to get a Discord channel ID:**
  1. Enable Developer Mode in Discord (User Settings → App Settings → Advanced → Developer Mode)
  2. Right-click on the channel
  3. Click “Copy Channel ID”


* * *
## 
[​](https://docs.postiz.com/public-api/providers/discord#complete-example)
Complete Example
### 
[​](https://docs.postiz.com/public-api/providers/discord#text-message)
Text Message
```
{
  "type": "schedule",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-discord-integration-id"
      },
      "value": [
        {
          "content": "🎉 **New Update Released!**\n\nWe've just shipped some exciting new features:\n\n• Feature 1\n• Feature 2\n• Feature 3\n\nCheck it out and let us know what you think!",
          "image": []
        }
      ],
      "settings": {
        "__type": "discord",
        "channel": "1234567890123456789"
      }
    }
  ]
}

```

### 
[​](https://docs.postiz.com/public-api/providers/discord#message-with-image)
Message with Image
```
{
  "type": "schedule",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-discord-integration-id"
      },
      "value": [
        {
          "content": "Check out this preview of our new feature! 👀",
          "image": [
            {
              "id": "preview-image-id",
              "path": "https://uploads.postiz.com/preview.png"
            }
          ]
        }
      ],
      "settings": {
        "__type": "discord",
        "channel": "1234567890123456789"
      }
    }
  ]
}

```

### 
[​](https://docs.postiz.com/public-api/providers/discord#announcement-with-formatting)
Announcement with Formatting
```
{
  "type": "now",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-discord-integration-id"
      },
      "value": [
        {
          "content": "# 📢 Important Announcement\n\n> We'll be performing scheduled maintenance tonight from 10 PM - 12 AM UTC.\n\n**What to expect:**\n- Brief service interruption\n- Improved performance after maintenance\n\n*Thank you for your patience!*",
          "image": []
        }
      ],
      "settings": {
        "__type": "discord",
        "channel": "9876543210987654321"
      }
    }
  ]
}

```

Discord supports Markdown formatting in messages. You can use:
  * `**bold**` for **bold**
  * `*italic*` for _italic_
  * `# Heading` for headings
  * `> quote` for quotes
  * ``code`` for inline code


Was this page helpful?
YesNo
[Previous](https://docs.postiz.com/public-api/providers/pinterest)[ Slack SettingsAPI settings for posting to Slack Next ](https://docs.postiz.com/public-api/providers/slack)
Ctrl+I
[discord](https://discord.postiz.com)
On this page
  * [Settings Schema](https://docs.postiz.com/public-api/providers/discord#settings-schema)
  * [Fields](https://docs.postiz.com/public-api/providers/discord#fields)
  * [channel](https://docs.postiz.com/public-api/providers/discord#channel)
  * [Complete Example](https://docs.postiz.com/public-api/providers/discord#complete-example)
  * [Text Message](https://docs.postiz.com/public-api/providers/discord#text-message)
  * [Message with Image](https://docs.postiz.com/public-api/providers/discord#message-with-image)
  * [Announcement with Formatting](https://docs.postiz.com/public-api/providers/discord#announcement-with-formatting)


![Logo](https://postiz.com/favicon.ico)
Postiz
Hi! Im the Postiz AI Chatbot, ask me any question you'd like, and I will answer it the best to my abilities!
QUICK QUESTIONS
Hashnode Settings - Postiz Documentation
← Asking about this page
Made by 
Chat