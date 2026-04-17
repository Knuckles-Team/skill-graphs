Menu
Menu
# NO_POSTINSTALL_SCRIPT
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
This rule is available from version 1.4.0.
Modifying, adding, or updating any dependencies in your application triggers the execution of the `"postinstall"` script. Consequently, incorporating a `"postinstall"` script in your application's package.json leads to increased installation times for all users.
##  [How to fix](https://vercel.com/docs/conformance/rules/NO_POSTINSTALL_SCRIPT#how-to-fix)[](https://vercel.com/docs/conformance/rules/NO_POSTINSTALL_SCRIPT#how-to-fix)
If you hit this issue, you can resolve it by removing the `"postinstall"` script in the `package.json` file.
package.json
```
{
  "scripts": {
    "postinstall": "sleep 360"
  },
}
```

* * *
Was this helpful?
Send
