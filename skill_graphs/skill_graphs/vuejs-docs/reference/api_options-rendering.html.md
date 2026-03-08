[Skip to content](https://vuejs.org/api/options-rendering.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/api/options-rendering)
[日本語 ](https://ja.vuejs.org/api/options-rendering)
[Українська ](https://ua.vuejs.org/api/options-rendering)
[Français ](https://fr.vuejs.org/api/options-rendering)
[한국어 ](https://ko.vuejs.org/api/options-rendering)
[Português ](https://pt.vuejs.org/api/options-rendering)
[বাংলা ](https://bn.vuejs.org/api/options-rendering)
[Italiano ](https://it.vuejs.org/api/options-rendering)
[فارسی ](https://fa.vuejs.org/api/options-rendering)
[Русский ](https://ru.vuejs.org/api/options-rendering)
[Čeština ](https://cs.vuejs.org/api/options-rendering)
[繁體中文 ](https://zh-hk.vuejs.org/api/options-rendering)
[Polski ](https://pl.vuejs.org/api/options-rendering)
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
  * [template](https://vuejs.org/api/options-rendering.html#template)
  * [render](https://vuejs.org/api/options-rendering.html#render)
  * [compilerOptions](https://vuejs.org/api/options-rendering.html#compileroptions)
  * [slots](https://vuejs.org/api/options-rendering.html#slots)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Options: Rendering [​](https://vuejs.org/api/options-rendering.html#options-rendering)
## template [​](https://vuejs.org/api/options-rendering.html#template)
A string template for the component.
  * **Type**
ts```
interface ComponentOptions {
  template?: string
}
```

  * **Details**
A template provided via the `template` option will be compiled on-the-fly at runtime. It is only supported when using a build of Vue that includes the template compiler. The template compiler is **NOT** included in Vue builds that have the word `runtime` in their names, e.g. `vue.runtime.esm-bundler.js`. Consult the
If the string starts with `#` it will be used as a `querySelector` and use the selected element's `innerHTML` as the template string. This allows the source template to be authored using native `<template>` elements.
If the `render` option is also present in the same component, `template` will be ignored.
If the root component of your application doesn't have a `template` or `render` option specified, Vue will try to use the `innerHTML` of the mounted element as the template instead.
Security Note
Only use template sources that you can trust. Do not use user-provided content as your template. See [Security Guide](https://vuejs.org/guide/best-practices/security#rule-no-1-never-use-non-trusted-templates) for more details.


## render [​](https://vuejs.org/api/options-rendering.html#render)
A function that programmatically returns the virtual DOM tree of the component.
  * **Type**
ts```
interface ComponentOptions {
  render?(this: ComponentPublicInstance) => VNodeChild
}

type VNodeChild = VNodeChildAtom | VNodeArrayChildren

type VNodeChildAtom =
  | VNode
  | string
  | number
  | boolean
  | null
  | undefined
  | void

type VNodeArrayChildren = (VNodeArrayChildren | VNodeChildAtom)[]
```

  * **Details**
`render` is an alternative to string templates that allows you to leverage the full programmatic power of JavaScript to declare the render output of the component.
Pre-compiled templates, for example those in Single-File Components, are compiled into the `render` option at build time. If both `render` and `template` are present in a component, `render` will take higher priority.
  * **See also**
    * [Rendering Mechanism](https://vuejs.org/guide/extras/rendering-mechanism)
    * [Render Functions](https://vuejs.org/guide/extras/render-function)


## compilerOptions [​](https://vuejs.org/api/options-rendering.html#compileroptions)
Configure runtime compiler options for the component's template.
  * **Type**
ts```
interface ComponentOptions {
  compilerOptions?: {
    isCustomElement?: (tag: string) => boolean
    whitespace?: 'condense' | 'preserve' // default: 'condense'
    delimiters?: [string, string] // default: ['{{', '}}']
    comments?: boolean // default: false
  }
}
```

  * **Details**
This config option is only respected when using the full build (i.e. the standalone `vue.js` that can compile templates in the browser). It supports the same options as the app-level [app.config.compilerOptions](https://vuejs.org/api/application#app-config-compileroptions), and has higher priority for the current component.
  * **See also** [app.config.compilerOptions](https://vuejs.org/api/application#app-config-compileroptions)


## slots[​](https://vuejs.org/api/options-rendering.html#slots)
  * Only supported in 3.3+


An option to assist with type inference when using slots programmatically in render functions.
  * **Details**
This option's runtime value is not used. The actual types should be declared via type casting using the `SlotsType` type helper:
ts```
import { SlotsType } from 'vue'

defineComponent({
  slots: Object as SlotsType<{
    default: { foo: string; bar: number }
    item: { data: number }
  }>,
  setup(props, { slots }) {
    expectType<
      undefined | ((scope: { foo: string; bar: number }) => any)
    >(slots.default)
    expectType<undefined | ((scope: { data: number }) => any)>(
      slots.item
    )
  }
})
```



[Options: State](https://vuejs.org/api/options-state)[Next Options: Lifecycle](https://vuejs.org/api/options-lifecycle)
Options: Rendering has loaded
