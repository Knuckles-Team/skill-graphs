# src Directory
Last updated February 27, 2026
As an alternative to having the special Next.js `app` or `pages` directories in the root of your project, Next.js also supports the common pattern of placing application code under the `src` folder.
This separates application code from project configuration files which mostly live in the root of a project, which is preferred by some individuals and teams.
To use the `src` folder, move the `app` Router folder or `pages` Router folder to `src/app` or `src/pages` respectively.
![An example folder structure with the `src` folder](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-src-directory.png&w=3840&q=75)![An example folder structure with the `src` folder](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-src-directory.png&w=3840&q=75)
> **Good to know** :
>   * The `/public` directory should remain in the root of your project.
>   * Config files like `package.json`, `next.config.js` and `tsconfig.json` should remain in the root of your project.
>   * `.env.*` files should remain in the root of your project.
>   * `src/app` or `src/pages` will be ignored if `app` or `pages` are present in the root directory.
>   * If you're using `src`, you'll probably also move other application folders such as `/components` or `/lib`.
>   * If you're using Proxy, ensure it is placed inside the `src` folder.
>   * If you're using Tailwind CSS, you'll need to add the `/src` prefix to the `tailwind.config.js` file in the
>   * If you are using TypeScript paths for imports such as `@/*`, you should update the `paths` object in `tsconfig.json` to include `src/`.
>

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
