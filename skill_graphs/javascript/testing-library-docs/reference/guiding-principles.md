[Skip to main content](https://testing-library.com/docs/guiding-principles/)
[![An octopus representing the DOM Testing Library Logo](https://testing-library.com/img/octopus-64x64.png) **Testing Library**](https://testing-library.com/)[Docs](https://testing-library.com/docs/)[Examples](https://testing-library.com/docs/recipes)
[Help](https://testing-library.com/help)[Blog](https://testing-library.com/blog)
Search`K`
  * [](https://testing-library.com/)
  * Getting Started
  * Guiding Principles


We try to only expose methods and utilities that encourage you to write tests that closely resemble how your web pages are used.
Utilities are included in this project based on the following guiding principles:
  1. If it relates to rendering components, then it should deal with DOM nodes rather than component instances, and it should not encourage dealing with component instances.
  2. It should be generally useful for testing the application components in the way the user would use it. We _are_ making some trade-offs here because we're using a computer and often a simulated browser environment, but in general, utilities should encourage tests that use the components the way they're intended to be used.
  3. Utility implementations and APIs should be simple and flexible.


At the end of the day, what we want is for this library to be pretty light-weight, simple, and understandable.
[Previous Introduction](https://testing-library.com/docs/)[Next FAQ](https://testing-library.com/docs/dom-testing-library/faq)
