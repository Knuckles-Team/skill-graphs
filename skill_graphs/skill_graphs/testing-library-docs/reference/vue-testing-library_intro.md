[Skip to main content](https://testing-library.com/docs/vue-testing-library/intro/)
[![An octopus representing the DOM Testing Library Logo](https://testing-library.com/img/octopus-64x64.png) **Testing Library**](https://testing-library.com/)[Docs](https://testing-library.com/docs/)[Examples](https://testing-library.com/docs/recipes)
[Help](https://testing-library.com/help)[Blog](https://testing-library.com/blog)
Search`K`
  * [Getting Started](https://testing-library.com/docs/vue-testing-library/intro/)
    * [Introduction](https://testing-library.com/docs/)
    * [Guiding Principles](https://testing-library.com/docs/guiding-principles)
    * [FAQ](https://testing-library.com/docs/dom-testing-library/faq)
  * [Core API](https://testing-library.com/docs/vue-testing-library/intro/)
  * [Frameworks](https://testing-library.com/docs/vue-testing-library/intro/)
    * [DOM Testing Library](https://testing-library.com/docs/vue-testing-library/intro/)
    * [React Testing Library](https://testing-library.com/docs/vue-testing-library/intro/)
    * [Vue Testing Library](https://testing-library.com/docs/vue-testing-library/intro/)
      * [Introduction](https://testing-library.com/docs/vue-testing-library/intro)
      * [Example](https://testing-library.com/docs/vue-testing-library/examples)
      * [Setup](https://testing-library.com/docs/vue-testing-library/setup)
      * [API](https://testing-library.com/docs/vue-testing-library/api)
      * [FAQ](https://testing-library.com/docs/vue-testing-library/faq)
      * [Cheatsheet](https://testing-library.com/docs/vue-testing-library/cheatsheet)
    * [Angular Testing Library](https://testing-library.com/docs/vue-testing-library/intro/)
    * [Svelte Testing Library](https://testing-library.com/docs/vue-testing-library/intro/)
    * [Marko Testing Library](https://testing-library.com/docs/vue-testing-library/intro/)
    * [Preact Testing Library](https://testing-library.com/docs/vue-testing-library/intro/)
    * [Reason Testing Library](https://testing-library.com/docs/vue-testing-library/intro/)
    * [Native Testing Library](https://testing-library.com/docs/vue-testing-library/intro/)
    * [Solid Testing Library](https://testing-library.com/docs/vue-testing-library/intro/)
    * [Qwik Testing Library](https://testing-library.com/docs/vue-testing-library/intro/)
    * [Cypress Testing Library](https://testing-library.com/docs/cypress-testing-library/intro)
    * [Puppeteer Testing Library](https://testing-library.com/docs/pptr-testing-library/intro)
    * [Testcafe Testing Library](https://testing-library.com/docs/testcafe-testing-library/intro)
    * [Nightwatch Testing Library](https://testing-library.com/docs/nightwatch-testing-library/intro)
    * [WebdriverIO Testing Library](https://testing-library.com/docs/webdriverio-testing-library/intro)
  * [User Interactions](https://testing-library.com/docs/vue-testing-library/intro/)
  * [Ecosystem](https://testing-library.com/docs/vue-testing-library/intro/)


  * [](https://testing-library.com/)
  * Frameworks
  * Vue Testing Library
  * Introduction


On this page
# Intro
Vue Testing Library builds on top of `DOM Testing Library` by adding APIs for working with Vue components. It is built on top of
In short, Vue Testing Library does three things:
  1. Re-exports query utilities and helpers from `DOM Testing Library`.
  2. Hides `@vue/test-utils` methods that are in conflict with Testing Library [Guiding Principle](https://testing-library.com/docs/guiding-principles).
  3. Tweaks some methods from both sources.


## Quickstart[​](https://testing-library.com/docs/vue-testing-library/intro/#quickstart "Direct link to heading")
If using Vue2
  * npm
  * Yarn


```
npm install --save-dev @testing-library/vue@5

```

```
yarn add --dev @testing-library/vue@5

```

If using Vue3
  * npm
  * Yarn


```
npm install --save-dev @testing-library/vue

```

```
yarn add --dev @testing-library/vue

```

You can now use all of `DOM Testing Library`'s `getBy`, `getAllBy`, `queryBy` and `queryAllBy` commands. See here the [full list of queries](https://testing-library.com/docs/queries/about#types-of-queries).
You may also be interested in installing `@testing-library/jest-dom` so you can use
## The problem[​](https://testing-library.com/docs/vue-testing-library/intro/#the-problem "Direct link to heading")
You want to write maintainable tests for your Vue components. As a part of this goal, **you want your tests to avoid including implementation details** of your components. You'd rather focus on making your tests give you the confidence for which they are intended.
## This solution[​](https://testing-library.com/docs/vue-testing-library/intro/#this-solution "Direct link to heading")
`Vue Testing Library` is a very light-weight solution for testing Vue components. It provides light utility functions on top of `@vue/test-utils`, in a way that encourages better testing practices.
Its primary guiding principle is:
> [The more your tests resemble the way your software is used, the more confidence they can give you.](https://testing-library.com/docs/guiding-principles)
So rather than dealing with instances of rendered Vue components, **your tests will work with actual DOM nodes**.
The utilities this library provides facilitate querying the DOM in the same way the user would. They allow you to find elements by their label text, finding links and buttons from their text, and assert that your application is **accessible**.
It also exposes a recommended way to find elements by a `data-testid` as an "escape hatch" for elements where the text content and label do not make sense or is not practical.
Last updated on **Dec 11, 2025** by **Uaena_Alex_John**
[ Previous Cheatsheet](https://testing-library.com/docs/react-testing-library/cheatsheet)[Next Example](https://testing-library.com/docs/vue-testing-library/examples)
  * [Quickstart](https://testing-library.com/docs/vue-testing-library/intro/#quickstart)
  * [The problem](https://testing-library.com/docs/vue-testing-library/intro/#the-problem)
  * [This solution](https://testing-library.com/docs/vue-testing-library/intro/#this-solution)


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
