[Skip to content](https://vuejs.org/guide/extras/rendering-mechanism.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/guide/extras/rendering-mechanism)
[日本語 ](https://ja.vuejs.org/guide/extras/rendering-mechanism)
[Українська ](https://ua.vuejs.org/guide/extras/rendering-mechanism)
[Français ](https://fr.vuejs.org/guide/extras/rendering-mechanism)
[한국어 ](https://ko.vuejs.org/guide/extras/rendering-mechanism)
[Português ](https://pt.vuejs.org/guide/extras/rendering-mechanism)
[বাংলা ](https://bn.vuejs.org/guide/extras/rendering-mechanism)
[Italiano ](https://it.vuejs.org/guide/extras/rendering-mechanism)
[فارسی ](https://fa.vuejs.org/guide/extras/rendering-mechanism)
[Русский ](https://ru.vuejs.org/guide/extras/rendering-mechanism)
[Čeština ](https://cs.vuejs.org/guide/extras/rendering-mechanism)
[繁體中文 ](https://zh-hk.vuejs.org/guide/extras/rendering-mechanism)
[Polski ](https://pl.vuejs.org/guide/extras/rendering-mechanism)
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
  * [Virtual DOM](https://vuejs.org/guide/extras/rendering-mechanism.html#virtual-dom)
  * [Render Pipeline](https://vuejs.org/guide/extras/rendering-mechanism.html#render-pipeline)
  * [Templates vs. Render Functions](https://vuejs.org/guide/extras/rendering-mechanism.html#templates-vs-render-functions)
  * [Compiler-Informed Virtual DOM](https://vuejs.org/guide/extras/rendering-mechanism.html#compiler-informed-virtual-dom)
    * [Cache Static](https://vuejs.org/guide/extras/rendering-mechanism.html#cache-static)
    * [Patch Flags](https://vuejs.org/guide/extras/rendering-mechanism.html#patch-flags)
    * [Tree Flattening](https://vuejs.org/guide/extras/rendering-mechanism.html#tree-flattening)
    * [Impact on SSR Hydration](https://vuejs.org/guide/extras/rendering-mechanism.html#impact-on-ssr-hydration)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Rendering Mechanism [​](https://vuejs.org/guide/extras/rendering-mechanism.html#rendering-mechanism)
How does Vue take a template and turn it into actual DOM nodes? How does Vue update those DOM nodes efficiently? We will attempt to shed some light on these questions here by diving into Vue's internal rendering mechanism.
## Virtual DOM [​](https://vuejs.org/guide/extras/rendering-mechanism.html#virtual-dom)
You have probably heard about the term "virtual DOM", which Vue's rendering system is based upon.
The virtual DOM (VDOM) is a programming concept where an ideal, or “virtual”, representation of a UI is kept in memory and synced with the “real” DOM. The concept was pioneered by
Virtual DOM is more of a pattern than a specific technology, so there is no one canonical implementation. We can illustrate the idea using a simple example:
js```
const vnode = {
  type: 'div',
  props: {
    id: 'hello'
  },
  children: [
    /* more vnodes */
  ]
}
```

Here, `vnode` is a plain JavaScript object (a "virtual node") representing a `<div>` element. It contains all the information that we need to create the actual element. It also contains more children vnodes, which makes it the root of a virtual DOM tree.
A runtime renderer can walk a virtual DOM tree and construct a real DOM tree from it. This process is called **mount**.
If we have two copies of virtual DOM trees, the renderer can also walk and compare the two trees, figuring out the differences, and apply those changes to the actual DOM. This process is called **patch** , also known as "diffing" or "reconciliation".
The main benefit of virtual DOM is that it gives the developer the ability to programmatically create, inspect and compose desired UI structures in a declarative way, while leaving the direct DOM manipulation to the renderer.
## Render Pipeline [​](https://vuejs.org/guide/extras/rendering-mechanism.html#render-pipeline)
At the high level, this is what happens when a Vue component is mounted:
  1. **Compile** : Vue templates are compiled into **render functions** : functions that return virtual DOM trees. This step can be done either ahead-of-time via a build step, or on-the-fly by using the runtime compiler.
  2. **Mount** : The runtime renderer invokes the render functions, walks the returned virtual DOM tree, and creates actual DOM nodes based on it. This step is performed as a [reactive effect](https://vuejs.org/guide/extras/reactivity-in-depth), so it keeps track of all reactive dependencies that were used.
  3. **Patch** : When a dependency used during mount changes, the effect re-runs. This time, a new, updated Virtual DOM tree is created. The runtime renderer walks the new tree, compares it with the old one, and applies necessary updates to the actual DOM.


![render pipeline](https://vuejs.org/assets/render-pipeline.CwxnH_lZ.png)
## Templates vs. Render Functions [​](https://vuejs.org/guide/extras/rendering-mechanism.html#templates-vs-render-functions)
Vue templates are compiled into virtual DOM render functions. Vue also provides APIs that allow us to skip the template compilation step and directly author render functions. Render functions are more flexible than templates when dealing with highly dynamic logic, because you can work with vnodes using the full power of JavaScript.
So why does Vue recommend templates by default? There are a number of reasons:
  1. Templates are closer to actual HTML. This makes it easier to reuse existing HTML snippets, apply accessibility best practices, style with CSS, and for designers to understand and modify.
  2. Templates are easier to statically analyze due to their more deterministic syntax. This allows Vue's template compiler to apply many compile-time optimizations to improve the performance of the virtual DOM (which we will discuss below).


In practice, templates are sufficient for most use cases in applications. Render functions are typically only used in reusable components that need to deal with highly dynamic rendering logic. Render function usage is discussed in more detail in [Render Functions & JSX](https://vuejs.org/guide/extras/render-function).
## Compiler-Informed Virtual DOM [​](https://vuejs.org/guide/extras/rendering-mechanism.html#compiler-informed-virtual-dom)
The virtual DOM implementation in React and most other virtual-DOM implementations are purely runtime: the reconciliation algorithm cannot make any assumptions about the incoming virtual DOM tree, so it has to fully traverse the tree and diff the props of every vnode in order to ensure correctness. In addition, even if a part of the tree never changes, new vnodes are always created for them on each re-render, resulting in unnecessary memory pressure. This is one of the most criticized aspect of virtual DOM: the somewhat brute-force reconciliation process sacrifices efficiency in return for declarativeness and correctness.
But it doesn't have to be that way. In Vue, the framework controls both the compiler and the runtime. This allows us to implement many compile-time optimizations that only a tightly-coupled renderer can take advantage of. The compiler can statically analyze the template and leave hints in the generated code so that the runtime can take shortcuts whenever possible. At the same time, we still preserve the capability for the user to drop down to the render function layer for more direct control in edge cases. We call this hybrid approach **Compiler-Informed Virtual DOM**.
Below, we will discuss a few major optimizations done by the Vue template compiler to improve the virtual DOM's runtime performance.
### Cache Static [​](https://vuejs.org/guide/extras/rendering-mechanism.html#cache-static)
Quite often there will be parts in a template that do not contain any dynamic bindings:
template```
<div>
  <div>foo</div> <!-- cached -->
  <div>bar</div> <!-- cached -->
  <div>{{ dynamic }}</div>
</div>
```

[Inspect in Template Explorer](https://template-explorer.vuejs.org/#eyJzcmMiOiI8ZGl2PlxuICA8ZGl2PmZvbzwvZGl2PiA8IS0tIGNhY2hlZCAtLT5cbiAgPGRpdj5iYXI8L2Rpdj4gPCEtLSBjYWNoZWQgLS0+XG4gIDxkaXY+e3sgZHluYW1pYyB9fTwvZGl2PlxuPC9kaXY+XG4iLCJvcHRpb25zIjp7ImhvaXN0U3RhdGljIjp0cnVlfX0=)
The `foo` and `bar` divs are static - re-creating vnodes and diffing them on each re-render is unnecessary. The renderer creates these vnodes during the initial render, caches them, and reuses the same vnodes for every subsequent re-render. The renderer is also able to completely skip diffing them when it notices the old vnode and the new vnode are the same one.
In addition, when there are enough consecutive static elements, they will be condensed into a single "static vnode" that contains the plain HTML string for all these nodes ([Example](https://template-explorer.vuejs.org/#eyJzcmMiOiI8ZGl2PlxuICA8ZGl2IGNsYXNzPVwiZm9vXCI+Zm9vPC9kaXY+XG4gIDxkaXYgY2xhc3M9XCJmb29cIj5mb288L2Rpdj5cbiAgPGRpdiBjbGFzcz1cImZvb1wiPmZvbzwvZGl2PlxuICA8ZGl2IGNsYXNzPVwiZm9vXCI+Zm9vPC9kaXY+XG4gIDxkaXYgY2xhc3M9XCJmb29cIj5mb288L2Rpdj5cbiAgPGRpdj57eyBkeW5hbWljIH19PC9kaXY+XG48L2Rpdj4iLCJzc3IiOmZhbHNlLCJvcHRpb25zIjp7ImhvaXN0U3RhdGljIjp0cnVlfX0=)). These static vnodes are mounted by directly setting `innerHTML`.
### Patch Flags [​](https://vuejs.org/guide/extras/rendering-mechanism.html#patch-flags)
For a single element with dynamic bindings, we can also infer a lot of information from it at compile time:
template```
<!-- class binding only -->
<div :class="{ active }"></div>

<!-- id and value bindings only -->
<input :id="id" :value="value">

<!-- text children only -->
<div>{{ dynamic }}</div>
```

[Inspect in Template Explorer](https://template-explorer.vuejs.org/#eyJzcmMiOiI8ZGl2IDpjbGFzcz1cInsgYWN0aXZlIH1cIj48L2Rpdj5cblxuPGlucHV0IDppZD1cImlkXCIgOnZhbHVlPVwidmFsdWVcIj5cblxuPGRpdj57eyBkeW5hbWljIH19PC9kaXY+Iiwib3B0aW9ucyI6e319)
When generating the render function code for these elements, Vue encodes the type of update each of them needs directly in the vnode creation call:
js```
createElementVNode("div", {
  class: _normalizeClass({ active: _ctx.active })
}, null, 2 /* CLASS */)
```

The last argument, `2`, is a
js```
if (vnode.patchFlag & PatchFlags.CLASS /* 2 */) {
  // update the element's class
}
```

Bitwise checks are extremely fast. With the patch flags, Vue is able to do the least amount of work necessary when updating elements with dynamic bindings.
Vue also encodes the type of children a vnode has. For example, a template that has multiple root nodes is represented as a fragment. In most cases, we know for sure that the order of these root nodes will never change, so this information can also be provided to the runtime as a patch flag:
js```
export function render() {
  return (_openBlock(), _createElementBlock(_Fragment, null, [
    /* children */
  ], 64 /* STABLE_FRAGMENT */))
}
```

The runtime can thus completely skip child-order reconciliation for the root fragment.
### Tree Flattening [​](https://vuejs.org/guide/extras/rendering-mechanism.html#tree-flattening)
Taking another look at the generated code from the previous example, you'll notice the root of the returned virtual DOM tree is created using a special `createElementBlock()` call:
js```
export function render() {
  return (_openBlock(), _createElementBlock(_Fragment, null, [
    /* children */
  ], 64 /* STABLE_FRAGMENT */))
}
```

Conceptually, a "block" is a part of the template that has stable inner structure. In this case, the entire template has a single block because it does not contain any structural directives like `v-if` and `v-for`.
Each block tracks any descendant nodes (not just direct children) that have patch flags. For example:
template```
<div> <!-- root block -->
  <div>...</div>         <!-- not tracked -->
  <div :id="id"></div>   <!-- tracked -->
  <div>                  <!-- not tracked -->
    <div>{{ bar }}</div> <!-- tracked -->
  </div>
</div>
```

The result is a flattened array that contains only the dynamic descendant nodes:
```
div (block root)
- div with :id binding
- div with {{ bar }} binding
```

When this component needs to re-render, it only needs to traverse the flattened tree instead of the full tree. This is called **Tree Flattening** , and it greatly reduces the number of nodes that need to be traversed during virtual DOM reconciliation. Any static parts of the template are effectively skipped.
`v-if` and `v-for` directives will create new block nodes:
template```
<div> <!-- root block -->
  <div>
    <div v-if> <!-- if block -->
      ...
    </div>
  </div>
</div>
```

A child block is tracked inside the parent block's array of dynamic descendants. This retains a stable structure for the parent block.
### Impact on SSR Hydration [​](https://vuejs.org/guide/extras/rendering-mechanism.html#impact-on-ssr-hydration)
Both patch flags and tree flattening also greatly improve Vue's [SSR Hydration](https://vuejs.org/guide/scaling-up/ssr#client-hydration) performance:
  * Single element hydration can take fast paths based on the corresponding vnode's patch flag.
  * Only block nodes and their dynamic descendants need to be traversed during hydration, effectively achieving partial hydration at the template level.


[Reactivity in Depth](https://vuejs.org/guide/extras/reactivity-in-depth)[Next Render Functions & JSX](https://vuejs.org/guide/extras/render-function)
Rendering Mechanism has loaded
