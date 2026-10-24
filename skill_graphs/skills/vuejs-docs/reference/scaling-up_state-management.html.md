[Skip to content](https://vuejs.org/guide/scaling-up/state-management.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/guide/scaling-up/state-management)
[日本語 ](https://ja.vuejs.org/guide/scaling-up/state-management)
[Українська ](https://ua.vuejs.org/guide/scaling-up/state-management)
[Français ](https://fr.vuejs.org/guide/scaling-up/state-management)
[한국어 ](https://ko.vuejs.org/guide/scaling-up/state-management)
[Português ](https://pt.vuejs.org/guide/scaling-up/state-management)
[বাংলা ](https://bn.vuejs.org/guide/scaling-up/state-management)
[Italiano ](https://it.vuejs.org/guide/scaling-up/state-management)
[فارسی ](https://fa.vuejs.org/guide/scaling-up/state-management)
[Русский ](https://ru.vuejs.org/guide/scaling-up/state-management)
[Čeština ](https://cs.vuejs.org/guide/scaling-up/state-management)
[繁體中文 ](https://zh-hk.vuejs.org/guide/scaling-up/state-management)
[Polski ](https://pl.vuejs.org/guide/scaling-up/state-management)
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
  * [What is State Management?](https://vuejs.org/guide/scaling-up/state-management.html#what-is-state-management)
  * [Simple State Management with Reactivity API](https://vuejs.org/guide/scaling-up/state-management.html#simple-state-management-with-reactivity-api)
  * [SSR Considerations](https://vuejs.org/guide/scaling-up/state-management.html#ssr-considerations)
  * [Pinia](https://vuejs.org/guide/scaling-up/state-management.html#pinia)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# State Management [​](https://vuejs.org/guide/scaling-up/state-management.html#state-management)
## What is State Management? [​](https://vuejs.org/guide/scaling-up/state-management.html#what-is-state-management)
Technically, every Vue component instance already "manages" its own reactive state. Take a simple counter component as an example:
vue```
<script setup>
import { ref } from 'vue'

// state
const count = ref(0)

// actions
function increment() {
  count.value++
}
</script>

<!-- view -->
<template>{{ count }}</template>
```

vue```
<script>
export default {
  // state
  data() {
    return {
      count: 0
    }
  },
  // actions
  methods: {
    increment() {
      this.count++
    }
  }
}
</script>

<!-- view -->
<template>{{ count }}</template>
```

It is a self-contained unit with the following parts:
  * The **state** , the source of truth that drives our app;
  * The **view** , a declarative mapping of the **state** ;
  * The **actions** , the possible ways the state could change in reaction to user inputs from the **view**.


This is a simple representation of the concept of "one-way data flow":
![state flow diagram](https://vuejs.org/assets/state-flow.Cd6No79V.png)
However, the simplicity starts to break down when we have **multiple components that share a common state** :
  1. Multiple views may depend on the same piece of state.
  2. Actions from different views may need to mutate the same piece of state.


For case one, a possible workaround is by "lifting" the shared state up to a common ancestor component, and then pass it down as props. However, this quickly gets tedious in component trees with deep hierarchies, leading to another problem known as [Prop Drilling](https://vuejs.org/guide/components/provide-inject#prop-drilling).
For case two, we often find ourselves resorting to solutions such as reaching for direct parent / child instances via template refs, or trying to mutate and synchronize multiple copies of the state via emitted events. Both of these patterns are brittle and quickly lead to unmaintainable code.
A simpler and more straightforward solution is to extract the shared state out of the components, and manage it in a global singleton. With this, our component tree becomes a big "view", and any component can access the state or trigger actions, no matter where they are in the tree!
## Simple State Management with Reactivity API [​](https://vuejs.org/guide/scaling-up/state-management.html#simple-state-management-with-reactivity-api)
In Options API, reactive data is declared using the `data()` option. Internally, the object returned by `data()` is made reactive via the [`reactive()`](https://vuejs.org/api/reactivity-core#reactive) function, which is also available as a public API.
If you have a piece of state that should be shared by multiple instances, you can use [`reactive()`](https://vuejs.org/api/reactivity-core#reactive) to create a reactive object, and then import it into multiple components:
store.js
js```
import { reactive } from 'vue'

export const store = reactive({
  count: 0
})
```

ComponentA.vue
vue```
<script setup>
import { store } from './store.js'
</script>

<template>From A: {{ store.count }}</template>
```

ComponentB.vue
vue```
<script setup>
import { store } from './store.js'
</script>

<template>From B: {{ store.count }}</template>
```

ComponentA.vue
vue```
<script>
import { store } from './store.js'

export default {
  data() {
    return {
      store
    }
  }
}
</script>

<template>From A: {{ store.count }}</template>
```

ComponentB.vue
vue```
<script>
import { store } from './store.js'

export default {
  data() {
    return {
      store
    }
  }
}
</script>

<template>From B: {{ store.count }}</template>
```

Now whenever the `store` object is mutated, both `<ComponentA>` and `<ComponentB>` will update their views automatically - we have a single source of truth now.
However, this also means any component importing `store` can mutate it however they want:
template```
<template>
  <button @click="store.count++">
    From B: {{ store.count }}
  </button>
</template>
```

While this works in simple cases, global state that can be arbitrarily mutated by any component is not going to be very maintainable in the long run. To ensure the state-mutating logic is centralized like the state itself, it is recommended to define methods on the store with names that express the intention of the actions:
store.js
js```
import { reactive } from 'vue'

export const store = reactive({
  count: 0,
  increment() {
    this.count++
  }
})
```

template```
<template>
  <button @click="store.increment()">
    From B: {{ store.count }}
  </button>
</template>
```

[Try it in the Playground](https://play.vuejs.org/#eNrNkk1uwyAQha8yYpNEiUzXllPVrtRTeJNSqtLGgGBsVbK4ewdwnT9FWWSTFczwmPc+xMhqa4uhl6xklRdOWQQvsbfPrVadNQ7h1dCqpcYaPp3pYFHwQyteXVxKm0tpM0krnm3IgAqUnd3vUFIFUB1Z8bNOkzoVny+wDTuNcZ1gBI/GSQhzqlQX3/5Gng81pA1t33tEo+FF7JX42bYsT1BaONlRguWqZZMU4C261CWMk3EhTK8RQphm8Twse/BscoUsvdqDkTX3kP3nI6aZwcmdQDUcMPJPabX8TQphtCf0RLqd1csxuqQAJTxtYnEUGtIpAH4pn1Ou17FDScOKhT+QNAVM)
[Try it in the Playground](https://play.vuejs.org/#eNrdU8FqhDAU/JVHLruyi+lZ3FIt9Cu82JilaTWR5CkF8d8bE5O1u1so9FYQzAyTvJnRTKTo+3QcOMlIbpgWPT5WUnS90gjPyr4ll1jAWasOdim9UMum3a20vJWWqxSgkvzTyRt+rocWYVpYFoQm8wRsJh+viHLBcyXtk9No2ALkXd/WyC0CyDfW6RVTOiancQM5ku+x7nUxgUGlOcwxn8Ppu7HJ7udqaqz3SYikOQ5aBgT+OA9slt9kasToFnb5OiAqCU+sFezjVBHvRUimeWdT7JOKrFKAl8VvYatdI6RMDRJhdlPtWdQf5mdQP+SHdtyX/IftlH9pJyS1vcQ2NK8ZivFSiL8BsQmmpMG1s1NU79frYA1k8OD+/I3pUA6+CeNdHg6hmoTMX9pPSnk=)
TIP
Note the click handler uses `store.increment()` with parentheses - this is necessary to call the method with the proper `this` context since it's not a component method.
Although here we are using a single reactive object as a store, you can also share reactive state created using other [Reactivity APIs](https://vuejs.org/api/reactivity-core) such as `ref()` or `computed()`, or even return global state from a [Composable](https://vuejs.org/guide/reusability/composables):
js```
import { ref } from 'vue'

// global state, created in module scope
const globalCount = ref(1)

export function useCount() {
  // local state, created per-component
  const localCount = ref(1)

  return {
    globalCount,
    localCount
  }
}
```

The fact that Vue's reactivity system is decoupled from the component model makes it extremely flexible.
## SSR Considerations [​](https://vuejs.org/guide/scaling-up/state-management.html#ssr-considerations)
If you are building an application that leverages [Server-Side Rendering (SSR)](https://vuejs.org/guide/scaling-up/ssr), the above pattern can lead to issues due to the store being a singleton shared across multiple requests. This is discussed in [more details](https://vuejs.org/guide/scaling-up/ssr#cross-request-state-pollution) in the SSR guide.
## Pinia [​](https://vuejs.org/guide/scaling-up/state-management.html#pinia)
While our hand-rolled state management solution will suffice in simple scenarios, there are many more things to consider in large-scale production applications:
  * Stronger conventions for team collaboration
  * Integrating with the Vue DevTools, including timeline, in-component inspection, and time-travel debugging
  * Hot Module Replacement
  * Server-Side Rendering support


[Pinia](https://pinia.vuejs.org) is a state management library that implements all of the above. It is maintained by the Vue core team, and works with both Vue 2 and Vue 3.
Existing users may be familiar with [Vuex](https://vuex.vuejs.org/), the previous official state management library for Vue. With Pinia serving the same role in the ecosystem, Vuex is now in maintenance mode. It still works, but will no longer receive new features. It is recommended to use Pinia for new applications.
Pinia started out as an exploration of what the next iteration of Vuex could look like, incorporating many ideas from core team discussions for Vuex 5. Eventually, we realized that Pinia already implements most of what we wanted in Vuex 5, and decided to make it the new recommendation instead.
Compared to Vuex, Pinia provides a simpler API with less ceremony, offers Composition-API-style APIs, and most importantly, has solid type inference support when used with TypeScript.
[Routing](https://vuejs.org/guide/scaling-up/routing)[Next Testing](https://vuejs.org/guide/scaling-up/testing)
State Management has loaded
