## Props[](https://nextjs.org/docs/app/api-reference/file-conventions/template#props)
###  `children` (required)[](https://nextjs.org/docs/app/api-reference/file-conventions/template#children-required)
Template accepts a `children` prop.
Output
```
<Layout>
  {/* Note that the template is automatically given a unique key. */}
  <Template key={routeParam}>{children}</Template>
</Layout>
```
