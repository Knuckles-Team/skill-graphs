## How It Works[](https://nextjs.org/docs/app/api-reference/config/next-config-js/reactCompiler#how-it-works)
The React Compiler runs through a Babel plugin. To keep builds fast, Next.js uses a custom SWC optimization that only applies the React Compiler to relevant files—like those with JSX or React Hooks.
This avoids compiling everything and keeps the performance cost minimal. You may still see slightly slower builds compared to the default Rust-based compiler, but the impact is small and localized.
To use it, install the `babel-plugin-react-compiler`:
pnpmnpmyarnbun
Terminal
```
pnpm add -D babel-plugin-react-compiler
```

Then, add `reactCompiler` option in `next.config.js`:
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  reactCompiler: true,
}

export default nextConfig
```
