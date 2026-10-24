## Optional Catch-all Segments[](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#optional-catch-all-segments)
Catch-all Segments can be made **optional** by including the parameter in double square brackets: `[[...segmentName]]`.
For example, `pages/shop/[[...slug]].js` will **also** match `/shop`, in addition to `/shop/clothes`, `/shop/clothes/tops`, `/shop/clothes/tops/t-shirts`.
The difference between **catch-all** and **optional catch-all** segments is that with optional, the route without the parameter is also matched (`/shop` in the example above).
Route | Example URL | `params`
---|---|---
`pages/shop/[[...slug]].js` | `/shop` | `{ slug: undefined }`
`pages/shop/[[...slug]].js` | `/shop/a` | `{ slug: ['a'] }`
`pages/shop/[[...slug]].js` | `/shop/a/b` | `{ slug: ['a', 'b'] }`
`pages/shop/[[...slug]].js` | `/shop/a/b/c` | `{ slug: ['a', 'b', 'c'] }`
