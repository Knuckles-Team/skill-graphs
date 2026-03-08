# viewTransition
This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on
Last updated February 27, 2026
`viewTransition` is an experimental flag that enables the new
To enable this feature, you need to set the `viewTransition` property to `true` in your `next.config.js` file.
next.config.js
```
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    viewTransition: true,
  },
}

module.exports = nextConfig
```

> Important Notice: The `<ViewTransition>` Component is already available in React's Canary release channel. `experimental.viewTransition` is only required to enable deeper integration with Next.js features e.g. automatically
