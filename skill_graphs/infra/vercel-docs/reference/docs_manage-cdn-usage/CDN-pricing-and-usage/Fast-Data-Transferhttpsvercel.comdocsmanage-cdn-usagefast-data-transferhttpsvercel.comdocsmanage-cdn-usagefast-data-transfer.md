##  [Fast Data Transfer](https://vercel.com/docs/manage-cdn-usage#fast-data-transfer)[](https://vercel.com/docs/manage-cdn-usage#fast-data-transfer)
When a user visits your site, the data transfer between Vercel's CDN and the user's device gets measured as Fast Data Transfer. The data transferred gets measured based on data volume transferred, and can include assets such as your homepage, images, and other static files.
Fast Data Transfer usage incurs alongside [CDN Requests](https://vercel.com/docs/manage-cdn-usage#cdn-requests) every time a user visits your site, and is [priced regionally](https://vercel.com/docs/pricing/regional-pricing).
Select a Region
Cape Town, South Africa (cpt1) Cleveland, USA (cle1) Dubai, UAE (dxb1) Dublin, Ireland (dub1) Frankfurt, Germany (fra1) Hong Kong (hkg1) London, UK (lhr1) Montréal, Canada (yul1) Mumbai, India (bom1) Osaka, Japan (kix1) Paris, France (cdg1) Portland, USA (pdx1) San Francisco, USA (sfo1) São Paulo, Brazil (gru1) Seoul, South Korea (icn1) Singapore (sin1) Stockholm, Sweden (arn1) Sydney, Australia (syd1) Tokyo, Japan (hnd1) Washington, D.C., USA (iad1)
Managed Infrastructure pricing Resource | Hobby Included | On-demand Rates
---|---|---
Resource | Hobby Included | On-demand Rates
[Fast Data Transfer](https://vercel.com/docs/pricing/regional-pricing) | First 100 GB | $0.15 per 1 GB
###  [Optimizing Fast Data Transfer](https://vercel.com/docs/manage-cdn-usage#optimizing-fast-data-transfer)[](https://vercel.com/docs/manage-cdn-usage#optimizing-fast-data-transfer)
The Fast Data Transfer chart on Usage in your dashboard sidebar shows the incoming and outgoing data transfer of your projects.
  * The Direction filter allows you to see the data transfer direction (incoming or outgoing)
  * The Projects filter allows you to see the data transfer of a specific project
  * The Regions filter allows you to see the data transfer of a specific region. This is can be helpful due to the nature of [regional pricing and Fast Data Transfer](https://vercel.com/docs/pricing/regional-pricing)


As with all charts on the Usage section in the sidebar, you can select the caret icon to view the chart as a full page.
To optimize Fast Data Transfer, you must optimize the assets that are being transferred. You can do this by:
  * Using Vercel's Image Optimization: [Image Optimization](https://vercel.com/docs/image-optimization) on Vercel uses advanced compression and modern file formats to reduce image and video file sizes. This decreases page load times and reduces Fast Data Transfer costs by serving optimized media tailored to the requesting device
  * Analyzing your bundles: See your preferred frameworks documentation for guidance on how to analyze and reduce the size of your bundles. For Next.js, see the


To further analyze the data transfer of your projects, you can use [Observability](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fobservability&title=Go+to+Observability) in the sidebar.
###  [Calculating Fast Data Transfer](https://vercel.com/docs/manage-cdn-usage#calculating-fast-data-transfer)[](https://vercel.com/docs/manage-cdn-usage#calculating-fast-data-transfer)
Fast Data Transfer is calculated based on the full size of each HTTP request and response transmitted to or from Vercel's [CDN](https://vercel.com/docs/cdn). This includes the body, all headers, the full URL and any compression. Incoming data transfer corresponds to the request, and outgoing corresponds to the response.
