##  `nextUrl`[](https://nextjs.org/docs/pages/api-reference/functions/next-request#nexturl)
Extends the native
```
// Given a request to /home, pathname is /home
request.nextUrl.pathname
// Given a request to /home?name=lee, searchParams is { 'name': 'lee' }
request.nextUrl.searchParams
```

The following options are available:
Property | Type | Description
---|---|---
`basePath` | `string` | The [base path](https://nextjs.org/docs/pages/api-reference/config/next-config-js/basePath) of the URL.
`buildId` |  `string` | `undefined` | The build identifier of the Next.js application. Can be [customized](https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateBuildId).
`defaultLocale` |  `string` | `undefined` | The default locale for [internationalization](https://nextjs.org/docs/pages/guides/internationalization).
`domainLocale` |  |
- `defaultLocale` | `string` | The default locale within a domain.
- `domain` | `string` | The domain associated with a specific locale.
- `http` |  `boolean` | `undefined` | Indicates if the domain is using HTTP.
`locales` |  `string[]` | `undefined` | An array of available locales.
`locale` |  `string` | `undefined` | The currently active locale.
`url` | `URL` | The URL object.
