##  [Verifying the Certificate](https://vercel.com/docs/domains/working-with-domains#verifying-the-certificate)[](https://vercel.com/docs/domains/working-with-domains#verifying-the-certificate)
Before you change the DNS records of your domain, you can verify if the certificate is correct and will be accepted by browsers. Run the following command:
terminal
```
curl https://example.com --resolve example.com:443:76.76.21.21 -I
```

curl command that sends a request directly to Vercel, ignoring the DNS configuration of the domain.
If the request is successful, the certificate is working and you can proceed with the migration.
