# urlImports
This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on
Last updated February 27, 2026
URL imports are an experimental feature that allows you to import modules directly from external servers (instead of from the local disk).
> **Warning** : Only use domains that you trust to download and execute on your machine. Please exercise discretion, and caution until the feature is flagged as stable.
To opt-in, add the allowed URL prefixes inside `next.config.js`:
next.config.js
```
module.exports = {
  experimental: {
    urlImports: ['https://example.com/assets/', 'https://cdn.skypack.dev'],
  },
}
```

Then, you can import modules directly from URLs:
```
import { a, b, c } from 'https://example.com/assets/some/module.js'
```

URL Imports can be used everywhere normal package imports can be used.
