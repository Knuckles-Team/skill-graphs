##  [Setting your DNS records and finalizing](https://vercel.com/docs/domains/working-with-domains#setting-your-dns-records-and-finalizing)[](https://vercel.com/docs/domains/working-with-domains#setting-your-dns-records-and-finalizing)
In order to verify ownership of your domain, copy the TXT records into your DNS on the registrar you are using.
Click "Verify" to verify that the records have been set and issue the certificate. DNS records can take time to propagate, so if it doesn't work immediately, it's worth waiting for the records to propagate before taking further action.
![Copy certificates modal containing the TXT records to copy into your DNS registrar](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fcopy-challenges-light.png&w=750&q=75)![Copy certificates modal containing the TXT records to copy into your DNS registrar](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fcopy-challenges-dark.png&w=750&q=75)Copy certificates modal containing the TXT records to copy into your DNS registrar
To check whether the TXT records have propagated, you can use the following command in a terminal of your choice:
terminal
```
nslookup -type=TXT example.com
```

Looking up the TXT records for example.com
Once TXT records have propagated, you can click "Verify" to issue the SSL certificates.
If you choose to issue SSL certificates through the terminal, you can run the command previously used without the `--challenge-only` flag:
terminal
```
vercel certs issue "*.example.com" example.com
```

Issuing a certificate that covers both *.example.com and example.com.
