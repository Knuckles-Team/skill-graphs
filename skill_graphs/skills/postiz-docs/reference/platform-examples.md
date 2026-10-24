# Platform Examples
Source: https://docs.postiz.com/cli/platform-examples

Ready-to-use examples for posting to specific platforms

## X (Twitter)

### Simple Post

```bash theme={null}
postiz posts:create \
  -c "Hello Twitter!" \
  -s "2025-01-15T10:00:00Z" \
  -i "twitter-id"
```

### Thread

```bash theme={null}
postiz posts:create \
  -c "Thread 1/3: Introduction" \
  -c "Thread 2/3: Main point" \
  -c "Thread 3/3: Conclusion" \
  -s "2025-01-15T10:00:00Z" \
  -d 2000 \
  -i "twitter-id"
```

### With Reply Controls

```bash theme={null}
postiz posts:create \
  -c "Only followers can reply to this" \
  -s "2025-01-15T10:00:00Z" \
  --settings '{"who_can_reply_post":"followers"}' \
  -i "twitter-id"
```

## Reddit

### Post with Flair

```bash theme={null}
