##  [Server-side tracking](https://vercel.com/docs/flags/observability/web-analytics#server-side-tracking)[](https://vercel.com/docs/flags/observability/web-analytics#server-side-tracking)
To track feature flags in server-side events:
  1. First, report the feature flag value using `reportValue` to make the flag show up in [Runtime Logs](https://vercel.com/docs/runtime-logs):
app/api/test/route.ts
```
import { reportValue } from 'flags';

export async function GET() {
  reportValue('summer-sale', false);
  return Response.json({ ok: true });
}
```

  2. Once reported, any calls to `track` can look up the feature flag while handling a specific request:
app/api/test/route.ts
```
import { track } from '@vercel/analytics/server';
import { reportValue } from 'flags';

export async function GET() {
  reportValue('summer-sale', false);
  track('My Event', {}, { flags: ['summer-sale'] });

  return Response.json({ ok: true });
}
```



If you are using an implementation of the [Flags SDK](https://vercel.com/docs/flags/flags-sdk-reference) you don't need to call `reportValue`. The respective implementation will automatically call `reportValue` for you.
* * *
[ Previous Runtime Logs ](https://vercel.com/docs/flags/observability/runtime-logs)[ Next Integrations/ Overview ](https://vercel.com/docs/integrations)
Was this helpful?
Send
On this page
  * [Client-side tracking](https://vercel.com/docs/flags/observability/web-analytics#client-side-tracking)
  * [Emit feature flags and connect them to Vercel Web Analytics](https://vercel.com/docs/flags/observability/web-analytics#emit-feature-flags-and-connect-them-to-vercel-web-analytics)
  * [Tracking feature flags in client-side events](https://vercel.com/docs/flags/observability/web-analytics#tracking-feature-flags-in-client-side-events)
  * [Server-side tracking](https://vercel.com/docs/flags/observability/web-analytics#server-side-tracking)


Copy as MarkdownGive feedbackAsk AI about this page
