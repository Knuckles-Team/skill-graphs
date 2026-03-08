[Skip to main content](https://testing-library.com/docs/react-testing-library/intro/)
[![An octopus representing the DOM Testing Library Logo](https://testing-library.com/img/octopus-64x64.png) **Testing Library**](https://testing-library.com/)[Docs](https://testing-library.com/docs/)[Examples](https://testing-library.com/docs/recipes)
[Help](https://testing-library.com/help)[Blog](https://testing-library.com/blog)
Search`K`
  * [Getting Started](https://testing-library.com/docs/react-testing-library/intro/)
  * [Core API](https://testing-library.com/docs/react-testing-library/intro/)
  * [Frameworks](https://testing-library.com/docs/react-testing-library/intro/)
    * [DOM Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
    * [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
      * [Introduction](https://testing-library.com/docs/react-testing-library/intro)
      * [Example](https://testing-library.com/docs/react-testing-library/example-intro)
      * [Setup](https://testing-library.com/docs/react-testing-library/setup)
      * [API](https://testing-library.com/docs/react-testing-library/api)
      * [Migrate from Enzyme](https://testing-library.com/docs/react-testing-library/migrate-from-enzyme)
      * [FAQ](https://testing-library.com/docs/react-testing-library/faq)
      * [Cheatsheet](https://testing-library.com/docs/react-testing-library/cheatsheet)
    * [Vue Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
      * [Introduction](https://testing-library.com/docs/vue-testing-library/intro)
      * [Example](https://testing-library.com/docs/vue-testing-library/examples)
      * [Setup](https://testing-library.com/docs/vue-testing-library/setup)
      * [API](https://testing-library.com/docs/vue-testing-library/api)
      * [FAQ](https://testing-library.com/docs/vue-testing-library/faq)
      * [Cheatsheet](https://testing-library.com/docs/vue-testing-library/cheatsheet)
    * [Angular Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
    * [Svelte Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
    * [Marko Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
    * [Preact Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
    * [Reason Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
    * [Native Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
    * [Solid Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
    * [Qwik Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
    * [Cypress Testing Library](https://testing-library.com/docs/cypress-testing-library/intro)
    * [Puppeteer Testing Library](https://testing-library.com/docs/pptr-testing-library/intro)
    * [Testcafe Testing Library](https://testing-library.com/docs/testcafe-testing-library/intro)
    * [Nightwatch Testing Library](https://testing-library.com/docs/nightwatch-testing-library/intro)
    * [WebdriverIO Testing Library](https://testing-library.com/docs/webdriverio-testing-library/intro)
  * [User Interactions](https://testing-library.com/docs/react-testing-library/intro/)
  * [Ecosystem](https://testing-library.com/docs/react-testing-library/intro/)


  * [](https://testing-library.com/)
  * Frameworks
  * React Testing Library
  * Introduction


On this page
# React Testing Library
`DOM Testing Library` by adding APIs for working with React components.
## Installation[​](https://testing-library.com/docs/react-testing-library/intro/#installation "Direct link to heading")
To get started with `React Testing Library`, you'll need to install it together with its peerDependency `@testing-library/dom`:
  * npm
  * Yarn


```
npm install --save-dev @testing-library/react @testing-library/dom

```

```
yarn add --dev @testing-library/react @testing-library/dom

```

### With TypeScript[​](https://testing-library.com/docs/react-testing-library/intro/#with-typescript "Direct link to heading")
To get full type coverage, you need to install the types for `react` and `react-dom` as well:
  * npm
  * Yarn


```
npm install --save-dev @testing-library/react @testing-library/dom @types/react @types/react-dom

```

```
yarn add --dev @testing-library/react @testing-library/dom @types/react @types/react-dom

```

## The problem[​](https://testing-library.com/docs/react-testing-library/intro/#the-problem "Direct link to heading")
You want to write maintainable tests for your React components. As a part of this goal, you want your tests to avoid including implementation details of your components and rather focus on making your tests give you the confidence for which they are intended. As part of this, you want your testbase to be maintainable in the long run so refactors of your components (changes to implementation but not functionality) don't break your tests and slow you and your team down.
## This solution[​](https://testing-library.com/docs/react-testing-library/intro/#this-solution "Direct link to heading")
The `React Testing Library` is a very light-weight solution for testing React components. It provides light utility functions on top of `react-dom` and `react-dom/test-utils`, in a way that encourages better testing practices. Its primary guiding principle is:
> [The more your tests resemble the way your software is used, the more confidence they can give you.](https://testing-library.com/docs/guiding-principles)
So rather than dealing with instances of rendered React components, your tests will work with actual DOM nodes. The utilities this library provides facilitate querying the DOM in the same way the user would. Finding form elements by their label text (just like a user would), finding links and buttons from their text (like a user would). It also exposes a recommended way to find elements by a `data-testid` as an "escape hatch" for elements where the text content and label do not make sense or is not practical.
This library encourages your applications to be more accessible and allows you to get your tests closer to using your components the way a user will, which allows your tests to give you more confidence that your application will work when a real user uses it.
This library is a replacement for _can_ follow these guidelines using Enzyme itself, enforcing this is harder because of all the extra utilities that Enzyme provides (utilities which facilitate testing implementation details). Read more about this in [the FAQ](https://testing-library.com/docs/react-testing-library/faq).
**What this library is not** :
  1. A test runner or framework
  2. Specific to a testing framework (though we recommend Jest as our preference, the library works with any framework. See [Using Without Jest](https://testing-library.com/docs/react-testing-library/setup#using-without-jest))


> NOTE: This library is built on top of [`DOM Testing Library`](https://testing-library.com/docs/dom-testing-library/intro) which is where most of the logic behind the queries is.
## Tutorials[​](https://testing-library.com/docs/react-testing-library/intro/#tutorials "Direct link to heading")
Have a look at the "What is React Testing library?" video below for an introduction to the library.
Also, don't miss this
Last updated on **Jun 3, 2024** by **Matan Borenkraout**
[ Previous Cheatsheet](https://testing-library.com/docs/dom-testing-library/cheatsheet)[Next Example](https://testing-library.com/docs/react-testing-library/example-intro)
  * [Installation](https://testing-library.com/docs/react-testing-library/intro/#installation)
    * [With TypeScript](https://testing-library.com/docs/react-testing-library/intro/#with-typescript)
  * [The problem](https://testing-library.com/docs/react-testing-library/intro/#the-problem)
  * [This solution](https://testing-library.com/docs/react-testing-library/intro/#this-solution)
  * [Tutorials](https://testing-library.com/docs/react-testing-library/intro/#tutorials)


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
