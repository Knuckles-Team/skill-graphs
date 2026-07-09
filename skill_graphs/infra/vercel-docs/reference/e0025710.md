##  [Prerequisites](https://vercel.com/docs/edge-config/edge-config-integrations/split-edge-config#prerequisites)[](https://vercel.com/docs/edge-config/edge-config-integrations/split-edge-config#prerequisites)
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



To configure this integration, Split Admin access (Split Admin users can add feature flags and segments, and edit them at will) is required.
  1. ###  [Set up the Split integration](https://vercel.com/docs/edge-config/edge-config-integrations/split-edge-config#set-up-the-split-integration)[](https://vercel.com/docs/edge-config/edge-config-integrations/split-edge-config#set-up-the-split-integration)
Visit [the Split page in the Vercel Integration Marketplace](https://vercel.com/marketplace/split) and select the Add Integration button. From the Integration dialog:
    1. Select a Vercel team and project to connect the integration to
    2. Log into Split
    3. Select the
    4. Select an existing Edge Config or create a new one
    5. Copy the Edge Config item key provided on this page. You'll need it to add it to your Environment Variables
You can also find your Edge Config Split item key in [your dashboard on Vercel](https://vercel.com/dashboard/integrations). In the **Integrations** section in the sidebar, select **Manage** , then select **Configure** on the integration page. You should see the item key on the page that opens.
  2. ###  [Create your feature flags](https://vercel.com/docs/edge-config/edge-config-integrations/split-edge-config#create-your-feature-flags)[](https://vercel.com/docs/edge-config/edge-config-integrations/split-edge-config#create-your-feature-flags)
If you already have existing feature flags, you can skip this step and use those. In this example, we'll create one called `New_Marketing_Page`. You can set the user targeting to Joe and Bobby.
To create a feature flag in Split:
    1. Log into your
    2. In the sidebar, under Target, select Feature flags. Add the name `New_Marketing_Page`, and set the traffic type to `user`. Select Create to finish
    3. With your feature flag created, select the feature flag and open Definition in the sidebar. Select Initiate Environment to configure your flag
    4. Add valid users to the feature flag
    5. Scroll down to Targeting and select Add new individual target
    6. Under To user, add any username you want to test. This example uses `Joe`.
    7. Select Add new individual target, then set the Description option to `off`. Add another username under To user. This example uses `Bobby`
    8. Select Review Changes, then Create to finish
Next, you need to add your credentials to your project's local environment to use the Split integration in your code.
  3. ###  [Get your credentials](https://vercel.com/docs/edge-config/edge-config-integrations/split-edge-config#get-your-credentials)[](https://vercel.com/docs/edge-config/edge-config-integrations/split-edge-config#get-your-credentials)
Next, you'll add the following credentials to your Vercel project:
     * `SPLIT_SDK_CLIENT_API_KEY`
     * `EDGE_CONFIG_SPLIT_ITEM_KEY`
     * `EDGE_CONFIG`
To add environment variables to your project, visit [your Vercel dashboard](https://vercel.com/dashboard) and select the project you want to use the Split integration with. Then select Settings > Environment Variables.
To get your Split client-side API keys:
    1. Log into your
    2. In the list of options that appears, select Admin Settings, then navigate to API Keys -> SDK API Keys
    3. Copy the client-side keys associated with the workspace and environment you're using
To add your Edge Config Split item key, if you didn't copy it after setting up the integration on Vercel:
    1. Visit [your dashboard on Vercel](https://vercel.com/dashboard/integrations)
    2. In the Integrations section in the sidebar, select Manage
    3. On the integration page, select Configure
    4. You should see the item key on the page that opens. Copy it
To add your Edge Config's connection string to your project:
    1. Visit your project's page in [the dashboard](https://vercel.com/dashboard)
    2. Open Storage in the sidebar. Select Connect Store and select the Edge Config associated with your Split integration. The `EDGE_CONFIG` environment variable will be set automatically.
Now you're ready to use the Split Edge Config integration in your code.
  4. ###  [Use the Split integration in your code](https://vercel.com/docs/edge-config/edge-config-integrations/split-edge-config#use-the-split-integration-in-your-code)[](https://vercel.com/docs/edge-config/edge-config-integrations/split-edge-config#use-the-split-integration-in-your-code)
Open your project's code on your local machine and do the following:
    1. Install Split's Browser SDK, Vercel integration utilities, and Vercel's Edge Config SDK:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i @splitsoftware/splitio-browserjs @splitsoftware/vercel-integration-utils @vercel/edge-config
```

```
yarn add @splitsoftware/splitio-browserjs @splitsoftware/vercel-integration-utils @vercel/edge-config
```

```
npm i @splitsoftware/splitio-browserjs @splitsoftware/vercel-integration-utils @vercel/edge-config
```

```
bun add @splitsoftware/splitio-browserjs @splitsoftware/vercel-integration-utils @vercel/edge-config
```

    1. Create an API route in your project. The following example fetches a treatment based on which user is visiting. You can specify the user by appending `?userKey=Joe` or `?userKey=Bobby` to the URL when visiting the route:
Next.js (/app)Next.js (/pages)Other frameworks
app/api/marketing-example/route.ts
TypeScript
TypeScript JavaScript Bash
```
import {
  SplitFactory,
  PluggableStorage,
  ErrorLogger,
} from '@splitsoftware/splitio-browserjs';
import { EdgeConfigWrapper } from '@splitsoftware/vercel-integration-utils';
import { createClient } from '@vercel/edge-config';

export async function GET(request: Request) {
  const { EDGE_CONFIG_SPLIT_ITEM_KEY, SPLIT_SDK_CLIENT_API_KEY } = process.env;

  if (!SPLIT_SDK_CLIENT_API_KEY || !EDGE_CONFIG_SPLIT_ITEM_KEY)
    return new Response(
      `Failed to find your SDK Key (${SPLIT_SDK_CLIENT_API_KEY})
      or item key ${EDGE_CONFIG_SPLIT_ITEM_KEY}`,
    );

  const edgeConfigClient = createClient(process.env.EDGE_CONFIG);
  const { searchParams } = new URL(request.url);
  const userKey = searchParams.get('userKey') || 'anonymous';
  const client = SplitFactory({
    core: {
      authorizationKey: SPLIT_SDK_CLIENT_API_KEY,
      key: userKey,
    },
    mode: 'consumer_partial',
    storage: PluggableStorage({
      wrapper: EdgeConfigWrapper({
        // The Edge Config item key where Split stores
        // feature flag definitions
        edgeConfigItemKey: EDGE_CONFIG_SPLIT_ITEM_KEY,
        // The Edge Config client
        edgeConfig: edgeConfigClient,
      }),
    }),
    // Disable or keep only ERROR log level in production,
    // to minimize performance impact
    debug: ErrorLogger(),
  }).client();

  await new Promise((resolve) => {
    client.on(client.Event.SDK_READY, () => resolve);
    client.on(client.Event.SDK_READY_TIMED_OUT, () => resolve);
  });

  // Replace this with the feature flag you want
  const FEATURE_FLAG = 'New_Marketing_Page';
  const treatment = await client.getTreatment(FEATURE_FLAG);

  // Must await in app-router; waitUntil() is not
  // yet supported
  await client.destroy();

  // treatment will be 'control' if the SDK timed out
  if (treatment == 'control') return new Response('Control marketing page');

  return treatment === 'on'
    ? new Response('New marketing page')
    : new Response('Old marketing page');
}
```

  5. ###  [Test your code](https://vercel.com/docs/edge-config/edge-config-integrations/split-edge-config#test-your-code)[](https://vercel.com/docs/edge-config/edge-config-integrations/split-edge-config#test-your-code)
    1. Start a local development server. If you're using Vercel CLI, enter the following command in the terminal:
terminal
```
vercel dev
```

    1. Navigate to `New marketing page` or `Old marketing page` based on how your feature flags are configured in Split
       * Try changing the `userKey` search param's value to `Bobby`, or deleting it altogether, to see different responses when you visit the route
