[Skip to content](https://vuejs.org/api/composition-api-helpers.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/api/composition-api-helpers)
[日本語 ](https://ja.vuejs.org/api/composition-api-helpers)
[Українська ](https://ua.vuejs.org/api/composition-api-helpers)
[Français ](https://fr.vuejs.org/api/composition-api-helpers)
[한국어 ](https://ko.vuejs.org/api/composition-api-helpers)
[Português ](https://pt.vuejs.org/api/composition-api-helpers)
[বাংলা ](https://bn.vuejs.org/api/composition-api-helpers)
[Italiano ](https://it.vuejs.org/api/composition-api-helpers)
[فارسی ](https://fa.vuejs.org/api/composition-api-helpers)
[Русский ](https://ru.vuejs.org/api/composition-api-helpers)
[Čeština ](https://cs.vuejs.org/api/composition-api-helpers)
[繁體中文 ](https://zh-hk.vuejs.org/api/composition-api-helpers)
[Polski ](https://pl.vuejs.org/api/composition-api-helpers)
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
  * [useAttrs()](https://vuejs.org/api/composition-api-helpers.html#useattrs)
  * [useSlots()](https://vuejs.org/api/composition-api-helpers.html#useslots)
  * [useModel()](https://vuejs.org/api/composition-api-helpers.html#usemodel)
  * [useTemplateRef()](https://vuejs.org/api/composition-api-helpers.html#usetemplateref)
  * [useId()](https://vuejs.org/api/composition-api-helpers.html#useid)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Composition API: Helpers [​](https://vuejs.org/api/composition-api-helpers.html#composition-api-helpers)
## useAttrs() [​](https://vuejs.org/api/composition-api-helpers.html#useattrs)
Returns the `attrs` object from the [Setup Context](https://vuejs.org/api/composition-api-setup#setup-context), which includes the [fallthrough attributes](https://vuejs.org/guide/components/attrs#fallthrough-attributes) of the current component. This is intended to be used in `<script setup>` where the setup context object is not available.
  * **Type**
ts```
function useAttrs(): Record<string, unknown>
```



## useSlots() [​](https://vuejs.org/api/composition-api-helpers.html#useslots)
Returns the `slots` object from the [Setup Context](https://vuejs.org/api/composition-api-setup#setup-context), which includes parent passed slots as callable functions that return Virtual DOM nodes. This is intended to be used in `<script setup>` where the setup context object is not available.
If using TypeScript, [`defineSlots()`](https://vuejs.org/api/sfc-script-setup#defineslots) should be preferred instead.
  * **Type**
ts```
function useSlots(): Record<string, (...args: any[]) => VNode[]>
```



## useModel() [​](https://vuejs.org/api/composition-api-helpers.html#usemodel)
This is the underlying helper that powers [`defineModel()`](https://vuejs.org/api/sfc-script-setup#definemodel). If using `<script setup>`, `defineModel()` should be preferred instead.
  * Only available in 3.4+
  * **Type**
ts```
function useModel(
  props: Record<string, any>,
  key: string,
  options?: DefineModelOptions
): ModelRef

type DefineModelOptions<T = any> = {
  get?: (v: T) => any
  set?: (v: T) => any
}

type ModelRef<T, M extends PropertyKey = string, G = T, S = T> = Ref<G, S> & [
  ModelRef<T, M, G, S>,
  Record<M, true | undefined>
]
```

  * **Example**
js```
export default {
  props: ['count'],
  emits: ['update:count'],
  setup(props) {
    const msg = useModel(props, 'count')
    msg.value = 1
  }
}
```

  * **Details**
`useModel()` can be used in non-SFC components, e.g. when using raw `setup()` function. It expects the `props` object as the first argument, and the model name as the second argument. The optional third argument can be used to declare custom getter and setter for the resulting model ref. Note that unlike `defineModel()`, you are responsible for declaring the props and emits yourself.


## useTemplateRef() [​](https://vuejs.org/api/composition-api-helpers.html#usetemplateref)
Returns a shallow ref whose value will be synced with the template element or component with a matching ref attribute.
  * **Type**
ts```
function useTemplateRef<T>(key: string): Readonly<ShallowRef<T | null>>
```

  * **Example**
vue```
<script setup>
import { useTemplateRef, onMounted } from 'vue'

const inputRef = useTemplateRef('input')

onMounted(() => {
  inputRef.value.focus()
})
</script>

<template>
  <input ref="input" />
</template>
```

  * **See also**
    * [Guide - Template Refs](https://vuejs.org/guide/essentials/template-refs)
    * [Guide - Typing Template Refs](https://vuejs.org/guide/typescript/composition-api#typing-template-refs)
    * [Guide - Typing Component Template Refs](https://vuejs.org/guide/typescript/composition-api#typing-component-template-refs)


## useId() [​](https://vuejs.org/api/composition-api-helpers.html#useid)
Used to generate unique-per-application IDs for accessibility attributes or form elements.
  * **Type**
ts```
function useId(): string
```

  * **Example**
vue```
<script setup>
import { useId } from 'vue'

const id = useId()
</script>

<template>
  <form>
    <label :for="id">Name:</label>
    <input :id="id" type="text" />
  </form>
</template>
```

  * **Details**
IDs generated by `useId()` are unique-per-application. It can be used to generate IDs for form elements and accessibility attributes. Multiple calls in the same component will generate different IDs; multiple instances of the same component calling `useId()` will also have different IDs.
IDs generated by `useId()` are also guaranteed to be stable across the server and client renders, so they can be used in SSR applications without leading to hydration mismatches.
If you have more than one Vue application instance of the same page, you can avoid ID conflicts by giving each app an ID prefix via [`app.config.idPrefix`](https://vuejs.org/api/application#app-config-idprefix).
Caution
`useId()` should not be called inside a `computed()` property as it may cause instance conflicts. Instead, declare the ID outside of `computed()` and reference it within the computed function.


[Dependency Injection](https://vuejs.org/api/composition-api-dependency-injection)[Next Options: State](https://vuejs.org/api/options-state)
Composition API: Helpers has loaded
