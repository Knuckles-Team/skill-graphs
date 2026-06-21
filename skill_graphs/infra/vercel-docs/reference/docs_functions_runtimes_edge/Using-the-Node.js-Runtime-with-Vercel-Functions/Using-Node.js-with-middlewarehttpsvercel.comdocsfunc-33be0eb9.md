##  [Using Node.js with middleware](https://vercel.com/docs/functions/runtimes/node-js#using-node.js-with-middleware)[](https://vercel.com/docs/functions/runtimes/node-js#using-node.js-with-middleware)
The Node.js runtime can be used as an experimental feature to run middleware. To enable, add the flag to your `next.config.ts` file:
next.config.ts
```
import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
  experimental: {
    nodeMiddleware: true,
  },
};

export default nextConfig;
```

```
const nextConfig = {
  experimental: {
    nodeMiddleware: true,
  },
};

export default nextConfig;
```

Then in your middleware file, set the runtime to `nodejs` in the `config` object:
middleware.ts
```
export const config = {
  matcher: '/about/:path*',
  runtime: 'nodejs',
};
```

```
export const config = {
  matcher: '/about/:path*',
  runtime: 'nodejs',
};
```

Running middleware on the Node.js runtime incurs charges under [Vercel Functions pricing](https://vercel.com/docs/functions/usage-and-pricing#pricing). These functions only run using [Fluid compute](https://vercel.com/docs/fluid-compute#fluid-compute).
* * *
[ Previous Runtimes ](https://vercel.com/docs/functions/runtimes)[ Next Advanced Node.js Usage ](https://vercel.com/docs/functions/runtimes/node-js/advanced-node-configuration)
Was this helpful?
Send
On this page
  * [Creating a Node.js function](https://vercel.com/docs/functions/runtimes/node-js#creating-a-node.js-function)
  * [Supported APIs](https://vercel.com/docs/functions/runtimes/node-js#supported-apis)
  * [Node.js version](https://vercel.com/docs/functions/runtimes/node-js#node.js-version)
  * [Node.js dependencies](https://vercel.com/docs/functions/runtimes/node-js#node.js-dependencies)
  * [Using TypeScript with the Node.js runtime](https://vercel.com/docs/functions/runtimes/node-js#using-typescript-with-the-node.js-runtime)
  * [Node.js request and response objects](https://vercel.com/docs/functions/runtimes/node-js#node.js-request-and-response-objects)
  * [Node.js helpers](https://vercel.com/docs/functions/runtimes/node-js#node.js-helpers)
  * [Request body](https://vercel.com/docs/functions/runtimes/node-js#request-body)
  * [Cancelled Requests](https://vercel.com/docs/functions/runtimes/node-js#cancelled-requests)
  * [Using Express with Vercel](https://vercel.com/docs/functions/runtimes/node-js#using-express-with-vercel)
  * [Using Node.js with middleware](https://vercel.com/docs/functions/runtimes/node-js#using-node.js-with-middleware)


Copy as MarkdownGive feedbackAsk AI about this page
[Functions](https://vercel.com/docs/functions)
[Runtimes](https://vercel.com/docs/functions/runtimes)
Node.js
