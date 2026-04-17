## Concurrent `dev` and `build`[](https://nextjs.org/docs/app/guides/upgrading/version-16#concurrent-dev-and-build)
`next dev` and `next build` now use separate output directories, enabling concurrent execution. The `next dev` command outputs to `.next/dev`. This is the new default behavior, controlled by [isolatedDevBuild](https://nextjs.org/docs/app/api-reference/config/next-config-js/isolatedDevBuild).
Additionally, a lockfile mechanism prevents multiple `next dev` or `next build` instances on the same project.
Since the development server outputs to `.next/dev`, the [Turbopack tracing command](https://nextjs.org/docs/app/guides/local-development#turbopack-tracing) should be:
pnpmnpmyarnbun
Terminal
```
pnpm next internal trace .next/dev/trace-turbopack
```
