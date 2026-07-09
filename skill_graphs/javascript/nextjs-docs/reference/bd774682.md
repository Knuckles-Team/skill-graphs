## Why This Error Occurred[](https://nextjs.org/docs/messages/empty-generate-static-params#why-this-error-occurred)
You're using [Cache Components](https://nextjs.org/docs/app/getting-started/caching) in your Next.js application, and one of your `generateStaticParams` functions returned an empty array, which causes a build error.
When Cache Components is enabled, Next.js performs build-time validation to ensure your routes can be properly prerendered without runtime dynamic access errors. If `generateStaticParams` returns an empty array, Next.js cannot validate that your route won't access dynamic values (like `await cookies()`, `await headers()`, or `await searchParams`) at runtime, which would cause errors.
This strict requirement ensures:
  * Build-time validation catches potential runtime errors early
  * All routes using Cache Components have at least one static variant to validate against
  * You don't accidentally deploy routes that will fail at runtime
