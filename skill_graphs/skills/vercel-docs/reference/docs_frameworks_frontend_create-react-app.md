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
# Create React App on Vercel
Last updated December 18, 2025
Create React App (CRA) is a development environment for building single-page applications with the React framework. It sets up and configures a new React project with the latest JavaScript features, and optimizes your app for production.
##  [Get Started with CRA on Vercel](https://vercel.com/docs/getting-started-with-vercel#get-started-with-cra-on-vercel)[](https://vercel.com/docs/getting-started-with-vercel#get-started-with-cra-on-vercel)
To get started with CRA on Vercel:
  * If you already have a project with CRA, install [Vercel CLI](https://vercel.com/docs/cli) and run the `vercel`command from your project's root directory
  * Clone one of our CRA example repos to your favorite git provider and deploy it on Vercel with the button below:


[![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/react.svg)Deploy our CRA template, or view a live example.](https://vercel.com/templates/react/create-react-app)
[Deploy](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fvercel%2Ftree%2Fmain%2Fexamples%2Fcreate-react-app&template=create-react-app)
  * Or, choose a template from Vercel's marketplace:
Get started in minutes
## Deploy a new CRA project with a template
[View All Templates](https://vercel.com/templates/react)
[![Create React App](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F2UUgkeU6sOmJLYTvXcjYtS%2F64969aae100f990c8a8be84d80dc3006%2Freact.png&w=3840&q=75) Create React App A client-side React app created with create-react-app. ](https://vercel.com/templates/react/create-react-app)[![Auth0 React Starter](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F7nPSny8D50VKSwshwKKNsh%2F95b29fe673d56d27a648b0a0430668ab%2Fget-started-auth0-react_-_Dan_Arias.png&w=3840&q=75) Auth0 React Starter React application that implements user login, logout and sign-up features using Auth0. ](https://vercel.com/templates/react/auth0-react)
[View All Templates](https://vercel.com/templates/react)


Vercel deployments can [integrate with your git provider](https://vercel.com/docs/git) to [generate preview URLs](https://vercel.com/docs/deployments/environments#preview-environment-pre-production) for each pull request you make to your CRA project.
##  [Static file caching](https://vercel.com/docs/getting-started-with-vercel#static-file-caching)[](https://vercel.com/docs/getting-started-with-vercel#static-file-caching)
On Vercel, static files are [replicated and deployed to every region in our global CDN after the first request](https://vercel.com/docs/cdn-cache#static-files-caching). This ensures that static files are served from the closest location to the visitor, improving performance and reducing latency.
Static files are cached for up to 31 days. If a file is unchanged, it can persist across deployments, as their hash caches static files. However, the cache is effectively invalidated when you redeploy, so we always serve the latest version.
To summarize, using Static Files with CRA on Vercel:
  * Automatically optimizes and caches assets for the best performance
  * Makes files easily accessible through the `public` folder
  * Supports zero-downtime rollouts
  * Requires no additional services needed to procure or set up


[Learn more about static files caching](https://vercel.com/docs/cdn-cache#static-files-caching)
##  [Preview Deployments](https://vercel.com/docs/getting-started-with-vercel#preview-deployments)[](https://vercel.com/docs/getting-started-with-vercel#preview-deployments)
When you deploy your CRA app to Vercel and connect your git repo, every pull request will generate a [Preview Deployment](https://vercel.com/docs/deployments/environments#preview-environment-pre-production).
Preview Deployments allow you to preview changes to your app in a live deployment. They are available by default for all projects, and are generated when you commit changes to a Git branch with an open pull request, or you create a deployment [using Vercel CLI](https://vercel.com/docs/cli/deploy#usage).
###  [Comments](https://vercel.com/docs/getting-started-with-vercel#comments)[](https://vercel.com/docs/getting-started-with-vercel#comments)
You can use the comments feature to receive feedback on your Preview Deployments from Vercel Team members and [people you share the Preview URL with](https://vercel.com/docs/comments/how-comments-work#sharing).
Comments allow you to start discussion threads, share screenshots, send notifications, and more.
To summarize, Preview Deployments with CRA on Vercel:
  * Enable you to share previews of pull request changes in a live environment
  * Come with a comment feature for improved collaboration and feedback
  * Experience changes to your product without merging them to your deployment branch


[Learn more about Preview Deployments](https://vercel.com/docs/deployments/environments#preview-environment-pre-production)
##  [Web Analytics](https://vercel.com/docs/getting-started-with-vercel#web-analytics)[](https://vercel.com/docs/getting-started-with-vercel#web-analytics)
Vercel's Web Analytics features enable you to visualize and monitor your application's performance over time. The Analytics section in your project's dashboard offers detailed insights into your website's visitors, with metrics like top pages, top referrers, and user demographics.
To use Web Analytics, navigate to the Analytics section in your project dashboard sidebar on Vercel and select Enable in the modal that appears.
To track visitors and page views, we recommend first installing our `@vercel/analytics` package.
You can then import the `inject` function from the package, which will add the tracking script to your app. This should only be called once in your app.
Add the following code to your main app file:
main.ts
TypeScript
TypeScript JavaScript Bash
```
import { inject } from '@vercel/analytics';

inject();
```

Then, [ensure you've enabled Web Analytics in your dashboard on Vercel](https://vercel.com/docs/analytics/quickstart). You should start seeing usage data in your Vercel dashboard.
To summarize, using Web Analytics with CRA on Vercel:
  * Enables you to track traffic and see your top-performing pages
  * Offers you detailed breakdowns of visitor demographics, including their OS, browser, geolocation and more


[Learn more about Web Analytics](https://vercel.com/docs/analytics)
##  [Speed Insights](https://vercel.com/docs/getting-started-with-vercel#speed-insights)[](https://vercel.com/docs/getting-started-with-vercel#speed-insights)
You can see data about your CRA project's [Core Web Vitals](https://vercel.com/docs/speed-insights/metrics#core-web-vitals-explained) performance in your dashboard on Vercel. Doing so will allow you to track your web application's loading speed, responsiveness, and visual stability so you can improve the overall user experience.
On Vercel, you can track your app's Core Web Vitals in your project's dashboard by enabling Speed Insights.
To summarize, using Speed Insights with CRA on Vercel:
  * Enables you to track traffic performance metrics, such as [First Contentful Paint](https://vercel.com/docs/speed-insights/metrics#first-contentful-paint-fcp), or [First Input Delay](https://vercel.com/docs/speed-insights/metrics#first-input-delay-fid)
  * Enables you to view performance analytics by page name and URL for more granular analysis
  * Shows you [a score for your app's performance](https://vercel.com/docs/speed-insights/metrics#how-the-scores-are-determined) on each recorded metric, which you can use to track improvements or regressions


[Learn more about Speed Insights](https://vercel.com/docs/speed-insights)
##  [Observability](https://vercel.com/docs/getting-started-with-vercel#observability)[](https://vercel.com/docs/getting-started-with-vercel#observability)
Vercel's observability features help you monitor, analyze, and manage your projects. From your project's dashboard on Vercel, you can track website usage and performance, record team members' activities, and visualize real-time data from logs.
[Activity Logs](https://vercel.com/docs/observability/activity-log), which you can see in the Activity section in your project dashboard sidebar, are available on all account plans. The following observability products are available for Enterprise teams:
  * [Monitoring](https://vercel.com/docs/observability/monitoring): A query editor that allows you to visualize, explore, and monitor your usage and traffic
  * [Runtime Logs](https://vercel.com/docs/runtime-logs): An interface that allows you to search and filter logs from static requests and Function invocations
  * [Audit Logs](https://vercel.com/docs/observability/audit-log): An interface that enables your team owners to track and analyze their team members' activity


For Pro (and Enterprise) accounts:
  * [Log Drains](https://vercel.com/docs/drains): Export your log data for better debugging and analyzing, either from the dashboard, or using one of [our integrations](https://vercel.com/integrations#logging)
  * [OpenTelemetry (OTEL) collector](https://vercel.com/docs/observability/audit-log): Send OTEL traces from your Vercel functions to application performance monitoring (APM) vendors


To summarize, using Vercel's observability features with CRA enable you to:
  * Visualize website usage data, performance metrics, and logs
  * Search and filter logs for static, and Function requests
  * Use queries to see in-depth information about your website's usage and traffic
  * Send your metrics and data to other observability services through our integrations
  * Track and analyze team members' activity


[Learn more about Observability](https://vercel.com/docs/observability)
##  [More benefits](https://vercel.com/docs/getting-started-with-vercel#more-benefits)[](https://vercel.com/docs/getting-started-with-vercel#more-benefits)
See [our Frameworks documentation page](https://vercel.com/docs/frameworks) to learn about the benefits available to all frameworks when you deploy on Vercel.
##  [More resources](https://vercel.com/docs/getting-started-with-vercel#more-resources)[](https://vercel.com/docs/getting-started-with-vercel#more-resources)
Learn more about deploying CRA projects on Vercel with the following resources:
  * [Remote caching docs](https://vercel.com/docs/monorepos/remote-caching)
  * [React with Formspree](https://vercel.com/kb/guide/deploying-react-forms-using-formspree-with-vercel)
  * [React Turborepo template](https://vercel.com/templates/react/turborepo-design-system)


* * *
[ Previous Vercel Documentation ](https://vercel.com/docs)[ Next Projects and Deployments ](https://vercel.com/docs/getting-started-with-vercel/projects-deployments)
Was this helpful?
Send
