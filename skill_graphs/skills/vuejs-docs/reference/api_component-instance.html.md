[Skip to content](https://vuejs.org/api/component-instance.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/api/component-instance)
[日本語 ](https://ja.vuejs.org/api/component-instance)
[Українська ](https://ua.vuejs.org/api/component-instance)
[Français ](https://fr.vuejs.org/api/component-instance)
[한국어 ](https://ko.vuejs.org/api/component-instance)
[Português ](https://pt.vuejs.org/api/component-instance)
[বাংলা ](https://bn.vuejs.org/api/component-instance)
[Italiano ](https://it.vuejs.org/api/component-instance)
[فارسی ](https://fa.vuejs.org/api/component-instance)
[Русский ](https://ru.vuejs.org/api/component-instance)
[Čeština ](https://cs.vuejs.org/api/component-instance)
[繁體中文 ](https://zh-hk.vuejs.org/api/component-instance)
[Polski ](https://pl.vuejs.org/api/component-instance)
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
  * [$data](https://vuejs.org/api/component-instance.html#data)
  * [$props](https://vuejs.org/api/component-instance.html#props)
  * [$el](https://vuejs.org/api/component-instance.html#el)
  * [$options](https://vuejs.org/api/component-instance.html#options)
  * [$parent](https://vuejs.org/api/component-instance.html#parent)
  * [$root](https://vuejs.org/api/component-instance.html#root)
  * [$slots](https://vuejs.org/api/component-instance.html#slots)
  * [$refs](https://vuejs.org/api/component-instance.html#refs)
  * [$attrs](https://vuejs.org/api/component-instance.html#attrs)
  * [$watch()](https://vuejs.org/api/component-instance.html#watch)
  * [$emit()](https://vuejs.org/api/component-instance.html#emit)
  * [$forceUpdate()](https://vuejs.org/api/component-instance.html#forceupdate)
  * [$nextTick()](https://vuejs.org/api/component-instance.html#nexttick)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Component Instance [​](https://vuejs.org/api/component-instance.html#component-instance)
INFO
This page documents the built-in properties and methods exposed on the component public instance, i.e. `this`.
All properties listed on this page are readonly (except nested properties in `$data`).
## $data [​](https://vuejs.org/api/component-instance.html#data)
The object returned from the [`data`](https://vuejs.org/api/options-state#data) option, made reactive by the component. The component instance proxies access to the properties on its data object.
  * **Type**
ts```
interface ComponentPublicInstance {
  $data: object
}
```



## $props [​](https://vuejs.org/api/component-instance.html#props)
An object representing the component's current, resolved props.
  * **Type**
ts```
interface ComponentPublicInstance {
  $props: object
}
```

  * **Details**
Only props declared via the [`props`](https://vuejs.org/api/options-state#props) option will be included. The component instance proxies access to the properties on its props object.


## $el [​](https://vuejs.org/api/component-instance.html#el)
The root DOM node that the component instance is managing.
  * **Type**
ts```
interface ComponentPublicInstance {
  $el: any
}
```

  * **Details**
`$el` will be `undefined` until the component is [mounted](https://vuejs.org/api/options-lifecycle#mounted).
    * For components with a single root element, `$el` will point to that element.
    * For components with text root, `$el` will point to the text node.
    * For components with multiple root nodes, `$el` will be the placeholder DOM node that Vue uses to keep track of the component's position in the DOM (a text node, or a comment node in SSR hydration mode).
TIP
For consistency, it is recommended to use [template refs](https://vuejs.org/guide/essentials/template-refs) for direct access to elements instead of relying on `$el`.


## $options [​](https://vuejs.org/api/component-instance.html#options)
The resolved component options used for instantiating the current component instance.
  * **Type**
ts```
interface ComponentPublicInstance {
  $options: ComponentOptions
}
```

  * **Details**
The `$options` object exposes the resolved options for the current component and is the merge result of these possible sources:
    * Global mixins
    * Component `extends` base
    * Component mixins
It is typically used to support custom component options:
js```
const app = createApp({
  customOption: 'foo',
  created() {
    console.log(this.$options.customOption) // => 'foo'
  }
})
```

  * **See also** [`app.config.optionMergeStrategies`](https://vuejs.org/api/application#app-config-optionmergestrategies)


## $parent [​](https://vuejs.org/api/component-instance.html#parent)
The parent instance, if the current instance has one. It will be `null` for the root instance itself.
  * **Type**
ts```
interface ComponentPublicInstance {
  $parent: ComponentPublicInstance | null
}
```



## $root [​](https://vuejs.org/api/component-instance.html#root)
The root component instance of the current component tree. If the current instance has no parents this value will be itself.
  * **Type**
ts```
interface ComponentPublicInstance {
  $root: ComponentPublicInstance
}
```



## $slots [​](https://vuejs.org/api/component-instance.html#slots)
An object representing the [slots](https://vuejs.org/guide/components/slots) passed by the parent component.
  * **Type**
ts```
interface ComponentPublicInstance {
  $slots: { [name: string]: Slot }
}

type Slot = (...args: any[]) => VNode[]
```

  * **Details**
Typically used when manually authoring [render functions](https://vuejs.org/guide/extras/render-function), but can also be used to detect whether a slot is present.
Each slot is exposed on `this.$slots` as a function that returns an array of vnodes under the key corresponding to that slot's name. The default slot is exposed as `this.$slots.default`.
If a slot is a [scoped slot](https://vuejs.org/guide/components/slots#scoped-slots), arguments passed to the slot functions are available to the slot as its slot props.
  * **See also** [Render Functions - Rendering Slots](https://vuejs.org/guide/extras/render-function#rendering-slots)


## $refs [​](https://vuejs.org/api/component-instance.html#refs)
An object of DOM elements and component instances, registered via [template refs](https://vuejs.org/guide/essentials/template-refs).
  * **Type**
ts```
interface ComponentPublicInstance {
  $refs: { [name: string]: Element | ComponentPublicInstance | null }
}
```

  * **See also**
    * [Template refs](https://vuejs.org/guide/essentials/template-refs)
    * [Special Attributes - ref](https://vuejs.org/api/built-in-special-attributes#ref)


## $attrs [​](https://vuejs.org/api/component-instance.html#attrs)
An object that contains the component's fallthrough attributes.
  * **Type**
ts```
interface ComponentPublicInstance {
  $attrs: object
}
```

  * **Details**
[Fallthrough Attributes](https://vuejs.org/guide/components/attrs) are attributes and event handlers passed by the parent component, but not declared as a prop or an emitted event by the child.
By default, everything in `$attrs` will be automatically inherited on the component's root element if there is only a single root element. This behavior is disabled if the component has multiple root nodes, and can be explicitly disabled with the [`inheritAttrs`](https://vuejs.org/api/options-misc#inheritattrs) option.
  * **See also**
    * [Fallthrough Attributes](https://vuejs.org/guide/components/attrs)


## $watch() [​](https://vuejs.org/api/component-instance.html#watch)
Imperative API for creating watchers.
  * **Type**
ts```
interface ComponentPublicInstance {
  $watch(
    source: string | (() => any),
    callback: WatchCallback,
    options?: WatchOptions
  ): StopHandle
}

type WatchCallback<T> = (
  value: T,
  oldValue: T,
  onCleanup: (cleanupFn: () => void) => void
) => void

interface WatchOptions {
  immediate?: boolean // default: false
  deep?: boolean // default: false
  flush?: 'pre' | 'post' | 'sync' // default: 'pre'
  onTrack?: (event: DebuggerEvent) => void
  onTrigger?: (event: DebuggerEvent) => void
}

type StopHandle = () => void
```

  * **Details**
The first argument is the watch source. It can be a component property name string, a simple dot-delimited path string, or a
The second argument is the callback function. The callback receives the new value and the old value of the watched source.
    * **`immediate`**: trigger the callback immediately on watcher creation. Old value will be`undefined` on the first call.
    * **`deep`**: force deep traversal of the source if it is an object, so that the callback fires on deep mutations. See[Deep Watchers](https://vuejs.org/guide/essentials/watchers#deep-watchers).
    * **`flush`**: adjust the callback's flush timing. See[Callback Flush Timing](https://vuejs.org/guide/essentials/watchers#callback-flush-timing) and [`watchEffect()`](https://vuejs.org/api/reactivity-core#watcheffect).
    * **`onTrack / onTrigger`**: debug the watcher's dependencies. See[Watcher Debugging](https://vuejs.org/guide/extras/reactivity-in-depth#watcher-debugging).
  * **Example**
Watch a property name:
js```
this.$watch('a', (newVal, oldVal) => {})
```

Watch a dot-delimited path:
js```
this.$watch('a.b', (newVal, oldVal) => {})
```

Using getter for more complex expressions:
js```
this.$watch(
  // every time the expression `this.a + this.b` yields
  // a different result, the handler will be called.
  // It's as if we were watching a computed property
  // without defining the computed property itself.
  () => this.a + this.b,
  (newVal, oldVal) => {}
)
```

Stopping the watcher:
js```
const unwatch = this.$watch('a', cb)

// later...
unwatch()
```

  * **See also**
    * [Options - `watch`](https://vuejs.org/api/options-state#watch)
    * [Guide - Watchers](https://vuejs.org/guide/essentials/watchers)


## $emit() [​](https://vuejs.org/api/component-instance.html#emit)
Trigger a custom event on the current instance. Any additional arguments will be passed into the listener's callback function.
  * **Type**
ts```
interface ComponentPublicInstance {
  $emit(event: string, ...args: any[]): void
}
```

  * **Example**
js```
export default {
  created() {
    // only event
    this.$emit('foo')
    // with additional arguments
    this.$emit('bar', 1, 2, 3)
  }
}
```

  * **See also**
    * [Component - Events](https://vuejs.org/guide/components/events)
    * [`emits` option](https://vuejs.org/api/options-state#emits)


## $forceUpdate() [​](https://vuejs.org/api/component-instance.html#forceupdate)
Force the component instance to re-render.
  * **Type**
ts```
interface ComponentPublicInstance {
  $forceUpdate(): void
}
```

  * **Details**
This should be rarely needed given Vue's fully automatic reactivity system. The only cases where you may need it is when you have explicitly created non-reactive component state using advanced reactivity APIs.


## $nextTick() [​](https://vuejs.org/api/component-instance.html#nexttick)
Instance-bound version of the global [`nextTick()`](https://vuejs.org/api/general#nexttick).
  * **Type**
ts```
interface ComponentPublicInstance {
  $nextTick(callback?: (this: ComponentPublicInstance) => void): Promise<void>
}
```

  * **Details**
The only difference from the global version of `nextTick()` is that the callback passed to `this.$nextTick()` will have its `this` context bound to the current component instance.
  * **See also** [`nextTick()`](https://vuejs.org/api/general#nexttick)


[Options: Misc](https://vuejs.org/api/options-misc)[Next Directives](https://vuejs.org/api/built-in-directives)
Component Instance has loaded
