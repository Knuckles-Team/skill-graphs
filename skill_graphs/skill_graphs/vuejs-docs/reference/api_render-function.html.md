[Skip to content](https://vuejs.org/api/render-function.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/api/render-function)
[日本語 ](https://ja.vuejs.org/api/render-function)
[Українська ](https://ua.vuejs.org/api/render-function)
[Français ](https://fr.vuejs.org/api/render-function)
[한국어 ](https://ko.vuejs.org/api/render-function)
[Português ](https://pt.vuejs.org/api/render-function)
[বাংলা ](https://bn.vuejs.org/api/render-function)
[Italiano ](https://it.vuejs.org/api/render-function)
[فارسی ](https://fa.vuejs.org/api/render-function)
[Русский ](https://ru.vuejs.org/api/render-function)
[Čeština ](https://cs.vuejs.org/api/render-function)
[繁體中文 ](https://zh-hk.vuejs.org/api/render-function)
[Polski ](https://pl.vuejs.org/api/render-function)
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
  * [h()](https://vuejs.org/api/render-function.html#h)
  * [mergeProps()](https://vuejs.org/api/render-function.html#mergeprops)
  * [cloneVNode()](https://vuejs.org/api/render-function.html#clonevnode)
  * [isVNode()](https://vuejs.org/api/render-function.html#isvnode)
  * [resolveComponent()](https://vuejs.org/api/render-function.html#resolvecomponent)
  * [resolveDirective()](https://vuejs.org/api/render-function.html#resolvedirective)
  * [withDirectives()](https://vuejs.org/api/render-function.html#withdirectives)
  * [withModifiers()](https://vuejs.org/api/render-function.html#withmodifiers)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Render Function APIs [​](https://vuejs.org/api/render-function.html#render-function-apis)
## h() [​](https://vuejs.org/api/render-function.html#h)
Creates virtual DOM nodes (vnodes).
  * **Type**
ts```
// full signature
function h(
  type: string | Component,
  props?: object | null,
  children?: Children | Slot | Slots
): VNode

// omitting props
function h(type: string | Component, children?: Children | Slot): VNode

type Children = string | number | boolean | VNode | null | Children[]

type Slot = () => Children

type Slots = { [name: string]: Slot }
```

> Types are simplified for readability.
  * **Details**
The first argument can either be a string (for native elements) or a Vue component definition. The second argument is the props to be passed, and the third argument is the children.
When creating a component vnode, the children must be passed as slot functions. A single slot function can be passed if the component expects only the default slot. Otherwise, the slots must be passed as an object of slot functions.
For convenience, the props argument can be omitted when the children is not a slots object.
  * **Example**
Creating native elements:
js```
import { h } from 'vue'

// all arguments except the type are optional
h('div')
h('div', { id: 'foo' })

// both attributes and properties can be used in props
// Vue automatically picks the right way to assign it
h('div', { class: 'bar', innerHTML: 'hello' })

// class and style have the same object / array
// value support like in templates
h('div', { class: [foo, { bar }], style: { color: 'red' } })

// event listeners should be passed as onXxx
h('div', { onClick: () => {} })

// children can be a string
h('div', { id: 'foo' }, 'hello')

// props can be omitted when there are no props
h('div', 'hello')
h('div', [h('span', 'hello')])

// children array can contain mixed vnodes and strings
h('div', ['hello', h('span', 'hello')])
```

Creating components:
js```
import Foo from './Foo.vue'

// passing props
h(Foo, {
  // equivalent of some-prop="hello"
  someProp: 'hello',
  // equivalent of @update="() => {}"
  onUpdate: () => {}
})

// passing single default slot
h(Foo, () => 'default slot')

// passing named slots
// notice the `null` is required to avoid
// slots object being treated as props
h(MyComponent, null, {
  default: () => 'default slot',
  foo: () => h('div', 'foo'),
  bar: () => [h('span', 'one'), h('span', 'two')]
})
```

  * **See also** [Guide - Render Functions - Creating VNodes](https://vuejs.org/guide/extras/render-function#creating-vnodes)


## mergeProps() [​](https://vuejs.org/api/render-function.html#mergeprops)
Merge multiple props objects with special handling for certain props.
  * **Type**
ts```
function mergeProps(...args: object[]): object
```

  * **Details**
`mergeProps()` supports merging multiple props objects with special handling for the following props:
    * `class`
    * `style`
    * `onXxx` event listeners - multiple listeners with the same name will be merged into an array.
If you do not need the merge behavior and want simple overwrites, native object spread can be used instead.
  * **Example**
js```
import { mergeProps } from 'vue'

const one = {
  class: 'foo',
  onClick: handlerA
}

const two = {
  class: { bar: true },
  onClick: handlerB
}

const merged = mergeProps(one, two)
/**
 {
   class: 'foo bar',
   onClick: [handlerA, handlerB]
 }
 */
```



## cloneVNode() [​](https://vuejs.org/api/render-function.html#clonevnode)
Clones a vnode.
  * **Type**
ts```
function cloneVNode(vnode: VNode, extraProps?: object): VNode
```

  * **Details**
Returns a cloned vnode, optionally with extra props to merge with the original.
Vnodes should be considered immutable once created, and you should not mutate the props of an existing vnode. Instead, clone it with different / extra props.
Vnodes have special internal properties, so cloning them is not as simple as an object spread. `cloneVNode()` handles most of the internal logic.
  * **Example**
js```
import { h, cloneVNode } from 'vue'

const original = h('div')
const cloned = cloneVNode(original, { id: 'foo' })
```



## isVNode() [​](https://vuejs.org/api/render-function.html#isvnode)
Checks if a value is a vnode.
  * **Type**
ts```
function isVNode(value: unknown): boolean
```



## resolveComponent() [​](https://vuejs.org/api/render-function.html#resolvecomponent)
For manually resolving a registered component by name.
  * **Type**
ts```
function resolveComponent(name: string): Component | string
```

  * **Details**
**Note: you do not need this if you can import the component directly.**
`resolveComponent()` must be called inside either `setup()` or the render function in order to resolve from the correct component context.
If the component is not found, a runtime warning will be emitted, and the name string is returned.
  * **Example**
js```
import { h, resolveComponent } from 'vue'

export default {
  setup() {
    const ButtonCounter = resolveComponent('ButtonCounter')

    return () => {
      return h(ButtonCounter)
    }
  }
}
```

js```
import { h, resolveComponent } from 'vue'

export default {
  render() {
    const ButtonCounter = resolveComponent('ButtonCounter')
    return h(ButtonCounter)
  }
}
```

  * **See also** [Guide - Render Functions - Components](https://vuejs.org/guide/extras/render-function#components)


## resolveDirective() [​](https://vuejs.org/api/render-function.html#resolvedirective)
For manually resolving a registered directive by name.
  * **Type**
ts```
function resolveDirective(name: string): Directive | undefined
```

  * **Details**
**Note: you do not need this if you can import the directive directly.**
`resolveDirective()` must be called inside either `setup()` or the render function in order to resolve from the correct component context.
If the directive is not found, a runtime warning will be emitted, and the function returns `undefined`.
  * **See also** [Guide - Render Functions - Custom Directives](https://vuejs.org/guide/extras/render-function#custom-directives)


## withDirectives() [​](https://vuejs.org/api/render-function.html#withdirectives)
For adding custom directives to vnodes.
  * **Type**
ts```
function withDirectives(
  vnode: VNode,
  directives: DirectiveArguments
): VNode

// [Directive, value, argument, modifiers]
type DirectiveArguments = Array<
  | [Directive]
  | [Directive, any]
  | [Directive, any, string]
  | [Directive, any, string, DirectiveModifiers]
>
```

  * **Details**
Wraps an existing vnode with custom directives. The second argument is an array of custom directives. Each custom directive is also represented as an array in the form of `[Directive, value, argument, modifiers]`. Tailing elements of the array can be omitted if not needed.
  * **Example**
js```
import { h, withDirectives } from 'vue'

// a custom directive
const pin = {
  mounted() {
    /* ... */
  },
  updated() {
    /* ... */
  }
}

// <div v-pin:top.animate="200"></div>
const vnode = withDirectives(h('div'), [
  [pin, 200, 'top', { animate: true }]
])
```

  * **See also** [Guide - Render Functions - Custom Directives](https://vuejs.org/guide/extras/render-function#custom-directives)


## withModifiers() [​](https://vuejs.org/api/render-function.html#withmodifiers)
For adding built-in [`v-on` modifiers](https://vuejs.org/guide/essentials/event-handling#event-modifiers) to an event handler function.
  * **Type**
ts```
function withModifiers(fn: Function, modifiers: ModifierGuardsKeys[]): Function
```

  * **Example**
js```
import { h, withModifiers } from 'vue'

const vnode = h('button', {
  // equivalent of v-on:click.stop.prevent
  onClick: withModifiers(() => {
    // ...
  }, ['stop', 'prevent'])
})
```

  * **See also** [Guide - Render Functions - Event Modifiers](https://vuejs.org/guide/extras/render-function#event-modifiers)


[Custom Elements](https://vuejs.org/api/custom-elements)[Next Server-Side Rendering](https://vuejs.org/api/ssr)
Render Function APIs has loaded
