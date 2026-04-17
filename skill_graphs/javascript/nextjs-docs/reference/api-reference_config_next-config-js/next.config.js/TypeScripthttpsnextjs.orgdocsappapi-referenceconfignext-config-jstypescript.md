## TypeScript[](https://nextjs.org/docs/app/api-reference/config/next-config-js#typescript)
If you are using TypeScript in your project, you can use `next.config.ts` to use TypeScript in your configuration:
next.config.ts
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  /* config options here */
}

export default nextConfig
```

The commented lines are the place where you can put the configs allowed by `next.config.js`, which are
However, none of the configs are required, and it's not necessary to understand what each config does. Instead, search for the features you need to enable or modify in this section and they will show you what to do.
> Avoid using new JavaScript features not available in your target Node.js version. `next.config.js` will not be parsed by Webpack or Babel.
This page documents all the available configuration options:
