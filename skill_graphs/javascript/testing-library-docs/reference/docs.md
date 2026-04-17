[Skip to main content](https://testing-library.com/docs/)
[![An octopus representing the DOM Testing Library Logo](https://testing-library.com/img/octopus-64x64.png) **Testing Library**](https://testing-library.com/)[Docs](https://testing-library.com/docs/)[Examples](https://testing-library.com/docs/recipes)
[Help](https://testing-library.com/help)[Blog](https://testing-library.com/blog)
Search`K`
  * [Getting Started](https://testing-library.com/docs/)
    * [Introduction](https://testing-library.com/docs/)
    * [Guiding Principles](https://testing-library.com/docs/guiding-principles)
    * [FAQ](https://testing-library.com/docs/dom-testing-library/faq)
  * [Core API](https://testing-library.com/docs/)
  * [Frameworks](https://testing-library.com/docs/)
  * [User Interactions](https://testing-library.com/docs/)
  * [Ecosystem](https://testing-library.com/docs/)


  * [](https://testing-library.com/)
  * Getting Started
  * Introduction


On this page
# Introduction
The
> [The more your tests resemble the way your software is used, the more confidence they can give you.](https://testing-library.com/docs/guiding-principles)
## The problem[​](https://testing-library.com/docs/#the-problem "Direct link to heading")
You want to write maintainable tests that give you high confidence that your components are working for your users. As a part of this goal, you want your tests to avoid including implementation details so refactors of your components (changes to implementation but not functionality) don't break your tests and slow you and your team down.
## The solution[​](https://testing-library.com/docs/#the-solution "Direct link to heading")
The core library, [`DOM Testing Library`](https://testing-library.com/docs/dom-testing-library/intro), is a light-weight solution for testing web pages by querying and interacting with DOM nodes (whether simulated with
The core library has been wrapped to provide ergonomic APIs for several frameworks, including [React](https://testing-library.com/docs/react-testing-library/intro), [Angular](https://testing-library.com/docs/angular-testing-library/intro), and [Vue](https://testing-library.com/docs/vue-testing-library/intro). There is also a plugin to use testing-library queries for end-to-end tests in [Cypress](https://testing-library.com/docs/cypress-testing-library/intro) and an implementation for [React Native](https://testing-library.com/docs/react-native-testing-library/intro).
### What this library is not[​](https://testing-library.com/docs/#what-this-library-is-not "Direct link to heading")
  1. A test runner or framework
  2. Specific to a testing framework


`DOM Testing Library` works with any environment that provides DOM APIs, such as Jest, Mocha + JSDOM, or a real browser.
### What you should avoid with Testing Library[​](https://testing-library.com/docs/#what-you-should-avoid-with-testing-library "Direct link to heading")
Testing Library encourages you to avoid testing [The Guiding Principles](https://testing-library.com/docs/guiding-principles) of this library emphasize a focus on tests that closely resemble how users interact with your web pages.
You may want to avoid the following implementation details:
  1. Internal state of a component
  2. Internal methods of a component
  3. Lifecycle methods of a component
  4. Child components


Last updated on **Jan 22, 2026** by **Brandon Zylstra**
[ Next Guiding Principles](https://testing-library.com/docs/guiding-principles)
  * [The problem](https://testing-library.com/docs/#the-problem)
  * [The solution](https://testing-library.com/docs/#the-solution)
    * [What this library is not](https://testing-library.com/docs/#what-this-library-is-not)
    * [What you should avoid with Testing Library](https://testing-library.com/docs/#what-you-should-avoid-with-testing-library)


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
