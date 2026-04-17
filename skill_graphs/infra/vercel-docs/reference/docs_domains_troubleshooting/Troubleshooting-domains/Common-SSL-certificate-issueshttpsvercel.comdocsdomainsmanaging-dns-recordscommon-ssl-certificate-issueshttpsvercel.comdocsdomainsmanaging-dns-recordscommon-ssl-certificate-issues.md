##  [Common SSL certificate issues](https://vercel.com/docs/domains/managing-dns-records#common-ssl-certificate-issues)[](https://vercel.com/docs/domains/managing-dns-records#common-ssl-certificate-issues)
There are many reasons why a certificate may not be generated. As the first starting point, we recommend testing your domain with:
For non-wildcard domains, we use
For wildcard domains, only [nameservers method](https://vercel.com/docs/domains/troubleshooting#configuring-nameservers-for-wildcard-domains) to handle DNS-01 challenge requests with Vercel's nameservers automatically.
###  [Missing `CAA` records](https://vercel.com/docs/domains/managing-dns-records#missing-caa-records)[](https://vercel.com/docs/domains/managing-dns-records#missing-caa-records)
Since we use Let's Encrypt for our automatic SSL certificates, you must add a `CAA` record with the value `0 issue "letsencrypt.org"` if other `CAA` records already exist on your domain.
You can check if your domain currently has any `CAA` records by running the `dig -t CAA +noall +ans example.com` command on your terminal, or check with `RR Type` to `CAA` and resolve).
For more information, see [Why is my domain not automatically generating an SSL certificate?](https://vercel.com/kb/guide/domain-not-generating-ssl-certificate)
###  [Existing `_acme-challenge` record](https://vercel.com/docs/domains/managing-dns-records#existing-_acme-challenge-record)[](https://vercel.com/docs/domains/managing-dns-records#existing-_acme-challenge-record)
An `_acme-challenge` record allows Let's Encrypt to verify the domain ownership using `dig -t TXT _acme-challenge.example.com` or `dig -t TXT _acme-challenge.subdomain.example.com`
If the domain was previously hosted on a different provider, and if the `_acme-challenge` record resolves to something, please consider [removing the DNS record](https://vercel.com/docs/domains/managing-dns-records#removing-dns-records). This will prevent any provider (other than the one in the DNS record) from provisioning certificates for that domain.
###  [Rewriting or redirecting `/.well-known`](https://vercel.com/docs/domains/managing-dns-records#rewriting-or-redirecting-/.well-known)[](https://vercel.com/docs/domains/managing-dns-records#rewriting-or-redirecting-/.well-known)
The /.well-known path is reserved and cannot be redirected or rewritten. Only Enterprise teams can configure custom SSL. [Contact sales](https://vercel.com/contact/sales) to learn more.
* * *
[ Previous Working with DNS ](https://vercel.com/docs/domains/working-with-dns)[ Next Working with Nameservers ](https://vercel.com/docs/domains/working-with-nameservers)
Was this helpful?
Send
On this page
  * [Misconfigured domain issues](https://vercel.com/docs/domains/managing-dns-records#misconfigured-domain-issues)
  * [Common DNS issues](https://vercel.com/docs/domains/managing-dns-records#common-dns-issues)
  * [DNS record propagation times](https://vercel.com/docs/domains/managing-dns-records#dns-record-propagation-times)
  * [IPv6 support](https://vercel.com/docs/domains/managing-dns-records#ipv6-support)
  * [Syntax errors debugging](https://vercel.com/docs/domains/managing-dns-records#syntax-errors-debugging)
  * [Using the domain as part of the Name argument](https://vercel.com/docs/domains/managing-dns-records#using-the-domain-as-part-of-the-name-argument)
  * [Absolute CNAME records](https://vercel.com/docs/domains/managing-dns-records#absolute-cname-records)
  * [Common Nameserver issues](https://vercel.com/docs/domains/managing-dns-records#common-nameserver-issues)
  * [Configuring nameservers for wildcard domains](https://vercel.com/docs/domains/managing-dns-records#configuring-nameservers-for-wildcard-domains)
  * [Common domain issues](https://vercel.com/docs/domains/managing-dns-records#common-domain-issues)
  * [Domains and emails](https://vercel.com/docs/domains/managing-dns-records#domains-and-emails)
  * [Purchasing a domain through Vercel](https://vercel.com/docs/domains/managing-dns-records#purchasing-a-domain-through-vercel)
  * [Pending domain purchases](https://vercel.com/docs/domains/managing-dns-records#pending-domain-purchases)
  * [Pending verification](https://vercel.com/docs/domains/managing-dns-records#pending-verification)
  * [Emoji and ASCII support](https://vercel.com/docs/domains/managing-dns-records#emoji-and-ascii-support)
  * [Unable to transfer-in a domain](https://vercel.com/docs/domains/managing-dns-records#unable-to-transfer-in-a-domain)
  * [Working with Apex domain](https://vercel.com/docs/domains/managing-dns-records#working-with-apex-domain)
  * [Domain IP address and geographic regions](https://vercel.com/docs/domains/managing-dns-records#domain-ip-address-and-geographic-regions)
  * [Domain ownership errors](https://vercel.com/docs/domains/managing-dns-records#domain-ownership-errors)
  * [Common SSL certificate issues](https://vercel.com/docs/domains/managing-dns-records#common-ssl-certificate-issues)
  * [Missing CAA records](https://vercel.com/docs/domains/managing-dns-records#missing-caa-records)
  * [Existing _acme-challenge record](https://vercel.com/docs/domains/managing-dns-records#existing-_acme-challenge-record)
  * [Rewriting or redirecting /.well-known](https://vercel.com/docs/domains/managing-dns-records#rewriting-or-redirecting-/.well-known)


Copy as MarkdownGive feedbackAsk AI about this page
