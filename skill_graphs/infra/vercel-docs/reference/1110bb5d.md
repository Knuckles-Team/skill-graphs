##  [Considerations](https://vercel.com/docs/getting-started-with-vercel#considerations)[](https://vercel.com/docs/getting-started-with-vercel#considerations)
###  [Tradeoffs of Disabling Source Maps](https://vercel.com/docs/getting-started-with-vercel#tradeoffs-of-disabling-source-maps)[](https://vercel.com/docs/getting-started-with-vercel#tradeoffs-of-disabling-source-maps)
Disabling source maps in production has the benefit of not exposing your source code publicly, but it also means that errors in production will lack helpful stack traces, complicating the debugging process.
###  [Protected Deployments](https://vercel.com/docs/getting-started-with-vercel#protected-deployments)[](https://vercel.com/docs/getting-started-with-vercel#protected-deployments)
For [protected deployments](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments), it is generally safe to enable source maps, as these deployments are only accessible by authorized users who would already have access to your source code. Preview deployments are protected by default, making them a safe environment for enabling source maps.
###  [Third-Party Error Tracking Services](https://vercel.com/docs/getting-started-with-vercel#third-party-error-tracking-services)[](https://vercel.com/docs/getting-started-with-vercel#third-party-error-tracking-services)
If you use a third-party error tracking service like
  1. Uploading the source maps to your error tracking service
  2. Emptying or deleting the source maps before deploying to production


Many third-party providers like Sentry offer built-in configuration options to automatically delete sourcemaps after uploading them. Check your provider's documentation for these features before implementing a manual solution.
If you need to implement this manually, you can use an approach like this:
```
// Empty the source maps after uploading them to your error tracking service
const sourcemapFiles = await findFiles('.next', /\.js\.map$/);
await Promise.all(
  sourcemapFiles.map(async (file) => {
    await writeFile(file, '', 'utf8');
  }),
);
```

* * *
[ Previous Vercel Documentation ](https://vercel.com/docs)[ Next Projects and Deployments ](https://vercel.com/docs/getting-started-with-vercel/projects-deployments)
Was this helpful?
Send
On this page
  * [Examples](https://vercel.com/docs/getting-started-with-vercel#examples)
  * [How to fix](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)
  * [Considerations](https://vercel.com/docs/getting-started-with-vercel#considerations)
  * [Tradeoffs of Disabling Source Maps](https://vercel.com/docs/getting-started-with-vercel#tradeoffs-of-disabling-source-maps)
  * [Protected Deployments](https://vercel.com/docs/getting-started-with-vercel#protected-deployments)
  * [Third-Party Error Tracking Services](https://vercel.com/docs/getting-started-with-vercel#third-party-error-tracking-services)


Copy as MarkdownGive feedbackAsk AI about this page
