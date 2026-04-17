[Skip to main content](https://svelte.dev/docs/kit/introduction#main) [](https://svelte.dev/ "Homepage")
Docs
[Docs ](https://svelte.dev/docs)
[Svelte](https://svelte.dev/docs/svelte)[SvelteKit](https://svelte.dev/docs/kit)[CLI](https://svelte.dev/docs/cli)[AI](https://svelte.dev/docs/ai)
[Tutorial](https://svelte.dev/tutorial)[Packages](https://svelte.dev/packages)[Playground](https://svelte.dev/playground)[Blog](https://svelte.dev/blog)
`Ctrl` `K`
[](https://svelte.dev/chat)
  * ### Getting started
    * [Introduction](https://svelte.dev/docs/kit/introduction)
    * [Creating a project](https://svelte.dev/docs/kit/creating-a-project)
    * [Project types](https://svelte.dev/docs/kit/project-types)
    * [Project structure](https://svelte.dev/docs/kit/project-structure)
    * [Web standards](https://svelte.dev/docs/kit/web-standards)
  * ### Core concepts
    * [Routing](https://svelte.dev/docs/kit/routing)
    * [Loading data](https://svelte.dev/docs/kit/load)
    * [Form actions](https://svelte.dev/docs/kit/form-actions)
    * [Page options](https://svelte.dev/docs/kit/page-options)
    * [State management](https://svelte.dev/docs/kit/state-management)
    * [Remote functions](https://svelte.dev/docs/kit/remote-functions)
  * ### Build and deploy
    * [Building your app](https://svelte.dev/docs/kit/building-your-app)
    * [Adapters](https://svelte.dev/docs/kit/adapters)
    * [Zero-config deployments](https://svelte.dev/docs/kit/adapter-auto)
    * [Node servers](https://svelte.dev/docs/kit/adapter-node)
    * [Static site generation](https://svelte.dev/docs/kit/adapter-static)
    * [Single-page apps](https://svelte.dev/docs/kit/single-page-apps)
    * [Cloudflare](https://svelte.dev/docs/kit/adapter-cloudflare)
    * [Cloudflare Workers](https://svelte.dev/docs/kit/adapter-cloudflare-workers)
    * [Netlify](https://svelte.dev/docs/kit/adapter-netlify)
    * [Vercel](https://svelte.dev/docs/kit/adapter-vercel)
    * [Writing adapters](https://svelte.dev/docs/kit/writing-adapters)
  * ### Advanced
    * [Advanced routing](https://svelte.dev/docs/kit/advanced-routing)
    * [Hooks](https://svelte.dev/docs/kit/hooks)
    * [Errors](https://svelte.dev/docs/kit/errors)
    * [Link options](https://svelte.dev/docs/kit/link-options)
    * [Service workers](https://svelte.dev/docs/kit/service-workers)
    * [Server-only modules](https://svelte.dev/docs/kit/server-only-modules)
    * [Snapshots](https://svelte.dev/docs/kit/snapshots)
    * [Shallow routing](https://svelte.dev/docs/kit/shallow-routing)
    * [Observability](https://svelte.dev/docs/kit/observability)
    * [Packaging](https://svelte.dev/docs/kit/packaging)
  * ### Best practices
    * [Auth](https://svelte.dev/docs/kit/auth)
    * [Performance](https://svelte.dev/docs/kit/performance)
    * [Icons](https://svelte.dev/docs/kit/icons)
    * [Images](https://svelte.dev/docs/kit/images)
    * [Accessibility](https://svelte.dev/docs/kit/accessibility)
    * [SEO](https://svelte.dev/docs/kit/seo)
  * ### Appendix
    * [Frequently asked questions](https://svelte.dev/docs/kit/faq)
    * [Integrations](https://svelte.dev/docs/kit/integrations)
    * [Breakpoint Debugging](https://svelte.dev/docs/kit/debugging)
    * [Migrating to SvelteKit v2](https://svelte.dev/docs/kit/migrating-to-sveltekit-2)
    * [Migrating from Sapper](https://svelte.dev/docs/kit/migrating)
    * [Additional resources](https://svelte.dev/docs/kit/additional-resources)
    * [Glossary](https://svelte.dev/docs/kit/glossary)
  * ### Reference
    * [@sveltejs/kit](https://svelte.dev/docs/kit/@sveltejs-kit)
    * [@sveltejs/kit/hooks](https://svelte.dev/docs/kit/@sveltejs-kit-hooks)
    * [@sveltejs/kit/node/polyfills](https://svelte.dev/docs/kit/@sveltejs-kit-node-polyfills)
    * [@sveltejs/kit/node](https://svelte.dev/docs/kit/@sveltejs-kit-node)
    * [@sveltejs/kit/vite](https://svelte.dev/docs/kit/@sveltejs-kit-vite)
    * [$app/environment](https://svelte.dev/docs/kit/$app-environment)
    * [$app/forms](https://svelte.dev/docs/kit/$app-forms)
    * [$app/navigation](https://svelte.dev/docs/kit/$app-navigation)
    * [$app/paths](https://svelte.dev/docs/kit/$app-paths)
    * [$app/server](https://svelte.dev/docs/kit/$app-server)
    * [$app/state](https://svelte.dev/docs/kit/$app-state)
    * [$app/stores](https://svelte.dev/docs/kit/$app-stores)
    * [$app/types](https://svelte.dev/docs/kit/$app-types)
    * [$env/dynamic/private](https://svelte.dev/docs/kit/$env-dynamic-private)
    * [$env/dynamic/public](https://svelte.dev/docs/kit/$env-dynamic-public)
    * [$env/static/private](https://svelte.dev/docs/kit/$env-static-private)
    * [$env/static/public](https://svelte.dev/docs/kit/$env-static-public)
    * [$lib](https://svelte.dev/docs/kit/$lib)
    * [$service-worker](https://svelte.dev/docs/kit/$service-worker)
    * [Configuration](https://svelte.dev/docs/kit/configuration)
    * [Command Line Interface](https://svelte.dev/docs/kit/cli)
    * [Types](https://svelte.dev/docs/kit/types)


SvelteKitGetting started
#  Introduction
### On this page
  * [Introduction](https://svelte.dev/docs/kit/introduction)
  * [Before we begin](https://svelte.dev/docs/kit/introduction#Before-we-begin)
  * [What is SvelteKit?](https://svelte.dev/docs/kit/introduction#What-is-SvelteKit)
  * [What is Svelte?](https://svelte.dev/docs/kit/introduction#What-is-Svelte)
  * [SvelteKit vs Svelte](https://svelte.dev/docs/kit/introduction#SvelteKit-vs-Svelte)


##  Before we begin[](https://svelte.dev/docs/kit/introduction#Before-we-begin)
> If you're new to Svelte or SvelteKit we recommend checking out the [interactive tutorial](https://svelte.dev/tutorial/kit).
> If you get stuck, reach out for help in the [Discord chatroom](https://svelte.dev/chat).
##  What is SvelteKit?[](https://svelte.dev/docs/kit/introduction#What-is-SvelteKit)
SvelteKit is a framework for rapidly developing robust, performant web applications using [Svelte](https://svelte.dev/docs/svelte). If you're coming from React, SvelteKit is similar to Next. If you're coming from Vue, SvelteKit is similar to Nuxt.
To learn more about the kinds of applications you can build with SvelteKit, see the [documentation regarding project types](https://svelte.dev/docs/kit/project-types).
##  What is Svelte?[](https://svelte.dev/docs/kit/introduction#What-is-Svelte)
In short, Svelte is a way of writing user interface components — like a navigation bar, comment section, or contact form — that users see and interact with in their browsers. The Svelte compiler converts your components to JavaScript that can be run to render the HTML for the page and to CSS that styles the page. You don't need to know Svelte to understand the rest of this guide, but it will help. If you'd like to learn more, check out [the Svelte tutorial](https://svelte.dev/tutorial).
##  SvelteKit vs Svelte[](https://svelte.dev/docs/kit/introduction#SvelteKit-vs-Svelte)
Svelte renders UI components. You can compose these components and render an entire page with just Svelte, but you need more than just Svelte to write an entire app.
SvelteKit helps you build web apps while following modern best practices and providing solutions to common development challenges. It offers everything from basic functionalities — like a [router](https://svelte.dev/docs/kit/glossary#Routing) that updates your UI when a link is clicked — to more advanced capabilities. Its extensive list of features includes [offline support](https://svelte.dev/docs/kit/service-workers); [preloading](https://svelte.dev/docs/kit/link-options#data-sveltekit-preload-data) pages before user navigation; [configurable rendering](https://svelte.dev/docs/kit/page-options) to handle different parts of your app on the server via [SSR](https://svelte.dev/docs/kit/glossary#SSR), in the browser through [client-side rendering](https://svelte.dev/docs/kit/glossary#CSR), or at build-time with [prerendering](https://svelte.dev/docs/kit/glossary#Prerendering); [image optimization](https://svelte.dev/docs/kit/images); and much more. Building an app with all the modern best practices is fiendishly complicated, but SvelteKit does all the boring stuff for you so that you can get on with the creative part.
It reflects changes to your code in the browser instantly to provide a lightning-fast and feature-rich development experience by leveraging
[ llms.txt](https://svelte.dev/docs/kit/introduction/llms.txt)
previous next
[Creating a project](https://svelte.dev/docs/kit/creating-a-project)
