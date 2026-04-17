Menu
Menu
# NEXTJS_USE_NEXT_SCRIPT
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
This rule is available from version 1.1.0.
`next/script` loads scripts so that they're non-blocking, meaning that they load after the page has loaded.
Additionally, `next/script` has built in event handlers for common events such as `onLoad` and `onError`.
By default, this rule is disabled. Enable it by [customizing Conformance](https://vercel.com/docs/conformance/customize).
For further reading, see:
##  [Examples](https://vercel.com/docs/conformance/rules/NEXTJS_USE_NEXT_SCRIPT#examples)[](https://vercel.com/docs/conformance/rules/NEXTJS_USE_NEXT_SCRIPT#examples)
This rule will catch the following code.
```
function insertScript() {
  const script = document.createElement('script');
  script.src = process.env.SCRIPT_PATH;
  document.body.appendChild(script);
}
```

```
function App() {
  return (
    <script
      dangerouslySetInnerHTML={{ __html: "console.log('Hello world');" }}
    />
  );
}
```

##  [How to fix](https://vercel.com/docs/conformance/rules/NEXTJS_USE_NEXT_SCRIPT#how-to-fix)[](https://vercel.com/docs/conformance/rules/NEXTJS_USE_NEXT_SCRIPT#how-to-fix)
Replace any `document.createElement('script')` calls and `<script>` elements that are caught by this rule with
* * *
Was this helpful?
Send
