## Next Steps[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#next-steps)
If everything worked, you now have a functioning Next.js application running as a single-page application. You aren’t yet leveraging Next.js features like server-side rendering or file-based routing, but you can now do so incrementally:
  * **Migrate from React Router** to the [Next.js App Router](https://nextjs.org/docs/app) for:
    * Automatic code splitting
    * [Streaming server rendering](https://nextjs.org/docs/app/api-reference/file-conventions/loading)
    * [React Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
  * **Optimize images** with the [`<Image>` component](https://nextjs.org/docs/app/api-reference/components/image)
  * **Optimize fonts** with [`next/font`](https://nextjs.org/docs/app/api-reference/components/font)
  * **Optimize third-party scripts** with the [`<Script>` component](https://nextjs.org/docs/app/guides/scripts)
  * **Enable ESLint** with Next.js [recommended rules](https://nextjs.org/docs/app/api-reference/config/eslint#setup-eslint)


> **Note** : Using a static export (`output: 'export'`) `useParams` hook or other server features. To use all Next.js features, remove `output: 'export'` from your `next.config.ts`.
[PreviousApp Router](https://nextjs.org/docs/app/guides/migrating/app-router-migration)[NextVite](https://nextjs.org/docs/app/guides/migrating/from-vite)
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
