## Accessing the locale information[](https://nextjs.org/docs/pages/guides/internationalization#accessing-the-locale-information)
You can access the locale information via the Next.js router. For example, using the [`useRouter()`](https://nextjs.org/docs/pages/api-reference/functions/use-router) hook the following properties are available:
  * `locale` contains the currently active locale.
  * `locales` contains all configured locales.
  * `defaultLocale` contains the configured default locale.


When [pre-rendering](https://nextjs.org/docs/pages/building-your-application/rendering/static-site-generation) pages with `getStaticProps` or `getServerSideProps`, the locale information is provided in [the context](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props) provided to the function.
When leveraging `getStaticPaths`, the configured locales are provided in the context parameter of the function under `locales` and the configured defaultLocale under `defaultLocale`.
