##  [Using self-signed certificates](https://vercel.com/docs/domains/custom-SSL-certificate#using-self-signed-certificates)[](https://vercel.com/docs/domains/custom-SSL-certificate#using-self-signed-certificates)
In rare cases, you may need to upload a self-signed certificate to Vercel. You can generate a custom self-signed certificate for your domain with OpenSSL:
```
openssl req -x509 -newkey rsa:4096 \
  -keyout key.pem -out cert.pem \
  -sha256 -days 360 -nodes \
  -subj "/CN=sub.example.com" \
  -addext "subjectAltName=DNS:sub.example.com"
```

This generates a `key.pem` file containing the private key and a `cert.pem` file containing the self-signed certificate. When uploading this certificate to Vercel, use `cert.pem` also for the Certificate Authority field.
* * *
[ Previous Working with SSL ](https://vercel.com/docs/domains/working-with-ssl)[ Next Pre-Generate SSL Certificates ](https://vercel.com/docs/domains/pre-generating-ssl-certs)
Was this helpful?
Send
On this page
  * [SSL best practices](https://vercel.com/docs/domains/custom-SSL-certificate#ssl-best-practices)
  * [Using self-signed certificates](https://vercel.com/docs/domains/custom-SSL-certificate#using-self-signed-certificates)


Copy as MarkdownGive feedbackAsk AI about this page
