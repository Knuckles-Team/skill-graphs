# Integrate flags with Runtime Logs
Last updated September 24, 2025
Runtime Logs integration is available in [Beta](https://vercel.com/docs/release-phases#beta) on [all plans](https://vercel.com/docs/plans)
On your dashboard, the [Logs](https://vercel.com/docs/runtime-logs) section in the sidebar displays your [runtime logs](https://vercel.com/docs/runtime-logs#what-are-runtime-logs). It can also display any feature flags your application evaluated while handling requests.
![Feature Flags section in runtime logs](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fworkflow-collaboration%2Ffeature-flags%2Flogs-light.png&w=1080&q=75)![Feature Flags section in runtime logs](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fworkflow-collaboration%2Ffeature-flags%2Flogs-dark.png&w=1080&q=75)Feature Flags section in runtime logs
To make the runtime logs aware of your feature flag call `reportValue(name, value)` with the flag name and value to be reported. Each call to `reportValue` will show up as a distinct entry, even when the same key is used:
app/api/test/route.ts
TypeScript
TypeScript JavaScript Bash
```
import { reportValue } from 'flags';

export async function GET() {
  reportValue('summer-sale', false);
  return Response.json({ ok: true });
}
```

If you are using an implementation of the [Flags SDK](https://vercel.com/docs/flags/flags-sdk-reference) you don't need to call `reportValue`. The respective implementation will automatically call `reportValue` for you.
