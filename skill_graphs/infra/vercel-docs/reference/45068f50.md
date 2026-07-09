##  [How to fix](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)[](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)
You can fix this error by wrapping your async component with a `<Suspense/>` boundary that has a fallback UI to indicate to Next.js that it should use the fallback until the promise resolves.
Alternatively, you can manually force the dynamic behavior of the page by exporting a `dynamic` value. This rule will only error if `dynamic` is not specified or is set to `auto`. Read more
app/page.tsx
```
export const dynamic = 'force-static';

export default async function Page() {
  const data = await fetch();
  return <div>{data}</div>;
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
