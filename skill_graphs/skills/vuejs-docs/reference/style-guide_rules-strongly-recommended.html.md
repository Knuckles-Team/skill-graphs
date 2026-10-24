[Skip to content](https://vuejs.org/style-guide/rules-strongly-recommended.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/style-guide/rules-strongly-recommended)
[日本語 ](https://ja.vuejs.org/style-guide/rules-strongly-recommended)
[Українська ](https://ua.vuejs.org/style-guide/rules-strongly-recommended)
[Français ](https://fr.vuejs.org/style-guide/rules-strongly-recommended)
[한국어 ](https://ko.vuejs.org/style-guide/rules-strongly-recommended)
[Português ](https://pt.vuejs.org/style-guide/rules-strongly-recommended)
[বাংলা ](https://bn.vuejs.org/style-guide/rules-strongly-recommended)
[Italiano ](https://it.vuejs.org/style-guide/rules-strongly-recommended)
[فارسی ](https://fa.vuejs.org/style-guide/rules-strongly-recommended)
[Русский ](https://ru.vuejs.org/style-guide/rules-strongly-recommended)
[Čeština ](https://cs.vuejs.org/style-guide/rules-strongly-recommended)
[繁體中文 ](https://zh-hk.vuejs.org/style-guide/rules-strongly-recommended)
[Polski ](https://pl.vuejs.org/style-guide/rules-strongly-recommended)
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
  * [Component files](https://vuejs.org/style-guide/rules-strongly-recommended.html#component-files)
  * [Single-file component filename casing](https://vuejs.org/style-guide/rules-strongly-recommended.html#single-file-component-filename-casing)
  * [Base component names](https://vuejs.org/style-guide/rules-strongly-recommended.html#base-component-names)
  * [Tightly coupled component names](https://vuejs.org/style-guide/rules-strongly-recommended.html#tightly-coupled-component-names)
  * [Order of words in component names](https://vuejs.org/style-guide/rules-strongly-recommended.html#order-of-words-in-component-names)
  * [Self-closing components](https://vuejs.org/style-guide/rules-strongly-recommended.html#self-closing-components)
  * [Component name casing in templates](https://vuejs.org/style-guide/rules-strongly-recommended.html#component-name-casing-in-templates)
  * [Component name casing in JS/JSX](https://vuejs.org/style-guide/rules-strongly-recommended.html#component-name-casing-in-js-jsx)
  * [Full-word component names](https://vuejs.org/style-guide/rules-strongly-recommended.html#full-word-component-names)
  * [Prop name casing](https://vuejs.org/style-guide/rules-strongly-recommended.html#prop-name-casing)
  * [Multi-attribute elements](https://vuejs.org/style-guide/rules-strongly-recommended.html#multi-attribute-elements)
  * [Simple expressions in templates](https://vuejs.org/style-guide/rules-strongly-recommended.html#simple-expressions-in-templates)
  * [Simple computed properties](https://vuejs.org/style-guide/rules-strongly-recommended.html#simple-computed-properties)
  * [Quoted attribute values](https://vuejs.org/style-guide/rules-strongly-recommended.html#quoted-attribute-values)
  * [Directive shorthands](https://vuejs.org/style-guide/rules-strongly-recommended.html#directive-shorthands)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Priority B Rules: Strongly Recommended [​](https://vuejs.org/style-guide/rules-strongly-recommended.html#priority-b-rules-strongly-recommended)
Note
This Vue.js Style Guide is outdated and needs to be reviewed. If you have any questions or suggestions, please
These rules have been found to improve readability and/or developer experience in most projects. Your code will still run if you violate them, but violations should be rare and well-justified.
## Component files [​](https://vuejs.org/style-guide/rules-strongly-recommended.html#component-files)
**Whenever a build system is available to concatenate files, each component should be in its own file.**
This helps you to more quickly find a component when you need to edit it or review how to use it.
### Bad
js```
app.component('TodoList', {
  // ...
})

app.component('TodoItem', {
  // ...
})
```

### Good
```
components/
|- TodoList.js
|- TodoItem.js
```

```
components/
|- TodoList.vue
|- TodoItem.vue
```

## Single-file component filename casing [​](https://vuejs.org/style-guide/rules-strongly-recommended.html#single-file-component-filename-casing)
**Filenames of[Single-File Components](https://vuejs.org/guide/scaling-up/sfc) should either be always PascalCase or always kebab-case.**
PascalCase works best with autocompletion in code editors, as it's consistent with how we reference components in JS(X) and templates, wherever possible. However, mixed case filenames can sometimes create issues on case-insensitive file systems, which is why kebab-case is also perfectly acceptable.
### Bad
```
components/
|- mycomponent.vue
```

```
components/
|- myComponent.vue
```

### Good
```
components/
|- MyComponent.vue
```

```
components/
|- my-component.vue
```

## Base component names [​](https://vuejs.org/style-guide/rules-strongly-recommended.html#base-component-names)
**Base components (a.k.a. presentational, dumb, or pure components) that apply app-specific styling and conventions should all begin with a specific prefix, such as`Base` , `App`, or `V`.**
Detailed Explanation
These components lay the foundation for consistent styling and behavior in your application. They may **only** contain:
  * HTML elements,
  * other base components, and
  * 3rd-party UI components.


But they'll **never** contain global state (e.g. from a [Pinia](https://pinia.vuejs.org/) store).
Their names often include the name of an element they wrap (e.g. `BaseButton`, `BaseTable`), unless no element exists for their specific purpose (e.g. `BaseIcon`). If you build similar components for a more specific context, they will almost always consume these components (e.g. `BaseButton` may be used in `ButtonSubmit`).
Some advantages of this convention:
  * When organized alphabetically in editors, your app's base components are all listed together, making them easier to identify.
  * Since component names should always be multi-word, this convention prevents you from having to choose an arbitrary prefix for simple component wrappers (e.g. `MyButton`, `VueButton`).
  * Since these components are so frequently used, you may want to simply make them global instead of importing them everywhere. A prefix makes this possible with Webpack:
js```
const requireComponent = require.context(
  './src',
  true,
  /Base[A-Z]\w+\.(vue|js)$/
)
requireComponent.keys().forEach(function (fileName) {
  let baseComponentConfig = requireComponent(fileName)
  baseComponentConfig =
    baseComponentConfig.default || baseComponentConfig
  const baseComponentName =
    baseComponentConfig.name ||
    fileName.replace(/^.+\//, '').replace(/\.\w+$/, '')
  app.component(baseComponentName, baseComponentConfig)
})
```



### Bad
```
components/
|- MyButton.vue
|- VueTable.vue
|- Icon.vue
```

### Good
```
components/
|- BaseButton.vue
|- BaseTable.vue
|- BaseIcon.vue
```

```
components/
|- AppButton.vue
|- AppTable.vue
|- AppIcon.vue
```

```
components/
|- VButton.vue
|- VTable.vue
|- VIcon.vue
```

## Tightly coupled component names [​](https://vuejs.org/style-guide/rules-strongly-recommended.html#tightly-coupled-component-names)
**Child components that are tightly coupled with their parent should include the parent component name as a prefix.**
If a component only makes sense in the context of a single parent component, that relationship should be evident in its name. Since editors typically organize files alphabetically, this also keeps these related files next to each other.
Detailed Explanation
You might be tempted to solve this problem by nesting child components in directories named after their parent. For example:
```
components/
|- TodoList/
   |- Item/
      |- index.vue
      |- Button.vue
   |- index.vue
```

or:
```
components/
|- TodoList/
   |- Item/
      |- Button.vue
   |- Item.vue
|- TodoList.vue
```

This isn't recommended, as it results in:
  * Many files with similar names, making rapid file switching in code editors more difficult.
  * Many nested sub-directories, which increases the time it takes to browse components in an editor's sidebar.


### Bad
```
components/
|- TodoList.vue
|- TodoItem.vue
|- TodoButton.vue
```

```
components/
|- SearchSidebar.vue
|- NavigationForSearchSidebar.vue
```

### Good
```
components/
|- TodoList.vue
|- TodoListItem.vue
|- TodoListItemButton.vue
```

```
components/
|- SearchSidebar.vue
|- SearchSidebarNavigation.vue
```

## Order of words in component names [​](https://vuejs.org/style-guide/rules-strongly-recommended.html#order-of-words-in-component-names)
**Component names should start with the highest-level (often most general) words and end with descriptive modifying words.**
Detailed Explanation
You may be wondering:
> "Why would we force component names to use less natural language?"
In natural English, adjectives and other descriptors do typically appear before the nouns, while exceptions require connector words. For example:
  * Coffee _with_ milk
  * Soup _of the_ day
  * Visitor _to the_ museum


You can definitely include these connector words in component names if you'd like, but the order is still important.
Also note that **what's considered "highest-level" will be contextual to your app**. For example, imagine an app with a search form. It may include components like this one:
```
components/
|- ClearSearchButton.vue
|- ExcludeFromSearchInput.vue
|- LaunchOnStartupCheckbox.vue
|- RunSearchButton.vue
|- SearchInput.vue
|- TermsCheckbox.vue
```

As you might notice, it's quite difficult to see which components are specific to the search. Now let's rename the components according to the rule:
```
components/
|- SearchButtonClear.vue
|- SearchButtonRun.vue
|- SearchInputExcludeGlob.vue
|- SearchInputQuery.vue
|- SettingsCheckboxLaunchOnStartup.vue
|- SettingsCheckboxTerms.vue
```

Since editors typically organize files alphabetically, all the important relationships between components are now evident at a glance.
You might be tempted to solve this problem differently, nesting all the search components under a "search" directory, then all the settings components under a "settings" directory. We only recommend considering this approach in very large apps (e.g. 100+ components), for these reasons:
  * It generally takes more time to navigate through nested sub-directories, than scrolling through a single `components` directory.
  * Name conflicts (e.g. multiple `ButtonDelete.vue` components) make it more difficult to quickly navigate to a specific component in a code editor.
  * Refactoring becomes more difficult, because find-and-replace often isn't sufficient to update relative references to a moved component.


### Bad
```
components/
|- ClearSearchButton.vue
|- ExcludeFromSearchInput.vue
|- LaunchOnStartupCheckbox.vue
|- RunSearchButton.vue
|- SearchInput.vue
|- TermsCheckbox.vue
```

### Good
```
components/
|- SearchButtonClear.vue
|- SearchButtonRun.vue
|- SearchInputQuery.vue
|- SearchInputExcludeGlob.vue
|- SettingsCheckboxTerms.vue
|- SettingsCheckboxLaunchOnStartup.vue
```

## Self-closing components [​](https://vuejs.org/style-guide/rules-strongly-recommended.html#self-closing-components)
**Components with no content should be self-closing in[Single-File Components](https://vuejs.org/guide/scaling-up/sfc), string templates, and [JSX](https://vuejs.org/guide/extras/render-function#jsx-tsx) - but never in in-DOM templates.**
Components that self-close communicate that they not only have no content, but are **meant** to have no content. It's the difference between a blank page in a book and one labeled "This page intentionally left blank." Your code is also cleaner without the unnecessary closing tag.
Unfortunately, HTML doesn't allow custom elements to be self-closing - only
### Bad
template```
<!-- In Single-File Components, string templates, and JSX -->
<MyComponent></MyComponent>
```

template```
<!-- In in-DOM templates -->
<my-component/>
```

### Good
template```
<!-- In Single-File Components, string templates, and JSX -->
<MyComponent/>
```

template```
<!-- In in-DOM templates -->
<my-component></my-component>
```

## Component name casing in templates [​](https://vuejs.org/style-guide/rules-strongly-recommended.html#component-name-casing-in-templates)
**In most projects, component names should always be PascalCase in[Single-File Components](https://vuejs.org/guide/scaling-up/sfc) and string templates - but kebab-case in in-DOM templates.**
PascalCase has a few advantages over kebab-case:
  * Editors can autocomplete component names in templates, because PascalCase is also used in JavaScript.
  * `<MyComponent>` is more visually distinct from a single-word HTML element than `<my-component>`, because there are two character differences (the two capitals), rather than just one (a hyphen).
  * If you use any non-Vue custom elements in your templates, such as a web component, PascalCase ensures that your Vue components remain distinctly visible.


Unfortunately, due to HTML's case insensitivity, in-DOM templates must still use kebab-case.
Also note that if you've already invested heavily in kebab-case, consistency with HTML conventions and being able to use the same casing across all your projects may be more important than the advantages listed above. In those cases, **using kebab-case everywhere is also acceptable.**
### Bad
template```
<!-- In Single-File Components and string templates -->
<mycomponent/>
```

template```
<!-- In Single-File Components and string templates -->
<myComponent/>
```

template```
<!-- In in-DOM templates -->
<MyComponent></MyComponent>
```

### Good
template```
<!-- In Single-File Components and string templates -->
<MyComponent/>
```

template```
<!-- In in-DOM templates -->
<my-component></my-component>
```

OR
template```
<!-- Everywhere -->
<my-component></my-component>
```

## Component name casing in JS/JSX [​](https://vuejs.org/style-guide/rules-strongly-recommended.html#component-name-casing-in-js-jsx)
**Component names in JS/[JSX](https://vuejs.org/guide/extras/render-function#jsx-tsx) should always be PascalCase, though they may be kebab-case inside strings for simpler applications that only use global component registration through `app.component`.**
Detailed Explanation
In JavaScript, PascalCase is the convention for classes and prototype constructors - essentially, anything that can have distinct instances. Vue components also have instances, so it makes sense to also use PascalCase. As an added benefit, using PascalCase within JSX (and templates) allows readers of the code to more easily distinguish between components and HTML elements.
However, for applications that use **only** global component definitions via `app.component`, we recommend kebab-case instead. The reasons are:
  * It's rare that global components are ever referenced in JavaScript, so following a convention for JavaScript makes less sense.
  * These applications always include many in-DOM templates, where [kebab-case **must** be used](https://vuejs.org/style-guide/rules-strongly-recommended.html#component-name-casing-in-templates).


### Bad
js```
app.component('myComponent', {
  // ...
})
```

js```
import myComponent from './MyComponent.vue'
```

js```
export default {
  name: 'myComponent'
  // ...
}
```

js```
export default {
  name: 'my-component'
  // ...
}
```

### Good
js```
app.component('MyComponent', {
  // ...
})
```

js```
app.component('my-component', {
  // ...
})
```

js```
import MyComponent from './MyComponent.vue'
```

js```
export default {
  name: 'MyComponent'
  // ...
}
```

## Full-word component names [​](https://vuejs.org/style-guide/rules-strongly-recommended.html#full-word-component-names)
**Component names should prefer full words over abbreviations.**
The autocompletion in editors make the cost of writing longer names very low, while the clarity they provide is invaluable. Uncommon abbreviations, in particular, should always be avoided.
### Bad
```
components/
|- SdSettings.vue
|- UProfOpts.vue
```

### Good
```
components/
|- StudentDashboardSettings.vue
|- UserProfileOptions.vue
```

## Prop name casing [​](https://vuejs.org/style-guide/rules-strongly-recommended.html#prop-name-casing)
**Prop names should always use camelCase during declaration. When used inside in-DOM templates, props should be kebab-cased. Single-File Components templates and[JSX](https://vuejs.org/guide/extras/render-function#jsx-tsx) can use either kebab-case or camelCase props. Casing should be consistent - if you choose to use camelCased props, make sure you don't use kebab-cased ones in your application**
### Bad
js```
props: {
  'greeting-text': String
}
```

js```
const props = defineProps({
  'greeting-text': String
})
```

template```
// for in-DOM templates
<welcome-message greetingText="hi"></welcome-message>
```

### Good
js```
props: {
  greetingText: String
}
```

js```
const props = defineProps({
  greetingText: String
})
```

template```
// for SFC - please make sure your casing is consistent throughout the project
// you can use either convention but we don't recommend mixing two different casing styles
<WelcomeMessage greeting-text="hi"/>
// or
<WelcomeMessage greetingText="hi"/>
```

template```
// for in-DOM templates
<welcome-message greeting-text="hi"></welcome-message>
```

## Multi-attribute elements [​](https://vuejs.org/style-guide/rules-strongly-recommended.html#multi-attribute-elements)
**Elements with multiple attributes should span multiple lines, with one attribute per line.**
In JavaScript, splitting objects with multiple properties over multiple lines is widely considered a good convention, because it's much easier to read. Our templates and [JSX](https://vuejs.org/guide/extras/render-function#jsx-tsx) deserve the same consideration.
### Bad
template```
<img src="https://vuejs.org/images/logo.png" alt="Vue Logo">
```

template```
<MyComponent foo="a" bar="b" baz="c"/>
```

### Good
template```
<img
  src="https://vuejs.org/images/logo.png"
  alt="Vue Logo"
>
```

template```
<MyComponent
  foo="a"
  bar="b"
  baz="c"
/>
```

## Simple expressions in templates [​](https://vuejs.org/style-guide/rules-strongly-recommended.html#simple-expressions-in-templates)
**Component templates should only include simple expressions, with more complex expressions refactored into computed properties or methods.**
Complex expressions in your templates make them less declarative. We should strive to describe _what_ should appear, not _how_ we're computing that value. Computed properties and methods also allow the code to be reused.
### Bad
template```
{{
  fullName.split(' ').map((word) => {
    return word[0].toUpperCase() + word.slice(1)
  }).join(' ')
}}
```

### Good
template```
<!-- In a template -->
{{ normalizedFullName }}
```

js```
// The complex expression has been moved to a computed property
computed: {
  normalizedFullName() {
    return this.fullName.split(' ')
      .map(word => word[0].toUpperCase() + word.slice(1))
      .join(' ')
  }
}
```

js```
// The complex expression has been moved to a computed property
const normalizedFullName = computed(() =>
  fullName.value
    .split(' ')
    .map((word) => word[0].toUpperCase() + word.slice(1))
    .join(' ')
)
```

## Simple computed properties [​](https://vuejs.org/style-guide/rules-strongly-recommended.html#simple-computed-properties)
**Complex computed properties should be split into as many simpler properties as possible.**
Detailed Explanation
Simpler, well-named computed properties are:
  * **Easier to test**
When each computed property contains only a very simple expression, with very few dependencies, it's much easier to write tests confirming that it works correctly.
  * **Easier to read**
Simplifying computed properties forces you to give each value a descriptive name, even if it's not reused. This makes it much easier for other developers (and future you) to focus in on the code they care about and figure out what's going on.
  * **More adaptable to changing requirements**
Any value that can be named might be useful to the view. For example, we might decide to display a message telling the user how much money they saved. We might also decide to calculate sales tax, but perhaps display it separately, rather than as part of the final price.
Small, focused computed properties make fewer assumptions about how information will be used, so require less refactoring as requirements change.


### Bad
js```
computed: {
  price() {
    const basePrice = this.manufactureCost / (1 - this.profitMargin)
    return (
      basePrice -
      basePrice * (this.discountPercent || 0)
    )
  }
}
```

js```
const price = computed(() => {
  const basePrice = manufactureCost.value / (1 - profitMargin.value)
  return basePrice - basePrice * (discountPercent.value || 0)
})
```

### Good
js```
computed: {
  basePrice() {
    return this.manufactureCost / (1 - this.profitMargin)
  },

  discount() {
    return this.basePrice * (this.discountPercent || 0)
  },

  finalPrice() {
    return this.basePrice - this.discount
  }
}
```

js```
const basePrice = computed(
  () => manufactureCost.value / (1 - profitMargin.value)
)

const discount = computed(
  () => basePrice.value * (discountPercent.value || 0)
)

const finalPrice = computed(() => basePrice.value - discount.value)
```

## Quoted attribute values [​](https://vuejs.org/style-guide/rules-strongly-recommended.html#quoted-attribute-values)
**Non-empty HTML attribute values should always be inside quotes (single or double, whichever is not used in JS).**
While attribute values without any spaces are not required to have quotes in HTML, this practice often leads to _avoiding_ spaces, making attribute values less readable.
### Bad
template```
<input type=text>
```

template```
<AppSidebar :style={width:sidebarWidth+'px'}>
```

### Good
template```
<input type="text">
```

template```
<AppSidebar :style="{ width: sidebarWidth + 'px' }">
```

## Directive shorthands [​](https://vuejs.org/style-guide/rules-strongly-recommended.html#directive-shorthands)
**Directive shorthands (`:` for `v-bind:`, `@` for `v-on:` and `#` for `v-slot`) should be used always or never.**
### Bad
template```
<input
  v-bind:value="newTodoText"
  :placeholder="newTodoInstructions"
>
```

template```
<input
  v-on:input="onInput"
  @focus="onFocus"
>
```

template```
<template v-slot:header>
  <h1>Here might be a page title</h1>
</template>

<template #footer>
  <p>Here's some contact info</p>
</template>
```

### Good
template```
<input
  :value="newTodoText"
  :placeholder="newTodoInstructions"
>
```

template```
<input
  v-bind:value="newTodoText"
  v-bind:placeholder="newTodoInstructions"
>
```

template```
<input
  @input="onInput"
  @focus="onFocus"
>
```

template```
<input
  v-on:input="onInput"
  v-on:focus="onFocus"
>
```

template```
<template v-slot:header>
  <h1>Here might be a page title</h1>
</template>

<template v-slot:footer>
  <p>Here's some contact info</p>
</template>
```

template```
<template #header>
  <h1>Here might be a page title</h1>
</template>

<template #footer>
  <p>Here's some contact info</p>
</template>
```

[A - Essential](https://vuejs.org/style-guide/rules-essential)[Next C - Recommended](https://vuejs.org/style-guide/rules-recommended)
Priority B Rules: Strongly Recommended has loaded
