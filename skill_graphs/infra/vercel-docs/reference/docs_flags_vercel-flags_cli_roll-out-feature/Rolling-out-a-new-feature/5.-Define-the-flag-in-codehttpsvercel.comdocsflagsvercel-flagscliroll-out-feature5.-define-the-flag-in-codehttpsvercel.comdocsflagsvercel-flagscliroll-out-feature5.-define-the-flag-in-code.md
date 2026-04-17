##  [5. Define the flag in code](https://vercel.com/docs/flags/vercel-flags/cli/roll-out-feature#5.-define-the-flag-in-code)[](https://vercel.com/docs/flags/vercel-flags/cli/roll-out-feature#5.-define-the-flag-in-code)
Create a flag definition using the Flags SDK. The `vercelAdapter` reads the `FLAGS` environment variable automatically:
flags.ts
```
import { flag } from 'flags/next';
import { vercelAdapter } from '@flags-sdk/vercel';

export const redesignedCheckout = flag({
  key: 'redesigned-checkout',
  adapter: vercelAdapter(),
});
```

The flag returns `false` until you enable it in the dashboard.
