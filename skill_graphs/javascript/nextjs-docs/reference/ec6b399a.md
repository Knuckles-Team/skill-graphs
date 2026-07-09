# isolatedDevBuild
Last updated February 27, 2026
The experimental `isolatedDevBuild` option separates development and production build outputs into different directories. When enabled, the development server (`next dev`) writes its output to `.next/dev` instead of `.next`, preventing conflicts when running `next dev` and `next build` concurrently.
This is especially helpful when automated tools (for example, AI agents) run `next build` to validate changes while your development server is running, ensuring the dev server is not affected by changes made by the build process.
This feature is **enabled by default** to keep development and production outputs separate and prevent conflicts.
