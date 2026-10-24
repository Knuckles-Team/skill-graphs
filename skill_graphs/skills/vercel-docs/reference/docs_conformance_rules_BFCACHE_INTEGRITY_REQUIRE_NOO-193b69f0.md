Menu
Menu
# BFCACHE_INTEGRITY_REQUIRE_NOOPENER_ATTRIBUTE
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
The Back-Forward Cache (bfcache) is a browser feature that allows pages to be cached in memory when the user navigates away from them. When the user navigates back to the page, it can be loaded almost instantly from the cache instead of having to be reloaded from the network. Breaking the bfcache's integrity can cause a page to be reloaded from the network when the user navigates back to it, which can be slow and jarring.
Pages opened with `window.open` that do not use the `noopener` attribute can both be a security risk and also will prevent browsers from caching the page in the bfcache. This is because the new window can access the `window.opener` property of the original window, so putting the original page into the bfcache could break the new window when attempting to access it.
Using the `noreferrer` attribute will also set the `noopener` attribute to true, so it can also be used to ensure the page is placed into the bfcache.
To learn more about the bfcache, see the
##  [Related Rules](https://vercel.com/docs/conformance/rules/BFCACHE_INTEGRITY_REQUIRE_NOOPENER_ATTRIBUTE#related-rules)[](https://vercel.com/docs/conformance/rules/BFCACHE_INTEGRITY_REQUIRE_NOOPENER_ATTRIBUTE#related-rules)
  * [BFCACHE_INTEGRITY_NO_UNLOAD_LISTENERS](https://vercel.com/docs/conformance/rules/BFCACHE_INTEGRITY_NO_UNLOAD_LISTENERS)


##  [Example](https://vercel.com/docs/conformance/rules/BFCACHE_INTEGRITY_REQUIRE_NOOPENER_ATTRIBUTE#example)[](https://vercel.com/docs/conformance/rules/BFCACHE_INTEGRITY_REQUIRE_NOOPENER_ATTRIBUTE#example)
Examples of when this check would fail:
```
window.open('https://example.com', '_blank');
window.open('https://example.com');
```

##  [How to fix](https://vercel.com/docs/conformance/rules/BFCACHE_INTEGRITY_REQUIRE_NOOPENER_ATTRIBUTE#how-to-fix)[](https://vercel.com/docs/conformance/rules/BFCACHE_INTEGRITY_REQUIRE_NOOPENER_ATTRIBUTE#how-to-fix)
Instead, use the `noopener` or `noreferrer` attributes:
```
window.open('https://example.com', '_blank', 'noopener');
window.open('https://example.com', '_top', 'noreferrer');
```

* * *
Was this helpful?
Send
