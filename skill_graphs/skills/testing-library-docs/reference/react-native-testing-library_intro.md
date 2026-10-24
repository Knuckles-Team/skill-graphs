[Skip to main content](https://testing-library.com/docs/react-native-testing-library/intro)
[![An octopus representing the DOM Testing Library Logo](https://testing-library.com/img/octopus-64x64.png) **Testing Library**](https://testing-library.com/)[Docs](https://testing-library.com/docs/)[Examples](https://testing-library.com/docs/recipes)
[Help](https://testing-library.com/help)[Blog](https://testing-library.com/blog)
Search`K`
  * [Getting Started](https://testing-library.com/docs/react-native-testing-library/intro)
  * [Core API](https://testing-library.com/docs/react-native-testing-library/intro)
  * [Frameworks](https://testing-library.com/docs/react-native-testing-library/intro)
    * [DOM Testing Library](https://testing-library.com/docs/react-native-testing-library/intro)
    * [React Testing Library](https://testing-library.com/docs/react-native-testing-library/intro)
    * [Vue Testing Library](https://testing-library.com/docs/react-native-testing-library/intro)
    * [Angular Testing Library](https://testing-library.com/docs/react-native-testing-library/intro)
    * [Svelte Testing Library](https://testing-library.com/docs/react-native-testing-library/intro)
    * [Marko Testing Library](https://testing-library.com/docs/react-native-testing-library/intro)
    * [Preact Testing Library](https://testing-library.com/docs/react-native-testing-library/intro)
    * [Reason Testing Library](https://testing-library.com/docs/react-native-testing-library/intro)
    * [Native Testing Library](https://testing-library.com/docs/react-native-testing-library/intro)
      * [Introduction](https://testing-library.com/docs/react-native-testing-library/intro)
      * [Example](https://testing-library.com/docs/react-native-testing-library/example-intro)
      * [Setup](https://testing-library.com/docs/react-native-testing-library/setup)
    * [Solid Testing Library](https://testing-library.com/docs/react-native-testing-library/intro)
    * [Qwik Testing Library](https://testing-library.com/docs/react-native-testing-library/intro)
    * [Cypress Testing Library](https://testing-library.com/docs/cypress-testing-library/intro)
    * [Puppeteer Testing Library](https://testing-library.com/docs/pptr-testing-library/intro)
    * [Testcafe Testing Library](https://testing-library.com/docs/testcafe-testing-library/intro)
    * [Nightwatch Testing Library](https://testing-library.com/docs/nightwatch-testing-library/intro)
    * [WebdriverIO Testing Library](https://testing-library.com/docs/webdriverio-testing-library/intro)
  * [User Interactions](https://testing-library.com/docs/react-native-testing-library/intro)
  * [Ecosystem](https://testing-library.com/docs/react-native-testing-library/intro)


  * [](https://testing-library.com/)
  * Frameworks
  * Native Testing Library
  * Introduction


On this page
# Introduction
React Native Testing Library is a testing library for **React Native** inspired by `React Testing Library`. Because React Native does not run in a browser environment, the core queries are implemented independently, unlike other wrappers that use `DOM Testing Library` as the base. You'll find much more information about the library, including examples, on the project sites:
The project is maintained by
## Quickstart[​](https://testing-library.com/docs/react-native-testing-library/intro#quickstart "Direct link to heading")
  * npm
  * Yarn


```
npm install --save-dev @testing-library/react-native

```

```
yarn add --dev @testing-library/react-native

```

## The problem[​](https://testing-library.com/docs/react-native-testing-library/intro#the-problem "Direct link to heading")
You want to write maintainable tests for your React Native components. As a part of this goal, you want your tests to avoid including implementation details of your components and rather focus on making your tests give you the confidence for which they are intended. As part of this, you want your testbase to be maintainable in the long run so refactors of your components (changes to implementation but not functionality) don't break your tests and slow you and your team down.
## This solution[​](https://testing-library.com/docs/react-native-testing-library/intro#this-solution "Direct link to heading")
The React Native Testing Library (RNTL) is a lightweight solution for testing React Native components. It provides light utility functions on top of `react-test-renderer`, in a way that encourages better testing practices. Its primary guiding principle is:
> The more your tests resemble the way your software is used, the more confidence they can give you.
This Project is tested to work with Jest, but it should work with other test runners as well.
Last updated on **Aug 9, 2022** by **Sergio Moreno**
[ Previous Example](https://testing-library.com/docs/bs-react-testing-library/examples)[Next Example](https://testing-library.com/docs/react-native-testing-library/example-intro)
  * [Quickstart](https://testing-library.com/docs/react-native-testing-library/intro#quickstart)
  * [The problem](https://testing-library.com/docs/react-native-testing-library/intro#the-problem)
  * [This solution](https://testing-library.com/docs/react-native-testing-library/intro#this-solution)


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
