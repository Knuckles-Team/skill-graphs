##  [Public storage security](https://vercel.com/docs/vercel-blob/security#public-storage-security)[](https://vercel.com/docs/vercel-blob/security#public-storage-security)
Vercel Blob URLs, although publicly accessible, are unique and hard to guess when you use the `addRandomSuffix: true` option. They consist of a unique store id, a pathname, and a unique random blob id generated when the blob is created.
This is similar to
Headers that enhance security by preventing unauthorized downloads, blocking external content from being embedded, and protecting against malicious file type manipulation, are enforced on each blob. They are:
  * `content-security-policy`: `default-src "none"`
  * `x-frame-options`: `DENY`
  * `x-content-type-options`: `nosniff`
  * `content-disposition`: `attachment/inline; filename="filename.extension"`


###  [Encryption](https://vercel.com/docs/vercel-blob/security#encryption)[](https://vercel.com/docs/vercel-blob/security#encryption)
All files stored on Vercel Blob are secured using AES-256 encryption. This encryption process is applied at rest and is transparent, ensuring that files are encrypted before being saved to the disk and decrypted upon retrieval.
###  [Firewall and WAF integration](https://vercel.com/docs/vercel-blob/security#firewall-and-waf-integration)[](https://vercel.com/docs/vercel-blob/security#firewall-and-waf-integration)
Vercel Blob is protected by Vercel's [platform-wide firewall](https://vercel.com/docs/vercel-firewall#platform-wide-firewall) which provides DDoS mitigation and blocks abnormal or suspicious levels of incoming requests.
Vercel Blob does not currently support [Vercel WAF](https://vercel.com/docs/vercel-firewall/vercel-waf). If you need WAF rules on your blob URLs, consider using a [Vercel function](https://vercel.com/docs/functions) to proxy the blob URL. This approach may introduce some latency to your requests but will enable the use of WAF rules on the blob URLs.
* * *
[ Previous Pricing ](https://vercel.com/docs/vercel-blob/usage-and-pricing)[ Next Examples ](https://vercel.com/docs/vercel-blob/examples)
Was this helpful?
Send
On this page
  * [Private storage](https://vercel.com/docs/vercel-blob/security#private-storage)
  * [Public storage security](https://vercel.com/docs/vercel-blob/security#public-storage-security)
  * [Encryption](https://vercel.com/docs/vercel-blob/security#encryption)
  * [Firewall and WAF integration](https://vercel.com/docs/vercel-blob/security#firewall-and-waf-integration)


Copy as MarkdownGive feedbackAsk AI about this page
