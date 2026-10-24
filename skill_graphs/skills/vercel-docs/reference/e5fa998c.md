##  [Asset Prefix](https://vercel.com/docs/deployments#asset-prefix)[](https://vercel.com/docs/deployments#asset-prefix)
An _asset prefix_ is a unique prefix prepended to paths in URLs of static assets, like JavaScript, CSS, or images. This is needed so that URLs are unique across microfrontends and can be correctly routed to the appropriate project. Without this, these static assets may collide with each other and not work correctly.
When using `withMicrofrontends`, a default auto-generated asset prefix is automatically added. The default value is an obfuscated hash of the project name, like `vc-ap-b3331f`, in order to not leak the project name to users.
If you would like to use a human readable asset prefix, you can also set the asset prefix that is used in `microfrontends.json`.
microfrontends.json
```
"your-application": {
  "assetPrefix": "marketing-assets",
  "routing": [...]
}
```

Changing the asset prefix is not guaranteed to be backwards compatible. Make sure that the asset prefix that you choose is routed to the correct project in production before changing the `assetPrefix` field.
###  [Next.js](https://vercel.com/docs/deployments#next.js)[](https://vercel.com/docs/deployments#next.js)
JavaScript and CSS URLs are automatically prefixed with the asset prefix, but content in the `public/` directory needs to be manually moved to a subdirectory with the name of the asset prefix.
