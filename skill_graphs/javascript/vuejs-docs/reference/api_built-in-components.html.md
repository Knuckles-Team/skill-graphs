[Skip to content](https://vuejs.org/api/built-in-components.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/api/built-in-components)
[日本語 ](https://ja.vuejs.org/api/built-in-components)
[Українська ](https://ua.vuejs.org/api/built-in-components)
[Français ](https://fr.vuejs.org/api/built-in-components)
[한국어 ](https://ko.vuejs.org/api/built-in-components)
[Português ](https://pt.vuejs.org/api/built-in-components)
[বাংলা ](https://bn.vuejs.org/api/built-in-components)
[Italiano ](https://it.vuejs.org/api/built-in-components)
[فارسی ](https://fa.vuejs.org/api/built-in-components)
[Русский ](https://ru.vuejs.org/api/built-in-components)
[Čeština ](https://cs.vuejs.org/api/built-in-components)
[繁體中文 ](https://zh-hk.vuejs.org/api/built-in-components)
[Polski ](https://pl.vuejs.org/api/built-in-components)
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
  * [<Transition>](https://vuejs.org/api/built-in-components.html#transition)
  * [<TransitionGroup>](https://vuejs.org/api/built-in-components.html#transitiongroup)
  * [<KeepAlive>](https://vuejs.org/api/built-in-components.html#keepalive)
  * [<Teleport>](https://vuejs.org/api/built-in-components.html#teleport)
  * [<Suspense>](https://vuejs.org/api/built-in-components.html#suspense)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Built-in Components [​](https://vuejs.org/api/built-in-components.html#built-in-components)
Registration and Usage
Built-in components can be used directly in templates without needing to be registered. They are also tree-shakeable: they are only included in the build when they are used.
When using them in [render functions](https://vuejs.org/guide/extras/render-function), they need to be imported explicitly. For example:
js```
import { h, Transition } from 'vue'

h(Transition, {
  /* props */
})
```

##  `<Transition>` [​](https://vuejs.org/api/built-in-components.html#transition)
Provides animated transition effects to a **single** element or component.
  * **Props**
ts```
interface TransitionProps {
  /**
   * Used to automatically generate transition CSS class names.
   * e.g. `name: 'fade'` will auto expand to `.fade-enter`,
   * `.fade-enter-active`, etc.
   */
  name?: string
  /**
   * Whether to apply CSS transition classes.
   * Default: true
   */
  css?: boolean
  /**
   * Specifies the type of transition events to wait for to
   * determine transition end timing.
   * Default behavior is auto detecting the type that has
   * longer duration.
   */
  type?: 'transition' | 'animation'
  /**
   * Specifies explicit durations of the transition.
   * Default behavior is wait for the first `transitionend`
   * or `animationend` event on the root transition element.
   */
  duration?: number | { enter: number; leave: number }
  /**
   * Controls the timing sequence of leaving/entering transitions.
   * Default behavior is simultaneous.
   */
  mode?: 'in-out' | 'out-in' | 'default'
  /**
   * Whether to apply transition on initial render.
   * Default: false
   */
  appear?: boolean

  /**
   * Props for customizing transition classes.
   * Use kebab-case in templates, e.g. enter-from-class="xxx"
   */
  enterFromClass?: string
  enterActiveClass?: string
  enterToClass?: string
  appearFromClass?: string
  appearActiveClass?: string
  appearToClass?: string
  leaveFromClass?: string
  leaveActiveClass?: string
  leaveToClass?: string
}
```

  * **Events**
    * `@before-enter`
    * `@before-leave`
    * `@enter`
    * `@leave`
    * `@appear`
    * `@after-enter`
    * `@after-leave`
    * `@after-appear`
    * `@enter-cancelled`
    * `@leave-cancelled` (`v-show` only)
    * `@appear-cancelled`
  * **Example**
Simple element:
template```
<Transition>
  <div v-if="ok">toggled content</div>
</Transition>
```

Forcing a transition by changing the `key` attribute:
template```
<Transition>
  <div :key="text">{{ text }}</div>
</Transition>
```

Dynamic component, with transition mode + animate on appear:
template```
<Transition name="fade" mode="out-in" appear>
  <component :is="view"></component>
</Transition>
```

Listening to transition events:
template```
<Transition @after-enter="onTransitionComplete">
  <div v-show="ok">toggled content</div>
</Transition>
```

  * **See also** [Guide - Transition](https://vuejs.org/guide/built-ins/transition)


##  `<TransitionGroup>` [​](https://vuejs.org/api/built-in-components.html#transitiongroup)
Provides transition effects for **multiple** elements or components in a list.
  * **Props**
`<TransitionGroup>` accepts the same props as `<Transition>` except `mode`, plus two additional props:
ts```
interface TransitionGroupProps extends Omit<TransitionProps, 'mode'> {
  /**
   * If not defined, renders as a fragment.
   */
  tag?: string
  /**
   * For customizing the CSS class applied during move transitions.
   * Use kebab-case in templates, e.g. move-class="xxx"
   */
  moveClass?: string
}
```

  * **Events**
`<TransitionGroup>` emits the same events as `<Transition>`.
  * **Details**
By default, `<TransitionGroup>` doesn't render a wrapper DOM element, but one can be defined via the `tag` prop.
Note that every child in a `<transition-group>` must be [**uniquely keyed**](https://vuejs.org/guide/essentials/list#maintaining-state-with-key) for the animations to work properly.
`<TransitionGroup>` supports moving transitions via CSS transform. When a child's position on screen has changed after an update, it will get applied a moving CSS class (auto generated from the `name` attribute or configured with the `move-class` prop). If the CSS `transform` property is "transition-able" when the moving class is applied, the element will be smoothly animated to its destination using the
  * **Example**
template```
<TransitionGroup tag="ul" name="slide">
  <li v-for="item in items" :key="item.id">
    {{ item.text }}
  </li>
</TransitionGroup>
```

  * **See also** [Guide - TransitionGroup](https://vuejs.org/guide/built-ins/transition-group)


##  `<KeepAlive>` [​](https://vuejs.org/api/built-in-components.html#keepalive)
Caches dynamically toggled components wrapped inside.
  * **Props**
ts```
interface KeepAliveProps {
  /**
   * If specified, only components with names matched by
   * `include` will be cached.
   */
  include?: MatchPattern
  /**
   * Any component with a name matched by `exclude` will
   * not be cached.
   */
  exclude?: MatchPattern
  /**
   * The maximum number of component instances to cache.
   */
  max?: number | string
}

type MatchPattern = string | RegExp | (string | RegExp)[]
```

  * **Details**
When wrapped around a dynamic component, `<KeepAlive>` caches the inactive component instances without destroying them.
There can only be one active component instance as the direct child of `<KeepAlive>` at any time.
When a component is toggled inside `<KeepAlive>`, its `activated` and `deactivated` lifecycle hooks will be invoked accordingly, providing an alternative to `mounted` and `unmounted`, which are not called. This applies to the direct child of `<KeepAlive>` as well as to all of its descendants.
  * **Example**
Basic usage:
template```
<KeepAlive>
  <component :is="view"></component>
</KeepAlive>
```

When used with `v-if` / `v-else` branches, there must be only one component rendered at a time:
template```
<KeepAlive>
  <comp-a v-if="a > 1"></comp-a>
  <comp-b v-else></comp-b>
</KeepAlive>
```

Used together with `<Transition>`:
template```
<Transition>
  <KeepAlive>
    <component :is="view"></component>
  </KeepAlive>
</Transition>
```

Using `include` / `exclude`:
template```
<!-- comma-delimited string -->
<KeepAlive include="a,b">
  <component :is="view"></component>
</KeepAlive>

<!-- regex (use `v-bind`) -->
<KeepAlive :include="/a|b/">
  <component :is="view"></component>
</KeepAlive>

<!-- Array (use `v-bind`) -->
<KeepAlive :include="['a', 'b']">
  <component :is="view"></component>
</KeepAlive>
```

Usage with `max`:
template```
<KeepAlive :max="10">
  <component :is="view"></component>
</KeepAlive>
```

  * **See also** [Guide - KeepAlive](https://vuejs.org/guide/built-ins/keep-alive)


##  `<Teleport>` [​](https://vuejs.org/api/built-in-components.html#teleport)
Renders its slot content to another part of the DOM.
  * **Props**
ts```
interface TeleportProps {
  /**
   * Required. Specify target container.
   * Can either be a selector or an actual element.
   */
  to: string | HTMLElement
  /**
   * When `true`, the content will remain in its original
   * location instead of moved into the target container.
   * Can be changed dynamically.
   */
  disabled?: boolean
  /**
   * When `true`, the Teleport will defer until other
   * parts of the application have been mounted before
   * resolving its target. (3.5+)
   */
  defer?: boolean
}
```

  * **Example**
Specifying target container:
template```
<Teleport to="#some-id" />
<Teleport to=".some-class" />
<Teleport to="[data-teleport]" />
```

Conditionally disabling:
template```
<Teleport to="#popup" :disabled="displayVideoInline">
  <video src="./my-movie.mp4">
</Teleport>
```

Defer target resolution
template```
<Teleport defer to="#late-div">...</Teleport>

<!-- somewhere later in the template -->
<div id="late-div"></div>
```

  * **See also** [Guide - Teleport](https://vuejs.org/guide/built-ins/teleport)


##  `<Suspense>` [​](https://vuejs.org/api/built-in-components.html#suspense)
Used for orchestrating nested async dependencies in a component tree.
  * **Props**
ts```
interface SuspenseProps {
  timeout?: string | number
  suspensible?: boolean
}
```

  * **Events**
    * `@resolve`
    * `@pending`
    * `@fallback`
  * **Details**
`<Suspense>` accepts two slots: the `#default` slot and the `#fallback` slot. It will display the content of the fallback slot while rendering the default slot in memory.
If it encounters async dependencies ([Async Components](https://vuejs.org/guide/components/async) and components with [`async setup()`](https://vuejs.org/guide/built-ins/suspense#async-setup)) while rendering the default slot, it will wait until all of them are resolved before displaying the default slot.
By setting the Suspense as `suspensible`, all the async dependency handling will be handled by the parent Suspense. See
  * **See also** [Guide - Suspense](https://vuejs.org/guide/built-ins/suspense)


[Directives](https://vuejs.org/api/built-in-directives)[Next Special Elements](https://vuejs.org/api/built-in-special-elements)
Built-in Components has loaded
