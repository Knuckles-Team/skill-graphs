##  [Allowlisting all errors](https://vercel.com/docs/conformance/allowlist#allowlisting-all-errors)[](https://vercel.com/docs/conformance/allowlist#allowlisting-all-errors)
The Conformance CLI can add an allowlist entry for all the active errors. This can be useful when adding a new entry to the allowlist for review, or when a new check is being added to the codebase. To add an allowlist entry for all active errors in a package:
From the package directory:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm conformance --allowlist-errors
```

```
yarn conformance --allowlist-errors
```

```
npm run conformance -- --allowlist-errors
```

```
bun run conformance -- --allowlist-errors
```

From the root of a monorepo:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm --filter=<package-name> conformance --allowlist-errors
```

```
yarn workspace <package-name> conformance --allowlist-errors
```

```
npm run conformance --workspace=<package-name> -- --allowlist-errors
```

```
bun run conformance --filter <package-name> -- --allowlist-errors
```
