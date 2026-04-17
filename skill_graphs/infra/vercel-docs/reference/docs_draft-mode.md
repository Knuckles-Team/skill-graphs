Draft Mode
Next.js (/app)
Choose a framework to optimize documentation to:
  * Next.js (/app)
  * Next.js (/pages)
  * SvelteKit


Draft Mode
# Draft Mode
Last updated September 24, 2025
Draft Mode lets you view your unpublished headless CMS content on your website rendered with all the normal styling and layout that you would see once published.
Both [Next.js](https://vercel.com/docs/frameworks/nextjs#draft-mode) and [SvelteKit](https://vercel.com/docs/frameworks/sveltekit#draft-mode) support Draft Mode. Any framework that uses the [Build Output API](https://vercel.com/docs/build-output-api/v3) can support Draft Mode by adding the `bypassToken` option to [prerender configuration](https://vercel.com/docs/build-output-api/v3/primitives#prerender-functions).
Draft Mode was called Preview Mode before the release of Next.js [preview deployments](https://vercel.com/docs/deployments/environments#preview-environment-pre-production), which is a different product.
You can use Draft Mode if you:
  1. Use [Incremental Static Regeneration (ISR)](https://vercel.com/docs/incremental-static-regeneration) to fetch and render data from a headless CMS
  2. Want to view your unpublished headless CMS content on your site without rebuilding your pages when you make changes
  3. Want to protect your unpublished content from being viewed publicly


##  [How Draft Mode works](https://vercel.com/docs/draft-mode#how-draft-mode-works)[](https://vercel.com/docs/draft-mode#how-draft-mode-works)
Draft Mode allows you to bypass [ISR](https://vercel.com/docs/incremental-static-regeneration) caching to fetch the latest CMS content at request time. This is useful for seeing your draft content on your website without waiting for the cache to refresh, or manually revalidating the page.
The process works like this:
  1. Each ISR route has a `bypassToken` configuration option, which is assigned a generated, cryptographically-secure value at build time
  2. When someone visits an ISR route with a `bypassToken` configured, the page will check for a `__prerender_bypass` cookie
  3. If the `__prerender_bypass` cookie exists and has the same value as the `bypassToken` your project is using, the visitor will view the page in Draft Mode


Only team members will be able to view pages in Draft Mode.
##  [Getting started](https://vercel.com/docs/draft-mode#getting-started)[](https://vercel.com/docs/draft-mode#getting-started)
To use Draft Mode with Next.js on Vercel, you must:
  1. [Enable ISR](https://vercel.com/docs/incremental-static-regeneration) on pages that fetch content. Using ISR is required on pages that you want to view in Draft Mode
  2. Add code to your ISR pages to detect when Draft Mode is enabled and render the draft content
  3. Toggle Draft Mode in the Vercel Toolbar by selecting Draft Mode in [the toolbar menu](https://vercel.com/docs/vercel-toolbar#using-the-toolbar-menu) to view your draft content. Once toggled, the toolbar will turn purple, indicating that Draft Mode is enabled
Next.js (/app)Next.js (/pages)SvelteKit
app/page.tsx
TypeScript
TypeScript JavaScript Bash
```
import { draftMode } from 'next/headers';

async function getContent() {
  const { isEnabled } = await draftMode();

  const contentUrl = isEnabled
    ? 'https://draft.example.com'
    : 'https://production.example.com';

  // This line enables ISR, required for draft mode
  const res = await fetch(contentUrl, { next: { revalidate: 120 } });

  return res.json();
}

export default async function Page() {
  const { title, desc } = await getContent();

  return (
    <main>
      <h1>{title}</h1>
      <p>{desc}</p>
    </main>
  );
}
```



See the Next.js docs to learn how to use Draft Mode with self-hosted Next.js projects:
Once implemented, team members can access Draft Mode from the Vercel Toolbar by selecting the eye icon
##  [Sharing drafts](https://vercel.com/docs/draft-mode#sharing-drafts)[](https://vercel.com/docs/draft-mode#sharing-drafts)
To share a draft URL, it must have the `?__vercel_draft=1` query parameter. For example:
```
https://my-site.com/blog/post-01?__vercel_draft=1
```

Viewers outside your Vercel team cannot enable Draft Mode or see your draft content, even with a draft URL.
* * *
[ Previous Comments ](https://vercel.com/docs/comments)[ Next Edit Mode ](https://vercel.com/docs/edit-mode)
Was this helpful?
Send
