##  [Runtime support](https://vercel.com/docs/og-image-generation#runtime-support)[](https://vercel.com/docs/og-image-generation#runtime-support)
Vercel OG image generation is supported on the [Node.js runtime](https://vercel.com/docs/functions/runtimes/node-js).
Local resources can be loaded directly using `fs.readFile`. Alternatively, `fetch` can be used to load remote resources.
og.js
```
const fs = require('fs').promises;

const loadLocalImage = async () => {
  const imageData = await fs.readFile('/path/to/image.png');
  // Process image data
};
```

###  [Runtime caveats](https://vercel.com/docs/og-image-generation#runtime-caveats)[](https://vercel.com/docs/og-image-generation#runtime-caveats)
There are limitations when using `vercel/og` with the Next.js Pages Router and the Node.js runtime. Specifically, this combination does not support the `return new Response(…)` syntax. The table below provides a breakdown of the supported syntaxes for different configurations.
Configuration | Supported Syntax | Notes
---|---|---
`pages/` + Edge runtime | `return new Response(…)` | Fully supported.
`app/` + Node.js runtime | `return new Response(…)` | Fully supported.
`app/` + Edge runtime | `return new Response(…)` | Fully supported.
`pages/` + Node.js runtime | Not supported | Does not support `return new Response(…)` syntax with `vercel/og`.
