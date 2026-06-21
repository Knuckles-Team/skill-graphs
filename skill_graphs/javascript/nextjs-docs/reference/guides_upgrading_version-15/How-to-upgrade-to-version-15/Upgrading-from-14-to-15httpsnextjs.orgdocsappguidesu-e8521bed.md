## Upgrading from 14 to 15[](https://nextjs.org/docs/app/guides/upgrading/version-15#upgrading-from-14-to-15)
To update to Next.js version 15, you can use the `upgrade` codemod:
pnpmnpmyarnbun
Terminal
```
pnpm dlx @next/codemod@canary upgrade latest
```

If you prefer to do it manually, ensure that you're installing the latest Next & React versions:
pnpmnpmyarnbun
Terminal
```
pnpm add next@latest react@latest react-dom@latest eslint-config-next@latest
```

> **Good to know:**
>   * If you see a peer dependencies warning, you may need to update `react` and `react-dom` to the suggested versions, or use the `--force` or `--legacy-peer-deps` flag to ignore the warning. This won't be necessary once both Next.js 15 and React 19 are stable.
>
