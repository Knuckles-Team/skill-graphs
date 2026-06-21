##  [When to use this rule type](https://vercel.com/docs/conformance/custom-rules/forbidden-code#when-to-use-this-rule-type)[](https://vercel.com/docs/conformance/custom-rules/forbidden-code#when-to-use-this-rule-type)
  * Disallowing comments
    * You want to disallow `// TODO` comments
    * You want to disallow usage of `@ts-ignore`
  * Disallowing specific strings
    * You want to enforce a certain casing for one or more strings
    * You want to disallow specific strings from being used within code


If you want to disallow specific operations on a property, you should instead use the [`forbidden-properties`](https://vercel.com/docs/conformance/custom-rules/forbidden-properties) rule type.
