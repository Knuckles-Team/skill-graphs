## Add a test script to `package.json`[](https://nextjs.org/docs/pages/guides/testing/jest#add-a-test-script-to-packagejson)
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
### Creating your first test[](https://nextjs.org/docs/pages/guides/testing/jest#creating-your-first-test)
Your project is now ready to run tests. Create a folder called `__tests__` in your project's root directory.
For example, we can add a test to check if the `<Home />` component successfully renders a heading:
```
export default function Home() {
  return <h1>Home</h1>
}
```

__tests__/index.test.js
```
import '@testing-library/jest-dom'
import { render, screen } from '@testing-library/react'
import Home from '../pages/index'

describe('Home', () => {
  it('renders a heading', () => {
    render(<Home />)

    const heading = screen.getByRole('heading', { level: 1 })

    expect(heading).toBeInTheDocument()
  })
})
```

Optionally, add a
__tests__/snapshot.js
```
import { render } from '@testing-library/react'
import Home from '../pages/index'

it('renders homepage unchanged', () => {
  const { container } = render(<Home />)
  expect(container).toMatchSnapshot()
})
```

> **Good to know** : Test files should not be included inside the Pages Router because any files inside the Pages Router are considered routes.
