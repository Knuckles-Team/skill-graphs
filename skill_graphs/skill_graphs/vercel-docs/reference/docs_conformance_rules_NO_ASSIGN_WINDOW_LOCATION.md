Menu
Menu
# NO_ASSIGN_WINDOW_LOCATION
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
Direct assignments to "window.location.href" or "window.location" should be avoided due to possible XSS attacks that can occur from lack of sanitization of input to the "href".
##  [How to fix](https://vercel.com/docs/conformance/rules/NO_ASSIGN_WINDOW_LOCATION#how-to-fix)[](https://vercel.com/docs/conformance/rules/NO_ASSIGN_WINDOW_LOCATION#how-to-fix)
The recommended approach for Next.js applications is to use a custom `redirectTo` function. This provides a clear way to use `router.push()` or `window.location.href` to provide an experience that is best for the user (client-side navigation only, or a full page refresh). Here's an example of how you might do this using Next.js:
Before:
my-site.js
```
windows.location.href = '/login';
```

After:
my-site.js
```
router.push('/login');
```

* * *
Was this helpful?
Send
