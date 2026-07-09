## Returns[](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segments#returns)
`useSelectedLayoutSegments` returns an array of strings containing the active segments one level down from the layout the hook was called from. Or an empty array if none exist.
For example, given the Layouts and URLs below, the returned segments would be:
Layout | Visited URL | Returned Segments
---|---|---
`app/layout.js` | `/` | `[]`
`app/layout.js` | `/dashboard` | `['dashboard']`
`app/layout.js` | `/dashboard/settings` | `['dashboard', 'settings']`
`app/dashboard/layout.js` | `/dashboard` | `[]`
`app/dashboard/layout.js` | `/dashboard/settings` | `['settings']`
For catch-all routes (`[...slug]`), all matched path segments are returned as a single joined string within the array:
Layout | Visited URL | Returned Segments
---|---|---
`app/layout.js` | `/blog/a/b/c` | `['blog', 'a/b/c']`
`app/blog/layout.js` | `/blog/a/b/c` | `['a/b/c']`
