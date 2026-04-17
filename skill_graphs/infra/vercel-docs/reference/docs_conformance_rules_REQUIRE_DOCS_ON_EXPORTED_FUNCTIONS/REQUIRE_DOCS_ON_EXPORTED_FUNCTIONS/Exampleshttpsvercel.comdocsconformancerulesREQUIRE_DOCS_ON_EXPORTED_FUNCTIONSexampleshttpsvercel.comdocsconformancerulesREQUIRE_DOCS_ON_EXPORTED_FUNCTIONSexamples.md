##  [Examples](https://vercel.com/docs/conformance/rules/REQUIRE_DOCS_ON_EXPORTED_FUNCTIONS#examples)[](https://vercel.com/docs/conformance/rules/REQUIRE_DOCS_ON_EXPORTED_FUNCTIONS#examples)
The below function is a minimal example of a function that would be caught by this rule.
```
export function appendWorld(str: string): string {
  return str + ' world';
}
```

This rule will also catch references within the same file, and different ways of declaring functions. For example:
```
const appendWorld = function (str: string): string {
  return str + ' world';
};

export default appendWorld;
```

This rule non-function exports and re-exports of functions.
