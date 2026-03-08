## Creating your first Cypress component test[](https://nextjs.org/docs/app/guides/testing/cypress#creating-your-first-cypress-component-test)
Component tests build and mount a specific component without having to bundle your whole application or start a server.
Select **Component Testing** in the Cypress app, then select **Next.js** as your front-end framework. A `cypress/component` folder will be created in your project, and a `cypress.config.js` file will be updated to enable Component Testing.
Ensure your `cypress.config` file has the following configuration:
cypress.config.ts
TypeScript
JavaScript TypeScript
```
import { defineConfig } from 'cypress'

export default defineConfig({
  component: {
    devServer: {
      framework: 'next',
      bundler: 'webpack',
    },
  },
})
```

Assuming the same components from the previous section, add a test to validate a component is rendering the expected output:
cypress/component/about.cy.tsx
```
import Page from '../../app/page'

describe('<Page />', () => {
  it('should render and display expected content', () => {
    // Mount the React component for the Home page
    cy.mount(<Page />)

    // The new page should contain an h1 with "Home"
    cy.get('h1').contains('Home')

    // Validate that a link with the expected URL is present
    // Following the link is better suited to an E2E test
    cy.get('a[href="/about"]').should('be.visible')
  })
})
```

> **Good to know** :
>   * Cypress currently doesn't support Component Testing for `async` Server Components. We recommend using E2E testing.
>   * Since component tests do not require a Next.js server, features like `<Image />` that rely on a server being available may not function out-of-the-box.
>

### Running Component Tests[](https://nextjs.org/docs/app/guides/testing/cypress#running-component-tests)
Run `npm run cypress:open` in your terminal to start Cypress and run your Component Testing suite.
