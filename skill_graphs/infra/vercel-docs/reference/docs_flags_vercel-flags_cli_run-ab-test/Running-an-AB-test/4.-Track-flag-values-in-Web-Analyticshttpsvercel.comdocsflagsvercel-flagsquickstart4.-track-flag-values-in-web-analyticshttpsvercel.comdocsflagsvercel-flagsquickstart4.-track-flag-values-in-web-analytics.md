##  [4. Track flag values in Web Analytics](https://vercel.com/docs/flags/vercel-flags/quickstart#4.-track-flag-values-in-web-analytics)[](https://vercel.com/docs/flags/vercel-flags/quickstart#4.-track-flag-values-in-web-analytics)
Add the `FlagValues` component to your layout so Web Analytics can correlate page views and events with flag values automatically:
app/layout.tsx
```
import { Suspense } from 'react';
import { FlagValues } from 'flags/react';
import { newPricingLayout } from '../flags';

export default async function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html>
      <body>
        {children}
        <Suspense fallback={null}>
          <FlagValues values={{ 'new-pricing-layout': await newPricingLayout() }} />
        </Suspense>
      </body>
    </html>
  );
}
```

See [Web Analytics integration](https://vercel.com/docs/flags/observability/web-analytics) for more on tracking flag values.
