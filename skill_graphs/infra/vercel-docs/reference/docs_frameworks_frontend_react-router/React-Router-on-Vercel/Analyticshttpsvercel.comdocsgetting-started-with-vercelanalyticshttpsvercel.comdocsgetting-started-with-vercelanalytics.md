##  [Analytics](https://vercel.com/docs/getting-started-with-vercel#analytics)[](https://vercel.com/docs/getting-started-with-vercel#analytics)
[Vercel's Analytics](https://vercel.com/docs/analytics) features enable you to visualize and monitor your application's performance over time. The Analytics section in your project's dashboard offers detailed insights into your website's visitors, with metrics like top pages, top referrers, and user demographics.
To use Analytics, navigate to the Analytics section in your project dashboard sidebar on Vercel and select Enable in the modal that appears.
To track visitors and page views, we recommend first installing our `@vercel/analytics` package by running the terminal command below in the root directory of your React Router project:
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

Then, follow the instructions below to add the `Analytics` component to your app. The `Analytics` component is a wrapper around Vercel's tracking script, offering a seamless integration with React Router.
Add the following component to your `root` file:
app/root.tsx
TypeScript
TypeScript JavaScript Bash
```
import { Analytics } from '@vercel/analytics/react';

export default function App() {
  return (
    <html lang="en">
      <body>
        <Analytics />
      </body>
    </html>
  );
}
```

To summarize, Analytics with React Router on Vercel:
  * Enables you to track traffic and see your top-performing pages
  * Offers you detailed breakdowns of visitor demographics, including their OS, browser, geolocation and more


[Learn more about Analytics](https://vercel.com/docs/analytics)
