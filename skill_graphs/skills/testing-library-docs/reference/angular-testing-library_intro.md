[Skip to main content](https://testing-library.com/docs/angular-testing-library/intro/)
[![An octopus representing the DOM Testing Library Logo](https://testing-library.com/img/octopus-64x64.png) **Testing Library**](https://testing-library.com/)[Docs](https://testing-library.com/docs/)[Examples](https://testing-library.com/docs/recipes)
[Help](https://testing-library.com/help)[Blog](https://testing-library.com/blog)
Search`K`
  * [Getting Started](https://testing-library.com/docs/angular-testing-library/intro/)
    * [Introduction](https://testing-library.com/docs/)
    * [Guiding Principles](https://testing-library.com/docs/guiding-principles)
    * [FAQ](https://testing-library.com/docs/dom-testing-library/faq)
  * [Core API](https://testing-library.com/docs/angular-testing-library/intro/)
  * [Frameworks](https://testing-library.com/docs/angular-testing-library/intro/)
    * [DOM Testing Library](https://testing-library.com/docs/angular-testing-library/intro/)
    * [React Testing Library](https://testing-library.com/docs/angular-testing-library/intro/)
    * [Vue Testing Library](https://testing-library.com/docs/angular-testing-library/intro/)
    * [Angular Testing Library](https://testing-library.com/docs/angular-testing-library/intro/)
      * [Introduction](https://testing-library.com/docs/angular-testing-library/intro)
      * [Example](https://testing-library.com/docs/angular-testing-library/examples)
      * [API](https://testing-library.com/docs/angular-testing-library/api)
      * [Version compatibility](https://testing-library.com/docs/angular-testing-library/version-compatibility)
      * [FAQ](https://testing-library.com/docs/angular-testing-library/faq)
    * [Svelte Testing Library](https://testing-library.com/docs/angular-testing-library/intro/)
    * [Marko Testing Library](https://testing-library.com/docs/angular-testing-library/intro/)
    * [Preact Testing Library](https://testing-library.com/docs/angular-testing-library/intro/)
    * [Reason Testing Library](https://testing-library.com/docs/angular-testing-library/intro/)
    * [Native Testing Library](https://testing-library.com/docs/angular-testing-library/intro/)
    * [Solid Testing Library](https://testing-library.com/docs/angular-testing-library/intro/)
    * [Qwik Testing Library](https://testing-library.com/docs/angular-testing-library/intro/)
    * [Cypress Testing Library](https://testing-library.com/docs/cypress-testing-library/intro)
    * [Puppeteer Testing Library](https://testing-library.com/docs/pptr-testing-library/intro)
    * [Testcafe Testing Library](https://testing-library.com/docs/testcafe-testing-library/intro)
    * [Nightwatch Testing Library](https://testing-library.com/docs/nightwatch-testing-library/intro)
    * [WebdriverIO Testing Library](https://testing-library.com/docs/webdriverio-testing-library/intro)
  * [User Interactions](https://testing-library.com/docs/angular-testing-library/intro/)
  * [Ecosystem](https://testing-library.com/docs/angular-testing-library/intro/)


  * [](https://testing-library.com/)
  * Frameworks
  * Angular Testing Library
  * Introduction


On this page
# Angular Testing Library
`@testing-library/dom`:
  * npm
  * Yarn


```
npm install --save-dev @testing-library/angular @testing-library/dom

```

```
yarn add --dev @testing-library/angular @testing-library/dom

```

Or, you can use the `ng add` command. This sets up your project to use Angular Testing Library, which also includes the installation of `@testing-library/dom`.
```
ng add @testing-library/angular

```

## The problem[​](https://testing-library.com/docs/angular-testing-library/intro/#the-problem "Direct link to heading")
You want to write maintainable tests for your Angular components. As a part of this goal, you want your tests to avoid including implementation details of your components and rather focus on making your tests give you the confidence for which they are intended. As part of this, you want your testbase to be maintainable in the long run so refactors of your components (changes to implementation but not functionality) don't break your tests and slow you and your team down.
## This solution[​](https://testing-library.com/docs/angular-testing-library/intro/#this-solution "Direct link to heading")
The `Angular Testing Library` is a very lightweight solution for testing Angular components. It provides light utility functions on top of
> [The more your tests resemble the way your software is used, the more confidence they can give you.](https://testing-library.com/docs/guiding-principles)
So rather than dealing with instances of rendered Angular components, your tests will work with actual DOM nodes. The utilities this library provides facilitate querying the DOM in the same way the user would. Finding form elements by their label text (just like a user would), finding links and buttons from their text (like a user would). It also exposes a recommended way to find elements by a `data-testid` as an "escape hatch" for elements where the text content and label do not make sense or is not practical.
This library encourages your applications to be more accessible and allows you to get your tests closer to using your components the way a user will, which allows your tests to give you more confidence that your application will work when a real user uses it.
The `Angular Testing Library`:
  * Re-exports the `query` and `fireEvent` utility functions from
  * Encapsulates the `fireEvent` functions of your component to automatically call `detectChanges()` after an event occurs
  * Is test framework agnostic, it runs on every test framework


Last updated on **Jul 2, 2024** by **Tim Deschryver**
[ Previous Cheatsheet](https://testing-library.com/docs/vue-testing-library/cheatsheet)[Next Example](https://testing-library.com/docs/angular-testing-library/examples)
  * [The problem](https://testing-library.com/docs/angular-testing-library/intro/#the-problem)
  * [This solution](https://testing-library.com/docs/angular-testing-library/intro/#this-solution)


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
