## Returns[](https://nextjs.org/docs/app/api-reference/functions/use-params#returns)
`useParams` returns an object containing the current route's filled in [dynamic parameters](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes).
  * Each property in the object is an active dynamic segment.
  * The properties name is the segment's name, and the properties value is what the segment is filled in with.
  * The properties value will either be a `string` or array of `string`'s depending on the [type of dynamic segment](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes).
  * If the route contains no dynamic parameters, `useParams` returns an empty object.
  * If used in Pages Router, `useParams` will return `null` on the initial render and updates with properties following the rules above once the router is ready.


For example:
Route | URL | `useParams()`
---|---|---
`app/shop/page.js` | `/shop` | `{}`
`app/shop/[slug]/page.js` | `/shop/1` | `{ slug: '1' }`
`app/shop/[tag]/[item]/page.js` | `/shop/1/2` | `{ tag: '1', item: '2' }`
`app/shop/[...slug]/page.js` | `/shop/1/2` | `{ slug: ['1', '2'] }`
