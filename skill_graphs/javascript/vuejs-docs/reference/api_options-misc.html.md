[Skip to content](https://vuejs.org/api/options-misc.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/api/options-misc)
[日本語 ](https://ja.vuejs.org/api/options-misc)
[Українська ](https://ua.vuejs.org/api/options-misc)
[Français ](https://fr.vuejs.org/api/options-misc)
[한국어 ](https://ko.vuejs.org/api/options-misc)
[Português ](https://pt.vuejs.org/api/options-misc)
[বাংলা ](https://bn.vuejs.org/api/options-misc)
[Italiano ](https://it.vuejs.org/api/options-misc)
[فارسی ](https://fa.vuejs.org/api/options-misc)
[Русский ](https://ru.vuejs.org/api/options-misc)
[Čeština ](https://cs.vuejs.org/api/options-misc)
[繁體中文 ](https://zh-hk.vuejs.org/api/options-misc)
[Polski ](https://pl.vuejs.org/api/options-misc)
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
  * [name](https://vuejs.org/api/options-misc.html#name)
  * [inheritAttrs](https://vuejs.org/api/options-misc.html#inheritattrs)
  * [components](https://vuejs.org/api/options-misc.html#components)
  * [directives](https://vuejs.org/api/options-misc.html#directives)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Options: Misc [​](https://vuejs.org/api/options-misc.html#options-misc)
## name [​](https://vuejs.org/api/options-misc.html#name)
Explicitly declare a display name for the component.
  * **Type**
ts```
interface ComponentOptions {
  name?: string
}
```

  * **Details**
The name of a component is used for the following:
    * Recursive self-reference in the component's own template
    * Display in Vue DevTools' component inspection tree
    * Display in warning component traces
When you use Single-File Components, the component already infers its own name from the filename. For example, a file named `MyComponent.vue` will have the inferred display name "MyComponent".
Another case is that when a component is registered globally with [`app.component`](https://vuejs.org/api/application#app-component), the global ID is automatically set as its name.
The `name` option allows you to override the inferred name, or to explicitly provide a name when no name can be inferred (e.g. when not using build tools, or an inlined non-SFC component).
There is one case where `name` is explicitly necessary: when matching against cacheable components in [`<KeepAlive>`](https://vuejs.org/guide/built-ins/keep-alive) via its `include / exclude` props.
TIP
Since version 3.2.34, a single-file component using `<script setup>` will automatically infer its `name` option based on the filename, removing the need to manually declare the name even when used with `<KeepAlive>`.


## inheritAttrs [​](https://vuejs.org/api/options-misc.html#inheritattrs)
Controls whether the default component attribute fallthrough behavior should be enabled.
  * **Type**
ts```
interface ComponentOptions {
  inheritAttrs?: boolean // default: true
}
```

  * **Details**
By default, parent scope attribute bindings that are not recognized as props will "fallthrough". This means that when we have a single-root component, these bindings will be applied to the root element of the child component as normal HTML attributes. When authoring a component that wraps a target element or another component, this may not always be the desired behavior. By setting `inheritAttrs` to `false`, this default behavior can be disabled. The attributes are available via the `$attrs` instance property and can be explicitly bound to a non-root element using `v-bind`.
  * **Example**
vue```
<script>
export default {
  inheritAttrs: false,
  props: ['label', 'value'],
  emits: ['input']
}
</script>

<template>
  <label>
    {{ label }}
    <input
      v-bind="$attrs"
      v-bind:value="value"
      v-on:input="$emit('input', $event.target.value)"
    />
  </label>
</template>
```

When declaring this option in a component that uses `<script setup>`, you can use the [`defineOptions`](https://vuejs.org/api/sfc-script-setup#defineoptions) macro:
vue```
<script setup>
defineProps(['label', 'value'])
defineEmits(['input'])
defineOptions({
  inheritAttrs: false
})
</script>

<template>
  <label>
    {{ label }}
    <input
      v-bind="$attrs"
      v-bind:value="value"
      v-on:input="$emit('input', $event.target.value)"
    />
  </label>
</template>
```

  * **See also**
    * [Fallthrough Attributes](https://vuejs.org/guide/components/attrs)
    * [Using `inheritAttrs` in normal `<script>`](https://vuejs.org/api/sfc-script-setup#usage-alongside-normal-script)


## components [​](https://vuejs.org/api/options-misc.html#components)
An object that registers components to be made available to the component instance.
  * **Type**
ts```
interface ComponentOptions {
  components?: { [key: string]: Component }
}
```

  * **Example**
js```
import Foo from './Foo.vue'
import Bar from './Bar.vue'

export default {
  components: {
    // shorthand
    Foo,
    // register under a different name
    RenamedBar: Bar
  }
}
```

  * **See also** [Component Registration](https://vuejs.org/guide/components/registration)


## directives [​](https://vuejs.org/api/options-misc.html#directives)
An object that registers directives to be made available to the component instance.
  * **Type**
ts```
interface ComponentOptions {
  directives?: { [key: string]: Directive }
}
```

  * **Example**
js```
export default {
  directives: {
    // enables v-focus in template
    focus: {
      mounted(el) {
        el.focus()
      }
    }
  }
}
```

template```
<input v-focus>
```

  * **See also** [Custom Directives](https://vuejs.org/guide/reusability/custom-directives)


[Options: Composition](https://vuejs.org/api/options-composition)[Next Component Instance](https://vuejs.org/api/component-instance)
Options: Misc has loaded
