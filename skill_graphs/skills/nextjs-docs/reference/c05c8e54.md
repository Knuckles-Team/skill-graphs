# reactStrictMode
Last updated February 27, 2026
> **Good to know** : Since Next.js 13.5.1, Strict Mode is `true` by default with `app` router, so the above configuration is only necessary for `pages`. You can still disable Strict Mode by setting `reactStrictMode: false`.
> **Suggested** : We strongly suggest you enable Strict Mode in your Next.js application to better prepare your application for the future of React.
React's
The Next.js runtime is Strict Mode-compliant. To opt-in to Strict Mode, configure the following option in your `next.config.js`:
next.config.js
```
module.exports = {
  reactStrictMode: true,
}
```

If you or your team are not ready to use Strict Mode in your entire application, that's OK! You can incrementally migrate on a page-by-page basis using `<React.StrictMode>`.
[PreviousreactMaxHeadersLength](https://nextjs.org/docs/app/api-reference/config/next-config-js/reactMaxHeadersLength)[Nextredirects](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects)
Was this helpful?
Send
