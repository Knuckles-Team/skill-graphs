##  `next-env.d.ts`[](https://nextjs.org/docs/app/api-reference/config/typescript#next-envdts)
Next.js generates a `next-env.d.ts` file in your project root. This file references Next.js type definitions, allowing TypeScript to recognize non-code imports (images, stylesheets, etc.) and Next.js-specific types.
Running `next dev`, `next build`, or [`next typegen`](https://nextjs.org/docs/app/api-reference/cli/next#next-typegen-options) regenerates this file.
> **Good to know** :
>   * We recommend adding `next-env.d.ts` to your `.gitignore` file.
>   * The file must be in your `tsconfig.json` `include` array (`create-next-app` does this automatically).
>
