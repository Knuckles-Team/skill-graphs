## Static vs Dynamic Rendering with CSP[](https://nextjs.org/docs/pages/guides/content-security-policy#static-vs-dynamic-rendering-with-csp)
Using nonces has important implications for how your Next.js application renders:
### Dynamic Rendering Requirement[](https://nextjs.org/docs/pages/guides/content-security-policy#dynamic-rendering-requirement)
When you use nonces in your CSP, **all pages must be dynamically rendered**. This means:
  * Pages will build successfully but may encounter runtime errors if not properly configured for dynamic rendering
  * Each request generates a fresh page with a new nonce
  * Static optimization and Incremental Static Regeneration (ISR) are disabled
  * Pages cannot be cached by CDNs without additional configuration
  * **Partial Prerendering (PPR) is incompatible** with nonce-based CSP since static shell scripts won't have access to the nonce


### Performance Implications[](https://nextjs.org/docs/pages/guides/content-security-policy#performance-implications)
The shift from static to dynamic rendering affects performance:
  * **Slower initial page loads** : Pages must be generated on each request
  * **Increased server load** : Every request requires server-side rendering
  * **No CDN caching** : Dynamic pages cannot be cached at the edge by default
  * **Higher hosting costs** : More server resources needed for dynamic rendering


### When to use nonces[](https://nextjs.org/docs/pages/guides/content-security-policy#when-to-use-nonces)
Consider nonces when:
  * You have strict security requirements that prohibit `'unsafe-inline'`
  * Your application handles sensitive data
  * You need to allow specific inline scripts while blocking others
  * Compliance requirements mandate strict CSP
