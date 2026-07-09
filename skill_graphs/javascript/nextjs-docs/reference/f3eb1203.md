## Codemods[](https://nextjs.org/docs/app/guides/upgrading/codemods#codemods)
### 16.0[](https://nextjs.org/docs/app/guides/upgrading/codemods#160)
#### Remove `experimental_ppr` Route Segment Config from App Router pages and layouts[](https://nextjs.org/docs/app/guides/upgrading/codemods#remove-experimental_ppr-route-segment-config-from-app-router-pages-and-layouts)
#####  `remove-experimental-ppr`[](https://nextjs.org/docs/app/guides/upgrading/codemods#remove-experimental-ppr)
Terminal
```
npx @next/codemod@latest remove-experimental-ppr .
```

This codemod removes the `experimental_ppr` Route Segment Config from App Router pages and layouts.
app/page.tsx
```
- export const experimental_ppr = true;
```

#### Remove `unstable_` prefix from stabilized API[](https://nextjs.org/docs/app/guides/upgrading/codemods#remove-unstable_-prefix-from-stabilized-api)
#####  `remove-unstable-prefix`[](https://nextjs.org/docs/app/guides/upgrading/codemods#remove-unstable-prefix)
Terminal
```
npx @next/codemod@latest remove-unstable-prefix .
```

This codemod removes the `unstable_` prefix from stabilized API.
For example:
```
import { unstable_cacheTag as cacheTag } from 'next/cache'

cacheTag()
```

Transforms into:
```
import { cacheTag } from 'next/cache'

cacheTag()
```

#### Migrate from deprecated `middleware` convention to `proxy`[](https://nextjs.org/docs/app/guides/upgrading/codemods#migrate-from-deprecated-middleware-convention-to-proxy)
#####  `middleware-to-proxy`[](https://nextjs.org/docs/app/guides/upgrading/codemods#middleware-to-proxy)
Terminal
```
npx @next/codemod@latest middleware-to-proxy .
```

This codemod migrates projects from using the deprecated `middleware` convention to using the `proxy` convention. It:
  * Renames `middleware.<extension>` to `proxy.<extension>` (e.g. `middleware.ts` to `proxy.ts`)
  * Renames named export `middleware` to `proxy`
  * Renames Next.js config property `experimental.middlewarePrefetch` to `experimental.proxyPrefetch`
  * Renames Next.js config property `experimental.middlewareClientMaxBodySize` to `experimental.proxyClientMaxBodySize`
  * Renames Next.js config property `experimental.externalMiddlewareRewritesResolve` to `experimental.externalProxyRewritesResolve`
  * Renames Next.js config property `skipMiddlewareUrlNormalize` to `skipProxyUrlNormalize`


For example:
middleware.ts
```
import { NextResponse } from 'next/server'

export function middleware() {
  return NextResponse.next()
}
```

Transforms into:
proxy.ts
```
import { NextResponse } from 'next/server'

export function proxy() {
  return NextResponse.next()
}
```

#### Migrate from `next lint` to ESLint CLI[](https://nextjs.org/docs/app/guides/upgrading/codemods#migrate-from-next-lint-to-eslint-cli)
#####  `next-lint-to-eslint-cli`[](https://nextjs.org/docs/app/guides/upgrading/codemods#next-lint-to-eslint-cli)
Terminal
```
npx @next/codemod@canary next-lint-to-eslint-cli .
```

This codemod migrates projects from using `next lint` to using the ESLint CLI with your local ESLint config. It:
  * Creates an `eslint.config.mjs` file with Next.js recommended configurations
  * Updates `package.json` scripts to use `eslint .` instead of `next lint`
  * Adds necessary ESLint dependencies to `package.json`
  * Preserves existing ESLint configurations when found


For example:
package.json
```
{
  "scripts": {
    "lint": "next lint"
  }
}
```

Becomes:
package.json
```
{
  "scripts": {
    "lint": "eslint ."
  }
}
```

And creates:
eslint.config.mjs
```
import { dirname } from 'path'
import { fileURLToPath } from 'url'
import { FlatCompat } from '@eslint/eslintrc'

const __filename = fileURLToPath(import.meta.url)
const __dirname = dirname(__filename)

const compat = new FlatCompat({
  baseDirectory: __dirname,
})

const eslintConfig = [
  ...compat.extends('next/core-web-vitals', 'next/typescript'),
  {
    ignores: [
      'node_modules/**',
      '.next/**',
      'out/**',
      'build/**',
      'next-env.d.ts',
    ],
  },
]

export default eslintConfig
```

