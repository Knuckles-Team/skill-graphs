[Skip to content](https://vuejs.org/guide/extras/reactivity-transform.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/guide/extras/reactivity-transform)
[日本語 ](https://ja.vuejs.org/guide/extras/reactivity-transform)
[Українська ](https://ua.vuejs.org/guide/extras/reactivity-transform)
[Français ](https://fr.vuejs.org/guide/extras/reactivity-transform)
[한국어 ](https://ko.vuejs.org/guide/extras/reactivity-transform)
[Português ](https://pt.vuejs.org/guide/extras/reactivity-transform)
[বাংলা ](https://bn.vuejs.org/guide/extras/reactivity-transform)
[Italiano ](https://it.vuejs.org/guide/extras/reactivity-transform)
[فارسی ](https://fa.vuejs.org/guide/extras/reactivity-transform)
[Русский ](https://ru.vuejs.org/guide/extras/reactivity-transform)
[Čeština ](https://cs.vuejs.org/guide/extras/reactivity-transform)
[繁體中文 ](https://zh-hk.vuejs.org/guide/extras/reactivity-transform)
[Polski ](https://pl.vuejs.org/guide/extras/reactivity-transform)
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
  * [Refs vs. Reactive Variables](https://vuejs.org/guide/extras/reactivity-transform.html#refs-vs-reactive-variables)
  * [Destructuring with $()](https://vuejs.org/guide/extras/reactivity-transform.html#destructuring-with)
  * [Convert Existing Refs to Reactive Variables with $()](https://vuejs.org/guide/extras/reactivity-transform.html#convert-existing-refs-to-reactive-variables-with)
  * [Reactive Props Destructure](https://vuejs.org/guide/extras/reactivity-transform.html#reactive-props-destructure)
  * [Retaining Reactivity Across Function Boundaries](https://vuejs.org/guide/extras/reactivity-transform.html#retaining-reactivity-across-function-boundaries)
  * [TypeScript Integration](https://vuejs.org/guide/extras/reactivity-transform.html#typescript-integration)
  * [Explicit Opt-in](https://vuejs.org/guide/extras/reactivity-transform.html#explicit-opt-in)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Reactivity Transform [​](https://vuejs.org/guide/extras/reactivity-transform.html#reactivity-transform)
Removed Experimental Feature
Reactivity Transform was an experimental feature, and has been removed in the latest 3.4 release. Please read about
If you still intend to use it, it is now available via the
Composition-API-specific
Reactivity Transform is a Composition-API-specific feature and requires a build step.
## Refs vs. Reactive Variables [​](https://vuejs.org/guide/extras/reactivity-transform.html#refs-vs-reactive-variables)
Ever since the introduction of the Composition API, one of the primary unresolved questions is the use of refs vs. reactive objects. It's easy to lose reactivity when destructuring reactive objects, while it can be cumbersome to use `.value` everywhere when using refs. Also, `.value` is easy to miss if not using a type system.
vue```
<script setup>
let count = $ref(0)

console.log(count)

function increment() {
  count++
}
</script>

<template>
  <button @click="increment">{{ count }}</button>
</template>
```

The `$ref()` method here is a **compile-time macro** : it is not an actual method that will be called at runtime. Instead, the Vue compiler uses it as a hint to treat the resulting `count` variable as a **reactive variable.**
Reactive variables can be accessed and re-assigned just like normal variables, but these operations are compiled into refs with `.value`. For example, the `<script>` part of the above component is compiled into:
js```
import { ref } from 'vue'

let count = ref(0)

console.log(count.value)

function increment() {
  count.value++
}
```

Every reactivity API that returns refs will have a `$`-prefixed macro equivalent. These APIs include:
  * [`ref`](https://vuejs.org/api/reactivity-core#ref) -> `$ref`
  * [`computed`](https://vuejs.org/api/reactivity-core#computed) -> `$computed`
  * [`shallowRef`](https://vuejs.org/api/reactivity-advanced#shallowref) -> `$shallowRef`
  * [`customRef`](https://vuejs.org/api/reactivity-advanced#customref) -> `$customRef`
  * [`toRef`](https://vuejs.org/api/reactivity-utilities#toref) -> `$toRef`


These macros are globally available and do not need to be imported when Reactivity Transform is enabled, but you can optionally import them from `vue/macros` if you want to be more explicit:
js```
import { $ref } from 'vue/macros'

let count = $ref(0)
```

## Destructuring with `$()` [​](https://vuejs.org/guide/extras/reactivity-transform.html#destructuring-with)
It is common for a composition function to return an object of refs, and use destructuring to retrieve these refs. For this purpose, reactivity transform provides the **`$()`**macro:
js```
import { useMouse } from '@vueuse/core'

const { x, y } = $(useMouse())

console.log(x, y)
```

Compiled output:
js```
import { toRef } from 'vue'
import { useMouse } from '@vueuse/core'

const __temp = useMouse(),
  x = toRef(__temp, 'x'),
  y = toRef(__temp, 'y')

console.log(x.value, y.value)
```

Note that if `x` is already a ref, `toRef(__temp, 'x')` will simply return it as-is and no additional ref will be created. If a destructured value is not a ref (e.g. a function), it will still work - the value will be wrapped in a ref so the rest of the code works as expected.
`$()` destructure works on both reactive objects **and** plain objects containing refs.
## Convert Existing Refs to Reactive Variables with `$()` [​](https://vuejs.org/guide/extras/reactivity-transform.html#convert-existing-refs-to-reactive-variables-with)
In some cases we may have wrapped functions that also return refs. However, the Vue compiler won't be able to know ahead of time that a function is going to return a ref. In such cases, the `$()` macro can also be used to convert any existing refs into reactive variables:
js```
function myCreateRef() {
  return ref(0)
}

let count = $(myCreateRef())
```

## Reactive Props Destructure [​](https://vuejs.org/guide/extras/reactivity-transform.html#reactive-props-destructure)
There are two pain points with the current `defineProps()` usage in `<script setup>`:
  1. Similar to `.value`, you need to always access props as `props.x` in order to retain reactivity. This means you cannot destructure `defineProps` because the resulting destructured variables are not reactive and will not update.
  2. When using the [type-only props declaration](https://vuejs.org/api/sfc-script-setup#type-only-props-emit-declarations), there is no easy way to declare default values for the props. We introduced the `withDefaults()` API for this exact purpose, but it's still clunky to use.


We can address these issues by applying a compile-time transform when `defineProps` is used with destructuring, similar to what we saw earlier with `$()`:
html```
<script setup lang="ts">
  interface Props {
    msg: string
    count?: number
    foo?: string
  }

  const {
    msg,
    // default value just works
    count = 1,
    // local aliasing also just works
    // here we are aliasing `props.foo` to `bar`
    foo: bar
  } = defineProps<Props>()

  watchEffect(() => {
    // will log whenever the props change
    console.log(msg, count, bar)
  })
</script>
```

The above will be compiled into the following runtime declaration equivalent:
js```
export default {
  props: {
    msg: { type: String, required: true },
    count: { type: Number, default: 1 },
    foo: String
  },
  setup(props) {
    watchEffect(() => {
      console.log(props.msg, props.count, props.foo)
    })
  }
}
```

## Retaining Reactivity Across Function Boundaries [​](https://vuejs.org/guide/extras/reactivity-transform.html#retaining-reactivity-across-function-boundaries)
While reactive variables relieve us from having to use `.value` everywhere, it creates an issue of "reactivity loss" when we pass reactive variables across function boundaries. This can happen in two cases:
### Passing into function as argument [​](https://vuejs.org/guide/extras/reactivity-transform.html#passing-into-function-as-argument)
Given a function that expects a ref as an argument, e.g.:
ts```
function trackChange(x: Ref<number>) {
  watch(x, (x) => {
    console.log('x changed!')
  })
}

let count = $ref(0)
trackChange(count) // doesn't work!
```

The above case will not work as expected because it compiles to:
ts```
let count = ref(0)
trackChange(count.value)
```

Here `count.value` is passed as a number, whereas `trackChange` expects an actual ref. This can be fixed by wrapping `count` with `$$()` before passing it:
diff```
let count = $ref(0)
- trackChange(count)
+ trackChange($$(count))
```

The above compiles to:
js```
import { ref } from 'vue'

let count = ref(0)
trackChange(count)
```

As we can see, `$$()` is a macro that serves as an **escape hint** : reactive variables inside `$$()` will not get `.value` appended.
### Returning inside function scope [​](https://vuejs.org/guide/extras/reactivity-transform.html#returning-inside-function-scope)
Reactivity can also be lost if reactive variables are used directly in a returned expression:
ts```
function useMouse() {
  let x = $ref(0)
  let y = $ref(0)

  // listen to mousemove...

  // doesn't work!
  return {
    x,
    y
  }
}
```

The above return statement compiles to:
ts```
return {
  x: x.value,
  y: y.value
}
```

In order to retain reactivity, we should be returning the actual refs, not the current value at return time.
Again, we can use `$$()` to fix this. In this case, `$$()` can be used directly on the returned object - any reference to reactive variables inside the `$$()` call will retain the reference to their underlying refs:
ts```
function useMouse() {
  let x = $ref(0)
  let y = $ref(0)

  // listen to mousemove...

  // fixed
  return $$({
    x,
    y
  })
}
```

### Using `$$()` on destructured props [​](https://vuejs.org/guide/extras/reactivity-transform.html#using-on-destructured-props)
`$$()` works on destructured props since they are reactive variables as well. The compiler will convert it with `toRef` for efficiency:
ts```
const { count } = defineProps<{ count: number }>()

passAsRef($$(count))
```

compiles to:
js```
setup(props) {
  const __props_count = toRef(props, 'count')
  passAsRef(__props_count)
}
```

## TypeScript Integration [​](https://vuejs.org/guide/extras/reactivity-transform.html#typescript-integration)
Vue provides typings for these macros (available globally) and all types will work as expected. There are no incompatibilities with standard TypeScript semantics, so the syntax will work with all existing tooling.
This also means the macros can work in any files where valid JS / TS are allowed - not just inside Vue SFCs.
Since the macros are available globally, their types need to be explicitly referenced (e.g. in a `env.d.ts` file):
ts```
/// <reference types="vue/macros-global" />
```

When explicitly importing the macros from `vue/macros`, the type will work without declaring the globals.
## Explicit Opt-in [​](https://vuejs.org/guide/extras/reactivity-transform.html#explicit-opt-in)
No longer supported in core
The following only applies up to Vue version 3.3 and below. Support has been removed in Vue core 3.4 and above, and `@vitejs/plugin-vue` 5.0 and above. If you intend to continue using the transform, please migrate to
### Vite [​](https://vuejs.org/guide/extras/reactivity-transform.html#vite)
  * Requires `@vitejs/plugin-vue@>=2.0.0`
  * Applies to SFCs and js(x)/ts(x) files. A fast usage check is performed on files before applying the transform so there should be no performance cost for files not using the macros.
  * Note `reactivityTransform` is now a plugin root-level option instead of nested as `script.refSugar`, since it affects not just SFCs.


vite.config.js
js```
export default {
  plugins: [
    vue({
      reactivityTransform: true
    })
  ]
}
```

###  `vue-cli` [​](https://vuejs.org/guide/extras/reactivity-transform.html#vue-cli)
  * Currently only affects SFCs
  * Requires `vue-loader@>=17.0.0`


vue.config.js
js```
module.exports = {
  chainWebpack: (config) => {
    config.module
      .rule('vue')
      .use('vue-loader')
      .tap((options) => {
        return {
          ...options,
          reactivityTransform: true
        }
      })
  }
}
```

### Plain `webpack` + `vue-loader` [​](https://vuejs.org/guide/extras/reactivity-transform.html#plain-webpack-vue-loader)
  * Currently only affects SFCs
  * Requires `vue-loader@>=17.0.0`


webpack.config.js
js```
module.exports = {
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
          reactivityTransform: true
        }
      }
    ]
  }
}
```

[Next Introduction](https://vuejs.org/guide/introduction)
Reactivity Transform has loaded
