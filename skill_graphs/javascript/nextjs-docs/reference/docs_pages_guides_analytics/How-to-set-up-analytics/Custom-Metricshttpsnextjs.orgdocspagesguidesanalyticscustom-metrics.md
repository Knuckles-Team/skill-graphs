## Custom Metrics[](https://nextjs.org/docs/pages/guides/analytics#custom-metrics)
In addition to the core metrics listed above, there are some additional custom metrics that measure the time it takes for the page to hydrate and render:
  * `Next.js-hydration`: Length of time it takes for the page to start and finish hydrating (in ms)
  * `Next.js-route-change-to-render`: Length of time it takes for a page to start rendering after a route change (in ms)
  * `Next.js-render`: Length of time it takes for a page to finish render after a route change (in ms)


You can handle all the results of these metrics separately:
```
export function reportWebVitals(metric) {
  switch (metric.name) {
    case 'Next.js-hydration':
      // handle hydration results
      break
    case 'Next.js-route-change-to-render':
      // handle route-change to render results
      break
    case 'Next.js-render':
      // handle render results
      break
    default:
      break
  }
}
```

These metrics work in all browsers that support the
