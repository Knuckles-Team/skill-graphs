##  [Using a custom server entrypoint](https://vercel.com/docs/getting-started-with-vercel#using-a-custom-server-entrypoint)[](https://vercel.com/docs/getting-started-with-vercel#using-a-custom-server-entrypoint)
Your React Router application may define a custom server entrypoint, which is useful for supplying a "load context" for use by the application's loaders and actions.
The server entrypoint file is expected to export a Web API-compatible function that matches the following signature:
```
export default async function (request: Request) => Response | Promise<Response>;
```

To implement a server entrypoint using the
First define the `build.rollupOptions.input` property in your Vite config file:
/vite.config.ts
TypeScript
TypeScript JavaScript Bash
```
import { reactRouter } from '@react-router/dev/vite';
import tailwindcss from '@tailwindcss/vite';
import { defineConfig } from 'vite';
import tsconfigPaths from 'vite-tsconfig-paths';

export default defineConfig(({ isSsrBuild }) => ({
  build: {
    rollupOptions: isSsrBuild
      ? {
          input: './server/app.ts',
        }
      : undefined,
  },
  plugins: [tailwindcss(), reactRouter(), tsconfigPaths()],
}));
```

Then, create the server entrypoint file:
/server/app.ts
TypeScript
TypeScript JavaScript Bash
```
import { Hono } from 'hono';
import { createRequestHandler } from 'react-router';

// @ts-expect-error - virtual module provided by React Router at build time
import * as build from 'virtual:react-router/server-build';

declare module 'react-router' {
  interface AppLoadContext {
    VALUE_FROM_HONO: string;
  }
}

const app = new Hono();

// Add any additional Hono middleware here

const handler = createRequestHandler(build);
app.mount('/', (req) =>
  handler(req, {
    // Add your "load context" here based on the current request
    VALUE_FROM_HONO: 'Hello from Hono',
  }),
);

export default app.fetch;
```

To summarize, using a custom server entrypoint with React Router on Vercel allows you to:
  * Supply a "load context" for use in your `loader` and `action` functions
  * Use a Web API-compatible framework alongside your React Router application
