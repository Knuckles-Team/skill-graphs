##  [Adding the toolbar using the `@vercel/toolbar` package](https://vercel.com/docs/comments#adding-the-toolbar-using-the-@vercel/toolbar-package)[](https://vercel.com/docs/comments#adding-the-toolbar-using-the-@vercel/toolbar-package)
For team members that do not use the browser extension or if you have more complex rules for when the toolbar shows in production, you can add the `@vercel/toolbar` package to your project:
  1. ###  [Install the `@vercel/toolbar` package and link your project](https://vercel.com/docs/comments#install-the-@vercel/toolbar-package-and-link-your-project)[](https://vercel.com/docs/comments#install-the-@vercel/toolbar-package-and-link-your-project)
Install the package in your project using the following command:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i @vercel/toolbar
```

```
yarn add @vercel/toolbar
```

```
npm i @vercel/toolbar
```

```
bun add @vercel/toolbar
```

Then link your local project to your Vercel project with the [`vercel link`](https://vercel.com/docs/cli/link) command using [Vercel CLI](https://vercel.com/docs/cli).
terminal
```
vercel link [path-to-directory]
```

  2. ###  [Add the toolbar to your project](https://vercel.com/docs/comments#add-the-toolbar-to-your-project)[](https://vercel.com/docs/comments#add-the-toolbar-to-your-project)
Before using the Vercel Toolbar in a production deployment Vercel recommends conditionally injecting the toolbar. Otherwise, all visitors will be prompted to log in when visiting your site.
The following example demonstrates code that will show the Vercel Toolbar to a team member on a production deployment.
components/staff-toolbar.tsx
TypeScript
TypeScript JavaScript Bash
```
'use client';

import { VercelToolbar } from '@vercel/toolbar/next';

function useIsEmployee() {
  // Replace this stub with your auth library hook
  return false;
}

export function StaffToolbar() {
  const isEmployee = useIsEmployee();
  return isEmployee ? <VercelToolbar /> : null;
}
```

app/layout.tsx
TypeScript
TypeScript JavaScript Bash
```
import { Suspense, type ReactNode } from 'react';
import { StaffToolbar } from '../components/staff-toolbar';

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>
        {children}
        <Suspense fallback={null}>
          <StaffToolbar />
        </Suspense>
      </body>
    </html>
  );
}
```

  3. ###  [Managing notifications and integrations for Comments on production](https://vercel.com/docs/comments#managing-notifications-and-integrations-for-comments-on-production)[](https://vercel.com/docs/comments#managing-notifications-and-integrations-for-comments-on-production)
Unlike comments on preview deployments, alerts for new comments won't be sent to a specific user by default. Vercel recommends [linking your project to Slack with the integration](https://vercel.com/docs/comments/integrations#use-the-vercel-slack-app), or directly mentioning someone when starting a new comment thread in production to ensure new comments are seen.
