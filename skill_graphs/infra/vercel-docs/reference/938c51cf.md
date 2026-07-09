##  [Creating a Node.js function](https://vercel.com/docs/functions/runtimes/node-js#creating-a-node.js-function)[](https://vercel.com/docs/functions/runtimes/node-js#creating-a-node.js-function)
In order to use the Node.js runtime, create a file inside the `api` directory with a function using the [`fetch` Web Standard export](https://vercel.com/docs/functions/functions-api-reference?framework=other&language=ts#fetch-web-standard). No additional configuration is needed:
api/hello.ts
```
export default {
  fetch(request: Request) {
    return new Response('Hello from Vercel!');
  },
};
```

Alternatively, you can export each HTTP method as a separate export instead of using the `fetch` Web Standard export:
api/hello.ts
```
export function GET(request: Request) {
  return new Response('Hello from Vercel!');
}
```

To learn more about creating Vercel Functions, see the [Functions API Reference](https://vercel.com/docs/functions/functions-api-reference). If you need more advanced behavior, such as a custom build step or private npm modules, see the [advanced Node.js usage page](https://vercel.com/docs/functions/runtimes/node-js/advanced-node-configuration).
The entry point for `src` must be a glob matching `.js`, `.mjs`, or `.ts` files** that export a default function.
