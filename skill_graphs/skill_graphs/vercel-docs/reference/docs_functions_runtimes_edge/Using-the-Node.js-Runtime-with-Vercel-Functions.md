# Using the Node.js Runtime with Vercel Functions
Last updated December 1, 2025
You can create Vercel Function in JavaScript or TypeScript by using the Node.js runtime. By default, the runtime builds and serves any function created within the `/api` directory of a project to Vercel.
[Node.js](https://vercel.com/docs/functions/runtimes/node-js)-powered functions are suited to computationally intense or large functions and provide benefits like:
  * More RAM and CPU power: For computationally intense workloads, or functions that have bundles up to 250 MB in size, this runtime is ideal
  * Complete Node.js compatibility: The Node.js runtime offers access to all Node.js APIs, making it a powerful tool for many applications
