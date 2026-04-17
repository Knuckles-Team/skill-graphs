# How to handle redirects in Next.js
Last updated February 27, 2026
There are a few ways you can handle redirects in Next.js. This page will go through each available option, use cases, and how to manage large numbers of redirects.
API | Purpose | Where | Status Code
---|---|---|---
[`redirect`](https://nextjs.org/docs/app/guides/redirecting#redirect-function) | Redirect user after a mutation or event | Server Components, Server Functions, Route Handlers | 307 (Temporary) or 303 (Server Action)
[`permanentRedirect`](https://nextjs.org/docs/app/guides/redirecting#permanentredirect-function) | Redirect user after a mutation or event | Server Components, Server Functions, Route Handlers | 308 (Permanent)
[`useRouter`](https://nextjs.org/docs/app/guides/redirecting#userouter-hook) | Perform a client-side navigation | Event Handlers in Client Components | N/A
[`redirects` in `next.config.js`](https://nextjs.org/docs/app/guides/redirecting#redirects-in-nextconfigjs) | Redirect an incoming request based on a path |  `next.config.js` file | 307 (Temporary) or 308 (Permanent)
[`NextResponse.redirect`](https://nextjs.org/docs/app/guides/redirecting#nextresponseredirect-in-proxy) | Redirect an incoming request based on a condition | Proxy | Any
