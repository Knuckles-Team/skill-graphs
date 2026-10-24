# Upload video first
VIDEO=$(postiz upload video.mp4)
VIDEO_URL=$(echo "$VIDEO" | jq -r '.path')

postiz posts:create \
  -c "Video description here" \
  -m "$VIDEO_URL" \
  -s "2025-01-15T10:00:00Z" \
  --settings '{"title":"My Video Title","type":"public","tags":[{"value":"tech","label":"Tech"}]}' \
  -i "youtube-id"
```

## TikTok

```bash theme={null}
