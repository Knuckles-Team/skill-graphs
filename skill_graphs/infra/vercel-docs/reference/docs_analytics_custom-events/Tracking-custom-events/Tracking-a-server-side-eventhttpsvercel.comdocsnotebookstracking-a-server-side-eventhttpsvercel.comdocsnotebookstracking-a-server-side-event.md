##  [Tracking a server-side event](https://vercel.com/docs/notebooks#tracking-a-server-side-event)[](https://vercel.com/docs/notebooks#tracking-a-server-side-event)
In scenarios such as when a user signs up or makes a purchase, it's more useful to track an event on the server-side. For this, you can use the `track` function on API routes or server actions.
To set up server-side events:
  1. Make sure you have `@vercel/analytics` version 1.1.0 or later [installed](https://vercel.com/docs/analytics/quickstart#add-@vercel/analytics-to-your-project).
  2. Import `{ track }` from `@vercel/analytics/server`.
  3. Use the `track` function in your API routes or server actions.
  4. Pass in a string representing the event name as the first argument to the `track` function. You can also pass [custom data](https://vercel.com/docs/notebooks#tracking-an-event-with-custom-data) as the second argument.


For example, if you want to track a purchase event:
app/actions.ts
TypeScript
TypeScript JavaScript Bash
```
'use server';
import { track } from '@vercel/analytics/server';

export async function purchase() {
  await track('Item purchased', {
    quantity: 1,
  });
}
```
