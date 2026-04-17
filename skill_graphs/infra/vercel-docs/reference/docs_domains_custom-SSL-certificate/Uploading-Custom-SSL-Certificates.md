# Uploading Custom SSL Certificates
Last updated December 19, 2025
Uploading Custom SSL Certificates are available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
By default, Vercel provides all domains with custom SSL certificates. However, Enterprise teams can upload a custom SSL certificate. This allows for Enterprise teams to serve their own SSL certificate on a Custom Domain on Vercel's global network, rather than the automatically generated certificate.
Custom SSL certificates can be uploaded through the [Domains section in the sidebar on your team's dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fdomains&title=Go+to+team%27s+domains+page), or by using the [Vercel REST API](https://vercel.com/docs/rest-api/reference/endpoints/certs/upload-a-cert#upload-a-cert).
Want to talk to our team?
This feature is available on the Enterprise plan.
Schedule Call
Uploading a custom certificate follows a three step process:
  1. Providing the private key for the certificate
  2. Providing the certificate itself
  3. Providing the Certificate Authority root certificate such as one of


The content of each element must be copied and pasted into the input box directly. The certificate and private key can be extracted from the
certificate.pem
```
-----BEGIN CERTIFICATE-----
<Certificate body will be here>
-----END CERTIFICATE-----
```

private-key.pem
```
-----BEGIN PRIVATE KEY-----
<Private key body will be here>
-----END PRIVATE KEY-----
```
