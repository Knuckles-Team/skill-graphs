## Debugging[](https://nextjs.org/docs/messages/missing-suspense-with-csr-bailout#debugging)
If you're having trouble locating where `useSearchParams()` is being used without a Suspense boundary, you can get more detailed stack traces by running:
```
next build --debug-prerender
```

This provides unminified stack traces with source maps, making it easier to pinpoint the exact component and route causing the issue.
