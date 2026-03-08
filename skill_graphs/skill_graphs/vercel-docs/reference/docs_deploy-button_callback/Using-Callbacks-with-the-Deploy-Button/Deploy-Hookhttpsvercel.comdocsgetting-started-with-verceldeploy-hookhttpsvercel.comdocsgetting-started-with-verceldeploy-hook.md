##  [Deploy Hook](https://vercel.com/docs/getting-started-with-vercel#deploy-hook)[](https://vercel.com/docs/getting-started-with-vercel#deploy-hook)
Parameter | Type | Value
---|---|---
`production-deploy-hook` | `string` | The name of the Deploy Hook to set up.
The Deploy Hook parameter allows you to receive [a URL](https://vercel.com/docs/deploy-hooks) when also using the Redirect URL parameter, which you can use to redeploy user's projects for them.
This is useful if you are directing a user to deploy a project that works with your application, for example a headless CMS, and you need to redeploy the user's project in case of a content change that needs to be rebuilt.
The value of this parameter should be the name of the [Deploy Hook](https://vercel.com/docs/deploy-hooks) you want to create for the user.
When redirected back to your application upon a successful deployment for the user, you will get the `production-deploy-hook-url` callback parameter in addition to [the default callback parameters](https://vercel.com/docs/getting-started-with-vercel#callback-parameters).
This parameter requires the [Redirect URL](https://vercel.com/docs/getting-started-with-vercel#redirect-url) parameter to also be set.
The example below shows a Deploy Button source URL using the Redirect URL and production Deploy Hook URL parameters:
deploy hook
```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&redirect-url=https%3A%2F%2Fmy-headless-application.com&production-deploy-hook=MyHeadlessProject
```

* * *
[ Previous Vercel Documentation ](https://vercel.com/docs)[ Next Projects and Deployments ](https://vercel.com/docs/getting-started-with-vercel/projects-deployments)
Was this helpful?
Send
On this page
  * [Redirect URL](https://vercel.com/docs/getting-started-with-vercel#redirect-url)
  * [Callback Parameters](https://vercel.com/docs/getting-started-with-vercel#callback-parameters)
  * [Developer ID](https://vercel.com/docs/getting-started-with-vercel#developer-id)
  * [External ID](https://vercel.com/docs/getting-started-with-vercel#external-id)
  * [Deploy Hook](https://vercel.com/docs/getting-started-with-vercel#deploy-hook)


Copy as MarkdownGive feedbackAsk AI about this page
