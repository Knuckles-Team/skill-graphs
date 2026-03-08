## Locale Strategies[](https://nextjs.org/docs/pages/guides/internationalization#locale-strategies)
There are two locale handling strategies: Sub-path Routing and Domain Routing.
### Sub-path Routing[](https://nextjs.org/docs/pages/guides/internationalization#sub-path-routing)
Sub-path Routing puts the locale in the url path.
next.config.js
```
module.exports = {
  i18n: {
    locales: ['en-US', 'fr', 'nl-NL'],
    defaultLocale: 'en-US',
  },
}
```

With the above configuration `en-US`, `fr`, and `nl-NL` will be available to be routed to, and `en-US` is the default locale. If you have a `pages/blog.js` the following urls would be available:
  * `/blog`
  * `/fr/blog`
  * `/nl-nl/blog`


The default locale does not have a prefix.
### Domain Routing[](https://nextjs.org/docs/pages/guides/internationalization#domain-routing)
By using domain routing you can configure locales to be served from different domains:
next.config.js
```
module.exports = {
  i18n: {
    locales: ['en-US', 'fr', 'nl-NL', 'nl-BE'],
    defaultLocale: 'en-US',

    domains: [
      {
        // Note: subdomains must be included in the domain value to be matched
        // e.g. www.example.com should be used if that is the expected hostname
        domain: 'example.com',
        defaultLocale: 'en-US',
      },
      {
        domain: 'example.fr',
        defaultLocale: 'fr',
      },
      {
        domain: 'example.nl',
        defaultLocale: 'nl-NL',
        // specify other locales that should be redirected
        // to this domain
        locales: ['nl-BE'],
      },
    ],
  },
}
```

For example if you have `pages/blog.js` the following urls will be available:
  * `example.com/blog`
  * `www.example.com/blog`
  * `example.fr/blog`
  * `example.nl/blog`
  * `example.nl/nl-BE/blog`
