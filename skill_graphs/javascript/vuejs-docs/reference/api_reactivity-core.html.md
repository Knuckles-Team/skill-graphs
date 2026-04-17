[Skip to content](https://vuejs.org/api/reactivity-core.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/api/reactivity-core)
[日本語 ](https://ja.vuejs.org/api/reactivity-core)
[Українська ](https://ua.vuejs.org/api/reactivity-core)
[Français ](https://fr.vuejs.org/api/reactivity-core)
[한국어 ](https://ko.vuejs.org/api/reactivity-core)
[Português ](https://pt.vuejs.org/api/reactivity-core)
[বাংলা ](https://bn.vuejs.org/api/reactivity-core)
[Italiano ](https://it.vuejs.org/api/reactivity-core)
[فارسی ](https://fa.vuejs.org/api/reactivity-core)
[Русский ](https://ru.vuejs.org/api/reactivity-core)
[Čeština ](https://cs.vuejs.org/api/reactivity-core)
[繁體中文 ](https://zh-hk.vuejs.org/api/reactivity-core)
[Polski ](https://pl.vuejs.org/api/reactivity-core)
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
  * [ref()](https://vuejs.org/api/reactivity-core.html#ref)
  * [computed()](https://vuejs.org/api/reactivity-core.html#computed)
  * [reactive()](https://vuejs.org/api/reactivity-core.html#reactive)
  * [readonly()](https://vuejs.org/api/reactivity-core.html#readonly)
  * [watchEffect()](https://vuejs.org/api/reactivity-core.html#watcheffect)
  * [watchPostEffect()](https://vuejs.org/api/reactivity-core.html#watchposteffect)
  * [watchSyncEffect()](https://vuejs.org/api/reactivity-core.html#watchsynceffect)
  * [watch()](https://vuejs.org/api/reactivity-core.html#watch)
  * [onWatcherCleanup()](https://vuejs.org/api/reactivity-core.html#onwatchercleanup)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Reactivity API: Core [​](https://vuejs.org/api/reactivity-core.html#reactivity-api-core)
See also
To better understand the Reactivity APIs, it is recommended to read the following chapters in the guide:
  * [Reactivity Fundamentals](https://vuejs.org/guide/essentials/reactivity-fundamentals) (with the API preference set to Composition API)
  * [Reactivity in Depth](https://vuejs.org/guide/extras/reactivity-in-depth)


## ref() [​](https://vuejs.org/api/reactivity-core.html#ref)
Takes an inner value and returns a reactive and mutable ref object, which has a single property `.value` that points to the inner value.
  * **Type**
ts```
function ref<T>(value: T): Ref<UnwrapRef<T>>

interface Ref<T> {
  value: T
}
```

  * **Details**
The ref object is mutable - i.e. you can assign new values to `.value`. It is also reactive - i.e. any read operations to `.value` are tracked, and write operations will trigger associated effects.
If an object is assigned as a ref's value, the object is made deeply reactive with [reactive()](https://vuejs.org/api/reactivity-core.html#reactive). This also means if the object contains nested refs, they will be deeply unwrapped.
To avoid the deep conversion, use [`shallowRef()`](https://vuejs.org/api/reactivity-advanced#shallowref) instead.
  * **Example**
js```
const count = ref(0)
console.log(count.value) // 0

count.value = 1
console.log(count.value) // 1
```

  * **See also**
    * [Guide - Reactivity Fundamentals with `ref()`](https://vuejs.org/guide/essentials/reactivity-fundamentals#ref)
    * [Guide - Typing `ref()`](https://vuejs.org/guide/typescript/composition-api#typing-ref)


## computed() [​](https://vuejs.org/api/reactivity-core.html#computed)
Takes a [ref](https://vuejs.org/api/reactivity-core.html#ref) object for the returned value from the getter. It can also take an object with `get` and `set` functions to create a writable ref object.
  * **Type**
ts```
// read-only
function computed<T>(
  getter: (oldValue: T | undefined) => T,
  // see "Computed Debugging" link below
  debuggerOptions?: DebuggerOptions
): Readonly<Ref<Readonly<T>>>

// writable
function computed<T>(
  options: {
    get: (oldValue: T | undefined) => T
    set: (value: T) => void
  },
  debuggerOptions?: DebuggerOptions
): Ref<T>
```

  * **Example**
Creating a readonly computed ref:
js```
const count = ref(1)
const plusOne = computed(() => count.value + 1)

console.log(plusOne.value) // 2

plusOne.value++ // error
```

Creating a writable computed ref:
js```
const count = ref(1)
const plusOne = computed({
  get: () => count.value + 1,
  set: (val) => {
    count.value = val - 1
  }
})

plusOne.value = 1
console.log(count.value) // 0
```

Debugging:
js```
const plusOne = computed(() => count.value + 1, {
  onTrack(e) {
    debugger
  },
  onTrigger(e) {
    debugger
  }
})
```

  * **See also**
    * [Guide - Computed Properties](https://vuejs.org/guide/essentials/computed)
    * [Guide - Computed Debugging](https://vuejs.org/guide/extras/reactivity-in-depth#computed-debugging)
    * [Guide - Typing `computed()`](https://vuejs.org/guide/typescript/composition-api#typing-computed)
    * [Guide - Performance - Computed Stability](https://vuejs.org/guide/best-practices/performance#computed-stability)


## reactive() [​](https://vuejs.org/api/reactivity-core.html#reactive)
Returns a reactive proxy of the object.
  * **Type**
ts```
function reactive<T extends object>(target: T): UnwrapNestedRefs<T>
```

  * **Details**
The reactive conversion is "deep": it affects all nested properties. A reactive object also deeply unwraps any properties that are [refs](https://vuejs.org/api/reactivity-core.html#ref) while maintaining reactivity.
It should also be noted that there is no ref unwrapping performed when the ref is accessed as an element of a reactive array or a native collection type like `Map`.
To avoid the deep conversion and only retain reactivity at the root level, use [shallowReactive()](https://vuejs.org/api/reactivity-advanced#shallowreactive) instead.
The returned object and its nested objects are wrapped with **not** equal to the original objects. It is recommended to work exclusively with the reactive proxy and avoid relying on the original object.
  * **Example**
Creating a reactive object:
js```
const obj = reactive({ count: 0 })
obj.count++
```

Ref unwrapping:
ts```
const count = ref(1)
const obj = reactive({ count })

// ref will be unwrapped
console.log(obj.count === count.value) // true

// it will update `obj.count`
count.value++
console.log(count.value) // 2
console.log(obj.count) // 2

// it will also update `count` ref
obj.count++
console.log(obj.count) // 3
console.log(count.value) // 3
```

Note that refs are **not** unwrapped when accessed as array or collection elements:
js```
const books = reactive([ref('Vue 3 Guide')])
// need .value here
console.log(books[0].value)

const map = reactive(new Map([['count', ref(0)]]))
// need .value here
console.log(map.get('count').value)
```

When assigning a [ref](https://vuejs.org/api/reactivity-core.html#ref) to a `reactive` property, that ref will also be automatically unwrapped:
ts```
const count = ref(1)
const obj = reactive({})

obj.count = count

console.log(obj.count) // 1
console.log(obj.count === count.value) // true
```

  * **See also**
    * [Guide - Reactivity Fundamentals](https://vuejs.org/guide/essentials/reactivity-fundamentals)
    * [Guide - Typing `reactive()`](https://vuejs.org/guide/typescript/composition-api#typing-reactive)


## readonly() [​](https://vuejs.org/api/reactivity-core.html#readonly)
Takes an object (reactive or plain) or a [ref](https://vuejs.org/api/reactivity-core.html#ref) and returns a readonly proxy to the original.
  * **Type**
ts```
function readonly<T extends object>(
  target: T
): DeepReadonly<UnwrapNestedRefs<T>>
```

  * **Details**
A readonly proxy is deep: any nested property accessed will be readonly as well. It also has the same ref-unwrapping behavior as `reactive()`, except the unwrapped values will also be made readonly.
To avoid the deep conversion, use [shallowReadonly()](https://vuejs.org/api/reactivity-advanced#shallowreadonly) instead.
  * **Example**
js```
const original = reactive({ count: 0 })

const copy = readonly(original)

watchEffect(() => {
  // works for reactivity tracking
  console.log(copy.count)
})

// mutating original will trigger watchers relying on the copy
original.count++

// mutating the copy will fail and result in a warning
copy.count++ // warning!
```



## watchEffect() [​](https://vuejs.org/api/reactivity-core.html#watcheffect)
Runs a function immediately while reactively tracking its dependencies and re-runs it whenever the dependencies are changed.
  * **Type**
ts```
function watchEffect(
  effect: (onCleanup: OnCleanup) => void,
  options?: WatchEffectOptions
): WatchHandle

type OnCleanup = (cleanupFn: () => void) => void

interface WatchEffectOptions {
  flush?: 'pre' | 'post' | 'sync' // default: 'pre'
  onTrack?: (event: DebuggerEvent) => void
  onTrigger?: (event: DebuggerEvent) => void
}

interface WatchHandle {
  (): void // callable, same as `stop`
  pause: () => void
  resume: () => void
  stop: () => void
}
```

  * **Details**
The first argument is the effect function to be run. The effect function receives a function that can be used to register a cleanup callback. The cleanup callback will be called right before the next time the effect is re-run, and can be used to clean up invalidated side effects, e.g. a pending async request (see example below).
The second argument is an optional options object that can be used to adjust the effect's flush timing or to debug the effect's dependencies.
By default, watchers will run just prior to component rendering. Setting `flush: 'post'` will defer the watcher until after component rendering. See [Callback Flush Timing](https://vuejs.org/guide/essentials/watchers#callback-flush-timing) for more information. In rare cases, it might be necessary to trigger a watcher immediately when a reactive dependency changes, e.g. to invalidate a cache. This can be achieved using `flush: 'sync'`. However, this setting should be used with caution, as it can lead to problems with performance and data consistency if multiple properties are being updated at the same time.
The return value is a handle function that can be called to stop the effect from running again.
  * **Example**
js```
const count = ref(0)

watchEffect(() => console.log(count.value))
// -> logs 0

count.value++
// -> logs 1
```

Stopping the watcher:
js```
const stop = watchEffect(() => {})

// when the watcher is no longer needed:
stop()
```

Pausing / resuming the watcher:
js```
const { stop, pause, resume } = watchEffect(() => {})

// temporarily pause the watcher
pause()

// resume later
resume()

// stop
stop()
```

Side effect cleanup:
js```
watchEffect(async (onCleanup) => {
  const { response, cancel } = doAsyncWork(newId)
  // `cancel` will be called if `id` changes, cancelling
  // the previous request if it hasn't completed yet
  onCleanup(cancel)
  data.value = await response
})
```

Side effect cleanup in 3.5+:
js```
import { onWatcherCleanup } from 'vue'

watchEffect(async () => {
  const { response, cancel } = doAsyncWork(newId)
  // `cancel` will be called if `id` changes, cancelling
  // the previous request if it hasn't completed yet
  onWatcherCleanup(cancel)
  data.value = await response
})
```

Options:
js```
watchEffect(() => {}, {
  flush: 'post',
  onTrack(e) {
    debugger
  },
  onTrigger(e) {
    debugger
  }
})
```

  * **See also**
    * [Guide - Watchers](https://vuejs.org/guide/essentials/watchers#watcheffect)
    * [Guide - Watcher Debugging](https://vuejs.org/guide/extras/reactivity-in-depth#watcher-debugging)


## watchPostEffect() [​](https://vuejs.org/api/reactivity-core.html#watchposteffect)
Alias of [`watchEffect()`](https://vuejs.org/api/reactivity-core.html#watcheffect) with `flush: 'post'` option.
## watchSyncEffect() [​](https://vuejs.org/api/reactivity-core.html#watchsynceffect)
Alias of [`watchEffect()`](https://vuejs.org/api/reactivity-core.html#watcheffect) with `flush: 'sync'` option.
## watch() [​](https://vuejs.org/api/reactivity-core.html#watch)
Watches one or more reactive data sources and invokes a callback function when the sources change.
  * **Type**
ts```
// watching single source
function watch<T>(
  source: WatchSource<T>,
  callback: WatchCallback<T>,
  options?: WatchOptions
): WatchHandle

// watching multiple sources
function watch<T>(
  sources: WatchSource<T>[],
  callback: WatchCallback<T[]>,
  options?: WatchOptions
): WatchHandle

type WatchCallback<T> = (
  value: T,
  oldValue: T,
  onCleanup: (cleanupFn: () => void) => void
) => void

type WatchSource<T> =
  | Ref<T> // ref
  | (() => T) // getter
  | (T extends object ? T : never) // reactive object

interface WatchOptions extends WatchEffectOptions {
  immediate?: boolean // default: false
  deep?: boolean | number // default: false
  flush?: 'pre' | 'post' | 'sync' // default: 'pre'
  onTrack?: (event: DebuggerEvent) => void
  onTrigger?: (event: DebuggerEvent) => void
  once?: boolean // default: false (3.4+)
}

interface WatchHandle {
  (): void // callable, same as `stop`
  pause: () => void
  resume: () => void
  stop: () => void
}
```

> Types are simplified for readability.
  * **Details**
`watch()` is lazy by default - i.e. the callback is only called when the watched source has changed.
The first argument is the watcher's **source**. The source can be one of the following:
    * A getter function that returns a value
    * A ref
    * A reactive object
    * ...or an array of the above.
The second argument is the callback that will be called when the source changes. The callback receives three arguments: the new value, the old value, and a function for registering a side effect cleanup callback. The cleanup callback will be called right before the next time the effect is re-run, and can be used to clean up invalidated side effects, e.g. a pending async request.
When watching multiple sources, the callback receives two arrays containing new / old values corresponding to the source array.
The third optional argument is an options object that supports the following options:
    * **`immediate`**: trigger the callback immediately on watcher creation. Old value will be`undefined` on the first call.
    * **`deep`**: force deep traversal of the source if it is an object, so that the callback fires on deep mutations. In 3.5+, this can also be a number indicating the max traversal depth. See[Deep Watchers](https://vuejs.org/guide/essentials/watchers#deep-watchers).
    * **`flush`**: adjust the callback's flush timing. See[Callback Flush Timing](https://vuejs.org/guide/essentials/watchers#callback-flush-timing) and [`watchEffect()`](https://vuejs.org/api/reactivity-core#watcheffect).
    * **`onTrack / onTrigger`**: debug the watcher's dependencies. See[Watcher Debugging](https://vuejs.org/guide/extras/reactivity-in-depth#watcher-debugging).
    * **`once`**: (3.4+) run the callback only once. The watcher is automatically stopped after the first callback run.
Compared to [`watchEffect()`](https://vuejs.org/api/reactivity-core.html#watcheffect), `watch()` allows us to:
    * Perform the side effect lazily;
    * Be more specific about what state should trigger the watcher to re-run;
    * Access both the previous and current value of the watched state.
  * **Example**
Watching a getter:
js```
const state = reactive({ count: 0 })
watch(
  () => state.count,
  (count, prevCount) => {
    /* ... */
  }
)
```

Watching a ref:
js```
const count = ref(0)
watch(count, (count, prevCount) => {
  /* ... */
})
```

When watching multiple sources, the callback receives arrays containing new / old values corresponding to the source array:
js```
watch([fooRef, barRef], ([foo, bar], [prevFoo, prevBar]) => {
  /* ... */
})
```

When using a getter source, the watcher only fires if the getter's return value has changed. If you want the callback to fire even on deep mutations, you need to explicitly force the watcher into deep mode with `{ deep: true }`. Note in deep mode, the new value and the old will be the same object if the callback was triggered by a deep mutation:
js```
const state = reactive({ count: 0 })
watch(
  () => state,
  (newValue, oldValue) => {
    // newValue === oldValue
  },
  { deep: true }
)
```

When directly watching a reactive object, the watcher is automatically in deep mode:
js```
const state = reactive({ count: 0 })
watch(state, () => {
  /* triggers on deep mutation to state */
})
```

`watch()` shares the same flush timing and debugging options with [`watchEffect()`](https://vuejs.org/api/reactivity-core.html#watcheffect):
js```
watch(source, callback, {
  flush: 'post',
  onTrack(e) {
    debugger
  },
  onTrigger(e) {
    debugger
  }
})
```

Stopping the watcher:
js```
const stop = watch(source, callback)

// when the watcher is no longer needed:
stop()
```

Pausing / resuming the watcher:
js```
const { stop, pause, resume } = watch(() => {})

// temporarily pause the watcher
pause()

// resume later
resume()

// stop
stop()
```

Side effect cleanup:
js```
watch(id, async (newId, oldId, onCleanup) => {
  const { response, cancel } = doAsyncWork(newId)
  // `cancel` will be called if `id` changes, cancelling
  // the previous request if it hasn't completed yet
  onCleanup(cancel)
  data.value = await response
})
```

Side effect cleanup in 3.5+:
js```
import { onWatcherCleanup } from 'vue'

watch(id, async (newId) => {
  const { response, cancel } = doAsyncWork(newId)
  onWatcherCleanup(cancel)
  data.value = await response
})
```

  * **See also**
    * [Guide - Watchers](https://vuejs.org/guide/essentials/watchers)
    * [Guide - Watcher Debugging](https://vuejs.org/guide/extras/reactivity-in-depth#watcher-debugging)


## onWatcherCleanup() [​](https://vuejs.org/api/reactivity-core.html#onwatchercleanup)
Register a cleanup function to be executed when the current watcher is about to re-run. Can only be called during the synchronous execution of a `watchEffect` effect function or `watch` callback function (i.e. it cannot be called after an `await` statement in an async function.)
  * **Type**
ts```
function onWatcherCleanup(
  cleanupFn: () => void,
  failSilently?: boolean
): void
```

  * **Example**
ts```
import { watch, onWatcherCleanup } from 'vue'

watch(id, (newId) => {
  const { response, cancel } = doAsyncWork(newId)
  // `cancel` will be called if `id` changes, cancelling
  // the previous request if it hasn't completed yet
  onWatcherCleanup(cancel)
})
```



[setup()](https://vuejs.org/api/composition-api-setup)[Next Reactivity: Utilities](https://vuejs.org/api/reactivity-utilities)
Reactivity API: Core has loaded
