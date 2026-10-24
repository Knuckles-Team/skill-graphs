[Skip to content](https://vuejs.org/api/ssr.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/api/ssr)
[日本語 ](https://ja.vuejs.org/api/ssr)
[Українська ](https://ua.vuejs.org/api/ssr)
[Français ](https://fr.vuejs.org/api/ssr)
[한국어 ](https://ko.vuejs.org/api/ssr)
[Português ](https://pt.vuejs.org/api/ssr)
[বাংলা ](https://bn.vuejs.org/api/ssr)
[Italiano ](https://it.vuejs.org/api/ssr)
[فارسی ](https://fa.vuejs.org/api/ssr)
[Русский ](https://ru.vuejs.org/api/ssr)
[Čeština ](https://cs.vuejs.org/api/ssr)
[繁體中文 ](https://zh-hk.vuejs.org/api/ssr)
[Polski ](https://pl.vuejs.org/api/ssr)
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
  * [renderToString()](https://vuejs.org/api/ssr.html#rendertostring)
  * [renderToNodeStream()](https://vuejs.org/api/ssr.html#rendertonodestream)
  * [pipeToNodeWritable()](https://vuejs.org/api/ssr.html#pipetonodewritable)
  * [renderToWebStream()](https://vuejs.org/api/ssr.html#rendertowebstream)
  * [pipeToWebWritable()](https://vuejs.org/api/ssr.html#pipetowebwritable)
  * [renderToSimpleStream()](https://vuejs.org/api/ssr.html#rendertosimplestream)
  * [useSSRContext()](https://vuejs.org/api/ssr.html#usessrcontext)
  * [data-allow-mismatch](https://vuejs.org/api/ssr.html#data-allow-mismatch)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Server-Side Rendering API [​](https://vuejs.org/api/ssr.html#server-side-rendering-api)
## renderToString() [​](https://vuejs.org/api/ssr.html#rendertostring)
  * **Exported from`vue/server-renderer`**
  * **Type**
ts```
function renderToString(
  input: App | VNode,
  context?: SSRContext
): Promise<string>
```

  * **Example**
js```
import { createSSRApp } from 'vue'
import { renderToString } from 'vue/server-renderer'

const app = createSSRApp({
  data: () => ({ msg: 'hello' }),
  template: `<div>{{ msg }}</div>`
})

;(async () => {
  const html = await renderToString(app)
  console.log(html)
})()
```

### SSR Context [​](https://vuejs.org/api/ssr.html#ssr-context)
You can pass an optional context object, which can be used to record additional data during the render, for example [accessing content of Teleports](https://vuejs.org/guide/scaling-up/ssr#teleports):
js```
const ctx = {}
const html = await renderToString(app, ctx)

console.log(ctx.teleports) // { '#teleported': 'teleported content' }
```

Most other SSR APIs on this page also optionally accept a context object. The context object can be accessed in component code via the [useSSRContext](https://vuejs.org/api/ssr.html#usessrcontext) helper.
  * **See also** [Guide - Server-Side Rendering](https://vuejs.org/guide/scaling-up/ssr)


## renderToNodeStream() [​](https://vuejs.org/api/ssr.html#rendertonodestream)
Renders input as a
  * **Exported from`vue/server-renderer`**
  * **Type**
ts```
function renderToNodeStream(
  input: App | VNode,
  context?: SSRContext
): Readable
```

  * **Example**
js```
// inside a Node.js http handler
renderToNodeStream(app).pipe(res)
```

Note
This method is not supported in the ESM build of `vue/server-renderer`, which is decoupled from Node.js environments. Use [`pipeToNodeWritable`](https://vuejs.org/api/ssr.html#pipetonodewritable) instead.


## pipeToNodeWritable() [​](https://vuejs.org/api/ssr.html#pipetonodewritable)
Render and pipe to an existing
  * **Exported from`vue/server-renderer`**
  * **Type**
ts```
function pipeToNodeWritable(
  input: App | VNode,
  context: SSRContext = {},
  writable: Writable
): void
```

  * **Example**
js```
// inside a Node.js http handler
pipeToNodeWritable(app, {}, res)
```



## renderToWebStream() [​](https://vuejs.org/api/ssr.html#rendertowebstream)
Renders input as a
  * **Exported from`vue/server-renderer`**
  * **Type**
ts```
function renderToWebStream(
  input: App | VNode,
  context?: SSRContext
): ReadableStream
```

  * **Example**
js```
// inside an environment with ReadableStream support
return new Response(renderToWebStream(app))
```

Note
In environments that do not expose `ReadableStream` constructor in the global scope, [`pipeToWebWritable()`](https://vuejs.org/api/ssr.html#pipetowebwritable) should be used instead.


## pipeToWebWritable() [​](https://vuejs.org/api/ssr.html#pipetowebwritable)
Render and pipe to an existing
  * **Exported from`vue/server-renderer`**
  * **Type**
ts```
function pipeToWebWritable(
  input: App | VNode,
  context: SSRContext = {},
  writable: WritableStream
): void
```

  * **Example**
This is typically used in combination with
js```
// TransformStream is available in environments such as CloudFlare workers.
// in Node.js, TransformStream needs to be explicitly imported from 'stream/web'
const { readable, writable } = new TransformStream()
pipeToWebWritable(app, {}, writable)

return new Response(readable)
```



## renderToSimpleStream() [​](https://vuejs.org/api/ssr.html#rendertosimplestream)
Renders input in streaming mode using a simple readable interface.
  * **Exported from`vue/server-renderer`**
  * **Type**
ts```
function renderToSimpleStream(
  input: App | VNode,
  context: SSRContext,
  options: SimpleReadable
): SimpleReadable

interface SimpleReadable {
  push(content: string | null): void
  destroy(err: any): void
}
```

  * **Example**
js```
let res = ''

renderToSimpleStream(
  app,
  {},
  {
    push(chunk) {
      if (chunk === null) {
        // done
        console(`render complete: ${res}`)
      } else {
        res += chunk
      }
    },
    destroy(err) {
      // error encountered
    }
  }
)
```



## useSSRContext() [​](https://vuejs.org/api/ssr.html#usessrcontext)
A runtime API used to retrieve the context object passed to `renderToString()` or other server render APIs.
  * **Type**
ts```
function useSSRContext<T = Record<string, any>>(): T | undefined
```

  * **Example**
The retrieved context can be used to attach information that is needed for rendering the final HTML (e.g. head metadata).
vue```
<script setup>
import { useSSRContext } from 'vue'

// make sure to only call it during SSR
// https://vite.dev/guide/ssr.html#conditional-logic
if (import.meta.env.SSR) {
  const ctx = useSSRContext()
  // ...attach properties to the context
}
</script>
```



## data-allow-mismatch [​](https://vuejs.org/api/ssr.html#data-allow-mismatch)
A special attribute that can be used to suppress [hydration mismatch](https://vuejs.org/guide/scaling-up/ssr#hydration-mismatch) warnings.
  * **Example**
html```
<div data-allow-mismatch="text">{{ data.toLocaleString() }}</div>
```

The value can limit the allowed mismatch to a specific type. Allowed values are:
    * `text`
    * `children` (only allows mismatch for direct children)
    * `class`
    * `style`
    * `attribute`
If no value is provided, all types of mismatches will be allowed.


[Render Function](https://vuejs.org/api/render-function)[Next TypeScript Utility Types](https://vuejs.org/api/utility-types)
Server-Side Rendering API has loaded
