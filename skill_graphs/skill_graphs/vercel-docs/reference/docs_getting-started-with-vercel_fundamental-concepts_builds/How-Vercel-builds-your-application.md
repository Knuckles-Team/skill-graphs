# How Vercel builds your application
Last updated January 29, 2026
When you push code to Vercel, your source files need to be transformed into something that can actually run on the internet. This transformation is what we call the build process. It takes your React components, your API routes, your configuration files, and turns them into optimized HTML, JavaScript bundles, and server-side functions that Vercel's infrastructure can serve to users around the world.
This guide explains what happens during that transformation, from the moment Vercel receives your code to when your application is ready to handle its first request.
