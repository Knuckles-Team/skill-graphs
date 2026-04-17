## Metadata[](https://nextjs.org/docs/community/contribution-guide#metadata)
Each page has a metadata block at the top of the file separated by three dashes.
### Required Fields[](https://nextjs.org/docs/community/contribution-guide#required-fields)
The following fields are **required** :
Field | Description
---|---
`title` | The page's `<h1>` title, used for SEO and OG Images.
`description` | The page's description, used in the `<meta name="description">` tag for SEO.
required-fields.mdx
```
---
title: Page Title
description: Page Description
---
```

It's good practice to limit the page title to 2-3 words (e.g. Optimizing Images) and the description to 1-2 sentences (e.g. Learn how to optimize images in Next.js).
### Optional Fields[](https://nextjs.org/docs/community/contribution-guide#optional-fields)
The following fields are **optional** :
Field | Description
---|---
`nav_title` | Overrides the page's title in the navigation. This is useful when the page's title is too long to fit. If not provided, the `title` field is used.
`source` | Pulls content into a shared page. See [Shared Pages](https://nextjs.org/docs/community/contribution-guide#shared-pages).
`related` | A list of related pages at the bottom of the document. These will automatically be turned into cards. See [Related Links](https://nextjs.org/docs/community/contribution-guide#related-links).
`version` | A stage of development. e.g. `experimental`,`legacy`,`unstable`,`RC`
optional-fields.mdx
```
---
nav_title: Nav Item Title
source: app/building-your-application/optimizing/images
related:
  description: See the image component API reference.
  links:
    - app/api-reference/components/image
version: experimental
---
```
