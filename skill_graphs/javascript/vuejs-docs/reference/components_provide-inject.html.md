[Skip to content](https://vuejs.org/guide/components/provide-inject.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/guide/components/provide-inject)
[日本語 ](https://ja.vuejs.org/guide/components/provide-inject)
[Українська ](https://ua.vuejs.org/guide/components/provide-inject)
[Français ](https://fr.vuejs.org/guide/components/provide-inject)
[한국어 ](https://ko.vuejs.org/guide/components/provide-inject)
[Português ](https://pt.vuejs.org/guide/components/provide-inject)
[বাংলা ](https://bn.vuejs.org/guide/components/provide-inject)
[Italiano ](https://it.vuejs.org/guide/components/provide-inject)
[فارسی ](https://fa.vuejs.org/guide/components/provide-inject)
[Русский ](https://ru.vuejs.org/guide/components/provide-inject)
[Čeština ](https://cs.vuejs.org/guide/components/provide-inject)
[繁體中文 ](https://zh-hk.vuejs.org/guide/components/provide-inject)
[Polski ](https://pl.vuejs.org/guide/components/provide-inject)
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
  * [Prop Drilling](https://vuejs.org/guide/components/provide-inject.html#prop-drilling)
  * [Provide](https://vuejs.org/guide/components/provide-inject.html#provide)
  * [App-level Provide](https://vuejs.org/guide/components/provide-inject.html#app-level-provide)
  * [Inject](https://vuejs.org/guide/components/provide-inject.html#inject)
  * [Working with Reactivity](https://vuejs.org/guide/components/provide-inject.html#working-with-reactivity)
  * [Working with Symbol Keys](https://vuejs.org/guide/components/provide-inject.html#working-with-symbol-keys)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Provide / Inject [​](https://vuejs.org/guide/components/provide-inject.html#provide-inject)
> This page assumes you've already read the [Components Basics](https://vuejs.org/guide/essentials/component-basics). Read that first if you are new to components.
## Prop Drilling [​](https://vuejs.org/guide/components/provide-inject.html#prop-drilling)
Usually, when we need to pass data from the parent to a child component, we use [props](https://vuejs.org/guide/components/props). However, imagine the case where we have a large component tree, and a deeply nested component needs something from a distant ancestor component. With only props, we would have to pass the same prop across the entire parent chain:
![prop drilling diagram](https://vuejs.org/assets/prop-drilling.XJXa8UE-.png)
Notice although the `<Footer>` component may not care about these props at all, it still needs to declare and pass them along just so `<DeepChild>` can access them. If there is a longer parent chain, more components would be affected along the way. This is called "props drilling" and definitely isn't fun to deal with.
We can solve props drilling with `provide` and `inject`. A parent component can serve as a **dependency provider** for all its descendants. Any component in the descendant tree, regardless of how deep it is, can **inject** dependencies provided by components up in its parent chain.
![Provide/inject scheme](https://vuejs.org/assets/provide-inject.C0gAIfVn.png)
## Provide [​](https://vuejs.org/guide/components/provide-inject.html#provide)
To provide data to a component's descendants, use the [`provide()`](https://vuejs.org/api/composition-api-dependency-injection#provide) function:
vue```
<script setup>
import { provide } from 'vue'

provide(/* key */ 'message', /* value */ 'hello!')
</script>
```

If not using `<script setup>`, make sure `provide()` is called synchronously inside `setup()`:
js```
import { provide } from 'vue'

export default {
  setup() {
    provide(/* key */ 'message', /* value */ 'hello!')
  }
}
```

The `provide()` function accepts two arguments. The first argument is called the **injection key** , which can be a string or a `Symbol`. The injection key is used by descendant components to lookup the desired value to inject. A single component can call `provide()` multiple times with different injection keys to provide different values.
The second argument is the provided value. The value can be of any type, including reactive state such as refs:
js```
import { ref, provide } from 'vue'

const count = ref(0)
provide('key', count)
```

Providing reactive values allows the descendant components using the provided value to establish a reactive connection to the provider component.
To provide data to a component's descendants, use the [`provide`](https://vuejs.org/api/options-composition#provide) option:
js```
export default {
  provide: {
    message: 'hello!'
  }
}
```

For each property in the `provide` object, the key is used by child components to locate the correct value to inject, while the value is what ends up being injected.
If we need to provide per-instance state, for example data declared via the `data()`, then `provide` must use a function value:
js```
export default {
  data() {
    return {
      message: 'hello!'
    }
  },
  provide() {
    // use function syntax so that we can access `this`
    return {
      message: this.message
    }
  }
}
```

However, do note this does **not** make the injection reactive. We will discuss [making injections reactive](https://vuejs.org/guide/components/provide-inject.html#working-with-reactivity) below.
## App-level Provide [​](https://vuejs.org/guide/components/provide-inject.html#app-level-provide)
In addition to providing data in a component, we can also provide at the app level:
js```
import { createApp } from 'vue'

const app = createApp({})

app.provide(/* key */ 'message', /* value */ 'hello!')
```

App-level provides are available to all components rendered in the app. This is especially useful when writing [plugins](https://vuejs.org/guide/reusability/plugins), as plugins typically wouldn't be able to provide values using components.
## Inject [​](https://vuejs.org/guide/components/provide-inject.html#inject)
To inject data provided by an ancestor component, use the [`inject()`](https://vuejs.org/api/composition-api-dependency-injection#inject) function:
vue```
<script setup>
import { inject } from 'vue'

const message = inject('message')
</script>
```

If multiple parents provide data with the same key, inject will resolve to the value from the closest parent in component's parent chain.
If the provided value is a ref, it will be injected as-is and will **not** be automatically unwrapped. This allows the injector component to retain the reactivity connection to the provider component.
[Full provide + inject Example with Reactivity](https://play.vuejs.org/#eNqFUUFugzAQ/MrKF1IpxfeIVKp66Kk/8MWFDXYFtmUbpArx967BhURRU9/WOzO7MzuxV+fKcUB2YlWovXYRAsbBvQije2d9hAk8Xo7gvB11gzDDxdseCuIUG+ZN6a7JjZIvVRIlgDCcw+d3pmvTglz1okJ499I0C3qB1dJQT9YRooVaSdNiACWdQ5OICj2WwtTWhAg9hiBbhHNSOxQKu84WT8LkNQ9FBhTHXyg1K75aJHNUROxdJyNSBVBp44YI43NvG+zOgmWWYGt7dcipqPhGZEe2ef07wN3lltD+lWN6tNkV/37+rdKjK2rzhRTt7f3u41xhe37/xJZGAL2PLECXa9NKdD/a6QTTtGnP88LgiXJtYv4BaLHhvg==)
Again, if not using `<script setup>`, `inject()` should only be called synchronously inside `setup()`:
js```
import { inject } from 'vue'

export default {
  setup() {
    const message = inject('message')
    return { message }
  }
}
```

To inject data provided by an ancestor component, use the [`inject`](https://vuejs.org/api/options-composition#inject) option:
js```
export default {
  inject: ['message'],
  created() {
    console.log(this.message) // injected value
  }
}
```

Injections are resolved **before** the component's own state, so you can access injected properties in `data()`:
js```
export default {
  inject: ['message'],
  data() {
    return {
      // initial data based on injected value
      fullMessage: this.message
    }
  }
}
```

If multiple parents provide data with the same key, inject will resolve to the value from the closest parent in component's parent chain.
[Full provide + inject example](https://play.vuejs.org/#eNqNkcFqwzAQRH9l0EUthOhuRKH00FO/oO7B2JtERZaEvA4F43+vZCdOTAIJCImRdpi32kG8h7A99iQKobs6msBvpTNt8JHxcTC2wS76FnKrJpVLZelKR39TSUO7qreMoXRA7ZPPkeOuwHByj5v8EqI/moZeXudCIBL30Z0V0FLXVXsqIA9krU8R+XbMR9rS0mqhS4KpDbZiSgrQc5JKQqvlRWzEQnyvuc9YuWbd4eXq+TZn0IvzOeKr8FvsNcaK/R6Ocb9Uc4FvefpE+fMwP0wH8DU7wB77nIo6x6a2hvNEME5D0CpbrjnHf+8excI=)
### Injection Aliasing [​](https://vuejs.org/guide/components/provide-inject.html#injection-aliasing)
When using the array syntax for `inject`, the injected properties are exposed on the component instance using the same key. In the example above, the property was provided under the key `"message"`, and injected as `this.message`. The local key is the same as the injection key.
If we want to inject the property using a different local key, we need to use the object syntax for the `inject` option:
js```
export default {
  inject: {
    /* local key */ localMessage: {
      from: /* injection key */ 'message'
    }
  }
}
```

Here, the component will locate a property provided with the key `"message"`, and then expose it as `this.localMessage`.
### Injection Default Values [​](https://vuejs.org/guide/components/provide-inject.html#injection-default-values)
By default, `inject` assumes that the injected key is provided somewhere in the parent chain. In the case where the key is not provided, there will be a runtime warning.
If we want to make an injected property work with optional providers, we need to declare a default value, similar to props:
js```
// `value` will be "default value"
// if no data matching "message" was provided
const value = inject('message', 'default value')
```

In some cases, the default value may need to be created by calling a function or instantiating a new class. To avoid unnecessary computation or side effects in case the optional value is not used, we can use a factory function for creating the default value:
js```
const value = inject('key', () => new ExpensiveClass(), true)
```

The third parameter indicates the default value should be treated as a factory function.
js```
export default {
  // object syntax is required
  // when declaring default values for injections
  inject: {
    message: {
      from: 'message', // this is optional if using the same key for injection
      default: 'default value'
    },
    user: {
      // use a factory function for non-primitive values that are expensive
      // to create, or ones that should be unique per component instance.
      default: () => ({ name: 'John' })
    }
  }
}
```

## Working with Reactivity [​](https://vuejs.org/guide/components/provide-inject.html#working-with-reactivity)
When using reactive provide / inject values, **it is recommended to keep any mutations to reactive state inside of the _provider_ whenever possible**. This ensures that the provided state and its possible mutations are co-located in the same component, making it easier to maintain in the future.
There may be times when we need to update the data from an injector component. In such cases, we recommend providing a function that is responsible for mutating the state:
vue```
<!-- inside provider component -->
<script setup>
import { provide, ref } from 'vue'

const location = ref('North Pole')

function updateLocation() {
  location.value = 'South Pole'
}

provide('location', {
  location,
  updateLocation
})
</script>
```

vue```
<!-- in injector component -->
<script setup>
import { inject } from 'vue'

const { location, updateLocation } = inject('location')
</script>

<template>
  <button @click="updateLocation">{{ location }}</button>
</template>
```

Finally, you can wrap the provided value with [`readonly()`](https://vuejs.org/api/reactivity-core#readonly) if you want to ensure that the data passed through `provide` cannot be mutated by the injector component.
vue```
<script setup>
import { ref, provide, readonly } from 'vue'

const count = ref(0)
provide('read-only-count', readonly(count))
</script>
```

In order to make injections reactively linked to the provider, we need to provide a computed property using the [computed()](https://vuejs.org/api/reactivity-core#computed) function:
js```
import { computed } from 'vue'

export default {
  data() {
    return {
      message: 'hello!'
    }
  },
  provide() {
    return {
      // explicitly provide a computed property
      message: computed(() => this.message)
    }
  }
}
```

[Full provide + inject Example with Reactivity](https://play.vuejs.org/#eNqNUctqwzAQ/JVFFyeQxnfjBEoPPfULqh6EtYlV9EKWTcH43ytZtmPTQA0CsdqZ2dlRT16tPXctkoKUTeWE9VeqhbLGeXirheRwc0ZBds7HKkKzBdBDZZRtPXIYJlzqU40/I4LjjbUyIKmGEWw0at8UgZrUh1PscObZ4ZhQAA596/RcAShsGnbHArIapTRBP74O8Up060wnOO5QmP0eAvZyBV+L5jw1j2tZqsMp8yWRUHhUVjKPoQIohQ460L0ow1FeKJlEKEnttFweijJfiORElhCf5f3umObb0B9PU/I7kk17PJj7FloN/2t7a2Pj/Zkdob+x8gV8ZlMs2de/8+14AXwkBngD9zgVqjg2rNXPvwjD+EdlHilrn8MvtvD1+Q==)
The `computed()` function is typically used in Composition API components, but can also be used to complement certain use cases in Options API. You can learn more about its usage by reading the [Reactivity Fundamentals](https://vuejs.org/guide/essentials/reactivity-fundamentals) and [Computed Properties](https://vuejs.org/guide/essentials/computed) with the API Preference set to Composition API.
## Working with Symbol Keys [​](https://vuejs.org/guide/components/provide-inject.html#working-with-symbol-keys)
So far, we have been using string injection keys in the examples. If you are working in a large application with many dependency providers, or you are authoring components that are going to be used by other developers, it is best to use
It's recommended to export the Symbols in a dedicated file:
keys.js
js```
export const myInjectionKey = Symbol()
```

js```
// in provider component
import { provide } from 'vue'
import { myInjectionKey } from './keys.js'

provide(myInjectionKey, {
  /* data to provide */
})
```

js```
// in injector component
import { inject } from 'vue'
import { myInjectionKey } from './keys.js'

const injected = inject(myInjectionKey)
```

See also: [Typing Provide / Inject](https://vuejs.org/guide/typescript/composition-api#typing-provide-inject)
js```
// in provider component
import { myInjectionKey } from './keys.js'

export default {
  provide() {
    return {
      [myInjectionKey]: {
        /* data to provide */
      }
    }
  }
}
```

js```
// in injector component
import { myInjectionKey } from './keys.js'

export default {
  inject: {
    injected: { from: myInjectionKey }
  }
}
```

[Slots](https://vuejs.org/guide/components/slots)[Next Async Components](https://vuejs.org/guide/components/async)
Provide / Inject has loaded
