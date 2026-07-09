##  [How to fix](https://vercel.com/docs/conformance/rules/BFCACHE_INTEGRITY_NO_UNLOAD_LISTENERS#how-to-fix)[](https://vercel.com/docs/conformance/rules/BFCACHE_INTEGRITY_NO_UNLOAD_LISTENERS#how-to-fix)
Instead, we can use the `pagehide` event to detect when the user navigates away from the page.
src/utils/handle-user-navigation.ts
```
export function handleUserNavigatingAway() {
  window.onpagehide = (event) => {
    console.log('Page is about to be hidden.');
  };
}
```

src/utils/handle-user-navigation.ts
```
export function handleUserNavigatingAway() {
  window.addEventListener('pagehide', (event) => {
    console.log('Page is about to be hidden.');
  });
}
```

* * *
Was this helpful?
Send
On this page
  * [Related Rules](https://vercel.com/docs/conformance/rules/BFCACHE_INTEGRITY_NO_UNLOAD_LISTENERS#related-rules)
  * [Example](https://vercel.com/docs/conformance/rules/BFCACHE_INTEGRITY_NO_UNLOAD_LISTENERS#example)
  * [How to fix](https://vercel.com/docs/conformance/rules/BFCACHE_INTEGRITY_NO_UNLOAD_LISTENERS#how-to-fix)


Copy as MarkdownGive feedbackAsk AI about this page
