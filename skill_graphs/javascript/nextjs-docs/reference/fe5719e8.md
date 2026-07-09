# Automatic Static Optimization
Last updated February 27, 2026
Next.js automatically determines that a page is static (can be prerendered) if it has no blocking data requirements. This determination is made by the absence of `getServerSideProps` and `getInitialProps` in the page.
This feature allows Next.js to emit hybrid applications that contain **both server-rendered and statically generated pages**.
> **Good to know** : Statically generated pages are still reactive. Next.js will hydrate your application client-side to give it full interactivity.
One of the main benefits of this feature is that optimized pages require no server-side computation, and can be instantly streamed to the end-user from multiple CDN locations. The result is an _ultra fast_ loading experience for your users.
