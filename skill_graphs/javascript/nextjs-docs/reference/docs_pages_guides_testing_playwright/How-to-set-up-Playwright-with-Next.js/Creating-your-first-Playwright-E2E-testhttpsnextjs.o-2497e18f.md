## Creating your first Playwright E2E test[](https://nextjs.org/docs/pages/guides/testing/playwright#creating-your-first-playwright-e2e-test)
Create two new Next.js pages:
pages/index.ts
```
import Link from 'next/link'

export default function Home() {
  return (
    <div>
      <h1>Home</h1>
      <Link href="/about">About</Link>
    </div>
  )
}
```

pages/about.ts
```
import Link from 'next/link'

export default function About() {
  return (
    <div>
      <h1>About</h1>
      <Link href="/">Home</Link>
    </div>
  )
}
```

Then, add a test to verify that your navigation is working correctly:
tests/example.spec.ts
```
import { test, expect } from '@playwright/test'

test('should navigate to the about page', async ({ page }) => {
  // Start from the index page (the baseURL is set via the webServer in the playwright.config.ts)
  await page.goto('http://localhost:3000/')
  // Find an element with the text 'About' and click on it
  await page.click('text=About')
  // The new URL should be "/about" (baseURL is used there)
  await expect(page).toHaveURL('http://localhost:3000/about')
  // The new page should contain an h1 with "About"
  await expect(page.locator('h1')).toContainText('About')
})
```

> **Good to know** : You can use `page.goto("/")` instead of `page.goto("http://localhost:3000/")`, if you add `playwright.config.ts`
### Running your Playwright tests[](https://nextjs.org/docs/pages/guides/testing/playwright#running-your-playwright-tests)
Playwright will simulate a user navigating your application using three browsers: Chromium, Firefox and Webkit, this requires your Next.js server to be running. We recommend running your tests against your production code to more closely resemble how your application will behave.
Run `npm run build` and `npm run start`, then run `npx playwright test` in another terminal window to run the Playwright tests.
> **Good to know** : Alternatively, you can use the
### Running Playwright on Continuous Integration (CI)[](https://nextjs.org/docs/pages/guides/testing/playwright#running-playwright-on-continuous-integration-ci)
Playwright will by default run your tests in the `npx playwright install-deps`.
You can learn more about Playwright and Continuous Integration from these resources:
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
