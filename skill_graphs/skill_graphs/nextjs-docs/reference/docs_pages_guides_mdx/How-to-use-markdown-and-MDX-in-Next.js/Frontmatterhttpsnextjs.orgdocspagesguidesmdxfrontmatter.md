## Frontmatter[](https://nextjs.org/docs/pages/guides/mdx#frontmatter)
Frontmatter is a YAML like key/value pairing that can be used to store data about a page. `@next/mdx` does **not** support frontmatter by default, though there are many solutions for adding frontmatter to your MDX content, such as:
`@next/mdx` **does** allow you to use exports like any other JavaScript component:
Metadata can now be referenced outside of the MDX file:
pages/blog.tsx
TypeScript
JavaScript TypeScript
```
import BlogPost, { metadata } from '@/content/blog-post.mdx'

export default function Page() {
  console.log('metadata: ', metadata)
  //=> { author: 'John Doe' }
  return <BlogPost />
}
```

A common use case for this is when you want to iterate over a collection of MDX and extract data. For example, creating a blog index page from all blog posts. You can use packages like
> **Good to know** :
>   * Using `fs`, `globby`, etc. can only be used server-side.
>   * View the
>
