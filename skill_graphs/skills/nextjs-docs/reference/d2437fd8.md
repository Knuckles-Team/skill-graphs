## Examples[](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client#examples)
### Error tracking[](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client#error-tracking)
Initialize error tracking before React starts and add navigation breadcrumbs for better debugging context.
instrumentation-client.ts
TypeScript
JavaScript TypeScript
```
import Monitor from './lib/monitoring'

Monitor.initialize()

export function onRouterTransitionStart(url: string) {
  Monitor.pushEvent({
    message: `Navigation to ${url}`,
    category: 'navigation',
  })
}
```

### Analytics tracking[](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client#analytics-tracking)
Initialize analytics and track navigation events with detailed metadata for user behavior analysis.
instrumentation-client.ts
TypeScript
JavaScript TypeScript
```
import { analytics } from './lib/analytics'

analytics.init()

export function onRouterTransitionStart(url: string, navigationType: string) {
  analytics.track('page_navigation', {
    url,
    type: navigationType,
    timestamp: Date.now(),
  })
}
```

### Performance monitoring[](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client#performance-monitoring)
Track Time to Interactive and navigation performance using the Performance Observer API and performance marks.
instrumentation-client.ts
TypeScript
JavaScript TypeScript
```
const startTime = performance.now()

const observer = new PerformanceObserver(
  (list: PerformanceObserverEntryList) => {
    for (const entry of list.getEntries()) {
      if (entry instanceof PerformanceNavigationTiming) {
        console.log('Time to Interactive:', entry.loadEventEnd - startTime)
      }
    }
  }
)

observer.observe({ entryTypes: ['navigation'] })

export function onRouterTransitionStart(url: string) {
  performance.mark(`nav-start-${url}`)
}
```

### Polyfills[](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client#polyfills)
Load polyfills before application code runs. Use static imports for immediate loading and dynamic imports for conditional loading based on feature detection.
instrumentation-client.ts
TypeScript
JavaScript TypeScript
```
import './lib/polyfills'

if (!window.ResizeObserver) {
  import('./lib/polyfills/resize-observer').then((mod) => {
    window.ResizeObserver = mod.default
  })
}
```
