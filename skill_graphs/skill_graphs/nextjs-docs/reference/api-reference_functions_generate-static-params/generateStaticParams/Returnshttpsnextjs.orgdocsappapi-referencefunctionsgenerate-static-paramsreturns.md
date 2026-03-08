## Returns[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#returns)
`generateStaticParams` should return an array of objects where each object represents the populated dynamic segments of a single route.
  * Each property in the object is a dynamic segment to be filled in for the route.
  * The properties name is the segment's name, and the properties value is what that segment should be filled in with.


Example Route |  `generateStaticParams` Return Type
---|---
`/product/[id]` | `{ id: string }[]`
`/products/[category]/[product]` | `{ category: string, product: string }[]`
`/products/[...slug]` | `{ slug: string[] }[]`
