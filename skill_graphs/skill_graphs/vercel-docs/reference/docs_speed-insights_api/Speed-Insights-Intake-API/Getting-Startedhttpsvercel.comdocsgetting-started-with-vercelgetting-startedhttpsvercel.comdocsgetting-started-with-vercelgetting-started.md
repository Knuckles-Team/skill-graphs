##  [Getting Started](https://vercel.com/docs/getting-started-with-vercel#getting-started)[](https://vercel.com/docs/getting-started-with-vercel#getting-started)
To use the Speed Insights API, you'll need to retrieve the analytics ID for your Vercel project. This value is exposed during the build and can be accessed by `process.env.VERCEL_ANALYTICS_ID` inside Node.js.
Inside your framework or Node.js script, you can then use this value in the `body` of your request to the Vercel Speed Insights API.
`vercel pull` does not pull `VERCEL_ANALYTICS_ID` as the Vercel Analytics ID environment variable is inlined during the build process. It is not part of your project Environment Variables, which can be pulled locally using Vercel CLI.
