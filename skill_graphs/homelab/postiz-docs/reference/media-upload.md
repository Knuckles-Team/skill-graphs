# Media Upload
Source: https://docs.postiz.com/cli/media-upload

Upload images, videos, and other media files for use in posts

## Uploading Files

Upload a local file and receive a URL you can use in posts:

```bash theme={null}
postiz upload <file-path>
```

The command returns a JSON response with the uploaded file's URL:

```json theme={null}
{
  "id": "img-123",
  "path": "https://uploads.postiz.com/your-file.jpg"
}
```

<Warning>
  You must upload media files to Postiz before using them in posts. Many platforms (TikTok, Instagram, YouTube) require verified URLs and will reject external links.
</Warning>

## Upload and Post Workflow

```bash theme={null}
