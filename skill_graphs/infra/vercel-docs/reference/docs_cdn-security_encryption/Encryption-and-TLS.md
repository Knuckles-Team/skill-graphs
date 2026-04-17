# Encryption and TLS
Last updated March 8, 2026
Every deployment on Vercel is served over an HTTPS connection. Vercel automatically generates
The CDN automatically forwards any HTTP requests to your deployment to HTTPS using the `308` status code:
```
HTTP/1.1 308 Moved Permanently
Content-Type: text/plain
Location: https://<your-deployment-host>
```

An example showing how all `HTTP` requests are forwarded to `HTTPS`.
HTTPS redirection is an industry standard and can't be disabled. This ensures that all web content is served over a secure connection, protecting your users' data and privacy.
If your client needs to establish a WebSocket connection, connect using HTTPS directly. The WSS protocol doesn't support redirects.
