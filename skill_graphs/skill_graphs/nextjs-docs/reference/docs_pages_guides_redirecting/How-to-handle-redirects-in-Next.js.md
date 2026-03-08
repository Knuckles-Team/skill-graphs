# How to handle redirects in Next.js
Last updated February 27, 2026
There are a few ways you can handle redirects in Next.js. This page will go through each available option, use cases, and how to manage large numbers of redirects.
API | Purpose | Where | Status Code
---|---|---|---
[`useRouter`](https://nextjs.org/docs/pages/guides/redirecting#userouter-hook) | Perform a client-side navigation | Components | N/A
[`redirects` in `next.config.js`](https://nextjs.org/docs/pages/guides/redirecting#redirects-in-nextconfigjs) | Redirect an incoming request based on a path |  `next.config.js` file | 307 (Temporary) or 308 (Permanent)
[`NextResponse.redirect`](https://nextjs.org/docs/pages/guides/redirecting#nextresponseredirect-in-proxy) | Redirect an incoming request based on a condition | Proxy | Any