### 15.0[](https://nextjs.org/docs/app/guides/upgrading/codemods#150)
#### Transform App Router Route Segment Config `runtime` value from `experimental-edge` to `edge`[](https://nextjs.org/docs/app/guides/upgrading/codemods#transform-app-router-route-segment-config-runtime-value-from-experimental-edge-to-edge)
#####  `app-dir-runtime-config-experimental-edge`[](https://nextjs.org/docs/app/guides/upgrading/codemods#app-dir-runtime-config-experimental-edge)
> **Note** : This codemod is App Router specific.
Terminal
```
npx @next/codemod@latest app-dir-runtime-config-experimental-edge .
```

This codemod transforms [Route Segment Config `runtime`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#runtime) value `experimental-edge` to `edge`.
For example:
```
export const runtime = 'experimental-edge'
```

Transforms into:
```
export const runtime = 'edge'
```

#### Migrate to async Dynamic APIs[](https://nextjs.org/docs/app/guides/upgrading/codemods#migrate-to-async-dynamic-apis)
APIs that opted into dynamic rendering that previously supported synchronous access are now asynchronous. You can read more about this breaking change in the [upgrade guide](https://nextjs.org/docs/app/guides/upgrading/version-15).
#####  `next-async-request-api`[](https://nextjs.org/docs/app/guides/upgrading/codemods#next-async-request-api)
Terminal
```
npx @next/codemod@latest next-async-request-api .
```

This codemod will transform dynamic APIs (`cookies()`, `headers()` and `draftMode()` from `next/headers`) that are now asynchronous to be properly awaited or wrapped with `React.use()` if applicable. When an automatic migration isn't possible, the codemod will either add a typecast (if a TypeScript file) or a comment to inform the user that it needs to be manually reviewed & updated.
For example:
```
import { cookies, headers } from 'next/headers'
const token = cookies().get('token')

function useToken() {
  const token = cookies().get('token')
  return token
}

export default function Page() {
  const name = cookies().get('name')
}

function getHeader() {
  return headers().get('x-foo')
}
```

Transforms into:
```
import { use } from 'react'
import {
  cookies,
  headers,
  type UnsafeUnwrappedCookies,
  type UnsafeUnwrappedHeaders,
} from 'next/headers'
const token = (cookies() as unknown as UnsafeUnwrappedCookies).get('token')

function useToken() {
  const token = use(cookies()).get('token')
  return token
}

export default async function Page() {
  const name = (await cookies()).get('name')
}

function getHeader() {
  return (headers() as unknown as UnsafeUnwrappedHeaders).get('x-foo')
}
```

When we detect property access on the `params` or `searchParams` props in the page / route entries (`page.js`, `layout.js`, `route.js`, or `default.js`) or the `generateMetadata` / `generateViewport` APIs, it will attempt to transform the callsite from a sync to an async function, and await the property access. If it can't be made async (such as with a Client Component), it will use `React.use` to unwrap the promise .
For example:
```
// page.tsx
export default function Page({
  params,
  searchParams,
}: {
  params: { slug: string }
  searchParams: { [key: string]: string | string[] | undefined }
}) {
  const { value } = searchParams
  if (value === 'foo') {
    // ...
  }
}

export function generateMetadata({ params }: { params: { slug: string } }) {
  const { slug } = params
  return {
    title: `My Page - ${slug}`,
  }
}
```

Transforms into:
```
// page.tsx
export default async function Page(props: {
  params: Promise<{ slug: string }>
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}) {
  const searchParams = await props.searchParams
  const { value } = searchParams
  if (value === 'foo') {
    // ...
  }
}

export async function generateMetadata(props: {
  params: Promise<{ slug: string }>
}) {
  const params = await props.params
  const { slug } = params
  return {
    title: `My Page - ${slug}`,
  }
}
```

> **Good to know:** When this codemod identifies a spot that might require manual intervention, but we aren't able to determine the exact fix, it will add a comment or typecast to the code to inform the user that it needs to be manually updated. These comments are prefixed with **@next/codemod** , and typecasts are prefixed with `UnsafeUnwrapped`. Your build will error until these comments are explicitly removed. [Read more](https://nextjs.org/docs/messages/sync-dynamic-apis).
#### Replace `geo` and `ip` properties of `NextRequest` with `@vercel/functions`[](https://nextjs.org/docs/app/guides/upgrading/codemods#replace-geo-and-ip-properties-of-nextrequest-with-vercelfunctions)
#####  `next-request-geo-ip`[](https://nextjs.org/docs/app/guides/upgrading/codemods#next-request-geo-ip)
Terminal
```
npx @next/codemod@latest next-request-geo-ip .
```

This codemod installs `@vercel/functions` and transforms `geo` and `ip` properties of `NextRequest` with corresponding `@vercel/functions` features.
For example:
```
import type { NextRequest } from 'next/server'

export function GET(req: NextRequest) {
  const { geo, ip } = req
}
```

Transforms into:
```
import type { NextRequest } from 'next/server'
import { geolocation, ipAddress } from '@vercel/functions'

export function GET(req: NextRequest) {
  const geo = geolocation(req)
  const ip = ipAddress(req)
}
```

### 14.0[](https://nextjs.org/docs/app/guides/upgrading/codemods#140)
#### Migrate `ImageResponse` imports[](https://nextjs.org/docs/app/guides/upgrading/codemods#migrate-imageresponse-imports)
#####  `next-og-import`[](https://nextjs.org/docs/app/guides/upgrading/codemods#next-og-import)
Terminal
```
npx @next/codemod@latest next-og-import .
```

This codemod moves transforms imports from `next/server` to `next/og` for usage of [Dynamic OG Image Generation](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#generated-open-graph-images).
For example:
```
import { ImageResponse } from 'next/server'
```

Transforms into:
```
import { ImageResponse } from 'next/og'
```

#### Use `viewport` export[](https://nextjs.org/docs/app/guides/upgrading/codemods#use-viewport-export)
#####  `metadata-to-viewport-export`[](https://nextjs.org/docs/app/guides/upgrading/codemods#metadata-to-viewport-export)
Terminal
```
npx @next/codemod@latest metadata-to-viewport-export .
```

This codemod migrates certain viewport metadata to `viewport` export.
For example:
```
export const metadata = {
  title: 'My App',
  themeColor: 'dark',
  viewport: {
    width: 1,
  },
}
```

Transforms into:
```
export const metadata = {
  title: 'My App',
}

export const viewport = {
  width: 1,
  themeColor: 'dark',
}
```

### 13.2[](https://nextjs.org/docs/app/guides/upgrading/codemods#132)
#### Use Built-in Font[](https://nextjs.org/docs/app/guides/upgrading/codemods#use-built-in-font)
#####  `built-in-next-font`[](https://nextjs.org/docs/app/guides/upgrading/codemods#built-in-next-font)
Terminal
```
npx @next/codemod@latest built-in-next-font .
```

This codemod uninstalls the `@next/font` package and transforms `@next/font` imports into the built-in `next/font`.
For example:
```
import { Inter } from '@next/font/google'
```

Transforms into:
```
import { Inter } from 'next/font/google'
```

### 13.0[](https://nextjs.org/docs/app/guides/upgrading/codemods#130)
#### Rename Next Image Imports[](https://nextjs.org/docs/app/guides/upgrading/codemods#rename-next-image-imports)
#####  `next-image-to-legacy-image`[](https://nextjs.org/docs/app/guides/upgrading/codemods#next-image-to-legacy-image)
Terminal
```
npx @next/codemod@latest next-image-to-legacy-image .
```

Safely renames `next/image` imports in existing Next.js 10, 11, or 12 applications to `next/legacy/image` in Next.js 13. Also renames `next/future/image` to `next/image`.
For example:
pages/index.js
```
import Image1 from 'next/image'
import Image2 from 'next/future/image'

export default function Home() {
  return (
    <div>
      <Image1 src="/test.jpg" width="200" height="300" />
      <Image2 src="/test.png" width="500" height="400" />
    </div>
  )
}
```

Transforms into:
pages/index.js
```
// 'next/image' becomes 'next/legacy/image'
import Image1 from 'next/legacy/image'
// 'next/future/image' becomes 'next/image'
import Image2 from 'next/image'

export default function Home() {
  return (
    <div>
      <Image1 src="/test.jpg" width="200" height="300" />
      <Image2 src="/test.png" width="500" height="400" />
    </div>
  )
}
```

#### Migrate to the New Image Component[](https://nextjs.org/docs/app/guides/upgrading/codemods#migrate-to-the-new-image-component)
#####  `next-image-experimental`[](https://nextjs.org/docs/app/guides/upgrading/codemods#next-image-experimental)
Terminal
```
npx @next/codemod@latest next-image-experimental .
```

Dangerously migrates from `next/legacy/image` to the new `next/image` by adding inline styles and removing unused props.
  * Removes `layout` prop and adds `style`.
  * Removes `objectFit` prop and adds `style`.
  * Removes `objectPosition` prop and adds `style`.
  * Removes `lazyBoundary` prop.
  * Removes `lazyRoot` prop.


#### Remove `<a>` Tags From Link Components[](https://nextjs.org/docs/app/guides/upgrading/codemods#remove-a-tags-from-link-components)
#####  `new-link`[](https://nextjs.org/docs/app/guides/upgrading/codemods#new-link)
Terminal
```
npx @next/codemod@latest new-link .
```

Remove `<a>` tags inside [Link Components](https://nextjs.org/docs/app/api-reference/components/link).
For example:
```
<Link href="/about">
  <a>About</a>
</Link>
// transforms into
<Link href="/about">
  About
</Link>

<Link href="/about">
  <a onClick={() => console.log('clicked')}>About</a>
</Link>
// transforms into
<Link href="/about" onClick={() => console.log('clicked')}>
  About
</Link>
```

### 11[](https://nextjs.org/docs/app/guides/upgrading/codemods#11)
#### Migrate from CRA[](https://nextjs.org/docs/app/guides/upgrading/codemods#migrate-from-cra)
#####  `cra-to-next`[](https://nextjs.org/docs/app/guides/upgrading/codemods#cra-to-next)
Terminal
```
npx @next/codemod cra-to-next
```

Migrates a Create React App project to Next.js; creating a Pages Router and necessary config to match behavior. Client-side only rendering is leveraged initially to prevent breaking compatibility due to `window` usage during SSR and can be enabled seamlessly to allow the gradual adoption of Next.js specific features.
Please share any feedback related to this transform
### 10[](https://nextjs.org/docs/app/guides/upgrading/codemods#10)
#### Add React imports[](https://nextjs.org/docs/app/guides/upgrading/codemods#add-react-imports)
#####  `add-missing-react-import`[](https://nextjs.org/docs/app/guides/upgrading/codemods#add-missing-react-import)
Terminal
```
npx @next/codemod add-missing-react-import
```

Transforms files that do not import `React` to include the import in order for the new
For example:
my-component.js
```
export default class Home extends React.Component {
  render() {
    return <div>Hello World</div>
  }
}
```

Transforms into:
my-component.js
```
import React from 'react'
export default class Home extends React.Component {
  render() {
    return <div>Hello World</div>
  }
}
```

### 9[](https://nextjs.org/docs/app/guides/upgrading/codemods#9)
#### Transform Anonymous Components into Named Components[](https://nextjs.org/docs/app/guides/upgrading/codemods#transform-anonymous-components-into-named-components)
#####  `name-default-component`[](https://nextjs.org/docs/app/guides/upgrading/codemods#name-default-component)
Terminal
```
npx @next/codemod name-default-component
```

**Versions 9 and above.**
Transforms anonymous components into named components to make sure they work with [Fast Refresh](https://nextjs.org/blog/next-9-4#fast-refresh).
For example:
my-component.js
```
export default function () {
  return <div>Hello World</div>
}
```

Transforms into:
my-component.js
```
export default function MyComponent() {
  return <div>Hello World</div>
}
```

The component will have a camel-cased name based on the name of the file, and it also works with arrow functions.
### 8[](https://nextjs.org/docs/app/guides/upgrading/codemods#8)
> **Note** : Built-in AMP support and this codemod have been removed in Next.js 16.
#### Transform AMP HOC into page config[](https://nextjs.org/docs/app/guides/upgrading/codemods#transform-amp-hoc-into-page-config)
#####  `withamp-to-config`[](https://nextjs.org/docs/app/guides/upgrading/codemods#withamp-to-config)
Terminal
```
npx @next/codemod withamp-to-config
```

Transforms the `withAmp` HOC into Next.js 9 page configuration.
For example:
```
// Before
import { withAmp } from 'next/amp'

function Home() {
  return <h1>My AMP Page</h1>
}

export default withAmp(Home)
```

```
// After
export default function Home() {
  return <h1>My AMP Page</h1>
}

export const config = {
  amp: true,
}
```

### 6[](https://nextjs.org/docs/app/guides/upgrading/codemods#6)
#### Use `withRouter`[](https://nextjs.org/docs/app/guides/upgrading/codemods#use-withrouter)
#####  `url-to-withrouter`[](https://nextjs.org/docs/app/guides/upgrading/codemods#url-to-withrouter)
Terminal
```
npx @next/codemod url-to-withrouter
```

Transforms the deprecated automatically injected `url` property on top level pages to using `withRouter` and the `router` property it injects. Read more here: [https://nextjs.org/docs/messages/url-deprecated](https://nextjs.org/docs/messages/url-deprecated)
For example:
From
```
import React from 'react'
export default class extends React.Component {
  render() {
    const { pathname } = this.props.url
    return <div>Current pathname: {pathname}</div>
  }
}
```

To
```
import React from 'react'
import { withRouter } from 'next/router'
export default withRouter(
  class extends React.Component {
    render() {
      const { pathname } = this.props.router
      return <div>Current pathname: {pathname}</div>
    }
  }
)
```

This is one case. All the cases that are transformed (and tested) can be found in the
[PreviousUpgrading](https://nextjs.org/docs/app/guides/upgrading)[NextVersion 14](https://nextjs.org/docs/app/guides/upgrading/version-14)
Was this helpful?
Send
* * *
* * *
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Next.js Conf](https://nextjs.org/conf)[Evals](https://nextjs.org/evals)
#### More
[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)
#### About Vercel
#### Legal
Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
* * *
* * *
