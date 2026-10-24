##  `nextUrl`[](https://nextjs.org/docs/app/api-reference/functions/next-request#nexturl)
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
`basePath` | `string` | The [base path](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath) of the URL.
`buildId` |  `string` | `undefined` | The build identifier of the Next.js application. Can be [customized](https://nextjs.org/docs/app/api-reference/config/next-config-js/generateBuildId).
`pathname` | `string` | The pathname of the URL.
`searchParams` | `Object` | The search parameters of the URL.
> **Note:** The internationalization properties from the Pages Router are not available for usage in the App Router. Learn more about [internationalization with the App Router](https://nextjs.org/docs/app/guides/internationalization).
