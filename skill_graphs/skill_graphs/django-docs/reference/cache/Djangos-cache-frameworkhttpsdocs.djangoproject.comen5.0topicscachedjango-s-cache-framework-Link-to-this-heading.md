# Django’s cache framework[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#django-s-cache-framework "Link to this heading")
A fundamental trade-off in dynamic websites is, well, they’re dynamic. Each time a user requests a page, the web server makes all sorts of calculations – from database queries to template rendering to business logic – to create the page that your site’s visitor sees. This is a lot more expensive, from a processing-overhead perspective, than your standard read-a-file-off-the-filesystem server arrangement.
For most web applications, this overhead isn’t a big deal. Most web applications aren’t `washingtonpost.com` or `slashdot.org`; they’re small- to medium-sized sites with so-so traffic. But for medium- to high-traffic sites, it’s essential to cut as much overhead as possible.
That’s where caching comes in.
To cache something is to save the result of an expensive calculation so that you don’t have to perform the calculation next time. Here’s some pseudocode explaining how this would work for a dynamically generated web page:
```
given a URL, try finding that page in the cache
if the page is in the cache:
    return the cached page
else:
    generate the page
    save the generated page in the cache (for next time)
    return the generated page

```

Django comes with a robust cache system that lets you save dynamic pages so they don’t have to be calculated for each request. For convenience, Django offers different levels of cache granularity: You can cache the output of specific views, you can cache only the pieces that are difficult to produce, or you can cache your entire site.
Django also works well with “downstream” caches, such as
See also
The [Cache Framework design philosophy](https://docs.djangoproject.com/en/5.0/misc/design-philosophies/#cache-design-philosophy) explains a few of the design decisions of the framework.
