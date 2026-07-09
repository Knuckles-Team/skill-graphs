## How to route requests to the right zone[](https://nextjs.org/docs/app/guides/multi-zones#how-to-route-requests-to-the-right-zone)
With the Multi Zones set-up, you need to route the paths to the correct zone since they are served by different applications. You can use any HTTP proxy to do this, but one of the Next.js applications can also be used to route requests for the entire domain.
To route to the correct zone using a Next.js application, you can use [`rewrites`](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites). For each path served by a different zone, you would add a rewrite rule to send that path to the domain of the other zone, and you also need to rewrite the requests for the static assets. For example:
next.config.js
```
async rewrites() {
    return [
        {
            source: '/blog',
            destination: `${process.env.BLOG_DOMAIN}/blog`,
        },
        {
            source: '/blog/:path+',
            destination: `${process.env.BLOG_DOMAIN}/blog/:path+`,
        },
        {
            source: '/blog-static/:path+',
            destination: `${process.env.BLOG_DOMAIN}/blog-static/:path+`,
        }
    ];
}
```

`destination` should be a URL that is served by the zone, including scheme and domain. This should point to the zone's production domain, but it can also be used to route requests to `localhost` in local development.
> **Good to know** : URL paths should be unique to a zone. For example, two zones trying to serve `/blog` would create a routing conflict.
### Routing requests using proxy[](https://nextjs.org/docs/app/guides/multi-zones#routing-requests-using-proxy)
Routing requests through [`rewrites`](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites) is recommended to minimize latency overhead for the requests, but proxy can also be used when there is a need for a dynamic decision when routing. For example, if you are using a feature flag to decide where a path should be routed such as during a migration, you can use proxy.
proxy.js
```
export async function proxy(request) {
  const { pathname, search } = request.nextUrl
  if (pathname === '/your-path' && myFeatureFlag.isEnabled()) {
    return NextResponse.rewrite(`${rewriteDomain}${pathname}${search}`)
  }
}
```
