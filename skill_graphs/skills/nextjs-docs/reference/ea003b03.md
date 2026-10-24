## Caveats[](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization#caveats)
  * If you have a [custom `App`](https://nextjs.org/docs/pages/building-your-application/routing/custom-app) with `getInitialProps` then this optimization will be turned off in pages without [Static Generation](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props).
  * If you have a [custom `Document`](https://nextjs.org/docs/pages/building-your-application/routing/custom-document) with `getInitialProps` be sure you check if `ctx.req` is defined before assuming the page is server-side rendered. `ctx.req` will be `undefined` for pages that are prerendered.
  * Avoid using the `asPath` value on [`next/router`](https://nextjs.org/docs/pages/api-reference/functions/use-router#router-object) in the rendering tree until the router's `isReady` field is `true`. Statically optimized pages only know `asPath` on the client and not the server, so using it as a prop may lead to mismatch errors. The `asPath` as a prop.


Was this helpful?
Send
* * *
* * *
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Next.js Conf](https://nextjs.org/conf)[Evals](https://nextjs.org/evals)
#### More
[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)
#### About Vercel
#### Legal
Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
* * *
* * *
