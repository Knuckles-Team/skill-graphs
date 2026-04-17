## Possible Ways to Fix It[](https://nextjs.org/docs/messages/empty-generate-static-params#possible-ways-to-fix-it)
### Option 1: Return at least one static param[](https://nextjs.org/docs/messages/empty-generate-static-params#option-1-return-at-least-one-static-param)
Modify your `generateStaticParams` function to return at least one set of parameters. This is the most common fix and allows build-time validation to work properly.
app/blog/[slug]/page.tsx
```
// This will cause an error with Cache Components
export async function generateStaticParams() {
  return [] // Empty array not allowed
}

// Return at least one sample param
export async function generateStaticParams() {
  return [{ slug: 'hello-world' }, { slug: 'getting-started' }]
}
```

These samples serve dual purposes:
  1. **Build-time validation** : Verify your route structure is safe
  2. **Prerendering** : Generate instant-loading pages for popular routes


The build process only validates code paths that execute with your sample params. If runtime parameters trigger conditional logic that renders branches accessing runtime APIs (like `cookies()`) without Suspense, or dynamic content without Suspense or `use cache`, those will cause runtime errors.
### Option 2: Use a placeholder param[](https://nextjs.org/docs/messages/empty-generate-static-params#option-2-use-a-placeholder-param)
If you don't know actual values at build time, you can use a placeholder for validation. However, this defeats the purpose of build-time validation and should be avoided:
app/blog/[slug]/page.tsx
```
export async function generateStaticParams() {
  // Placeholder only validates one code path
  return [{ slug: '__placeholder__' }]
}

export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params

  // Handle placeholder case
  if (slug === '__placeholder__') {
    notFound()
  }

  // Real params may trigger code paths
  // that access dynamic APIs incorrectly, causing
  // runtime errors that cannot be caught by error boundaries
  const post = await getPost(slug)
  return <div>{post.title}</div>
}
```

Using placeholders provides minimal build-time validation and increases the risk of runtime errors for actual parameter values.
