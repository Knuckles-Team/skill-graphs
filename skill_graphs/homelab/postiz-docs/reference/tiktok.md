[Skip to main content](https://docs.postiz.com/public-api/providers/linkedin#content-area)
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
LinkedIn Settings
[Documentation](https://docs.postiz.com/introduction)[Public API](https://docs.postiz.com/public-api/introduction)[CLI](https://docs.postiz.com/cli/introduction)[MCP](https://docs.postiz.com/mcp/introduction)[Developer App (oAuth2)](https://docs.postiz.com/public-api/oauth)[Contributing](https://docs.postiz.com/developer-guide)
[Documentation](https://docs.postiz.com/introduction)[Public API](https://docs.postiz.com/public-api/introduction)[CLI](https://docs.postiz.com/cli/introduction)[MCP](https://docs.postiz.com/mcp/introduction)[Developer App (oAuth2)](https://docs.postiz.com/public-api/oauth)[Contributing](https://docs.postiz.com/developer-guide)
Provider Settings (25 with custom settings)
# LinkedIn Settings
Copy page
API settings for posting to LinkedIn
Copy page
##
[​](https://docs.postiz.com/public-api/providers/linkedin#settings-schema)
Settings Schema
When creating a post for LinkedIn (profile or page), use the following settings schema:
```
{
  "settings": {
    "__type": "linkedin",
    "post_as_images_carousel": false
  }
}

```

Use `__type: "linkedin"` for personal profiles and `__type: "linkedin-page"` for company pages. Both use the same settings schema.
##
[​](https://docs.postiz.com/public-api/providers/linkedin#fields)
Fields
Field | Type | Required | Description
---|---|---|---
`__type` | `string` | Yes |  `linkedin` or `linkedin-page`
`post_as_images_carousel` | `boolean` | No | Display multiple images as a carousel
`carousel_name` | `string` | No | Name for the carousel document
###
[​](https://docs.postiz.com/public-api/providers/linkedin#post_as_images_carousel)
`post_as_images_carousel`
When set to `true` and you have multiple images, they will be displayed as a swipeable carousel instead of a collage.
Value | Description
---|---
`true` | Images displayed as carousel
`false` | Images displayed as collage (default)
###
[​](https://docs.postiz.com/public-api/providers/linkedin#carousel_name)
`carousel_name`
Optional name for the carousel document. Only used when `post_as_images_carousel` is `true`.
* * *
##
[​](https://docs.postiz.com/public-api/providers/linkedin#complete-example)
Complete Example
###
[​](https://docs.postiz.com/public-api/providers/linkedin#text-post)
Text Post
```
{
  "type": "schedule",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-linkedin-integration-id"
      },
      "value": [
        {
          "content": "Excited to share our latest update! 🎉\n\n#innovation #tech",
          "image": []
        }
      ],
      "settings": {
        "__type": "linkedin"
      }
    }
  ]
}

```

###
[​](https://docs.postiz.com/public-api/providers/linkedin#carousel-post)
Carousel Post
```
{
  "type": "schedule",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-linkedin-integration-id"
      },
      "value": [
        {
          "content": "Check out our product showcase! Swipe through to see all features →",
          "image": [
            {
              "id": "image-1-id",
              "path": "https://uploads.postiz.com/image1.png"
            },
            {
              "id": "image-2-id",
              "path": "https://uploads.postiz.com/image2.png"
            },
            {
              "id": "image-3-id",
              "path": "https://uploads.postiz.com/image3.png"
            }
          ]
        }
      ],
      "settings": {
        "__type": "linkedin",
        "post_as_images_carousel": true,
        "carousel_name": "Product Showcase"
      }
    }
  ]
}

```

###
[​](https://docs.postiz.com/public-api/providers/linkedin#company-page-post)
Company Page Post
```
{
  "type": "now",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-linkedin-page-integration-id"
      },
      "value": [
        {
          "content": "We're hiring! Join our team and help us build the future.",
          "image": []
        }
      ],
      "settings": {
        "__type": "linkedin-page",
        "post_as_images_carousel": false
      }
    }
  ]
}

```

Was this page helpful?
YesNo
[Previous](https://docs.postiz.com/public-api/providers/x)[ Facebook SettingsProvider settings for Facebook posts Next ](https://docs.postiz.com/public-api/providers/facebook)
Ctrl+I
[discord](https://discord.postiz.com)
On this page
  * [Settings Schema](https://docs.postiz.com/public-api/providers/linkedin#settings-schema)
  * [Fields](https://docs.postiz.com/public-api/providers/linkedin#fields)
  * [post_as_images_carousel](https://docs.postiz.com/public-api/providers/linkedin#post_as_images_carousel)
  * [carousel_name](https://docs.postiz.com/public-api/providers/linkedin#carousel_name)
  * [Complete Example](https://docs.postiz.com/public-api/providers/linkedin#complete-example)
  * [Text Post](https://docs.postiz.com/public-api/providers/linkedin#text-post)
  * [Carousel Post](https://docs.postiz.com/public-api/providers/linkedin#carousel-post)
  * [Company Page Post](https://docs.postiz.com/public-api/providers/linkedin#company-page-post)


![Logo](https://postiz.com/favicon.ico)
Postiz
Hi! Im the Postiz AI Chatbot, ask me any question you'd like, and I will answer it the best to my abilities!
QUICK QUESTIONS
Made by
Chat
