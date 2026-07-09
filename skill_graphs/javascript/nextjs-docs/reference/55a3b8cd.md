# webVitalsAttribution
This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on
Last updated February 27, 2026
When debugging issues related to Web Vitals, it is often helpful if we can pinpoint the source of the problem. For example, in the case of Cumulative Layout Shift (CLS), we might want to know the first element that shifted when the single largest layout shift occurred. Or, in the case of Largest Contentful Paint (LCP), we might want to identify the element corresponding to the LCP for the page. If the LCP element is an image, knowing the URL of the image resource can help us locate the asset we need to optimize.
Pinpointing the biggest contributor to the Web Vitals score, aka
Attribution is disabled by default in Next.js but can be enabled **per metric** by specifying the following in `next.config.js`.
next.config.js
```
module.exports = {
  experimental: {
    webVitalsAttribution: ['CLS', 'LCP'],
  },
}
```

Valid attribution values are all `web-vitals` metrics specified in the
[Previouswebpack](https://nextjs.org/docs/app/api-reference/config/next-config-js/webpack)[NextTypeScript](https://nextjs.org/docs/app/api-reference/config/typescript)
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
