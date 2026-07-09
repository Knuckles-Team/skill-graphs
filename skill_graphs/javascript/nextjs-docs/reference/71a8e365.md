## Manual setup[](https://nextjs.org/docs/app/guides/testing/jest#manual-setup)
Since the release of [Next.js 12](https://nextjs.org/blog/next-12), Next.js now has built-in configuration for Jest.
To set up Jest, install `jest` and the following packages as dev dependencies:
pnpmnpmyarnbun
Terminal
```
pnpm add -D jest jest-environment-jsdom @testing-library/react @testing-library/dom @testing-library/jest-dom ts-node @types/jest
```

Generate a basic Jest configuration file by running the following command:
pnpmnpmyarnbun
Terminal
```
pnpm create jest@latest
```

This will take you through a series of prompts to setup Jest for your project, including automatically creating a `jest.config.ts|js` file.
Update your config file to use `next/jest`. This transformer has all the necessary configuration options for Jest to work with Next.js:
jest.config.ts
TypeScript
JavaScript TypeScript
```
import type { Config } from 'jest'
import nextJest from 'next/jest.js'

const createJestConfig = nextJest({
  // Provide the path to your Next.js app to load next.config.js and .env files in your test environment
  dir: './',
})

// Add any custom config to be passed to Jest
const config: Config = {
  coverageProvider: 'v8',
  testEnvironment: 'jsdom',
  // Add more setup options before each test is run
  // setupFilesAfterEnv: ['<rootDir>/jest.setup.ts'],
}

// createJestConfig is exported this way to ensure that next/jest can load the Next.js config which is async
export default createJestConfig(config)
```

Under the hood, `next/jest` is automatically configuring Jest for you, including:
  * Setting up `transform` using the [Next.js Compiler](https://nextjs.org/docs/architecture/nextjs-compiler).
  * Auto mocking stylesheets (`.css`, `.module.css`, and their scss variants), image imports and [`next/font`](https://nextjs.org/docs/app/api-reference/components/font).
  * Loading `.env` (and all variants) into `process.env`.
  * Ignoring `node_modules` from test resolving and transforms.
  * Ignoring `.next` from test resolving.
  * Loading `next.config.js` for flags that enable SWC transforms.


> **Good to know** : To test environment variables directly, load them manually in a separate setup script or in your `jest.config.ts` file. For more information, please see [Test Environment Variables](https://nextjs.org/docs/app/guides/environment-variables#test-environment-variables).
