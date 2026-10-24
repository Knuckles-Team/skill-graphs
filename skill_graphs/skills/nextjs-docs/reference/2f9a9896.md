## Performance considerations[](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client#performance-considerations)
Keep instrumentation code lightweight.
Next.js monitors initialization time in development and will log warnings if it takes longer than 16ms, which could impact smooth page loading.
