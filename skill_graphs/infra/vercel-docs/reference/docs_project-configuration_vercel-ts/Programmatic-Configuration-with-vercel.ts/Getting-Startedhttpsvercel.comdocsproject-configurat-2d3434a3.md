##  [Getting Started](https://vercel.com/docs/project-configuration/vercel-ts#getting-started)[](https://vercel.com/docs/project-configuration/vercel-ts#getting-started)
###  [Requirements](https://vercel.com/docs/project-configuration/vercel-ts#requirements)[](https://vercel.com/docs/project-configuration/vercel-ts#requirements)
Use only one configuration file: `vercel.ts` or `vercel.json`.
You can have any sort of code in your `vercel.ts` file, but the final set of rules and configuration properties must be in a `config` struct export. Use the same property names as `vercel.json` in your `config` export. For rewrites, redirects, headers, and transforms, prefer the helper functions from `routes`:
```
export const config: VercelConfig = {
  buildCommand: 'npm run build',
  cleanUrls: true,
  trailingSlash: false,
  // See the sections below for all available options
};
```

To migrate from `vercel.json`, copy its contents into your `config` export, then add new capabilities as needed.
###  [Install @vercel/config](https://vercel.com/docs/project-configuration/vercel-ts#install-@vercel/config)[](https://vercel.com/docs/project-configuration/vercel-ts#install-@vercel/config)
Install the NPM package to get access to types and helpers.
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i @vercel/config
```

```
yarn add @vercel/config
```

```
npm i @vercel/config
```

```
bun add @vercel/config
```

Create a `vercel.ts` in your project root and export a typed config. The example below shows how to configure build commands, framework settings, routing rules (rewrites and redirects), and headers:
You can also use `vercel.js`, `vercel.mjs`, `vercel.cjs`, or `vercel.mts` to create this configuration file.
vercel.ts
```
import { routes, deploymentEnv, type VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  buildCommand: 'npm run build',
  framework: 'nextjs',

  rewrites: [
    routes.rewrite('/api/(.*)', 'https://backend.api.example.com/$1'),
    routes.rewrite('/(.*)', 'https://api.example.com/$1', {
      requestHeaders: {
        authorization: `Bearer ${deploymentEnv('API_TOKEN')}`,
      },
    }),
    routes.rewrite(
      '/users/:userId/posts/:postId',
      'https://api.example.com/users/$1/posts/$2',
      ({ userId, postId }) => ({
        requestHeaders: {
          'x-user-id': userId,
          'x-post-id': postId,
          authorization: `Bearer ${deploymentEnv('API_KEY')}`,
        },
      }),
    ),
  ],

  redirects: [routes.redirect('/old-docs', '/docs', { permanent: true })],

  headers: [
    routes.cacheControl('/static/(.*)', {
      public: true,
      maxAge: '1 week',
      immutable: true,
    }),
  ],

  crons: [{ path: '/api/cleanup', schedule: '0 0 * * *' }],
};
```

###  [Migrating from vercel.json](https://vercel.com/docs/project-configuration/vercel-ts#migrating-from-vercel.json)[](https://vercel.com/docs/project-configuration/vercel-ts#migrating-from-vercel.json)
To migrate from an existing `vercel.json`, paste its contents into a `config` export in a new vercel.ts file:
vercel.ts
```
export const config = {
  buildCommand: 'pnpm run generate-config',
  outputDirectory: ".next",
  headers: [
    {
      source: "/(.*)\\\\.(js|css|jpg|jpeg|gif|png|svg|txt|ttf|woff2|webmanifest)",
      headers: [
        {
          key: "Cache-Control",
          value: "public, max-age=2592000, s-maxage=2592000"
        }
      ]
    }
  ]
}
```

Then install the `@vercel/config` package and enhance your configuration:
vercel.ts
```
import { routes, type VercelConfig } from '@vercel/config/v1'

export const config: VercelConfig = {
  buildCommand: 'pnpm run generate-config',
  outputDirectory: `.${process.env.framework}`,
  headers: [
    routes.cacheControl(
      '/(.*)\\\\.(js|css|jpg|jpeg|gif|png|svg|txt|ttf|woff2|webmanifest)',
      {
        public: true,
        maxAge: '30days',
        sMaxAge: '30days'
      }
    )
  ]
}
```
