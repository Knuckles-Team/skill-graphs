##  [Flags Explorer integration](https://vercel.com/docs/flags/vercel-flags/sdks/flags-sdk#flags-explorer-integration)[](https://vercel.com/docs/flags/vercel-flags/sdks/flags-sdk#flags-explorer-integration)
The Flags SDK automatically integrates with [Flags Explorer](https://vercel.com/docs/flags/flags-explorer/getting-started), allowing you to view and override flags during development.
To enable this, create a discovery endpoint that exposes your flag definitions:
app/.well-known/vercel/flags/route.ts
```
import { createFlagsDiscoveryEndpoint } from 'flags/next';
import { getProviderData } from '@flags-sdk/vercel';
import * as flags from '../../../../flags';

export const GET = createFlagsDiscoveryEndpoint(async (request) => {
  return getProviderData(flags);
});
```

`getProviderData` reads the metadata from your flag definitions — keys, descriptions, and options — and returns it in the format Flags Explorer expects.
