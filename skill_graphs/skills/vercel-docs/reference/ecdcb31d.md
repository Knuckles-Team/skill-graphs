##  [How To Fix](https://vercel.com/docs/conformance/rules/TYPESCRIPT_ONLY#how-to-fix)[](https://vercel.com/docs/conformance/rules/TYPESCRIPT_ONLY#how-to-fix)
To fix this error, you must convert the JavaScript file to TypeScript. You can do this by changing the file extension from `.js` to `.ts` or `.jsx` to `.tsx` and adding the appropriate type annotations.
diff
```
--- a/apps/docs/src/add-numbers.js
+++ b/apps/docs/src/add-numbers.ts
-export function addNumbers(a, b) {
+export function addNumbers(a: number, b: number): number {
  return a + b;
}
```
