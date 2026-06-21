## Upgrading[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#upgrading)
### Node.js Version[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#nodejs-version)
The minimum Node.js version is now **v18.17**. See the
### Next.js Version[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#nextjs-version)
To update to Next.js version 13, run the following command using your preferred package manager:
pnpmnpmyarnbun
Terminal
```
pnpm add next@latest react@latest react-dom@latest
```

### ESLint Version[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#eslint-version)
If you're using ESLint, you need to upgrade your ESLint version:
pnpmnpmyarnbun
Terminal
```
pnpm add -D eslint-config-next@latest
```

> **Good to know** : You may need to restart the ESLint server in VS Code for the ESLint changes to take effect. Open the Command Palette (`cmd+shift+p` on Mac; `ctrl+shift+p` on Windows) and search for `ESLint: Restart ESLint Server`.
