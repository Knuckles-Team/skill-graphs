## Generating trace files for performance debugging[](https://nextjs.org/docs/pages/api-reference/turbopack#generating-trace-files-for-performance-debugging)
If you encounter performance or memory issues and want to help the Next.js team diagnose them, you can generate a trace file by appending `NEXT_TURBOPACK_TRACING=1` to your dev command:
```
NEXT_TURBOPACK_TRACING=1 next dev
```

This will produce a `.next/dev/trace-turbopack` file. Include that file when creating a GitHub issue on the
By default the development server outputs to `.next/dev`. Read more about [isolatedDevBuild](https://nextjs.org/docs/app/api-reference/config/next-config-js/isolatedDevBuild).
