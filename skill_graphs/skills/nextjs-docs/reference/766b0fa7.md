## Exports[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#exports)
### Proxy function[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#proxy-function)
The file must export a single function, either as a default export or named `proxy`. Note that multiple proxy from the same file are not supported.
proxy.js
```
// Example of default export
export default function proxy(request) {
  // Proxy logic
}
```

### Config object (optional)[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#config-object-optional)
Optionally, a config object can be exported alongside the Proxy function. This object includes the [matcher](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#matcher) to specify paths where the Proxy applies.
### Matcher[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#matcher)
The `matcher` option allows you to target specific paths for the Proxy to run on. You can specify these paths in several ways:
  * For a single path: Directly use a string to define the path, like `'/about'`.
  * For multiple paths: Use an array to list multiple paths, such as `matcher: ['/about', '/contact']`, which applies the Proxy to both `/about` and `/contact`.


proxy.js
```
export const config = {
  matcher: ['/about/:path*', '/dashboard/:path*'],
}
```

Additionally, the `matcher` option supports complex path specifications using regular expressions. For example, you can exclude certain paths with a regular expression matcher:
proxy.js
```
export const config = {
  matcher: [
    // Exclude API routes, static files, image optimizations, and .png files
    '/((?!api|_next/static|_next/image|.*\\.png$).*)',
  ],
}
```

This enables precise control over which paths to include or exclude.
The `matcher` option accepts an array of objects with the following keys:
  * `source`: The path or pattern used to match the request paths. It can be a string for direct path matching or a pattern for more complex matching.
  * `locale` (optional): A boolean that, when set to `false`, ignores locale-based routing in path matching.
  * `has` (optional): Specifies conditions based on the presence of specific request elements such as headers, query parameters, or cookies.
  * `missing` (optional): Focuses on conditions where certain request elements are absent, like missing headers or cookies.


proxy.js
```
export const config = {
  matcher: [
    {
      source: '/api/:path*',
      locale: false,
      has: [
        { type: 'header', key: 'Authorization', value: 'Bearer Token' },
        { type: 'query', key: 'userId', value: '123' },
      ],
      missing: [{ type: 'cookie', key: 'session', value: 'active' }],
    },
  ],
}
```

The `source` path patterns:
  1. MUST start with `/`
  2. Can include named parameters: `/about/:path` matches `/about/a` and `/about/b` but not `/about/a/c`
  3. Can have modifiers on named parameters (starting with `:`): `/about/:path*` matches `/about/a/b/c` because `*` is _zero or more_. `?` is _zero or one_ and `+` _one or more_
  4. Can use regular expression enclosed in parenthesis: `/about/(.*)` is the same as `/about/:path*`
  5. Are anchored to the start of the path: `/about` matches `/about` and `/about/team` but not `/blog/about`


Read more details on
> **Good to know** :
>   * The `matcher` values need to be constants so they can be statically analyzed at build-time. Dynamic values such as variables will be ignored.
>   * For backward compatibility, Next.js always considers `/public` as `/public/index`. Therefore, a matcher of `/public/:path` will match.
>
