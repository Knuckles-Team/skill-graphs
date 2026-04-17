Getting Started
Getting Started
# Getting started with Vercel
Last updated September 24, 2025
Vercel is a platform for developers that provides the tools, workflows, and infrastructure you need to build and deploy your web apps faster, without the need for additional configuration.
Vercel supports [popular frontend frameworks](https://vercel.com/docs/frameworks) out-of-the-box, and its scalable, secure infrastructure is globally distributed to serve content from data centers near your users for optimal speeds.
During development, Vercel provides tools for real-time collaboration on your projects such as automatic preview and production environments, and comments on preview deployments.
##  [Before you begin](https://vercel.com/docs/getting-started-with-vercel#before-you-begin)[](https://vercel.com/docs/getting-started-with-vercel#before-you-begin)
To get started, create an account with Vercel. You can [select the plan](https://vercel.com/docs/plans) that's right for you.
  * [Sign up for a new Vercel account](https://vercel.com/signup)
  * [Log in to your existing Vercel account](https://vercel.com/login)


Once you create an account, you can choose to authenticate either with a Git provider or by using an email. When using email authentication, you may need to confirm both your email address and a phone number.
##  [Customizing your journey](https://vercel.com/docs/getting-started-with-vercel#customizing-your-journey)[](https://vercel.com/docs/getting-started-with-vercel#customizing-your-journey)
This tutorial is framework agnostic but Vercel supports many frontend [frameworks](https://vercel.com/docs/frameworks/more-frameworks). As you go through the docs, the quickstarts will provide specific instructions for your framework. If you don't find what you need, give us feedback and we'll update them!
While many of our instructions use the dashboard, you can also use [Vercel CLI](https://vercel.com/docs/cli) to carry out most tasks on Vercel. In this tutorial, look for the "Using CLI?" section for the CLI steps. To use the CLI, you'll need to install it:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i -g vercel
```

```
yarn global add vercel
```

```
npm i -g vercel
```

```
bun add -g vercel
```

[Let's go](https://vercel.com/docs/getting-started-with-vercel/projects-deployments)
* * *
[ Previous Vercel Documentation ](https://vercel.com/docs)[ Next Projects and Deployments ](https://vercel.com/docs/getting-started-with-vercel/projects-deployments)
Was this helpful?
Send
Getting Started
# NEXTJS_NO_SELF_HOSTED_VIDEOS
Last updated November 25, 2025
Video files, which are typically large, can consume a lot of bandwidth for your Next.js application. Video files are better served from a dedicated video CDN that is optimized for serving videos.
##  [How to fix](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)[](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)
Vercel Blob can be used for storing and serving large files such as videos.
You can use either [server uploads or client uploads](https://vercel.com/docs/storage/vercel-blob#server-and-client-uploads) depending on the file size:
  * [Server uploads](https://vercel.com/docs/storage/vercel-blob/server-upload) are suitable for files up to 4.5 MB
  * [Client uploads](https://vercel.com/docs/storage/vercel-blob/client-upload) allow for uploading larger files directly from the browser to Vercel Blob, supporting files up to 5 TB (5,000 GB)


See the [best practices for hosting videos on Vercel](https://vercel.com/kb/guide/best-practices-for-hosting-videos-on-vercel-nextjs-mp4-gif) guide to learn more about various other options for hosting videos.
* * *
[ Previous Vercel Documentation ](https://vercel.com/docs)[ Next Projects and Deployments ](https://vercel.com/docs/getting-started-with-vercel/projects-deployments)
Was this helpful?
Send
