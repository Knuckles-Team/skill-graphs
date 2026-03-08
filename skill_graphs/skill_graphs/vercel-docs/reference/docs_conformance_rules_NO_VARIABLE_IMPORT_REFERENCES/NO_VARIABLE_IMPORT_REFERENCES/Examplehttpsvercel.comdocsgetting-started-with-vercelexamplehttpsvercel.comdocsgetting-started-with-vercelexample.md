##  [Example](https://vercel.com/docs/getting-started-with-vercel#example)[](https://vercel.com/docs/getting-started-with-vercel#example)
The following code would be flagged by this rule:
```
function loadDynamicCode(moduleName: string) {
  return import(moduleName);
}
```

In this example, it can not be guaranteed that the `moduleName` that is provided would not be arbitrary input that could load unintended code.
