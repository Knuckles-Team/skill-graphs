##  [Yarn dynamic require of "util" is not supported](https://vercel.com/docs/getting-started-with-vercel#yarn-dynamic-require-of-util-is-not-supported)[](https://vercel.com/docs/getting-started-with-vercel#yarn-dynamic-require-of-util-is-not-supported)
This error occurs when projects use yarn, corepack, and have a `package.json` with a `type` field set to `module`. This is a known
To prevent this error, consider the following options:
  * Remove `"type": "module"` from the project's `package.json`
  * Install yarn into the project instead of using corepack with `yarn set version [desired-version] --yarn-path`
