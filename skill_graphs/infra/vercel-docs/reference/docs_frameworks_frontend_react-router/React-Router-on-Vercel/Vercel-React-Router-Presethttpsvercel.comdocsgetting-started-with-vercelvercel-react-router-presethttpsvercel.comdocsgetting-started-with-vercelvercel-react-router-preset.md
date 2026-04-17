##  [Vercel React Router Preset](https://vercel.com/docs/getting-started-with-vercel#vercel-react-router-preset)[](https://vercel.com/docs/getting-started-with-vercel#vercel-react-router-preset)
When using the
To configure the Preset, add the following lines to your `react-router.config` file:
/react-router.config.ts
```
import { vercelPreset } from '@vercel/react-router/vite';
import type { Config } from '@react-router/dev/config';

export default {
  // Config options...
  // Server-side render by default, to enable SPA mode set this to `false`
  ssr: true,
  presets: [vercelPreset()],
} satisfies Config;
```

When this Preset is configured, your React Router application is enhanced with Vercel-specific functionality:
  * Allows function-level configuration (i.e. `memory`, `maxDuration`, etc.) on a per-route basis
  * Allows Vercel to understand the routing structure of the application, which allows for bundle splitting
  * Accurate "Deployment Summary" on the deployment details page
