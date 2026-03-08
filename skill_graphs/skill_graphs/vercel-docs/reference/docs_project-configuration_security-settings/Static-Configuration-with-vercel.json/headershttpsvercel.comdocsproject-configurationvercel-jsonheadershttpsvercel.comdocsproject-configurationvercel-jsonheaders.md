##  [headers](https://vercel.com/docs/project-configuration/vercel-json#headers)[](https://vercel.com/docs/project-configuration/vercel-json#headers)
Type: `Array` of header `Object`.
Valid values: a list of header definitions.
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "headers": [
    {
      "source": "/service-worker.js",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "public, max-age=0, must-revalidate"
        }
      ]
    },
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "X-Content-Type-Options",
          "value": "nosniff"
        },
        {
          "key": "X-Frame-Options",
          "value": "DENY"
        },
        {
          "key": "X-XSS-Protection",
          "value": "1; mode=block"
        }
      ]
    },
    {
      "source": "/:path*",
      "has": [
        {
          "type": "query",
          "key": "authorized"
        }
      ],
      "headers": [
        {
          "key": "x-authorized",
          "value": "true"
        }
      ]
    }
  ]
}
```

This example configures custom response headers for static files, [Vercel functions](https://vercel.com/docs/functions), and a wildcard that matches all routes.
###  [Header object definition](https://vercel.com/docs/project-configuration/vercel-json#header-object-definition)[](https://vercel.com/docs/project-configuration/vercel-json#header-object-definition)
Property | Description
---|---
`source` | A pattern that matches each incoming pathname (excluding querystring).
`headers` | A non-empty array of key/value pairs representing each response header.
`has` | An optional array of `has` objects with the `type`, `key` and `value` properties. Used for conditional path matching based on the presence of specified properties.
`missing` | An optional array of `missing` objects with the `type`, `key` and `value` properties. Used for conditional path matching based on the absence of specified properties.
###  [Header `has` or `missing` object definition](https://vercel.com/docs/project-configuration/vercel-json#header-has-or-missing-object-definition)[](https://vercel.com/docs/project-configuration/vercel-json#header-has-or-missing-object-definition)
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
This example demonstrates using the expressive `value` object to append the header `x-authorized: true` if the `X-Custom-Header` request header's value is prefixed by `valid` and ends with `value`.
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "headers": [
    {
      "source": "/:path*",
      "has": [
        {
          "type": "header",
          "key": "X-Custom-Header",
          "value": {
            "pre": "valid",
            "suf": "value"
          }
        }
      ],
      "headers": [
        {
          "key": "x-authorized",
          "value": "true"
        }
      ]
    }
  ]
}
```

Learn more about [headers](https://vercel.com/docs/headers) on Vercel and see [limitations](https://vercel.com/docs/cdn-cache#limits).
