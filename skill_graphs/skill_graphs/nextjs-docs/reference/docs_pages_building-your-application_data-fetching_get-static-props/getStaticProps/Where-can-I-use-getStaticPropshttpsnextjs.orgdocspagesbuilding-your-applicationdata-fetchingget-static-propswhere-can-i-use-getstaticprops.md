## Where can I use getStaticProps[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props#where-can-i-use-getstaticprops)
`getStaticProps` can only be exported from a **page**. You **cannot** export it from non-page files, `_app`, `_document`, or `_error`.
One of the reasons for this restriction is that React needs to have all the required data before the page is rendered.
Also, you must use export `getStaticProps` as a standalone function — it will **not** work if you add `getStaticProps` as a property of the page component.
> **Good to know** : if you have created a [custom app](https://nextjs.org/docs/pages/building-your-application/routing/custom-app), ensure you are passing the `pageProps` to the page component as shown in the linked document, otherwise the props will be empty.
