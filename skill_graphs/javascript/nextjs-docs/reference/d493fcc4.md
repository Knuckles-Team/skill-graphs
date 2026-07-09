## Disabling[](https://nextjs.org/docs/messages/missing-suspense-with-csr-bailout#disabling)
> **Note** : This is only available with Next.js version 14.x. If you're in versions above 14 please fix it with the approach above.
We don't recommend disabling this rule. However, if you need to, you can disable it by setting the `missingSuspenseWithCSRBailout` option to `false` in your `next.config.js`:
next.config.js
```
module.exports = {
  experimental: {
    missingSuspenseWithCSRBailout: false,
  },
}
```

This configuration option will be removed in a future major version.
