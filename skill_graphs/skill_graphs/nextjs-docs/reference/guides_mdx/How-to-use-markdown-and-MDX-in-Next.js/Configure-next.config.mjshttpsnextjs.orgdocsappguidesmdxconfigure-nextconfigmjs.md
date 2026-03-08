## Configure `next.config.mjs`[](https://nextjs.org/docs/app/guides/mdx#configure-nextconfigmjs)
Update the `next.config.mjs` file at your project's root to configure it to use MDX:
next.config.mjs
```
import createMDX from '@next/mdx'

/** @type {import('next').NextConfig} */
const nextConfig = {
  // Configure `pageExtensions` to include markdown and MDX files
  pageExtensions: ['js', 'jsx', 'md', 'mdx', 'ts', 'tsx'],
  // Optionally, add any other Next.js config below
}

const withMDX = createMDX({
  // Add markdown plugins here, as desired
})

// Merge MDX config with Next.js config
export default withMDX(nextConfig)
```

This allows `.mdx` files to act as pages, routes, or imports in your application.
### Handling `.md` files[](https://nextjs.org/docs/app/guides/mdx#handling-md-files)
By default, `next/mdx` only compiles files with the `.mdx` extension. To handle `.md` files with webpack, update the `extension` option:
next.config.mjs
```
const withMDX = createMDX({
  extension: /\.(md|mdx)$/,
})
```
