## Options[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cssChunking#options)
  * **`true`(default)** : Next.js will try to merge CSS files whenever possible, determining explicit and implicit dependencies between files from import order to reduce the number of chunks and therefore the number of requests.
  * **`false`**: Next.js will not attempt to merge or re-order your CSS files.
  * **`'strict'`**: Next.js will load CSS files in the correct order they are imported into your files, which can lead to more chunks and requests.


You may consider using `'strict'` if you run into unexpected CSS behavior. For example, if you import `a.css` and `b.css` in different files using a different `import` order (`a` before `b`, or `b` before `a`), `true` will merge the files in any order and assume there are no dependencies between them. However, if `b.css` depends on `a.css`, you may want to use `'strict'` to prevent the files from being merged, and instead, load them in the order they are imported - which can result in more chunks and requests.
For most applications, we recommend `true` as it leads to fewer requests and better performance.
[PreviouscrossOrigin](https://nextjs.org/docs/app/api-reference/config/next-config-js/crossOrigin)[NextdeploymentId](https://nextjs.org/docs/app/api-reference/config/next-config-js/deploymentId)
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
