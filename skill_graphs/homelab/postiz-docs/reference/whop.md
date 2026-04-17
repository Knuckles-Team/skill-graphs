[Skip to main content](https://docs.postiz.com/public-api/providers/slack#content-area)
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
  * [School Settings](https://docs.postiz.com/public-api/providers/school)
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
Slack Settings
[Documentation](https://docs.postiz.com/introduction)[Public API](https://docs.postiz.com/public-api/introduction)[CLI](https://docs.postiz.com/cli/introduction)[MCP](https://docs.postiz.com/mcp/introduction)[Developer App (oAuth2)](https://docs.postiz.com/public-api/oauth)[Contributing](https://docs.postiz.com/developer-guide)
[Documentation](https://docs.postiz.com/introduction)[Public API](https://docs.postiz.com/public-api/introduction)[CLI](https://docs.postiz.com/cli/introduction)[MCP](https://docs.postiz.com/mcp/introduction)[Developer App (oAuth2)](https://docs.postiz.com/public-api/oauth)[Contributing](https://docs.postiz.com/developer-guide)
Provider Settings (25 with custom settings)
# Slack Settings
Copy page
API settings for posting to Slack
Copy page
##
[​](https://docs.postiz.com/public-api/providers/slack#settings-schema)
Settings Schema
When posting a message to Slack, use the following settings schema:
```
{
  "settings": {
    "__type": "slack",
    "channel": "channel-id"
  }
}

```

##
[​](https://docs.postiz.com/public-api/providers/slack#fields)
Fields
Field | Type | Required | Description
---|---|---|---
`__type` | `string` | Yes | Must be `slack`
`channel` | `string` | Yes | Slack channel ID
###
[​](https://docs.postiz.com/public-api/providers/slack#channel)
`channel`
The Slack channel ID where the message will be posted. This is required.
**How to get a Slack channel ID:**
  1. Right-click on the channel name in Slack
  2. Click “View channel details”
  3. Scroll to the bottom - the Channel ID is displayed there
  4. Or, the channel ID is in the URL when viewing a channel: `https://app.slack.com/client/WORKSPACE/CHANNEL_ID`


* * *
##
[​](https://docs.postiz.com/public-api/providers/slack#complete-example)
Complete Example
###
[​](https://docs.postiz.com/public-api/providers/slack#simple-message)
Simple Message
```
{
  "type": "schedule",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-slack-integration-id"
      },
      "value": [
        {
          "content": "🎉 *New Release v2.0*\n\nWe're excited to announce our latest update!\n\n• New dashboard design\n• Improved performance\n• Bug fixes\n\nCheck it out: https://example.com/release",
          "image": []
        }
      ],
      "settings": {
        "__type": "slack",
        "channel": "C0123456789"
      }
    }
  ]
}

```

###
[​](https://docs.postiz.com/public-api/providers/slack#message-with-image)
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
        "id": "your-slack-integration-id"
      },
      "value": [
        {
          "content": "📊 *Weekly Metrics Report*\n\nHere's our performance this week:",
          "image": [
            {
              "id": "metrics-image-id",
              "path": "https://uploads.postiz.com/metrics.png"
            }
          ]
        }
      ],
      "settings": {
        "__type": "slack",
        "channel": "C0123456789"
      }
    }
  ]
}

```

###
[​](https://docs.postiz.com/public-api/providers/slack#team-announcement)
Team Announcement
```
{
  "type": "now",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-slack-integration-id"
      },
      "value": [
        {
          "content": ":mega: *Team Update*\n\n> Reminder: All-hands meeting tomorrow at 2 PM\n\n*Agenda:*\n1. Q4 Review\n2. 2025 Planning\n3. Open Q&A\n\nSee you there! :wave:",
          "image": []
        }
      ],
      "settings": {
        "__type": "slack",
        "channel": "C9876543210"
      }
    }
  ]
}

```

Slack supports its own formatting syntax:
  * `*bold*` for **bold**
  * `_italic_` for _italic_
  * `~strikethrough~` for ~~strikethrough~~
  * `:emoji_name:` for emojis
  * `> quote` for quotes
  * ``code`` for inline code


Was this page helpful?
YesNo
[Previous](https://docs.postiz.com/public-api/providers/discord)[ Dribbble SettingsAPI settings for posting to Dribbble Next ](https://docs.postiz.com/public-api/providers/dribbble)
Ctrl+I
[discord](https://discord.postiz.com)
On this page
  * [Settings Schema](https://docs.postiz.com/public-api/providers/slack#settings-schema)
  * [Fields](https://docs.postiz.com/public-api/providers/slack#fields)
  * [channel](https://docs.postiz.com/public-api/providers/slack#channel)
  * [Complete Example](https://docs.postiz.com/public-api/providers/slack#complete-example)
  * [Simple Message](https://docs.postiz.com/public-api/providers/slack#simple-message)
  * [Message with Image](https://docs.postiz.com/public-api/providers/slack#message-with-image)
  * [Team Announcement](https://docs.postiz.com/public-api/providers/slack#team-announcement)


![Logo](https://postiz.com/favicon.ico)
Postiz
Hi! Im the Postiz AI Chatbot, ask me any question you'd like, and I will answer it the best to my abilities!
QUICK QUESTIONS
Made by
Chat
