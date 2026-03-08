##  [Examples](https://vercel.com/docs/conformance/rules/NEXTJS_USE_NATIVE_FETCH#examples)[](https://vercel.com/docs/conformance/rules/NEXTJS_USE_NATIVE_FETCH#examples)
This rule will catch the following code.
```
import fetch from 'isomorphic-fetch';

export async function getAuth() {
  const auth = await fetch('/api/auth');
  return auth.json();
}
```
