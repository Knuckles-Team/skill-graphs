## Reference[](https://nextjs.org/docs/app/api-reference/components/form#reference)
The behavior of the `<Form>` component depends on whether the `action` prop is passed a `string` or `function`.
  * When `action` is a **string** , the `<Form>` behaves like a native HTML form that uses a **`GET`**method. The form data is encoded into the URL as search params, and when the form is submitted, it navigates to the specified URL. In addition, Next.js:
    * [Prefetches](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching) the path when the form becomes visible, this preloads shared UI (e.g. `layout.js` and `loading.js`), resulting in faster navigation.
    * Performs a [client-side navigation](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions) instead of a full page reload when the form is submitted. This retains shared UI and client-side state.
  * When `action` is a **function** (Server Action), `<Form>` behaves like a


###  `action` (string) Props[](https://nextjs.org/docs/app/api-reference/components/form#action-string-props)
When `action` is a string, the `<Form>` component supports the following props:
Prop | Example | Type | Required
---|---|---|---
`action` | `action="/search"` |  `string` (URL or relative path) | Yes
`replace` | `replace={false}` | `boolean` | -
`scroll` | `scroll={true}` | `boolean` | -
`prefetch` | `prefetch={true}` | `boolean` | -
  * **`action`**: The URL or path to navigate to when the form is submitted.
    * An empty string `""` will navigate to the same route with updated search params.
  * **`replace`**: Replaces the current history state instead of pushing a new one to the`false`.
  * **`scroll`**: Controls the scroll behavior during navigation. Defaults to`true` , this means it will scroll to the top of the new route, and maintain the scroll position for backwards and forwards navigation.
  * **`prefetch`**: Controls whether the path should be prefetched when the form becomes visible in the user's viewport. Defaults to`true`.


###  `action` (function) Props[](https://nextjs.org/docs/app/api-reference/components/form#action-function-props)
When `action` is a function, the `<Form>` component supports the following prop:
Prop | Example | Type | Required
---|---|---|---
`action` | `action={myAction}` |  `function` (Server Action) | Yes
  * **`action`**: The Server Action to be called when the form is submitted. See the


> **Good to know** : When `action` is a function, the `replace` and `scroll` props are ignored.
### Caveats[](https://nextjs.org/docs/app/api-reference/components/form#caveats)
  * **`formAction`**: Can be used in a`<button>` or `<input type="submit">` fields to override the `action` prop. Next.js will perform a client-side navigation, however, this approach doesn't support prefetching.
    * When using [`basePath`](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath), you must also include it in the `formAction` path. e.g. `formAction="/base-path/search"`.
  * **`key`**: Passing a`key` prop to a string `action` is not supported. If you'd like to trigger a re-render or perform a mutation, consider using a function `action` instead.


  * **`onSubmit`**: Can be used to handle form submission logic. However, calling`event.preventDefault()` will override `<Form>` behavior such as navigating to the specified URL.
  * `<Form>` behavior.
    * Similarly, `formMethod`, `formEncType`, and `formTarget` can be used to override the `method`, `encType`, and `target` props respectively, and using them will fallback to native browser behavior.
    * If you need to use these props, use the HTML `<form>` element instead.
  * **`<input type="file">`**: Using this input type when the`action` is a string will match browser behavior by submitting the filename instead of the file object.
