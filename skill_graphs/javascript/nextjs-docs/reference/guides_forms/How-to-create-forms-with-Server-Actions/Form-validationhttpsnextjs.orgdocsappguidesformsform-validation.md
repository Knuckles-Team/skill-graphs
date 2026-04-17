## Form validation[](https://nextjs.org/docs/app/guides/forms#form-validation)
Forms can be validated on the client or server.
  * For **client-side validation** , you can use the HTML attributes like `required` and `type="email"` for basic validation.
  * For **server-side validation** , you can use a library like


app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { z } from 'zod'

const schema = z.object({
  email: z.string({
    invalid_type_error: 'Invalid Email',
  }),
})

export default async function createUser(formData: FormData) {
  const validatedFields = schema.safeParse({
    email: formData.get('email'),
  })

  // Return early if the form data is invalid
  if (!validatedFields.success) {
    return {
      errors: validatedFields.error.flatten().fieldErrors,
    }
  }

  // Mutate data
}
```
