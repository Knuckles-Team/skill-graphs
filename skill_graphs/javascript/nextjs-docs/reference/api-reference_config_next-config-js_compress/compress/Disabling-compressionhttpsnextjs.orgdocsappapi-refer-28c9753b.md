## Disabling compression[](https://nextjs.org/docs/app/api-reference/config/next-config-js/compress#disabling-compression)
To disable **compression** , set the `compress` config option to `false`:
next.config.js
```
module.exports = {
  compress: false,
}
```

We **do not recommend disabling compression** unless you have compression configured on your server, as compression reduces bandwidth usage and improves the performance of your application. For example, you're using `brotli`, set the `compress` option to `false` to allow nginx to handle compression.
[PreviouscacheLife](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife)[NextcrossOrigin](https://nextjs.org/docs/app/api-reference/config/next-config-js/crossOrigin)
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
