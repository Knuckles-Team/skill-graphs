##  [redirects](https://vercel.com/docs/project-configuration/vercel-ts#redirects)[](https://vercel.com/docs/project-configuration/vercel-ts#redirects)
Type: `Array` of redirect `Object`.
Valid values: a list of redirect definitions.
###  [Redirects examples](https://vercel.com/docs/project-configuration/vercel-ts#redirects-examples)[](https://vercel.com/docs/project-configuration/vercel-ts#redirects-examples)
Some redirects and rewrites configurations can accidentally become gateways for semantic attacks. Learn how to check and protect your configurations with the [Enhancing Security for Redirects and Rewrites guide](https://vercel.com/kb/guide/enhancing-security-for-redirects-and-rewrites).
This example redirects requests to the path `/me` from your site's root to the `profile.html` file relative to your site's root with a
vercel.ts
```
import { routes, type VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  redirects: [
    routes.redirect('/me', '/profile.html', { permanent: false }),
  ],
};
```

This example redirects requests to the path `/me` from your site's root to the `profile.html` file relative to your site's root with a
vercel.ts
```
import { routes, type VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  redirects: [
    routes.redirect('/me', '/profile.html', { permanent: true }),
  ],
};
```

This example redirects requests to the path `/user` from your site's root to the api route `/api/user` relative to your site's root with a
vercel.ts
```
import { routes, type VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  redirects: [
    routes.redirect('/user', '/api/user', { statusCode: 301 }),
  ],
};
```

This example redirects requests to the path `/view-source` from your site's root to the absolute path `https://github.com/vercel/vercel` of an external site with a redirect status of 308:
vercel.ts
```
import { routes, type VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  redirects: [
    routes.redirect('/view-source', 'https://github.com/vercel/vercel'),
  ],
};
```

This example redirects requests to all the paths (including all sub-directories and pages) from your site's root to the absolute path `https://vercel.com/docs` of an external site with a redirect status of 308:
vercel.ts
```
import { routes, type VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  redirects: [
    routes.redirect('/(.*)', 'https://vercel.com/docs'),
  ],
};
```

This example uses wildcard path matching to redirect requests to any path (including subdirectories) under `/blog/` from your site's root to a corresponding path under `/news/` relative to your site's root with a redirect status of 308:
vercel.ts
```
import { routes, type VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  redirects: [
    routes.redirect('/blog/:path*', '/news/:path*'),
  ],
};
```

This example uses regex path matching to redirect requests to any path under `/posts/` that only contain numerical digits from your site's root to a corresponding path under `/news/` relative to your site's root with a redirect status of 308:
vercel.ts
```
import { routes, type VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  redirects: [
    routes.redirect('/post/:path(\\d{1,})', '/news/:path*'),
  ],
};
```

This example redirects requests to any path from your site's root that does not start with `/uk/` and has `x-vercel-ip-country` header value of `GB` to a corresponding path under `/uk/` relative to your site's root with a redirect status of 307:
vercel.ts
```
import { routes, type VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  redirects: [
    routes.redirect('/:path((?!uk/).*)', '/uk/:path*', {
      has: [
        {
          type: 'header',
          key: 'x-vercel-ip-country',
          value: 'GB',
        },
      ],
      permanent: false,
    }),
  ],
};
```

Using `has` does not yet work locally while using `vercel dev`, but does work when deployed.
###  [Redirect object definition](https://vercel.com/docs/project-configuration/vercel-ts#redirect-object-definition)[](https://vercel.com/docs/project-configuration/vercel-ts#redirect-object-definition)
Property | Description
---|---
`source` | A pattern that matches each incoming pathname (excluding querystring).
`destination` | A location destination defined as an absolute pathname or external URL.
`permanent` | An optional boolean to toggle between permanent and temporary redirect (default `true`). When `true`, the status code is `false` the status code is
`statusCode` | An optional integer to define the status code of the redirect. Used when you need a value other than 307/308 from `permanent`, and therefore cannot be used with `permanent` boolean.
`has` | An optional array of `has` objects with the `type`, `key` and `value` properties. Used for conditional redirects based on the presence of specified properties.
`missing` | An optional array of `missing` objects with the `type`, `key` and `value` properties. Used for conditional redirects based on the absence of specified properties.
###  [Redirect `has` or `missing` object definition](https://vercel.com/docs/project-configuration/vercel-ts#redirect-has-or-missing-object-definition)[](https://vercel.com/docs/project-configuration/vercel-ts#redirect-has-or-missing-object-definition)
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
This example uses the expressive `value` object to define a route that redirects users with a redirect status of 308 to `/end` only if the `X-Custom-Header` header's value is prefixed by `valid` and ends with `value`.
vercel.ts
```
import { routes, type VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  redirects: [
    routes.redirect('/start', '/end', {
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

Learn more about [redirects on Vercel](https://vercel.com/docs/redirects) and see [limitations](https://vercel.com/docs/redirects#limits).
