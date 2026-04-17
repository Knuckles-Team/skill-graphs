##  [Common domain issues](https://vercel.com/docs/domains/managing-dns-records#common-domain-issues)[](https://vercel.com/docs/domains/managing-dns-records#common-domain-issues)
###  [Domains and emails](https://vercel.com/docs/domains/managing-dns-records#domains-and-emails)[](https://vercel.com/docs/domains/managing-dns-records#domains-and-emails)
When you buy a new domain, you may want to also set up an email address with this domain. Vercel does not provide a mail service for domains purchased with or transferred into it. To learn how to set up email, see [How do I send and receive emails with my Vercel purchased domain?](https://vercel.com/kb/guide/using-email-with-your-vercel-domain)
When you add your custom domain to a project and use Vercel's nameservers, you will need to add `MX` records to continue receiving email. To learn how to add `MX` records, see [Why am I no longer receiving email after adding my domain to Vercel?](https://vercel.com/kb/guide/why-has-email-stopped-working)
###  [Purchasing a domain through Vercel](https://vercel.com/docs/domains/managing-dns-records#purchasing-a-domain-through-vercel)[](https://vercel.com/docs/domains/managing-dns-records#purchasing-a-domain-through-vercel)
All domain purchases and renewals through Vercel are final once processed. For more information, see [Can I get a refund for a domain purchased or renewed with Vercel?](https://vercel.com/kb/guide/can-i-get-a-refund-for-a-domain-purchased-or-renewed-with-vercel)
###  [Pending domain purchases](https://vercel.com/docs/domains/managing-dns-records#pending-domain-purchases)[](https://vercel.com/docs/domains/managing-dns-records#pending-domain-purchases)
When a domain purchase does not go through immediately, your payment method may show a temporary authorization — this is a pending hold, not a completed charge. It will be automatically released by your bank if the domain is not successfully registered.
If the purchase is processing, your domain will appear in the [Domains tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fdomains&title=Domains+page) with a “Pending” status. Most purchases complete within minutes, but some TLDs may take up to 5 days to finalize. There is no need to retry the purchase or contact support while the domain is pending. You will receive a confirmation email once the registration completes.
###  [Pending verification](https://vercel.com/docs/domains/managing-dns-records#pending-verification)[](https://vercel.com/docs/domains/managing-dns-records#pending-verification)
If verification is needed, you will receive an email with instructions from Vercel. You will also see an alert on your team's domain page, which you can access through the [Domain Dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fdomains%2F&title=). From there, you can resend the verification email or update your registrant information and email address.
###  [Emoji and ASCII support](https://vercel.com/docs/domains/managing-dns-records#emoji-and-ascii-support)[](https://vercel.com/docs/domains/managing-dns-records#emoji-and-ascii-support)
You will need to convert the domain to `jérémie.fr` can do so in the form of `xn--jrmie-bsab.fr`.
###  [Unable to transfer-in a domain](https://vercel.com/docs/domains/managing-dns-records#unable-to-transfer-in-a-domain)[](https://vercel.com/docs/domains/managing-dns-records#unable-to-transfer-in-a-domain)
60 days:
  * between transfers
  * between a new registration and a subsequent transfer


If you transfer before this time, the transfer will fail. Besides this restriction, some DNS providers may further restrict domain transferring by default as a security measure, unless the owner explicitly turns off their protection setting. Please refer to the DNS provider's documentation for more details.
###  [Working with Apex domain](https://vercel.com/docs/domains/managing-dns-records#working-with-apex-domain)[](https://vercel.com/docs/domains/managing-dns-records#working-with-apex-domain)
When you add an [apex domain](https://vercel.com/docs/domains/working-with-domains#subdomains-wildcard-domains-and-apex-domains) (e.g. `example.com`) to your project, Vercel provides you with details, including an IP address, to add as an `A` record in your DNS configuration, as opposed to a `CNAME` record.
The main reason for that is the DNS `If a CNAME RR is present at a node, no other data should be present`. Because an apex domain requires `NS` records and usually some other records, such as `MX` (for a mail service), adding a `CNAME` at the zone apex would violate this rule and likely cause an issue on your domain. Therefore, we encourage you to use an `A` record at your zone apex instead.
###  [Domain IP address and geographic regions](https://vercel.com/docs/domains/managing-dns-records#domain-ip-address-and-geographic-regions)[](https://vercel.com/docs/domains/managing-dns-records#domain-ip-address-and-geographic-regions)
When you configure an apex domain (example.com) as a custom domain for your project on Vercel, Vercel will be give you an IP address to add as an A record in your DNS configuration. Although this IP address resolves to a specific geographic location, it does not mean that when your users point to your domain, they will be sent to this specific geographic location to resolve the domain.
This is because Vercel uses
###  [Domain ownership errors](https://vercel.com/docs/domains/managing-dns-records#domain-ownership-errors)[](https://vercel.com/docs/domains/managing-dns-records#domain-ownership-errors)
When you add a domain to your project, Vercel checks if it is already associated with a [Personal Account or Team](https://vercel.com/docs/accounts). A domain can only be associated with _one_ Personal Account or Team at a time.
The following table shows errors that can be encountered when adding a domain to your project:
Error Text | Description
---|---
`This team has already registered this domain` | The domain you are trying to add is already connected to the team you have selected.
`You have already registered this domain` | The domain you are trying to add is already connected to the Personal Account you have selected.
`The domain mydomain.com is not available` or `Another Vercel account is using this domain` | This domain is already linked to another Vercel account or team.

If you have access to that account: Transfer the domain to your current account via the [Domains dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fdomains&title=Domains+Dashboard) by following [the working with domains guide](https://vercel.com/docs/domains/working-with-domains/transfer-your-domain).

If you own the domain but not the other account: Use the Add Existing option on the [Domains dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fdomains&title=Domains+Dashboard). You'll receive a TXT record to add to your DNS to verify ownership. Once verified, the domain will automatically transfer to your account.
