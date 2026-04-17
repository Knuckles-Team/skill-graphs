## Parameters[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#parameters)
```
revalidatePath(path: string, type?: 'page' | 'layout'): void;
```

  * `path`: Either a route pattern corresponding to the data you want to revalidate, for example `/product/[slug]`, or a specific URL, `/product/123`. Do not append `/page` or `/layout`, use the `type` parameter instead. Must not exceed 1024 characters. This value is case-sensitive.
  * `type`: (optional) `'page'` or `'layout'` string to change the type of path to revalidate. If `path` contains a dynamic segment, for example `/product/[slug]`, this parameter is required. If `path` is a specific URL, `/product/1`, omit `type`.


Use a specific URL when you want to refresh a [single page](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#revalidating-a-specific-url). Use a route pattern plus `type` to refresh [multiple URLs](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#revalidating-a-page-path).
