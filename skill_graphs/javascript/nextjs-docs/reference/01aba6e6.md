## Navigation uses Activity[](https://nextjs.org/docs/app/getting-started/cache-components#navigation-uses-activity)
When the [`cacheComponents`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents) flag is enabled, Next.js uses React's
Rather than unmounting the previous route when you navigate away, Next.js sets the Activity mode to
  * Component state is preserved when navigating between routes
  * When you navigate back, the previous route reappears with its state intact
  * Effects are cleaned up when a route is hidden, and recreated when it becomes visible again


This behavior improves the navigation experience by maintaining UI state (form inputs, or expanded sections) when users navigate back and forth between routes.
> **Good to know** : Next.js uses heuristics to keep a few recently visited routes `"hidden"`, while older routes are removed from the DOM to prevent excessive growth.
