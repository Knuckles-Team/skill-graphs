Menu
Menu
# NEXTJS_NO_DYNAMIC_AUTO
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
Changing the dynamic behavior of a layout or page using "force-dynamic" is not recommended in App Router. This is because this will force only dynamic rendering of those pages and opt-out "fetch" request from the fetch cache. Furthermore, opting out will also prevent future optimizations such as partially static subtrees and hybrid server-side rendering, which can significantly improve performance.
See
##  [How to fix](https://vercel.com/docs/conformance/rules/NEXTJS_NO_DYNAMIC_AUTO#how-to-fix)[](https://vercel.com/docs/conformance/rules/NEXTJS_NO_DYNAMIC_AUTO#how-to-fix)
Usage of `force-dynamic` can be avoided and instead `no-store` or `fetch` calls can be used instead. Alternatively, usage of `cookies()` can also avoid the need to use `force-dynamic`.
```
// Example of how to use `no-store` on `fetch` calls.
const data = fetch(someURL, { cache: 'no-store' });
```

* * *
Was this helpful?
Send
