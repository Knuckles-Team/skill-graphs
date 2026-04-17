## Add a test script to `package.json`[](https://nextjs.org/docs/app/guides/testing/jest#add-a-test-script-to-packagejson)
Finally, add a Jest `test` script to your `package.json` file:
package.json
```
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "test": "jest",
    "test:watch": "jest --watch"
  }
}
```

`jest --watch` will re-run tests when a file is changed. For more Jest CLI options, please refer to the
### Creating your first test[](https://nextjs.org/docs/app/guides/testing/jest#creating-your-first-test)
Your project is now ready to run tests. Create a folder called `__tests__` in your project's root directory.
For example, we can add a test to check if the `<Page />` component successfully renders a heading:
app/page.js
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

__tests__/page.test.jsx
```
import '@testing-library/jest-dom'
import { render, screen } from '@testing-library/react'
import Page from '../app/page'

describe('Page', () => {
  it('renders a heading', () => {
    render(<Page />)

    const heading = screen.getByRole('heading', { level: 1 })

    expect(heading).toBeInTheDocument()
  })
})
```

Optionally, add a
__tests__/snapshot.js
```
import { render } from '@testing-library/react'
import Page from '../app/page'

it('renders homepage unchanged', () => {
  const { container } = render(<Page />)
  expect(container).toMatchSnapshot()
})
```
