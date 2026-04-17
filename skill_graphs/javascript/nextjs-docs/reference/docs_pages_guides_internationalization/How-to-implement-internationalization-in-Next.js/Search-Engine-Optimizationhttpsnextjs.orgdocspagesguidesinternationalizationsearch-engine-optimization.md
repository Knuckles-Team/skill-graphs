## Search Engine Optimization[](https://nextjs.org/docs/pages/guides/internationalization#search-engine-optimization)
Since Next.js knows what language the user is visiting it will automatically add the `lang` attribute to the `<html>` tag.
Next.js doesn't know about variants of a page so it's up to you to add the `hreflang` meta tags using [`next/head`](https://nextjs.org/docs/pages/api-reference/components/head). You can learn more about `hreflang` in the
