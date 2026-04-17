##  [Support for HSTS](https://vercel.com/docs/cdn-security/encryption#support-for-hsts)[](https://vercel.com/docs/cdn-security/encryption#support-for-hsts)
The `.vercel.app` domain (and therefore all of its sub domains, which are the unique URLs set when creating a deployment) support
```
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload;
```

The default `Strict-Transport-Security` header for *.vercel.app
Custom domains use HSTS, but only for the particular subdomain.
```
Strict-Transport-Security: max-age=63072000;
```

The default `Strict-Transport-Security` header for custom domains
You can modify the `Strict-Transport-Security` header by configuring [custom response headers](https://vercel.com/docs/headers/cache-control-headers#custom-response-headers) in your project.
You can set the `max-age` parameter to a different value. It controls how long the client remembers that your site is HTTPS-only. Since Vercel doesn't allow HTTP connections, there's no reason to shorten it.
You can test whether your site qualifies for HSTS Preloading
