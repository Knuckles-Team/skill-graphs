## How does this work with Static Generation?[](https://nextjs.org/docs/pages/guides/internationalization#how-does-this-work-with-static-generation)
> Note that Internationalized Routing does not integrate with [`output: 'export'`](https://nextjs.org/docs/pages/guides/static-exports) as it does not leverage the Next.js routing layer. Hybrid Next.js applications that do not use `output: 'export'` are fully supported.
### Dynamic Routes and `getStaticProps` Pages[](https://nextjs.org/docs/pages/guides/internationalization#dynamic-routes-and-getstaticprops-pages)
For pages using `getStaticProps` with [Dynamic Routes](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes), all locale variants of the page desired to be prerendered need to be returned from [`getStaticPaths`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths). Along with the `params` object returned for `paths`, you can also return a `locale` field specifying which locale you want to render. For example:
pages/blog/[slug].js
```
export const getStaticPaths = ({ locales }) => {
  return {
    paths: [
      // if no `locale` is provided only the defaultLocale will be generated
      { params: { slug: 'post-1' }, locale: 'en-US' },
      { params: { slug: 'post-1' }, locale: 'fr' },
    ],
    fallback: true,
  }
}
```

For [Automatically Statically Optimized](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization) and non-dynamic `getStaticProps` pages, **a version of the page will be generated for each locale**. This is important to consider because it can increase build times depending on how many locales are configured inside `getStaticProps`.
For example, if you have 50 locales configured with 10 non-dynamic pages using `getStaticProps`, this means `getStaticProps` will be called 500 times. 50 versions of the 10 pages will be generated during each build.
To decrease the build time of dynamic pages with `getStaticProps`, use a [`fallback` mode](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-true). This allows you to return only the most popular paths and locales from `getStaticPaths` for prerendering during the build. Then, Next.js will build the remaining pages at runtime as they are requested.
### Automatically Statically Optimized Pages[](https://nextjs.org/docs/pages/guides/internationalization#automatically-statically-optimized-pages)
For pages that are [automatically statically optimized](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization), a version of the page will be generated for each locale.
### Non-dynamic getStaticProps Pages[](https://nextjs.org/docs/pages/guides/internationalization#non-dynamic-getstaticprops-pages)
For non-dynamic `getStaticProps` pages, a version is generated for each locale like above. `getStaticProps` is called with each `locale` that is being rendered. If you would like to opt-out of a certain locale from being pre-rendered, you can return `notFound: true` from `getStaticProps` and this variant of the page will not be generated.
```
export async function getStaticProps({ locale }) {
  // Call an external API endpoint to get posts.
  // You can use any data fetching library
  const res = await fetch(`https://.../posts?locale=${locale}`)
  const posts = await res.json()

  if (posts.length === 0) {
    return {
      notFound: true,
    }
  }

  // By returning { props: posts }, the Blog component
  // will receive `posts` as a prop at build time
  return {
    props: {
      posts,
    },
  }
}
```
