[Skip to content](https://vuejs.org/api/reactivity-utilities.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/api/reactivity-utilities)
[日本語 ](https://ja.vuejs.org/api/reactivity-utilities)
[Українська ](https://ua.vuejs.org/api/reactivity-utilities)
[Français ](https://fr.vuejs.org/api/reactivity-utilities)
[한국어 ](https://ko.vuejs.org/api/reactivity-utilities)
[Português ](https://pt.vuejs.org/api/reactivity-utilities)
[বাংলা ](https://bn.vuejs.org/api/reactivity-utilities)
[Italiano ](https://it.vuejs.org/api/reactivity-utilities)
[فارسی ](https://fa.vuejs.org/api/reactivity-utilities)
[Русский ](https://ru.vuejs.org/api/reactivity-utilities)
[Čeština ](https://cs.vuejs.org/api/reactivity-utilities)
[繁體中文 ](https://zh-hk.vuejs.org/api/reactivity-utilities)
[Polski ](https://pl.vuejs.org/api/reactivity-utilities)
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
  * [isRef()](https://vuejs.org/api/reactivity-utilities.html#isref)
  * [unref()](https://vuejs.org/api/reactivity-utilities.html#unref)
  * [toRef()](https://vuejs.org/api/reactivity-utilities.html#toref)
  * [toValue()](https://vuejs.org/api/reactivity-utilities.html#tovalue)
  * [toRefs()](https://vuejs.org/api/reactivity-utilities.html#torefs)
  * [isProxy()](https://vuejs.org/api/reactivity-utilities.html#isproxy)
  * [isReactive()](https://vuejs.org/api/reactivity-utilities.html#isreactive)
  * [isReadonly()](https://vuejs.org/api/reactivity-utilities.html#isreadonly)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Reactivity API: Utilities [​](https://vuejs.org/api/reactivity-utilities.html#reactivity-api-utilities)
## isRef() [​](https://vuejs.org/api/reactivity-utilities.html#isref)
Checks if a value is a ref object.
  * **Type**
ts```
function isRef<T>(r: Ref<T> | unknown): r is Ref<T>
```

Note the return type is a `isRef` can be used as a type guard:
ts```
let foo: unknown
if (isRef(foo)) {
  // foo's type is narrowed to Ref<unknown>
  foo.value
}
```



## unref() [​](https://vuejs.org/api/reactivity-utilities.html#unref)
Returns the inner value if the argument is a ref, otherwise return the argument itself. This is a sugar function for `val = isRef(val) ? val.value : val`.
  * **Type**
ts```
function unref<T>(ref: T | Ref<T>): T
```

  * **Example**
ts```
function useFoo(x: number | Ref<number>) {
  const unwrapped = unref(x)
  // unwrapped is guaranteed to be number now
}
```



## toRef() [​](https://vuejs.org/api/reactivity-utilities.html#toref)
Can be used to normalize values / refs / getters into refs (3.3+).
Can also be used to create a ref for a property on a source reactive object. The created ref is synced with its source property: mutating the source property will update the ref, and vice-versa.
  * **Type**
ts```
// normalization signature (3.3+)
function toRef<T>(
  value: T
): T extends () => infer R
  ? Readonly<Ref<R>>
  : T extends Ref
  ? T
  : Ref<UnwrapRef<T>>

// object property signature
function toRef<T extends object, K extends keyof T>(
  object: T,
  key: K,
  defaultValue?: T[K]
): ToRef<T[K]>

type ToRef<T> = T extends Ref ? T : Ref<T>
```

  * **Example**
Normalization signature (3.3+):
js```
// returns existing refs as-is
toRef(existingRef)

// creates a readonly ref that calls the getter on .value access
toRef(() => props.foo)

// creates normal refs from non-function values
// equivalent to ref(1)
toRef(1)
```

Object property signature:
js```
const state = reactive({
  foo: 1,
  bar: 2
})

// a two-way ref that syncs with the original property
const fooRef = toRef(state, 'foo')

// mutating the ref updates the original
fooRef.value++
console.log(state.foo) // 2

// mutating the original also updates the ref
state.foo++
console.log(fooRef.value) // 3
```

Note this is different from:
js```
const fooRef = ref(state.foo)
```

The above ref is **not** synced with `state.foo`, because the `ref()` receives a plain number value.
`toRef()` is useful when you want to pass the ref of a prop to a composable function:
vue```
<script setup>
import { toRef } from 'vue'

const props = defineProps(/* ... */)

// convert `props.foo` into a ref, then pass into
// a composable
useSomeFeature(toRef(props, 'foo'))

// getter syntax - recommended in 3.3+
useSomeFeature(toRef(() => props.foo))
</script>
```

When `toRef` is used with component props, the usual restrictions around mutating the props still apply. Attempting to assign a new value to the ref is equivalent to trying to modify the prop directly and is not allowed. In that scenario you may want to consider using [`computed`](https://vuejs.org/api/reactivity-core#computed) with `get` and `set` instead. See the guide to [using `v-model` with components](https://vuejs.org/guide/components/v-model) for more information.
When using the object property signature, `toRef()` will return a usable ref even if the source property doesn't currently exist. This makes it possible to work with optional properties, which wouldn't be picked up by [`toRefs`](https://vuejs.org/api/reactivity-utilities.html#torefs).


## toValue() [​](https://vuejs.org/api/reactivity-utilities.html#tovalue)
  * Only supported in 3.3+


Normalizes values / refs / getters to values. This is similar to [unref()](https://vuejs.org/api/reactivity-utilities.html#unref), except that it also normalizes getters. If the argument is a getter, it will be invoked and its return value will be returned.
This can be used in [Composables](https://vuejs.org/guide/reusability/composables) to normalize an argument that can be either a value, a ref, or a getter.
  * **Type**
ts```
function toValue<T>(source: T | Ref<T> | (() => T)): T
```

  * **Example**
js```
toValue(1) //       --> 1
toValue(ref(1)) //  --> 1
toValue(() => 1) // --> 1
```

Normalizing arguments in composables:
ts```
import type { MaybeRefOrGetter } from 'vue'

function useFeature(id: MaybeRefOrGetter<number>) {
  watch(() => toValue(id), id => {
    // react to id changes
  })
}

// this composable supports any of the following:
useFeature(1)
useFeature(ref(1))
useFeature(() => 1)
```



## toRefs() [​](https://vuejs.org/api/reactivity-utilities.html#torefs)
Converts a reactive object to a plain object where each property of the resulting object is a ref pointing to the corresponding property of the original object. Each individual ref is created using [`toRef()`](https://vuejs.org/api/reactivity-utilities.html#toref).
  * **Type**
ts```
function toRefs<T extends object>(
  object: T
): {
  [K in keyof T]: ToRef<T[K]>
}

type ToRef = T extends Ref ? T : Ref<T>
```

  * **Example**
js```
const state = reactive({
  foo: 1,
  bar: 2
})

const stateAsRefs = toRefs(state)
/*
Type of stateAsRefs: {
  foo: Ref<number>,
  bar: Ref<number>
}
*/

// The ref and the original property is "linked"
state.foo++
console.log(stateAsRefs.foo.value) // 2

stateAsRefs.foo.value++
console.log(state.foo) // 3
```

`toRefs` is useful when returning a reactive object from a composable function so that the consuming component can destructure/spread the returned object without losing reactivity:
js```
function useFeatureX() {
  const state = reactive({
    foo: 1,
    bar: 2
  })

  // ...logic operating on state

  // convert to refs when returning
  return toRefs(state)
}

// can destructure without losing reactivity
const { foo, bar } = useFeatureX()
```

`toRefs` will only generate refs for properties that are enumerable on the source object at call time. To create a ref for a property that may not exist yet, use [`toRef`](https://vuejs.org/api/reactivity-utilities.html#toref) instead.


## isProxy() [​](https://vuejs.org/api/reactivity-utilities.html#isproxy)
Checks if an object is a proxy created by [`reactive()`](https://vuejs.org/api/reactivity-core#reactive), [`readonly()`](https://vuejs.org/api/reactivity-core#readonly), [`shallowReactive()`](https://vuejs.org/api/reactivity-advanced#shallowreactive) or [`shallowReadonly()`](https://vuejs.org/api/reactivity-advanced#shallowreadonly).
  * **Type**
ts```
function isProxy(value: any): boolean
```



## isReactive() [​](https://vuejs.org/api/reactivity-utilities.html#isreactive)
Checks if an object is a proxy created by [`reactive()`](https://vuejs.org/api/reactivity-core#reactive) or [`shallowReactive()`](https://vuejs.org/api/reactivity-advanced#shallowreactive).
  * **Type**
ts```
function isReactive(value: unknown): boolean
```



## isReadonly() [​](https://vuejs.org/api/reactivity-utilities.html#isreadonly)
Checks whether the passed value is a readonly object. The properties of a readonly object can change, but they can't be assigned directly via the passed object.
The proxies created by [`readonly()`](https://vuejs.org/api/reactivity-core#readonly) and [`shallowReadonly()`](https://vuejs.org/api/reactivity-advanced#shallowreadonly) are both considered readonly, as is a [`computed()`](https://vuejs.org/api/reactivity-core#computed) ref without a `set` function.
  * **Type**
ts```
function isReadonly(value: unknown): boolean
```



[Reactivity: Core](https://vuejs.org/api/reactivity-core)[Next Reactivity: Advanced](https://vuejs.org/api/reactivity-advanced)
Reactivity API: Utilities has loaded
