## Returns[](https://nextjs.org/docs/app/api-reference/functions/use-pathname#returns)
`usePathname` returns a string of the current URL's pathname. For example:
URL | Returned value
---|---
`/` | `'/'`
`/dashboard` | `'/dashboard'`
`/dashboard?v=2` | `'/dashboard'`
`/blog/hello-world` | `'/blog/hello-world'`
