##  [Prerequisites](https://vercel.com/docs/edge-config/edge-config-integrations/devcycle-edge-config#prerequisites)[](https://vercel.com/docs/edge-config/edge-config-integrations/devcycle-edge-config#prerequisites)
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

  2. A project. If you don't have one, you can run the following terminal commands to create a Next.js project:


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



  1. ###  [Set up the DevCycle integration](https://vercel.com/docs/edge-config/edge-config-integrations/devcycle-edge-config#set-up-the-devcycle-integration)[](https://vercel.com/docs/edge-config/edge-config-integrations/devcycle-edge-config#set-up-the-devcycle-integration)
Visit [the DevCycle page in the Integration Marketplace](https://vercel.com/marketplace/devcycle) and select the Add Integration button. From the modal that opens:
    1. Select your Vercel team and project.
    2. Continue and log into DevCycle.
    3. Select the DevCycle Organization and Project you want to use with Vercel Edge Config.
    4. Connect your DevCycle project to an existing or new Edge Config store.
    5. Click Finish Setup.
  2. ###  [Install the DevCycle Edge Config package](https://vercel.com/docs/edge-config/edge-config-integrations/devcycle-edge-config#install-the-devcycle-edge-config-package)[](https://vercel.com/docs/edge-config/edge-config-integrations/devcycle-edge-config#install-the-devcycle-edge-config-package)
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i @devcycle/vercel-edge-config @vercel/edge-config
```

```
yarn add @devcycle/vercel-edge-config @vercel/edge-config
```

```
npm i @devcycle/vercel-edge-config @vercel/edge-config
```

```
bun add @devcycle/vercel-edge-config @vercel/edge-config
```

  3. ###  [Use the DevCycle integration in your code](https://vercel.com/docs/edge-config/edge-config-integrations/devcycle-edge-config#use-the-devcycle-integration-in-your-code)[](https://vercel.com/docs/edge-config/edge-config-integrations/devcycle-edge-config#use-the-devcycle-integration-in-your-code)
For more information on DevCycle Next.js SDK usage, see the
Next.js (/app)Next.js (/pages)Node.js
app/index.tsx
TypeScript
TypeScript JavaScript Bash
```
import { createClient } from '@vercel/edge-config';
import { EdgeConfigSource } from '@devcycle/vercel-edge-config';
import { setupDevCycle } from '@devcycle/nextjs-sdk/server';

const edgeClient = createClient(process.env.EDGE_CONFIG ?? '');
const edgeConfigSource = new EdgeConfigSource(edgeClient);

export const { getVariableValue, getClientContext } = setupDevCycle({
  serverSDKKey: process.env.DEVCYCLE_SERVER_SDK_KEY ?? '',
  clientSDKKey: process.env.NEXT_PUBLIC_DEVCYCLE_CLIENT_SDK_KEY ?? '',
  userGetter: () => ({ user_id: 'test_user' }),
  options: {
    // pass the configSource option with the instance of EdgeConfigSource
    configSource: edgeConfigSource,
  },
});
```
