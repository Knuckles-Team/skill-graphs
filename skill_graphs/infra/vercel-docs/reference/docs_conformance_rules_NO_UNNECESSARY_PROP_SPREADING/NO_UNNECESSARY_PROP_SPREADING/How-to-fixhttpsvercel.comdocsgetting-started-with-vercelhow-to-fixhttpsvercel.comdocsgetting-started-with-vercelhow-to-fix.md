##  [How to fix](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)[](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)
You can remove the spread operator from the JSX component, and list all props explicitly.
app/dashboard/page.tsx
```
function HomePage() {
  return (
    <Header bar={foo.bar} baz={foo.baz}>
      Hello World
    </Header>
  );
}

export default HomePage;
```

In the example above,
* * *
[ Previous Vercel Documentation ](https://vercel.com/docs)[ Next Projects and Deployments ](https://vercel.com/docs/getting-started-with-vercel/projects-deployments)
Was this helpful?
Send
On this page
  * [Examples](https://vercel.com/docs/getting-started-with-vercel#examples)
  * [How to fix](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)


Copy as MarkdownGive feedbackAsk AI about this page
