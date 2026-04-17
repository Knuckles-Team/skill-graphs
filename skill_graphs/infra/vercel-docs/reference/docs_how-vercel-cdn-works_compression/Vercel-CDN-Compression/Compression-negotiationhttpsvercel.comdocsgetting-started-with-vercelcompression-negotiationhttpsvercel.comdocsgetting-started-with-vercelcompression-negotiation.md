##  [Compression negotiation](https://vercel.com/docs/getting-started-with-vercel#compression-negotiation)[](https://vercel.com/docs/getting-started-with-vercel#compression-negotiation)
Many clients (e.g., browsers like Chrome, Firefox, and Safari) include the `Accept-Encoding`
You can verify if a response was compressed by checking the `Content-Encoding` `gzip` or `brotli`.
###  [Clients that don't use `Accept-Encoding`](https://vercel.com/docs/getting-started-with-vercel#clients-that-don't-use-accept-encoding)[](https://vercel.com/docs/getting-started-with-vercel#clients-that-don't-use-accept-encoding)
The following clients may not include the `Accept-Encoding` header by default:
  * Custom applications, such as Python scripts, Node.js servers, or other software that can send HTTP requests to your deployment
  * HTTP libraries, such as `curl` or `wget`
  * Older browsers. Check `Accept-Encoding` by default
  * Bots and crawlers sometimes don't specify `Accept-Encoding` in their headers by default when visiting your deployment


When writing a client that doesn't run in a browser, for example a CLI, you will need to set the `Accept-Encoding` request header in your client code to opt into compression.
###  [Automatically compressed MIME types](https://vercel.com/docs/getting-started-with-vercel#automatically-compressed-mime-types)[](https://vercel.com/docs/getting-started-with-vercel#automatically-compressed-mime-types)
When the `Accept-Encoding` request header is present, only the following list of MIME types will be automatically compressed.
####  [Application types](https://vercel.com/docs/getting-started-with-vercel#application-types)[](https://vercel.com/docs/getting-started-with-vercel#application-types)
  * `json`
  * `x-web-app-manifest+json`
  * `geo+json`
  * `manifest+json`
  * `ld+json`
  * `atom+xml`
  * `rss+xml`
  * `xhtml+xml`
  * `xml`
  * `rdf+xml`
  * `javascript`
  * `tar`
  * `vnd.ms-fontobject`
  * `wasm`


####  [Font types](https://vercel.com/docs/getting-started-with-vercel#font-types)[](https://vercel.com/docs/getting-started-with-vercel#font-types)
  * `otf`
  * `ttf`


####  [Image types](https://vercel.com/docs/getting-started-with-vercel#image-types)[](https://vercel.com/docs/getting-started-with-vercel#image-types)
  * `svg+xml`
  * `bmp`
  * `x-icon`


####  [Text types](https://vercel.com/docs/getting-started-with-vercel#text-types)[](https://vercel.com/docs/getting-started-with-vercel#text-types)
  * `cache-manifest`
  * `css`
  * `csv`
  * `dns`
  * `javascript`
  * `plain`
  * `markdown`
  * `vcard`
  * `calendar`
  * `vnd.rim.location.xloc`
  * `vtt`
  * `x-component`
  * `x-cross-domain-policy`


###  [Compression allowlist](https://vercel.com/docs/getting-started-with-vercel#compression-allowlist)[](https://vercel.com/docs/getting-started-with-vercel#compression-allowlist)
The compression allowlist above is necessary to avoid accidentally increasing the size of non-compressible files, which can negatively impact performance.
For example, most image formats are already compressed such as JPEG, PNG, WebP, etc. If you want to compress an image even further, consider lowering the quality using [Vercel Image Optimization](https://vercel.com/docs/image-optimization).
* * *
[ Previous Vercel Documentation ](https://vercel.com/docs)[ Next Projects and Deployments ](https://vercel.com/docs/getting-started-with-vercel/projects-deployments)
Was this helpful?
Send
On this page
  * [Compression algorithms](https://vercel.com/docs/getting-started-with-vercel#compression-algorithms)
  * [Compression negotiation](https://vercel.com/docs/getting-started-with-vercel#compression-negotiation)
  * [Clients that don't use Accept-Encoding](https://vercel.com/docs/getting-started-with-vercel#clients-that-don't-use-accept-encoding)
  * [Automatically compressed MIME types](https://vercel.com/docs/getting-started-with-vercel#automatically-compressed-mime-types)
  * [Application types](https://vercel.com/docs/getting-started-with-vercel#application-types)
  * [Font types](https://vercel.com/docs/getting-started-with-vercel#font-types)
  * [Image types](https://vercel.com/docs/getting-started-with-vercel#image-types)
  * [Text types](https://vercel.com/docs/getting-started-with-vercel#text-types)
  * [Compression allowlist](https://vercel.com/docs/getting-started-with-vercel#compression-allowlist)


Copy as MarkdownGive feedbackAsk AI about this page
