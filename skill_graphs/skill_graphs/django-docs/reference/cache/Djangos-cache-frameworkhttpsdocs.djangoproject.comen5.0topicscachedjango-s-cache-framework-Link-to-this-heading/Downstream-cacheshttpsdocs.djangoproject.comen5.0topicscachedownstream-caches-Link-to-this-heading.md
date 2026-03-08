## Downstream caches[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#downstream-caches "Link to this heading")
So far, this document has focused on caching your _own_ data. But another type of caching is relevant to web development, too: caching performed by “downstream” caches. These are systems that cache pages for users even before the request reaches your website.
Here are a few examples of downstream caches:
  * When using HTTP, your ISP may cache certain pages, so if you requested a page from `http://example.com/`, your ISP would send you the page without having to access example.com directly. The maintainers of example.com have no knowledge of this caching; the ISP sits between example.com and your web browser, handling all of the caching transparently. Such caching is not possible under HTTPS as it would constitute a man-in-the-middle attack.
  * Your Django website may sit behind a _proxy cache_ , such as Squid Web Proxy Cache (
  * Your web browser caches pages, too. If a web page sends out the appropriate headers, your browser will use the local cached copy for subsequent requests to that page, without even contacting the web page again to see whether it has changed.


Downstream caching is a nice efficiency boost, but there’s a danger to it: Many web pages’ contents differ based on authentication and a host of other variables, and cache systems that blindly save pages based purely on URLs could expose incorrect or sensitive data to subsequent visitors to those pages.
For example, if you operate a web email system, then the contents of the “inbox” page depend on which user is logged in. If an ISP blindly cached your site, then the first user who logged in through that ISP would have their user-specific inbox page cached for subsequent visitors to the site. That’s not cool.
Fortunately, HTTP provides a solution to this problem. A number of HTTP headers exist to instruct downstream caches to differ their cache contents depending on designated variables, and to tell caching mechanisms not to cache particular pages. We’ll look at some of these headers in the sections that follow.
