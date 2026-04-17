## Generate a Robots file[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#generate-a-robots-file)
Add a `robots.js` or `robots.ts` file that returns a [`Robots` object](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#robots-object).
> **Good to know** : `robots.js` is a special Route Handler that is cached by default unless it uses a [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-apis) or [dynamic config](https://nextjs.org/docs/app/guides/caching#segment-config-options) option.
app/robots.ts
TypeScript
JavaScript TypeScript
```
import type { MetadataRoute } from 'next'

export default function robots(): MetadataRoute.Robots {
  return {
    rules: {
      userAgent: '*',
      allow: '/',
      disallow: '/private/',
    },
    sitemap: 'https://acme.com/sitemap.xml',
  }
}
```

Output:
```
User-Agent: *
Allow: /
Disallow: /private/

Sitemap: https://acme.com/sitemap.xml
```

### Customizing specific user agents[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#customizing-specific-user-agents)
You can customize how individual search engine bots crawl your site by passing an array of user agents to the `rules` property. For example:
app/robots.ts
TypeScript
JavaScript TypeScript
```
import type { MetadataRoute } from 'next'

export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      {
        userAgent: 'Googlebot',
        allow: ['/'],
        disallow: '/private/',
      },
      {
        userAgent: ['Applebot', 'Bingbot'],
        disallow: ['/'],
      },
    ],
    sitemap: 'https://acme.com/sitemap.xml',
  }
}
```

Output:
```
User-Agent: Googlebot
Allow: /
Disallow: /private/

User-Agent: Applebot
Disallow: /

User-Agent: Bingbot
Disallow: /

Sitemap: https://acme.com/sitemap.xml
```

### Robots object[](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#robots-object)
```
type Robots = {
  rules:
    | {
        userAgent?: string | string[]
        allow?: string | string[]
        disallow?: string | string[]
        crawlDelay?: number
      }
    | Array<{
        userAgent: string | string[]
        allow?: string | string[]
        disallow?: string | string[]
        crawlDelay?: number
      }>
  sitemap?: string | string[]
  host?: string
}
```
