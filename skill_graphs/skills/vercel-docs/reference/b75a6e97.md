##  [DNS Presets](https://vercel.com/docs/domains/managing-dns-records#dns-presets)[](https://vercel.com/docs/domains/managing-dns-records#dns-presets)
Vercel does not provide an email service. To be able to receive emails or add specific DNS configurations through a domain that you've added to Vercel, you need to add the respective DNS Records, such as MX for email or TXT for other services.
Vercel streamlines this process for common third-party services by allowing you to add missing DNS Records using DNS Presets on your dashboard.
  1. From your [dashboard](https://vercel.com/dashboard), open [Domains](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fdomains&title=Go+to+Domains) in the sidebar.
  2. Select the domain you wish to add a preset to and click the Add DNS Preset dropdown on the right:

![Adding a DNS Preset by clicking the Add DNS Preset button.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fdns-presents-light.png&w=640&q=75)![Adding a DNS Preset by clicking the Add DNS Preset button.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fdns-presets-dark.png&w=640&q=75)Adding a DNS Preset by clicking the Add DNS Preset button.
  1. You will be presented with a list of commonly used third-party providers. If your provider is listed, select it, and the necessary DNS Records—such as MX for email or TXT for other services like [Bluesky](https://vercel.com/kb/guide/use-my-domain-bluesky) will automatically be configured on your domain.


If your provider is not listed, please refer to their documentation to find out which DNS Records you need to add.
