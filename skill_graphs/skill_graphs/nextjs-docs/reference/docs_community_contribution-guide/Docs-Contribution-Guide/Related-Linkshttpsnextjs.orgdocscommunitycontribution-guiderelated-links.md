## Related Links[](https://nextjs.org/docs/community/contribution-guide#related-links)
Related Links guide the user's learning journey by adding links to logical next steps.
  * Links will be displayed in cards under the main content of the page.
  * Links will be automatically generated for pages that have child pages.


Create related links using the `related` field in the page's metadata.
example.mdx
```
---
related:
  description: Learn how to quickly get started with your first application.
  links:
    - app/building-your-application/routing/defining-routes
    - app/building-your-application/data-fetching
    - app/api-reference/file-conventions/page
---
```

### Nested Fields[](https://nextjs.org/docs/community/contribution-guide#nested-fields)
Field | Required? | Description
---|---|---
`title` | Optional | The title of the card list. Defaults to **Next Steps**.
`description` | Optional | The description of the card list.
`links` | Required | A list of links to other doc pages. Each list item should be a relative URL path (without a leading slash) e.g. `app/api-reference/file-conventions/page`
