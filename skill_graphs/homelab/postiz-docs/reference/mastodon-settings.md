# Mastodon Settings
Source: https://docs.postiz.com/public-api/providers/mastodon

API settings for posting to Mastodon

## Settings Schema

When creating a post for Mastodon, use the following settings schema:

```json theme={null}
{
  "settings": {
    "__type": "mastodon"
  }
}
```

<Note>
  Mastodon has no provider-specific settings beyond `__type`. Post content,
  images, and the schedule are configured at the post level - see the
  [Create Post](/public-api/posts/create) reference. The instance the post
  publishes to is determined by the connected integration, not the settings
  block.
</Note>

## Fields

| Field    | Type     | Required | Description        |
| -------- | -------- | -------- | ------------------ |
| `__type` | `string` | Yes      | Must be `mastodon` |

***

## Complete Example

### Text Post

```json theme={null}
{
  "type": "schedule",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-mastodon-integration-id"
      },
      "value": [
        {
          "content": "Hello from the Postiz API! 🐘",
          "image": []
        }
      ],
      "settings": {
        "__type": "mastodon"
      }
    }
  ]
}
```

### Thread Post

Create a thread by adding multiple items to the `value` array. Each entry
becomes a reply chained to the previous toot:

```json theme={null}
{
  "type": "schedule",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-mastodon-integration-id"
      },
      "value": [
        {
          "content": "1/ Starting a thread on Mastodon from the API",
          "image": []
        },
        {
          "content": "2/ Each value entry becomes a reply in the thread",
          "image": []
        }
      ],
      "settings": {
        "__type": "mastodon"
      }
    }
  ]
}
```

### Post with Image

```json theme={null}
{
  "type": "now",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": {
        "id": "your-mastodon-integration-id"
      },
      "value": [
        {
          "content": "Sharing a launch screenshot",
          "image": [
            {
              "id": "image-id",
              "path": "https://uploads.postiz.com/launch.png"
            }
          ]
        }
      ],
      "settings": {
        "__type": "mastodon"
      }
    }
  ]
}
```
