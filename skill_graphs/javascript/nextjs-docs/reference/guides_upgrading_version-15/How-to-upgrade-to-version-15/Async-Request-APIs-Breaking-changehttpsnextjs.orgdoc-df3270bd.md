## Async Request APIs (Breaking change)[](https://nextjs.org/docs/app/guides/upgrading/version-15#async-request-apis-breaking-change)
Previously synchronous Dynamic APIs that rely on runtime information are now **asynchronous** :
  * [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies)
  * [`headers`](https://nextjs.org/docs/app/api-reference/functions/headers)
  * [`draftMode`](https://nextjs.org/docs/app/api-reference/functions/draft-mode)
  * `params` in [`layout.js`](https://nextjs.org/docs/app/api-reference/file-conventions/layout), [`page.js`](https://nextjs.org/docs/app/api-reference/file-conventions/page), [`route.js`](https://nextjs.org/docs/app/api-reference/file-conventions/route), [`default.js`](https://nextjs.org/docs/app/api-reference/file-conventions/default), [`opengraph-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image), [`twitter-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image), [`icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons), and [`apple-icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons).
  * `searchParams` in [`page.js`](https://nextjs.org/docs/app/api-reference/file-conventions/page)


To ease the burden of migration, a [codemod is available](https://nextjs.org/docs/app/guides/upgrading/codemods#150) to automate the process and the APIs can temporarily be accessed synchronously.
###  `cookies`[](https://nextjs.org/docs/app/guides/upgrading/version-15#cookies)
#### Recommended Async Usage[](https://nextjs.org/docs/app/guides/upgrading/version-15#recommended-async-usage)
```
import { cookies } from 'next/headers'

// Before
const cookieStore = cookies()
const token = cookieStore.get('token')

// After
const cookieStore = await cookies()
const token = cookieStore.get('token')
```

#### Temporary Synchronous Usage[](https://nextjs.org/docs/app/guides/upgrading/version-15#temporary-synchronous-usage)
app/page.tsx
TypeScript
JavaScript TypeScript
```
import { cookies, type UnsafeUnwrappedCookies } from 'next/headers'

// Before
const cookieStore = cookies()
const token = cookieStore.get('token')

// After
const cookieStore = cookies() as unknown as UnsafeUnwrappedCookies
// will log a warning in dev
const token = cookieStore.get('token')
```

###  `headers`[](https://nextjs.org/docs/app/guides/upgrading/version-15#headers)
#### Recommended Async Usage[](https://nextjs.org/docs/app/guides/upgrading/version-15#recommended-async-usage-1)
```
import { headers } from 'next/headers'

// Before
const headersList = headers()
const userAgent = headersList.get('user-agent')

// After
const headersList = await headers()
const userAgent = headersList.get('user-agent')
```

#### Temporary Synchronous Usage[](https://nextjs.org/docs/app/guides/upgrading/version-15#temporary-synchronous-usage-1)
app/page.tsx
TypeScript
JavaScript TypeScript
```
import { headers, type UnsafeUnwrappedHeaders } from 'next/headers'

// Before
const headersList = headers()
const userAgent = headersList.get('user-agent')

// After
const headersList = headers() as unknown as UnsafeUnwrappedHeaders
// will log a warning in dev
const userAgent = headersList.get('user-agent')
```

###  `draftMode`[](https://nextjs.org/docs/app/guides/upgrading/version-15#draftmode)
#### Recommended Async Usage[](https://nextjs.org/docs/app/guides/upgrading/version-15#recommended-async-usage-2)
```
import { draftMode } from 'next/headers'

// Before
const { isEnabled } = draftMode()

// After
const { isEnabled } = await draftMode()
```

#### Temporary Synchronous Usage[](https://nextjs.org/docs/app/guides/upgrading/version-15#temporary-synchronous-usage-2)
app/page.tsx
TypeScript
JavaScript TypeScript
```
import { draftMode, type UnsafeUnwrappedDraftMode } from 'next/headers'

// Before
const { isEnabled } = draftMode()

// After
// will log a warning in dev
const { isEnabled } = draftMode() as unknown as UnsafeUnwrappedDraftMode
```

###  `params` & `searchParams`[](https://nextjs.org/docs/app/guides/upgrading/version-15#params--searchparams)
#### Asynchronous Layout[](https://nextjs.org/docs/app/guides/upgrading/version-15#asynchronous-layout)
app/layout.tsx
TypeScript
JavaScript TypeScript
```
// Before
type Params = { slug: string }

export function generateMetadata({ params }: { params: Params }) {
  const { slug } = params
}

export default async function Layout({
  children,
  params,
}: {
  children: React.ReactNode
  params: Params
}) {
  const { slug } = params
}

// After
type Params = Promise<{ slug: string }>

export async function generateMetadata({ params }: { params: Params }) {
  const { slug } = await params
}

export default async function Layout({
  children,
  params,
}: {
  children: React.ReactNode
  params: Params
}) {
  const { slug } = await params
}
```

#### Synchronous Layout[](https://nextjs.org/docs/app/guides/upgrading/version-15#synchronous-layout)
app/layout.tsx
TypeScript
JavaScript TypeScript
```
// Before
type Params = { slug: string }

export default function Layout({
  children,
  params,
}: {
  children: React.ReactNode
  params: Params
}) {
  const { slug } = params
}

// After
import { use } from 'react'

type Params = Promise<{ slug: string }>

export default function Layout(props: {
  children: React.ReactNode
  params: Params
}) {
  const params = use(props.params)
  const slug = params.slug
}
```

#### Asynchronous Page[](https://nextjs.org/docs/app/guides/upgrading/version-15#asynchronous-page)
app/page.tsx
TypeScript
JavaScript TypeScript
```
// Before
type Params = { slug: string }
type SearchParams = { [key: string]: string | string[] | undefined }

export function generateMetadata({
  params,
  searchParams,
}: {
  params: Params
  searchParams: SearchParams
}) {
  const { slug } = params
  const { query } = searchParams
}

export default async function Page({
  params,
  searchParams,
}: {
  params: Params
  searchParams: SearchParams
}) {
  const { slug } = params
  const { query } = searchParams
}

// After
type Params = Promise<{ slug: string }>
type SearchParams = Promise<{ [key: string]: string | string[] | undefined }>

export async function generateMetadata(props: {
  params: Params
  searchParams: SearchParams
}) {
  const params = await props.params
  const searchParams = await props.searchParams
  const slug = params.slug
  const query = searchParams.query
}

export default async function Page(props: {
  params: Params
  searchParams: SearchParams
}) {
  const params = await props.params
  const searchParams = await props.searchParams
  const slug = params.slug
  const query = searchParams.query
}
```

#### Synchronous Page[](https://nextjs.org/docs/app/guides/upgrading/version-15#synchronous-page)
```
'use client'

// Before
type Params = { slug: string }
type SearchParams = { [key: string]: string | string[] | undefined }

export default function Page({
  params,
  searchParams,
}: {
  params: Params
  searchParams: SearchParams
}) {
  const { slug } = params
  const { query } = searchParams
}

// After
import { use } from 'react'

type Params = Promise<{ slug: string }>
type SearchParams = Promise<{ [key: string]: string | string[] | undefined }>

export default function Page(props: {
  params: Params
  searchParams: SearchParams
}) {
  const params = use(props.params)
  const searchParams = use(props.searchParams)
  const slug = params.slug
  const query = searchParams.query
}
```

```
// Before
export default function Page({ params, searchParams }) {
  const { slug } = params
  const { query } = searchParams
}

// After
import { use } from "react"

export default function Page(props) {
  const params = use(props.params)
  const searchParams = use(props.searchParams)
  const slug = params.slug
  const query = searchParams.query
}

```

#### Route Handlers[](https://nextjs.org/docs/app/guides/upgrading/version-15#route-handlers)
app/api/route.ts
TypeScript
JavaScript TypeScript
```
// Before
type Params = { slug: string }

export async function GET(request: Request, segmentData: { params: Params }) {
  const params = segmentData.params
  const slug = params.slug
}

// After
type Params = Promise<{ slug: string }>

export async function GET(request: Request, segmentData: { params: Params }) {
  const params = await segmentData.params
  const slug = params.slug
}
```
