# Step 2: pass id + path into the post
```

## `upload-from-url` timeouts or "fetch failed"

`/upload-from-url` proxies the source URL through the Postiz backend.
If the source server is slow, unreachable, blocks Postiz's user agent,
or sits behind authentication, the upload fails.

**Fix**

* Make sure the source URL is publicly reachable HTTPS, with no auth.
* Don't link to private S3 URLs, signed URLs that have expired, or
  intranet hosts.
* If the source is consistently slow, pre-download the file locally and
  use the multipart `/upload` endpoint instead.

## "Failed to load video metadata"

Postiz inspects uploaded videos for duration, dimensions, and codec
before passing them to the social provider. Files outside the supported
range fail here.

**Recommended video format**

* Container: MP4
* Video codec: H.264 (baseline or main profile)
* Audio codec: AAC
* Frame rate: 30 fps or less
* Resolution: ≤ 1920×1080 for most providers; TikTok and YouTube
  Shorts prefer portrait 1080×1920.

Other formats may upload but get rejected by the social provider
downstream.

## "uploader plugin does not allow removing files during an upload"

You hit Cancel on a file that was already being uploaded. Postiz's
uploader doesn't support mid-flight cancellation — wait for the upload
to complete, then delete the asset from the post.

This is a known UX limitation; see [Known Issues](/troubleshooting/known-issues).
