##  [Node.js dependencies](https://vercel.com/docs/functions/runtimes/node-js#node.js-dependencies)[](https://vercel.com/docs/functions/runtimes/node-js#node.js-dependencies)
For dependencies listed in a `package.json` file at the root of a project, the following behavior is used:
  * If `bun.lock` or `bun.lockb` is present, `bun install` is executed
  * If `yarn.lock` is present `yarn install` is executed
  * If `pnpm-lock.yaml` is present, `pnpm install` is executed
    * See [supported package managers](https://vercel.com/docs/package-managers#supported-package-managers) for pnpm detection details
  * If `package-lock.json` is present, `npm install` is executed
  * If `vlt-lock.json` is present, `vlt install` is executed
  * Otherwise, `npm install` is executed


If you need to select a specific version of a package manager, see [corepack](https://vercel.com/docs/deployments/configure-a-build#corepack).
