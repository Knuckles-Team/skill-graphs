##  [Pnpm engine unsupported](https://vercel.com/docs/getting-started-with-vercel#pnpm-engine-unsupported)[](https://vercel.com/docs/getting-started-with-vercel#pnpm-engine-unsupported)
`ERR_PNPM_UNSUPPORTED_ENGINE` occurs when `package.json#engines.pnpm` does not match the currently running version of `pnpm`.
To fix, do one of the following:
  * [Set the env var `ENABLE_EXPERIMENTAL_COREPACK` to 1](https://vercel.com/docs/deployments/configure-a-build#corepack), and make sure the `packageManager` value is set correctly in your `package.json`


package.json
```
{
  "engines": {
    "pnpm": "^7.5.1"
  },
  "packageManager": "pnpm@7.5.1"
}
```

  * Remove the `package.json`


You cannot use `engine-strict` only handles dependencies.
