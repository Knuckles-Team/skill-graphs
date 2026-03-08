[Skip to content](https://vuejs.org/guide/built-ins/suspense.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/guide/built-ins/suspense)
[日本語 ](https://ja.vuejs.org/guide/built-ins/suspense)
[Українська ](https://ua.vuejs.org/guide/built-ins/suspense)
[Français ](https://fr.vuejs.org/guide/built-ins/suspense)
[한국어 ](https://ko.vuejs.org/guide/built-ins/suspense)
[Português ](https://pt.vuejs.org/guide/built-ins/suspense)
[বাংলা ](https://bn.vuejs.org/guide/built-ins/suspense)
[Italiano ](https://it.vuejs.org/guide/built-ins/suspense)
[فارسی ](https://fa.vuejs.org/guide/built-ins/suspense)
[Русский ](https://ru.vuejs.org/guide/built-ins/suspense)
[Čeština ](https://cs.vuejs.org/guide/built-ins/suspense)
[繁體中文 ](https://zh-hk.vuejs.org/guide/built-ins/suspense)
[Polski ](https://pl.vuejs.org/guide/built-ins/suspense)
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
  * [Async Dependencies](https://vuejs.org/guide/built-ins/suspense.html#async-dependencies)
    * [async setup()](https://vuejs.org/guide/built-ins/suspense.html#async-setup)
    * [Async Components](https://vuejs.org/guide/built-ins/suspense.html#async-components)
  * [Loading State](https://vuejs.org/guide/built-ins/suspense.html#loading-state)
  * [Events](https://vuejs.org/guide/built-ins/suspense.html#events)
  * [Error Handling](https://vuejs.org/guide/built-ins/suspense.html#error-handling)
  * [Combining with Other Components](https://vuejs.org/guide/built-ins/suspense.html#combining-with-other-components)
  * [Nested Suspense](https://vuejs.org/guide/built-ins/suspense.html#nested-suspense)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Suspense [​](https://vuejs.org/guide/built-ins/suspense.html#suspense)
Experimental Feature
`<Suspense>` is an experimental feature. It is not guaranteed to reach stable status and the API may change before it does.
`<Suspense>` is a built-in component for orchestrating async dependencies in a component tree. It can render a loading state while waiting for multiple nested async dependencies down the component tree to be resolved.
## Async Dependencies [​](https://vuejs.org/guide/built-ins/suspense.html#async-dependencies)
To explain the problem `<Suspense>` is trying to solve and how it interacts with these async dependencies, let's imagine a component hierarchy like the following:
```
<Suspense>
└─ <Dashboard>
   ├─ <Profile>
   │  └─ <FriendStatus> (component with async setup())
   └─ <Content>
      ├─ <ActivityFeed> (async component)
      └─ <Stats> (async component)
```

In the component tree there are multiple nested components whose rendering depends on some async resource to be resolved first. Without `<Suspense>`, each of them will need to handle its own loading / error and loaded states. In the worst case scenario, we may see three loading spinners on the page, with content displayed at different times.
The `<Suspense>` component gives us the ability to display top-level loading / error states while we wait on these nested async dependencies to be resolved.
There are two types of async dependencies that `<Suspense>` can wait on:
  1. Components with an async `setup()` hook. This includes components using `<script setup>` with top-level `await` expressions.
  2. [Async Components](https://vuejs.org/guide/components/async).


###  `async setup()` [​](https://vuejs.org/guide/built-ins/suspense.html#async-setup)
A Composition API component's `setup()` hook can be async:
js```
export default {
  async setup() {
    const res = await fetch(...)
    const posts = await res.json()
    return {
      posts
    }
  }
}
```

If using `<script setup>`, the presence of top-level `await` expressions automatically makes the component an async dependency:
vue```
<script setup>
const res = await fetch(...)
const posts = await res.json()
</script>

<template>
  {{ posts }}
</template>
```

### Async Components [​](https://vuejs.org/guide/built-ins/suspense.html#async-components)
Async components are **"suspensible"** by default. This means that if it has a `<Suspense>` in the parent chain, it will be treated as an async dependency of that `<Suspense>`. In this case, the loading state will be controlled by the `<Suspense>`, and the component's own loading, error, delay and timeout options will be ignored.
The async component can opt-out of `Suspense` control and let the component always control its own loading state by specifying `suspensible: false` in its options.
## Loading State [​](https://vuejs.org/guide/built-ins/suspense.html#loading-state)
The `<Suspense>` component has two slots: `#default` and `#fallback`. Both slots only allow for **one** immediate child node. The node in the default slot is shown if possible. If not, the node in the fallback slot will be shown instead.
template```
<Suspense>
  <!-- component with nested async dependencies -->
  <Dashboard />

  <!-- loading state via #fallback slot -->
  <template #fallback>
    Loading...
  </template>
</Suspense>
```

On initial render, `<Suspense>` will render its default slot content in memory. If any async dependencies are encountered during the process, it will enter a **pending** state. During the pending state, the fallback content will be displayed. When all encountered async dependencies have been resolved, `<Suspense>` enters a **resolved** state and the resolved default slot content is displayed.
If no async dependencies were encountered during the initial render, `<Suspense>` will directly go into a resolved state.
Once in a resolved state, `<Suspense>` will only revert to a pending state if the root node of the `#default` slot is replaced. New async dependencies nested deeper in the tree will **not** cause the `<Suspense>` to revert to a pending state.
When a revert happens, fallback content will not be immediately displayed. Instead, `<Suspense>` will display the previous `#default` content while waiting for the new content and its async dependencies to be resolved. This behavior can be configured with the `timeout` prop: `<Suspense>` will switch to fallback content if it takes longer than `timeout` milliseconds to render the new default content. A `timeout` value of `0` will cause the fallback content to be displayed immediately when default content is replaced.
## Events [​](https://vuejs.org/guide/built-ins/suspense.html#events)
The `<Suspense>` component emits 3 events: `pending`, `resolve` and `fallback`. The `pending` event occurs when entering a pending state. The `resolve` event is emitted when new content has finished resolving in the `default` slot. The `fallback` event is fired when the contents of the `fallback` slot are shown.
The events could be used, for example, to show a loading indicator in front of the old DOM while new components are loading.
## Error Handling [​](https://vuejs.org/guide/built-ins/suspense.html#error-handling)
`<Suspense>` currently does not provide error handling via the component itself - however, you can use the [`errorCaptured`](https://vuejs.org/api/options-lifecycle#errorcaptured) option or the [`onErrorCaptured()`](https://vuejs.org/api/composition-api-lifecycle#onerrorcaptured) hook to capture and handle async errors in the parent component of `<Suspense>`.
## Combining with Other Components [​](https://vuejs.org/guide/built-ins/suspense.html#combining-with-other-components)
It is common to want to use `<Suspense>` in combination with the [`<Transition>`](https://vuejs.org/guide/built-ins/transition) and [`<KeepAlive>`](https://vuejs.org/guide/built-ins/keep-alive) components. The nesting order of these components is important to get them all working correctly.
In addition, these components are often used in conjunction with the `<RouterView>` component from [Vue Router](https://router.vuejs.org/).
The following example shows how to nest these components so that they all behave as expected. For simpler combinations you can remove the components that you don't need:
template```
<RouterView v-slot="{ Component }">
  <template v-if="Component">
    <Transition mode="out-in">
      <KeepAlive>
        <Suspense>
          <!-- main content -->
          <component :is="Component"></component>

          <!-- loading state -->
          <template #fallback>
            Loading...
          </template>
        </Suspense>
      </KeepAlive>
    </Transition>
  </template>
</RouterView>
```

Vue Router has built-in support for [lazily loading components](https://router.vuejs.org/guide/advanced/lazy-loading.html) using dynamic imports. These are distinct from async components and currently they will not trigger `<Suspense>`. However, they can still have async components as descendants and those can trigger `<Suspense>` in the usual way.
## Nested Suspense [​](https://vuejs.org/guide/built-ins/suspense.html#nested-suspense)
  * Only supported in 3.3+


When we have multiple async components (common for nested or layout-based routes) like this:
template```
<Suspense>
  <component :is="DynamicAsyncOuter">
    <component :is="DynamicAsyncInner" />
  </component>
</Suspense>
```

`<Suspense>` creates a boundary that will resolve all the async components down the tree, as expected. However, when we change `DynamicAsyncOuter`, `<Suspense>` awaits it correctly, but when we change `DynamicAsyncInner`, the nested `DynamicAsyncInner` renders an empty node until it has been resolved (instead of the previous one or fallback slot).
In order to solve that, we could have a nested suspense to handle the patch for the nested component, like:
template```
<Suspense>
  <component :is="DynamicAsyncOuter">
    <Suspense suspensible> <!-- this -->
      <component :is="DynamicAsyncInner" />
    </Suspense>
  </component>
</Suspense>
```

If you don't set the `suspensible` prop, the inner `<Suspense>` will be treated like a sync component by the parent `<Suspense>`. That means that it has its own fallback slot and if both `Dynamic` components change at the same time, there might be empty nodes and multiple patching cycles while the child `<Suspense>` is loading its own dependency tree, which might not be desirable. When it's set, all the async dependency handling is given to the parent `<Suspense>` (including the events emitted) and the inner `<Suspense>` serves solely as another boundary for the dependency resolution and patching.
* * *
**Related**
  * [`<Suspense>` API reference](https://vuejs.org/api/built-in-components#suspense)


[Teleport](https://vuejs.org/guide/built-ins/teleport)[Next Single-File Components](https://vuejs.org/guide/scaling-up/sfc)
Suspense has loaded
