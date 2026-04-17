[Skip to main content](https://testing-library.com/docs/cypress-testing-library/intro/)
[![An octopus representing the DOM Testing Library Logo](https://testing-library.com/img/octopus-64x64.png) **Testing Library**](https://testing-library.com/)[Docs](https://testing-library.com/docs/)[Examples](https://testing-library.com/docs/recipes)
[Help](https://testing-library.com/help)[Blog](https://testing-library.com/blog)
Search`K`
  * [Getting Started](https://testing-library.com/docs/cypress-testing-library/intro/)
  * [Core API](https://testing-library.com/docs/cypress-testing-library/intro/)
  * [Frameworks](https://testing-library.com/docs/cypress-testing-library/intro/)
    * [DOM Testing Library](https://testing-library.com/docs/cypress-testing-library/intro/)
    * [React Testing Library](https://testing-library.com/docs/cypress-testing-library/intro/)
    * [Vue Testing Library](https://testing-library.com/docs/cypress-testing-library/intro/)
    * [Angular Testing Library](https://testing-library.com/docs/cypress-testing-library/intro/)
    * [Svelte Testing Library](https://testing-library.com/docs/cypress-testing-library/intro/)
    * [Marko Testing Library](https://testing-library.com/docs/cypress-testing-library/intro/)
    * [Preact Testing Library](https://testing-library.com/docs/cypress-testing-library/intro/)
    * [Reason Testing Library](https://testing-library.com/docs/cypress-testing-library/intro/)
    * [Native Testing Library](https://testing-library.com/docs/cypress-testing-library/intro/)
    * [Solid Testing Library](https://testing-library.com/docs/cypress-testing-library/intro/)
      * [Introduction](https://testing-library.com/docs/solid-testing-library/intro)
      * [API](https://testing-library.com/docs/solid-testing-library/api)
    * [Qwik Testing Library](https://testing-library.com/docs/cypress-testing-library/intro/)
    * [Cypress Testing Library](https://testing-library.com/docs/cypress-testing-library/intro)
    * [Puppeteer Testing Library](https://testing-library.com/docs/pptr-testing-library/intro)
    * [Testcafe Testing Library](https://testing-library.com/docs/testcafe-testing-library/intro)
    * [Nightwatch Testing Library](https://testing-library.com/docs/nightwatch-testing-library/intro)
    * [WebdriverIO Testing Library](https://testing-library.com/docs/webdriverio-testing-library/intro)
  * [User Interactions](https://testing-library.com/docs/cypress-testing-library/intro/)
  * [Ecosystem](https://testing-library.com/docs/cypress-testing-library/intro/)


  * [](https://testing-library.com/)
  * Frameworks
  * Cypress Testing Library


On this page
# Cypress Testing Library
  * npm
  * Yarn


```
npm install --save-dev cypress @testing-library/cypress

```

```
yarn add --dev cypress @testing-library/cypress

```

## Usage[​](https://testing-library.com/docs/cypress-testing-library/intro/#usage "Direct link to heading")
`Cypress Testing Library` extends Cypress's `cy` commands.
Add this line to your project's `cypress/support/commands.js`:
```
import '@testing-library/cypress/add-commands'

```

You can now use some of `DOM Testing Library`'s `findBy`, and `findAllBy` commands off the global `cy` object. [See the `About queries` docs for reference](https://testing-library.com/docs/queries/about).
> Note: the `get*` queries are not supported because for reasonable Cypress tests you need retryability and `find*` queries already support that. `query*` queries are no longer necessary since v5 and will be removed in v6. `find*` fully support built-in Cypress assertions (removes the only use-case for `query*`).
## With TypeScript[​](https://testing-library.com/docs/cypress-testing-library/intro/#with-typescript "Direct link to heading")
Typings should be added as follows in `tsconfig.json`:
```
{
  "compilerOptions": {
    "types": ["cypress", "@testing-library/cypress"]
  }
}

```

You can find
## Examples[​](https://testing-library.com/docs/cypress-testing-library/intro/#examples "Direct link to heading")
To show some simple examples (from
```
cy.findByRole('button', {name: /Jackie Chan/i}).click()
cy.findByRole('button', {name: /Button Text/i}).should('exist')
cy.findByRole('button', {name: /Non-existing Button Text/i}).should('not.exist')
cy.findByLabelText(/Label text/i, {timeout: 7000}).should('exist')

// findByRole _inside_ a form element
cy.get('form')
  .findByRole('button', {name: /Button Text/i})
  .should('exist')
cy.findByRole('dialog').within(() => {
  cy.findByRole('button', {name: /confirm/i})
})

```

`Cypress Testing Library` supports both jQuery elements and DOM nodes. This is necessary because Cypress uses jQuery elements, while `DOM Testing Library` expects DOM nodes. When you pass a jQuery element as `container`, it will get the first DOM node from the collection and use that as the `container` parameter for the `DOM Testing Library` functions.
Last updated on **Nov 26, 2023** by **Vadim Shvetsov**
[ Previous FAQ](https://testing-library.com/docs/qwik-testing-library/faq)[Next Puppeteer Testing Library](https://testing-library.com/docs/pptr-testing-library/intro)
  * [Usage](https://testing-library.com/docs/cypress-testing-library/intro/#usage)
  * [With TypeScript](https://testing-library.com/docs/cypress-testing-library/intro/#with-typescript)
  * [Examples](https://testing-library.com/docs/cypress-testing-library/intro/#examples)


Docs
  * [Getting Started](https://testing-library.com/docs)
  * [Examples](https://testing-library.com/docs/example-codesandbox)
  * [API](https://testing-library.com/docs/dom-testing-library/api)
  * [Help](https://testing-library.com/docs/dom-testing-library/faq)


Community
  * [Blog](https://testing-library.com/blog)


More
![An octopus representing the DOM Testing Library Logo](https://testing-library.com/img/octopus-128x128.png)
Copyright © 2018-2026 Kent C. Dodds and contributors
