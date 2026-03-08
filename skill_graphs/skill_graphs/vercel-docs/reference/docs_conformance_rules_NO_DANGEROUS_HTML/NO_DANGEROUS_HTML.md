# NO_DANGEROUS_HTML
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
Unsafe creation of DOM can be done a variety of ways:
  * `element.innerHTML`
  * `element.outerHTML`
  * `DOMParser.parseFromString()`
  * `element.insertAdjacentHTML()`
  * `srcdoc` on iframe elements
  * `dangerouslySetInnerHTML` prop in React apps


Usage of these methods is deemed an unsafe coding practice as the HTML might result in security vulnerabilities.
