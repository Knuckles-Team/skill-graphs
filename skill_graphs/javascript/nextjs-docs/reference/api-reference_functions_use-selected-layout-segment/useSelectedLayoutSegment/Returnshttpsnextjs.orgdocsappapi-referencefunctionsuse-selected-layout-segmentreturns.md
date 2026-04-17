## Returns[](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment#returns)
`useSelectedLayoutSegment` returns a string of the active segment or `null` if one doesn't exist.
For example, given the Layouts and URLs below, the returned segment would be:
Layout | Visited URL | Returned Segment
---|---|---
`app/layout.js` | `/` | `null`
`app/layout.js` | `/dashboard` | `'dashboard'`
`app/dashboard/layout.js` | `/dashboard` | `null`
`app/dashboard/layout.js` | `/dashboard/settings` | `'settings'`
`app/dashboard/layout.js` | `/dashboard/analytics` | `'analytics'`
`app/dashboard/layout.js` | `/dashboard/analytics/monthly` | `'analytics'`
For catch-all routes (`[...slug]`), the returned segment contains all matched path segments joined as a single string:
Layout | Visited URL | Returned Segment
---|---|---
`app/blog/layout.js` | `/blog/a/b/c` | `'a/b/c'`
