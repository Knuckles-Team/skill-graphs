## Returns[](https://nextjs.org/docs/community/rspack#returns)
`useParams` returns an object containing the current route's filled in [dynamic parameters](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes), or `null` during [pre-rendering](https://nextjs.org/docs/community/rspack#behavior-during-pre-rendering).
  * Each property in the object is an active dynamic segment.
  * The property name is the segment's name, and the property value is what the segment is filled in with.
  * The property value will either be a `string` or array of `string`s depending on the [type of dynamic segment](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes).
  * If the route contains no dynamic parameters, `useParams` returns an empty object.


For example:
Route | URL | `useParams()`
---|---|---
`pages/shop/page.js` | `/shop` | `{}`
`pages/shop/[slug].js` | `/shop/1` | `{ slug: '1' }`
`pages/shop/[tag]/[item].js` | `/shop/1/2` | `{ tag: '1', item: '2' }`
`pages/shop/[...slug].js` | `/shop/1/2` | `{ slug: ['1', '2'] }`
> **Good to know** : `useParams` is a
