## What can be invalidated[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#what-can-be-invalidated)
The path parameter can point to pages, layouts, or route handlers:
  * **Pages** : Invalidates the specific page
  * **Layouts** : Invalidates the layout (the `layout.tsx` at that segment), all nested layouts beneath it, and all pages beneath them
  * **Route Handlers** : Invalidates Data Cache entries accessed within route handlers. For example `revalidatePath("/api/data")` invalidates this GET handler:


app/api/data/route.ts
```
export async function GET() {
  const data = await fetch('https://api.vercel.app/blog', {
    cache: 'force-cache',
  })

  return Response.json(await data.json())
}
```
