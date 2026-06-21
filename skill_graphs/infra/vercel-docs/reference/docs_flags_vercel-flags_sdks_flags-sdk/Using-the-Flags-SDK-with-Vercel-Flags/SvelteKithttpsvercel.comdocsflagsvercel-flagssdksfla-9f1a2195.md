##  [SvelteKit](https://vercel.com/docs/flags/vercel-flags/sdks/flags-sdk#sveltekit)[](https://vercel.com/docs/flags/vercel-flags/sdks/flags-sdk#sveltekit)
For SvelteKit applications, use `flags/sveltekit` instead of `flags/next`:
src/lib/flags.ts
```
import { flag } from 'flags/sveltekit';
import { vercelAdapter } from '@flags-sdk/vercel';

export const showNewFeature = flag({
  key: 'show-new-feature',
  adapter: vercelAdapter(),
});
```

See the
