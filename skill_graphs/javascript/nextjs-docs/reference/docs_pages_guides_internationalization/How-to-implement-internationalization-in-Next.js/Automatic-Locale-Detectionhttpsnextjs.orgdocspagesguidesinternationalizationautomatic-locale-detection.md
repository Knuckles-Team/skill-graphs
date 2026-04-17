## Automatic Locale Detection[](https://nextjs.org/docs/pages/guides/internationalization#automatic-locale-detection)
When a user visits the application root (generally `/`), Next.js will try to automatically detect which locale the user prefers based on the
If a locale other than the default locale is detected, the user will be redirected to either:
  * **When using Sub-path Routing:** The locale prefixed path
  * **When using Domain Routing:** The domain with that locale specified as the default


When using Domain Routing, if a user with the `Accept-Language` header `fr;q=0.9` visits `example.com`, they will be redirected to `example.fr` since that domain handles the `fr` locale by default.
When using Sub-path Routing, the user would be redirected to `/fr`.
### Prefixing the Default Locale[](https://nextjs.org/docs/pages/guides/internationalization#prefixing-the-default-locale)
With Next.js 12 and [Proxy](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy), we can add a prefix to the default locale with a
For example, here's a `next.config.js` file with support for a few languages. Note the `"default"` locale has been added intentionally.
next.config.js
```
module.exports = {
  i18n: {
    locales: ['default', 'en', 'de', 'fr'],
    defaultLocale: 'default',
    localeDetection: false,
  },
  trailingSlash: true,
}
```

Next, we can use [Proxy](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy) to add custom routing rules:
proxy.ts
```
import { NextRequest, NextResponse } from 'next/server'

const PUBLIC_FILE = /\.(.*)$/

export async function proxy(req: NextRequest) {
  if (
    req.nextUrl.pathname.startsWith('/_next') ||
    req.nextUrl.pathname.includes('/api/') ||
    PUBLIC_FILE.test(req.nextUrl.pathname)
  ) {
    return
  }

  if (req.nextUrl.locale === 'default') {
    const locale = req.cookies.get('NEXT_LOCALE')?.value || 'en'

    return NextResponse.redirect(
      new URL(`/${locale}${req.nextUrl.pathname}${req.nextUrl.search}`, req.url)
    )
  }
}
```

This [Proxy](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy) skips adding the default prefix to [API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes) and [public](https://nextjs.org/docs/pages/api-reference/file-conventions/public-folder) files like fonts or images. If a request is made to the default locale, we redirect to our prefix `/en`.
### Disabling Automatic Locale Detection[](https://nextjs.org/docs/pages/guides/internationalization#disabling-automatic-locale-detection)
The automatic locale detection can be disabled with:
next.config.js
```
module.exports = {
  i18n: {
    localeDetection: false,
  },
}
```

When `localeDetection` is set to `false` Next.js will no longer automatically redirect based on the user's preferred locale and will only provide locale information detected from either the locale based domain or locale path as described above.
