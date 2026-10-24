##  `App` and `Pages` Docs[](https://nextjs.org/docs/community/contribution-guide#app-and-pages-docs)
Since most of the features in the **App Router** and **Pages Router** are completely different, their docs for each are kept in separate sections (`02-app` and `03-pages`). However, there are a few features that are shared between them.
### Shared Pages[](https://nextjs.org/docs/community/contribution-guide#shared-pages)
To avoid content duplication and risk the content becoming out of sync, we use the `source` field to pull content from one page into another. For example, the `<Link>` component behaves _mostly_ the same in **App** and **Pages**. Instead of duplicating the content, we can pull the content from `app/.../link.mdx` into `pages/.../link.mdx`:
app/.../link.mdx
```
---
title: <Link>
description: API reference for the <Link> component.
---

This API reference will help you understand how to use the props
and configuration options available for the Link Component.
```

pages/.../link.mdx
```
---
title: <Link>
description: API reference for the <Link> component.
source: app/api-reference/components/link
---

{/* DO NOT EDIT THIS PAGE. */}
{/* The content of this page is pulled from the source above. */}
```

We can therefore edit the content in one place and have it reflected in both sections.
### Shared Content[](https://nextjs.org/docs/community/contribution-guide#shared-content)
In shared pages, sometimes there might be content that is **App Router** or **Pages Router** specific. For example, the `<Link>` component has a `shallow` prop that is only available in **Pages** but not in **App**.
To make sure the content only shows in the correct router, we can wrap content blocks in an `<AppOnly>` or `<PagesOnly>` components:
app/.../link.mdx
```
This content is shared between App and Pages.

<PagesOnly>

This content will only be shown on the Pages docs.

</PagesOnly>

This content is shared between App and Pages.
```

You'll likely use these components for examples and code blocks.
