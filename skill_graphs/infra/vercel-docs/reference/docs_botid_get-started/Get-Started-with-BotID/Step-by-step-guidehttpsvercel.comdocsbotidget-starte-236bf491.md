##  [Step by step guide](https://vercel.com/docs/botid/get-started#step-by-step-guide)[](https://vercel.com/docs/botid/get-started#step-by-step-guide)
Before setting up BotID, ensure you have a JavaScript [project deployed](https://vercel.com/docs/projects/managing-projects#creating-a-project) on Vercel.
  1. ###  [Install the package](https://vercel.com/docs/botid/get-started#install-the-package)[](https://vercel.com/docs/botid/get-started#install-the-package)
Add BotID to your project:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i botid
```

```
yarn add botid
```

```
npm i botid
```

```
bun add botid
```

  2. ###  [Configure redirects](https://vercel.com/docs/botid/get-started#configure-redirects)[](https://vercel.com/docs/botid/get-started#configure-redirects)
Use the appropriate configuration method for your framework to set up proxy rewrites. This ensures that ad-blockers, third party scripts, and more won't make BotID any less effective.
Next.js (/app)SvelteKitNuxtOther frameworks
next.config.ts
TypeScript
TypeScript JavaScript Bash
```
import { withBotId } from 'botid/next/config';

const nextConfig = {
  // Your existing Next.js config
};

export default withBotId(nextConfig);
```

  3. ###  [Add client-side protection](https://vercel.com/docs/botid/get-started#add-client-side-protection)[](https://vercel.com/docs/botid/get-started#add-client-side-protection)
Choose the appropriate method for your framework:
     * Next.js 15.3+: Use `initBotId()` in `instrumentation-client.ts` for optimal performance
     * Other Next.js: Mount the `<BotIdClient/>` component in your layout `head`
     * Other frameworks: Call `initBotId()` during application initialization
Next.js 15.3+ (Recommended)
We recommend using `initBotId()` in
Next.js (/app)SvelteKitNuxtOther frameworks
instrumentation-client.ts
TypeScript
TypeScript JavaScript Bash
```
import { initBotId } from 'botid/client/core';

// Define the paths that need bot protection.
// These are paths that are routed to by your app.
// These can be:
// - API endpoints (e.g., '/api/checkout')
// - Server actions invoked from a page (e.g., '/dashboard')
// - Dynamic routes (e.g., '/api/create/*')

initBotId({
  protect: [
    {
      path: '/api/checkout',
      method: 'POST',
    },
    {
      // Wildcards can be used to expand multiple segments
      // /team/*/activate will match
      // /team/a/activate
      // /team/a/b/activate
      // /team/a/b/c/activate
      // ...
      path: '/team/*/activate',
      method: 'POST',
    },
    {
      // Wildcards can also be used at the end for dynamic routes
      path: '/api/user/*',
      method: 'POST',
    },
  ],
});
```

Next.js < 15.3
Next.js (/app)SvelteKitNuxtOther frameworks
app/layout.tsx
TypeScript
TypeScript JavaScript Bash
```
import { BotIdClient } from 'botid/client';
import { ReactNode } from 'react';

const protectedRoutes = [
  {
    path: '/api/checkout',
    method: 'POST',
  },
];

type RootLayoutProps = {
  children: ReactNode;
};

export default function RootLayout({ children }: RootLayoutProps) {
  return (
    <html lang="en">
      <head>
        <BotIdClient protect={protectedRoutes} />
      </head>
      <body>{children}</body>
    </html>
  );
}
```

  4. ###  [Perform BotID checks on the server](https://vercel.com/docs/botid/get-started#perform-botid-checks-on-the-server)[](https://vercel.com/docs/botid/get-started#perform-botid-checks-on-the-server)
Use `checkBotId()` on the routes configured in the `<BotIdClient/>` component.
Important configuration requirements: - Not adding the protected route to `<BotIdClient />` will result in `checkBotId()` failing. The client side component dictates which requests to attach special headers to for classification purposes. - Local development always returns `isBot: false` unless you configure the `developmentOptions` option on `checkBotId()`. [Learn more about local development behavior](https://vercel.com/docs/botid/local-development-behavior).
Using API routes
Next.js (/app)SvelteKitNuxtOther frameworks
app/api/sensitive/route.ts
TypeScript
TypeScript JavaScript Bash
```
import { checkBotId } from 'botid/server';
import { NextRequest, NextResponse } from 'next/server';

export async function POST(request: NextRequest) {
  const verification = await checkBotId();

  if (verification.isBot) {
    return NextResponse.json({ error: 'Access denied' }, { status: 403 });
  }

  const data = await processUserRequest(request);

  return NextResponse.json({ data });
}

async function processUserRequest(request: NextRequest) {
  // Your business logic here
  const body = await request.json();
  // Process the request...
  return { success: true };
}
```

Using Server Actions
Next.js (/app)SvelteKitNuxtOther frameworks
app/actions/create-user.ts
TypeScript
TypeScript JavaScript Bash
```
'use server';

import { checkBotId } from 'botid/server';

export async function createUser(formData: FormData) {
  const verification = await checkBotId();

  if (verification.isBot) {
    throw new Error('Access denied');
  }

  const userData = {
    name: formData.get('name') as string,
    email: formData.get('email') as string,
  };

  const user = await saveUser(userData);
  return { success: true, user };
}

async function saveUser(userData: { name: string; email: string }) {
  // Your database logic here
  console.log('Saving user:', userData);
  return { id: '123', ...userData };
}
```

BotID actively runs JavaScript on page sessions and sends headers to the server. If you test with `curl` or visit a protected route directly, BotID will block you in production. To effectively test, make a `fetch` request from a page in your application to the protected route.
  5. ###  [Enable BotID deep analysis in Vercel (Recommended)](https://vercel.com/docs/botid/get-started#enable-botid-deep-analysis-in-vercel-recommended)[](https://vercel.com/docs/botid/get-started#enable-botid-deep-analysis-in-vercel-recommended)
BotID Deep Analysis are available on [Enterprise](https://vercel.com/docs/plans/enterprise) and [Pro](https://vercel.com/docs/plans/pro) plans
From the [Vercel dashboard](https://vercel.com/dashboard)
     * Select your Project
     * Click the Firewall tab
     * Click Rules
     * Enable Vercel BotID Deep Analysis
[Go to Firewall Rules](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Ffirewall%2Frules&title=Open+Firewall+Rules)
