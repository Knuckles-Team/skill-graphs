##  [How to fix](https://vercel.com/docs/conformance/rules/NO_SERIAL_ASYNC_CALLS#how-to-fix)[](https://vercel.com/docs/conformance/rules/NO_SERIAL_ASYNC_CALLS#how-to-fix)
Instead, of executing async logic sequentially, opt to refactor the logic so it can be run parallel.
This can be fixed using `Promise.all`:
```
export async function getStaticProps() {
  const firstThing = await getFirstThing();
  const secondThing = await getSecondThing();

  return {
    props: {
      firstThing,
      secondThing,
    },
  };
}
```

We can extract both `await` expressions into a single `Promise.all`, as follows:
```
export async function getStaticProps() {
  const [firstThing, secondThing] = await Promise.all([
    getFirstThing(),
    getSecondThing(),
  ]);

  return {
    props: {
      firstThing,
      secondThing,
    },
  };
}
```

* * *
Was this helpful?
Send
On this page
  * [How to fix](https://vercel.com/docs/conformance/rules/NO_SERIAL_ASYNC_CALLS#how-to-fix)


Copy as MarkdownGive feedbackAsk AI about this page
