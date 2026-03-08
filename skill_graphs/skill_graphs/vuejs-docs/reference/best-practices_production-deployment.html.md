[Skip to content](https://vuejs.org/guide/best-practices/production-deployment.html#VPContent)
[Vue.js](https://vuejs.org/)
Search`Ctrl``K`
Main Navigation
Docs
[Guide](https://vuejs.org/guide/introduction)[Tutorial](https://vuejs.org/tutorial/)[Examples](https://vuejs.org/examples/)[Quick Start](https://vuejs.org/guide/quick-start)[Glossary](https://vuejs.org/glossary/)[Error Reference](https://vuejs.org/error-reference/)[Vue 2 Docs](https://v2.vuejs.org)[Migration from Vue 2](https://v3-migration.vuejs.org/)
[API](https://vuejs.org/api/)[Playground](https://play.vuejs.org)
Ecosystem
Resources
[Partners](https://vuejs.org/partners/)[Themes](https://vuejs.org/ecosystem/themes)
Official Libraries
[Vue Router](https://router.vuejs.org/)[Pinia](https://pinia.vuejs.org/)[Tooling Guide](https://vuejs.org/guide/scaling-up/tooling)
Video Courses
Help
News
[Blog](https://blog.vuejs.org/)[Events](https://events.vuejs.org/)[Newsletters](https://vuejs.org/ecosystem/newsletters)
About
[FAQ](https://vuejs.org/about/faq)[Team](https://vuejs.org/about/team)[Releases](https://vuejs.org/about/releases)[Community Guide](https://vuejs.org/about/community-guide)[Code of Conduct](https://vuejs.org/about/coc)[Privacy Policy](https://vuejs.org/about/privacy)
[Sponsor](https://vuejs.org/sponsor/)[Partners](https://vuejs.org/partners/)
[简体中文 ](https://cn.vuejs.org/guide/best-practices/production-deployment)
[日本語 ](https://ja.vuejs.org/guide/best-practices/production-deployment)
[Українська ](https://ua.vuejs.org/guide/best-practices/production-deployment)
[Français ](https://fr.vuejs.org/guide/best-practices/production-deployment)
[한국어 ](https://ko.vuejs.org/guide/best-practices/production-deployment)
[Português ](https://pt.vuejs.org/guide/best-practices/production-deployment)
[বাংলা ](https://bn.vuejs.org/guide/best-practices/production-deployment)
[Italiano ](https://it.vuejs.org/guide/best-practices/production-deployment)
[فارسی ](https://fa.vuejs.org/guide/best-practices/production-deployment)
[Русский ](https://ru.vuejs.org/guide/best-practices/production-deployment)
[Čeština ](https://cs.vuejs.org/guide/best-practices/production-deployment)
[繁體中文 ](https://zh-hk.vuejs.org/guide/best-practices/production-deployment)
[Polski ](https://pl.vuejs.org/guide/best-practices/production-deployment)
Help Us Translate!
Appearance
Menu
On this page
API Preference
OptionsComposition[?](https://vuejs.org/guide/introduction#api-styles "About API preference")
API style now defaults to Composition API.
Some pages contain different content based on the API style chosen. Use this switch to toggle between APIs styles.
[Learn more](https://vuejs.org/guide/introduction#api-styles)Got it
Sidebar Navigation
## Getting Started
[Introduction](https://vuejs.org/guide/introduction)[Quick Start](https://vuejs.org/guide/quick-start)
## Essentials
[Creating an Application](https://vuejs.org/guide/essentials/application)[Template Syntax](https://vuejs.org/guide/essentials/template-syntax)[Reactivity Fundamentals](https://vuejs.org/guide/essentials/reactivity-fundamentals)[Computed Properties](https://vuejs.org/guide/essentials/computed)[Class and Style Bindings](https://vuejs.org/guide/essentials/class-and-style)[Conditional Rendering](https://vuejs.org/guide/essentials/conditional)[List Rendering](https://vuejs.org/guide/essentials/list)[Event Handling](https://vuejs.org/guide/essentials/event-handling)[Form Input Bindings](https://vuejs.org/guide/essentials/forms)[Watchers](https://vuejs.org/guide/essentials/watchers)[Template Refs](https://vuejs.org/guide/essentials/template-refs)[Components Basics](https://vuejs.org/guide/essentials/component-basics)[Lifecycle Hooks](https://vuejs.org/guide/essentials/lifecycle)
## Components In-Depth
[Registration](https://vuejs.org/guide/components/registration)[Props](https://vuejs.org/guide/components/props)[Events](https://vuejs.org/guide/components/events)[Component v-model](https://vuejs.org/guide/components/v-model)[Fallthrough Attributes](https://vuejs.org/guide/components/attrs)[Slots](https://vuejs.org/guide/components/slots)[Provide / inject](https://vuejs.org/guide/components/provide-inject)[Async Components](https://vuejs.org/guide/components/async)
## Reusability
[Composables](https://vuejs.org/guide/reusability/composables)[Custom Directives](https://vuejs.org/guide/reusability/custom-directives)[Plugins](https://vuejs.org/guide/reusability/plugins)
## Built-in Components
[Transition](https://vuejs.org/guide/built-ins/transition)[TransitionGroup](https://vuejs.org/guide/built-ins/transition-group)[KeepAlive](https://vuejs.org/guide/built-ins/keep-alive)[Teleport](https://vuejs.org/guide/built-ins/teleport)[Suspense](https://vuejs.org/guide/built-ins/suspense)
## Scaling Up
[Single-File Components](https://vuejs.org/guide/scaling-up/sfc)[Tooling](https://vuejs.org/guide/scaling-up/tooling)[Routing](https://vuejs.org/guide/scaling-up/routing)[State Management](https://vuejs.org/guide/scaling-up/state-management)[Testing](https://vuejs.org/guide/scaling-up/testing)[Server-Side Rendering (SSR)](https://vuejs.org/guide/scaling-up/ssr)
## Best Practices
[Production Deployment](https://vuejs.org/guide/best-practices/production-deployment)[Performance](https://vuejs.org/guide/best-practices/performance)[Accessibility](https://vuejs.org/guide/best-practices/accessibility)[Security](https://vuejs.org/guide/best-practices/security)
## TypeScript
[Overview](https://vuejs.org/guide/typescript/overview)[TS with Composition API](https://vuejs.org/guide/typescript/composition-api)[TS with Options API](https://vuejs.org/guide/typescript/options-api)
## Extra Topics
[Ways of Using Vue](https://vuejs.org/guide/extras/ways-of-using-vue)[Composition API FAQ](https://vuejs.org/guide/extras/composition-api-faq)[Reactivity in Depth](https://vuejs.org/guide/extras/reactivity-in-depth)[Rendering Mechanism](https://vuejs.org/guide/extras/rendering-mechanism)[Render Functions & JSX](https://vuejs.org/guide/extras/render-function)[Vue and Web Components](https://vuejs.org/guide/extras/web-components)[Animation Techniques](https://vuejs.org/guide/extras/animation)
On this page
Table of Contents for current page
  * [Development vs. Production](https://vuejs.org/guide/best-practices/production-deployment.html#development-vs-production)
  * [Without Build Tools](https://vuejs.org/guide/best-practices/production-deployment.html#without-build-tools)
  * [With Build Tools](https://vuejs.org/guide/best-practices/production-deployment.html#with-build-tools)
  * [Tracking Runtime Errors](https://vuejs.org/guide/best-practices/production-deployment.html#tracking-runtime-errors)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Production Deployment [​](https://vuejs.org/guide/best-practices/production-deployment.html#production-deployment)
## Development vs. Production [​](https://vuejs.org/guide/best-practices/production-deployment.html#development-vs-production)
During development, Vue provides a number of features to improve the development experience:
  * Warning for common errors and pitfalls
  * Props / events validation
  * [Reactivity debugging hooks](https://vuejs.org/guide/extras/reactivity-in-depth#reactivity-debugging)
  * Devtools integration


However, these features become useless in production. Some of the warning checks can also incur a small amount of performance overhead. When deploying to production, we should drop all the unused, development-only code branches for smaller payload size and better performance.
## Without Build Tools [​](https://vuejs.org/guide/best-practices/production-deployment.html#without-build-tools)
If you are using Vue without a build tool by loading it from a CDN or self-hosted script, make sure to use the production build (dist files that end in `.prod.js`) when deploying to production. Production builds are pre-minified with all development-only code branches removed.
  * If using global build (accessing via the `Vue` global): use `vue.global.prod.js`.
  * If using ESM build (accessing via native ESM imports): use `vue.esm-browser.prod.js`.


Consult the
## With Build Tools [​](https://vuejs.org/guide/best-practices/production-deployment.html#with-build-tools)
Projects scaffolded via `create-vue` (based on Vite) or Vue CLI (based on webpack) are pre-configured for production builds.
If using a custom setup, make sure that:
  1. `vue` resolves to `vue.runtime.esm-bundler.js`.
  2. The [compile time feature flags](https://vuejs.org/api/compile-time-flags) are properly configured.
  3. `process.env.NODE_ENV` is replaced with `"production"` during build.


Additional references:
  * [Vue CLI deployment guide](https://cli.vuejs.org/guide/deployment.html)


## Tracking Runtime Errors [​](https://vuejs.org/guide/best-practices/production-deployment.html#tracking-runtime-errors)
The [app-level error handler](https://vuejs.org/api/application#app-config-errorhandler) can be used to report errors to tracking services:
js```
import { createApp } from 'vue'

const app = createApp(...)

app.config.errorHandler = (err, instance, info) => {
  // report error to tracking services
}
```

Services such as
[Server-Side Rendering (SSR)](https://vuejs.org/guide/scaling-up/ssr)[Next Performance](https://vuejs.org/guide/best-practices/performance)
Production Deployment has loaded
