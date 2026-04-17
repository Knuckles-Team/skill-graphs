##  [Many Node.js APIs are not available](https://vercel.com/docs/functions/runtimes/node-js#many-node.js-apis-are-not-available)[](https://vercel.com/docs/functions/runtimes/node-js#many-node.js-apis-are-not-available)
Middleware with the `edge` runtime configured is neither a Node.js nor browser application, which means it doesn't have access to all browser and Node.js APIs. Currently, our runtime offers a subset of browser APIs and some Node.js APIs and we plan to implement more functionality in the future.
In summary:
  * Use ES modules
  * Most libraries that use Node.js APIs as dependencies can't be used in Middleware with the `edge` runtime configured.
  * Dynamic code execution (such as `eval`) is not allowed (see the next section for more details)
