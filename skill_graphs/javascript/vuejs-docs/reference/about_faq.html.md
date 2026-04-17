[Skip to content](https://vuejs.org/about/faq.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/about/faq)
[日本語 ](https://ja.vuejs.org/about/faq)
[Українська ](https://ua.vuejs.org/about/faq)
[Français ](https://fr.vuejs.org/about/faq)
[한국어 ](https://ko.vuejs.org/about/faq)
[Português ](https://pt.vuejs.org/about/faq)
[বাংলা ](https://bn.vuejs.org/about/faq)
[Italiano ](https://it.vuejs.org/about/faq)
[فارسی ](https://fa.vuejs.org/about/faq)
[Русский ](https://ru.vuejs.org/about/faq)
[Čeština ](https://cs.vuejs.org/about/faq)
[繁體中文 ](https://zh-hk.vuejs.org/about/faq)
[Polski ](https://pl.vuejs.org/about/faq)
Help Us Translate!
Appearance
On this page
Table of Contents for current page
  * [Who maintains Vue?](https://vuejs.org/about/faq.html#who-maintains-vue)
  * [What's the difference between Vue 2 and Vue 3?](https://vuejs.org/about/faq.html#what-s-the-difference-between-vue-2-and-vue-3)
  * [Is Vue 2 Still Supported?](https://vuejs.org/about/faq.html#is-vue-2-still-supported)
  * [What license does Vue use?](https://vuejs.org/about/faq.html#what-license-does-vue-use)
  * [What browsers does Vue support?](https://vuejs.org/about/faq.html#what-browsers-does-vue-support)
  * [Is Vue reliable?](https://vuejs.org/about/faq.html#is-vue-reliable)
  * [Is Vue fast?](https://vuejs.org/about/faq.html#is-vue-fast)
  * [Is Vue lightweight?](https://vuejs.org/about/faq.html#is-vue-lightweight)
  * [Does Vue scale?](https://vuejs.org/about/faq.html#does-vue-scale)
  * [How do I contribute to Vue?](https://vuejs.org/about/faq.html#how-do-i-contribute-to-vue)
  * [Should I use Options API or Composition API?](https://vuejs.org/about/faq.html#should-i-use-options-api-or-composition-api)
  * [Should I use JavaScript or TypeScript with Vue?](https://vuejs.org/about/faq.html#should-i-use-javascript-or-typescript-with-vue)
  * [How does Vue compare to Web Components?](https://vuejs.org/about/faq.html#how-does-vue-compare-to-web-components)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Frequently Asked Questions [​](https://vuejs.org/about/faq.html#frequently-asked-questions)
## Who maintains Vue? [​](https://vuejs.org/about/faq.html#who-maintains-vue)
Vue is an independent, community-driven project. It was created by [a team of both full-time and volunteer members from all around the world](https://vuejs.org/about/team), where Evan serves as the project lead. You can learn more about the story of Vue in this
Vue's development is primarily funded through sponsorships and we have been financially sustainable since 2016. If you or your business benefit from Vue, consider [sponsoring us](https://vuejs.org/sponsor/) to support Vue's development!
## What's the difference between Vue 2 and Vue 3? [​](https://vuejs.org/about/faq.html#what-s-the-difference-between-vue-2-and-vue-3)
Vue 3 is the current, latest major version of Vue. It contains new features that are not present in Vue 2, such as Teleport, Suspense, and multiple root elements per template. It also contains breaking changes that make it incompatible with Vue 2. Full details are documented in the [Vue 3 Migration Guide](https://v3-migration.vuejs.org/).
Despite the differences, the majority of Vue APIs are shared between the two major versions, so most of your Vue 2 knowledge will continue to work in Vue 3. Notably, Composition API was originally a Vue-3-only feature, but has now been backported to Vue 2 and is available in
In general, Vue 3 provides smaller bundle sizes, better performance, better scalability, and better TypeScript / IDE support. If you are starting a new project today, Vue 3 is the recommended choice. There are only a few reasons for you to consider Vue 2 as of now:
  * You need to support IE11. Vue 3 leverages modern JavaScript features and does not support IE11.


If you intend to migrate an existing Vue 2 app to Vue 3, consult the [migration guide](https://v3-migration.vuejs.org/).
## Is Vue 2 Still Supported? [​](https://vuejs.org/about/faq.html#is-vue-2-still-supported)
Vue 2.7, which was shipped in July 2022, is the final minor release of the Vue 2 version range. Vue 2 has entered maintenance mode: it will no longer ship new features, but will continue to receive critical bug fixes and security updates for 18 months starting from the 2.7 release date. This means **Vue 2 reached End of Life on December 31st, 2023**.
We believe this should provide plenty of time for most of the ecosystem to migrate over to Vue 3. However, we also understand that there could be teams or projects that cannot upgrade by this timeline while still needing to fulfill security and compliance requirements. We are partnering with industry experts to provide extended support for Vue 2 for teams with such needs - if your team expects to be using Vue 2 beyond the end of 2023, make sure to plan ahead and learn more about [Vue 2 Extended LTS](https://v2.vuejs.org/lts/).
## What license does Vue use? [​](https://vuejs.org/about/faq.html#what-license-does-vue-use)
Vue is a free and open source project released under the
## What browsers does Vue support? [​](https://vuejs.org/about/faq.html#what-browsers-does-vue-support)
The latest version of Vue (3.x) only supports
## Is Vue reliable? [​](https://vuejs.org/about/faq.html#is-vue-reliable)
Vue is a mature and battle-tested framework. It is one of the most widely used JavaScript frameworks in production today, with over 1.5 million users worldwide, and is downloaded close to 10 million times a month on npm.
Vue is used in production by renowned organizations in varying capacities all around the world, including Wikimedia Foundation, NASA, Apple, Google, Microsoft, GitLab, Zoom, Tencent, Weibo, Bilibili, Kuaishou, and many more.
## Is Vue fast? [​](https://vuejs.org/about/faq.html#is-vue-fast)
Vue 3 is one of the most performant mainstream frontend frameworks, and handles most web application use cases with ease, without the need for manual optimizations.
In stress-testing scenarios, Vue outperforms React and Angular by a decent margin in the
Do note that synthetic benchmarks like the above focus on raw rendering performance with dedicated optimizations and may not be fully representative of real-world performance results. If you care more about page load performance, you are welcome to audit this very website using
You can learn more about how Vue automatically optimizes runtime performance in the [Rendering Mechanism](https://vuejs.org/guide/extras/rendering-mechanism) section, and how to optimize a Vue app in particularly demanding cases in the [Performance Optimization Guide](https://vuejs.org/guide/best-practices/performance).
## Is Vue lightweight? [​](https://vuejs.org/about/faq.html#is-vue-lightweight)
When you use a build tool, many of Vue's APIs are `<Transition>` component, it won't be included in the final production bundle.
A hello world Vue app that only uses the absolutely minimal APIs has a baseline size of only around **16kb** , with minification and brotli compression. The actual size of the application will depend on how many optional features you use from the framework. In the unlikely case where an app uses every single feature that Vue provides, the total runtime size is around **27kb**.
When using Vue without a build tool, we not only lose tree-shaking, but also have to ship the template compiler to the browser. This bloats up the size to around **41kb**. Therefore, if you are using Vue primarily for progressive enhancement without a build step, consider using **6kb**) instead.
Some frameworks, such as Svelte, use a compilation strategy that produces extremely lightweight output in single-component scenarios. However,
## Does Vue scale? [​](https://vuejs.org/about/faq.html#does-vue-scale)
Yes. Despite a common misconception that Vue is only suitable for simple use cases, Vue is perfectly capable of handling large scale applications:
  * [Single-File Components](https://vuejs.org/guide/scaling-up/sfc) provide a modularized development model that allows different parts of an application to be developed in isolation.
  * [Composition API](https://vuejs.org/guide/reusability/composables) provides first-class TypeScript integration and enables clean patterns for organizing, extracting and reusing complex logic.
  * [Comprehensive tooling support](https://vuejs.org/guide/scaling-up/tooling) ensures a smooth development experience as the application grows.
  * Lower barrier to entry and excellent documentation translate to lower onboarding and training costs for new developers.


## How do I contribute to Vue? [​](https://vuejs.org/about/faq.html#how-do-i-contribute-to-vue)
We appreciate your interest! Please check out our [Community Guide](https://vuejs.org/about/community-guide).
## Should I use Options API or Composition API? [​](https://vuejs.org/about/faq.html#should-i-use-options-api-or-composition-api)
If you are new to Vue, we provide a high-level comparison between the two styles [here](https://vuejs.org/guide/introduction#which-to-choose).
If you have previously used Options API and are currently evaluating Composition API, check out [this FAQ](https://vuejs.org/guide/extras/composition-api-faq).
## Should I use JavaScript or TypeScript with Vue? [​](https://vuejs.org/about/faq.html#should-i-use-javascript-or-typescript-with-vue)
While Vue itself is implemented in TypeScript and provides first-class TypeScript support, it does not enforce an opinion on whether you should use TypeScript as a user.
TypeScript support is an important consideration when new features are added to Vue. APIs that are designed with TypeScript in mind are typically easier for IDEs and linters to understand, even if you aren't using TypeScript yourself. Everybody wins. Vue APIs are also designed to work the same way in both JavaScript and TypeScript as much as possible.
Adopting TypeScript involves a trade-off between onboarding complexity and long-term maintainability gains. Whether such a trade-off can be justified can vary depending on your team's background and project scale, but Vue isn't really an influencing factor in making that decision.
## How does Vue compare to Web Components? [​](https://vuejs.org/about/faq.html#how-does-vue-compare-to-web-components)
Vue was created before Web Components were natively available, and some aspects of Vue's design (e.g. slots) were inspired by the Web Components model.
The Web Components specs are relatively low-level, as they are centered around defining custom elements. As a framework, Vue addresses additional higher-level concerns such as efficient DOM rendering, reactive state management, tooling, client-side routing, and server-side rendering.
Vue also fully supports consuming or exporting to native custom elements - check out the [Vue and Web Components Guide](https://vuejs.org/guide/extras/web-components) for more details.
Frequently Asked Questions has loaded
