# updateTag
Last updated February 27, 2026
`updateTag` allows you to update [cached data](https://nextjs.org/docs/app/guides/caching) on-demand for a specific cache tag from within [Server Actions](https://nextjs.org/docs/app/getting-started/updating-data).
This function is designed for **read-your-own-writes** scenarios, where a user makes a change (like creating a post), and the UI immediately shows the change, rather than stale data.
