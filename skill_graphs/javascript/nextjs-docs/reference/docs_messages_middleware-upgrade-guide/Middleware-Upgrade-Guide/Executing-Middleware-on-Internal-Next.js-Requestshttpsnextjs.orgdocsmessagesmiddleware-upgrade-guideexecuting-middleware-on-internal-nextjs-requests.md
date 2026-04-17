## Executing Middleware on Internal Next.js Requests[](https://nextjs.org/docs/messages/middleware-upgrade-guide#executing-middleware-on-internal-nextjs-requests)
### Summary of changes[](https://nextjs.org/docs/messages/middleware-upgrade-guide#summary-of-changes-5)
  * Middleware will be executed for _all_ requests, including `_next`


### Explanation[](https://nextjs.org/docs/messages/middleware-upgrade-guide#explanation-5)
Prior to Next.js `v12.2`, Middleware was not executed for `_next` requests.
For cases where Middleware is used for authorization, you should migrate to use `rewrite`/`redirect` to Pages that show an authorization error, login forms, or to an API Route.
See [No Response Body](https://nextjs.org/docs/messages/middleware-upgrade-guide#no-response-body) for an example of how to migrate to use `rewrite`/`redirect`.
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
