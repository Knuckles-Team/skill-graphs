##  [Automatic URL normalization](https://vercel.com/docs/routing/redirects#automatic-url-normalization)[](https://vercel.com/docs/routing/redirects#automatic-url-normalization)
Vercel's CDN automatically normalizes certain URL patterns and redirects with a `308` status code. These normalizations happen before your redirects, rewrites, or application code runs.
###  [Consecutive slashes](https://vercel.com/docs/routing/redirects#consecutive-slashes)[](https://vercel.com/docs/routing/redirects#consecutive-slashes)
The CDN normalizes URLs containing consecutive slashes (e.g., `//`) to single slashes and redirects with a `308` status code.
For example:
  * `/blog//post` redirects to `/blog/post`
  * `//about` redirects to `/about`


###  [Case sensitivity](https://vercel.com/docs/routing/redirects#case-sensitivity)[](https://vercel.com/docs/routing/redirects#case-sensitivity)
The CDN does not normalize URL paths to lowercase. URLs are case-sensitive, and requests are served exactly as specified.
For example, `/About` and `/about` are treated as different paths. If no content exists at the requested path with the given case, the CDN returns a `404` response.
