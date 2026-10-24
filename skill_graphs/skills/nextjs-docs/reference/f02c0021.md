# How to create a static export of your Next.js application
Last updated February 27, 2026
Next.js enables starting as a static site or Single-Page Application (SPA), then later optionally upgrading to use features that require a server.
When running `next build`, Next.js generates an HTML file per route. By breaking a strict SPA into individual HTML files, Next.js can avoid loading unnecessary JavaScript code on the client-side, reducing the bundle size and enabling faster page loads.
Since Next.js supports this static export, it can be deployed and hosted on any web server that can serve HTML/CSS/JS static assets.
