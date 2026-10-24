## Possible Ways to Fix It[](https://nextjs.org/docs/messages/google-font-preconnect#possible-ways-to-fix-it)
Add `rel="preconnect"` to the Google Font domain `<link>` tag:
pages/_document.js
```
<link rel="preconnect" href="https://fonts.gstatic.com" />
```

> **Note** : a **separate** link with `dns-prefetch` can be used as a fallback for browsers that don't support `preconnect` although this is not required.
