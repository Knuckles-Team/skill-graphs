##  [Manage IP Address visibility for Query](https://vercel.com/docs/query#manage-ip-address-visibility-for-query)[](https://vercel.com/docs/query#manage-ip-address-visibility-for-query)
Managing IP Address visibility is available on [Enterprise](https://vercel.com/docs/plans/enterprise) and [Pro](https://vercel.com/docs/plans/pro) plans
Those with the [owner, admin](https://vercel.com/docs/rbac/access-roles#owner,%20admin-role) role can access this feature
Vercel creates events each time a request is made to your website. These events include unique parameters such as execution time and bandwidth used.
Certain events such as `public_ip` may be considered personal information under certain data protection laws. To hide IP addresses from your query:
  1. Go to the Vercel [dashboard](https://vercel.com/d?to=%2Fdashboard&title=Open+Dashboard) and ensure your team is selected in the team switcher.
  2. Open Settings in the sidebar and navigate to Security & Privacy.
  3. Under IP Address Visibility, toggle the switch next to "Off" so the text reads IP addresses are currently hidden in the Vercel Dashboard..


For business purposes, such as DDoS mitigation, Vercel will still collect IP addresses.
