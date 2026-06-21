## Usage[](https://nextjs.org/docs/app/api-reference/config/next-config-js/taint#usage)
The `taint` option enables support for experimental React APIs for tainting objects and values. This feature helps prevent sensitive data from being accidentally passed to the client. When enabled, you can use:
> **Good to know** : Activating this flag also enables the React `experimental` channel for `app` directory.
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    taint: true,
  },
}

export default nextConfig
```

> **Warning:** Do not rely on the taint API as your only mechanism to prevent exposing sensitive data to the client. See our [security recommendations](https://nextjs.org/blog/security-nextjs-server-components-actions).
The taint APIs allows you to be defensive, by declaratively and explicitly marking data that is not allowed to pass through the Server-Client boundary. When an object or value, is passed through the Server-Client boundary, React throws an error.
This is helpful for cases where:
  * The methods to read data are out of your control
  * You have to work with sensitive data shapes not defined by you
  * Sensitive data is accessed during Server Component rendering


It is recommended to model your data and APIs so that sensitive data is not returned to contexts where it is not needed.
