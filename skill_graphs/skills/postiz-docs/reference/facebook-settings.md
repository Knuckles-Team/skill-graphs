# Facebook Settings
Source: https://docs.postiz.com/public-api/providers/facebook

Provider settings for Facebook posts

## Overview

Facebook integration allows you to post to Facebook pages. You can optionally include a link URL in your posts.

## Settings Schema

```json theme={null}
{
  "__type": "facebook",
  "url": "https://example.com/my-article"
}
```

## Properties

| Property | Type   | Required | Description                              |
| -------- | ------ | -------- | ---------------------------------------- |
| `__type` | string | ✅        | Must be `"facebook"`                     |
| `url`    | string | ❌        | Optional link URL to include in the post |

## Examples

### Simple text post

```json theme={null}
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

### Post with link

```json theme={null}
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

### Post with image

```json theme={null}
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

## Notes

* The `url` field is optional and creates a link preview in the post
* If posting with images, Facebook will display them as attachments
* Video uploads are also supported
