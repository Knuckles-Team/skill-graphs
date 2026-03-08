[Skip to content](https://vuejs.org/api/options-state.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/api/options-state)
[日本語 ](https://ja.vuejs.org/api/options-state)
[Українська ](https://ua.vuejs.org/api/options-state)
[Français ](https://fr.vuejs.org/api/options-state)
[한국어 ](https://ko.vuejs.org/api/options-state)
[Português ](https://pt.vuejs.org/api/options-state)
[বাংলা ](https://bn.vuejs.org/api/options-state)
[Italiano ](https://it.vuejs.org/api/options-state)
[فارسی ](https://fa.vuejs.org/api/options-state)
[Русский ](https://ru.vuejs.org/api/options-state)
[Čeština ](https://cs.vuejs.org/api/options-state)
[繁體中文 ](https://zh-hk.vuejs.org/api/options-state)
[Polski ](https://pl.vuejs.org/api/options-state)
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
  * [data](https://vuejs.org/api/options-state.html#data)
  * [props](https://vuejs.org/api/options-state.html#props)
  * [computed](https://vuejs.org/api/options-state.html#computed)
  * [methods](https://vuejs.org/api/options-state.html#methods)
  * [watch](https://vuejs.org/api/options-state.html#watch)
  * [emits](https://vuejs.org/api/options-state.html#emits)
  * [expose](https://vuejs.org/api/options-state.html#expose)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Options: State [​](https://vuejs.org/api/options-state.html#options-state)
## data [​](https://vuejs.org/api/options-state.html#data)
A function that returns the initial reactive state for the component instance.
  * **Type**
ts```
interface ComponentOptions {
  data?(
    this: ComponentPublicInstance,
    vm: ComponentPublicInstance
  ): object
}
```

  * **Details**
The function is expected to return a plain JavaScript object, which will be made reactive by Vue. After the instance is created, the reactive data object can be accessed as `this.$data`. The component instance also proxies all the properties found on the data object, so `this.a` will be equivalent to `this.$data.a`.
All top-level data properties must be included in the returned data object. Adding new properties to `this.$data` is possible, but it is **not** recommended. If the desired value of a property is not yet available then an empty value such as `undefined` or `null` should be included as a placeholder to ensure that Vue knows that the property exists.
Properties that start with `_` or `$` will **not** be proxied on the component instance because they may conflict with Vue's internal properties and API methods. You will have to access them as `this.$data._property`.
It is **not** recommended to return objects with their own stateful behavior like browser API objects and prototype properties. The returned object should ideally be a plain object that only represents the state of the component.
  * **Example**
js```
export default {
  data() {
    return { a: 1 }
  },
  created() {
    console.log(this.a) // 1
    console.log(this.$data) // { a: 1 }
  }
}
```

Note that if you use an arrow function with the `data` property, `this` won't be the component's instance, but you can still access the instance as the function's first argument:
js```
data: (vm) => ({ a: vm.myProp })
```

  * **See also** [Reactivity in Depth](https://vuejs.org/guide/extras/reactivity-in-depth)


## props [​](https://vuejs.org/api/options-state.html#props)
Declare the props of a component.
  * **Type**
ts```
interface ComponentOptions {
  props?: ArrayPropsOptions | ObjectPropsOptions
}

type ArrayPropsOptions = string[]

type ObjectPropsOptions = { [key: string]: Prop }

type Prop<T = any> = PropOptions<T> | PropType<T> | null

interface PropOptions<T> {
  type?: PropType<T>
  required?: boolean
  default?: T | ((rawProps: object) => T)
  validator?: (value: unknown, rawProps: object) => boolean
}

type PropType<T> = { new (): T } | { new (): T }[]
```

> Types are simplified for readability.
  * **Details**
In Vue, all component props need to be explicitly declared. Component props can be declared in two forms:
    * Simple form using an array of strings
    * Full form using an object where each property key is the name of the prop, and the value is the prop's type (a constructor function) or advanced options.
With object-based syntax, each prop can further define the following options:
    * **`type`**: Can be one of the following native constructors:`String` , `Number`, `Boolean`, `Array`, `Object`, `Date`, `Function`, `Symbol`, any custom constructor function or an array of those. In development mode, Vue will check if a prop's value matches the declared type, and will throw a warning if it doesn't. See [Prop Validation](https://vuejs.org/guide/components/props#prop-validation) for more details.
Also note that a prop with `Boolean` type affects its value casting behavior in both development and production. See [Boolean Casting](https://vuejs.org/guide/components/props#boolean-casting) for more details.
    * **`default`**: Specifies a default value for the prop when it is not passed by the parent or has`undefined` value. Object or array defaults must be returned using a factory function. The factory function also receives the raw props object as the argument.
    * **`required`**: Defines if the prop is required. In a non-production environment, a console warning will be thrown if this value is truthy and the prop is not passed.
    * **`validator`**: Custom validator function that takes the prop value and props object as arguments. In development mode, a console warning will be thrown if this function returns a falsy value (i.e. the validation fails).
  * **Example**
Simple declaration:
js```
export default {
  props: ['size', 'myMessage']
}
```

Object declaration with validations:
js```
export default {
  props: {
    // type check
    height: Number,
    // type check plus other validations
    age: {
      type: Number,
      default: 0,
      required: true,
      validator: (value) => {
        return value >= 0
      }
    }
  }
}
```

  * **See also**
    * [Guide - Props](https://vuejs.org/guide/components/props)
    * [Guide - Typing Component Props](https://vuejs.org/guide/typescript/options-api#typing-component-props)


## computed [​](https://vuejs.org/api/options-state.html#computed)
Declare computed properties to be exposed on the component instance.
  * **Type**
ts```
interface ComponentOptions {
  computed?: {
    [key: string]: ComputedGetter<any> | WritableComputedOptions<any>
  }
}

type ComputedGetter<T> = (
  this: ComponentPublicInstance,
  vm: ComponentPublicInstance
) => T

type ComputedSetter<T> = (
  this: ComponentPublicInstance,
  value: T
) => void

type WritableComputedOptions<T> = {
  get: ComputedGetter<T>
  set: ComputedSetter<T>
}
```

  * **Details**
The option accepts an object where the key is the name of the computed property, and the value is either a computed getter, or an object with `get` and `set` methods (for writable computed properties).
All getters and setters have their `this` context automatically bound to the component instance.
Note that if you use an arrow function with a computed property, `this` won't point to the component's instance, but you can still access the instance as the function's first argument:
js```
export default {
  computed: {
    aDouble: (vm) => vm.a * 2
  }
}
```

  * **Example**
js```
export default {
  data() {
    return { a: 1 }
  },
  computed: {
    // readonly
    aDouble() {
      return this.a * 2
    },
    // writable
    aPlus: {
      get() {
        return this.a + 1
      },
      set(v) {
        this.a = v - 1
      }
    }
  },
  created() {
    console.log(this.aDouble) // => 2
    console.log(this.aPlus) // => 2

    this.aPlus = 3
    console.log(this.a) // => 2
    console.log(this.aDouble) // => 4
  }
}
```

  * **See also**
    * [Guide - Computed Properties](https://vuejs.org/guide/essentials/computed)
    * [Guide - Typing Computed Properties](https://vuejs.org/guide/typescript/options-api#typing-computed-properties)


## methods [​](https://vuejs.org/api/options-state.html#methods)
Declare methods to be mixed into the component instance.
  * **Type**
ts```
interface ComponentOptions {
  methods?: {
    [key: string]: (this: ComponentPublicInstance, ...args: any[]) => any
  }
}
```

  * **Details**
Declared methods can be directly accessed on the component instance, or used in template expressions. All methods have their `this` context automatically bound to the component instance, even when passed around.
Avoid using arrow functions when declaring methods, as they will not have access to the component instance via `this`.
  * **Example**
js```
export default {
  data() {
    return { a: 1 }
  },
  methods: {
    plus() {
      this.a++
    }
  },
  created() {
    this.plus()
    console.log(this.a) // => 2
  }
}
```

  * **See also** [Event Handling](https://vuejs.org/guide/essentials/event-handling)


## watch [​](https://vuejs.org/api/options-state.html#watch)
Declare watch callbacks to be invoked on data change.
  * **Type**
ts```
interface ComponentOptions {
  watch?: {
    [key: string]: WatchOptionItem | WatchOptionItem[]
  }
}

type WatchOptionItem = string | WatchCallback | ObjectWatchOptionItem

type WatchCallback<T> = (
  value: T,
  oldValue: T,
  onCleanup: (cleanupFn: () => void) => void
) => void

type ObjectWatchOptionItem = {
  handler: WatchCallback | string
  immediate?: boolean // default: false
  deep?: boolean // default: false
  flush?: 'pre' | 'post' | 'sync' // default: 'pre'
  onTrack?: (event: DebuggerEvent) => void
  onTrigger?: (event: DebuggerEvent) => void
}
```

> Types are simplified for readability.
  * **Details**
The `watch` option expects an object where keys are the reactive component instance properties to watch (e.g. properties declared via `data` or `computed`) — and values are the corresponding callbacks. The callback receives the new value and the old value of the watched source.
In addition to a root-level property, the key can also be a simple dot-delimited path, e.g. `a.b.c`. Note that this usage does **not** support complex expressions - only dot-delimited paths are supported. If you need to watch complex data sources, use the imperative [`$watch()`](https://vuejs.org/api/component-instance#watch) API instead.
The value can also be a string of a method name (declared via `methods`), or an object that contains additional options. When using the object syntax, the callback should be declared under the `handler` field. Additional options include:
    * **`immediate`**: trigger the callback immediately on watcher creation. Old value will be`undefined` on the first call.
    * **`deep`**: force deep traversal of the source if it is an object or an array, so that the callback fires on deep mutations. See[Deep Watchers](https://vuejs.org/guide/essentials/watchers#deep-watchers).
    * **`flush`**: adjust the callback's flush timing. See[Callback Flush Timing](https://vuejs.org/guide/essentials/watchers#callback-flush-timing) and [`watchEffect()`](https://vuejs.org/api/reactivity-core#watcheffect).
    * **`onTrack / onTrigger`**: debug the watcher's dependencies. See[Watcher Debugging](https://vuejs.org/guide/extras/reactivity-in-depth#watcher-debugging).
Avoid using arrow functions when declaring watch callbacks as they will not have access to the component instance via `this`.
  * **Example**
js```
export default {
  data() {
    return {
      a: 1,
      b: 2,
      c: {
        d: 4
      },
      e: 5,
      f: 6
    }
  },
  watch: {
    // watching top-level property
    a(val, oldVal) {
      console.log(`new: ${val}, old: ${oldVal}`)
    },
    // string method name
    b: 'someMethod',
    // the callback will be called whenever any of the watched object properties change regardless of their nested depth
    c: {
      handler(val, oldVal) {
        console.log('c changed')
      },
      deep: true
    },
    // watching a single nested property:
    'c.d': function (val, oldVal) {
      // do something
    },
    // the callback will be called immediately after the start of the observation
    e: {
      handler(val, oldVal) {
        console.log('e changed')
      },
      immediate: true
    },
    // you can pass array of callbacks, they will be called one-by-one
    f: [
      'handle1',
      function handle2(val, oldVal) {
        console.log('handle2 triggered')
      },
      {
        handler: function handle3(val, oldVal) {
          console.log('handle3 triggered')
        }
        /* ... */
      }
    ]
  },
  methods: {
    someMethod() {
      console.log('b changed')
    },
    handle1() {
      console.log('handle 1 triggered')
    }
  },
  created() {
    this.a = 3 // => new: 3, old: 1
  }
}
```

  * **See also** [Watchers](https://vuejs.org/guide/essentials/watchers)


## emits [​](https://vuejs.org/api/options-state.html#emits)
Declare the custom events emitted by the component.
  * **Type**
ts```
interface ComponentOptions {
  emits?: ArrayEmitsOptions | ObjectEmitsOptions
}

type ArrayEmitsOptions = string[]

type ObjectEmitsOptions = { [key: string]: EmitValidator | null }

type EmitValidator = (...args: unknown[]) => boolean
```

  * **Details**
Emitted events can be declared in two forms:
    * Simple form using an array of strings
    * Full form using an object where each property key is the name of the event, and the value is either `null` or a validator function.
The validation function will receive the additional arguments passed to the component's `$emit` call. For example, if `this.$emit('foo', 1)` is called, the corresponding validator for `foo` will receive the argument `1`. The validator function should return a boolean to indicate whether the event arguments are valid.
Note that the `emits` option affects which event listeners are considered component event listeners, rather than native DOM event listeners. The listeners for declared events will be removed from the component's `$attrs` object, so they will not be passed through to the component's root element. See [Fallthrough Attributes](https://vuejs.org/guide/components/attrs) for more details.
  * **Example**
Array syntax:
js```
export default {
  emits: ['check'],
  created() {
    this.$emit('check')
  }
}
```

Object syntax:
js```
export default {
  emits: {
    // no validation
    click: null,

    // with validation
    submit: (payload) => {
      if (payload.email && payload.password) {
        return true
      } else {
        console.warn(`Invalid submit event payload!`)
        return false
      }
    }
  }
}
```

  * **See also**
    * [Guide - Fallthrough Attributes](https://vuejs.org/guide/components/attrs)
    * [Guide - Typing Component Emits](https://vuejs.org/guide/typescript/options-api#typing-component-emits)


## expose [​](https://vuejs.org/api/options-state.html#expose)
Declare exposed public properties when the component instance is accessed by a parent via template refs.
  * **Type**
ts```
interface ComponentOptions {
  expose?: string[]
}
```

  * **Details**
By default, a component instance exposes all instance properties to the parent when accessed via `$parent`, `$root`, or template refs. This can be undesirable, since a component most likely has internal state or methods that should be kept private to avoid tight coupling.
The `expose` option expects a list of property name strings. When `expose` is used, only the properties explicitly listed will be exposed on the component's public instance.
`expose` only affects user-defined properties - it does not filter out built-in component instance properties.
  * **Example**
js```
export default {
  // only `publicMethod` will be available on the public instance
  expose: ['publicMethod'],
  methods: {
    publicMethod() {
      // ...
    },
    privateMethod() {
      // ...
    }
  }
}
```



[Helpers](https://vuejs.org/api/composition-api-helpers)[Next Options: Rendering](https://vuejs.org/api/options-rendering)
Options: State has loaded
