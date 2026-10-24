# Uploads & Storage
Source: https://docs.postiz.com/configuration/uploads

Local filesystem vs Cloudflare R2 for media uploads

Postiz writes user-uploaded media (post images, avatars, generated
content) through a single storage abstraction. Pick one of two backends.

## Pick a backend

```env theme={null}
STORAGE_PROVIDER="local"      # default — write to local filesystem
