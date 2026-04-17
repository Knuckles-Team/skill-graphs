##  [Client-side tracking](https://vercel.com/docs/flags/observability/web-analytics#client-side-tracking)[](https://vercel.com/docs/flags/observability/web-analytics#client-side-tracking)
Vercel Web Analytics can look up the values of evaluated feature flags in the DOM. It can then enrich page views and client-side events with these feature flags.
  1. ###  [Emit feature flags and connect them to Vercel Web Analytics](https://vercel.com/docs/flags/observability/web-analytics#emit-feature-flags-and-connect-them-to-vercel-web-analytics)[](https://vercel.com/docs/flags/observability/web-analytics#emit-feature-flags-and-connect-them-to-vercel-web-analytics)
To share your feature flags with Web Analytics you have to emit your feature flag values to the DOM as described in [Supporting Feature Flags](https://vercel.com/docs/flags/flags-explorer/reference#values).
This will automatically annotate all page views and client-side events with your feature flags.
  2. ###  [Tracking feature flags in client-side events](https://vercel.com/docs/flags/observability/web-analytics#tracking-feature-flags-in-client-side-events)[](https://vercel.com/docs/flags/observability/web-analytics#tracking-feature-flags-in-client-side-events)
Client-side events in Web Analytics will now automatically respect your flags and attach those to custom events.
To manually overwrite the tracked flags for a specific `track` event, call:
component.ts
```
import { track } from '@vercel/analytics';

track('My Event', {}, { flags: ['summer-sale'] });
```

If the flag values on the client are encrypted, the entire encrypted string becomes part of the event payload. This can lead to the event getting reported without any flags when the encrypted string exceeds size limits.
