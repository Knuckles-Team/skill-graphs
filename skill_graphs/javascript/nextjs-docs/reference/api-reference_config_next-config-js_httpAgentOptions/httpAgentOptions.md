# httpAgentOptions
Last updated February 27, 2026
In Node.js versions prior to 18, Next.js automatically polyfills `fetch()` with [undici](https://nextjs.org/docs/architecture/supported-browsers#polyfills) and enables
To disable HTTP Keep-Alive for all `fetch()` calls on the server-side, open `next.config.js` and add the `httpAgentOptions` config:
next.config.js
```
module.exports = {
  httpAgentOptions: {
    keepAlive: false,
  },
}
```

[PrevioushtmlLimitedBots](https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots)[Nextimages](https://nextjs.org/docs/app/api-reference/config/next-config-js/images)
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
