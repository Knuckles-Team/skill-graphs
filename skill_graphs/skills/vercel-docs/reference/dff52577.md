##  [Compression algorithms](https://vercel.com/docs/getting-started-with-vercel#compression-algorithms)[](https://vercel.com/docs/getting-started-with-vercel#compression-algorithms)
While `gzip` has been around for quite some time, `brotli` is a newer compression algorithm built by Google that best serves text compression. If your client supports
  * `brotli` compressed JavaScript files are 14% smaller than `gzip`
  * HTML files are 21% smaller than `gzip`
  * CSS files are 17% smaller than `gzip`


`brotli` has an advantage over `gzip` since it uses a dictionary of common keywords on both the client and server-side, which gives a better compression ratio.
