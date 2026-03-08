## Creating your first Vitest Unit Test[](https://nextjs.org/docs/pages/guides/testing/vitest#creating-your-first-vitest-unit-test)
Check that everything is working by creating a test to check if the `<Page />` component successfully renders a heading:
pages/index.tsx
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

__tests__/index.test.tsx
TypeScript
JavaScript TypeScript
```
import { expect, test } from 'vitest'
import { render, screen } from '@testing-library/react'
import Page from '../pages/index'

test('Page', () => {
  render(<Page />)
  expect(screen.getByRole('heading', { level: 1, name: 'Home' })).toBeDefined()
})
```
