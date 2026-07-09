##  [Sandbox creation](https://vercel.com/docs/og-image-generation#sandbox-creation)[](https://vercel.com/docs/og-image-generation#sandbox-creation)
Policies can be defined on sandboxes on creation, ensuring they will never run without them.
CLITypeScript
```
# Sandbox has full Internet and secure-compute access (default).
sandbox create --network-policy allow-all

# Sandbox has no Internet or secure-compute access.
sandbox create --network-policy deny-all

# Sandbox only gets access to listed websites.
sandbox create --allowed-domain "*.google.com" --allowed-domain ai-gateway.vercel.sh
```

```
import { Sandbox } from '@vercel/sandbox';

// Sandbox has full Internet and secure-compute access (default).
const sandbox = await Sandbox.create({
  networkPolicy: 'allow-all'
});

// Sandbox has no Internet or secure-compute access.
const sandbox = await Sandbox.create({
  networkPolicy: 'deny-all'
});

// Sandbox only gets access to listed websites.
const sandbox = await Sandbox.create({
  networkPolicy: {
    allow: ["*.google.com", "ai-gateway.vercel.sh"]
  }
});
```
