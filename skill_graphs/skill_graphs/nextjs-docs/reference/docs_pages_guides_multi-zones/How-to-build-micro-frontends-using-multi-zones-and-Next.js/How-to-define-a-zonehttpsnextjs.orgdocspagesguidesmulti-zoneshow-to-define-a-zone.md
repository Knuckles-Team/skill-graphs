## How to define a zone[](https://nextjs.org/docs/pages/guides/multi-zones#how-to-define-a-zone)
A zone is a normal Next.js application where you also configure an [assetPrefix](https://nextjs.org/docs/app/api-reference/config/next-config-js/assetPrefix) to avoid conflicts with pages and static files in other zones.
next.config.js
```
/** @type {import('next').NextConfig} */
const nextConfig = {
  assetPrefix: '/blog-static',
}
```

Next.js assets, such as JavaScript and CSS, will be prefixed with `assetPrefix` to make sure that they don't conflict with assets from other zones. These assets will be served under `/assetPrefix/_next/...` for each of the zones.
The default application handling all paths not routed to another more specific zone does not need an `assetPrefix`.
In versions older than Next.js 15, you may also need an additional rewrite to handle the static assets. This is no longer necessary in Next.js 15.
next.config.js
```
/** @type {import('next').NextConfig} */
const nextConfig = {
  assetPrefix: '/blog-static',
  async rewrites() {
    return {
      beforeFiles: [
        {
          source: '/blog-static/_next/:path+',
          destination: '/_next/:path+',
        },
      ],
    }
  },
}
```
