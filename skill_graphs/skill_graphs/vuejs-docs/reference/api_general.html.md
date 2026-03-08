[Skip to content](https://vuejs.org/api/general.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/api/general)
[日本語 ](https://ja.vuejs.org/api/general)
[Українська ](https://ua.vuejs.org/api/general)
[Français ](https://fr.vuejs.org/api/general)
[한국어 ](https://ko.vuejs.org/api/general)
[Português ](https://pt.vuejs.org/api/general)
[বাংলা ](https://bn.vuejs.org/api/general)
[Italiano ](https://it.vuejs.org/api/general)
[فارسی ](https://fa.vuejs.org/api/general)
[Русский ](https://ru.vuejs.org/api/general)
[Čeština ](https://cs.vuejs.org/api/general)
[繁體中文 ](https://zh-hk.vuejs.org/api/general)
[Polski ](https://pl.vuejs.org/api/general)
Help Us Translate!
Appearance
Menu
On this page
Sidebar Navigation
## Global API
[Application](https://vuejs.org/api/application)[General](https://vuejs.org/api/general)
## Composition API
[setup()](https://vuejs.org/api/composition-api-setup)[Reactivity: Core](https://vuejs.org/api/reactivity-core)[Reactivity: Utilities](https://vuejs.org/api/reactivity-utilities)[Reactivity: Advanced](https://vuejs.org/api/reactivity-advanced)[Lifecycle Hooks](https://vuejs.org/api/composition-api-lifecycle)[Dependency Injection](https://vuejs.org/api/composition-api-dependency-injection)[Helpers](https://vuejs.org/api/composition-api-helpers)
## Options API
[Options: State](https://vuejs.org/api/options-state)[Options: Rendering](https://vuejs.org/api/options-rendering)[Options: Lifecycle](https://vuejs.org/api/options-lifecycle)[Options: Composition](https://vuejs.org/api/options-composition)[Options: Misc](https://vuejs.org/api/options-misc)[Component Instance](https://vuejs.org/api/component-instance)
## Built-ins
[Directives](https://vuejs.org/api/built-in-directives)[Components](https://vuejs.org/api/built-in-components)[Special Elements](https://vuejs.org/api/built-in-special-elements)[Special Attributes](https://vuejs.org/api/built-in-special-attributes)
## Single-File Component
[Syntax Specification](https://vuejs.org/api/sfc-spec)[<script setup>](https://vuejs.org/api/sfc-script-setup)[CSS Features](https://vuejs.org/api/sfc-css-features)
## Advanced APIs
[Custom Elements](https://vuejs.org/api/custom-elements)[Render Function](https://vuejs.org/api/render-function)[Server-Side Rendering](https://vuejs.org/api/ssr)[TypeScript Utility Types](https://vuejs.org/api/utility-types)[Custom Renderer](https://vuejs.org/api/custom-renderer)[Compile-Time Flags](https://vuejs.org/api/compile-time-flags)
On this page
Table of Contents for current page
  * [version](https://vuejs.org/api/general.html#version)
  * [nextTick()](https://vuejs.org/api/general.html#nexttick)
  * [defineComponent()](https://vuejs.org/api/general.html#definecomponent)
  * [defineAsyncComponent()](https://vuejs.org/api/general.html#defineasynccomponent)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Global API: General [​](https://vuejs.org/api/general.html#global-api-general)
## version [​](https://vuejs.org/api/general.html#version)
Exposes the current version of Vue.
  * **Type:** `string`
  * **Example**
js```
import { version } from 'vue'

console.log(version)
```



## nextTick() [​](https://vuejs.org/api/general.html#nexttick)
A utility for waiting for the next DOM update flush.
  * **Type**
ts```
function nextTick(callback?: () => void): Promise<void>
```

  * **Details**
When you mutate reactive state in Vue, the resulting DOM updates are not applied synchronously. Instead, Vue buffers them until the "next tick" to ensure that each component updates only once no matter how many state changes you have made.
`nextTick()` can be used immediately after a state change to wait for the DOM updates to complete. You can either pass a callback as an argument, or await the returned Promise.
  * **Example**
vue```
<script setup>
import { ref, nextTick } from 'vue'

const count = ref(0)

async function increment() {
  count.value++

  // DOM not yet updated
  console.log(document.getElementById('counter').textContent) // 0

  await nextTick()
  // DOM is now updated
  console.log(document.getElementById('counter').textContent) // 1
}
</script>

<template>
  <button id="counter" @click="increment">{{ count }}</button>
</template>
```

vue```
<script>
import { nextTick } from 'vue'

export default {
  data() {
    return {
      count: 0
    }
  },
  methods: {
    async increment() {
      this.count++

      // DOM not yet updated
      console.log(document.getElementById('counter').textContent) // 0

      await nextTick()
      // DOM is now updated
      console.log(document.getElementById('counter').textContent) // 1
    }
  }
}
</script>

<template>
  <button id="counter" @click="increment">{{ count }}</button>
</template>
```

  * **See also** [`this.$nextTick()`](https://vuejs.org/api/component-instance#nexttick)


## defineComponent() [​](https://vuejs.org/api/general.html#definecomponent)
A type helper for defining a Vue component with type inference.
  * **Type**
ts```
// options syntax
function defineComponent(
  component: ComponentOptions
): ComponentConstructor

// function syntax (requires 3.3+)
function defineComponent(
  setup: ComponentOptions['setup'],
  extraOptions?: ComponentOptions
): () => any
```

> Type is simplified for readability.
  * **Details**
The first argument expects a component options object. The return value will be the same options object, since the function is essentially a runtime no-op for type inference purposes only.
Note that the return type is a bit special: it will be a constructor type whose instance type is the inferred component instance type based on the options. This is used for type inference when the returned type is used as a tag in TSX.
You can extract the instance type of a component (equivalent to the type of `this` in its options) from the return type of `defineComponent()` like this:
ts```
const Foo = defineComponent(/* ... */)

type FooInstance = InstanceType<typeof Foo>
```

### Function Signature [​](https://vuejs.org/api/general.html#function-signature)
    * Only supported in 3.3+
`defineComponent()` also has an alternative signature that is meant to be used with the Composition API and [render functions or JSX](https://vuejs.org/guide/extras/render-function).
Instead of passing in an options object, a function is expected instead. This function works the same as the Composition API [`setup()`](https://vuejs.org/api/composition-api-setup#composition-api-setup) function: it receives the props and the setup context. The return value should be a render function - both `h()` and JSX are supported:
js```
import { ref, h } from 'vue'

const Comp = defineComponent(
  (props) => {
    // use Composition API here like in <script setup>
    const count = ref(0)

    return () => {
      // render function or JSX
      return h('div', count.value)
    }
  },
  // extra options, e.g. declare props and emits
  {
    props: {
      /* ... */
    }
  }
)
```

The main use case for this signature is with TypeScript (and in particular with TSX), as it supports generics:
tsx```
const Comp = defineComponent(
  <T extends string | number>(props: { msg: T; list: T[] }) => {
    // use Composition API here like in <script setup>
    const count = ref(0)

    return () => {
      // render function or JSX
      return <div>{count.value}</div>
    }
  },
  // manual runtime props declaration is currently still needed.
  {
    props: ['msg', 'list']
  }
)
```

In the future, we plan to provide a Babel plugin that automatically infers and injects the runtime props (like for `defineProps` in SFCs) so that the runtime props declaration can be omitted.
### Note on webpack Treeshaking [​](https://vuejs.org/api/general.html#note-on-webpack-treeshaking)
Because `defineComponent()` is a function call, it could look like it would produce side-effects to some build tools, e.g. webpack. This will prevent the component from being tree-shaken even when the component is never used.
To tell webpack that this function call is safe to be tree-shaken, you can add a `/*#__PURE__*/` comment notation before the function call:
js```
export default /*#__PURE__*/ defineComponent(/* ... */)
```

Note this is not necessary if you are using Vite, because Rollup (the underlying production bundler used by Vite) is smart enough to determine that `defineComponent()` is in fact side-effect-free without the need for manual annotations.
  * **See also** [Guide - Using Vue with TypeScript](https://vuejs.org/guide/typescript/overview#general-usage-notes)


## defineAsyncComponent() [​](https://vuejs.org/api/general.html#defineasynccomponent)
Define an async component which is lazy loaded only when it is rendered. The argument can either be a loader function, or an options object for more advanced control of the loading behavior.
  * **Type**
ts```
function defineAsyncComponent(
  source: AsyncComponentLoader | AsyncComponentOptions
): Component

type AsyncComponentLoader = () => Promise<Component>

interface AsyncComponentOptions {
  loader: AsyncComponentLoader
  loadingComponent?: Component
  errorComponent?: Component
  delay?: number
  timeout?: number
  suspensible?: boolean
  onError?: (
    error: Error,
    retry: () => void,
    fail: () => void,
    attempts: number
  ) => any
}
```

  * **See also** [Guide - Async Components](https://vuejs.org/guide/components/async)


[Application](https://vuejs.org/api/application)[Next setup()](https://vuejs.org/api/composition-api-setup)
Global API: General has loaded
