[Skip to main content](https://docs.postiz.com/public-api/providers/instagram#content-area)
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
Instagram Settings
[Documentation](https://docs.postiz.com/introduction)[Public API](https://docs.postiz.com/public-api/introduction)[CLI](https://docs.postiz.com/cli/introduction)[MCP](https://docs.postiz.com/mcp/introduction)[Developer App (oAuth2)](https://docs.postiz.com/public-api/oauth)[Contributing](https://docs.postiz.com/developer-guide)
[Documentation](https://docs.postiz.com/introduction)[Public API](https://docs.postiz.com/public-api/introduction)[CLI](https://docs.postiz.com/cli/introduction)[MCP](https://docs.postiz.com/mcp/introduction)[Developer App (oAuth2)](https://docs.postiz.com/public-api/oauth)[Contributing](https://docs.postiz.com/developer-guide)
Provider Settings (25 with custom settings)
# Instagram Settings
Copy page
API settings for posting to Instagram
Copy page
##
[​](https://docs.postiz.com/public-api/providers/instagram#settings-schema)
Settings Schema
When creating a post for Instagram, use the following settings schema:
```
{
  "settings": {
    "__type": "instagram",
    "post_type": "post",
    "is_trial_reel": false,
    "collaborators": []
  }
}

```

Use `__type: "instagram"` for Facebook Business-linked accounts and `__type: "instagram-standalone"` for standalone Instagram accounts. Both use the same settings schema.
##
[​](https://docs.postiz.com/public-api/providers/instagram#fields)
Fields
Field | Type | Required | Description
---|---|---|---
`__type` | `string` | Yes |  `instagram` or `instagram-standalone`
`post_type` | `string` | Yes | Type of Instagram post
`is_trial_reel` | `boolean` | No | Whether to post as a trial reel
`graduation_strategy` | `string` | No | Graduation strategy for trial reels
`collaborators` | `array` | No | List of collaborator usernames
###
[​](https://docs.postiz.com/public-api/providers/instagram#post_type)
`post_type`
Value | Description
---|---
`post` | Regular feed post
`story` | Instagram Story (24-hour visibility)
###
[​](https://docs.postiz.com/public-api/providers/instagram#is_trial_reel)
`is_trial_reel`
When set to `true`, the post will be published as a trial reel with limited initial visibility.
###
[​](https://docs.postiz.com/public-api/providers/instagram#graduation_strategy)
`graduation_strategy`
Controls how trial reels graduate to full visibility. Only applicable when `is_trial_reel` is `true`.
Value | Description
---|---
`MANUAL` | Manually graduate the reel
`SS_PERFORMANCE` | Automatically graduate based on performance
###
[​](https://docs.postiz.com/public-api/providers/instagram#collaborators)
`collaborators`
Array of collaborator objects. Each collaborator will receive an invite to be added as a collaborator on the post.
```
{
  "collaborators": [
    { "label": "username1" },
    { "label": "username2" }
  ]
}

```

* * *
##
[​](https://docs.postiz.com/public-api/providers/instagram#complete-example)
Complete Example
###
[​](https://docs.postiz.com/public-api/providers/instagram#feed-post)
Feed Post
```
{
  "type": "schedule",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-instagram-integration-id"
      },
      "value": [
        {
          "content": "Beautiful sunset today! 🌅\n\n#sunset #photography #nature",
          "image": [
            {
              "id": "image-id",
              "path": "https://uploads.postiz.com/sunset.jpg"
            }
          ]
        }
      ],
      "settings": {
        "__type": "instagram",
        "post_type": "post",
        "is_trial_reel": false,
        "collaborators": []
      }
    }
  ]
}

```

###
[​](https://docs.postiz.com/public-api/providers/instagram#story-post)
Story Post
```
{
  "type": "now",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-instagram-integration-id"
      },
      "value": [
        {
          "content": "",
          "image": [
            {
              "id": "story-image-id",
              "path": "https://uploads.postiz.com/story.jpg"
            }
          ]
        }
      ],
      "settings": {
        "__type": "instagram",
        "post_type": "story"
      }
    }
  ]
}

```

###
[​](https://docs.postiz.com/public-api/providers/instagram#collaborative-post)
Collaborative Post
```
{
  "type": "schedule",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-instagram-integration-id"
      },
      "value": [
        {
          "content": "Amazing collab with @partner! 🤝",
          "image": [
            {
              "id": "collab-image-id",
              "path": "https://uploads.postiz.com/collab.jpg"
            }
          ]
        }
      ],
      "settings": {
        "__type": "instagram",
        "post_type": "post",
        "collaborators": [
          { "label": "partner_username" }
        ]
      }
    }
  ]
}

```

###
[​](https://docs.postiz.com/public-api/providers/instagram#carousel-post)
Carousel Post
Create a carousel by adding multiple images:
```
{
  "type": "schedule",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-instagram-integration-id"
      },
      "value": [
        {
          "content": "Swipe to see all the photos! 📸",
          "image": [
            { "id": "img1", "path": "https://uploads.postiz.com/1.jpg" },
            { "id": "img2", "path": "https://uploads.postiz.com/2.jpg" },
            { "id": "img3", "path": "https://uploads.postiz.com/3.jpg" }
          ]
        }
      ],
      "settings": {
        "__type": "instagram",
        "post_type": "post"
      }
    }
  ]
}

```

Was this page helpful?
YesNo
[Previous](https://docs.postiz.com/public-api/providers/facebook)[ Warpcast (Farcaster) SettingsProvider settings for Warpcast/Farcaster posts Next ](https://docs.postiz.com/public-api/providers/warpcast)
Ctrl+I
[discord](https://discord.postiz.com)
On this page
  * [Settings Schema](https://docs.postiz.com/public-api/providers/instagram#settings-schema)
  * [Fields](https://docs.postiz.com/public-api/providers/instagram#fields)
  * [post_type](https://docs.postiz.com/public-api/providers/instagram#post_type)
  * [is_trial_reel](https://docs.postiz.com/public-api/providers/instagram#is_trial_reel)
  * [graduation_strategy](https://docs.postiz.com/public-api/providers/instagram#graduation_strategy)
  * [collaborators](https://docs.postiz.com/public-api/providers/instagram#collaborators)
  * [Complete Example](https://docs.postiz.com/public-api/providers/instagram#complete-example)
  * [Feed Post](https://docs.postiz.com/public-api/providers/instagram#feed-post)
  * [Story Post](https://docs.postiz.com/public-api/providers/instagram#story-post)
  * [Collaborative Post](https://docs.postiz.com/public-api/providers/instagram#collaborative-post)
  * [Carousel Post](https://docs.postiz.com/public-api/providers/instagram#carousel-post)


![Logo](https://postiz.com/favicon.ico)
Postiz
Hi! Im the Postiz AI Chatbot, ask me any question you'd like, and I will answer it the best to my abilities!
QUICK QUESTIONS
Instagram Settings - Postiz Documentation
← Asking about this page
Made by
Chat
