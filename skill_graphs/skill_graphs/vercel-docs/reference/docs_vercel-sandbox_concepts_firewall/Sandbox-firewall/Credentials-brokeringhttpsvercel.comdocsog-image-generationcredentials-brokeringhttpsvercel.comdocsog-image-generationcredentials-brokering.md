##  [Credentials brokering](https://vercel.com/docs/og-image-generation#credentials-brokering)[](https://vercel.com/docs/og-image-generation#credentials-brokering)
Commands running in the sandbox often require authentication with external services, for instance code repositories or AI services. Providing API keys to those commands would risk abuse or exfiltration. On the other hand, allowing access to a domain can allow data exfiltration if not restricting the permissions or sessions attached to it.
Credentials brokering allows the injection of credentials on egressing traffic, while ensuring those secrets never enter the sandbox scope, preventing exfiltration.
Only Pro and Enterprise users can define transformations, including for credentials brokering.
TypeScript
```
import { Sandbox } from '@vercel/sandbox';

// Sandbox has access to everything, with credential brokering for two specific domains.
const sandbox = await Sandbox.create({
  networkPolicy: {
    allow: {
      "ai-gateway.vercel.sh": [{
        transform: [{ headers: { "Authorization": `Bearer ${process.env.AI_GATEWAY_TOKEN}` } }],
      }],
      "*.github.com": [{
        transform: [{ headers: { "Authorization": `Bearer ${process.env.GITHUB_TOKEN}` } }],
      }],
      // Allow traffic to all other domains. If unset only defined ones are reachable.
      "*": []
    }
  }
});

// Sandbox no longer has Internet or secure-compute access.
// Credential brokering is deactivated.
await sandbox.updateNetworkPolicy('deny-all');

// Reallow traffic only to ai-gateway, and use the same key.
await sandbox.updateNetworkPolicy({
  allow: {
    "ai-gateway.vercel.sh": [{
      transform: [{ headers: { "Authorization": `Bearer ${process.env.AI_GATEWAY_TOKEN}` } }],
    }],
  }
});
```

###  [TLS termination](https://vercel.com/docs/og-image-generation#tls-termination)[](https://vercel.com/docs/og-image-generation#tls-termination)
In order to perform transformation within requests, the firewall needs to terminate TLS connections. Only connections targeting domains with defined transformation rules are terminated in the proxy.
A unique, per-sandbox CA is added to the system certificates. Standard environment variables are configured automatically to ensure compatibility with most clients.
