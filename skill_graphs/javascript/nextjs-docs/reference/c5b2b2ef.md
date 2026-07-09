# generateViewport
Last updated February 27, 2026
You can customize the initial viewport of the page with the static `viewport` object or the dynamic `generateViewport` function.
> **Good to know** :
>   * The `viewport` object and `generateViewport` function exports are **only supported in Server Components**.
>   * You cannot export both the `viewport` object and `generateViewport` function from the same route segment.
>   * If you're coming from migrating `metadata` exports, you can use [metadata-to-viewport-export codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#metadata-to-viewport-export) to update your changes.
>
