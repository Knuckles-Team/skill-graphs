# Uploads & Media
Source: https://docs.postiz.com/troubleshooting/uploads

Payload limits, upload-from-url, video, and cancel-in-flight behaviour

## Body size limit

The Postiz backend accepts JSON bodies up to **50 MB** on the post-creation
routes (`POST /public/v1/posts` for the public API, plus the internal
`/posts` and `/copilot/*` endpoints used by the web UI). Other endpoints
fall back to the framework default and are much smaller — don't inline
base64-encoded images in arbitrary endpoints.

## Accepted MIME types (Public API)

The `/public/v1/upload` and `/public/v1/upload-from-url` endpoints validate
the uploaded file's detected MIME type against this allowlist:

| Type      | MIME         |
| --------- | ------------ |
| JPEG      | `image/jpeg` |
| PNG       | `image/png`  |
| GIF       | `image/gif`  |
| WebP      | `image/webp` |
| AVIF      | `image/avif` |
| BMP       | `image/bmp`  |
| TIFF      | `image/tiff` |
| MP4 video | `video/mp4`  |

PDFs are **not** accepted by the public API. The only PDF flow Postiz
supports is LinkedIn document carousels, which are produced internally
by converting an image carousel to PDF — you can't post a PDF directly
through the public API.

## "PayloadTooLargeError" when creating a post

You sent a request body larger than 50 MB to `POST /public/v1/posts` —
almost always because you inlined image data instead of uploading first.

**Fix:** upload media via `/public/v1/upload` (or `/public/v1/upload-from-url`),
then reference the returned `id` and `path` in the post body's
`image` array.

```bash theme={null}
