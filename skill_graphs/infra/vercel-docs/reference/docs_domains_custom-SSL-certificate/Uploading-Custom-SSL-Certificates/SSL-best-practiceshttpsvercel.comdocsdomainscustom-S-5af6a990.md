##  [SSL best practices](https://vercel.com/docs/domains/custom-SSL-certificate#ssl-best-practices)[](https://vercel.com/docs/domains/custom-SSL-certificate#ssl-best-practices)
When uploading your SSL certificate, you should note the following:
  1. The automatically generated certificate will remain in place, but a custom certificate is prioritized over the existing certificate. This means that if a custom certificate is uploaded and then later removed, Vercel will revert to the automatically generated certificate.
  2. You can include canonical names CN's (CN's) for other subdomains on the certificate without needing to add these domains to Vercel. The certificate will be served on these domains if or when they are added.
  3. Wildcards certificates can be uploaded.
  4. Certificates with an explicitly defined subdomain are prioritized over a wildcard certificate when both are valid for a given subdomain.
  5. Vercel cannot automatically renew custom certificates. If a custom certificate is within 5 days of expiration, an automatically generated certificate will be served in its place to prevent downtime.
  6. Certificates imported to Vercel require the Subject Alternative Name (SAN) to be present
