## Manual setup[](https://nextjs.org/docs/pages/guides/testing/cypress#manual-setup)
To manually set up Cypress, install `cypress` as a dev dependency:
pnpmnpmyarnbun
Terminal
```
pnpm add -D cypress
```

Add the Cypress `open` command to the `package.json` scripts field:
package.json
```
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "eslint",
    "cypress:open": "cypress open"
  }
}
```

Run Cypress for the first time to open the Cypress testing suite:
pnpmnpmyarnbun
Terminal
```
pnpm cypress:open
```

You can choose to configure **E2E Testing** and/or **Component Testing**. Selecting any of these options will automatically create a `cypress.config.js` file and a `cypress` folder in your project.
