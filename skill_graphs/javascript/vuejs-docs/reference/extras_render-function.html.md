[Skip to content](https://vuejs.org/guide/extras/render-function.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/guide/extras/render-function)
[日本語 ](https://ja.vuejs.org/guide/extras/render-function)
[Українська ](https://ua.vuejs.org/guide/extras/render-function)
[Français ](https://fr.vuejs.org/guide/extras/render-function)
[한국어 ](https://ko.vuejs.org/guide/extras/render-function)
[Português ](https://pt.vuejs.org/guide/extras/render-function)
[বাংলা ](https://bn.vuejs.org/guide/extras/render-function)
[Italiano ](https://it.vuejs.org/guide/extras/render-function)
[فارسی ](https://fa.vuejs.org/guide/extras/render-function)
[Русский ](https://ru.vuejs.org/guide/extras/render-function)
[Čeština ](https://cs.vuejs.org/guide/extras/render-function)
[繁體中文 ](https://zh-hk.vuejs.org/guide/extras/render-function)
[Polski ](https://pl.vuejs.org/guide/extras/render-function)
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
  * [Basic Usage](https://vuejs.org/guide/extras/render-function.html#basic-usage)
    * [Creating Vnodes](https://vuejs.org/guide/extras/render-function.html#creating-vnodes)
    * [Declaring Render Functions](https://vuejs.org/guide/extras/render-function.html#declaring-render-functions)
    * [Vnodes Must Be Unique](https://vuejs.org/guide/extras/render-function.html#vnodes-must-be-unique)
    * [Using Vnodes in <template>](https://vuejs.org/guide/extras/render-function.html#using-vnodes-in-template)
  * [JSX / TSX](https://vuejs.org/guide/extras/render-function.html#jsx-tsx)
    * [JSX Type Inference](https://vuejs.org/guide/extras/render-function.html#jsx-type-inference)
  * [Render Function Recipes](https://vuejs.org/guide/extras/render-function.html#render-function-recipes)
    * [v-if](https://vuejs.org/guide/extras/render-function.html#v-if)
    * [v-for](https://vuejs.org/guide/extras/render-function.html#v-for)
    * [v-on](https://vuejs.org/guide/extras/render-function.html#v-on)
    * [Components](https://vuejs.org/guide/extras/render-function.html#components)
    * [Rendering Slots](https://vuejs.org/guide/extras/render-function.html#rendering-slots)
    * [Passing Slots](https://vuejs.org/guide/extras/render-function.html#passing-slots)
    * [Scoped Slots](https://vuejs.org/guide/extras/render-function.html#scoped-slots)
    * [Built-in Components](https://vuejs.org/guide/extras/render-function.html#built-in-components)
    * [v-model](https://vuejs.org/guide/extras/render-function.html#v-model)
    * [Custom Directives](https://vuejs.org/guide/extras/render-function.html#custom-directives)
    * [Template Refs](https://vuejs.org/guide/extras/render-function.html#template-refs)
  * [Functional Components](https://vuejs.org/guide/extras/render-function.html#functional-components)
    * [Typing Functional Components](https://vuejs.org/guide/extras/render-function.html#typing-functional-components)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Render Functions & JSX [​](https://vuejs.org/guide/extras/render-function.html#render-functions-jsx)
Vue recommends using templates to build applications in the vast majority of cases. However, there are situations where we need the full programmatic power of JavaScript. That's where we can use the **render function**.
> If you are new to the concept of virtual DOM and render functions, make sure to read the [Rendering Mechanism](https://vuejs.org/guide/extras/rendering-mechanism) chapter first.
## Basic Usage [​](https://vuejs.org/guide/extras/render-function.html#basic-usage)
### Creating Vnodes [​](https://vuejs.org/guide/extras/render-function.html#creating-vnodes)
Vue provides an `h()` function for creating vnodes:
js```
import { h } from 'vue'

const vnode = h(
  'div', // type
  { id: 'foo', class: 'bar' }, // props
  [
    /* children */
  ]
)
```

`h()` is short for **hyperscript** - which means "JavaScript that produces HTML (hypertext markup language)". This name is inherited from conventions shared by many virtual DOM implementations. A more descriptive name could be `createVNode()`, but a shorter name helps when you have to call this function many times in a render function.
The `h()` function is designed to be very flexible:
js```
// all arguments except the type are optional
h('div')
h('div', { id: 'foo' })

// both attributes and properties can be used in props
// Vue automatically picks the right way to assign it
h('div', { class: 'bar', innerHTML: 'hello' })

// props modifiers such as `.prop` and `.attr` can be added
// with `.` and `^` prefixes respectively
h('div', { '.name': 'some-name', '^width': '100' })

// class and style have the same object / array
// value support that they have in templates
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

The resulting vnode has the following shape:
js```
const vnode = h('div', { id: 'foo' }, [])

vnode.type // 'div'
vnode.props // { id: 'foo' }
vnode.children // []
vnode.key // null
```

Note
The full `VNode` interface contains many other internal properties, but it is strongly recommended to avoid relying on any properties other than the ones listed here. This avoids unintended breakage in case the internal properties are changed.
### Declaring Render Functions [​](https://vuejs.org/guide/extras/render-function.html#declaring-render-functions)
When using templates with Composition API, the return value of the `setup()` hook is used to expose data to the template. When using render functions, however, we can directly return the render function instead:
js```
import { ref, h } from 'vue'

export default {
  props: {
    /* ... */
  },
  setup(props) {
    const count = ref(1)

    // return the render function
    return () => h('div', props.msg + count.value)
  }
}
```

The render function is declared inside `setup()` so it naturally has access to the props and any reactive state declared in the same scope.
In addition to returning a single vnode, you can also return strings or arrays:
js```
export default {
  setup() {
    return () => 'hello world!'
  }
}
```

js```
import { h } from 'vue'

export default {
  setup() {
    // use an array to return multiple root nodes
    return () => [
      h('div'),
      h('div'),
      h('div')
    ]
  }
}
```

TIP
Make sure to return a function instead of directly returning values! The `setup()` function is called only once per component, while the returned render function will be called multiple times.
We can declare render functions using the `render` option:
js```
import { h } from 'vue'

export default {
  data() {
    return {
      msg: 'hello'
    }
  },
  render() {
    return h('div', this.msg)
  }
}
```

The `render()` function has access to the component instance via `this`.
In addition to returning a single vnode, you can also return strings or arrays:
js```
export default {
  render() {
    return 'hello world!'
  }
}
```

js```
import { h } from 'vue'

export default {
  render() {
    // use an array to return multiple root nodes
    return [
      h('div'),
      h('div'),
      h('div')
    ]
  }
}
```

If a render function component doesn't need any instance state, they can also be declared directly as a function for brevity:
js```
function Hello() {
  return 'hello world!'
}
```

That's right, this is a valid Vue component! See [Functional Components](https://vuejs.org/guide/extras/render-function.html#functional-components) for more details on this syntax.
### Vnodes Must Be Unique [​](https://vuejs.org/guide/extras/render-function.html#vnodes-must-be-unique)
All vnodes in the component tree must be unique. That means the following render function is invalid:
js```
function render() {
  const p = h('p', 'hi')
  return h('div', [
    // Yikes - duplicate vnodes!
    p,
    p
  ])
}
```

If you really want to duplicate the same element/component many times, you can do so with a factory function. For example, the following render function is a perfectly valid way of rendering 20 identical paragraphs:
js```
function render() {
  return h(
    'div',
    Array.from({ length: 20 }).map(() => {
      return h('p', 'hi')
    })
  )
}
```

### Using Vnodes in `<template>` [​](https://vuejs.org/guide/extras/render-function.html#using-vnodes-in-template)
vue```
<script setup>
import { h } from 'vue'

const vnode = h('button', ['Hello'])
</script>

<template>
  <!-- Via <component /> -->
  <component :is="vnode">Hi</component>

  <!-- Or directly as element -->
  <vnode />
  <vnode>Hi</vnode>
</template>
```

A vnode object has been declared in `setup()`, you can use it like a normal component for rendering.
WARNING
A vnode represents an already created render output, not a component definition. Using a vnode in `<template>` does not create a new component instance, and the vnode will be rendered as-is.
This pattern should be used with care and is not a replacement for normal components.
## JSX / TSX [​](https://vuejs.org/guide/extras/render-function.html#jsx-tsx)
jsx```
const vnode = <div>hello</div>
```

Inside JSX expressions, use curly braces to embed dynamic values:
jsx```
const vnode = <div id={dynamicId}>hello, {userName}</div>
```

`create-vue` and Vue CLI both have options for scaffolding projects with pre-configured JSX support. If you are configuring JSX manually, please refer to the documentation of
Although first introduced by React, JSX actually has no defined runtime semantics and can be compiled into various different outputs. If you have worked with JSX before, do note that **Vue JSX transform is different from React's JSX transform** , so you can't use React's JSX transform in Vue applications. Some notable differences from React JSX include:
  * You can use HTML attributes such as `class` and `for` as props - no need to use `className` or `htmlFor`.
  * Passing children to components (i.e. slots) [works differently](https://vuejs.org/guide/extras/render-function.html#passing-slots).


Vue's type definition also provides type inference for TSX usage. When using TSX, make sure to specify `"jsx": "preserve"` in `tsconfig.json` so that TypeScript leaves the JSX syntax intact for Vue JSX transform to process.
### JSX Type Inference [​](https://vuejs.org/guide/extras/render-function.html#jsx-type-inference)
Similar to the transform, Vue's JSX also needs different type definitions.
Starting in Vue 3.4, Vue no longer implicitly registers the global `JSX` namespace. To instruct TypeScript to use Vue's JSX type definitions, make sure to include the following in your `tsconfig.json`:
json```
{
  "compilerOptions": {
    "jsx": "preserve",
    "jsxImportSource": "vue"
    // ...
  }
}
```

You can also opt-in per file by adding a `/* @jsxImportSource vue */` comment at the top of the file.
If there is code that depends on the presence of the global `JSX` namespace, you can retain the exact pre-3.4 global behavior by explicitly importing or referencing `vue/jsx` in your project, which registers the global `JSX` namespace.
## Render Function Recipes [​](https://vuejs.org/guide/extras/render-function.html#render-function-recipes)
Below we will provide some common recipes for implementing template features as their equivalent render functions / JSX.
###  `v-if` [​](https://vuejs.org/guide/extras/render-function.html#v-if)
Template:
template```
<div>
  <div v-if="ok">yes</div>
  <span v-else>no</span>
</div>
```

Equivalent render function / JSX:
js```
h('div', [ok.value ? h('div', 'yes') : h('span', 'no')])
```

jsx```
<div>{ok.value ? <div>yes</div> : <span>no</span>}</div>
```

js```
h('div', [this.ok ? h('div', 'yes') : h('span', 'no')])
```

jsx```
<div>{this.ok ? <div>yes</div> : <span>no</span>}</div>
```

###  `v-for` [​](https://vuejs.org/guide/extras/render-function.html#v-for)
Template:
template```
<ul>
  <li v-for="{ id, text } in items" :key="id">
    {{ text }}
  </li>
</ul>
```

Equivalent render function / JSX:
js```
h(
  'ul',
  // assuming `items` is a ref with array value
  items.value.map(({ id, text }) => {
    return h('li', { key: id }, text)
  })
)
```

jsx```
<ul>
  {items.value.map(({ id, text }) => {
    return <li key={id}>{text}</li>
  })}
</ul>
```

js```
h(
  'ul',
  this.items.map(({ id, text }) => {
    return h('li', { key: id }, text)
  })
)
```

jsx```
<ul>
  {this.items.map(({ id, text }) => {
    return <li key={id}>{text}</li>
  })}
</ul>
```

###  `v-on` [​](https://vuejs.org/guide/extras/render-function.html#v-on)
Props with names that start with `on` followed by an uppercase letter are treated as event listeners. For example, `onClick` is the equivalent of `@click` in templates.
js```
h(
  'button',
  {
    onClick(event) {
      /* ... */
    }
  },
  'Click Me'
)
```

jsx```
<button
  onClick={(event) => {
    /* ... */
  }}
>
  Click Me
</button>
```

#### Event Modifiers [​](https://vuejs.org/guide/extras/render-function.html#event-modifiers)
For the `.passive`, `.capture`, and `.once` event modifiers, they can be concatenated after the event name using camelCase.
For example:
js```
h('input', {
  onClickCapture() {
    /* listener in capture mode */
  },
  onKeyupOnce() {
    /* triggers only once */
  },
  onMouseoverOnceCapture() {
    /* once + capture */
  }
})
```

jsx```
<input
  onClickCapture={() => {}}
  onKeyupOnce={() => {}}
  onMouseoverOnceCapture={() => {}}
/>
```

For other event and key modifiers, the [`withModifiers`](https://vuejs.org/api/render-function#withmodifiers) helper can be used:
js```
import { withModifiers } from 'vue'

h('div', {
  onClick: withModifiers(() => {}, ['self'])
})
```

jsx```
<div onClick={withModifiers(() => {}, ['self'])} />
```

### Components [​](https://vuejs.org/guide/extras/render-function.html#components)
To create a vnode for a component, the first argument passed to `h()` should be the component definition. This means when using render functions, it is unnecessary to register components - you can just use the imported components directly:
js```
import Foo from './Foo.vue'
import Bar from './Bar.jsx'

function render() {
  return h('div', [h(Foo), h(Bar)])
}
```

jsx```
function render() {
  return (
    <div>
      <Foo />
      <Bar />
    </div>
  )
}
```

As we can see, `h` can work with components imported from any file format as long as it's a valid Vue component.
Dynamic components are straightforward with render functions:
js```
import Foo from './Foo.vue'
import Bar from './Bar.jsx'

function render() {
  return ok.value ? h(Foo) : h(Bar)
}
```

jsx```
function render() {
  return ok.value ? <Foo /> : <Bar />
}
```

If a component is registered by name and cannot be imported directly (for example, globally registered by a library), it can be programmatically resolved by using the [`resolveComponent()`](https://vuejs.org/api/render-function#resolvecomponent) helper.
### Rendering Slots [​](https://vuejs.org/guide/extras/render-function.html#rendering-slots)
In render functions, slots can be accessed from the `setup()` context. Each slot on the `slots` object is a **function that returns an array of vnodes** :
js```
export default {
  props: ['message'],
  setup(props, { slots }) {
    return () => [
      // default slot:
      // <div><slot /></div>
      h('div', slots.default()),

      // named slot:
      // <div><slot name="footer" :text="message" /></div>
      h(
        'div',
        slots.footer({
          text: props.message
        })
      )
    ]
  }
}
```

JSX equivalent:
jsx```
// default
<div>{slots.default()}</div>

// named
<div>{slots.footer({ text: props.message })}</div>
```

In render functions, slots can be accessed from [`this.$slots`](https://vuejs.org/api/component-instance#slots):
js```
export default {
  props: ['message'],
  render() {
    return [
      // <div><slot /></div>
      h('div', this.$slots.default()),

      // <div><slot name="footer" :text="message" /></div>
      h(
        'div',
        this.$slots.footer({
          text: this.message
        })
      )
    ]
  }
}
```

JSX equivalent:
jsx```
// <div><slot /></div>
<div>{this.$slots.default()}</div>

// <div><slot name="footer" :text="message" /></div>
<div>{this.$slots.footer({ text: this.message })}</div>
```

### Passing Slots [​](https://vuejs.org/guide/extras/render-function.html#passing-slots)
Passing children to components works a bit differently from passing children to elements. Instead of an array, we need to pass either a slot function, or an object of slot functions. Slot functions can return anything a normal render function can return - which will always be normalized to arrays of vnodes when accessed in the child component.
js```
// single default slot
h(MyComponent, () => 'hello')

// named slots
// notice the `null` is required to avoid
// the slots object being treated as props
h(MyComponent, null, {
  default: () => 'default slot',
  foo: () => h('div', 'foo'),
  bar: () => [h('span', 'one'), h('span', 'two')]
})
```

JSX equivalent:
jsx```
// default
<MyComponent>{() => 'hello'}</MyComponent>

// named
<MyComponent>{{
  default: () => 'default slot',
  foo: () => <div>foo</div>,
  bar: () => [<span>one</span>, <span>two</span>]
}}</MyComponent>
```

Passing slots as functions allows them to be invoked lazily by the child component. This leads to the slot's dependencies being tracked by the child instead of the parent, which results in more accurate and efficient updates.
### Scoped Slots [​](https://vuejs.org/guide/extras/render-function.html#scoped-slots)
To render a scoped slot in the parent component, a slot is passed to the child. Notice how the slot now has a parameter `text`. The slot will be called in the child component and the data from the child component will be passed up to the parent component.
js```
// parent component
export default {
  setup() {
    return () => h(MyComp, null, {
      default: ({ text }) => h('p', text)
    })
  }
}
```

Remember to pass `null` so the slots will not be treated as props.
js```
// child component
export default {
  setup(props, { slots }) {
    const text = ref('hi')
    return () => h('div', null, slots.default({ text: text.value }))
  }
}
```

JSX equivalent:
jsx```
<MyComponent>{{
  default: ({ text }) => <p>{ text }</p>
}}</MyComponent>
```

### Built-in Components [​](https://vuejs.org/guide/extras/render-function.html#built-in-components)
[Built-in components](https://vuejs.org/api/built-in-components) such as `<KeepAlive>`, `<Transition>`, `<TransitionGroup>`, `<Teleport>` and `<Suspense>` must be imported for use in render functions:
js```
import { h, KeepAlive, Teleport, Transition, TransitionGroup } from 'vue'

export default {
  setup () {
    return () => h(Transition, { mode: 'out-in' }, /* ... */)
  }
}
```

js```
import { h, KeepAlive, Teleport, Transition, TransitionGroup } from 'vue'

export default {
  render () {
    return h(Transition, { mode: 'out-in' }, /* ... */)
  }
}
```

###  `v-model` [​](https://vuejs.org/guide/extras/render-function.html#v-model)
The `v-model` directive is expanded to `modelValue` and `onUpdate:modelValue` props during template compilation—we will have to provide these props ourselves:
js```
export default {
  props: ['modelValue'],
  emits: ['update:modelValue'],
  setup(props, { emit }) {
    return () =>
      h(SomeComponent, {
        modelValue: props.modelValue,
        'onUpdate:modelValue': (value) => emit('update:modelValue', value)
      })
  }
}
```

js```
export default {
  props: ['modelValue'],
  emits: ['update:modelValue'],
  render() {
    return h(SomeComponent, {
      modelValue: this.modelValue,
      'onUpdate:modelValue': (value) => this.$emit('update:modelValue', value)
    })
  }
}
```

### Custom Directives [​](https://vuejs.org/guide/extras/render-function.html#custom-directives)
Custom directives can be applied to a vnode using [`withDirectives`](https://vuejs.org/api/render-function#withdirectives):
js```
import { h, withDirectives } from 'vue'

// a custom directive
const pin = {
  mounted() { /* ... */ },
  updated() { /* ... */ }
}

// <div v-pin:top.animate="200"></div>
const vnode = withDirectives(h('div'), [
  [pin, 200, 'top', { animate: true }]
])
```

If the directive is registered by name and cannot be imported directly, it can be resolved using the [`resolveDirective`](https://vuejs.org/api/render-function#resolvedirective) helper.
### Template Refs [​](https://vuejs.org/guide/extras/render-function.html#template-refs)
With the Composition API, when using [`useTemplateRef()`](https://vuejs.org/api/composition-api-helpers#usetemplateref)
js```
import { h, useTemplateRef } from 'vue'

export default {
  setup() {
    const divEl = useTemplateRef('my-div')

    // <div ref="my-div">
    return () => h('div', { ref: 'my-div' })
  }
}
```

Usage before 3.5
In versions before 3.5 where useTemplateRef() was not introduced, template refs are created by passing the ref() itself as a prop to the vnode:
js```
import { h, ref } from 'vue'

export default {
  setup() {
    const divEl = ref()

    // <div ref="divEl">
    return () => h('div', { ref: divEl })
  }
}
```

With the Options API, template refs are created by passing the ref name as a string in the vnode props:
js```
export default {
  render() {
    // <div ref="divEl">
    return h('div', { ref: 'divEl' })
  }
}
```

## Functional Components [​](https://vuejs.org/guide/extras/render-function.html#functional-components)
Functional components are an alternative form of component that don't have any state of their own. They act like pure functions: props in, vnodes out. They are rendered without creating a component instance (i.e. no `this`), and without the usual component lifecycle hooks.
To create a functional component we use a plain function, rather than an options object. The function is effectively the `render` function for the component.
The signature of a functional component is the same as the `setup()` hook:
js```
function MyComponent(props, { slots, emit, attrs }) {
  // ...
}
```

As there is no `this` reference for a functional component, Vue will pass in the `props` as the first argument:
js```
function MyComponent(props, context) {
  // ...
}
```

The second argument, `context`, contains three properties: `attrs`, `emit`, and `slots`. These are equivalent to the instance properties [`$attrs`](https://vuejs.org/api/component-instance#attrs), [`$emit`](https://vuejs.org/api/component-instance#emit), and [`$slots`](https://vuejs.org/api/component-instance#slots) respectively.
Most of the usual configuration options for components are not available for functional components. However, it is possible to define [`props`](https://vuejs.org/api/options-state#props) and [`emits`](https://vuejs.org/api/options-state#emits) by adding them as properties:
js```
MyComponent.props = ['value']
MyComponent.emits = ['click']
```

If the `props` option is not specified, then the `props` object passed to the function will contain all attributes, the same as `attrs`. The prop names will not be normalized to camelCase unless the `props` option is specified.
For functional components with explicit `props`, [attribute fallthrough](https://vuejs.org/guide/components/attrs) works much the same as with normal components. However, for functional components that don't explicitly specify their `props`, only the `class`, `style`, and `onXxx` event listeners will be inherited from the `attrs` by default. In either case, `inheritAttrs` can be set to `false` to disable attribute inheritance:
js```
MyComponent.inheritAttrs = false
```

Functional components can be registered and consumed just like normal components. If you pass a function as the first argument to `h()`, it will be treated as a functional component.
### Typing Functional Components[​](https://vuejs.org/guide/extras/render-function.html#typing-functional-components)
Functional Components can be typed based on whether they are named or anonymous.
**Named Functional Component**
tsx```
import type { SetupContext } from 'vue'
type FComponentProps = {
  message: string
}

type Events = {
  sendMessage(message: string): void
}

function FComponent(
  props: FComponentProps,
  context: SetupContext<Events>
) {
  return (
    <button onClick={() => context.emit('sendMessage', props.message)}>
        {props.message} {' '}
    </button>
  )
}

FComponent.props = {
  message: {
    type: String,
    required: true
  }
}

FComponent.emits = {
  sendMessage: (value: unknown) => typeof value === 'string'
}
```

**Anonymous Functional Component**
tsx```
import type { FunctionalComponent } from 'vue'

type FComponentProps = {
  message: string
}

type Events = {
  sendMessage(message: string): void
}

const FComponent: FunctionalComponent<FComponentProps, Events> = (
  props,
  context
) => {
  return (
    <button onClick={() => context.emit('sendMessage', props.message)}>
        {props.message} {' '}
    </button>
  )
}

FComponent.props = {
  message: {
    type: String,
    required: true
  }
}

FComponent.emits = {
  sendMessage: (value) => typeof value === 'string'
}
```

[Rendering Mechanism](https://vuejs.org/guide/extras/rendering-mechanism)[Next Vue and Web Components](https://vuejs.org/guide/extras/web-components)
Render Functions & JSX has loaded
