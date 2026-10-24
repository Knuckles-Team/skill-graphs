[Skip to main content](https://testing-library.com/docs/dom-testing-library/intro/)
[![An octopus representing the DOM Testing Library Logo](https://testing-library.com/img/octopus-64x64.png) **Testing Library**](https://testing-library.com/)[Docs](https://testing-library.com/docs/)[Examples](https://testing-library.com/docs/recipes)
[Help](https://testing-library.com/help)[Blog](https://testing-library.com/blog)
Search`K`
  * [Getting Started](https://testing-library.com/docs/dom-testing-library/intro/)
    * [Introduction](https://testing-library.com/docs/)
    * [Guiding Principles](https://testing-library.com/docs/guiding-principles)
    * [FAQ](https://testing-library.com/docs/dom-testing-library/faq)
  * [Core API](https://testing-library.com/docs/dom-testing-library/intro/)
  * [Frameworks](https://testing-library.com/docs/dom-testing-library/intro/)
    * [DOM Testing Library](https://testing-library.com/docs/dom-testing-library/intro/)
      * [Introduction](https://testing-library.com/docs/dom-testing-library/intro)
      * [Install](https://testing-library.com/docs/dom-testing-library/install)
      * [Example](https://testing-library.com/docs/dom-testing-library/example-intro)
      * [Setup](https://testing-library.com/docs/dom-testing-library/setup)
      * [API](https://testing-library.com/docs/dom-testing-library/api)
      * [Cheatsheet](https://testing-library.com/docs/dom-testing-library/cheatsheet)
    * [React Testing Library](https://testing-library.com/docs/dom-testing-library/intro/)
    * [Vue Testing Library](https://testing-library.com/docs/dom-testing-library/intro/)
    * [Angular Testing Library](https://testing-library.com/docs/dom-testing-library/intro/)
    * [Svelte Testing Library](https://testing-library.com/docs/dom-testing-library/intro/)
    * [Marko Testing Library](https://testing-library.com/docs/dom-testing-library/intro/)
    * [Preact Testing Library](https://testing-library.com/docs/dom-testing-library/intro/)
    * [Reason Testing Library](https://testing-library.com/docs/dom-testing-library/intro/)
    * [Native Testing Library](https://testing-library.com/docs/dom-testing-library/intro/)
    * [Solid Testing Library](https://testing-library.com/docs/dom-testing-library/intro/)
    * [Qwik Testing Library](https://testing-library.com/docs/dom-testing-library/intro/)
    * [Cypress Testing Library](https://testing-library.com/docs/cypress-testing-library/intro)
    * [Puppeteer Testing Library](https://testing-library.com/docs/pptr-testing-library/intro)
    * [Testcafe Testing Library](https://testing-library.com/docs/testcafe-testing-library/intro)
    * [Nightwatch Testing Library](https://testing-library.com/docs/nightwatch-testing-library/intro)
    * [WebdriverIO Testing Library](https://testing-library.com/docs/webdriverio-testing-library/intro)
  * [User Interactions](https://testing-library.com/docs/dom-testing-library/intro/)
  * [Ecosystem](https://testing-library.com/docs/dom-testing-library/intro/)


  * [](https://testing-library.com/)
  * Frameworks
  * DOM Testing Library
  * Introduction


On this page
# Introduction
## The problem[​](https://testing-library.com/docs/dom-testing-library/intro/#the-problem "Direct link to heading")
You want to write maintainable tests for your Web UI. As a part of this goal, you want your tests to avoid including implementation details of your components and rather focus on making your tests give you the confidence for which they are intended. As part of this, you want your testbase to be maintainable in the long run so refactors of your components (changes to implementation but not functionality) don't break your tests and slow you and your team down.
## This solution[​](https://testing-library.com/docs/dom-testing-library/intro/#this-solution "Direct link to heading")
The `DOM Testing Library` is a very light-weight solution for testing DOM nodes (whether simulated with `DOM Testing Library`'s primary guiding principle is:
> [The more your tests resemble the way your software is used, the more confidence they can give you.](https://testing-library.com/docs/guiding-principles)
As part of this goal, the utilities this library provides facilitate querying the DOM in the same way the user would. Finding form elements by their label text (just like a user would), finding links and buttons from their text (like a user would), and more. It also exposes a recommended way to find elements by a `data-testid` as an "escape hatch" for elements where the text content and label do not make sense or is not practical.
This library encourages your applications to be more accessible and allows you to get your tests closer to using your components the way a user will, which allows your tests to give you more confidence that your application will work when a real user uses it.
**What this library is not** :
  1. A test runner or framework
  2. Specific to a testing framework (though we recommend Jest as our preference, the library works with any framework. See [Using Without Jest](https://testing-library.com/docs/dom-testing-library/setup#using-without-jest))


Last updated on **Nov 4, 2020** by **Matan Borenkraout**
[ Previous Configuration Options](https://testing-library.com/docs/dom-testing-library/api-configuration)[Next Install](https://testing-library.com/docs/dom-testing-library/install)
  * [The problem](https://testing-library.com/docs/dom-testing-library/intro/#the-problem)
  * [This solution](https://testing-library.com/docs/dom-testing-library/intro/#this-solution)


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
