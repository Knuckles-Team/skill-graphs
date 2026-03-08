## Adding a trailing slash[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/exportPathMap#adding-a-trailing-slash)
It is possible to configure Next.js to export pages as `index.html` files and require trailing slashes, `/about` becomes `/about/index.html` and is routable via `/about/`. This was the default behavior prior to Next.js 9.
To switch back and add a trailing slash, open `next.config.js` and enable the `trailingSlash` config:
next.config.js
```
module.exports = {
  trailingSlash: true,
}
```
