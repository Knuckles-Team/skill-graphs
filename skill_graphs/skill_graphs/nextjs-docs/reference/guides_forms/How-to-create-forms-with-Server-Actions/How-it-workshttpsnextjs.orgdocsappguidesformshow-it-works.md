## How it works[](https://nextjs.org/docs/app/guides/forms#how-it-works)
React extends the HTML
When used in a form, the function automatically receives the
app/invoices/page.tsx
TypeScript
JavaScript TypeScript
```
export default function Page() {
  async function createInvoice(formData: FormData) {
    'use server'

    const rawFormData = {
      customerId: formData.get('customerId'),
      amount: formData.get('amount'),
      status: formData.get('status'),
    }

    // mutate data
    // revalidate the cache
  }

  return <form action={createInvoice}>...</form>
}
```

> **Good to know:** When working with forms that have multiple fields, use JavaScript's `const rawFormData = Object.fromEntries(formData)`. Note that this object will contain extra properties prefixed with `$ACTION_`.
