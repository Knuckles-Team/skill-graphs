[Skip to content](https://vuejs.org/api/sfc-css-features.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/api/sfc-css-features)
[日本語 ](https://ja.vuejs.org/api/sfc-css-features)
[Українська ](https://ua.vuejs.org/api/sfc-css-features)
[Français ](https://fr.vuejs.org/api/sfc-css-features)
[한국어 ](https://ko.vuejs.org/api/sfc-css-features)
[Português ](https://pt.vuejs.org/api/sfc-css-features)
[বাংলা ](https://bn.vuejs.org/api/sfc-css-features)
[Italiano ](https://it.vuejs.org/api/sfc-css-features)
[فارسی ](https://fa.vuejs.org/api/sfc-css-features)
[Русский ](https://ru.vuejs.org/api/sfc-css-features)
[Čeština ](https://cs.vuejs.org/api/sfc-css-features)
[繁體中文 ](https://zh-hk.vuejs.org/api/sfc-css-features)
[Polski ](https://pl.vuejs.org/api/sfc-css-features)
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
  * [Scoped CSS](https://vuejs.org/api/sfc-css-features.html#scoped-css)
  * [CSS Modules](https://vuejs.org/api/sfc-css-features.html#css-modules)
  * [v-bind() in CSS](https://vuejs.org/api/sfc-css-features.html#v-bind-in-css)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# SFC CSS Features [​](https://vuejs.org/api/sfc-css-features.html#sfc-css-features)
## Scoped CSS [​](https://vuejs.org/api/sfc-css-features.html#scoped-css)
When a `<style>` tag has the `scoped` attribute, its CSS will apply to elements of the current component only. This is similar to the style encapsulation found in Shadow DOM. It comes with some caveats, but doesn't require any polyfills. It is achieved by using PostCSS to transform the following:
vue```
<style scoped>
.example {
  color: red;
}
</style>

<template>
  <div class="example">hi</div>
</template>
```

Into the following:
vue```
<style>
.example[data-v-f3f3eg9] {
  color: red;
}
</style>

<template>
  <div class="example" data-v-f3f3eg9>hi</div>
</template>
```

### Child Component Root Elements [​](https://vuejs.org/api/sfc-css-features.html#child-component-root-elements)
With `scoped`, the parent component's styles will not leak into child components. However, a child component's root node will be affected by both the parent's scoped CSS and the child's scoped CSS. This is by design so that the parent can style the child root element for layout purposes.
### Deep Selectors [​](https://vuejs.org/api/sfc-css-features.html#deep-selectors)
If you want a selector in `scoped` styles to be "deep", i.e. affecting child components, you can use the `:deep()` pseudo-class:
vue```
<style scoped>
.a :deep(.b) {
  /* ... */
}
</style>
```

The above will be compiled into:
css```
.a[data-v-f3f3eg9] .b {
  /* ... */
}
```

TIP
DOM content created with `v-html` are not affected by scoped styles, but you can still style them using deep selectors.
### Slotted Selectors [​](https://vuejs.org/api/sfc-css-features.html#slotted-selectors)
By default, scoped styles do not affect contents rendered by `<slot/>`, as they are considered to be owned by the parent component passing them in. To explicitly target slot content, use the `:slotted` pseudo-class:
vue```
<style scoped>
:slotted(div) {
  color: red;
}
</style>
```

### Global Selectors [​](https://vuejs.org/api/sfc-css-features.html#global-selectors)
If you want just one rule to apply globally, you can use the `:global` pseudo-class rather than creating another `<style>` (see below):
vue```
<style scoped>
:global(.red) {
  color: red;
}
</style>
```

### Mixing Local and Global Styles [​](https://vuejs.org/api/sfc-css-features.html#mixing-local-and-global-styles)
You can also include both scoped and non-scoped styles in the same component:
vue```
<style>
/* global styles */
</style>

<style scoped>
/* local styles */
</style>
```

### Scoped Style Tips [​](https://vuejs.org/api/sfc-css-features.html#scoped-style-tips)
  * **Scoped styles do not eliminate the need for classes**. Due to the way browsers render various CSS selectors, `p { color: red }` will be many times slower when scoped (i.e. when combined with an attribute selector). If you use classes or ids instead, such as in `.example { color: red }`, then you virtually eliminate that performance hit.
  * **Be careful with descendant selectors in recursive components!** For a CSS rule with the selector `.a .b`, if the element that matches `.a` contains a recursive child component, then all `.b` in that child component will be matched by the rule.


## CSS Modules [​](https://vuejs.org/api/sfc-css-features.html#css-modules)
A `<style module>` tag is compiled as `$style`:
vue```
<template>
  <p :class="$style.red">This should be red</p>
</template>

<style module>
.red {
  color: red;
}
</style>
```

The resulting classes are hashed to avoid collision, achieving the same effect of scoping the CSS to the current component only.
Refer to the
### Custom Inject Name [​](https://vuejs.org/api/sfc-css-features.html#custom-inject-name)
You can customize the property key of the injected classes object by giving the `module` attribute a value:
vue```
<template>
  <p :class="classes.red">red</p>
</template>

<style module="classes">
.red {
  color: red;
}
</style>
```

### Usage with Composition API [​](https://vuejs.org/api/sfc-css-features.html#usage-with-composition-api)
The injected classes can be accessed in `setup()` and `<script setup>` via the `useCssModule` API. For `<style module>` blocks with custom injection names, `useCssModule` accepts the matching `module` attribute value as the first argument:
js```
import { useCssModule } from 'vue'

// inside setup() scope...
// default, returns classes for <style module>
useCssModule()

// named, returns classes for <style module="classes">
useCssModule('classes')
```

  * **Example**


vue```
<script setup lang="ts">
import { useCssModule } from 'vue'

const classes = useCssModule()
</script>

<template>
  <p :class="classes.red">red</p>
</template>

<style module>
.red {
  color: red;
}
</style>
```

##  `v-bind()` in CSS [​](https://vuejs.org/api/sfc-css-features.html#v-bind-in-css)
SFC `<style>` tags support linking CSS values to dynamic component state using the `v-bind` CSS function:
vue```
<template>
  <div class="text">hello</div>
</template>

<script>
export default {
  data() {
    return {
      color: 'red'
    }
  }
}
</script>

<style>
.text {
  color: v-bind(color);
}
</style>
```

The syntax works with [`<script setup>`](https://vuejs.org/api/sfc-script-setup), and supports JavaScript expressions (must be wrapped in quotes):
vue```
<script setup>
import { ref } from 'vue'
const theme = ref({
    color: 'red',
})
</script>

<template>
  <p>hello</p>
</template>

<style scoped>
p {
  color: v-bind('theme.color');
}
</style>
```

The actual value will be compiled into a hashed CSS custom property, so the CSS is still static. The custom property will be applied to the component's root element via inline styles and reactively updated if the source value changes.
[<script setup>](https://vuejs.org/api/sfc-script-setup)[Next Custom Elements](https://vuejs.org/api/custom-elements)
SFC CSS Features has loaded
