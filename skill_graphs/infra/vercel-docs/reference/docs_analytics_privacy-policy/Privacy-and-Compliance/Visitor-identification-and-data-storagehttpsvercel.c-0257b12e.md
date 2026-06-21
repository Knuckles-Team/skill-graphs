##  [Visitor identification and data storage](https://vercel.com/docs/drains#visitor-identification-and-data-storage)[](https://vercel.com/docs/drains#visitor-identification-and-data-storage)
Vercel Web Analytics allows you to track your website traffic and gather valuable insights without using any third-party cookies, instead end users are identified by a hash created from the incoming request.
The lifespan of a visitor session is not stored permanently, it is automatically discarded after 24 hours.
After following the dashboard instructions to enable Vercel Web Analytics, see our [Quickstart](https://vercel.com/docs/analytics/quickstart) for a step-by-step tutorial on integrating the Vercel Web Analytics script into your application. After successfully completing the quickstart and deploying your application, the script will begin transmitting page view data to Vercel's servers.
All page views will automatically be tracked by Vercel Web Analytics, including both fresh page loads and client-side page transitions.
###  [Data point information](https://vercel.com/docs/drains#data-point-information)[](https://vercel.com/docs/drains#data-point-information)
The following information may be stored with every data point:
Collected Value | Example Value
---|---
Event Timestamp | 2020-10-29 09:06:30
URL | `/blog/nextjs-10`
Dynamic Path | `/blog/[slug]`
Referrer |
Query Params (Filtered) | `?ref=hackernews`
Geolocation | US, California, San Francisco
Device OS & Version | Android 10
Browser & Version | Chrome 86 (Blink)
Device Type | Mobile (or Desktop/Tablet)
Web Analytics Script Version | 1.0.0
