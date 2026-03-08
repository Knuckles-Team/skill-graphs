##  [Adding DNS Records](https://vercel.com/docs/domains/managing-dns-records#adding-dns-records)[](https://vercel.com/docs/domains/managing-dns-records#adding-dns-records)
  1. ###  [Selecting your Domain](https://vercel.com/docs/domains/managing-dns-records#selecting-your-domain)[](https://vercel.com/docs/domains/managing-dns-records#selecting-your-domain)
On your team's [dashboard](https://vercel.com/dashboard), open Domains in the sidebar. From the Domains page, click on a domain of your choice to view its Advanced Settings page.
  2. ###  [Add DNS Record](https://vercel.com/docs/domains/managing-dns-records#add-dns-record)[](https://vercel.com/docs/domains/managing-dns-records#add-dns-record)
Once on the Advanced Settings page of your domain, select the Enable Vercel DNS button to fill out the DNS Record form. Once complete, click on the Add button.
![DNS Records form to add a new DNS Record.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fdns-records-form.png&w=3840&q=75)![DNS Records form to add a new DNS Record.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fdns-records-form-dark.png&w=3840&q=75)DNS Records form to add a new DNS Record.
You can then create a new DNS record with the following data:
     * Name: The prefix or location of the record. For
     * Type: Types can be `A`, `AAAA`, `ALIAS`, `CAA`, `CNAME`, `HTTPS`, `MX`, `NS`, `SRV`, or `TXT`.
     * Value: The value of the record.
     * TTL: Default is 60 seconds. For advanced users, this value can be customized.
     * Comment: An optional comment to provide context on what this record is for.
     * More: Some records will require more data. MX records, for example, will request "priority".
Once a DNS record has been added, it can take up to 24 hours to the DNS records to fully update and any local caches to be cleared.
