##  [Prerequisites](https://vercel.com/docs/speed-insights/quickstart#prerequisites)[](https://vercel.com/docs/speed-insights/quickstart#prerequisites)
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



  1. ###  [Enable Speed Insights in Vercel](https://vercel.com/docs/speed-insights/quickstart#enable-speed-insights-in-vercel)[](https://vercel.com/docs/speed-insights/quickstart#enable-speed-insights-in-vercel)
On the [Vercel dashboard](https://vercel.com/dashboard), select your Project followed by [Speed Insights](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fspeed-insights&title=Go+to+Speed+Insights) in the sidebar. You can also select the button below to be taken there. Then, select Enable from the dialog.
[Go to Speed Insights](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fspeed-insights&title=Open+Speed+Insights)
Enabling Speed Insights will add new routes (scoped at `/_vercel/speed-insights/*`) after your next deployment.
  2. ###  [Add `@vercel/speed-insights` to your project](https://vercel.com/docs/speed-insights/quickstart#add-@vercel/speed-insights-to-your-project)[](https://vercel.com/docs/speed-insights/quickstart#add-@vercel/speed-insights-to-your-project)
Using the package manager of your choice, add the `@vercel/speed-insights` package to your project:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i @vercel/speed-insights
```

```
yarn add @vercel/speed-insights
```

```
npm i @vercel/speed-insights
```

```
bun add @vercel/speed-insights
```

  3. ###  [Add the `SpeedInsights` component to your app](https://vercel.com/docs/speed-insights/quickstart#add-the-speedinsights-component-to-your-app)[](https://vercel.com/docs/speed-insights/quickstart#add-the-speedinsights-component-to-your-app)
The `SpeedInsights` component is a wrapper around the tracking script, offering more seamless integration with Next.js.
Add the following component to the root layout:
Next.js v13.5+Older Next.js versions
Add the following component to your main app file:
app/layout.tsx
Next.js (/app)
Next.js (/app) Next.js (/pages) SvelteKit Create React App Nuxt Vue Remix Astro HTML Other frameworks
TypeScript
TypeScript JavaScript Bash
```
import { SpeedInsights } from '@vercel/speed-insights/next';

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
        <SpeedInsights />
      </body>
    </html>
  );
}
```

For versions of Next.js older than 13.5, import the `<SpeedInsights>` component from `@vercel/speed-insights/react`.
Create a dedicated component to avoid opting out from SSR on the layout and pass the pathname of the route to the `SpeedInsights` component:
app/insights.tsx
Next.js (/app)
Next.js (/app) Next.js (/pages) SvelteKit Create React App Nuxt Vue Remix Astro HTML Other frameworks
TypeScript
TypeScript JavaScript Bash
```
'use client';

import { SpeedInsights } from '@vercel/speed-insights/react';
import { usePathname } from 'next/navigation';

export function Insights() {
  const pathname = usePathname();

  return <SpeedInsights route={pathname} />;
}
```

Then, import the `Insights` component in your layout:
app/layout.tsx
Next.js (/app)
Next.js (/app) Next.js (/pages) SvelteKit Create React App Nuxt Vue Remix Astro HTML Other frameworks
TypeScript
TypeScript JavaScript Bash
```
import type { ReactNode } from 'react';
import { Insights } from './insights';

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <head>
        <title>Next.js</title>
      </head>
      <body>
        {children}
        <Insights />
      </body>
    </html>
  );
}
```

  4. ###  [Deploy your app to Vercel](https://vercel.com/docs/speed-insights/quickstart#deploy-your-app-to-vercel)[](https://vercel.com/docs/speed-insights/quickstart#deploy-your-app-to-vercel)
You can deploy your app to Vercel's global [CDN](https://vercel.com/docs/cdn) by running the following command from your terminal:
terminal
```
vercel deploy
```

Alternatively, you can [connect your project's git repository](https://vercel.com/docs/git#deploying-a-git-repository), which will enable Vercel to deploy your latest pushes and merges to main.
Once your app is deployed, it's ready to begin tracking performance metrics.
If everything is set up correctly, you should be able to find the `/_vercel/speed-insights/script.js` script inside the body tag of your page.
  5. ###  [View your data in the dashboard](https://vercel.com/docs/speed-insights/quickstart#view-your-data-in-the-dashboard)[](https://vercel.com/docs/speed-insights/quickstart#view-your-data-in-the-dashboard)
Once your app is deployed, and users have visited your site, you can view the data in the dashboard.
To do so, go to your [dashboard](https://vercel.com/dashboard), select your project, and click [Speed Insights](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fspeed-insights&title=Go+to+Speed+Insights) in the sidebar.
After a few days of visitors, you'll be able to start exploring your metrics. For more information on how to use Speed Insights, see [Using Speed Insights](https://vercel.com/docs/speed-insights/using-speed-insights).


Learn more about how Vercel supports [privacy and data compliance standards](https://vercel.com/docs/speed-insights/privacy-policy) with Vercel Speed Insights.
