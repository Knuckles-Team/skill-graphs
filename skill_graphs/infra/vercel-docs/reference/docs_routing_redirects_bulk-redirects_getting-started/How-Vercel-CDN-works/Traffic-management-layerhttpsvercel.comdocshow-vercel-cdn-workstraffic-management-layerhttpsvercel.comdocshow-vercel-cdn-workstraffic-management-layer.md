##  [Traffic management layer](https://vercel.com/docs/how-vercel-cdn-works#traffic-management-layer)[](https://vercel.com/docs/how-vercel-cdn-works#traffic-management-layer)
After routing rules resolve, the CDN determines which deployment handles the request:
  * [Skew Protection](https://vercel.com/docs/skew-protection): Locks each client session to a specific deployment version so client-side code and server responses stay in sync. This prevents errors caused by version mismatches during deployments.
  * [Rolling Releases](https://vercel.com/docs/rolling-releases): Gradually shifts traffic from your current production deployment to a new one across configurable stages. You can monitor metrics at each stage and abort if needed.
  * [Microfrontends](https://vercel.com/docs/microfrontends): Routes requests to different microfrontend applications based on path configuration in `microfrontends.json`. This routing happens within the same request with no additional network hop.
