##  [Verifying DNS Records](https://vercel.com/docs/domains/managing-dns-records#verifying-dns-records)[](https://vercel.com/docs/domains/managing-dns-records#verifying-dns-records)
Once DNS records have been changed, you may wish to check that these have been set correctly. There are many third-party tools that do this, such as DNS Checker and DNS Map - these show the state of your DNS records in different regions of the world.
You can also use the `dig` command to check the DNS record for your domain:
terminal
```
$ dig A api.example.com +short
```

Verifying the A record set for a domain using the terminal.
terminal
```
$ dig MX example.com +short
```

Verifying the MX record set for a domain using the terminal.
