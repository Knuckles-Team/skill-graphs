##  [Live updates](https://vercel.com/docs/og-image-generation#live-updates)[](https://vercel.com/docs/og-image-generation#live-updates)
Policies can be updated on running sandboxes, allowing for incremental restrictions.
For instance start by installing needed packages, downloading data, and then run untrusted code on it. Without live updates the entire run would have to get Internet access (creating exfiltration risk), or multiple steps and sandboxes would be needed.
CLITypeScript
```
sandbox create --network-policy allow-all

# Install packages
sandbox exec sb_12345678 npm install
# Download data
sandbox exec sb_12345678 aws s3 cp s3://my-bucket/dataset .

# Lockdown Internet access
sandbox config network-policy --mode deny-all

# Run untrusted workload, without exfiltration risk
sandbox exec sb_12345678 ./agent
```

```
import { Sandbox } from '@vercel/sandbox';

// Start with Internet access (default)
const sandbox = await Sandbox.create();

// Install dependencies, download data, configure environment, etc.
await sandbox.runCommand('npm', ['install']);
await sandbox.runCommand('aws', ['s3', 'cp', 's3://my-bucket/dataset', '.']);

// Lockdown Internet access
await sandbox.updateNetworkPolicy('deny-all')

// Run untrusted workload, without exfiltration risk
await sandbox.runCommand('./agent', []);
```

* * *
[ Previous Cron Jobs ](https://vercel.com/docs/cron-jobs)[ Next @vercel/og ](https://vercel.com/docs/og-image-generation/og-image-api)
Was this helpful?
Send
Next.js (/app)
Choose a framework to optimize documentation to:
  * Next.js (/app)
  * Next.js (/pages)
  * Other frameworks


On this page
  * [When to use network firewall](https://vercel.com/docs/og-image-generation#when-to-use-network-firewall)
  * [Network policies](https://vercel.com/docs/og-image-generation#network-policies)
  * [allow-all](https://vercel.com/docs/og-image-generation#allow-all)
  * [deny-all](https://vercel.com/docs/og-image-generation#deny-all)
  * [User-defined](https://vercel.com/docs/og-image-generation#user-defined)
  * [Credentials brokering](https://vercel.com/docs/og-image-generation#credentials-brokering)
  * [TLS termination](https://vercel.com/docs/og-image-generation#tls-termination)
  * [Sandbox creation](https://vercel.com/docs/og-image-generation#sandbox-creation)
  * [Live updates](https://vercel.com/docs/og-image-generation#live-updates)


Copy as MarkdownGive feedbackAsk AI about this page
