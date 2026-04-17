##  [Prerequisites](https://vercel.com/docs/edge-config/edge-config-integrations/launchdarkly-edge-config#prerequisites)[](https://vercel.com/docs/edge-config/edge-config-integrations/launchdarkly-edge-config#prerequisites)
Before using this integration, you should have:
  1. The latest version of Vercel CLI. To check your version, use `vercel --version`. To [install](https://vercel.com/docs/cli#installing-vercel-cli) or update Vercel CLI, use:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i -g vercel@latest
```

```
yarn global add vercel@latest
```

```
npm i -g vercel@latest
```

```
bun add -g vercel@latest
```

  2. A project. If you don't have one, you can run the following terminal commands to create a Next project:


Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm create next-app@latest
```

```
yarn create next-app@latest
```

```
npx create-next-app@latest
```

```
bunx create-next-app@latest
```

  1. A Vercel project. If you don't have one, see [Creating a Project](https://vercel.com/docs/projects/overview#creating-a-project)
  2. An Edge Config. If you don't have one, follow [the Edge Config quickstart](https://vercel.com/docs/edge-config/get-started)
  3. The Edge Config SDK:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i @vercel/edge-config
```

```
yarn add @vercel/edge-config
```

```
npm i @vercel/edge-config
```

```
bun add @vercel/edge-config
```



  1. ###  [Set up the LaunchDarkly integration](https://vercel.com/docs/edge-config/edge-config-integrations/launchdarkly-edge-config#set-up-the-launchdarkly-integration)[](https://vercel.com/docs/edge-config/edge-config-integrations/launchdarkly-edge-config#set-up-the-launchdarkly-integration)
Visit [the LaunchDarkly page in the Integration Marketplace](https://vercel.com/marketplace/launchdarkly) and select the Add Integration button. From the Integration dialog:
    1. Select a Vercel team and project to connect the integration to
    2. Log into LaunchDarkly
    3. Select the Authorize button to allow the integration to access your LaunchDarkly account data
    4. Name the integration, and select an existing Edge Config or create a new one
  2. ###  [Get your client-side ID](https://vercel.com/docs/edge-config/edge-config-integrations/launchdarkly-edge-config#get-your-client-side-id)[](https://vercel.com/docs/edge-config/edge-config-integrations/launchdarkly-edge-config#get-your-client-side-id)
To use the integration, you'll need your client-side ID from LaunchDarkly. Here's how to add it to your project:
    1. Select the LaunchDarkly project your integration is connected to
    2. On the next page, copy the Client-side ID under the environment your integration is connected to (for example, Test or Production)
Now, you must add the value to your project as an Environment Variable:
    1. Navigate to [your Vercel dashboard](https://vercel.com/dashboard) and select the project you want to use LaunchDarkly with
    2. Under the Settings tab, navigate to Environment Variables, and create an `LD_CLIENT_SIDE_ID` variable with the value of your client-side ID
[See our Environment Variables docs to learn more](https://vercel.com/docs/environment-variables#creating-environment-variables).
  3. ###  [Use the LaunchDarkly integration in your code](https://vercel.com/docs/edge-config/edge-config-integrations/launchdarkly-edge-config#use-the-launchdarkly-integration-in-your-code)[](https://vercel.com/docs/edge-config/edge-config-integrations/launchdarkly-edge-config#use-the-launchdarkly-integration-in-your-code)
Open your project's code on your local machine and do the following:
    1. Install LaunchDarkly's Vercel Server SDK:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i @launchdarkly/vercel-server-sdk
```

```
yarn add @launchdarkly/vercel-server-sdk
```

```
npm i @launchdarkly/vercel-server-sdk
```

```
bun add @launchdarkly/vercel-server-sdk
```

    1. Use [Vercel CLI](https://vercel.com/docs/cli#installing-vercel-cli) to pull your Vercel project's environment variables:
```
vercel env pull
```

    2. Finally, create a `middleware.ts` file at the root of your project. This file will configure a Middleware that redirects your site visitors from `/homepage` to `/new-homepage` based on a feature flag fetched from LaunchDarkly:
middleware.ts
TypeScript
TypeScript JavaScript Bash
```
import { init } from '@launchdarkly/vercel-server-sdk';
import { createClient } from '@vercel/edge-config';

const edgeConfigClient = createClient(process.env.EDGE_CONFIG!);
const launchDarklyClient = init('YOUR CLIENT-SIDE ID', edgeConfigClient);

export const config = {
  // Only run the middleware on the dashboard route
  matcher: '/homepage',
};

export default function middleware(request: Request): Response {
  await launchDarklyClient.initFromServerIfNeeded();
  const launchDarklyContext = { kind: 'org', key: 'my-org-key' };
  const showExperimentalHomepage = await launchDarklyClient.variation(
    'experimental-homepage',
    launchDarklyContext,
    true,
  );

  if (showExperimentalHomepage) {
    const url = new URL(request.url);
    url.pathname = '/new-homepage';
    return Response.redirect(url);
  }
}
```
