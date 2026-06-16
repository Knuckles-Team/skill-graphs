# Find an audio ID
AUDIO_ID=$(postiz integrations:trigger instagram-id audioSearch \
  -d '{"q":"summer vibes","type":"music"}' | jq -r '.output[0].id')

postiz posts:create \
  -c "Reel with trending audio" \
  -m "$VIDEO_URL" \
  -s "2025-01-15T10:00:00Z" \
  --settings "{\"post_type\":\"post\",\"audio\":{\"id\":\"$AUDIO_ID\",\"audio_volume\":80,\"video_volume\":20}}" \
  -i "instagram-id"
```

## LinkedIn

```bash theme={null}
postiz posts:create \
  -c "Professional update on LinkedIn" \
  -s "2025-01-15T10:00:00Z" \
  -i "linkedin-id"
```

### Image Carousel

```bash theme={null}
postiz posts:create \
  -c "Check out these slides!" \
  -m "image1.jpg,image2.jpg,image3.jpg" \
  -s "2025-01-15T10:00:00Z" \
  --settings '{"post_as_images_carousel":true}' \
  -i "linkedin-id"
```

## Pinterest

```bash theme={null}
postiz posts:create \
  -c "Pin description" \
  -m "$IMAGE_URL" \
  -s "2025-01-15T10:00:00Z" \
  --settings '{"board":"board-id","title":"Pin Title","link":"https://example.com"}' \
  -i "pinterest-id"
```

## Discord

```bash theme={null}
postiz posts:create \
  -c "Message to Discord" \
  -s "2025-01-15T10:00:00Z" \
  --settings '{"channel":"channel-id"}' \
  -i "discord-id"
```

## Batch Scheduling

Schedule multiple posts across different dates:

```bash theme={null}
#!/bin/bash
DATES=("2025-01-14T09:00:00Z" "2025-01-15T09:00:00Z" "2025-01-16T09:00:00Z")
CONTENT=("Monday motivation" "Tuesday tips" "Wednesday wisdom")

for i in "${!DATES[@]}"; do
  postiz posts:create \
    -c "${CONTENT[$i]}" \
    -s "${DATES[$i]}" \
    -i "twitter-id"
done
```

## Multi-Platform Campaign

Post different content per platform in one command using a JSON file:

```bash theme={null}
postiz posts:create --json campaign.json
```

Example `campaign.json`:

```json theme={null}
{
  "integrations": ["twitter-123", "linkedin-456", "reddit-789"],
  "posts": [
    {
      "provider": "twitter",
      "post": [{ "content": "Short tweet version", "image": [] }]
    },
    {
      "provider": "linkedin",
      "post": [{ "content": "More detailed LinkedIn post with professional tone", "image": [] }]
    },
    {
      "provider": "reddit",
      "post": [{ "content": "Reddit post body", "image": [] }],
      "settings": {
        "__type": "reddit",
        "subreddit": [{ "value": { "subreddit": "programming", "title": "Post Title", "type": "text" } }]
      }
    }
  ]
}
```
