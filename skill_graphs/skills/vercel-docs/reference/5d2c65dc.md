##  [Tracking a client-side event](https://vercel.com/docs/notebooks#tracking-a-client-side-event)[](https://vercel.com/docs/notebooks#tracking-a-client-side-event)
To track an event:
  1. Make sure you have `@vercel/analytics` version 1.1.0 or later [installed](https://vercel.com/docs/analytics/quickstart#add-@vercel/analytics-to-your-project).
  2. Import `{ track }` from `@vercel/analytics`.
  3. In most cases you will want to track an event when a user performs an action, such as clicking a button or submitting a form, so you should use this on the button handler.
  4. Call `track` and pass in a string representing the event name as the first argument. You can also pass [custom data](https://vercel.com/docs/notebooks#tracking-an-event-with-custom-data) as the second argument:
component.ts
```
import { track } from '@vercel/analytics';

// Call this function when a user clicks a button or performs an action you want to track
track('Signup');
```



This will track an event named **Signup**.
For example, if you have a button that says Sign Up, you can track an event when the user clicks the button:
components/button.tsx
TypeScript
TypeScript JavaScript Bash
```
import { track } from '@vercel/analytics';

function SignupButton() {
  return (
    <button
      onClick={() => {
        track('Signup');
        // ... other logic
      }}
    >
      Sign Up
    </button>
  );
}
```
