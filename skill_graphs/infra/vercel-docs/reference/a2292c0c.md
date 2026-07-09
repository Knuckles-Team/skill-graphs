##  [How to fix](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)[](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)
If you see this issue in your codebase, you can resolve it by explicitly setting the `dynamic` route segment option for the page or route.
In this example, the `dynamic` route segment option is set to `error`, which forces the page to static, and will throw an error if any components use
app/page.tsx
```
export const dynamic = 'error';

export default function Page() {
  const text = 'Hello world';
  return <div>{text}</div>;
}
```

* * *
[ Previous Vercel Documentation ](https://vercel.com/docs)[ Next Projects and Deployments ](https://vercel.com/docs/getting-started-with-vercel/projects-deployments)
Was this helpful?
Send
On this page
  * [Examples](https://vercel.com/docs/getting-started-with-vercel#examples)
  * [How to fix](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)


Copy as MarkdownGive feedbackAsk AI about this page
