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
# NestJS on Vercel
Last updated October 28, 2025
NestJS is a progressive Node.js framework for building efficient, reliable and scalable server-side applications. You can deploy a NestJS app to Vercel with zero configuration using [Vercel Functions](https://vercel.com/docs/functions).
NestJS applications on Vercel benefit from:
  * [Fluid compute](https://vercel.com/docs/fluid-compute): Pay for the CPU you use, automatic cold start reduction, optimized concurrency, background processing, and more
  * [Preview deployments](https://vercel.com/docs/deployments/environments#preview-environment-pre-production): Test your changes in a copy of your production infrastructure
  * [Instant Rollback](https://vercel.com/docs/instant-rollback): Recover from breaking changes or bugs in milliseconds
  * [Vercel Firewall](https://vercel.com/docs/vercel-firewall): Protect your applications from a wide range of threats with a robust, multi-layered security system
  * [Secure Compute](https://vercel.com/docs/secure-compute): Create private links between your Vercel-hosted backend and other clouds


##  [Get started with NestJS on Vercel](https://vercel.com/docs/getting-started-with-vercel#get-started-with-nestjs-on-vercel)[](https://vercel.com/docs/getting-started-with-vercel#get-started-with-nestjs-on-vercel)
You can quickly deploy a NestJS application to Vercel by creating a NestJS app or using an existing one:
[![](https://api-frameworks.vercel.sh/framework-logos/nestjs.svg)Deploy NestJS to Vercel](https://vercel.com/templates/backend/nestjs-on-vercel)
[Deploy](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fvercel%2Ftree%2Fmain%2Fexamples%2Fnestjs&template=nestjs)
##  [NestJS entrypoint detection](https://vercel.com/docs/getting-started-with-vercel#nestjs-entrypoint-detection)[](https://vercel.com/docs/getting-started-with-vercel#nestjs-entrypoint-detection)
To allow Vercel to deploy your NestJS application and process web requests, your server entrypoint file should be named one of the following:
  * `src/main.{js,mjs,cjs,ts,cts,mts}`
  * `src/app.{js,mjs,cjs,ts,cts,mts}`
  * `src/index.{js,mjs,cjs,ts,cts,mts}`
  * `src/server.{js,mjs,cjs,ts,cts,mts}`
  * `app.{js,mjs,cjs,ts,cts,mts}`
  * `index.{js,mjs,cjs,ts,cts,mts}`
  * `server.{js,mjs,cjs,ts,cts,mts}`


For example, use the following code as an entrypoint:
src/app.ts
```
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(process.env.PORT ?? 3000);
}
bootstrap();
```

###  [Local development](https://vercel.com/docs/getting-started-with-vercel#local-development)[](https://vercel.com/docs/getting-started-with-vercel#local-development)
Use `vercel dev` to run your application locally
terminal
```
vercel dev
```

Minimum CLI version required: 48.4.0
###  [Deploying the application](https://vercel.com/docs/getting-started-with-vercel#deploying-the-application)[](https://vercel.com/docs/getting-started-with-vercel#deploying-the-application)
To deploy, [connect your Git repository](https://vercel.com/new) or [use Vercel CLI](https://vercel.com/docs/cli/deploy):
terminal
```
vc deploy
```

Minimum CLI version required: 48.4.0
##  [Vercel Functions](https://vercel.com/docs/getting-started-with-vercel#vercel-functions)[](https://vercel.com/docs/getting-started-with-vercel#vercel-functions)
When you deploy a NestJS app to Vercel, your NestJS application becomes a single [Vercel Function](https://vercel.com/docs/functions) and uses [Fluid compute](https://vercel.com/docs/fluid-compute) by default. This means your NestJS app will automatically scale up and down based on traffic.
##  [Limitations](https://vercel.com/docs/getting-started-with-vercel#limitations)[](https://vercel.com/docs/getting-started-with-vercel#limitations)
All [Vercel Functions limitations](https://vercel.com/docs/functions/limitations) apply to the NestJS application, including the size of the application being limited to 250MB.
##  [More resources](https://vercel.com/docs/getting-started-with-vercel#more-resources)[](https://vercel.com/docs/getting-started-with-vercel#more-resources)
Learn more about deploying NestJS projects on Vercel with the following resources:
  * [Vercel Functions documentation](https://vercel.com/docs/functions)
  * [Backend templates on Vercel](https://vercel.com/templates?type=backend)


* * *
[ Previous Vercel Documentation ](https://vercel.com/docs)[ Next Projects and Deployments ](https://vercel.com/docs/getting-started-with-vercel/projects-deployments)
Was this helpful?
Send
