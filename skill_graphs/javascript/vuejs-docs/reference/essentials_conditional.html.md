[Skip to content](https://vuejs.org/guide/essentials/conditional.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/guide/essentials/conditional)
[日本語 ](https://ja.vuejs.org/guide/essentials/conditional)
[Українська ](https://ua.vuejs.org/guide/essentials/conditional)
[Français ](https://fr.vuejs.org/guide/essentials/conditional)
[한국어 ](https://ko.vuejs.org/guide/essentials/conditional)
[Português ](https://pt.vuejs.org/guide/essentials/conditional)
[বাংলা ](https://bn.vuejs.org/guide/essentials/conditional)
[Italiano ](https://it.vuejs.org/guide/essentials/conditional)
[فارسی ](https://fa.vuejs.org/guide/essentials/conditional)
[Русский ](https://ru.vuejs.org/guide/essentials/conditional)
[Čeština ](https://cs.vuejs.org/guide/essentials/conditional)
[繁體中文 ](https://zh-hk.vuejs.org/guide/essentials/conditional)
[Polski ](https://pl.vuejs.org/guide/essentials/conditional)
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
  * [v-if](https://vuejs.org/guide/essentials/conditional.html#v-if)
  * [v-else](https://vuejs.org/guide/essentials/conditional.html#v-else)
  * [v-else-if](https://vuejs.org/guide/essentials/conditional.html#v-else-if)
  * [v-if on <template>](https://vuejs.org/guide/essentials/conditional.html#v-if-on-template)
  * [v-show](https://vuejs.org/guide/essentials/conditional.html#v-show)
  * [v-if vs. v-show](https://vuejs.org/guide/essentials/conditional.html#v-if-vs-v-show)
  * [v-if with v-for](https://vuejs.org/guide/essentials/conditional.html#v-if-with-v-for)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Conditional Rendering [​](https://vuejs.org/guide/essentials/conditional.html#conditional-rendering)
##  `v-if` [​](https://vuejs.org/guide/essentials/conditional.html#v-if)
The directive `v-if` is used to conditionally render a block. The block will only be rendered if the directive's expression returns a truthy value.
template```
<h1 v-if="awesome">Vue is awesome!</h1>
```

##  `v-else` [​](https://vuejs.org/guide/essentials/conditional.html#v-else)
You can use the `v-else` directive to indicate an "else block" for `v-if`:
template```
<button @click="awesome = !awesome">Toggle</button>

<h1 v-if="awesome">Vue is awesome!</h1>
<h1 v-else>Oh no 😢</h1>
```

Toggle
# Vue is awesome!
[Try it in the Playground](https://play.vuejs.org/#eNpFjkEOgjAQRa8ydIMulLA1hegJ3LnqBskAjdA27RQXhHu4M/GEHsEiKLv5mfdf/sBOxux7j+zAuCutNAQOyZtcKNkZbQkGsFjBCJXVHcQBjYUSqtTKERR3dLpDyCZmQ9bjViiezKKgCIGwM21BGBIAv3oireBYtrK8ZYKtgmg5BctJ13WLPJnhr0YQb1Lod7JaS4G8eATpfjMinjTphC8wtg7zcwNKw/v5eC1fnvwnsfEDwaha7w==)
[Try it in the Playground](https://play.vuejs.org/#eNpFjj0OwjAMha9iMsEAFWuVVnACNqYsoXV/RJpEqVOQqt6DDYkTcgRSWoplWX7y56fXs6O1u84jixlvM1dbSoXGuzWOIMdCekXQCw2QS5LrzbQLckje6VEJglDyhq1pMAZyHidkGG9hhObRYh0EYWOVJAwKgF88kdFwyFSdXRPBZidIYDWvgqVkylIhjyb4ayOIV3votnXxfwrk2SPU7S/PikfVfsRnGFWL6akCbeD9fLzmK4+WSGz4AA5dYQY=)
A `v-else` element must immediately follow a `v-if` or a `v-else-if` element - otherwise it will not be recognized.
##  `v-else-if` [​](https://vuejs.org/guide/essentials/conditional.html#v-else-if)
The `v-else-if`, as the name suggests, serves as an "else if block" for `v-if`. It can also be chained multiple times:
template```
<div v-if="type === 'A'">
  A
</div>
<div v-else-if="type === 'B'">
  B
</div>
<div v-else-if="type === 'C'">
  C
</div>
<div v-else>
  Not A/B/C
</div>
```

Similar to `v-else`, a `v-else-if` element must immediately follow a `v-if` or a `v-else-if` element.
##  `v-if` on `<template>` [​](https://vuejs.org/guide/essentials/conditional.html#v-if-on-template)
Because `v-if` is a directive, it has to be attached to a single element. But what if we want to toggle more than one element? In this case we can use `v-if` on a `<template>` element, which serves as an invisible wrapper. The final rendered result will not include the `<template>` element.
template```
<template v-if="ok">
  <h1>Title</h1>
  <p>Paragraph 1</p>
  <p>Paragraph 2</p>
</template>
```

`v-else` and `v-else-if` can also be used on `<template>`.
##  `v-show` [​](https://vuejs.org/guide/essentials/conditional.html#v-show)
Another option for conditionally displaying an element is the `v-show` directive. The usage is largely the same:
template```
<h1 v-show="ok">Hello!</h1>
```

The difference is that an element with `v-show` will always be rendered and remain in the DOM; `v-show` only toggles the `display` CSS property of the element.
`v-show` doesn't support the `<template>` element, nor does it work with `v-else`.
##  `v-if` vs. `v-show` [​](https://vuejs.org/guide/essentials/conditional.html#v-if-vs-v-show)
`v-if` is "real" conditional rendering because it ensures that event listeners and child components inside the conditional block are properly destroyed and re-created during toggles.
`v-if` is also **lazy** : if the condition is false on initial render, it will not do anything - the conditional block won't be rendered until the condition becomes true for the first time.
In comparison, `v-show` is much simpler - the element is always rendered regardless of initial condition, with CSS-based toggling.
Generally speaking, `v-if` has higher toggle costs while `v-show` has higher initial render costs. So prefer `v-show` if you need to toggle something very often, and prefer `v-if` if the condition is unlikely to change at runtime.
##  `v-if` with `v-for` [​](https://vuejs.org/guide/essentials/conditional.html#v-if-with-v-for)
When `v-if` and `v-for` are both used on the same element, `v-if` will be evaluated first. See the [list rendering guide](https://vuejs.org/guide/essentials/list#v-for-with-v-if) for details.
Note
It's **not** recommended to use `v-if` and `v-for` on the same element due to implicit precedence. Refer to [list rendering guide](https://vuejs.org/guide/essentials/list#v-for-with-v-if) for details.
[Class and Style Bindings](https://vuejs.org/guide/essentials/class-and-style)[Next List Rendering](https://vuejs.org/guide/essentials/list)
Conditional Rendering has loaded
