[Skip to content](https://vuejs.org/api/options-lifecycle.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/api/options-lifecycle)
[日本語 ](https://ja.vuejs.org/api/options-lifecycle)
[Українська ](https://ua.vuejs.org/api/options-lifecycle)
[Français ](https://fr.vuejs.org/api/options-lifecycle)
[한국어 ](https://ko.vuejs.org/api/options-lifecycle)
[Português ](https://pt.vuejs.org/api/options-lifecycle)
[বাংলা ](https://bn.vuejs.org/api/options-lifecycle)
[Italiano ](https://it.vuejs.org/api/options-lifecycle)
[فارسی ](https://fa.vuejs.org/api/options-lifecycle)
[Русский ](https://ru.vuejs.org/api/options-lifecycle)
[Čeština ](https://cs.vuejs.org/api/options-lifecycle)
[繁體中文 ](https://zh-hk.vuejs.org/api/options-lifecycle)
[Polski ](https://pl.vuejs.org/api/options-lifecycle)
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
  * [beforeCreate](https://vuejs.org/api/options-lifecycle.html#beforecreate)
  * [created](https://vuejs.org/api/options-lifecycle.html#created)
  * [beforeMount](https://vuejs.org/api/options-lifecycle.html#beforemount)
  * [mounted](https://vuejs.org/api/options-lifecycle.html#mounted)
  * [beforeUpdate](https://vuejs.org/api/options-lifecycle.html#beforeupdate)
  * [updated](https://vuejs.org/api/options-lifecycle.html#updated)
  * [beforeUnmount](https://vuejs.org/api/options-lifecycle.html#beforeunmount)
  * [unmounted](https://vuejs.org/api/options-lifecycle.html#unmounted)
  * [errorCaptured](https://vuejs.org/api/options-lifecycle.html#errorcaptured)
  * [renderTracked](https://vuejs.org/api/options-lifecycle.html#rendertracked)
  * [renderTriggered](https://vuejs.org/api/options-lifecycle.html#rendertriggered)
  * [activated](https://vuejs.org/api/options-lifecycle.html#activated)
  * [deactivated](https://vuejs.org/api/options-lifecycle.html#deactivated)
  * [serverPrefetch](https://vuejs.org/api/options-lifecycle.html#serverprefetch)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Options: Lifecycle [​](https://vuejs.org/api/options-lifecycle.html#options-lifecycle)
See also
For shared usage of lifecycle hooks, see [Guide - Lifecycle Hooks](https://vuejs.org/guide/essentials/lifecycle)
## beforeCreate [​](https://vuejs.org/api/options-lifecycle.html#beforecreate)
Called when the instance is initialized.
  * **Type**
ts```
interface ComponentOptions {
  beforeCreate?(this: ComponentPublicInstance): void
}
```

  * **Details**
Called immediately when the instance is initialized and props are resolved.
Then the props will be defined as reactive properties and the state such as `data()` or `computed` will be set up.
Note that the `setup()` hook of Composition API is called before any Options API hooks, even `beforeCreate()`.


## created [​](https://vuejs.org/api/options-lifecycle.html#created)
Called after the instance has finished processing all state-related options.
  * **Type**
ts```
interface ComponentOptions {
  created?(this: ComponentPublicInstance): void
}
```

  * **Details**
When this hook is called, the following have been set up: reactive data, computed properties, methods, and watchers. However, the mounting phase has not been started, and the `$el` property will not be available yet.


## beforeMount [​](https://vuejs.org/api/options-lifecycle.html#beforemount)
Called right before the component is to be mounted.
  * **Type**
ts```
interface ComponentOptions {
  beforeMount?(this: ComponentPublicInstance): void
}
```

  * **Details**
When this hook is called, the component has finished setting up its reactive state, but no DOM nodes have been created yet. It is about to execute its DOM render effect for the first time.
**This hook is not called during server-side rendering.**


## mounted [​](https://vuejs.org/api/options-lifecycle.html#mounted)
Called after the component has been mounted.
  * **Type**
ts```
interface ComponentOptions {
  mounted?(this: ComponentPublicInstance): void
}
```

  * **Details**
A component is considered mounted after:
    * All of its synchronous child components have been mounted (does not include async components or components inside `<Suspense>` trees).
    * Its own DOM tree has been created and inserted into the parent container. Note it only guarantees that the component's DOM tree is in-document if the application's root container is also in-document.
This hook is typically used for performing side effects that need access to the component's rendered DOM, or for limiting DOM-related code to the client in a [server-rendered application](https://vuejs.org/guide/scaling-up/ssr).
**This hook is not called during server-side rendering.**


## beforeUpdate [​](https://vuejs.org/api/options-lifecycle.html#beforeupdate)
Called right before the component is about to update its DOM tree due to a reactive state change.
  * **Type**
ts```
interface ComponentOptions {
  beforeUpdate?(this: ComponentPublicInstance): void
}
```

  * **Details**
This hook can be used to access the DOM state before Vue updates the DOM. It is also safe to modify component state inside this hook.
**This hook is not called during server-side rendering.**


## updated [​](https://vuejs.org/api/options-lifecycle.html#updated)
Called after the component has updated its DOM tree due to a reactive state change.
  * **Type**
ts```
interface ComponentOptions {
  updated?(this: ComponentPublicInstance): void
}
```

  * **Details**
A parent component's updated hook is called after that of its child components.
This hook is called after any DOM update of the component, which can be caused by different state changes. If you need to access the updated DOM after a specific state change, use [nextTick()](https://vuejs.org/api/general#nexttick) instead.
**This hook is not called during server-side rendering.**
WARNING
Do not mutate component state in the updated hook - this will likely lead to an infinite update loop!


## beforeUnmount [​](https://vuejs.org/api/options-lifecycle.html#beforeunmount)
Called right before a component instance is to be unmounted.
  * **Type**
ts```
interface ComponentOptions {
  beforeUnmount?(this: ComponentPublicInstance): void
}
```

  * **Details**
When this hook is called, the component instance is still fully functional.
**This hook is not called during server-side rendering.**


## unmounted [​](https://vuejs.org/api/options-lifecycle.html#unmounted)
Called after the component has been unmounted.
  * **Type**
ts```
interface ComponentOptions {
  unmounted?(this: ComponentPublicInstance): void
}
```

  * **Details**
A component is considered unmounted after:
    * All of its child components have been unmounted.
    * All of its associated reactive effects (render effect and computed / watchers created during `setup()`) have been stopped.
Use this hook to clean up manually created side effects such as timers, DOM event listeners or server connections.
**This hook is not called during server-side rendering.**


## errorCaptured [​](https://vuejs.org/api/options-lifecycle.html#errorcaptured)
Called when an error propagating from a descendant component has been captured.
  * **Type**
ts```
interface ComponentOptions {
  errorCaptured?(
    this: ComponentPublicInstance,
    err: unknown,
    instance: ComponentPublicInstance | null,
    info: string
  ): boolean | void
}
```

  * **Details**
Errors can be captured from the following sources:
    * Component renders
    * Event handlers
    * Lifecycle hooks
    * `setup()` function
    * Watchers
    * Custom directive hooks
    * Transition hooks
The hook receives three arguments: the error, the component instance that triggered the error, and an information string specifying the error source type.
TIP
In production, the 3rd argument (`info`) will be a shortened code instead of the full information string. You can find the code to string mapping in the [Production Error Code Reference](https://vuejs.org/error-reference/#runtime-errors).
You can modify component state in `errorCaptured()` to display an error state to the user. However, it is important that the error state should not render the original content that caused the error; otherwise the component will be thrown into an infinite render loop.
The hook can return `false` to stop the error from propagating further. See error propagation details below.
**Error Propagation Rules**
    * By default, all errors are still sent to the application-level [`app.config.errorHandler`](https://vuejs.org/api/application#app-config-errorhandler) if it is defined, so that these errors can still be reported to an analytics service in a single place.
    * If multiple `errorCaptured` hooks exist on a component's inheritance chain or parent chain, all of them will be invoked on the same error, in the order of bottom to top. This is similar to the bubbling mechanism of native DOM events.
    * If the `errorCaptured` hook itself throws an error, both this error and the original captured error are sent to `app.config.errorHandler`.
    * An `errorCaptured` hook can return `false` to prevent the error from propagating further. This is essentially saying "this error has been handled and should be ignored." It will prevent any additional `errorCaptured` hooks or `app.config.errorHandler` from being invoked for this error.
**Error Capturing Caveats**
    * In components with async `setup()` function (with top-level `await`) Vue **will always** try to render component template, even if `setup()` throwed error. This will likely cause more errors because during render component's template might try to access non-existing properties of failed `setup()` context. When capturing errors in such components, be ready to handle errors from both failed async `setup()` (they will always come first) and failed render process.
    * `<Suspense>` will cause hydration mismatches in SSR. Instead, try to separate logic that can possibly throw from child `setup()` into separate function and execute it in the parent component's `setup()`, where you can safely `try/catch` the execution process and make replacement if needed before rendering the actual child component.


## renderTracked [​](https://vuejs.org/api/options-lifecycle.html#rendertracked)
Called when a reactive dependency has been tracked by the component's render effect.
**This hook is development-mode-only and not called during server-side rendering.**
  * **Type**
ts```
interface ComponentOptions {
  renderTracked?(this: ComponentPublicInstance, e: DebuggerEvent): void
}

type DebuggerEvent = {
  effect: ReactiveEffect
  target: object
  type: TrackOpTypes /* 'get' | 'has' | 'iterate' */
  key: any
}
```

  * **See also** [Reactivity in Depth](https://vuejs.org/guide/extras/reactivity-in-depth)


## renderTriggered [​](https://vuejs.org/api/options-lifecycle.html#rendertriggered)
Called when a reactive dependency triggers the component's render effect to be re-run.
**This hook is development-mode-only and not called during server-side rendering.**
  * **Type**
ts```
interface ComponentOptions {
  renderTriggered?(this: ComponentPublicInstance, e: DebuggerEvent): void
}

type DebuggerEvent = {
  effect: ReactiveEffect
  target: object
  type: TriggerOpTypes /* 'set' | 'add' | 'delete' | 'clear' */
  key: any
  newValue?: any
  oldValue?: any
  oldTarget?: Map<any, any> | Set<any>
}
```

  * **See also** [Reactivity in Depth](https://vuejs.org/guide/extras/reactivity-in-depth)


## activated [​](https://vuejs.org/api/options-lifecycle.html#activated)
Called after the component instance is inserted into the DOM as part of a tree cached by [`<KeepAlive>`](https://vuejs.org/api/built-in-components#keepalive).
**This hook is not called during server-side rendering.**
  * **Type**
ts```
interface ComponentOptions {
  activated?(this: ComponentPublicInstance): void
}
```

  * **See also** [Guide - Lifecycle of Cached Instance](https://vuejs.org/guide/built-ins/keep-alive#lifecycle-of-cached-instance)


## deactivated [​](https://vuejs.org/api/options-lifecycle.html#deactivated)
Called after the component instance is removed from the DOM as part of a tree cached by [`<KeepAlive>`](https://vuejs.org/api/built-in-components#keepalive).
**This hook is not called during server-side rendering.**
  * **Type**
ts```
interface ComponentOptions {
  deactivated?(this: ComponentPublicInstance): void
}
```

  * **See also** [Guide - Lifecycle of Cached Instance](https://vuejs.org/guide/built-ins/keep-alive#lifecycle-of-cached-instance)


## serverPrefetch [​](https://vuejs.org/api/options-lifecycle.html#serverprefetch)
Async function to be resolved before the component instance is to be rendered on the server.
  * **Type**
ts```
interface ComponentOptions {
  serverPrefetch?(this: ComponentPublicInstance): Promise<any>
}
```

  * **Details**
If the hook returns a Promise, the server renderer will wait until the Promise is resolved before rendering the component.
This hook is only called during server-side rendering can be used to perform server-only data fetching.
  * **Example**
js```
export default {
  data() {
    return {
      data: null
    }
  },
  async serverPrefetch() {
    // component is rendered as part of the initial request
    // pre-fetch data on server as it is faster than on the client
    this.data = await fetchOnServer(/* ... */)
  },
  async mounted() {
    if (!this.data) {
      // if data is null on mount, it means the component
      // is dynamically rendered on the client. Perform a
      // client-side fetch instead.
      this.data = await fetchOnClient(/* ... */)
    }
  }
}
```

  * **See also** [Server-Side Rendering](https://vuejs.org/guide/scaling-up/ssr)


[Options: Rendering](https://vuejs.org/api/options-rendering)[Next Options: Composition](https://vuejs.org/api/options-composition)
Options: Lifecycle has loaded
