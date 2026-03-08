[Skip to content](https://vuejs.org/style-guide/rules-recommended.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/style-guide/rules-recommended)
[日本語 ](https://ja.vuejs.org/style-guide/rules-recommended)
[Українська ](https://ua.vuejs.org/style-guide/rules-recommended)
[Français ](https://fr.vuejs.org/style-guide/rules-recommended)
[한국어 ](https://ko.vuejs.org/style-guide/rules-recommended)
[Português ](https://pt.vuejs.org/style-guide/rules-recommended)
[বাংলা ](https://bn.vuejs.org/style-guide/rules-recommended)
[Italiano ](https://it.vuejs.org/style-guide/rules-recommended)
[فارسی ](https://fa.vuejs.org/style-guide/rules-recommended)
[Русский ](https://ru.vuejs.org/style-guide/rules-recommended)
[Čeština ](https://cs.vuejs.org/style-guide/rules-recommended)
[繁體中文 ](https://zh-hk.vuejs.org/style-guide/rules-recommended)
[Polski ](https://pl.vuejs.org/style-guide/rules-recommended)
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
## Style Guide
[Overview](https://vuejs.org/style-guide/)[A - Essential](https://vuejs.org/style-guide/rules-essential)[B - Strongly Recommended](https://vuejs.org/style-guide/rules-strongly-recommended)[C - Recommended](https://vuejs.org/style-guide/rules-recommended)[D - Use with Caution](https://vuejs.org/style-guide/rules-use-with-caution)
On this page
Table of Contents for current page
  * [Component/instance options order](https://vuejs.org/style-guide/rules-recommended.html#component-instance-options-order)
  * [Element attribute order](https://vuejs.org/style-guide/rules-recommended.html#element-attribute-order)
  * [Empty lines in component/instance options](https://vuejs.org/style-guide/rules-recommended.html#empty-lines-in-component-instance-options)
  * [Single-file component top-level element order](https://vuejs.org/style-guide/rules-recommended.html#single-file-component-top-level-element-order)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Priority C Rules: Recommended [​](https://vuejs.org/style-guide/rules-recommended.html#priority-c-rules-recommended)
Note
This Vue.js Style Guide is outdated and needs to be reviewed. If you have any questions or suggestions, please
Where multiple, equally good options exist, an arbitrary choice can be made to ensure consistency. In these rules, we describe each acceptable option and suggest a default choice. That means you can feel free to make a different choice in your own codebase, as long as you're consistent and have a good reason. Please do have a good reason though! By adapting to the community standard, you will:
  1. Train your brain to more easily parse most of the community code you encounter
  2. Be able to copy and paste most community code examples without modification
  3. Often find new hires are already accustomed to your preferred coding style, at least in regards to Vue


## Component/instance options order [​](https://vuejs.org/style-guide/rules-recommended.html#component-instance-options-order)
**Component/instance options should be ordered consistently.**
This is the default order we recommend for component options. They're split into categories, so you'll know where to add new properties from plugins.
  1. **Global Awareness** (requires knowledge beyond the component)
     * `name`
  2. **Template Compiler Options** (changes the way templates are compiled)
     * `compilerOptions`
  3. **Template Dependencies** (assets used in the template)
     * `components`
     * `directives`
  4. **Composition** (merges properties into the options)
     * `extends`
     * `mixins`
     * `provide`/`inject`
  5. **Interface** (the interface to the component)
     * `inheritAttrs`
     * `props`
     * `emits`
  6. **Composition API** (the entry point for using the Composition API)
     * `setup`
  7. **Local State** (local reactive properties)
     * `data`
     * `computed`
  8. **Events** (callbacks triggered by reactive events)
     * `watch`
     * Lifecycle Events (in the order they are called)
       * `beforeCreate`
       * `created`
       * `beforeMount`
       * `mounted`
       * `beforeUpdate`
       * `updated`
       * `activated`
       * `deactivated`
       * `beforeUnmount`
       * `unmounted`
       * `errorCaptured`
       * `renderTracked`
       * `renderTriggered`
  9. **Non-Reactive Properties** (instance properties independent of the reactivity system)
     * `methods`
  10. **Rendering** (the declarative description of the component output)
     * `template`/`render`


## Element attribute order [​](https://vuejs.org/style-guide/rules-recommended.html#element-attribute-order)
**The attributes of elements (including components) should be ordered consistently.**
This is the default order we recommend for component options. They're split into categories, so you'll know where to add custom attributes and directives.
  1. **Definition** (provides the component options)
     * `is`
  2. **List Rendering** (creates multiple variations of the same element)
     * `v-for`
  3. **Conditionals** (whether the element is rendered/shown)
     * `v-if`
     * `v-else-if`
     * `v-else`
     * `v-show`
     * `v-cloak`
  4. **Render Modifiers** (changes the way the element renders)
     * `v-pre`
     * `v-once`
  5. **Global Awareness** (requires knowledge beyond the component)
     * `id`
  6. **Unique Attributes** (attributes that require unique values)
     * `ref`
     * `key`
  7. **Two-Way Binding** (combining binding and events)
     * `v-model`
  8. **Other Attributes** (all unspecified bound & unbound attributes)
  9. **Events** (component event listeners)
     * `v-on`
  10. **Content** (overrides the content of the element)
     * `v-html`
     * `v-text`


## Empty lines in component/instance options [​](https://vuejs.org/style-guide/rules-recommended.html#empty-lines-in-component-instance-options)
**You may want to add one empty line between multi-line properties, particularly if the options can no longer fit on your screen without scrolling.**
When components begin to feel cramped or difficult to read, adding spaces between multi-line properties can make them easier to skim again. In some editors, such as Vim, formatting options like this can also make them easier to navigate with the keyboard.
### Bad
js```
props: {
  value: {
    type: String,
    required: true
  },

  focused: {
    type: Boolean,
    default: false
  },

  label: String,
  icon: String
},

computed: {
  formattedValue() {
    // ...
  },

  inputClasses() {
    // ...
  }
}
```

### Good
js```
// No spaces are also fine, as long as the component
// is still easy to read and navigate.
props: {
  value: {
    type: String,
    required: true
  },
  focused: {
    type: Boolean,
    default: false
  },
  label: String,
  icon: String
},
computed: {
  formattedValue() {
    // ...
  },
  inputClasses() {
    // ...
  }
}
```

### Bad
js```
defineProps({
  value: {
    type: String,
    required: true
  },
  focused: {
    type: Boolean,
    default: false
  },
  label: String,
  icon: String
})
const formattedValue = computed(() => {
  // ...
})
const inputClasses = computed(() => {
  // ...
})
```

### Good
js```
defineProps({
  value: {
    type: String,
    required: true
  },

  focused: {
    type: Boolean,
    default: false
  },

  label: String,
  icon: String
})

const formattedValue = computed(() => {
  // ...
})

const inputClasses = computed(() => {
  // ...
})
```

## Single-file component top-level element order [​](https://vuejs.org/style-guide/rules-recommended.html#single-file-component-top-level-element-order)
**[Single-File Components](https://vuejs.org/guide/scaling-up/sfc) should always order `<script>`, `<template>`, and `<style>` tags consistently, with `<style>` last, because at least one of the other two is always necessary.**
### Bad
ComponentX.vue
template```
<style>/* ... */</style>
<script>/* ... */</script>
<template>...</template>
```

ComponentA.vue
template```
<script>/* ... */</script>
<template>...</template>
<style>/* ... */</style>
```

ComponentB.vue
template```
<template>...</template>
<script>/* ... */</script>
<style>/* ... */</style>
```

### Good
ComponentA.vue
template```
<script>/* ... */</script>
<template>...</template>
<style>/* ... */</style>
```

ComponentB.vue
template```
<script>/* ... */</script>
<template>...</template>
<style>/* ... */</style>
```

or
ComponentA.vue
template```
<template>...</template>
<script>/* ... */</script>
<style>/* ... */</style>
```

ComponentB.vue
template```
<template>...</template>
<script>/* ... */</script>
<style>/* ... */</style>
```

[B - Strongly Recommended](https://vuejs.org/style-guide/rules-strongly-recommended)[Next D - Use with Caution](https://vuejs.org/style-guide/rules-use-with-caution)
Priority C Rules: Recommended has loaded
