## Additional Considerations[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#additional-considerations)
### Using a Custom `homepage` in CRA[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#using-a-custom-homepage-in-cra)
If you used the `homepage` field in your CRA `package.json` to serve the app under a specific subpath, you can replicate that in Next.js using the [`basePath` configuration](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath) in `next.config.ts`:
next.config.ts
```
import { NextConfig } from 'next'

const nextConfig: NextConfig = {
  basePath: '/my-subpath',
  // ...
}

export default nextConfig
```

### Handling a Custom `Service Worker`[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#handling-a-custom-service-worker)
If you used CRA’s service worker (e.g., `serviceWorker.js` from `create-react-app`), you can learn how to create [Progressive Web Applications (PWAs)](https://nextjs.org/docs/app/guides/progressive-web-apps) with Next.js.
### Proxying API Requests[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#proxying-api-requests)
If your CRA app used the `proxy` field in `package.json` to forward requests to a backend server, you can replicate this with [Next.js rewrites](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites) in `next.config.ts`:
next.config.ts
```
import { NextConfig } from 'next'

const nextConfig: NextConfig = {
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: 'https://your-backend.com/:path*',
      },
    ]
  },
}
```

### Custom Webpack[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#custom-webpack)
If you had a custom webpack or Babel configuration in CRA, you can extend Next.js’s config in `next.config.ts`:
next.config.ts
```
import { NextConfig } from 'next'

const nextConfig: NextConfig = {
  webpack: (config, { isServer }) => {
    // Modify the webpack config here
    return config
  },
}

export default nextConfig
```

> **Note** : This will require using Webpack by adding `--webpack` to your `dev` script.
### TypeScript Setup[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#typescript-setup)
Next.js automatically sets up TypeScript if you have a `tsconfig.json`. Make sure `next-env.d.ts` is listed in your `tsconfig.json` `include` array:
```
{
  "include": ["next-env.d.ts", "app/**/*", "src/**/*"]
}
```
