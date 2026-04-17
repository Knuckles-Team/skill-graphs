## 404 Page[](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#404-page)
A 404 page may be accessed very often. Server-rendering an error page for every visit increases the load of the Next.js server. This can result in increased costs and slow experiences.
To avoid the above pitfalls, Next.js provides a static 404 page by default without having to add any additional files.
### Customizing The 404 Page[](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#customizing-the-404-page)
To create a custom 404 page you can create a `pages/404.js` file. This file is statically generated at build time.
pages/404.js
```
export default function Custom404() {
  return <h1>404 - Page Not Found</h1>
}
```

> **Good to know** : You can use [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props) inside this page if you need to fetch data at build time.
