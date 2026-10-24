## Examples[](https://nextjs.org/docs/app/api-reference/cli/create-next-app#examples)
### With the default template[](https://nextjs.org/docs/app/api-reference/cli/create-next-app#with-the-default-template)
To create a new app using the default template, run the following command in your terminal:
pnpmnpmyarnbun
Terminal
```
pnpm create next-app
```

On installation, you'll see the following prompts:
Terminal
```
What is your project named? my-app
Would you like to use the recommended Next.js defaults?
    Yes, use recommended defaults - TypeScript, ESLint, Tailwind CSS, App Router, Turbopack
    No, reuse previous settings
    No, customize settings - Choose your own preferences
```

If you choose to `customize settings`, you'll see the following prompts:
Terminal
```
Would you like to use TypeScript? No / Yes
Which linter would you like to use? ESLint / Biome / None
Would you like to use React Compiler? No / Yes
Would you like to use Tailwind CSS? No / Yes
Would you like your code inside a `src/` directory? No / Yes
Would you like to use App Router? (recommended) No / Yes
Would you like to customize the import alias (`@/*` by default)? No / Yes
What import alias would you like configured? @/*
```

After the prompts, `create-next-app` will create a folder with your project name and install the required dependencies.
### Linter Options[](https://nextjs.org/docs/app/api-reference/cli/create-next-app#linter-options)
**ESLint** : The traditional and most popular JavaScript linter. Includes Next.js-specific rules from `@next/eslint-plugin-next`.
**Biome** : A fast, modern linter and formatter that combines the functionality of ESLint and Prettier. Includes built-in Next.js and React domain support for optimal performance.
**None** : Skip linter configuration entirely. You can always add a linter later.
Once you've answered the prompts, a new project will be created with your chosen configuration.
### With an official Next.js example[](https://nextjs.org/docs/app/api-reference/cli/create-next-app#with-an-official-nextjs-example)
To create a new app using an official Next.js example, use the `--example` flag. For example:
pnpmnpmyarnbun
Terminal
```
pnpm create next-app --example [example-name] [your-project-name]
```

You can view a list of all available examples along with setup instructions in the
### With any public GitHub example[](https://nextjs.org/docs/app/api-reference/cli/create-next-app#with-any-public-github-example)
To create a new app using any public GitHub example, use the `--example` option with the GitHub repo's URL. For example:
pnpmnpmyarnbun
Terminal
```
pnpm create next-app --example "https://github.com/.../" [your-project-name]
```

[PreviousCLI](https://nextjs.org/docs/app/api-reference/cli)[Nextnext CLI](https://nextjs.org/docs/app/api-reference/cli/next)
Was this helpful?
Send
* * *
* * *
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Next.js Conf](https://nextjs.org/conf)[Evals](https://nextjs.org/evals)
#### More
[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)
#### About Vercel
#### Legal
Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
* * *
* * *
