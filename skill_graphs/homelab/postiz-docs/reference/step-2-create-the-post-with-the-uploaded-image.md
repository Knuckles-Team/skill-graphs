# Step 2: Create the post with the uploaded image
curl -X POST "https://api.postiz.com/public/v1/posts" \
  -H "Authorization: your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "schedule",
    "date": "2024-12-14T10:00:00.000Z",
    "shortLink": false,
    "tags": [],
    "posts": [{
      "integration": { "id": "your-instagram-id" },
      "value": [{
        "content": "Beautiful sunset 🌅 #photography",
        "image": [{ "id": "img-123", "path": "https://uploads.postiz.com/photo.jpg" }]
      }],
      "settings": {
        "__type": "instagram",
        "post_type": "post"
      }
    }]
  }'
```

### Publish a Medium article

```json theme={null}
{
  "type": "now",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": { "id": "your-medium-id" },
      "value": [
        {
          "content": "# Introduction\n\nThis is my article in markdown...",
          "image": []
        }
      ],
      "settings": {
        "__type": "medium",
        "title": "My Amazing Article",
        "subtitle": "A deep dive into something interesting",
        "tags": [
          { "value": "programming", "label": "Programming" }
        ]
      }
    }
  ]
}
```

### Create a Google My Business offer

```json theme={null}
{
  "type": "schedule",
  "date": "2024-12-14T10:00:00.000Z",
  "shortLink": false,
  "tags": [],
  "posts": [
    {
      "integration": { "id": "your-gmb-id" },
      "value": [
        {
          "content": "🎉 Holiday Sale! 20% off everything!",
          "image": []
        }
      ],
      "settings": {
        "__type": "gmb",
        "topicType": "OFFER",
        "callToActionType": "GET_OFFER",
        "callToActionUrl": "https://example.com/sale",
        "offerCouponCode": "HOLIDAY20"
      }
    }
  ]
}
```
