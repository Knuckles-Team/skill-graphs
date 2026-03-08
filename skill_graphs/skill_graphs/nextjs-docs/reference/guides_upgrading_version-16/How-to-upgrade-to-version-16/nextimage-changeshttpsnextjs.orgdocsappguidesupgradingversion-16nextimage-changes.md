##  `next/image` changes[](https://nextjs.org/docs/app/guides/upgrading/version-16#nextimage-changes)
### Local Images with Query Strings (Breaking change)[](https://nextjs.org/docs/app/guides/upgrading/version-16#local-images-with-query-strings-breaking-change)
Local image sources with query strings now require `images.localPatterns.search` configuration to prevent enumeration attacks.
app/page.tsx
```
import Image from 'next/image'

export default function Page() {
  return <Image src="/assets/photo?v=1" alt="Photo" width="100" height="100" />
}
```

If you need to use query strings with local images, add the pattern to your configuration:
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  images: {
    localPatterns: [
      {
        pathname: '/assets/**',
        search: '?v=1',
      },
    ],
  },
}

export default nextConfig
```

###  `minimumCacheTTL` Default (Breaking change)[](https://nextjs.org/docs/app/guides/upgrading/version-16#minimumcachettl-default-breaking-change)
The default value for `images.minimumCacheTTL` has changed from `60 seconds` to `4 hours` (14400 seconds). This reduces revalidation cost for images without cache-control headers.
For some Next.js users, image revalidation was happening frequently, often because the upstream source images missed a `cache-control` header. This caused revalidation to happen every `60` seconds, which increased CPU usage and cost.
Since most images do not change often, this short interval is not ideal. Setting the default to 4 hours offers a more durable cache by default, while still allowing images to update a few times per day if needed.
If you need the previous behavior, change `minimumCacheTTL` to a lower value, for example back to `60` seconds:
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  images: {
    minimumCacheTTL: 60,
  },
}

export default nextConfig
```

###  `imageSizes` Default (Breaking change)[](https://nextjs.org/docs/app/guides/upgrading/version-16#imagesizes-default-breaking-change)
The value `16` has been removed from the default `images.imageSizes` array.
We have looked at request analytics and found out that very few projects ever serve 16 pixels width images. Removing this setting reduces the size of the `srcset` attribute shipped to the browser by `next/image`.
If you need to support 16px images:
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  images: {
    imageSizes: [16, 32, 48, 64, 96, 128, 256, 384],
  },
}

export default nextConfig
```

Rather than lack of developer usage, we believe 16 pixels width images have become less common, because `devicePixelRatio: 2` actually fetches a 32px image to prevent blurriness in retina displays.
###  `qualities` Default (Breaking change)[](https://nextjs.org/docs/app/guides/upgrading/version-16#qualities-default-breaking-change)
The default value for `images.qualities` has changed from allowing all qualities to only `[75]`.
If you need to support multiple quality levels:
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  images: {
    qualities: [50, 75, 100],
  },
}

export default nextConfig
```

If you specify a `quality` prop not included in the `image.qualities` array, the quality will be coerced to the closest value in `images.qualities`. For example, given the configuration above, a `quality` prop of 80, is coerced to 75.
### Local IP Restriction (Breaking change)[](https://nextjs.org/docs/app/guides/upgrading/version-16#local-ip-restriction-breaking-change)
A new security restriction blocks local IP optimization by default. Set `images.dangerouslyAllowLocalIP` to `true` only for private networks.
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  images: {
    dangerouslyAllowLocalIP: true, // Only for private networks
  },
}

export default nextConfig
```

### Maximum Redirects (Breaking change)[](https://nextjs.org/docs/app/guides/upgrading/version-16#maximum-redirects-breaking-change)
The default for `images.maximumRedirects` has changed from unlimited to 3 redirects maximum.
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  images: {
    maximumRedirects: 0, // Disable redirects
    // or
    maximumRedirects: 5, // Increase for edge cases
  },
}

export default nextConfig
```

###  `next/legacy/image` Component (deprecated)[](https://nextjs.org/docs/app/guides/upgrading/version-16#nextlegacyimage-component-deprecated)
The `next/legacy/image` component is deprecated. Use `next/image` instead:
```
// Before
import Image from 'next/legacy/image'

// After
import Image from 'next/image'
```

###  `images.domains` Configuration (deprecated)[](https://nextjs.org/docs/app/guides/upgrading/version-16#imagesdomains-configuration-deprecated)
The `images.domains` config is deprecated.
next.config.js
```
// image.domains is deprecated
module.exports = {
  images: {
    domains: ['example.com'],
  },
}
```

Use `images.remotePatterns` instead for improved security:
next.config.js
```
// Use image.remotePatterns instead
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'example.com',
      },
    ],
  },
}
```
