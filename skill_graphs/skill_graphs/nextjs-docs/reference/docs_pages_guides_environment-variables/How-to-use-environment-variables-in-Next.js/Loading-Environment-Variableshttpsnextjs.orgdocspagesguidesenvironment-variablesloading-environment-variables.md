## Loading Environment Variables[](https://nextjs.org/docs/pages/guides/environment-variables#loading-environment-variables)
Next.js has built-in support for loading environment variables from `.env*` files into `process.env`.
.env
```
DB_HOST=localhost
DB_USER=myuser
DB_PASS=mypassword
```

This loads `process.env.DB_HOST`, `process.env.DB_USER`, and `process.env.DB_PASS` into the Node.js environment automatically allowing you to use them in [Next.js data fetching methods](https://nextjs.org/docs/pages/building-your-application/data-fetching) and [API routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes).
For example, using [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props):
pages/index.js
```
export async function getStaticProps() {
  const db = await myDB.connect({
    host: process.env.DB_HOST,
    username: process.env.DB_USER,
    password: process.env.DB_PASS,
  })
  // ...
}
```

### Loading Environment Variables with `@next/env`[](https://nextjs.org/docs/pages/guides/environment-variables#loading-environment-variables-with-nextenv)
If you need to load environment variables outside of the Next.js runtime, such as in a root config file for an ORM or test runner, you can use the `@next/env` package.
This package is used internally by Next.js to load environment variables from `.env*` files.
To use it, install the package and use the `loadEnvConfig` function to load the environment variables:
pnpmnpmyarnbun
Terminal
```
pnpm add @next/env
```

envConfig.ts
TypeScript
JavaScript TypeScript
```
import { loadEnvConfig } from '@next/env'

const projectDir = process.cwd()
loadEnvConfig(projectDir)
```

Then, you can import the configuration where needed. For example:
orm.config.ts
TypeScript
JavaScript TypeScript
```
import './envConfig.ts'

export default defineConfig({
  dbCredentials: {
    connectionString: process.env.DATABASE_URL!,
  },
})
```

### Referencing Other Variables[](https://nextjs.org/docs/pages/guides/environment-variables#referencing-other-variables)
Next.js will automatically expand variables that use `$` to reference other variables e.g. `$VARIABLE` inside of your `.env*` files. This allows you to reference other secrets. For example:
.env
```
TWITTER_USER=nextjs
TWITTER_URL=https://x.com/$TWITTER_USER
```

In the above example, `process.env.TWITTER_URL` would be set to `https://x.com/nextjs`.
> **Good to know** : If you need to use variable with a `$` in the actual value, it needs to be escaped e.g. `\$`.
