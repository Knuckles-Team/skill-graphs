Menu
Menu
# NO_EVAL
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
JavaScript's `eval()` function is potentially dangerous, is often misused, and might cause security issues. Using `eval()` on untrusted code can open an application up to several different injection attacks.
This rule will also catch eval-like function usage (or _implied eval_), such as passing a string as the first argument to `setTimeout`.
This is especially dangerous when working with data from external sources.
```
const dontDoThis = req.body;
setTimeout(dontDoThis, 1000);
```

For more information on why you should never use evaluation, see the
##  [Example](https://vercel.com/docs/conformance/rules/NO_EVAL#example)[](https://vercel.com/docs/conformance/rules/NO_EVAL#example)
The lines below (and variations of those) will all be caught by this rule.
```
eval('() => console.log("DROP TABLE")');

setTimeout('() => console.log("DROP TABLE")', 1000);

window.setInterval('() => console.log("DROP TABLE")', 1000);

new Function('() => console.log("DROP TABLE")');
```

###  [References](https://vercel.com/docs/conformance/rules/NO_EVAL#references)[](https://vercel.com/docs/conformance/rules/NO_EVAL#references)
Conformance rules are not type-aware, but will follow variable references within the current module (or file).
```
import { importedVar } from 'foo';

// No error reported, as this rule doesn't have access to the value.
setTimeout(importedVar, 100);

const localVar = 'bar';

// An error will be reported, as the variable was declared in this file.
setTimeout(localVar, 100);
```

##  [How to fix](https://vercel.com/docs/conformance/rules/NO_EVAL#how-to-fix)[](https://vercel.com/docs/conformance/rules/NO_EVAL#how-to-fix)
Avoid usage of this type of evaluation entirely in your application. Instead, you should write the same functionality as raw code (not within a string).
```
setTimeout(() => {
  console.log('Safe usage');
});
```

* * *
Was this helpful?
Send
