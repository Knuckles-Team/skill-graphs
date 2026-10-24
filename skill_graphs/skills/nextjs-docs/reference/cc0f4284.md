# proxyClientMaxBodySize
This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on
Last updated February 27, 2026
When proxy is used, Next.js automatically clones the request body and buffers it in memory to enable multiple reads - both in proxy and the underlying route handler. To prevent excessive memory usage, this configuration option sets a size limit on the buffered body.
By default, the maximum body size is **10MB**. If a request body exceeds this limit, the body will only be buffered up to the limit, and a warning will be logged indicating which route exceeded the limit.
