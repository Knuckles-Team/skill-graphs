##  [Migrating DNS records from an external registrar](https://vercel.com/docs/domains/managing-dns-records#migrating-dns-records-from-an-external-registrar)[](https://vercel.com/docs/domains/managing-dns-records#migrating-dns-records-from-an-external-registrar)
Once you have added a [domain to your Vercel project](https://vercel.com/docs/concepts/projects/custom-domains) and also verified the certificate is working as expected, you can choose three options of records to finally complete the migration: A, CNAME, or Nameservers. In case you decide to use an A or a CNAME record, then you can change those records in your DNS provider to make Vercel serve your deployment from the selected domain, as instructed on your dashboard.
If you decide to change the Nameservers of your domain, you can follow the below instructions which will help you migrate your DNS configuration from any provider and avoid downtime.
###  [Clone the Current DNS Configuration](https://vercel.com/docs/domains/managing-dns-records#clone-the-current-dns-configuration)[](https://vercel.com/docs/domains/managing-dns-records#clone-the-current-dns-configuration)
To locate the current DNS provider of your domain, you can run the following command:
terminal
```
$ dig NS example.com +short
```

Checking the DNS authority for a domain using the terminal.
The result will show the current DNS authority. Next, you'll need to locate your DNS records from the provider's dashboard.
After you've successfully located all records associated with your domain, you may now add them to Vercel. You can either do this manually or by importing a zone file.
Importing a zone file
If you have downloaded a zone file from your existing file, you may use the following command to upload that to Vercel:
```
vercel dns import [your-domain] [zonefile]
```

If you do not apply a custom zone file, transferring in a domain automatically applies the default Vercel DNS settings.
###  [Verify the Records](https://vercel.com/docs/domains/managing-dns-records#verify-the-records)[](https://vercel.com/docs/domains/managing-dns-records#verify-the-records)
To verify the records, you can now query the DNS configuration that will be served by Vercel:
terminal
```
$ dig A api.example.com +short @ns1.vercel-dns.com
```

Checking the DNS configuration of the A record under "api" served by Vercel.
Then, check the DNS records from the existing provider to make sure they match. If you were moving your DNS from [Cloudflare](https://vercel.com/docs/integrations/cloudflare), for example, the correct command would be:
terminal
```
$ dig A api.example.com +short @example.ns.cloudflare.com
```

Checking the DNS configuration of the A record under "api" served by Cloudflare. The example should be replaced with the authoritative nameserver given by your provider.
Before proceeding, we recommend checking every record you moved. For more insight into the DNS resolution, remove the `+short` flag.
###  [Switch the Nameservers](https://vercel.com/docs/domains/managing-dns-records#switch-the-nameservers)[](https://vercel.com/docs/domains/managing-dns-records#switch-the-nameservers)
In your registrar's dashboard (where you bought the domain), change the Nameservers to your new provider. Nameserver changes can take up to 48 hours to propagate. If you bought the domain from Vercel, you can [manage nameservers](https://vercel.com/docs/concepts/projects/domains/managing-nameservers) from the [domains page](https://vercel.com/dashboard/domains).
* * *
[ Previous Working with DNS ](https://vercel.com/docs/domains/working-with-dns)[ Next Working with Nameservers ](https://vercel.com/docs/domains/working-with-nameservers)
Was this helpful?
Send
On this page
  * [Adding DNS Records](https://vercel.com/docs/domains/managing-dns-records#adding-dns-records)
  * [Selecting your Domain](https://vercel.com/docs/domains/managing-dns-records#selecting-your-domain)
  * [Add DNS Record](https://vercel.com/docs/domains/managing-dns-records#add-dns-record)
  * [Verifying DNS Records](https://vercel.com/docs/domains/managing-dns-records#verifying-dns-records)
  * [Removing DNS Records](https://vercel.com/docs/domains/managing-dns-records#removing-dns-records)
  * [DNS Presets](https://vercel.com/docs/domains/managing-dns-records#dns-presets)
  * [Migrating DNS records from an external registrar](https://vercel.com/docs/domains/managing-dns-records#migrating-dns-records-from-an-external-registrar)
  * [Clone the Current DNS Configuration](https://vercel.com/docs/domains/managing-dns-records#clone-the-current-dns-configuration)
  * [Verify the Records](https://vercel.com/docs/domains/managing-dns-records#verify-the-records)
  * [Switch the Nameservers](https://vercel.com/docs/domains/managing-dns-records#switch-the-nameservers)


Copy as MarkdownGive feedbackAsk AI about this page
[Domains](https://vercel.com/docs/domains)
Managing DNS Records
