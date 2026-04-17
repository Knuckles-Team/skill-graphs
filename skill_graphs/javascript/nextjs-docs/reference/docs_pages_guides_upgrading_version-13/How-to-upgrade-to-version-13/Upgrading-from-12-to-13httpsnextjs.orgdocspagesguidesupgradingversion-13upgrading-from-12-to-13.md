## Upgrading from 12 to 13[](https://nextjs.org/docs/pages/guides/upgrading/version-13#upgrading-from-12-to-13)
To update to Next.js version 13, run the following command using your preferred package manager:
Terminal
```
npm i next@13 react@latest react-dom@latest eslint-config-next@13
```

Terminal
```
yarn add next@13 react@latest react-dom@latest eslint-config-next@13
```

Terminal
```
pnpm i next@13 react@latest react-dom@latest eslint-config-next@13
```

Terminal
```
bun add next@13 react@latest react-dom@latest eslint-config-next@13
```

> **Good to know:** If you are using TypeScript, ensure you also upgrade `@types/react` and `@types/react-dom` to their latest versions.
### v13 Summary[](https://nextjs.org/docs/pages/guides/upgrading/version-13#v13-summary)
  * The [Supported Browsers](https://nextjs.org/docs/architecture/supported-browsers) have been changed to drop Internet Explorer and target modern browsers.
  * The minimum Node.js version has been bumped from 12.22.0 to 16.14.0, since 12.x and 14.x have reached end-of-life.
  * The minimum React version has been bumped from 17.0.2 to 18.2.0.
  * The `swcMinify` configuration property was changed from `false` to `true`. See [Next.js Compiler](https://nextjs.org/docs/architecture/nextjs-compiler) for more info.
  * The `next/image` import was renamed to `next/legacy/image`. The `next/future/image` import was renamed to `next/image`. A [codemod is available](https://nextjs.org/docs/pages/guides/upgrading/codemods#next-image-to-legacy-image) to safely and automatically rename your imports.
  * The `next/link` child can no longer be `<a>`. Add the `legacyBehavior` prop to use the legacy behavior or remove the `<a>` to upgrade. A [codemod is available](https://nextjs.org/docs/pages/guides/upgrading/codemods#new-link) to automatically upgrade your code.
  * The `target` configuration property has been removed and superseded by [Output File Tracing](https://nextjs.org/docs/pages/api-reference/config/next-config-js/output).
