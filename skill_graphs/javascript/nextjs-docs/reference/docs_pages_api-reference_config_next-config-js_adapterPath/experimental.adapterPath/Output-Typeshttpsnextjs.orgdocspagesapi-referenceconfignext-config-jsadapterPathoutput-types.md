## Output Types[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/adapterPath#output-types)
The `outputs` object contains arrays of different output types:
### Pages (`outputs.pages`)[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/adapterPath#pages-outputspages)
React pages from the `pages/` directory:
```
{
  type: 'PAGES'
  id: string           // Route identifier
  filePath: string     // Path to the built file
  pathname: string     // URL pathname
  sourcePage: string   // Original source file path in pages/ directory
  runtime: 'nodejs' | 'edge'
  assets: Record<string, string>  // Traced dependencies (key: relative path from repo root, value: absolute path)
  wasmAssets?: Record<string, string>  // Bundled wasm files (key: name, value: absolute path)
  config: {
    maxDuration?: number
    preferredRegion?: string | string[]
    env?: Record<string, string>  // Environment variables (edge runtime only)
  }
}
```

### API Routes (`outputs.pagesApi`)[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/adapterPath#api-routes-outputspagesapi)
API routes from `pages/api/`:
```
{
  type: 'PAGES_API'
  id: string
  filePath: string
  pathname: string
  sourcePage: string   // Original relative source file path
  runtime: 'nodejs' | 'edge'
  assets: Record<string, string>
  wasmAssets?: Record<string, string>
  config: {
    maxDuration?: number
    preferredRegion?: string | string[]
    env?: Record<string, string>
  }
}
```

### App Pages (`outputs.appPages`)[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/adapterPath#app-pages-outputsapppages)
React pages from the `app/` directory with `page.{js,ts,jsx,tsx}`:
```
{
  type: 'APP_PAGE'
  id: string
  filePath: string
  pathname: string     // Includes .rsc suffix for RSC routes
  sourcePage: string   // Original relative source file path
  runtime: 'nodejs' | 'edge'
  assets: Record<string, string>
  wasmAssets?: Record<string, string>
  config: {
    maxDuration?: number
    preferredRegion?: string | string[]
    env?: Record<string, string>
  }
}
```

### App Routes (`outputs.appRoutes`)[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/adapterPath#app-routes-outputsapproutes)
API and metadata routes from `app/` with `route.{js,ts,jsx,tsx}`:
```
{
  type: 'APP_ROUTE'
  id: string
  filePath: string
  pathname: string
  sourcePage: string
  runtime: 'nodejs' | 'edge'
  assets: Record<string, string>
  wasmAssets?: Record<string, string>
  config: {
    maxDuration?: number
    preferredRegion?: string | string[]
    env?: Record<string, string>
  }
}
```

### Prerenders (`outputs.prerenders`)[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/adapterPath#prerenders-outputsprerenders)
ISR-enabled routes and static prerenders:
```
{
  type: 'PRERENDER'
  id: string
  pathname: string
  parentOutputId: string  // ID of the source page/route
  groupId: number        // Revalidation group identifier (prerenders with same groupId revalidate together)
  pprChain?: {
    headers: Record<string, string>  // PPR chain headers (e.g., 'x-nextjs-resume': '1')
  }
  parentFallbackMode?: 'blocking' | false | null  // Fallback mode from getStaticPaths
  fallback?: {
    filePath: string
    initialStatus?: number
    initialHeaders?: Record<string, string | string[]>
    initialExpiration?: number
    initialRevalidate?: number
    postponedState?: string  // PPR postponed state
  }
  config: {
    allowQuery?: string[]     // Allowed query parameters
    allowHeader?: string[]    // Allowed headers for ISR
    bypassFor?: RouteHas[]    // Cache bypass conditions
    renderingMode?: RenderingMode
    bypassToken?: string
  }
}
```

### Static Files (`outputs.staticFiles`)[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/adapterPath#static-files-outputsstaticfiles)
Static assets and auto-statically optimized pages:
```
{
  type: 'STATIC_FILE'
  id: string
  filePath: string
  pathname: string
}
```

### Middleware (`outputs.middleware`)[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/adapterPath#middleware-outputsmiddleware)
Middleware function (if present):
```
{
  type: 'MIDDLEWARE'
  id: string
  filePath: string
  pathname: string      // Always '/_middleware'
  sourcePage: string    // Always 'middleware'
  runtime: 'nodejs' | 'edge'
  assets: Record<string, string>
  wasmAssets?: Record<string, string>
  config: {
    maxDuration?: number
    preferredRegion?: string | string[]
    env?: Record<string, string>
    matchers?: Array<{
      source: string
      sourceRegex: string
      has: RouteHas[] | undefined
      missing: RouteHas[] | undefined
    }>
  }
}
```
