##  [Get Started](https://vercel.com/docs/edge-config/edge-config-integrations/hypertune-edge-config#get-started)[](https://vercel.com/docs/edge-config/edge-config-integrations/hypertune-edge-config#get-started)
If you deploy a template like the [Hypertune Flags SDK Example](https://vercel.com/templates/next.js/flags-sdk-hypertune-nextjs), it will guide you through most of these steps.
Navigate to your Project and click the Flags tab.
Install a flag provider, select Hypertune and click continue, then toggle Enable Edge Config Syncing on.
  1. ###  [Set up your local environment](https://vercel.com/docs/edge-config/edge-config-integrations/hypertune-edge-config#set-up-your-local-environment)[](https://vercel.com/docs/edge-config/edge-config-integrations/hypertune-edge-config#set-up-your-local-environment)
Open your project in your development environment and link it to Vercel.
```
vercel link
```

Once linked, you can pull the environment variables that were added to your project.
```
vercel env pull
```

You should have a `.env.local` file with the following environment variables:
```
EXPERIMENTATION_CONFIG="..."
EXPERIMENTATION_CONFIG_ITEM_KEY="..."
NEXT_PUBLIC_HYPERTUNE_TOKEN="..."
```

If you don't see these environment variables, ensure your project is linked to the Hypertune integration in the Flags tab.
  2. ###  [Manage your flags in Hypertune](https://vercel.com/docs/edge-config/edge-config-integrations/hypertune-edge-config#manage-your-flags-in-hypertune)[](https://vercel.com/docs/edge-config/edge-config-integrations/hypertune-edge-config#manage-your-flags-in-hypertune)
From the Flags tab, click Open in Hypertune to make changes in your Hypertune project.
When you click save, changes will be synchronized to your Edge Config and ready for use.
  3. ###  [Generate a type-safe client](https://vercel.com/docs/edge-config/edge-config-integrations/hypertune-edge-config#generate-a-type-safe-client)[](https://vercel.com/docs/edge-config/edge-config-integrations/hypertune-edge-config#generate-a-type-safe-client)
Run code generation to produce the type-safe client for use with the Hypertune SDK.
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm dlx hypertune
```

```
yarn dlx hypertune
```

```
npx hypertune
```

```
bunx hypertune
```

You should now have a `generated` directory with generated code reflecting your saved changes.
  4. ###  [Declare flags in your code](https://vercel.com/docs/edge-config/edge-config-integrations/hypertune-edge-config#declare-flags-in-your-code)[](https://vercel.com/docs/edge-config/edge-config-integrations/hypertune-edge-config#declare-flags-in-your-code)
You can declare server side flags using the Flags SDK with Hypertune as follows:
flags.ts
TypeScript
TypeScript JavaScript Bash
```
import {
  createSource,
  vercelFlagDefinitions as flagDefinitions,
  flagFallbacks,
  type FlagValues,
  type Context,
} from '@/generated/hypertune';
import { flag } from 'flags/next';
import { createHypertuneAdapter } from '@flags-sdk/hypertune';
import { identify } from './lib/identify';

// Generate a Flags SDK adapter from generated Hypertune code
const hypertuneAdapter = createHypertuneAdapter<FlagValues, Context>({
  createSource,
  flagDefinitions,
  flagFallbacks,
  identify,
});

// Use generated definitions to declare flags in your framework
export const exampleFlag = flag(hypertuneAdapter.declarations.exampleFlag);
```

See the [more resources](https://vercel.com/docs/edge-config/edge-config-integrations/hypertune-edge-config#more-resources) section for more information about the Hypertune and Flags SDK.
  5. ###  [Use flags in your app](https://vercel.com/docs/edge-config/edge-config-integrations/hypertune-edge-config#use-flags-in-your-app)[](https://vercel.com/docs/edge-config/edge-config-integrations/hypertune-edge-config#use-flags-in-your-app)
app/page.tsx
TypeScript
TypeScript JavaScript Bash
```
import { exampleFlag } from '@/flags';

export default async function Home() {
  const isExampleFlagEnabled = await exampleFlag();
  return <div>Example Flag is {isExampleFlagEnabled ? 'enabled' : 'disabled'}</div>;
}
```
