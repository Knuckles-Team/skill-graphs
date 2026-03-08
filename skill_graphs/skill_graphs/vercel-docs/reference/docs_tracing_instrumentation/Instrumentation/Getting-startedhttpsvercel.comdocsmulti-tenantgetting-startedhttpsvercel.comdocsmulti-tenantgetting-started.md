##  [Getting started](https://vercel.com/docs/multi-tenant#getting-started)[](https://vercel.com/docs/multi-tenant#getting-started)
To get started, install the following packages:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i @opentelemetry/api @vercel/otel
```

```
yarn add @opentelemetry/api @vercel/otel
```

```
npm i @opentelemetry/api @vercel/otel
```

```
bun add @opentelemetry/api @vercel/otel
```

Next, create a `instrumentation.ts` (or `.js`) file in the root directory of the project, or, on Next.js `src` directory if you are using one. Add the following code to initialize and configure OTel using `@vercel/otel`:
instrumentation.ts
TypeScript
TypeScript JavaScript Bash
```
import { registerOTel } from '@vercel/otel';

export function register() {
  registerOTel({ serviceName: 'your-project-name' });
}
// NOTE: You can replace `your-project-name` with the actual name of your project
```
