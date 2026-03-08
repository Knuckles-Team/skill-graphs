## Multi-Server Deployments[](https://nextjs.org/docs/app/guides/self-hosting#multi-server-deployments)
When running Next.js across multiple server instances (for example, containers behind a load balancer), there are additional considerations to ensure consistent behavior.
### Server Functions encryption key[](https://nextjs.org/docs/app/guides/self-hosting#server-functions-encryption-key)
Next.js encrypts [Server Function](https://nextjs.org/docs/app/getting-started/updating-data) closure variables before sending them to the client. By default, a unique encryption key is generated for each build.
When running multiple server instances, all instances must use the same encryption key. Otherwise, a Server Function encrypted by one instance cannot be decrypted by another, causing "Failed to find Server Action" errors.
Set a consistent encryption key using the `NEXT_SERVER_ACTIONS_ENCRYPTION_KEY` environment variable. The key must be a base64-encoded value with a valid AES key length (16, 24, or 32 bytes). Next.js generates 32-byte keys by default.
```
NEXT_SERVER_ACTIONS_ENCRYPTION_KEY=your-generated-key next build
```

The key is embedded in the build output and used automatically at runtime. Learn more in the [Data Security guide](https://nextjs.org/docs/app/guides/data-security#overwriting-encryption-keys-advanced).
### Deployment identifier[](https://nextjs.org/docs/app/guides/self-hosting#deployment-identifier)
Configure a [`deploymentId`](https://nextjs.org/docs/app/api-reference/config/next-config-js/deploymentId) to enable version skew protection during rolling deployments. This ensures clients always receive assets from a consistent deployment version.
### Shared cache[](https://nextjs.org/docs/app/guides/self-hosting#shared-cache)
By default, Next.js uses an in-memory cache that is not shared across instances. For consistent caching behavior, use [`'use cache: remote'`](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote) with a [custom cache handler](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers) that stores data in external storage.
