##  [Network policies](https://vercel.com/docs/og-image-generation#network-policies)[](https://vercel.com/docs/og-image-generation#network-policies)
Sandboxes can use three distinct modes, which can be updated at runtime, without restarting the process.
###  [`allow-all`](https://vercel.com/docs/og-image-generation#allow-all)[](https://vercel.com/docs/og-image-generation#allow-all)
Default policy. This gives the sandbox unrestricted access to the public Internet.
Have the ability to install software packages, download dependencies and pull any data from external sources with the enhanced security model of sandboxes.
###  [`deny-all`](https://vercel.com/docs/og-image-generation#deny-all)[](https://vercel.com/docs/og-image-generation#deny-all)
Most restrictive policy. Denies all outbound network access, including DNS.
This is useful to reduce the chance of data exfiltration when running untrusted code or an agent on private data.
###  [User-defined](https://vercel.com/docs/og-image-generation#user-defined)[](https://vercel.com/docs/og-image-generation#user-defined)
Most specific policy, denying all traffic by default, while allowing users to get fine-grain control on their sandbox setup. Users can define:
  * a list of domains to allow traffic to. Domain-based policies are easy to use and maintain fine-grain access control for services like S3 (per bucket) or behind virtual hosting (as Vercel). Wildcard support (`*`) allows easier management for complex websites.
  * a list of address ranges to allow traffic to. Those ranges will not enforce per-domain rules, supporting non-encrypted traffic. This is recommended when using secure-compute to connect to your private network securely.
  * a list of address ranges to deny traffic to. Those range will take precedence to block traffic. This is useful when using secure-compute, allowing Internet access to be granted while blocking internal network.
