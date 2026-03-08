## Generate a Manifest file[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest#generate-a-manifest-file)
Add a `manifest.js` or `manifest.ts` file that returns a [`Manifest` object](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest#manifest-object).
> Good to know: `manifest.js` is a special Route Handler that is cached by default unless it uses a [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-apis) or [dynamic config](https://nextjs.org/docs/app/guides/caching#segment-config-options) option.
app/manifest.ts
TypeScript
JavaScript TypeScript
```
import type { MetadataRoute } from 'next'

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: 'Next.js App',
    short_name: 'Next.js App',
    description: 'Next.js App',
    start_url: '/',
    display: 'standalone',
    background_color: '#fff',
    theme_color: '#fff',
    icons: [
      {
        src: '/favicon.ico',
        sizes: 'any',
        type: 'image/x-icon',
      },
    ],
  }
}
```

### Manifest Object[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest#manifest-object)
The manifest object contains an extensive list of options that may be updated due to new web standards. For information on all the current options, refer to the `MetadataRoute.Manifest` type in your code editor if using [TypeScript](https://nextjs.org/docs/app/api-reference/config/typescript#ide-plugin) or see the
[Previousfavicon, icon, and apple-icon](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons)[Nextopengraph-image and twitter-image](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image)
Was this helpful?
Send
