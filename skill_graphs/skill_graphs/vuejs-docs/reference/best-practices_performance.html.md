[Skip to content](https://vuejs.org/guide/best-practices/performance.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/guide/best-practices/performance)
[日本語 ](https://ja.vuejs.org/guide/best-practices/performance)
[Українська ](https://ua.vuejs.org/guide/best-practices/performance)
[Français ](https://fr.vuejs.org/guide/best-practices/performance)
[한국어 ](https://ko.vuejs.org/guide/best-practices/performance)
[Português ](https://pt.vuejs.org/guide/best-practices/performance)
[বাংলা ](https://bn.vuejs.org/guide/best-practices/performance)
[Italiano ](https://it.vuejs.org/guide/best-practices/performance)
[فارسی ](https://fa.vuejs.org/guide/best-practices/performance)
[Русский ](https://ru.vuejs.org/guide/best-practices/performance)
[Čeština ](https://cs.vuejs.org/guide/best-practices/performance)
[繁體中文 ](https://zh-hk.vuejs.org/guide/best-practices/performance)
[Polski ](https://pl.vuejs.org/guide/best-practices/performance)
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
  * [Overview](https://vuejs.org/guide/best-practices/performance.html#overview)
  * [Profiling Options](https://vuejs.org/guide/best-practices/performance.html#profiling-options)
  * [Page Load Optimizations](https://vuejs.org/guide/best-practices/performance.html#page-load-optimizations)
    * [Choosing the Right Architecture](https://vuejs.org/guide/best-practices/performance.html#choosing-the-right-architecture)
    * [Bundle Size and Tree-shaking](https://vuejs.org/guide/best-practices/performance.html#bundle-size-and-tree-shaking)
    * [Code Splitting](https://vuejs.org/guide/best-practices/performance.html#code-splitting)
  * [Update Optimizations](https://vuejs.org/guide/best-practices/performance.html#update-optimizations)
    * [Props Stability](https://vuejs.org/guide/best-practices/performance.html#props-stability)
    * [v-once](https://vuejs.org/guide/best-practices/performance.html#v-once)
    * [v-memo](https://vuejs.org/guide/best-practices/performance.html#v-memo)
    * [Computed Stability](https://vuejs.org/guide/best-practices/performance.html#computed-stability)
  * [General Optimizations](https://vuejs.org/guide/best-practices/performance.html#general-optimizations)
    * [Virtualize Large Lists](https://vuejs.org/guide/best-practices/performance.html#virtualize-large-lists)
    * [Reduce Reactivity Overhead for Large Immutable Structures](https://vuejs.org/guide/best-practices/performance.html#reduce-reactivity-overhead-for-large-immutable-structures)
    * [Avoid Unnecessary Component Abstractions](https://vuejs.org/guide/best-practices/performance.html#avoid-unnecessary-component-abstractions)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Performance [​](https://vuejs.org/guide/best-practices/performance.html#performance)
## Overview [​](https://vuejs.org/guide/best-practices/performance.html#overview)
Vue is designed to be performant for most common use cases without much need for manual optimizations. However, there are always challenging scenarios where extra fine-tuning is needed. In this section, we will discuss what you should pay attention to when it comes to performance in a Vue application.
First, let's discuss the two major aspects of web performance:
  * **Page Load Performance** : how fast the application shows content and becomes interactive on the initial visit. This is usually measured using web vital metrics like
  * **Update Performance** : how fast the application updates in response to user input. For example, how fast a list updates when the user types in a search box, or how fast the page switches when the user clicks a navigation link in a Single-Page Application (SPA).


While it would be ideal to maximize both, different frontend architectures tend to affect how easy it is to attain desired performance in these aspects. In addition, the type of application you are building greatly influences what you should prioritize in terms of performance. Therefore, the first step of ensuring optimal performance is picking the right architecture for the type of application you are building:
  * Consult [Ways of Using Vue](https://vuejs.org/guide/extras/ways-of-using-vue) to see how you can leverage Vue in different ways.
  * Jason Miller discusses the types of web applications and their respective ideal implementation / delivery in


## Profiling Options [​](https://vuejs.org/guide/best-practices/performance.html#profiling-options)
To improve performance, we need to first know how to measure it. There are a number of great tools that can help in this regard:
For profiling load performance of production deployments:
For profiling performance during local development:
  *     * [`app.config.performance`](https://vuejs.org/api/application#app-config-performance) enables Vue-specific performance markers in Chrome DevTools' performance timeline.
  * [Vue DevTools Extension](https://vuejs.org/guide/scaling-up/tooling#browser-devtools) also provides a performance profiling feature.


## Page Load Optimizations [​](https://vuejs.org/guide/best-practices/performance.html#page-load-optimizations)
There are many framework-agnostic aspects for optimizing page load performance - check out
### Choosing the Right Architecture [​](https://vuejs.org/guide/best-practices/performance.html#choosing-the-right-architecture)
If your use case is sensitive to page load performance, avoid shipping it as a pure client-side SPA. You want your server to be directly sending HTML containing the content the users want to see. Pure client-side rendering suffers from slow time-to-content. This can be mitigated with [Server-Side Rendering (SSR)](https://vuejs.org/guide/extras/ways-of-using-vue#fullstack-ssr) or [Static Site Generation (SSG)](https://vuejs.org/guide/extras/ways-of-using-vue#jamstack-ssg). Check out the [SSR Guide](https://vuejs.org/guide/scaling-up/ssr) to learn about performing SSR with Vue. If your app doesn't have rich interactivity requirements, you can also use a traditional backend server to render the HTML and enhance it with Vue on the client.
If your main application has to be an SPA, but has marketing pages (landing, about, blog), ship them separately! Your marketing pages should ideally be deployed as static HTML with minimal JS, by using SSG.
### Bundle Size and Tree-shaking [​](https://vuejs.org/guide/best-practices/performance.html#bundle-size-and-tree-shaking)
One of the most effective ways to improve page load performance is shipping smaller JavaScript bundles. Here are a few ways to reduce bundle size when using Vue:
  * Use a build step if possible.
    * Many of Vue's APIs are `<Transition>` component, it won't be included in the final production bundle. Tree-shaking can also remove other unused modules in your source code.
    * When using a build step, templates are pre-compiled so we don't need to ship the Vue compiler to the browser. This saves **14kb** min+gzipped JavaScript and avoids the runtime compilation cost.
  * Be cautious of size when introducing new dependencies! In real-world applications, bloated bundles are most often a result of introducing heavy dependencies without realizing it.
    * If using a build step, prefer dependencies that offer ES module formats and are tree-shaking friendly. For example, prefer `lodash-es` over `lodash`.
    * Check a dependency's size and evaluate whether it is worth the functionality it provides. Note if the dependency is tree-shaking friendly, the actual size increase will depend on the APIs you actually import from it. Tools like
  * If you are using Vue primarily for progressive enhancement and prefer to avoid a build step, consider using **6kb**) instead.


### Code Splitting [​](https://vuejs.org/guide/best-practices/performance.html#code-splitting)
Code splitting is where a build tool splits the application bundle into multiple smaller chunks, which can then be loaded on demand or in parallel. With proper code splitting, features required at page load can be downloaded immediately, with additional chunks being lazy loaded only when needed, thus improving performance.
Bundlers like Rollup (which Vite is based upon) or webpack can automatically create split chunks by detecting the ESM dynamic import syntax:
js```
// lazy.js and its dependencies will be split into a separate chunk
// and only loaded when `loadLazy()` is called.
function loadLazy() {
  return import('./lazy.js')
}
```

Lazy loading is best used on features that are not immediately needed after initial page load. In Vue applications, this can be used in combination with Vue's [Async Component](https://vuejs.org/guide/components/async) feature to create split chunks for component trees:
js```
import { defineAsyncComponent } from 'vue'

// a separate chunk is created for Foo.vue and its dependencies.
// it is only fetched on demand when the async component is
// rendered on the page.
const Foo = defineAsyncComponent(() => import('./Foo.vue'))
```

For applications using Vue Router, it is strongly recommended to use lazy loading for route components. Vue Router has explicit support for lazy loading, separate from `defineAsyncComponent`. See [Lazy Loading Routes](https://router.vuejs.org/guide/advanced/lazy-loading.html) for more details.
## Update Optimizations [​](https://vuejs.org/guide/best-practices/performance.html#update-optimizations)
### Props Stability [​](https://vuejs.org/guide/best-practices/performance.html#props-stability)
In Vue, a child component only updates when at least one of its received props has changed. Consider the following example:
template```
<ListItem
  v-for="item in list"
  :id="item.id"
  :active-id="activeId" />
```

Inside the `<ListItem>` component, it uses its `id` and `activeId` props to determine whether it is the currently active item. While this works, the problem is that whenever `activeId` changes, **every** `<ListItem>` in the list has to update!
Ideally, only the items whose active status changed should update. We can achieve that by moving the active status computation into the parent, and make `<ListItem>` directly accept an `active` prop instead:
template```
<ListItem
  v-for="item in list"
  :id="item.id"
  :active="item.id === activeId" />
```

Now, for most components the `active` prop will remain the same when `activeId` changes, so they no longer need to update. In general, the idea is keeping the props passed to child components as stable as possible.
###  `v-once` [​](https://vuejs.org/guide/best-practices/performance.html#v-once)
`v-once` is a built-in directive that can be used to render content that relies on runtime data but never needs to update. The entire sub-tree it is used on will be skipped for all future updates. Consult its [API reference](https://vuejs.org/api/built-in-directives#v-once) for more details.
###  `v-memo` [​](https://vuejs.org/guide/best-practices/performance.html#v-memo)
`v-memo` is a built-in directive that can be used to conditionally skip the update of large sub-trees or `v-for` lists. Consult its [API reference](https://vuejs.org/api/built-in-directives#v-memo) for more details.
### Computed Stability [​](https://vuejs.org/guide/best-practices/performance.html#computed-stability)
In Vue 3.4 and above, a computed property will only trigger effects when its computed value has changed from the previous one. For example, the following `isEven` computed only triggers effects if the returned value has changed from `true` to `false`, or vice-versa:
js```
const count = ref(0)
const isEven = computed(() => count.value % 2 === 0)

watchEffect(() => console.log(isEven.value)) // true

// will not trigger new logs because the computed value stays `true`
count.value = 2
count.value = 4
```

This reduces unnecessary effect triggers, but unfortunately doesn't work if the computed creates a new object on each compute:
js```
const computedObj = computed(() => {
  return {
    isEven: count.value % 2 === 0
  }
})
```

Because a new object is created each time, the new value is technically always different from the old value. Even if the `isEven` property remains the same, Vue won't be able to know unless it performs a deep comparison of the old value and the new value. Such comparison could be expensive and likely not worth it.
Instead, we can optimize this by manually comparing the new value with the old value, and conditionally returning the old value if we know nothing has changed:
js```
const computedObj = computed((oldValue) => {
  const newValue = {
    isEven: count.value % 2 === 0
  }
  if (oldValue && oldValue.isEven === newValue.isEven) {
    return oldValue
  }
  return newValue
})
```

[Try it in the playground](https://play.vuejs.org/#eNqVVMtu2zAQ/JUFgSZK4UpuczMkow/40AJ9IC3aQ9mDIlG2EokUyKVt1PC/d0lKtoEminMQQC1nZ4c7S+7Yu66L11awGUtNoesOwQi03ZzLuu2URtiBFtUECtV2FkU5gU2OxWpRVaJA2EOlVQuXxHDJJZeFkgYJayVC5hKj6dUxLnzSjZXmV40rZfFrh3Vb/82xVrLH//5DCQNNKPkweNiNVFP+zBsrIJvDjksgGrRahjVAbRZrIWdBVLz2yBfwBrIsg6mD7LncPyryfIVnywupUmz68HOEEqqCI+XFBQzrOKR79MDdx66GCn1jhpQDZx8f0oZ+nBgdRVcH/aMuBt1xZ80qGvGvh/X6nlXwnGpPl6qsLLxTtitzFFTNl0oSN/79AKOCHHQuS5pw4XorbXsr9ImHZN7nHFdx1SilI78MeOJ7Ca+nbvgd+GgomQOv6CNjSQqXaRJuHd03+kHRdg3JoT+A3a7XsfcmpbcWkQS/LZq6uM84C8o5m4fFuOg0CemeOXXX2w2E6ylsgj2gTgeYio/f1l5UEqj+Z3yC7lGuNDlpApswNNTrql7Gd0ZJeqW8TZw5t+tGaMdDXnA2G4acs7xp1OaTj6G2YjLEi5Uo7h+I35mti3H2TQsj9Jp6etjDXC8Fhu3F9y9iS+vDZqtK2xB6ZPNGGNVYpzHA3ltZkuwTnFf70b+1tVz+MIstCmmGQzmh/p56PGf00H4YOfpR7nV8PTxubP8P2GAP9Q==)
Note that you should always perform the full computation before comparing and returning the old value, so that the same dependencies can be collected on every run.
## General Optimizations [​](https://vuejs.org/guide/best-practices/performance.html#general-optimizations)
> The following tips affect both page load and update performance.
### Virtualize Large Lists [​](https://vuejs.org/guide/best-practices/performance.html#virtualize-large-lists)
One of the most common performance issues in all frontend applications is rendering large lists. No matter how performant a framework is, rendering a list with thousands of items **will** be slow due to the sheer number of DOM nodes that the browser needs to handle.
However, we don't necessarily have to render all these nodes upfront. In most cases, the user's screen size can display only a small subset of our large list. We can greatly improve the performance with **list virtualization** , the technique of only rendering the items that are currently in or close to the viewport in a large list.
Implementing list virtualization isn't easy, luckily there are existing community libraries that you can directly use:
### Reduce Reactivity Overhead for Large Immutable Structures [​](https://vuejs.org/guide/best-practices/performance.html#reduce-reactivity-overhead-for-large-immutable-structures)
Vue's reactivity system is deep by default. While this makes state management intuitive, it does create a certain level of overhead when the data size is large, because every property access triggers proxy traps that perform dependency tracking. This typically becomes noticeable when dealing with large arrays of deeply nested objects, where a single render needs to access 100,000+ properties, so it should only affect very specific use cases.
Vue does provide an escape hatch to opt-out of deep reactivity by using [`shallowRef()`](https://vuejs.org/api/reactivity-advanced#shallowref) and [`shallowReactive()`](https://vuejs.org/api/reactivity-advanced#shallowreactive). Shallow APIs create state that is reactive only at the root level, and exposes all nested objects untouched. This keeps nested property access fast, with the trade-off being that we must now treat all nested objects as immutable, and updates can only be triggered by replacing the root state:
js```
const shallowArray = shallowRef([
  /* big list of deep objects */
])

// this won't trigger updates...
shallowArray.value.push(newObject)
// this does:
shallowArray.value = [...shallowArray.value, newObject]

// this won't trigger updates...
shallowArray.value[0].foo = 1
// this does:
shallowArray.value = [
  {
    ...shallowArray.value[0],
    foo: 1
  },
  ...shallowArray.value.slice(1)
]
```

### Avoid Unnecessary Component Abstractions [​](https://vuejs.org/guide/best-practices/performance.html#avoid-unnecessary-component-abstractions)
Sometimes we may create [renderless components](https://vuejs.org/guide/components/slots#renderless-components) or higher-order components (i.e. components that render other components with extra props) for better abstraction or code organization. While there is nothing wrong with this, do keep in mind that component instances are much more expensive than plain DOM nodes, and creating too many of them due to abstraction patterns will incur performance costs.
Note that reducing only a few instances won't have noticeable effect, so don't sweat it if the component is rendered only a few times in the app. The best scenario to consider this optimization is again in large lists. Imagine a list of 100 items where each item component contains many child components. Removing one unnecessary component abstraction here could result in a reduction of hundreds of component instances.
[Production Deployment](https://vuejs.org/guide/best-practices/production-deployment)[Next Accessibility](https://vuejs.org/guide/best-practices/accessibility)
Performance has loaded
