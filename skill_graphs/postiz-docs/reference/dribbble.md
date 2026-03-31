[Skip to main content](https://docs.postiz.com/public-api/providers/reddit#content-area)
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
Reddit Settings
[Documentation](https://docs.postiz.com/introduction)[Public API](https://docs.postiz.com/public-api/introduction)[CLI](https://docs.postiz.com/cli/introduction)[MCP](https://docs.postiz.com/mcp/introduction)[Developer App (oAuth2)](https://docs.postiz.com/public-api/oauth)[Contributing](https://docs.postiz.com/developer-guide)
[Documentation](https://docs.postiz.com/introduction)[Public API](https://docs.postiz.com/public-api/introduction)[CLI](https://docs.postiz.com/cli/introduction)[MCP](https://docs.postiz.com/mcp/introduction)[Developer App (oAuth2)](https://docs.postiz.com/public-api/oauth)[Contributing](https://docs.postiz.com/developer-guide)
Provider Settings (25 with custom settings)
# Reddit Settings
Copy page
API settings for posting to Reddit
Copy page
##
[​](https://docs.postiz.com/public-api/providers/reddit#settings-schema)
Settings Schema
When creating a post for Reddit, use the following settings schema:
```
{
  "settings": {
    "__type": "reddit",
    "subreddit": [
      {
        "value": {
          "subreddit": "programming",
          "title": "My Post Title",
          "type": "self",
          "url": "",
          "is_flair_required": false,
          "flair": null
        }
      }
    ]
  }
}

```

##
[​](https://docs.postiz.com/public-api/providers/reddit#fields)
Fields
Field | Type | Required | Description
---|---|---|---
`__type` | `string` | Yes | Must be `reddit`
`subreddit` | `array` | Yes | Array of subreddit configurations
###
[​](https://docs.postiz.com/public-api/providers/reddit#subreddit-object)
Subreddit Object
Each item in the `subreddit` array contains a `value` object with:
Field | Type | Required | Description
---|---|---|---
`subreddit` | `string` | Yes | Subreddit name (without r/)
`title` | `string` | Yes | Post title (min 2 characters)
`type` | `string` | Yes | Post type
`url` | `string` | Conditional | URL for link posts
`is_flair_required` | `boolean` | Yes | Whether flair is required
`flair` | `object` | Conditional | Flair object (required if `is_flair_required` is true)
###
[​](https://docs.postiz.com/public-api/providers/reddit#type-post-type)
`type` (Post Type)
Value | Description
---|---
`self` | Text post (uses content from post value)
`link` | Link post (requires `url` field)
`image` | Image post
`video` | Video post
###
[​](https://docs.postiz.com/public-api/providers/reddit#flair-object)
Flair Object
Required when `is_flair_required` is `true`:
```
{
  "flair": {
    "id": "flair-template-id",
    "name": "Discussion"
  }
}

```

* * *
##
[​](https://docs.postiz.com/public-api/providers/reddit#complete-example)
Complete Example
###
[​](https://docs.postiz.com/public-api/providers/reddit#text-post-self-post)
Text Post (Self Post)
```
{
  "type": "schedule",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-reddit-integration-id"
      },
      "value": [
        {
          "content": "I've been working on this project for the past few months and wanted to share my experience.\n\n## What I learned\n\n1. Planning is crucial\n2. Start small\n3. Iterate quickly\n\nWhat are your thoughts?",
          "image": []
        }
      ],
      "settings": {
        "__type": "reddit",
        "subreddit": [
          {
            "value": {
              "subreddit": "programming",
              "title": "My journey building a side project - lessons learned",
              "type": "self",
              "url": "",
              "is_flair_required": false,
              "flair": null
            }
          }
        ]
      }
    }
  ]
}

```

###
[​](https://docs.postiz.com/public-api/providers/reddit#link-post)
Link Post
```
{
  "type": "schedule",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-reddit-integration-id"
      },
      "value": [
        {
          "content": "",
          "image": []
        }
      ],
      "settings": {
        "__type": "reddit",
        "subreddit": [
          {
            "value": {
              "subreddit": "technology",
              "title": "Interesting article about AI developments",
              "type": "link",
              "url": "https://example.com/ai-article",
              "is_flair_required": false,
              "flair": null
            }
          }
        ]
      }
    }
  ]
}

```

###
[​](https://docs.postiz.com/public-api/providers/reddit#post-with-required-flair)
Post with Required Flair
```
{
  "type": "schedule",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-reddit-integration-id"
      },
      "value": [
        {
          "content": "Looking for advice on my situation...",
          "image": []
        }
      ],
      "settings": {
        "__type": "reddit",
        "subreddit": [
          {
            "value": {
              "subreddit": "personalfinance",
              "title": "Need advice on budgeting",
              "type": "self",
              "url": "",
              "is_flair_required": true,
              "flair": {
                "id": "abc123-flair-id",
                "name": "Budgeting"
              }
            }
          }
        ]
      }
    }
  ]
}

```

###
[​](https://docs.postiz.com/public-api/providers/reddit#cross-post-to-multiple-subreddits)
Cross-post to Multiple Subreddits
```
{
  "settings": {
    "__type": "reddit",
    "subreddit": [
      {
        "value": {
          "subreddit": "webdev",
          "title": "New CSS feature just dropped!",
          "type": "link",
          "url": "https://example.com/css-news",
          "is_flair_required": false,
          "flair": null
        }
      },
      {
        "value": {
          "subreddit": "frontend",
          "title": "New CSS feature just dropped!",
          "type": "link",
          "url": "https://example.com/css-news",
          "is_flair_required": false,
          "flair": null
        }
      }
    ]
  }
}

```

**Tip:** You can post to multiple subreddits simultaneously by adding multiple objects to the `subreddit` array.
Was this page helpful?
YesNo
[Previous](https://docs.postiz.com/public-api/providers/tiktok)[ Lemmy SettingsProvider settings for Lemmy posts Next ](https://docs.postiz.com/public-api/providers/lemmy)
Ctrl+I
[discord](https://discord.postiz.com)
On this page
  * [Settings Schema](https://docs.postiz.com/public-api/providers/reddit#settings-schema)
  * [Fields](https://docs.postiz.com/public-api/providers/reddit#fields)
  * [Subreddit Object](https://docs.postiz.com/public-api/providers/reddit#subreddit-object)
  * [type (Post Type)](https://docs.postiz.com/public-api/providers/reddit#type-post-type)
  * [Flair Object](https://docs.postiz.com/public-api/providers/reddit#flair-object)
  * [Complete Example](https://docs.postiz.com/public-api/providers/reddit#complete-example)
  * [Text Post (Self Post)](https://docs.postiz.com/public-api/providers/reddit#text-post-self-post)
  * [Link Post](https://docs.postiz.com/public-api/providers/reddit#link-post)
  * [Post with Required Flair](https://docs.postiz.com/public-api/providers/reddit#post-with-required-flair)
  * [Cross-post to Multiple Subreddits](https://docs.postiz.com/public-api/providers/reddit#cross-post-to-multiple-subreddits)


![Logo](https://postiz.com/favicon.ico)
Postiz
Hi! Im the Postiz AI Chatbot, ask me any question you'd like, and I will answer it the best to my abilities!
QUICK QUESTIONS
Dribbble Settings - Postiz Documentation
← Asking about this page
Made by
Chat
