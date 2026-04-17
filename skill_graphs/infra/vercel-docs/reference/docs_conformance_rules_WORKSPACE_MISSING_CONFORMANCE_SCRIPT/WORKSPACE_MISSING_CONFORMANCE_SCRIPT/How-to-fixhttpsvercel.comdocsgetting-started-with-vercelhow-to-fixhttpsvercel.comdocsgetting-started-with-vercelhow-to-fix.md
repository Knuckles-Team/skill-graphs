##  [How to fix](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)[](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)
Install the `@vercel-private/conformance` package in this workspace and define a `conformance` script in the `package.json` file.
package.json
```
{
  "name": "test-workspace",
  "scripts": {
    "build": "tsc -b",
    "conformance": "vercel conformance"
  },
  "devDependencies": {
    "@vercel-private/conformance": "^1.0.0"
  }
}
```

* * *
[ Previous Vercel Documentation ](https://vercel.com/docs)[ Next Projects and Deployments ](https://vercel.com/docs/getting-started-with-vercel/projects-deployments)
Was this helpful?
Send
On this page
  * [Example](https://vercel.com/docs/getting-started-with-vercel#example)
  * [How to fix](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)


Copy as MarkdownGive feedbackAsk AI about this page
