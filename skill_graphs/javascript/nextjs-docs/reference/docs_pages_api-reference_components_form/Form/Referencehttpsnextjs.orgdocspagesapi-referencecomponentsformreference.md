## Reference[](https://nextjs.org/docs/pages/api-reference/components/form#reference)
The behavior of the `<Form>` component depends on whether the `action` prop is passed a `string` or `function`.
  * When `action` is a **string** , the `<Form>` behaves like a native HTML form that uses a **`GET`**method. The form data is encoded into the URL as search params, and when the form is submitted, it navigates to the specified URL. In addition, Next.js:
    * Performs a [client-side navigation](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions) instead of a full page reload when the form is submitted. This retains shared UI and client-side state.


###  `action` (string) Props[](https://nextjs.org/docs/pages/api-reference/components/form#action-string-props)
When `action` is a string, the `<Form>` component supports the following props:
Prop | Example | Type | Required
---|---|---|---
`action` | `action="/search"` |  `string` (URL or relative path) | Yes
`replace` | `replace={false}` | `boolean` | -
`scroll` | `scroll={true}` | `boolean` | -
  * **`action`**: The URL or path to navigate to when the form is submitted.
    * An empty string `""` will navigate to the same route with updated search params.
  * **`replace`**: Replaces the current history state instead of pushing a new one to the`false`.
  * **`scroll`**: Controls the scroll behavior during navigation. Defaults to`true` , this means it will scroll to the top of the new route, and maintain the scroll position for backwards and forwards navigation.


### Caveats[](https://nextjs.org/docs/pages/api-reference/components/form#caveats)
  * **`onSubmit`**: Can be used to handle form submission logic. However, calling`event.preventDefault()` will override `<Form>` behavior such as navigating to the specified URL.
  * `<Form>` behavior.
    * Similarly, `formMethod`, `formEncType`, and `formTarget` can be used to override the `method`, `encType`, and `target` props respectively, and using them will fallback to native browser behavior.
    * If you need to use these props, use the HTML `<form>` element instead.
  * **`<input type="file">`**: Using this input type when the`action` is a string will match browser behavior by submitting the filename instead of the file object.


Was this helpful?
Send
* * *
* * *
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Next.js Conf](https://nextjs.org/conf)[Evals](https://nextjs.org/evals)
#### More
[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)
#### About Vercel
#### Legal
Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
* * *
* * *
