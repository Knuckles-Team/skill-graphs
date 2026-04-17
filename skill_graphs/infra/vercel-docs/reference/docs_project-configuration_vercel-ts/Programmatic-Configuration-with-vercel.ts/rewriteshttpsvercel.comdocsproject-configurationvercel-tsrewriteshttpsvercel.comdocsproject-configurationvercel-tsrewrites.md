##  [rewrites](https://vercel.com/docs/project-configuration/vercel-ts#rewrites)[](https://vercel.com/docs/project-configuration/vercel-ts#rewrites)
Type: `Array` of rewrite `Object`.
Valid values: a list of rewrite definitions.
If [`cleanUrls`](https://vercel.com/docs/project-configuration/vercel-ts#cleanurls) is set to `true` in your project's `vercel.ts`, do not include the file extension in the source or destination path. For example, `/about-our-company.html` would be `/about-our-company`
Some redirects and rewrites configurations can accidentally become gateways for semantic attacks. Learn how to check and protect your configurations with the [Enhancing Security for Redirects and Rewrites guide](https://vercel.com/kb/guide/enhancing-security-for-redirects-and-rewrites).
###  [Rewrites examples](https://vercel.com/docs/project-configuration/vercel-ts#rewrites-examples)[](https://vercel.com/docs/project-configuration/vercel-ts#rewrites-examples)
  * This example rewrites requests to the path `/about` from your site's root to the `/about-our-company.html` file relative to your site's root:
vercel.ts
```
import { routes, type VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  rewrites: [routes.rewrite('/about', '/about-our-company.html')],
};
```

  * This example rewrites all requests to the root path which is often used for a Single Page Application (SPA).
vercel.ts
```
import { routes, type VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  rewrites: [routes.rewrite('/(.*)', '/index.html')],
};
```

  * This example rewrites requests to the paths under `/resize` with 2 path levels (defined as variables `width` and `height` that can be used in the destination value) to the api route `/api/sharp` relative to your site's root:
vercel.ts
```
import { routes, type VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  rewrites: [routes.rewrite('/resize/:width/:height', '/api/sharp')],
};
```

  * This example uses wildcard path matching to rewrite requests to any path (including subdirectories) under `/proxy/` from your site's root to a corresponding path under the root of an external site `https://example.com/`:
vercel.ts
```
import { routes, type VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  rewrites: [
    routes.rewrite('/proxy/:match*', 'https://example.com/:match*'),
  ],
};
```

  * This example rewrites requests to any path from your site's root that does not start with /uk/ and has x-vercel-ip-country header value of GB to a corresponding path under /uk/ relative to your site's root:
vercel.ts
```
import { routes, type VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  rewrites: [
    routes.rewrite('/:path((?!uk/).*)', '/uk/:path*', {
      has: [
        {
          type: 'header',
          key: 'x-vercel-ip-country',
          value: 'GB',
        },
      ],
    }),
  ],
};
```

  * This example rewrites requests to the path `/dashboard` from your site's root that does not have a cookie with key `auth_token` to the path `/login` relative to your site's root:
vercel.ts
```
import { routes, type VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  rewrites: [
    routes.rewrite('/dashboard', '/login', {
      missing: [
        {
          type: 'cookie',
          key: 'auth_token',
        },
      ],
    }),
  ],
};
```



###  [Rewrite object definition](https://vercel.com/docs/project-configuration/vercel-ts#rewrite-object-definition)[](https://vercel.com/docs/project-configuration/vercel-ts#rewrite-object-definition)
Property | Description
---|---
`source` | A pattern that matches each incoming pathname (excluding querystring).
`destination` | A location destination defined as an absolute pathname or external URL.
`permanent` | A boolean to toggle between permanent and temporary redirect (default true). When `true`, the status code is `false` the status code is
`has` | An optional array of `has` objects with the `type`, `key` and `value` properties. Used for conditional rewrites based on the presence of specified properties.
`missing` | An optional array of `missing` objects with the `type`, `key` and `value` properties. Used for conditional rewrites based on the absence of specified properties.
###  [Rewrite `has` or `missing` object definition](https://vercel.com/docs/project-configuration/vercel-ts#rewrite-has-or-missing-object-definition)[](https://vercel.com/docs/project-configuration/vercel-ts#rewrite-has-or-missing-object-definition)
Property | Type | Description
---|---|---
`type` | `String` | Must be either `header`, `cookie`, `host`, or `query`. The `type` property only applies to request headers sent by clients, not response headers sent by your functions or backends.
`key` | `String` | The key from the selected type to match against. For example, if the `type` is `header` and the `key` is `X-Custom-Header`, we will match against the `X-Custom-Header` header key.
`value` |  `String` or `Object` or `undefined` | The value to check for, if `undefined` any value will match. A regex like string can be used to capture a specific part of the value. For example, if the value `first-(?<paramName>.*)` is used for `first-second` then `second` will be usable in the destination with `:paramName`. If an object is provided, it will match when all conditions are met for its fields below.
If `value` is an object, it has one or more of the following fields:
Condition | Type | Description
---|---|---
`eq` |  `String` (optional) | Check for equality
`neq` |  `String` (optional) | Check for inequality
`inc` |  `Array<String>` (optional) | Check for inclusion in the array
`ninc` |  `Array<String>` (optional) | Check for non-inclusion in the array
`pre` |  `String` (optional) | Check for prefix
`suf` |  `String` (optional) | Check for suffix
`re` |  `String` (optional) | Check for a regex match
`gt` |  `Number` (optional) | Check for greater than
`gte` |  `Number` (optional) | Check for greater than or equal to
`lt` |  `Number` (optional) | Check for less than
`lte` |  `Number` (optional) | Check for less than or equal to
This example demonstrates using the expressive `value` object to define a route that rewrites users to `/end` only if the `X-Custom-Header` header's value is prefixed by `valid` and ends with `value`.
vercel.ts
```
import { routes, type VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  rewrites: [
    routes.rewrite('/start', '/end', {
      has: [
        {
          type: 'header',
          key: 'X-Custom-Header',
          value: { pre: 'valid', suf: 'value' },
        },
      ],
    }),
  ],
};
```

The `source` property should NOT be a file because precedence is given to the filesystem prior to rewrites being applied. Instead, you should rename your static file or Vercel Function.
Using `has` does not yet work locally while using `vercel dev`, but does work when deployed.
Learn more about [rewrites](https://vercel.com/docs/rewrites) on Vercel.
