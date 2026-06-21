## Disable static analysis[](https://nextjs.org/docs/app/guides/memory-usage#disable-static-analysis)
Typechecking may require a lot of memory, especially in large projects. However, most projects have a dedicated CI runner that already handles these tasks. When the build produces out-of-memory issues during the "Running TypeScript" step, you can disable this task during builds:
next.config.mjs
```
/** @type {import('next').NextConfig} */
const nextConfig = {
  typescript: {
    // !! WARN !!
    // Dangerously allow production builds to successfully complete even if
    // your project has type errors.
    // !! WARN !!
    ignoreBuildErrors: true,
  },
}

export default nextConfig
```

  * [Ignoring TypeScript Errors](https://nextjs.org/docs/app/api-reference/config/typescript#disabling-typescript-errors-in-production)


Keep in mind that this may produce faulty deploys due to type errors. We strongly recommend only promoting builds to production after static analysis has completed. If you deploy to Vercel, you can check out the
