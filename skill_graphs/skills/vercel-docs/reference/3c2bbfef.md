##  [Environment variables and prefixes](https://vercel.com/docs/integrations/create-integration/native-integration#environment-variables-and-prefixes)[](https://vercel.com/docs/integrations/create-integration/native-integration#environment-variables-and-prefixes)
When a user connects a resource to a Vercel project, Vercel creates environment variables from the secrets your integration provides during [provisioning](https://vercel.com/docs/integrations/create-integration/marketplace-flows#submit-store-creation) or through the [Update Resource Secrets endpoint](https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/vercel/update-resource-secrets-by-id).
These environment variables are the same across all projects connected to a resource. For example, if your integration provisions a database with a `DATABASE_URL` secret, every connected project receives the same `DATABASE_URL` variable.
###  [Differentiate variables with prefixes](https://vercel.com/docs/integrations/create-integration/native-integration#differentiate-variables-with-prefixes)[](https://vercel.com/docs/integrations/create-integration/native-integration#differentiate-variables-with-prefixes)
When a user connects the same resource to multiple projects, or connects multiple resources of the same type to one project, environment variable names can collide. Prefixes solve this by adding a namespace to each variable name.
There are two ways to apply prefixes:
  * Provider-defined prefixes: Include a `prefix` field in the secrets array when [provisioning a resource](https://vercel.com/docs/integrations/create-integration/marketplace-flows#submit-store-creation) or [updating resource secrets](https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/vercel/update-resource-secrets-by-id). Vercel prepends this prefix to each secret name when creating environment variables.
  * User-defined prefixes: When a user connects a resource to a project, they can set a custom prefix in the Custom Prefix field of the connection dialog. If set, this overrides any provider-defined prefix for that connection.


For example, if your integration returns a secret named `PGHOST` and the user sets a custom prefix of `DB1`, the resulting environment variable is `DB1_PGHOST`.
Scenario | Secret name | Prefix | Environment variable
---|---|---|---
No prefix | `PGHOST` | (none) | `PGHOST`
Provider-defined prefix | `PGHOST` | `ACME` | `ACME_PGHOST`
User-defined prefix | `PGHOST` | `DB1` | `DB1_PGHOST`
Both (user overrides provider) | `PGHOST` | Provider: `ACME`, User: `DB1` | `DB1_PGHOST`
For secrets that start with `NEXT_PUBLIC_`, the prefix is inserted after `NEXT_PUBLIC_` (for example, `NEXT_PUBLIC_ACME_PGHOST` instead of `ACME_NEXT_PUBLIC_PGHOST`). This preserves the Next.js client-side exposure behavior.
This is useful when a project needs to connect to two instances of the same resource type, such as a primary and replica database. Each connection can use a different prefix to avoid conflicts.
