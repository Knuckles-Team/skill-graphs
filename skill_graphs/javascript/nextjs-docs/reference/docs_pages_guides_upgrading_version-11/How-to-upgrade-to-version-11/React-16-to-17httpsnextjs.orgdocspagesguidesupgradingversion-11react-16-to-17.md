## React 16 to 17[](https://nextjs.org/docs/pages/guides/upgrading/version-11#react-16-to-17)
React 17 introduced a new `import React from 'react'` when using JSX. When using React 17 Next.js will automatically use the new transform. This transform does not make the `React` variable global, which was an unintended side-effect of the previous Next.js implementation. A [codemod is available](https://nextjs.org/docs/pages/guides/upgrading/codemods#add-missing-react-import) to automatically fix cases where you accidentally used `React` without importing it.
Most applications already use the latest version of React, with Next.js 11 the minimum React version has been updated to 17.0.2.
To upgrade you can run the following command:
```
npm install react@latest react-dom@latest

```

Or using `yarn`:
```
yarn add react@latest react-dom@latest

```

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
