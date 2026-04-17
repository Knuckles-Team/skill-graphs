##  [Generating a Certificate](https://vercel.com/docs/domains/working-with-domains#generating-a-certificate)[](https://vercel.com/docs/domains/working-with-domains#generating-a-certificate)
In order to issue certificates through the dashboard for a domain, first ensure the domain belongs to a team. You can then click into the domain management page, scroll down to "SSL Certificates" and click "Pre-generate SSL certificates". Please note this option is only available if you do not already have any SSL certificates issued for the domain.
![Pre-Generate button found under the SSL Certificates section of the Domain configuration page](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fssl-pregen-light.png&w=3840&q=75)![Pre-Generate button found under the SSL Certificates section of the Domain configuration page](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fssl-pregen-dark.png&w=3840&q=75)Pre-Generate button found under the SSL Certificates section of the Domain configuration page
If you choose to do this through the terminal, you can run the following command to get the challenge records for your domain:
terminal
```
vercel certs issue "*.example.com" example.com --challenge-only
```

Creating the challenge for the certificate that will be used for *.example.com and example.com.
