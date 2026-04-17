## Examples[](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes#examples)
### Modals[](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes#modals)
Intercepting Routes can be used together with [Parallel Routes](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes) to create modals. This allows you to solve common challenges when building modals, such as:
  * Making the modal content **shareable through a URL**.
  * **Preserving context** when the page is refreshed, instead of closing the modal.
  * **Closing the modal on backwards navigation** rather than going to the previous route.
  * **Reopening the modal on forwards navigation**.


Consider the following UI pattern, where a user can open a photo modal from a gallery using client-side navigation, or navigate to the photo page directly from a shareable URL:
![Intercepting routes modal example](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fintercepted-routes-modal-example.png&w=3840&q=75)![Intercepting routes modal example](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fintercepted-routes-modal-example.png&w=3840&q=75)
In the above example, the path to the `photo` segment can use the `(..)` matcher since `@modal` is a slot and **not** a segment. This means that the `photo` route is only one segment level higher, despite being two file-system levels higher.
See the [Parallel Routes](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#modals) documentation for a step-by-step example, or see our
> **Good to know:**
>   * Other examples could include opening a login modal in a top navbar while also having a dedicated `/login` page, or opening a shopping cart in a side modal.
>
