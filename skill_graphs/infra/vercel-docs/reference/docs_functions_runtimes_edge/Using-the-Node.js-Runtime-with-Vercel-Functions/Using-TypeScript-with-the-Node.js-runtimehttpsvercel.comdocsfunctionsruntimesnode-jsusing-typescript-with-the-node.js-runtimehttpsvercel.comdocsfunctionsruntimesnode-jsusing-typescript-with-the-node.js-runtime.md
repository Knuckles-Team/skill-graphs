##  [Using TypeScript with the Node.js runtime](https://vercel.com/docs/functions/runtimes/node-js#using-typescript-with-the-node.js-runtime)[](https://vercel.com/docs/functions/runtimes/node-js#using-typescript-with-the-node.js-runtime)
The Node.js runtime supports files ending with `.ts` inside of the `/api` directory as TypeScript files to compile and serve when deploying.
An example TypeScript file that exports a Web signature handler is as follows:
api/hello.ts
```
export default {
  async fetch(request: Request) {
    const url = new URL(request.url);
    const name = url.searchParams.get('name') || 'World';

    return Response.json({ message: `Hello ${name}!` });
  },
};
```

You can use a `tsconfig.json` file at the root of your project to configure the TypeScript compiler. Most options are supported aside from
