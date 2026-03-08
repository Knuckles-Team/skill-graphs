##  [Passing evaluation context](https://vercel.com/docs/flags/vercel-flags/sdks/flags-sdk#passing-evaluation-context)[](https://vercel.com/docs/flags/vercel-flags/sdks/flags-sdk#passing-evaluation-context)
To evaluate targeting rules based on user attributes, provide an `identify` function on your flags. This function returns the context that Vercel Flags uses to match targeting rules configured in the dashboard.
flags.ts
```
import { flag, dedupe } from 'flags/next';
import { vercelAdapter } from '@flags-sdk/vercel';

type Entities = {
  user?: { id: string; email: string; plan: string };
  team?: { id: string };
};

const identify = dedupe(async (): Promise<Entities> => {
  const session = await getSession(); // getSession would be implemented by your app
  return {
    user: session?.user
      ? {
          id: session.user.id,
          email: session.user.email,
          plan: session.user.plan,
        }
      : undefined,
  };
});

export const premiumFeature = flag<boolean, Entities>({
  key: 'premium-feature',
  adapter: vercelAdapter(),
  identify,
});
```

The `dedupe` wrapper ensures the context is only computed once per request, even if multiple flags call the same `identify` function.
