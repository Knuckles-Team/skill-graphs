##  [Examples](https://vercel.com/docs/getting-started-with-vercel#examples)[](https://vercel.com/docs/getting-started-with-vercel#examples)
In this example, an error is returned from a `instanceof Error` returns false.
```
const vm = require('node:vm');

const context = vm.createContext({});
const error = vm.runInContext('new Error()', context);

if (error instanceof Error) {
  // Returns `false` because `error` is from a different realm.
}
```
