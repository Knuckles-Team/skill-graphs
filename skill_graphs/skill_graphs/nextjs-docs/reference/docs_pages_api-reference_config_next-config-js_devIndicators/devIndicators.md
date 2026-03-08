# devIndicators
Last updated February 27, 2026
`devIndicators` allows you to configure the on-screen indicator that gives context about the current route you're viewing during development.
Types
```
  devIndicators: false | {
    position?: 'bottom-right'
    | 'bottom-left'
    | 'top-right'
    | 'top-left', // defaults to 'bottom-left',
  },
```

Setting `devIndicators` to `false` will hide the indicator, however Next.js will continue to surface any build or runtime errors that were encountered.
