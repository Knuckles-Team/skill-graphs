##  [When to use this rule type](https://vercel.com/docs/conformance/custom-rules/forbidden-properties#when-to-use-this-rule-type)[](https://vercel.com/docs/conformance/custom-rules/forbidden-properties#when-to-use-this-rule-type)
  * Disallowing use of global properties
    * You want to disallow calling `document.write`
    * You want to disallow using browser-only APIs in a component library that may be server-rendered
    * You want to disallow calls to usage of `window.location` in favor of another solution.
  * Disallowing use of deprecated features
    * You want to disallow using `event.keyCode`
    * You want to disallow specific strings from being used within code
