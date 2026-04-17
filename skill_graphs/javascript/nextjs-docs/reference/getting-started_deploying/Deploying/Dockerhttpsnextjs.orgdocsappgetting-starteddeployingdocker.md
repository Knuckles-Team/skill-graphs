## Docker[](https://nextjs.org/docs/app/getting-started/deploying#docker)
Next.js can be deployed to any provider that supports
Docker deployments support all Next.js features. Learn how to [configure them](https://nextjs.org/docs/app/guides/self-hosting) for your infrastructure.
> **Note for development:** While Docker is excellent for production deployments, consider using local development (`npm run dev`) instead of Docker during development on Mac and Windows for better performance. [Learn more about optimizing local development](https://nextjs.org/docs/app/guides/local-development).
### Templates[](https://nextjs.org/docs/app/getting-started/deploying#templates-1)
The following examples demonstrate best practices for containerizing Next.js applications:
  * `output: "standalone"` to generate a minimal, production-ready Docker image with only the required runtime files and dependencies.
  * `output: "export"` to generate optimized HTML files that can be served from a lightweight container or any static hosting environment.


Additionally, hosting providers offer guidance on deploying Next.js:
