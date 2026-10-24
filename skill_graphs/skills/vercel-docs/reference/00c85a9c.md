##  [When to use network firewall](https://vercel.com/docs/og-image-generation#when-to-use-network-firewall)[](https://vercel.com/docs/og-image-generation#when-to-use-network-firewall)
  * Protect user data: Allow untrusted code to touch user-data without a risk of it getting exfiltrated.
  * Avoid malware injection: Constrain package sources, or S3 buckets to access.
  * Dynamic policies for multi-step work: Start with Internet access, get required data, lock access and start untrusted process.
  * Protect your credentials: Untrusted code running within the sandbox cannot be trusted with credentials, but needs to authenticate to external services (e.g. AI Gateway).
