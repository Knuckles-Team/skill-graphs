# allowedDevOrigins
Last updated February 27, 2026
Next.js does not automatically block cross-origin requests during development, but will block by default in a future major version of Next.js to prevent unauthorized requesting of internal assets/endpoints that are available in development mode.
To configure a Next.js application to allow requests from origins other than the hostname the server was initialized with (`localhost` by default) you can use the `allowedDevOrigins` config option.
`allowedDevOrigins` allows you to set additional origins that can be used in development mode. For example, to use `local-origin.dev` instead of only `localhost`, open `next.config.js` and add the `allowedDevOrigins` config:
next.config.js
```
module.exports = {
  allowedDevOrigins: ['local-origin.dev', '*.local-origin.dev'],
}
```

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
