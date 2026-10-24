##  [CDN Requests](https://vercel.com/docs/manage-cdn-usage#cdn-requests)[](https://vercel.com/docs/manage-cdn-usage#cdn-requests)
When visiting your site, requests are made to a Vercel CDN [region](https://vercel.com/docs/pricing/regional-pricing). Traffic is routed to the nearest region to the visitor. Static assets and functions all incur CDN Requests.
CDN Requests appear as Edge Requests in your billing dashboard and usage charts.
Select a Region
Cape Town, South Africa (cpt1) Cleveland, USA (cle1) Dubai, UAE (dxb1) Dublin, Ireland (dub1) Frankfurt, Germany (fra1) Hong Kong (hkg1) London, UK (lhr1) Montréal, Canada (yul1) Mumbai, India (bom1) Osaka, Japan (kix1) Paris, France (cdg1) Portland, USA (pdx1) San Francisco, USA (sfo1) São Paulo, Brazil (gru1) Seoul, South Korea (icn1) Singapore (sin1) Stockholm, Sweden (arn1) Sydney, Australia (syd1) Tokyo, Japan (hnd1) Washington, D.C., USA (iad1)
Managed Infrastructure pricing Resource | Hobby Included | On-demand Rates
---|---|---
Resource | Hobby Included | On-demand Rates
[Edge Requests](https://vercel.com/docs/pricing/regional-pricing) | First 1,000,000 | $2.00 per 1,000,000 Requests
[Edge Request Additional CPU Duration](https://vercel.com/docs/pricing/regional-pricing) | N/A | $0.30 per 1 Hour
###  [Managing CDN Requests](https://vercel.com/docs/manage-cdn-usage#managing-cdn-requests)[](https://vercel.com/docs/manage-cdn-usage#managing-cdn-requests)
You can view the Edge Requests chart on Usage in your dashboard sidebar. This chart shows:
  * Count: The total count of requests made to your deployments
  * Projects: The projects that received the requests
  * Region: The region where the requests are made


As with all charts on the Usage section in the sidebar, you can select the caret icon to view the chart in full screen mode.
###  [Optimizing CDN Requests](https://vercel.com/docs/manage-cdn-usage#optimizing-cdn-requests)[](https://vercel.com/docs/manage-cdn-usage#optimizing-cdn-requests)
Frameworks such as [Next.js](https://vercel.com/docs/frameworks/nextjs), [SvelteKit](https://vercel.com/docs/frameworks/sveltekit), [Nuxt](https://vercel.com/docs/frameworks/nuxt), and others help build applications that automatically reduce unnecessary requests.
The most significant opportunities for optimizing CDN Requests include:
  * Identifying frequent re-mounting: If your application involves rendering a large number of images and re-mounts them, it can inadvertently increase requests
    * To identify: Use your browsers devtools and browse your site. Pay attention to responses with a 304 status code on repeated requests paths. This indicates content that has been fetched multiple times
  * Excessive polling or data fetching: Applications that poll APIs for live updates, or use tools like SWR or React Query to reload data on user focus can contribute to increased requests
