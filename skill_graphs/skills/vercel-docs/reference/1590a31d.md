##  [Declaring options](https://vercel.com/docs/flags/vercel-flags/sdks/flags-sdk#declaring-options)[](https://vercel.com/docs/flags/vercel-flags/sdks/flags-sdk#declaring-options)
You can declare the possible values a flag can evaluate to using the `options` array. This works for booleans, strings, numbers, or any other type:
flags.ts
```
import { flag } from 'flags/next';
import { vercelAdapter } from '@flags-sdk/vercel';

export const pricingTier = flag({
  key: 'pricing-tier',
  adapter: vercelAdapter(),
  options: [
    { value: 'standard', label: 'Standard' },
    { value: 'premium', label: 'Premium' },
    { value: 'enterprise', label: 'Enterprise' },
  ],
  description: 'Which pricing tier to show',
});
```

Declaring options serves these purposes:
  * [Flags Explorer](https://vercel.com/docs/flags/flags-explorer/reference#definitions) displays them as a dropdown, so you can override the flag to any declared value during development.
  * When Vercel detects the flag as a [draft](https://vercel.com/docs/flags/vercel-flags/dashboard/drafts#how-to-promote-a-draft), the options pre-fill the flag configuration when you promote it to a fully managed Vercel Flag.
  * When you use the Flags SDK's precompute function the declared options are serialized more efficiently.
