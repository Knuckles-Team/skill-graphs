## Router navigation tracking[](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client#router-navigation-tracking)
You can export an `onRouterTransitionStart` function to receive notifications when navigation begins:
instrumentation-client.ts
TypeScript
JavaScript TypeScript
```
performance.mark('app-init')

export function onRouterTransitionStart(
  url: string,
  navigationType: 'push' | 'replace' | 'traverse'
) {
  console.log(`Navigation started: ${navigationType} to ${url}`)
  performance.mark(`nav-start-${Date.now()}`)
}
```

The `onRouterTransitionStart` function receives two parameters:
  * `url: string` - The URL being navigated to
  * `navigationType: 'push' | 'replace' | 'traverse'` - The type of navigation
