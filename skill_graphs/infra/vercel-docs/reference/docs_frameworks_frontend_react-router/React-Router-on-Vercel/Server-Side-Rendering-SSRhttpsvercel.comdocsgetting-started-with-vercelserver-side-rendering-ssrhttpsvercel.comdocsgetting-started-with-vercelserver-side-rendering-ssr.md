##  [Server-Side Rendering (SSR)](https://vercel.com/docs/getting-started-with-vercel#server-side-rendering-ssr)[](https://vercel.com/docs/getting-started-with-vercel#server-side-rendering-ssr)
Server-Side Rendering (SSR) allows you to render pages dynamically on the server. This is useful for pages where the rendered data needs to be unique on every request. For example, checking authentication or looking at the location of an incoming request. Server-Side Rendering is invoked using [Vercel Functions](https://vercel.com/docs/functions).
The following example demonstrates a basic route that renders with SSR:
/app/routes.ts
TypeScript
TypeScript JavaScript Bash
```
import { type RouteConfig, index } from '@react-router/dev/routes';

export default [index('routes/home.tsx')] satisfies RouteConfig;
```

/app/routes/home.tsx
TypeScript
TypeScript JavaScript Bash
```
import type { Route } from './+types/home';
import { Welcome } from '../welcome/welcome';

export function meta({}: Route.MetaArgs) {
  return [
    { title: 'New React Router App' },
    { name: 'description', content: 'Welcome to React Router!' },
  ];
}

export default function Home() {
  return <Welcome />;
}
```

To summarize, Server-Side Rendering (SSR) with React Router on Vercel:
  * Scales to zero when not in use
  * Scales automatically with traffic increases
  * Has framework-aware infrastructure to generate Vercel Functions
  * Supports the use of Vercel's [Fluid compute](https://vercel.com/docs/fluid-compute) for enhanced performance
