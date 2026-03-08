##  [How to fix](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)[](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)
###  [Node.js](https://vercel.com/docs/getting-started-with-vercel#node.js)[](https://vercel.com/docs/getting-started-with-vercel#node.js)
You can use `true` for errors from other realms.
```
import { isNativeError } from 'node:util/types';
const vm = require('node:vm');

const context = vm.createContext({});
const error = vm.runInContext('new Error()', context);

if (isNativeError(error)) {
  // ...
}
```

###  [Browsers](https://vercel.com/docs/getting-started-with-vercel#browsers)[](https://vercel.com/docs/getting-started-with-vercel#browsers)
Use a library like
You can also use `Object.prototype.toString.call(error) === '[object Error]'` in some cases. This method will not work for custom errors, and you'll need to traverse the prototype chain (i.e. `Object.getPrototypeOf(error)`)to handle those cases.
The following code is a simplified version of the code used in the `is-error` library:
```
function isError(error) {
  if (typeof error !== 'object') {
    return false;
  }

  if (error instanceof Error) {
    return true;
  }

  let currentError = error;
  while (currentError) {
    if (Object.prototype.toString.call(currentError) === '[object Error]') {
      return true;
    }
    currentError = Object.getPrototypeOf(currentError);
  }

  return false;
}
```

* * *
[ Previous Vercel Documentation ](https://vercel.com/docs)[ Next Projects and Deployments ](https://vercel.com/docs/getting-started-with-vercel/projects-deployments)
Was this helpful?
Send
On this page
  * [Examples](https://vercel.com/docs/getting-started-with-vercel#examples)
  * [How to fix](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)
  * [Node.js](https://vercel.com/docs/getting-started-with-vercel#node.js)
  * [Browsers](https://vercel.com/docs/getting-started-with-vercel#browsers)


Copy as MarkdownGive feedbackAsk AI about this page
