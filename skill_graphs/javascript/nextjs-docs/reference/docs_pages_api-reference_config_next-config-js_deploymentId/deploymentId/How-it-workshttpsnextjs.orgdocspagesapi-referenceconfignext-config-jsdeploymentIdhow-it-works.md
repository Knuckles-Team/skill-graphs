## How it works[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/deploymentId#how-it-works)
When a `deploymentId` is configured, Next.js:
  1. Appends `?dpl=<deploymentId>` to static asset URLs (JavaScript, CSS, images)
  2. Adds an `x-deployment-id` header to client-side navigation requests
  3. Adds an `x-nextjs-deployment-id` header to navigation responses
  4. Injects a `data-dpl-id` attribute on the `<html>` element


When the client detects a mismatch between its deployment ID and the server's (via the response header), it triggers a hard navigation (full page reload) instead of a client-side navigation. This ensures users always receive assets  from a consistent deployment version.
> **Good to know:** Next.js does not read the `?dpl=` query parameter on incoming requests. The query parameter is for cache busting (ensuring browsers and CDNs fetch fresh assets), not for routing. If you need version-aware routing, consult your hosting provider or CDN's documentation for implementing deployment-based routing.
