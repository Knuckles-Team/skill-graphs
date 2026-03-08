[Skip to content](https://vuejs.org/api/sfc-spec.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/api/sfc-spec)
[日本語 ](https://ja.vuejs.org/api/sfc-spec)
[Українська ](https://ua.vuejs.org/api/sfc-spec)
[Français ](https://fr.vuejs.org/api/sfc-spec)
[한국어 ](https://ko.vuejs.org/api/sfc-spec)
[Português ](https://pt.vuejs.org/api/sfc-spec)
[বাংলা ](https://bn.vuejs.org/api/sfc-spec)
[Italiano ](https://it.vuejs.org/api/sfc-spec)
[فارسی ](https://fa.vuejs.org/api/sfc-spec)
[Русский ](https://ru.vuejs.org/api/sfc-spec)
[Čeština ](https://cs.vuejs.org/api/sfc-spec)
[繁體中文 ](https://zh-hk.vuejs.org/api/sfc-spec)
[Polski ](https://pl.vuejs.org/api/sfc-spec)
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
  * [Overview](https://vuejs.org/api/sfc-spec.html#overview)
  * [Language Blocks](https://vuejs.org/api/sfc-spec.html#language-blocks)
  * [Automatic Name Inference](https://vuejs.org/api/sfc-spec.html#automatic-name-inference)
  * [Pre-Processors](https://vuejs.org/api/sfc-spec.html#pre-processors)
  * [src Imports](https://vuejs.org/api/sfc-spec.html#src-imports)
  * [Comments](https://vuejs.org/api/sfc-spec.html#comments)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# SFC Syntax Specification [​](https://vuejs.org/api/sfc-spec.html#sfc-syntax-specification)
## Overview [​](https://vuejs.org/api/sfc-spec.html#overview)
A Vue Single-File Component (SFC), conventionally using the `*.vue` file extension, is a custom file format that uses an HTML-like syntax to describe a Vue component. A Vue SFC is syntactically compatible with HTML.
Each `*.vue` file consists of three types of top-level language blocks: `<template>`, `<script>`, and `<style>`, and optionally additional custom blocks:
vue```
<template>
  <div class="example">{{ msg }}</div>
</template>

<script>
export default {
  data() {
    return {
      msg: 'Hello world!'
    }
  }
}
</script>

<style>
.example {
  color: red;
}
</style>

<custom1>
  This could be e.g. documentation for the component.
</custom1>
```

## Language Blocks [​](https://vuejs.org/api/sfc-spec.html#language-blocks)
###  `<template>` [​](https://vuejs.org/api/sfc-spec.html#template)
  * Each `*.vue` file can contain at most one top-level `<template>` block.
  * Contents will be extracted and passed on to `@vue/compiler-dom`, pre-compiled into JavaScript render functions, and attached to the exported component as its `render` option.


###  `<script>` [​](https://vuejs.org/api/sfc-spec.html#script)
  * Each `*.vue` file can contain at most one `<script>` block (excluding [`<script setup>`](https://vuejs.org/api/sfc-script-setup)).
  * The script is executed as an ES Module.
  * The **default export** should be a Vue component options object, either as a plain object or as the return value of [defineComponent](https://vuejs.org/api/general#definecomponent).


###  `<script setup>` [​](https://vuejs.org/api/sfc-spec.html#script-setup)
  * Each `*.vue` file can contain at most one `<script setup>` block (excluding normal `<script>`).
  * The script is pre-processed and used as the component's `setup()` function, which means it will be executed **for each instance of the component**. Top-level bindings in `<script setup>` are automatically exposed to the template. For more details, see [dedicated documentation on `<script setup>`](https://vuejs.org/api/sfc-script-setup).


###  `<style>` [​](https://vuejs.org/api/sfc-spec.html#style)
  * A single `*.vue` file can contain multiple `<style>` tags.
  * A `<style>` tag can have `scoped` or `module` attributes (see [SFC Style Features](https://vuejs.org/api/sfc-css-features) for more details) to help encapsulate the styles to the current component. Multiple `<style>` tags with different encapsulation modes can be mixed in the same component.


### Custom Blocks [​](https://vuejs.org/api/sfc-spec.html#custom-blocks)
Additional custom blocks can be included in a `*.vue` file for any project-specific needs, for example a `<docs>` block. Some real-world examples of custom blocks include:
Handling of Custom Blocks will depend on tooling - if you want to build your own custom block integrations, see the [SFC custom block integrations tooling section](https://vuejs.org/guide/scaling-up/tooling#sfc-custom-block-integrations) for more details.
## Automatic Name Inference [​](https://vuejs.org/api/sfc-spec.html#automatic-name-inference)
An SFC automatically infers the component's name from its **filename** in the following cases:
  * Dev warning formatting
  * DevTools inspection
  * Recursive self-reference, e.g. a file named `FooBar.vue` can refer to itself as `<FooBar/>` in its template. This has lower priority than explicitly registered/imported components.


## Pre-Processors [​](https://vuejs.org/api/sfc-spec.html#pre-processors)
Blocks can declare pre-processor languages using the `lang` attribute. The most common case is using TypeScript for the `<script>` block:
template```
<script lang="ts">
  // use TypeScript
</script>
```

`lang` can be applied to any block - for example we can use `<style>` with `<template>` with
template```
<template lang="pug">
p {{ msg }}
</template>

<style lang="scss">
  $primary-color: #333;
  body {
    color: $primary-color;
  }
</style>
```

Note that integration with various pre-processors may differ by toolchain. Check out the respective documentation for examples:
  * [Vue CLI](https://cli.vuejs.org/guide/css.html#pre-processors)
  * [webpack + vue-loader](https://vue-loader.vuejs.org/guide/pre-processors.html#using-pre-processors)


##  `src` Imports [​](https://vuejs.org/api/sfc-spec.html#src-imports)
If you prefer splitting up your `*.vue` components into multiple files, you can use the `src` attribute to import an external file for a language block:
vue```
<template src="./template.html"></template>
<style src="./style.css"></style>
<script src="./script.js"></script>
```

Beware that `src` imports follow the same path resolution rules as webpack module requests, which means:
  * Relative paths need to start with `./`
  * You can import resources from npm dependencies:


vue```
<!-- import a file from the installed "todomvc-app-css" npm package -->
<style src="todomvc-app-css/index.css" />
```

`src` imports also work with custom blocks, e.g.:
vue```
<unit-test src="./unit-test.js">
</unit-test>
```

Note
While using aliases in `src`, don't start with `~`, anything after it is interpreted as a module request. This means you can reference assets inside node modules:
vue```
<img src="~some-npm-package/foo.png">
```

## Comments [​](https://vuejs.org/api/sfc-spec.html#comments)
Inside each block you shall use the comment syntax of the language being used (HTML, CSS, JavaScript, Pug, etc.). For top-level comments, use HTML comment syntax: `<!-- comment contents here -->`
[Special Attributes](https://vuejs.org/api/built-in-special-attributes)[Next <script setup>](https://vuejs.org/api/sfc-script-setup)
SFC Syntax Specification has loaded
