## Configuration Options[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#configuration-options)
### Remote Patterns[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#remote-patterns)
To protect your application from malicious users, configuration is required in order to use external images. This ensures that only external images from your account can be served from the Next.js Image Optimization API. These external images can be configured with the `remotePatterns` property in your `next.config.js` file, as shown below:
next.config.js
```
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'example.com',
        port: '',
        pathname: '/account123/**',
        search: '',
      },
    ],
  },
}
```

> **Good to know** : The example above will ensure the `src` property of `next/legacy/image` must start with `https://example.com/account123/` and must not have a query string. Any other protocol, hostname, port, or unmatched path will respond with 400 Bad Request.
Below is an example of the `remotePatterns` property in the `next.config.js` file using a wildcard pattern in the `hostname`:
next.config.js
```
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: '**.example.com',
        port: '',
        search: '',
      },
    ],
  },
}
```

> **Good to know** : The example above will ensure the `src` property of `next/legacy/image` must start with `https://img1.example.com` or `https://me.avatar.example.com` or any number of subdomains. It cannot have a port or query string. Any other protocol or unmatched hostname will respond with 400 Bad Request.
Wildcard patterns can be used for both `pathname` and `hostname` and have the following syntax:
  * `*` match a single path segment or subdomain
  * `**` match any number of path segments at the end or subdomains at the beginning


The `**` syntax does not work in the middle of the pattern.
> **Good to know** : When omitting `protocol`, `port`, `pathname`, or `search` then the wildcard `**` is implied. This is not recommended because it may allow malicious actors to optimize urls you did not intend.
Below is an example of the `remotePatterns` property in the `next.config.js` file using `search`:
next.config.js
```
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'assets.example.com',
        search: '?v=1727111025337',
      },
    ],
  },
}
```

> **Good to know** : The example above will ensure the `src` property of `next/legacy/image` must start with `https://assets.example.com` and must have the exact query string `?v=1727111025337`. Any other protocol or query string will respond with 400 Bad Request.
### Domains[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#domains)
> **Warning** : Deprecated since Next.js 14 in favor of strict [`remotePatterns`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#remote-patterns) in order to protect your application from malicious users. Only use `domains` if you own all the content served from the domain.
Similar to [`remotePatterns`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#remote-patterns), the `domains` configuration can be used to provide a list of allowed hostnames for external images.
However, the `domains` configuration does not support wildcard pattern matching and it cannot restrict protocol, port, or pathname.
Below is an example of the `domains` property in the `next.config.js` file:
next.config.js
```
module.exports = {
  images: {
    domains: ['assets.acme.com'],
  },
}
```

### Loader Configuration[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader-configuration)
If you want to use a cloud provider to optimize images instead of using the Next.js built-in Image Optimization API, you can configure the `loader` and `path` prefix in your `next.config.js` file. This allows you to use relative URLs for the Image [`src`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#src) and automatically generate the correct absolute URL for your provider.
next.config.js
```
module.exports = {
  images: {
    loader: 'imgix',
    path: 'https://example.com/myaccount/',
  },
}
```

#### Customizing the Built-in Image Path[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#customizing-the-built-in-image-path)
If you want to change or prefix the default path for the built-in Next.js image optimization, you can do so with the `path` property. The default value for `path` is `/_next/image`.
next.config.js
```
module.exports = {
  images: {
    path: '/my-prefix/_next/image',
  },
}
```

### Built-in Loaders[](https://nextjs.org/docs/pages/api-reference/components/image-legacy#built-in-loaders)
The following Image Optimization cloud providers are included:
  * Default: Works automatically with `next dev`, `next start`, or a custom server
  * `loader: 'imgix'`
  * `loader: 'cloudinary'`
  * `loader: 'akamai'`
  * Custom: `loader: 'custom'` use a custom cloud provider by implementing the [`loader`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader) prop on the `next/legacy/image` component


If you need a different provider, you can use the [`loader`](https://nextjs.org/docs/pages/api-reference/components/image-legacy#loader) prop with `next/legacy/image`.
> Images cannot be optimized at build time using [`output: 'export'`](https://nextjs.org/docs/pages/guides/static-exports), only on-demand. To use `next/legacy/image` with `output: 'export'`, you will need to use a different loader than the default.
