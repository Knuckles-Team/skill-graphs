[Skip to content](https://vuejs.org/api/reactivity-advanced.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/api/reactivity-advanced)
[日本語 ](https://ja.vuejs.org/api/reactivity-advanced)
[Українська ](https://ua.vuejs.org/api/reactivity-advanced)
[Français ](https://fr.vuejs.org/api/reactivity-advanced)
[한국어 ](https://ko.vuejs.org/api/reactivity-advanced)
[Português ](https://pt.vuejs.org/api/reactivity-advanced)
[বাংলা ](https://bn.vuejs.org/api/reactivity-advanced)
[Italiano ](https://it.vuejs.org/api/reactivity-advanced)
[فارسی ](https://fa.vuejs.org/api/reactivity-advanced)
[Русский ](https://ru.vuejs.org/api/reactivity-advanced)
[Čeština ](https://cs.vuejs.org/api/reactivity-advanced)
[繁體中文 ](https://zh-hk.vuejs.org/api/reactivity-advanced)
[Polski ](https://pl.vuejs.org/api/reactivity-advanced)
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
  * [shallowRef()](https://vuejs.org/api/reactivity-advanced.html#shallowref)
  * [triggerRef()](https://vuejs.org/api/reactivity-advanced.html#triggerref)
  * [customRef()](https://vuejs.org/api/reactivity-advanced.html#customref)
  * [shallowReactive()](https://vuejs.org/api/reactivity-advanced.html#shallowreactive)
  * [shallowReadonly()](https://vuejs.org/api/reactivity-advanced.html#shallowreadonly)
  * [toRaw()](https://vuejs.org/api/reactivity-advanced.html#toraw)
  * [markRaw()](https://vuejs.org/api/reactivity-advanced.html#markraw)
  * [effectScope()](https://vuejs.org/api/reactivity-advanced.html#effectscope)
  * [getCurrentScope()](https://vuejs.org/api/reactivity-advanced.html#getcurrentscope)
  * [onScopeDispose()](https://vuejs.org/api/reactivity-advanced.html#onscopedispose)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Reactivity API: Advanced [​](https://vuejs.org/api/reactivity-advanced.html#reactivity-api-advanced)
## shallowRef() [​](https://vuejs.org/api/reactivity-advanced.html#shallowref)
Shallow version of [`ref()`](https://vuejs.org/api/reactivity-core#ref).
  * **Type**
ts```
function shallowRef<T>(value: T): ShallowRef<T>

interface ShallowRef<T> {
  value: T
}
```

  * **Details**
Unlike `ref()`, the inner value of a shallow ref is stored and exposed as-is, and will not be made deeply reactive. Only the `.value` access is reactive.
`shallowRef()` is typically used for performance optimizations of large data structures, or integration with external state management systems.
  * **Example**
js```
const state = shallowRef({ count: 1 })

// does NOT trigger change
state.value.count = 2

// does trigger change
state.value = { count: 2 }
```

  * **See also**
    * [Guide - Reduce Reactivity Overhead for Large Immutable Structures](https://vuejs.org/guide/best-practices/performance#reduce-reactivity-overhead-for-large-immutable-structures)
    * [Guide - Integration with External State Systems](https://vuejs.org/guide/extras/reactivity-in-depth#integration-with-external-state-systems)


## triggerRef() [​](https://vuejs.org/api/reactivity-advanced.html#triggerref)
Force trigger effects that depend on a [shallow ref](https://vuejs.org/api/reactivity-advanced.html#shallowref). This is typically used after making deep mutations to the inner value of a shallow ref.
  * **Type**
ts```
function triggerRef(ref: ShallowRef): void
```

  * **Example**
js```
const shallow = shallowRef({
  greet: 'Hello, world'
})

// Logs "Hello, world" once for the first run-through
watchEffect(() => {
  console.log(shallow.value.greet)
})

// This won't trigger the effect because the ref is shallow
shallow.value.greet = 'Hello, universe'

// Logs "Hello, universe"
triggerRef(shallow)
```



## customRef() [​](https://vuejs.org/api/reactivity-advanced.html#customref)
Creates a customized ref with explicit control over its dependency tracking and updates triggering.
  * **Type**
ts```
function customRef<T>(factory: CustomRefFactory<T>): Ref<T>

type CustomRefFactory<T> = (
  track: () => void,
  trigger: () => void
) => {
  get: () => T
  set: (value: T) => void
}
```

  * **Details**
`customRef()` expects a factory function, which receives `track` and `trigger` functions as arguments and should return an object with `get` and `set` methods.
In general, `track()` should be called inside `get()`, and `trigger()` should be called inside `set()`. However, you have full control over when they should be called, or whether they should be called at all.
  * **Example**
Creating a debounced ref that only updates the value after a certain timeout after the latest set call:
js```
import { customRef } from 'vue'

export function useDebouncedRef(value, delay = 200) {
  let timeout
  return customRef((track, trigger) => {
    return {
      get() {
        track()
        return value
      },
      set(newValue) {
        clearTimeout(timeout)
        timeout = setTimeout(() => {
          value = newValue
          trigger()
        }, delay)
      }
    }
  })
}
```

Usage in component:
vue```
<script setup>
import { useDebouncedRef } from './debouncedRef'
const text = useDebouncedRef('hello')
</script>

<template>
  <input v-model="text" />
</template>
```

[Try it in the Playground](https://play.vuejs.org/#eNplUkFugzAQ/MqKC1SiIekxIpEq9QVV1BMXCguhBdsyaxqE/PcuGAhNfYGd3Z0ZDwzeq1K7zqB39OI205UiaJGMOieiapTUBAOYFt/wUxqRYf6OBVgotGzA30X5Bt59tX4iMilaAsIbwelxMfCvWNfSD+Gw3++fEhFHTpLFuCBsVJ0ScgUQjw6Az+VatY5PiroHo3IeaeHANlkrh7Qg1NBL43cILUmlMAfqVSXK40QUOSYmHAZHZO0KVkIZgu65kTnWp8Qb+4kHEXfjaDXkhd7DTTmuNZ7MsGyzDYbz5CgSgbdppOBFqqT4l0eX1gZDYOm057heOBQYRl81coZVg9LQWGr+IlrchYKAdJp9h0C6KkvUT3A6u8V1dq4ASqRgZnVnWg04/QWYNyYzC2rD5Y3/hkDgz8fY/cOT1ZjqizMZzGY3rDPC12KGZYyd3J26M8ny1KKx7c3X25q1c1wrZN3L9LCMWs/+AmeG6xI=)
Use with caution
When using customRef, we should be cautious about the return value of its getter, particularly when generating new object datatypes each time the getter is run. This affects the relationship between parent and child components, where such a customRef has been passed as a prop.
The parent component's render function could be triggered by changes to a different reactive state. During rerender, the value of our customRef is reevaluated, returning a new object datatype as a prop to a child component. This prop is compared with its last value in the child component, and since they are different, the reactive dependencies of the customRef are triggered in the child component. Meanwhile, the reactive dependencies in the parent component do not run because the customRef's setter was not called, and its dependencies were not triggered as a result.
[See it in the Playground](https://play.vuejs.org/#eNqFVEtP3DAQ/itTS9Vm1ZCt1J6WBZUiDvTQIsoNcwiOkzU4tmU7+9Aq/71jO1mCWuhlN/PyfPP45kAujCk2HSdLsnLMCuPBcd+Zc6pEa7T1cADWOa/bW17nYMPPtvRsDT3UVrcww+DZ0flStybpKSkWQQqPU0IVVUwr58FYvdvDWXgpu6ek1pqSHL0fS0vJw/z0xbN1jUPHY/Ys87Zkzzl4K5qG2zmcnUN2oAqg4T6bQ/wENKNXNk+CxWKsSlmLTSk7XlhedYxnWclYDiK+MkQCoK4wnVtnIiBJuuEJNA2qPof7hzkEoc8DXgg9yzYTBBFgNr4xyY4FbaK2p6qfI0iqFgtgulOe27HyQRy69Dk1JXY9C03JIeQ6wg4xWvJCqFpnlNytOcyC2wzYulQNr0Ao+Mhw0KnTTEttl/CIaIJiMz8NGBHFtYetVrPwa58/IL48Zag4N0ssquNYLYBoW16J0vOkC3VQtVqk7cG9QcHz1kj0QAlgVYkNMFk6d0bJ1pbGYKUkmtD42HmvFfi94WhOEiXwjUnBnlEz9OLTJwy5qCo44D4O7en71SIFjI/F9VuG4jEy/GHQKq5hQrJAKOc4uNVighBF5/cygS0GgOMoK+HQb7+EWvLdMM7weVIJy5kXWi0Rj+xaNRhLKRp1IvB9hxYegA6WJ1xkUe9PcF4e9a+suA3YwYiC5MQ79KlFUzw5rZCZEUtoRWuE5PaXCXmxtuWIkpJSSr39EXXHQcWYNWfP/9A/uV3QUXJjueN2E1ZhtPnSIqGS+er3T77D76Ox1VUn0fsd4y3HfewCxuT2vVMVwp74RbTX8WQI1dy5qx12xI1Fpa1K5AreeEHCCN8q/QXul+LrSC3s4nh93jltkVPDIYt5KJkcIKStCReo4rVQ/CZI6dyEzToCCJu7hAtry/1QH/qXncQB400KJwqPxZHxEyona0xS/E3rt1m9Ld1rZl+uhaxecRtP3EjtgddCyimtXyj9H/Ii3eId7uOGTkyk/wOEbQ9h)


## shallowReactive() [​](https://vuejs.org/api/reactivity-advanced.html#shallowreactive)
Shallow version of [`reactive()`](https://vuejs.org/api/reactivity-core#reactive).
  * **Type**
ts```
function shallowReactive<T extends object>(target: T): T
```

  * **Details**
Unlike `reactive()`, there is no deep conversion: only root-level properties are reactive for a shallow reactive object. Property values are stored and exposed as-is - this also means properties with ref values will **not** be automatically unwrapped.
Use with Caution
Shallow data structures should only be used for root level state in a component. Avoid nesting it inside a deep reactive object as it creates a tree with inconsistent reactivity behavior which can be difficult to understand and debug.
  * **Example**
js```
const state = shallowReactive({
  foo: 1,
  nested: {
    bar: 2
  }
})

// mutating state's own properties is reactive
state.foo++

// ...but does not convert nested objects
isReactive(state.nested) // false

// NOT reactive
state.nested.bar++
```



## shallowReadonly() [​](https://vuejs.org/api/reactivity-advanced.html#shallowreadonly)
Shallow version of [`readonly()`](https://vuejs.org/api/reactivity-core#readonly).
  * **Type**
ts```
function shallowReadonly<T extends object>(target: T): Readonly<T>
```

  * **Details**
Unlike `readonly()`, there is no deep conversion: only root-level properties are made readonly. Property values are stored and exposed as-is - this also means properties with ref values will **not** be automatically unwrapped.
Use with Caution
Shallow data structures should only be used for root level state in a component. Avoid nesting it inside a deep reactive object as it creates a tree with inconsistent reactivity behavior which can be difficult to understand and debug.
  * **Example**
js```
const state = shallowReadonly({
  foo: 1,
  nested: {
    bar: 2
  }
})

// mutating state's own properties will fail
state.foo++

// ...but works on nested objects
isReadonly(state.nested) // false

// works
state.nested.bar++
```



## toRaw() [​](https://vuejs.org/api/reactivity-advanced.html#toraw)
Returns the raw, original object of a Vue-created proxy.
  * **Type**
ts```
function toRaw<T>(proxy: T): T
```

  * **Details**
`toRaw()` can return the original object from proxies created by [`reactive()`](https://vuejs.org/api/reactivity-core#reactive), [`readonly()`](https://vuejs.org/api/reactivity-core#readonly), [`shallowReactive()`](https://vuejs.org/api/reactivity-advanced.html#shallowreactive) or [`shallowReadonly()`](https://vuejs.org/api/reactivity-advanced.html#shallowreadonly).
This is an escape hatch that can be used to temporarily read without incurring proxy access / tracking overhead or write without triggering changes. It is **not** recommended to hold a persistent reference to the original object. Use with caution.
  * **Example**
js```
const foo = {}
const reactiveFoo = reactive(foo)

console.log(toRaw(reactiveFoo) === foo) // true
```



## markRaw() [​](https://vuejs.org/api/reactivity-advanced.html#markraw)
Marks an object so that it will never be converted to a proxy. Returns the object itself.
  * **Type**
ts```
function markRaw<T extends object>(value: T): T
```

  * **Example**
js```
const foo = markRaw({})
console.log(isReactive(reactive(foo))) // false

// also works when nested inside other reactive objects
const bar = reactive({ foo })
console.log(isReactive(bar.foo)) // false
```

Use with Caution
`markRaw()` and shallow APIs such as `shallowReactive()` allow you to selectively opt-out of the default deep reactive/readonly conversion and embed raw, non-proxied objects in your state graph. They can be used for various reasons:
    * Some values simply should not be made reactive, for example a complex 3rd party class instance, or a Vue component object.
    * Skipping proxy conversion can provide performance improvements when rendering large lists with immutable data sources.
They are considered advanced because the raw opt-out is only at the root level, so if you set a nested, non-marked raw object into a reactive object and then access it again, you get the proxied version back. This can lead to **identity hazards** - i.e. performing an operation that relies on object identity but using both the raw and the proxied version of the same object:
js```
const foo = markRaw({
  nested: {}
})

const bar = reactive({
  // although `foo` is marked as raw, foo.nested is not.
  nested: foo.nested
})

console.log(foo.nested === bar.nested) // false
```

Identity hazards are in general rare. However, to properly utilize these APIs while safely avoiding identity hazards requires a solid understanding of how the reactivity system works.


## effectScope() [​](https://vuejs.org/api/reactivity-advanced.html#effectscope)
Creates an effect scope object which can capture the reactive effects (i.e. computed and watchers) created within it so that these effects can be disposed together. For detailed use cases of this API, please consult its corresponding
  * **Type**
ts```
function effectScope(detached?: boolean): EffectScope

interface EffectScope {
  run<T>(fn: () => T): T | undefined // undefined if scope is inactive
  stop(): void
}
```

  * **Example**
js```
const scope = effectScope()

scope.run(() => {
  const doubled = computed(() => counter.value * 2)

  watch(doubled, () => console.log(doubled.value))

  watchEffect(() => console.log('Count: ', doubled.value))
})

// to dispose all effects in the scope
scope.stop()
```



## getCurrentScope() [​](https://vuejs.org/api/reactivity-advanced.html#getcurrentscope)
Returns the current active [effect scope](https://vuejs.org/api/reactivity-advanced.html#effectscope) if there is one.
  * **Type**
ts```
function getCurrentScope(): EffectScope | undefined
```



## onScopeDispose() [​](https://vuejs.org/api/reactivity-advanced.html#onscopedispose)
Registers a dispose callback on the current active [effect scope](https://vuejs.org/api/reactivity-advanced.html#effectscope). The callback will be invoked when the associated effect scope is stopped.
This method can be used as a non-component-coupled replacement of `onUnmounted` in reusable composition functions, since each Vue component's `setup()` function is also invoked in an effect scope.
A warning will be thrown if this function is called without an active effect scope. In 3.5+, this warning can be suppressed by passing `true` as the second argument.
  * **Type**
ts```
function onScopeDispose(fn: () => void, failSilently?: boolean): void
```



[Reactivity: Utilities](https://vuejs.org/api/reactivity-utilities)[Next Lifecycle Hooks](https://vuejs.org/api/composition-api-lifecycle)
Reactivity API: Advanced has loaded
