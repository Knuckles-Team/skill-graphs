# Metadata Files API Reference
Last updated February 27, 2026
This section of the docs covers **Metadata file conventions**. File-based metadata can be defined by adding special metadata files to route segments.
Each file convention can be defined using a static file (e.g. `opengraph-image.jpg`), or a dynamic variant that uses code to generate the file (e.g. `opengraph-image.js`).
Once a file is defined, Next.js will automatically serve the file (with hashes in production for caching) and update the relevant head elements with the correct metadata, such as the asset's URL, file type, and image size.
> **Good to know** :
>   * Special Route Handlers like [`sitemap.ts`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap), [`opengraph-image.tsx`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image), and [`icon.tsx`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons), and other [metadata files](https://nextjs.org/docs/app/api-reference/file-conventions/metadata) are cached by default.
>   * If using along with [`proxy.ts`](https://nextjs.org/docs/app/api-reference/file-conventions/proxy), [configure the matcher](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#matcher) to exclude the metadata files.
>

### [favicon, icon, and apple-icon API Reference for the Favicon, Icon and Apple Icon file conventions.](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons)### [manifest.json API Reference for manifest.json file.](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest)### [opengraph-image and twitter-image API Reference for the Open Graph Image and Twitter Image file conventions.](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image)### [robots.txt API Reference for robots.txt file.](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots)### [sitemap.xml API Reference for the sitemap.xml file.](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap)
[Previousunauthorized.js](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized)[Nextfavicon, icon, and apple-icon](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons)
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
