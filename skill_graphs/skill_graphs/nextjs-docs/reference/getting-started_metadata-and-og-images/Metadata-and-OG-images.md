# Metadata and OG images
Last updated February 27, 2026
The Metadata APIs can be used to define your application metadata for improved SEO and web shareability and include:
  1. [The static `metadata` object](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#static-metadata)
  2. [The dynamic `generateMetadata` function](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#generated-metadata)
  3. Special [file conventions](https://nextjs.org/docs/app/api-reference/file-conventions/metadata) that can be used to add static or dynamically generated [favicons](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#favicons) and [OG images](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#static-open-graph-images).


With all the options above, Next.js will automatically generate the relevant `<head>` tags for your page, which can be inspected in the browser's developer tools.
The `metadata` object and `generateMetadata` function exports are only supported in Server Components.
