# Programmatic Configuration with vercel.ts
Last updated December 19, 2025
The `vercel.ts` file lets you configure and override the default behavior of Vercel from within your project. Unlike `vercel.json`, which is static, `vercel.ts` executes at build time, which lets you dynamically generate configuration. For example, you can fetch content from APIs, use environment variables to conditionally set routes, or compute configuration values based on your project structure.
