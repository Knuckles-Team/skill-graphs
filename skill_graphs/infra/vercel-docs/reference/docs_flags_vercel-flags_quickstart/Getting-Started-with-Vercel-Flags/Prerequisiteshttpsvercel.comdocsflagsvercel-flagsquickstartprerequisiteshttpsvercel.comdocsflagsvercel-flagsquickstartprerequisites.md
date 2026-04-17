##  [Prerequisites](https://vercel.com/docs/flags/vercel-flags/quickstart#prerequisites)[](https://vercel.com/docs/flags/vercel-flags/quickstart#prerequisites)
  * A [Next.js](https://vercel.com/docs/frameworks/nextjs) project connected to Vercel.
  * [Vercel CLI](https://vercel.com/docs/cli) installed.


  1. ###  [Create a flag in the dashboard](https://vercel.com/docs/flags/vercel-flags/quickstart#create-a-flag-in-the-dashboard)[](https://vercel.com/docs/flags/vercel-flags/quickstart#create-a-flag-in-the-dashboard)
    1. Go to your [Vercel Dashboard](https://vercel.com/dashboard).
    2. Open Flags in the sidebar for your project.
    3. Create a new flag named `marketing-banner`.
    4. Leave the Type set to Boolean and configure the environment settings to be on for Development and off for Preview and Production.
  2. ###  [Pull environment variables](https://vercel.com/docs/flags/vercel-flags/quickstart#pull-environment-variables)[](https://vercel.com/docs/flags/vercel-flags/quickstart#pull-environment-variables)
When you create your first flag, Vercel provisions [SDK Keys](https://vercel.com/docs/flags/vercel-flags/dashboard/sdk-keys) for each environment and stores them in a `FLAGS` environment variable on your project. Pull them into your local `.env.local` file:
terminal
```
vercel env pull
```

If your project isn't linked yet, run `vercel link` first.
  3. ###  [Install the required packages](https://vercel.com/docs/flags/vercel-flags/quickstart#install-the-required-packages)[](https://vercel.com/docs/flags/vercel-flags/quickstart#install-the-required-packages)
Flags SDKOpenFeatureCore
The [Flags SDK](https://vercel.com/docs/flags/vercel-flags/sdks/flags-sdk) is a framework-native way to define and evaluate feature flags. It works with any flag provider through adapters. The `@flags-sdk/vercel` adapter connects it to your Vercel Flags project, and `@vercel/flags-core` is the evaluation engine used behind the scenes.
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i flags @flags-sdk/vercel
```

```
yarn add flags @flags-sdk/vercel
```

```
npm i flags @flags-sdk/vercel
```

```
bun add flags @flags-sdk/vercel
```

If you use an AI coding assistant, you can also install the [Flags SDK agent skill](https://vercel.com/docs/agent-resources/skills) to help define, evaluate, and clean up feature flags:
terminal
```
npx skills add vercel/flags --skill flags-sdk
```

`@vercel/flags-core` package includes the Vercel Flags evaluation engine and the OpenFeature provider.
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i @openfeature/server-sdk @vercel/flags-core
```

```
yarn add @openfeature/server-sdk @vercel/flags-core
```

```
npm i @openfeature/server-sdk @vercel/flags-core
```

```
bun add @openfeature/server-sdk @vercel/flags-core
```

The [@vercel/flags-core](https://vercel.com/docs/flags/vercel-flags/sdks/core) library gives you direct access to the Vercel Flags evaluation engine. Use it when you need full control or are working outside of supported frameworks.
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i @vercel/flags-core
```

```
yarn add @vercel/flags-core
```

```
npm i @vercel/flags-core
```

```
bun add @vercel/flags-core
```

  4. ###  [Evaluate the flag in your application](https://vercel.com/docs/flags/vercel-flags/quickstart#evaluate-the-flag-in-your-application)[](https://vercel.com/docs/flags/vercel-flags/quickstart#evaluate-the-flag-in-your-application)
Flags SDKOpenFeatureCore
Define the flag in a `flags.ts` file. The `vercelAdapter` reads the `FLAGS` environment variable automatically:
flags.ts
```
import { flag } from 'flags/next';
import { vercelAdapter } from '@flags-sdk/vercel';

export const marketingBanner = flag({
  key: 'marketing-banner',
  adapter: vercelAdapter(),
});
```

Then call the flag in a server component:
app/page.tsx
```
import { marketingBanner } from '../flags';

export default async function Page() {
  const showBanner = await marketingBanner();

  return <div>{showBanner ? 'Sale live now!' : 'Welcome'}</div>;
}
```

See the [Flags SDK guide](https://vercel.com/docs/flags/vercel-flags/sdks/flags-sdk) for full setup instructions.
Create a helper that initializes the Vercel provider once and returns a reusable client:
lib/openfeature.ts
```
import { OpenFeature } from '@openfeature/server-sdk';
import { flagsClient } from '@vercel/flags-core';
import { VercelProvider } from '@vercel/flags-core/openfeature';

let initPromise: Promise<void> | null = null;
let initialized = false;
const vercelProvider = new VercelProvider(flagsClient);

async function initialize() {
  try {
    await OpenFeature.setProviderAndWait(vercelProvider);
    initialized = true;
  } catch (error) {
    console.error('Failed to initialize provider:', error);
    initPromise = null;
  }
}

export async function getOpenFeatureClient() {
  if (initialized) return OpenFeature.getClient();
  if (!initPromise) initPromise = initialize();
  await initPromise;
  return OpenFeature.getClient();
}
```

Then use it in a server component:
app/page.tsx
```
import { getOpenFeatureClient } from '../lib/openfeature';

export default async function Page() {
  const client = await getOpenFeatureClient();
  const showBanner = await client.getBooleanValue(
    'marketing-banner',
    false,
  );

  return <div>{showBanner ? 'Sale live now!' : 'Welcome'}</div>;
}
```

See the [OpenFeature guide](https://vercel.com/docs/flags/vercel-flags/sdks/openfeature) for full setup instructions.
Use the `flagsClient` to evaluate the flag directly:
app/page.tsx
```
import { flagsClient } from '@vercel/flags-core';

export default async function Page() {
  const result = await flagsClient.evaluate<boolean>(
    'marketing-banner',
    false,
  );

  return <div>{result.value ? 'Sale live now!' : 'Welcome'}</div>;
}
```

See the [Core Library guide](https://vercel.com/docs/flags/vercel-flags/sdks/core) for full setup instructions.
Toggle the flag off for the Development environment in the Vercel Dashboard, then press Review and save and leave a message for the change. Reload the page to see the change.
