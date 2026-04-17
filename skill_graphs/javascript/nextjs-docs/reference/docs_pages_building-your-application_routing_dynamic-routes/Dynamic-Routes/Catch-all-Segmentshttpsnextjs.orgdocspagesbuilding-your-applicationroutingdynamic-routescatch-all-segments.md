## Catch-all Segments[](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#catch-all-segments)
Dynamic Segments can be extended to **catch-all** subsequent segments by adding an ellipsis inside the brackets `[...segmentName]`.
For example, `pages/shop/[...slug].js` will match `/shop/clothes`, but also `/shop/clothes/tops`, `/shop/clothes/tops/t-shirts`, and so on.
Route | Example URL | `params`
---|---|---
`pages/shop/[...slug].js` | `/shop/a` | `{ slug: ['a'] }`
`pages/shop/[...slug].js` | `/shop/a/b` | `{ slug: ['a', 'b'] }`
`pages/shop/[...slug].js` | `/shop/a/b/c` | `{ slug: ['a', 'b', 'c'] }`
