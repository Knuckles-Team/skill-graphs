## Optional: Extend Jest with custom matchers[](https://nextjs.org/docs/pages/guides/testing/jest#optional-extend-jest-with-custom-matchers)
`@testing-library/jest-dom` includes a set of convenient `.toBeInTheDocument()` making it easier to write tests. You can import the custom matchers for every test by adding the following option to the Jest configuration file:
jest.config.ts
TypeScript
JavaScript TypeScript
```
setupFilesAfterEnv: ['<rootDir>/jest.setup.ts']
```

Then, inside `jest.setup`, add the following import:
jest.setup.ts
TypeScript
JavaScript TypeScript
```
import '@testing-library/jest-dom'
```

> **Good to know:** `@testing-library/jest-dom` before version 6, you will need to import `@testing-library/jest-dom/extend-expect` instead.
If you need to add more setup options before each test, you can add them to the `jest.setup` file above.
