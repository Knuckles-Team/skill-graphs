## Usage[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#usage)
### Basic setup[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#basic-setup)
To use `cacheLife`, first enable the [`cacheComponents` flag](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents) in your `next.config.js` file:
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  cacheComponents: true,
}

export default nextConfig
```

`cacheLife` requires the `use cache` directive, which must be placed at the file level or at the top of an async function or component.
> **Good to know** :
>   * If used, `cacheLife` should be placed within the function whose output is being cached, even when the `use cache` directive is at file level
>   * Only one `cacheLife` call should execute per function invocation. You can call `cacheLife` in different control flow branches, but ensure only one executes per run. See the [conditional cache lifetimes](https://nextjs.org/docs/app/api-reference/functions/cacheLife#conditional-cache-lifetimes) example
>

### Using preset profiles[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#using-preset-profiles)
Next.js provides preset cache profiles that cover common caching needs. Each profile balances three factors:
  * How long users see cached content without checking for updates (client-side)
  * How often fresh content is generated on the server
  * When old content expires completely


Choose a profile based on how frequently your content changes:
  * **`seconds`**- Real-time data (stock prices, live scores)
  * **`minutes`**- Frequently updated (social feeds, news)
  * **`hours`**- Multiple daily updates (product inventory, weather)
  * **`days`**- Daily updates (blog posts, articles)
  * **`weeks`**- Weekly updates (podcasts, newsletters)
  * **`max`**- Rarely changes (legal pages, archived content)


Import `cacheLife` and pass a profile name:
app/blog/page.tsx
```
'use cache'
import { cacheLife } from 'next/cache'

export default async function BlogPage() {
  cacheLife('days') // Blog content updated daily

  const posts = await getBlogPosts()
  return <div>{/* render posts */}</div>
}
```

The profile name tells Next.js how to cache the entire function's output. If you don't call `cacheLife`, the `default` profile is used. See [preset cache profiles](https://nextjs.org/docs/app/api-reference/functions/cacheLife#preset-cache-profiles) for timing details.
