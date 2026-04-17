##  [Examples](https://vercel.com/docs/getting-started-with-vercel#examples)[](https://vercel.com/docs/getting-started-with-vercel#examples)
This rule will catch any pages or routes that are using `process.env.NEXT_PUBLIC_*` environment variables.
In the following example, we are using a local variable to initialize our analytics service. As the variable will be visible in the client, a review of the code is required, and the usage should be added to the [allowlist](https://vercel.com/docs/conformance/allowlist).
app/dashboard/page.tsx
```
setupAnalyticsService(process.env.NEXT_PUBLIC_ANALYTICS_ID);

function HomePage() {
  return <h1>Hello World</h1>;
}

export default HomePage;
```
