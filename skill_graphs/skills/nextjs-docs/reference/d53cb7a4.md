# compress
Last updated February 27, 2026
By default, Next.js uses `gzip` to compress rendered content and static files when using `next start` or a custom server. This is an optimization for applications that do not have compression configured. If compression is _already_ configured in your application via a custom server, Next.js will not add compression.
You can check if compression is enabled and which algorithm is used by looking at the
