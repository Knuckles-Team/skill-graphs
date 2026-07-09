## Why This Error Occurred[](https://nextjs.org/docs/messages/next-request-in-use-cache#why-this-error-occurred)
A function is trying to read from the current incoming request inside the scope of a function annotated with `"use cache"`. This is not supported because it would make the cache invalidated by every request which is probably not what you intended.
