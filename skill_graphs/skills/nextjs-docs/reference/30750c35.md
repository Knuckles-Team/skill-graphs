## Creating your first Vitest Unit Test[](https://nextjs.org/docs/app/guides/testing/vitest#creating-your-first-vitest-unit-test)
Check that everything is working by creating a test to check if the `<Page />` component successfully renders a heading:
app/page.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

export default function Page() {
  return (
    <div>
      <h1>Home</h1>
      <Link href="/about">About</Link>
    </div>
  )
}
```

__tests__/page.test.tsx
TypeScript
JavaScript TypeScript
```
import { expect, test } from 'vitest'
import { render, screen } from '@testing-library/react'
import Page from '../app/page'

test('Page', () => {
  render(<Page />)
  expect(screen.getByRole('heading', { level: 1, name: 'Home' })).toBeDefined()
})
```

> **Good to know** : The example above uses the common `__tests__` convention, but test files can also be colocated inside the `app` router.
