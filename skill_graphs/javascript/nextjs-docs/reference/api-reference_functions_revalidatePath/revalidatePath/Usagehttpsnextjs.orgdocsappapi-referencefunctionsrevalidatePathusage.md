## Usage[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#usage)
`revalidatePath` can be called in Server Functions and Route Handlers.
`revalidatePath` cannot be called in Client Components or Proxy, as it only works in server environments.
> **Good to know** :
>   * **Server Functions** : Updates the UI immediately (if viewing the affected path). Currently, it also causes all previously visited pages to refresh when navigated to again. This behavior is temporary and will be updated in the future to apply only to the specific path.
>   * **Route Handlers** : Marks the path for revalidation. The revalidation is done on the next visit to the specified path. This means calling `revalidatePath` with a dynamic route segment will not immediately trigger many revalidations at once. The invalidation only happens when the path is next visited.
>
