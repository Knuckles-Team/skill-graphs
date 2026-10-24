## Using `use server` inline[](https://nextjs.org/docs/app/api-reference/directives/use-server#using-use-server-inline)
In the following example, `use server` is used inline at the top of a function to mark it as a
app/posts/[id]/page.tsx
TypeScript
JavaScript TypeScript
```
import { EditPost } from './edit-post'
import { revalidatePath } from 'next/cache'

export default async function PostPage({ params }: { params: { id: string } }) {
  const post = await getPost(params.id)

  async function updatePost(formData: FormData) {
    'use server'
    await savePost(params.id, formData)
    revalidatePath(`/posts/${params.id}`)
  }

  return <EditPost updatePostAction={updatePost} post={post} />
}
```
