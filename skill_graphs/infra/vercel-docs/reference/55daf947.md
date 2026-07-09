##  [Prerequisites](https://vercel.com/docs/analytics/quickstart#prerequisites)[](https://vercel.com/docs/analytics/quickstart#prerequisites)
  * A Vercel account. If you don't have one, you can [sign up for free](https://vercel.com/signup).
  * A Vercel project. If you don't have one, you can [create a new project](https://vercel.com/new).
  * The Vercel CLI installed. If you don't have it, you can install it using the following command:
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



  1. ###  [Enable Web Analytics in Vercel](https://vercel.com/docs/analytics/quickstart#enable-web-analytics-in-vercel)[](https://vercel.com/docs/analytics/quickstart#enable-web-analytics-in-vercel)
On the [Vercel dashboard](https://vercel.com/dashboard), select your Project and then click [Analytics](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fanalytics&title=Go+to+Analytics) in the sidebar and click Enable from the dialog.
[Go to Web Analytics](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fanalytics&title=Open+Web+Analytics)
Enabling Web Analytics will add new routes (scoped at `/_vercel/insights/*`) after your next deployment.
  2. ###  [Add `@vercel/analytics` to your project](https://vercel.com/docs/analytics/quickstart#add-@vercel/analytics-to-your-project)[](https://vercel.com/docs/analytics/quickstart#add-@vercel/analytics-to-your-project)
Using the package manager of your choice, add the `@vercel/analytics` package to your project:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i @vercel/analytics
```

```
yarn add @vercel/analytics
```

```
npm i @vercel/analytics
```

```
bun add @vercel/analytics
```

  3. ###  [Add the `Analytics` component to your app](https://vercel.com/docs/analytics/quickstart#add-the-analytics-component-to-your-app)[](https://vercel.com/docs/analytics/quickstart#add-the-analytics-component-to-your-app)
The `Analytics` component is a wrapper around the tracking script, offering more seamless integration with Next.js, including route support.
Add the following code to the root layout:
app/layout.tsx
Next.js (/app)
Next.js (/app) Next.js (/pages) SvelteKit Create React App Nuxt Vue Remix Astro HTML Other frameworks
TypeScript
TypeScript JavaScript Bash
```
import { Analytics } from '@vercel/analytics/next';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <title>Next.js</title>
      </head>
      <body>
        {children}
        <Analytics />
      </body>
    </html>
  );
}
```

  4. ###  [Deploy your app to Vercel](https://vercel.com/docs/analytics/quickstart#deploy-your-app-to-vercel)[](https://vercel.com/docs/analytics/quickstart#deploy-your-app-to-vercel)
Deploy your app using the following command:
terminal
```
vercel deploy
```

If you haven't already, we also recommend [connecting your project's Git repository](https://vercel.com/docs/git#deploying-a-git-repository), which will enable Vercel to deploy your latest commits to main without terminal commands.
Once your app is deployed, it will start tracking visitors and page views.
If everything is set up properly, you should be able to see a Fetch/XHR request in your browser's Network tab from `/_vercel/insights/view` when you visit any page.
  5. ###  [View your data in the dashboard](https://vercel.com/docs/analytics/quickstart#view-your-data-in-the-dashboard)[](https://vercel.com/docs/analytics/quickstart#view-your-data-in-the-dashboard)
Once your app is deployed, and users have visited your site, you can view your data in the dashboard.
To do so, go to your [dashboard](https://vercel.com/dashboard), select your project, and click [Analytics](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fanalytics&title=Go+to+Analytics) in the sidebar.
After a few days of visitors, you'll be able to start exploring your data by viewing and [filtering](https://vercel.com/docs/analytics/filtering) the panels.
Users on Pro and Enterprise plans can also add [custom events](https://vercel.com/docs/analytics/custom-events) to their data to track user interactions such as button clicks, form submissions, or purchases.


Learn more about how Vercel supports [privacy and data compliance standards](https://vercel.com/docs/analytics/privacy-policy) with Vercel Web Analytics.
