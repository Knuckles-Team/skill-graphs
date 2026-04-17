## Latest version[](https://nextjs.org/docs/app/getting-started/upgrading#latest-version)
To update to the latest version of Next.js, you can use the `upgrade` command:
pnpmnpmyarnbun
Terminal
```
pnpm next upgrade
```

Versions before Next.js 16.1.0 do not support the `upgrade` command and need to use a separate package instead:
Terminal
```
npx @next/codemod@canary upgrade latest
```

If you prefer to upgrade manually, install the latest Next.js and React versions:
pnpmnpmyarnbun
Terminal
```
pnpm i next@latest react@latest react-dom@latest eslint-config-next@latest
```
