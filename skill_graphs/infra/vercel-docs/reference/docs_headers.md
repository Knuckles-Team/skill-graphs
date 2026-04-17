System Headers
System Headers
# System Headers
Last updated March 8, 2026
Headers are small pieces of information that are sent between the client (usually a web browser) and the server. They contain metadata about the request and response, such as the content type, cache-control directives, and authentication tokens.
##  [Using headers](https://vercel.com/docs/headers#using-headers)[](https://vercel.com/docs/headers#using-headers)
By using headers effectively, you can optimize the performance and security of your application on Vercel's global network. Here are some tips for using headers on Vercel:
  1. [Use caching headers](https://vercel.com/docs/headers#cache-control-header): Caching headers instruct the client and server to cache resources like images, CSS files, and JavaScript files, so they don't need to be reloaded every time a user visits your site. By using caching headers, you can significantly reduce the time it takes for your site to load.
  2. [Use compression headers](https://vercel.com/docs/compression#compression-with-vercel-cdn): Use the `Accept-Encoding` header to tell the client and server to compress data before it's sent over the network. By using compression, you can reduce the amount of data that needs to be sent, resulting in faster load times.
  3. Use custom headers: You can also use custom headers in your `vercel.json` file to add metadata specific to your application. For example, you could add a header that indicates the user's preferred language or the version of your application. See [Project Configuration](https://vercel.com/docs/project-configuration#headers) docs for more information.


##  [Request headers](https://vercel.com/docs/headers#request-headers)[](https://vercel.com/docs/headers#request-headers)
To learn about the request headers sent to each Vercel deployment and how to use them to process requests before sending a response, see [Request headers](https://vercel.com/docs/headers/request-headers).
##  [Response headers](https://vercel.com/docs/headers#response-headers)[](https://vercel.com/docs/headers#response-headers)
To learn about the response headers included in Vercel deployment responses and how to use them to process responses before sending a response, see [Response headers](https://vercel.com/docs/headers/response-headers).
##  [Cache-Control header](https://vercel.com/docs/headers#cache-control-header)[](https://vercel.com/docs/headers#cache-control-header)
To learn about the cache-control headers sent to each Vercel deployment and how to use them to control the caching behavior of your application, see [Cache-Control headers](https://vercel.com/docs/caching/cache-control-headers).
##  [More resources](https://vercel.com/docs/headers#more-resources)[](https://vercel.com/docs/headers#more-resources)
  * [Set Caching Header](https://vercel.com/kb/guide/set-cache-control-headers)


* * *
[ Previous Caching ](https://vercel.com/docs/caching)[ Next Request Headers ](https://vercel.com/docs/headers/request-headers)
Was this helpful?
Send
