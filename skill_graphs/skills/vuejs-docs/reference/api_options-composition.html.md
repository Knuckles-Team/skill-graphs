[Skip to content](https://vuejs.org/api/options-composition.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/api/options-composition)
[日本語 ](https://ja.vuejs.org/api/options-composition)
[Українська ](https://ua.vuejs.org/api/options-composition)
[Français ](https://fr.vuejs.org/api/options-composition)
[한국어 ](https://ko.vuejs.org/api/options-composition)
[Português ](https://pt.vuejs.org/api/options-composition)
[বাংলা ](https://bn.vuejs.org/api/options-composition)
[Italiano ](https://it.vuejs.org/api/options-composition)
[فارسی ](https://fa.vuejs.org/api/options-composition)
[Русский ](https://ru.vuejs.org/api/options-composition)
[Čeština ](https://cs.vuejs.org/api/options-composition)
[繁體中文 ](https://zh-hk.vuejs.org/api/options-composition)
[Polski ](https://pl.vuejs.org/api/options-composition)
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
  * [provide](https://vuejs.org/api/options-composition.html#provide)
  * [inject](https://vuejs.org/api/options-composition.html#inject)
  * [mixins](https://vuejs.org/api/options-composition.html#mixins)
  * [extends](https://vuejs.org/api/options-composition.html#extends)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Options: Composition [​](https://vuejs.org/api/options-composition.html#options-composition)
## provide [​](https://vuejs.org/api/options-composition.html#provide)
Provide values that can be injected by descendant components.
  * **Type**
ts```
interface ComponentOptions {
  provide?: object | ((this: ComponentPublicInstance) => object)
}
```

  * **Details**
`provide` and [`inject`](https://vuejs.org/api/options-composition.html#inject) are used together to allow an ancestor component to serve as a dependency injector for all its descendants, regardless of how deep the component hierarchy is, as long as they are in the same parent chain.
The `provide` option should be either an object or a function that returns an object. This object contains the properties that are available for injection into its descendants. You can use Symbols as keys in this object.
  * **Example**
Basic usage:
js```
const s = Symbol()

export default {
  provide: {
    foo: 'foo',
    [s]: 'bar'
  }
}
```

Using a function to provide per-component state:
js```
export default {
  data() {
    return {
      msg: 'foo'
    }
  }
  provide() {
    return {
      msg: this.msg
    }
  }
}
```

Note in the above example, the provided `msg` will NOT be reactive. See [Working with Reactivity](https://vuejs.org/guide/components/provide-inject#working-with-reactivity) for more details.
  * **See also** [Provide / Inject](https://vuejs.org/guide/components/provide-inject)


## inject [​](https://vuejs.org/api/options-composition.html#inject)
Declare properties to inject into the current component by locating them from ancestor providers.
  * **Type**
ts```
interface ComponentOptions {
  inject?: ArrayInjectOptions | ObjectInjectOptions
}

type ArrayInjectOptions = string[]

type ObjectInjectOptions = {
  [key: string | symbol]:
    | string
    | symbol
    | { from?: string | symbol; default?: any }
}
```

  * **Details**
The `inject` option should be either:
    * An array of strings, or
    * An object where the keys are the local binding name and the value is either:
      * The key (string or Symbol) to search for in available injections, or
      * An object where:
        * The `from` property is the key (string or Symbol) to search for in available injections, and
        * The `default` property is used as fallback value. Similar to props default values, a factory function is needed for object types to avoid value sharing between multiple component instances.
An injected property will be `undefined` if neither a matching property nor a default value was provided.
Note that injected bindings are NOT reactive. This is intentional. However, if the injected value is a reactive object, properties on that object do remain reactive. See [Working with Reactivity](https://vuejs.org/guide/components/provide-inject#working-with-reactivity) for more details.
  * **Example**
Basic usage:
js```
export default {
  inject: ['foo'],
  created() {
    console.log(this.foo)
  }
}
```

Using an injected value as the default for a prop:
js```
const Child = {
  inject: ['foo'],
  props: {
    bar: {
      default() {
        return this.foo
      }
    }
  }
}
```

Using an injected value as data entry:
js```
const Child = {
  inject: ['foo'],
  data() {
    return {
      bar: this.foo
    }
  }
}
```

Injections can be optional with default value:
js```
const Child = {
  inject: {
    foo: { default: 'foo' }
  }
}
```

If it needs to be injected from a property with a different name, use `from` to denote the source property:
js```
const Child = {
  inject: {
    foo: {
      from: 'bar',
      default: 'foo'
    }
  }
}
```

Similar to prop defaults, you need to use a factory function for non-primitive values:
js```
const Child = {
  inject: {
    foo: {
      from: 'bar',
      default: () => [1, 2, 3]
    }
  }
}
```

  * **See also** [Provide / Inject](https://vuejs.org/guide/components/provide-inject)


## mixins [​](https://vuejs.org/api/options-composition.html#mixins)
An array of option objects to be mixed into the current component.
  * **Type**
ts```
interface ComponentOptions {
  mixins?: ComponentOptions[]
}
```

  * **Details**
The `mixins` option accepts an array of mixin objects. These mixin objects can contain instance options like normal instance objects, and they will be merged against the eventual options using the certain option merging logic. For example, if your mixin contains a `created` hook and the component itself also has one, both functions will be called.
Mixin hooks are called in the order they are provided, and called before the component's own hooks.
No Longer Recommended
In Vue 2, mixins were the primary mechanism for creating reusable chunks of component logic. While mixins continue to be supported in Vue 3, [Composable functions using Composition API](https://vuejs.org/guide/reusability/composables) is now the preferred approach for code reuse between components.
  * **Example**
js```
const mixin = {
  created() {
    console.log(1)
  }
}

createApp({
  created() {
    console.log(2)
  },
  mixins: [mixin]
})

// => 1
// => 2
```



## extends [​](https://vuejs.org/api/options-composition.html#extends)
A "base class" component to extend from.
  * **Type**
ts```
interface ComponentOptions {
  extends?: ComponentOptions
}
```

  * **Details**
Allows one component to extend another, inheriting its component options.
From an implementation perspective, `extends` is almost identical to `mixins`. The component specified by `extends` will be treated as though it were the first mixin.
However, `extends` and `mixins` express different intents. The `mixins` option is primarily used to compose chunks of functionality, whereas `extends` is primarily concerned with inheritance.
As with `mixins`, any options (except for `setup()`) will be merged using the relevant merge strategy.
  * **Example**
js```
const CompA = { ... }

const CompB = {
  extends: CompA,
  ...
}
```

Not Recommended for Composition API
`extends` is designed for Options API and does not handle the merging of the `setup()` hook.
In Composition API, the preferred mental model for logic reuse is "compose" over "inheritance". If you have logic from a component that needs to be reused in another one, consider extracting the relevant logic into a [Composable](https://vuejs.org/guide/reusability/composables#composables).
If you still intend to "extend" a component using Composition API, you can call the base component's `setup()` in the extending component's `setup()`:
js```
import Base from './Base.js'
export default {
  extends: Base,
  setup(props, ctx) {
    return {
      ...Base.setup(props, ctx),
      // local bindings
    }
  }
}
```



[Options: Lifecycle](https://vuejs.org/api/options-lifecycle)[Next Options: Misc](https://vuejs.org/api/options-misc)
Options: Composition has loaded
