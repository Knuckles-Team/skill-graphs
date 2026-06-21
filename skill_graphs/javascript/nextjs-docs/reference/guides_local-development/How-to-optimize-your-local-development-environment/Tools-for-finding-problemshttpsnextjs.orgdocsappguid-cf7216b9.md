## Tools for finding problems[](https://nextjs.org/docs/app/guides/local-development#tools-for-finding-problems)
### Detailed fetch logging[](https://nextjs.org/docs/app/guides/local-development#detailed-fetch-logging)
Use the `logging.fetches` option in your `next.config.js` file, to see more detailed information about what's happening during development:
```
module.exports = {
  logging: {
    fetches: {
      fullUrl: true,
    },
  },
}
```

[Learn more about fetch logging](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging).
### Turbopack tracing[](https://nextjs.org/docs/app/guides/local-development#turbopack-tracing)
Turbopack tracing is a tool that helps you understand the performance of your application during local development. It provides detailed information about the time taken for each module to compile and how they are related.
  1. Make sure you have the latest version of Next.js installed.
  2. Generate a Turbopack trace file:
pnpmnpmyarnbun
Terminal
```
NEXT_TURBOPACK_TRACING=1 pnpm dev
```

  3. Navigate around your application or make edits to files to reproduce the problem.
  4. Stop the Next.js development server.
  5. A file called `trace-turbopack` will be available in the `.next/dev` folder.
  6. You can interpret the file using `npx next internal trace [path-to-file]`:
```
npx next internal trace .next/dev/trace-turbopack
```

On versions where `trace` is not available, the command was named `turbo-trace-server`:
```
npx next internal turbo-trace-server .next/dev/trace-turbopack
```

  7. Once the trace server is running you can view the trace at <https://trace.nextjs.org/>.
  8. By default the trace viewer will aggregate timings, in order to see each individual time you can switch from "Aggregated in order" to "Spans in order" at the top right of the viewer.


> **Good to know** : The trace file is place under the development server directory, which defaults to `.next/dev`. This is controllable using the [`isolatedDevBuild`](https://nextjs.org/docs/app/api-reference/config/next-config-js/isolatedDevBuild) flag in your Next config file.
### Still having problems?[](https://nextjs.org/docs/app/guides/local-development#still-having-problems)
Share the trace file generated in the [Turbopack Tracing](https://nextjs.org/docs/app/guides/local-development#turbopack-tracing) section and share it on [Discord](https://nextjs.org/discord).
[PreviousLazy Loading](https://nextjs.org/docs/app/guides/lazy-loading)[NextNext.js MCP Server](https://nextjs.org/docs/app/guides/mcp)
Was this helpful?
Send
* * *
* * *
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Next.js Conf](https://nextjs.org/conf)[Evals](https://nextjs.org/evals)
#### More
[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)
#### About Vercel
#### Legal
Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
* * *
* * *
