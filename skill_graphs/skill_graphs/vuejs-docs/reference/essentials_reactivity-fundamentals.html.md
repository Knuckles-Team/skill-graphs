[Skip to content](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/guide/essentials/reactivity-fundamentals)
[日本語 ](https://ja.vuejs.org/guide/essentials/reactivity-fundamentals)
[Українська ](https://ua.vuejs.org/guide/essentials/reactivity-fundamentals)
[Français ](https://fr.vuejs.org/guide/essentials/reactivity-fundamentals)
[한국어 ](https://ko.vuejs.org/guide/essentials/reactivity-fundamentals)
[Português ](https://pt.vuejs.org/guide/essentials/reactivity-fundamentals)
[বাংলা ](https://bn.vuejs.org/guide/essentials/reactivity-fundamentals)
[Italiano ](https://it.vuejs.org/guide/essentials/reactivity-fundamentals)
[فارسی ](https://fa.vuejs.org/guide/essentials/reactivity-fundamentals)
[Русский ](https://ru.vuejs.org/guide/essentials/reactivity-fundamentals)
[Čeština ](https://cs.vuejs.org/guide/essentials/reactivity-fundamentals)
[繁體中文 ](https://zh-hk.vuejs.org/guide/essentials/reactivity-fundamentals)
[Polski ](https://pl.vuejs.org/guide/essentials/reactivity-fundamentals)
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
  * [Declaring Reactive State](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#declaring-reactive-state)
    * [Reactive Proxy vs. Original](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#reactive-proxy-vs-original)
  * [Declaring Reactive State](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#declaring-reactive-state-1)
    * [ref()](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#ref)
    * [<script setup>](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#script-setup)
    * [Why Refs?](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#why-refs)
  * [Declaring Methods](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#declaring-methods)
    * [Deep Reactivity](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#deep-reactivity)
    * [DOM Update Timing](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#dom-update-timing)
  * [reactive()](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#reactive)
    * [Reactive Proxy vs. Original](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#reactive-proxy-vs-original-1)
    * [Limitations of reactive()](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#limitations-of-reactive)
  * [Additional Ref Unwrapping Details](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#additional-ref-unwrapping-details)
    * [As Reactive Object Property](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#ref-unwrapping-as-reactive-object-property)
    * [Caveat in Arrays and Collections](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#caveat-in-arrays-and-collections)
    * [Caveat when Unwrapping in Templates](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#caveat-when-unwrapping-in-templates)
    * [Stateful Methods](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#stateful-methods)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Reactivity Fundamentals [​](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#reactivity-fundamentals)
API Preference
This page and many other chapters later in the guide contain different content for the Options API and the Composition API. Your current preference is Options APIComposition API. You can toggle between the API styles using the "API Preference" switches at the top of the left sidebar.
## Declaring Reactive State [​](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#declaring-reactive-state)
With the Options API, we use the `data` option to declare reactive state of a component. The option value should be a function that returns an object. Vue will call the function when creating a new component instance, and wrap the returned object in its reactivity system. Any top-level properties of this object are proxied on the component instance (`this` in methods and lifecycle hooks):
js```
export default {
  data() {
    return {
      count: 1
    }
  },

  // `mounted` is a lifecycle hook which we will explain later
  mounted() {
    // `this` refers to the component instance.
    console.log(this.count) // => 1

    // data can be mutated as well
    this.count = 2
  }
}
```

[Try it in the Playground](https://play.vuejs.org/#eNpFUNFqhDAQ/JXBpzsoHu2j3B2U/oYPpnGtoetGkrW2iP/eRFsPApthd2Zndilex7H8mqioimu0wY16r4W+Rx8ULXVmYsVSC9AaNafz/gcC6RTkHwHWT6IVnne85rI+1ZLr5YJmyG1qG7gIA3Yd2R/LhN77T8y9sz1mwuyYkXazcQI2SiHz/7iP3VlQexeb5KKjEKEe2lPyMIxeSBROohqxVO4E6yV6ppL9xykTy83tOQvd7tnzoZtDwhrBO2GYNFloYWLyxrzPPOi44WWLWUt618txvASUhhRCKSHgbZt2scKy7HfCujGOqWL9BVfOgyI=)
These instance properties are only added when the instance is first created, so you need to ensure they are all present in the object returned by the `data` function. Where necessary, use `null`, `undefined` or some other placeholder value for properties where the desired value isn't yet available.
It is possible to add a new property directly to `this` without including it in `data`. However, properties added this way will not be able to trigger reactive updates.
Vue uses a `$` prefix when exposing its own built-in APIs via the component instance. It also reserves the prefix `_` for internal properties. You should avoid using names for top-level `data` properties that start with either of these characters.
### Reactive Proxy vs. Original [​](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#reactive-proxy-vs-original)
In Vue 3, data is made reactive by leveraging
js```
export default {
  data() {
    return {
      someObject: {}
    }
  },
  mounted() {
    const newObject = {}
    this.someObject = newObject

    console.log(newObject === this.someObject) // false
  }
}
```

When you access `this.someObject` after assigning it, the value is a reactive proxy of the original `newObject`. **Unlike in Vue 2, the original`newObject` is left intact and will not be made reactive: make sure to always access reactive state as a property of `this`.**
## Declaring Reactive State [​](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#declaring-reactive-state-1)
###  `ref()` [​](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#ref)
In Composition API, the recommended way to declare reactive state is using the [`ref()`](https://vuejs.org/api/reactivity-core#ref) function:
js```
import { ref } from 'vue'

const count = ref(0)
```

`ref()` takes the argument and returns it wrapped within a ref object with a `.value` property:
js```
const count = ref(0)

console.log(count) // { value: 0 }
console.log(count.value) // 0

count.value++
console.log(count.value) // 1
```

> See also: [Typing Refs](https://vuejs.org/guide/typescript/composition-api#typing-ref)
To access refs in a component's template, declare and return them from a component's `setup()` function:
js```
import { ref } from 'vue'

export default {
  // `setup` is a special hook dedicated for the Composition API.
  setup() {
    const count = ref(0)

    // expose the ref to the template
    return {
      count
    }
  }
}
```

template```
<div>{{ count }}</div>
```

Notice that we did **not** need to append `.value` when using the ref in the template. For convenience, refs are automatically unwrapped when used inside templates (with a few [caveats](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#caveat-when-unwrapping-in-templates)).
You can also mutate a ref directly in event handlers:
template```
<button @click="count++">
  {{ count }}
</button>
```

For more complex logic, we can declare functions that mutate refs in the same scope and expose them as methods alongside the state:
js```
import { ref } from 'vue'

export default {
  setup() {
    const count = ref(0)

    function increment() {
      // .value is needed in JavaScript
      count.value++
    }

    // don't forget to expose the function as well.
    return {
      count,
      increment
    }
  }
}
```

Exposed methods can then be used as event handlers:
template```
<button @click="increment">
  {{ count }}
</button>
```

Here's the example live on
###  `<script setup>` [​](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#script-setup)
Manually exposing state and methods via `setup()` can be verbose. Luckily, it can be avoided when using [Single-File Components (SFCs)](https://vuejs.org/guide/scaling-up/sfc). We can simplify the usage with `<script setup>`:
vue```
<script setup>
import { ref } from 'vue'

const count = ref(0)

function increment() {
  count.value++
}
</script>

<template>
  <button @click="increment">
    {{ count }}
  </button>
</template>
```

[Try it in the Playground](https://play.vuejs.org/#eNo9jUEKgzAQRa8yZKMiaNcllvYe2dgwQqiZhDhxE3L3jrW4/DPvv1/UK8Zhz6juSm82uciwIef4MOR8DImhQMIFKiwpeGgEbQwZsoE2BhsyMUwH0d66475ksuwCgSOb0CNx20ExBCc77POase8NVUN6PBdlSwKjj+vMKAlAvzOzWJ52dfYzGXXpjPoBAKX856uopDGeFfnq8XKp+gWq4FAi)
Top-level imports, variables and functions declared in `<script setup>` are automatically usable in the template of the same component. Think of the template as a JavaScript function declared in the same scope - it naturally has access to everything declared alongside it.
TIP
For the rest of the guide, we will be primarily using SFC + `<script setup>` syntax for the Composition API code examples, as that is the most common usage for Vue developers.
If you are not using SFC, you can still use Composition API with the [`setup()`](https://vuejs.org/api/composition-api-setup) option.
### Why Refs? [​](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#why-refs)
You might be wondering why we need refs with the `.value` instead of plain variables. To explain that, we will need to briefly discuss how Vue's reactivity system works.
When you use a ref in a template, and change the ref's value later, Vue automatically detects the change and updates the DOM accordingly. This is made possible with a dependency-tracking based reactivity system. When a component is rendered for the first time, Vue **tracks** every ref that was used during the render. Later on, when a ref is mutated, it will **trigger** a re-render for components that are tracking it.
In standard JavaScript, there is no way to detect the access or mutation of plain variables. However, we can intercept the get and set operations of an object's properties using getter and setter methods.
The `.value` property gives Vue the opportunity to detect when a ref has been accessed or mutated. Under the hood, Vue performs the tracking in its getter, and performs triggering in its setter. Conceptually, you can think of a ref as an object that looks like this:
js```
// pseudo code, not actual implementation
const myRef = {
  _value: 0,
  get value() {
    track()
    return this._value
  },
  set value(newValue) {
    this._value = newValue
    trigger()
  }
}
```

Another nice trait of refs is that unlike plain variables, you can pass refs into functions while retaining access to the latest value and the reactivity connection. This is particularly useful when refactoring complex logic into reusable code.
The reactivity system is discussed in more details in the [Reactivity in Depth](https://vuejs.org/guide/extras/reactivity-in-depth) section.
## Declaring Methods [​](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#declaring-methods)
To add methods to a component instance we use the `methods` option. This should be an object containing the desired methods:
js```
export default {
  data() {
    return {
      count: 0
    }
  },
  methods: {
    increment() {
      this.count++
    }
  },
  mounted() {
    // methods can be called in lifecycle hooks, or other methods!
    this.increment()
  }
}
```

Vue automatically binds the `this` value for `methods` so that it always refers to the component instance. This ensures that a method retains the correct `this` value if it's used as an event listener or callback. You should avoid using arrow functions when defining `methods`, as that prevents Vue from binding the appropriate `this` value:
js```
export default {
  methods: {
    increment: () => {
      // BAD: no `this` access here!
    }
  }
}
```

Just like all other properties of the component instance, the `methods` are accessible from within the component's template. Inside a template they are most commonly used as event listeners:
template```
<button @click="increment">{{ count }}</button>
```

[Try it in the Playground](https://play.vuejs.org/#eNplj9EKwyAMRX8l+LSx0e65uLL9hy+dZlTWqtg4BuK/z1baDgZicsPJgUR2d656B2QN45P02lErDH6c9QQKn10YCKIwAKqj7nAsPYBHCt6sCUDaYKiBS8lpLuk8/yNSb9XUrKg20uOIhnYXAPV6qhbF6fRvmOeodn6hfzwLKkx+vN5OyIFwdENHmBMAfwQia+AmBy1fV8E2gWBtjOUASInXBcxLvN4MLH0BCe1i4Q==)
In the example above, the method `increment` will be called when the `<button>` is clicked.
### Deep Reactivity [​](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#deep-reactivity)
In Vue, state is deeply reactive by default. This means you can expect changes to be detected even when you mutate nested objects or arrays:
js```
export default {
  data() {
    return {
      obj: {
        nested: { count: 0 },
        arr: ['foo', 'bar']
      }
    }
  },
  methods: {
    mutateDeeply() {
      // these will work as expected.
      this.obj.nested.count++
      this.obj.arr.push('baz')
    }
  }
}
```

Refs can hold any value type, including deeply nested objects, arrays, or JavaScript built-in data structures like `Map`.
A ref will make its value deeply reactive. This means you can expect changes to be detected even when you mutate nested objects or arrays:
js```
import { ref } from 'vue'

const obj = ref({
  nested: { count: 0 },
  arr: ['foo', 'bar']
})

function mutateDeeply() {
  // these will work as expected.
  obj.value.nested.count++
  obj.value.arr.push('baz')
}
```

Non-primitive values are turned into reactive proxies via [`reactive()`](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#reactive), which is discussed below.
It is also possible to opt-out of deep reactivity with [shallow refs](https://vuejs.org/api/reactivity-advanced#shallowref). For shallow refs, only `.value` access is tracked for reactivity. Shallow refs can be used for optimizing performance by avoiding the observation cost of large objects, or in cases where the inner state is managed by an external library.
Further reading:
  * [Reduce Reactivity Overhead for Large Immutable Structures](https://vuejs.org/guide/best-practices/performance#reduce-reactivity-overhead-for-large-immutable-structures)
  * [Integration with External State Systems](https://vuejs.org/guide/extras/reactivity-in-depth#integration-with-external-state-systems)


### DOM Update Timing [​](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#dom-update-timing)
When you mutate reactive state, the DOM is updated automatically. However, it should be noted that the DOM updates are not applied synchronously. Instead, Vue buffers them until the "next tick" in the update cycle to ensure that each component updates only once no matter how many state changes you have made.
To wait for the DOM update to complete after a state change, you can use the [nextTick()](https://vuejs.org/api/general#nexttick) global API:
js```
import { nextTick } from 'vue'

async function increment() {
  count.value++
  await nextTick()
  // Now the DOM is updated
}
```

js```
import { nextTick } from 'vue'

export default {
  methods: {
    async increment() {
      this.count++
      await nextTick()
      // Now the DOM is updated
    }
  }
}
```

##  `reactive()` [​](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#reactive)
There is another way to declare reactive state, with the `reactive()` API. Unlike a ref which wraps the inner value in a special object, `reactive()` makes an object itself reactive:
js```
import { reactive } from 'vue'

const state = reactive({ count: 0 })
```

> See also: [Typing Reactive](https://vuejs.org/guide/typescript/composition-api#typing-reactive)
Usage in template:
template```
<button @click="state.count++">
  {{ state.count }}
</button>
```

Reactive objects are
`reactive()` converts the object deeply: nested objects are also wrapped with `reactive()` when accessed. It is also called by `ref()` internally when the ref value is an object. Similar to shallow refs, there is also the [`shallowReactive()`](https://vuejs.org/api/reactivity-advanced#shallowreactive) API for opting-out of deep reactivity.
### Reactive Proxy vs. Original [​](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#reactive-proxy-vs-original-1)
It is important to note that the returned value from `reactive()` is a
js```
const raw = {}
const proxy = reactive(raw)

// proxy is NOT equal to the original.
console.log(proxy === raw) // false
```

Only the proxy is reactive - mutating the original object will not trigger updates. Therefore, the best practice when working with Vue's reactivity system is to **exclusively use the proxied versions of your state**.
To ensure consistent access to the proxy, calling `reactive()` on the same object always returns the same proxy, and calling `reactive()` on an existing proxy also returns that same proxy:
js```
// calling reactive() on the same object returns the same proxy
console.log(reactive(raw) === proxy) // true

// calling reactive() on a proxy returns itself
console.log(reactive(proxy) === proxy) // true
```

This rule applies to nested objects as well. Due to deep reactivity, nested objects inside a reactive object are also proxies:
js```
const proxy = reactive({})

const raw = {}
proxy.nested = raw

console.log(proxy.nested === raw) // false
```

### Limitations of `reactive()` [​](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#limitations-of-reactive)
The `reactive()` API has a few limitations:
  1. **Limited value types:** it only works for object types (objects, arrays, and `Map` and `Set`). It cannot hold `string`, `number` or `boolean`.
  2. **Cannot replace entire object:** since Vue's reactivity tracking works over property access, we must always keep the same reference to the reactive object. This means we can't easily "replace" a reactive object because the reactivity connection to the first reference is lost:
js```
let state = reactive({ count: 0 })

// the above reference ({ count: 0 }) is no longer being tracked
// (reactivity connection is lost!)
state = reactive({ count: 1 })
```

  3. **Not destructure-friendly:** when we destructure a reactive object's primitive type property into local variables, or when we pass that property into a function, we will lose the reactivity connection:
js```
const state = reactive({ count: 0 })

// count is disconnected from state.count when destructured.
let { count } = state
// does not affect original state
count++

// the function receives a plain number and
// won't be able to track changes to state.count
// we have to pass the entire object in to retain reactivity
callSomeFunction(state.count)
```



Due to these limitations, we recommend using `ref()` as the primary API for declaring reactive state.
## Additional Ref Unwrapping Details [​](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#additional-ref-unwrapping-details)
### As Reactive Object Property [​](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#ref-unwrapping-as-reactive-object-property)
A ref is automatically unwrapped when accessed or mutated as a property of a reactive object. In other words, it behaves like a normal property:
js```
const count = ref(0)
const state = reactive({
  count
})

console.log(state.count) // 0

state.count = 1
console.log(count.value) // 1
```

If a new ref is assigned to a property linked to an existing ref, it will replace the old ref:
js```
const otherCount = ref(2)

state.count = otherCount
console.log(state.count) // 2
// original ref is now disconnected from state.count
console.log(count.value) // 1
```

Ref unwrapping only happens when nested inside a deep reactive object. It does not apply when it is accessed as a property of a [shallow reactive object](https://vuejs.org/api/reactivity-advanced#shallowreactive).
### Caveat in Arrays and Collections [​](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#caveat-in-arrays-and-collections)
Unlike reactive objects, there is **no** unwrapping performed when the ref is accessed as an element of a reactive array or a native collection type like `Map`:
js```
const books = reactive([ref('Vue 3 Guide')])
// need .value here
console.log(books[0].value)

const map = reactive(new Map([['count', ref(0)]]))
// need .value here
console.log(map.get('count').value)
```

### Caveat when Unwrapping in Templates [​](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#caveat-when-unwrapping-in-templates)
Ref unwrapping in templates only applies if the ref is a top-level property in the template render context.
In the example below, `count` and `object` are top-level properties, but `object.id` is not:
js```
const count = ref(0)
const object = { id: ref(1) }
```

Therefore, this expression works as expected:
template```
{{ count + 1 }}
```

...while this one does **NOT** :
template```
{{ object.id + 1 }}
```

The rendered result will be `[object Object]1` because `object.id` is not unwrapped when evaluating the expression and remains a ref object. To fix this, we can destructure `id` into a top-level property:
js```
const { id } = object
```

template```
{{ id + 1 }}
```

Now the render result will be `2`.
Another thing to note is that a ref does get unwrapped if it is the final evaluated value of a text interpolation (i.e. a `{{ }}` tag), so the following will render `1`:
template```
{{ object.id }}
```

This is just a convenience feature of text interpolation and is equivalent to `{{ object.id.value }}`.
### Stateful Methods [​](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#stateful-methods)
In some cases, we may need to dynamically create a method function, for example creating a debounced event handler:
js```
import { debounce } from 'lodash-es'

export default {
  methods: {
    // Debouncing with Lodash
    click: debounce(function () {
      // ... respond to click ...
    }, 500)
  }
}
```

However, this approach is problematic for components that are reused because a debounced function is **stateful** : it maintains some internal state on the elapsed time. If multiple component instances share the same debounced function, they will interfere with one another.
To keep each component instance's debounced function independent of the others, we can create the debounced version in the `created` lifecycle hook:
js```
export default {
  created() {
    // each instance now has its own copy of debounced handler
    this.debouncedClick = _.debounce(this.click, 500)
  },
  unmounted() {
    // also a good idea to cancel the timer
    // when the component is removed
    this.debouncedClick.cancel()
  },
  methods: {
    click() {
      // ... respond to click ...
    }
  }
}
```

[Template Syntax](https://vuejs.org/guide/essentials/template-syntax)[Next Computed Properties](https://vuejs.org/guide/essentials/computed)
Reactivity Fundamentals has loaded
