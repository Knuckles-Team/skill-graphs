# Upload video first
VIDEO=$(postiz upload video.mp4)
VIDEO_URL=$(echo "$VIDEO" | jq -r '.path')

postiz posts:create \
  -c "Check this out! #fyp" \
  -m "$VIDEO_URL" \
  -s "2025-01-15T10:00:00Z" \
  --settings '{"privacy_level":"PUBLIC_TO_EVERYONE","duet":true,"stitch":true}' \
  -i "tiktok-id"
```

## Instagram

```bash theme={null}
