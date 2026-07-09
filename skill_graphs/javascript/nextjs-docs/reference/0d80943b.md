## Reference[](https://nextjs.org/docs/app/api-reference/file-conventions/not-found#reference)
### Props[](https://nextjs.org/docs/app/api-reference/file-conventions/not-found#props)
`not-found.js` or `global-not-found.js` components do not accept any props.
> **Good to know** : In addition to catching expected `notFound()` errors, the root `app/not-found.js` and `app/global-not-found.js` files handle any unmatched URLs for your whole application. This means users that visit a URL that is not handled by your app will be shown the exported UI.
