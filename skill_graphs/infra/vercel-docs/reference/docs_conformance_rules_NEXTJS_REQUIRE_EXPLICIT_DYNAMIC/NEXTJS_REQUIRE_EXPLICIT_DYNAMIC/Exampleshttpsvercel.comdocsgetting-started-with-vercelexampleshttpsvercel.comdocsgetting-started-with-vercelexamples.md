##  [Examples](https://vercel.com/docs/getting-started-with-vercel#examples)[](https://vercel.com/docs/getting-started-with-vercel#examples)
This rule will catch any pages or routes that:
  * Do not have the `dynamic` option set to a valid value.
  * Have the `dynamic` option set to `'auto'` (which is the default value).


In the following example, the page component does not have the `dynamic` route segment option set.
app/page.tsx
```
export default function Page() {
  // ...
}
```

The next example sets the `dynamic` route segment option, however it sets it to `'auto'`, which is already the default behavior and will not satisfy this rule.
app/dashboard/page.tsx
```
export const dynamic = 'auto';

export default function Page() {
  // ...
}
```
