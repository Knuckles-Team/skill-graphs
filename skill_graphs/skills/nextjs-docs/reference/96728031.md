## Server Actions[](https://nextjs.org/docs/app/guides/multi-zones#server-actions)
When using [Server Actions](https://nextjs.org/docs/app/getting-started/updating-data) with Multi-Zones, you must explicitly allow the user-facing origin since your user facing domain may serve multiple applications. In your `next.config.js` file, add the following lines:
next.config.js
```
const nextConfig = {
  experimental: {
    serverActions: {
      allowedOrigins: ['your-production-domain.com'],
    },
  },
}
```

See [`serverActions.allowedOrigins`](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions#allowedorigins) for more information.
[PreviousMulti-tenant](https://nextjs.org/docs/app/guides/multi-tenant)[NextOpenTelemetry](https://nextjs.org/docs/app/guides/open-telemetry)
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
