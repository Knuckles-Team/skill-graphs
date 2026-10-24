## Behavior[](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#behavior)
By default, Next.js keeps track of the active _state_ (or subpage) for each slot. However, the content rendered within a slot will depend on the type of navigation:
  * [**Soft Navigation**](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions): During client-side navigation, Next.js will perform a [partial render](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions), changing the subpage within the slot, while maintaining the other slot's active subpages, even if they don't match the current URL.
  * **Hard Navigation** : After a full-page load (browser refresh), Next.js cannot determine the active state for the slots that don't match the current URL. Instead, it will render a [`default.js`](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#defaultjs) file for the unmatched slots, or `404` if `default.js` doesn't exist.


> **Good to know** :
>   * The `404` for unmatched routes helps ensure that you don't accidentally render a parallel route on a page that it was not intended for.
>
