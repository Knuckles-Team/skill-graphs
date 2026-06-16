# Regular post
postiz posts:create \
  -c "Beautiful day! #photography" \
  -m "$IMAGE_URL" \
  -s "2025-01-15T10:00:00Z" \
  --settings '{"post_type":"post"}' \
  -i "instagram-id"
```

### Story

```bash theme={null}
postiz posts:create \
  -c "Story content" \
  -m "$IMAGE_URL" \
  -s "2025-01-15T10:00:00Z" \
  --settings '{"post_type":"story"}' \
  -i "instagram-id"
```

### Reel

A single video with `post_type: "post"` is published as a Reel:

```bash theme={null}
postiz posts:create \
  -c "Reel caption" \
  -m "$VIDEO_URL" \
  -s "2025-01-15T10:00:00Z" \
  --settings '{"post_type":"post"}' \
  -i "instagram-id"
```

### Reel with Audio

Search the Instagram audio catalog and attach a track to the Reel
(Facebook Business-linked channels only — an empty `q` returns trending audio):

```bash theme={null}
