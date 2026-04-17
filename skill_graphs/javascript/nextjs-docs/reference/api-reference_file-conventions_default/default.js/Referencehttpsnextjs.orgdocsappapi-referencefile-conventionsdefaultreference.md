## Reference[](https://nextjs.org/docs/app/api-reference/file-conventions/default#reference)
###  `params` (optional)[](https://nextjs.org/docs/app/api-reference/file-conventions/default#params-optional)
A promise that resolves to an object containing the [dynamic route parameters](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) from the root segment down to the slot's subpages. For example:
app/[artist]/@sidebar/default.js
TypeScript
JavaScript TypeScript
```
export default async function Default({
  params,
}: {
  params: Promise<{ artist: string }>
}) {
  const { artist } = await params
}
```

Example | URL | `params`
---|---|---
`app/[artist]/@sidebar/default.js` | `/zack` | `Promise<{ artist: 'zack' }>`
`app/[artist]/[album]/@sidebar/default.js` | `/zack/next` | `Promise<{ artist: 'zack', album: 'next' }>`
  * Since the `params` prop is a promise. You must use `async/await` or React's
    * In version 14 and earlier, `params` was a synchronous prop. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
