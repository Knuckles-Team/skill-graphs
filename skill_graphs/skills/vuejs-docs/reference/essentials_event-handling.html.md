[Skip to content](https://vuejs.org/guide/essentials/event-handling.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/guide/essentials/event-handling)
[日本語 ](https://ja.vuejs.org/guide/essentials/event-handling)
[Українська ](https://ua.vuejs.org/guide/essentials/event-handling)
[Français ](https://fr.vuejs.org/guide/essentials/event-handling)
[한국어 ](https://ko.vuejs.org/guide/essentials/event-handling)
[Português ](https://pt.vuejs.org/guide/essentials/event-handling)
[বাংলা ](https://bn.vuejs.org/guide/essentials/event-handling)
[Italiano ](https://it.vuejs.org/guide/essentials/event-handling)
[فارسی ](https://fa.vuejs.org/guide/essentials/event-handling)
[Русский ](https://ru.vuejs.org/guide/essentials/event-handling)
[Čeština ](https://cs.vuejs.org/guide/essentials/event-handling)
[繁體中文 ](https://zh-hk.vuejs.org/guide/essentials/event-handling)
[Polski ](https://pl.vuejs.org/guide/essentials/event-handling)
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
  * [Listening to Events](https://vuejs.org/guide/essentials/event-handling.html#listening-to-events)
  * [Inline Handlers](https://vuejs.org/guide/essentials/event-handling.html#inline-handlers)
  * [Method Handlers](https://vuejs.org/guide/essentials/event-handling.html#method-handlers)
  * [Calling Methods in Inline Handlers](https://vuejs.org/guide/essentials/event-handling.html#calling-methods-in-inline-handlers)
  * [Accessing Event Argument in Inline Handlers](https://vuejs.org/guide/essentials/event-handling.html#accessing-event-argument-in-inline-handlers)
  * [Event Modifiers](https://vuejs.org/guide/essentials/event-handling.html#event-modifiers)
  * [Key Modifiers](https://vuejs.org/guide/essentials/event-handling.html#key-modifiers)
  * [Mouse Button Modifiers](https://vuejs.org/guide/essentials/event-handling.html#mouse-button-modifiers)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Event Handling [​](https://vuejs.org/guide/essentials/event-handling.html#event-handling)
## Listening to Events [​](https://vuejs.org/guide/essentials/event-handling.html#listening-to-events)
We can use the `v-on` directive, which we typically shorten to the `@` symbol, to listen to DOM events and run some JavaScript when they're triggered. The usage would be `v-on:click="handler"` or with the shortcut, `@click="handler"`.
The handler value can be one of the following:
  1. **Inline handlers:** Inline JavaScript to be executed when the event is triggered (similar to the native `onclick` attribute).
  2. **Method handlers:** A property name or path that points to a method defined on the component.


## Inline Handlers [​](https://vuejs.org/guide/essentials/event-handling.html#inline-handlers)
Inline handlers are typically used in simple cases, for example:
js```
const count = ref(0)
```

js```
data() {
  return {
    count: 0
  }
}
```

template```
<button @click="count++">Add 1</button>
<p>Count is: {{ count }}</p>
```

[Try it in the Playground](https://play.vuejs.org/#eNo9jssKgzAURH/lko0tgrbbEqX+Q5fZaLxiqHmQ3LgJ+fdqFZcD58xMYp1z1RqRvRgP0itHEJCia4VR2llPkMDjBBkmbzUUG1oII4y0JhBIGw2hh2Znbo+7MLw+WjZ/C4TaLT3hnogPkcgaeMtFyW8j2GmXpWBtN47w5PWBHLhrPzPCKfWDXRHmPsCAaOBfgSOkdH3IGUhpDBWv9/e8vsZZ/gFFhFJN)
[Try it in the Playground](https://play.vuejs.org/#eNo9jcEKgzAQRH9lyKlF0PYqqdR/6DGXaLYo1RjiRgrivzepIizLzu7sm1XUzuVLIFEKObe+d1wpS183eYahtw4DY1UWMJr15ZpmxYAnDt7uF0BxOwXL5Evc0kbxlmyxxZLFyY2CaXSDZkqKZROYJ4tnO/Tt56HEgckyJaraGNxlsVt2u6teHeF40s20EDo9oyGy+CPIYF1xULBt4H6kOZeFiwBZnOFi+wH0B1hk)
## Method Handlers [​](https://vuejs.org/guide/essentials/event-handling.html#method-handlers)
The logic for many event handlers will be more complex though, and likely isn't feasible with inline handlers. That's why `v-on` can also accept the name or path of a component method you'd like to call.
For example:
js```
const name = ref('Vue.js')

function greet(event) {
  alert(`Hello ${name.value}!`)
  // `event` is the native DOM event
  if (event) {
    alert(event.target.tagName)
  }
}
```

js```
data() {
  return {
    name: 'Vue.js'
  }
},
methods: {
  greet(event) {
    // `this` inside methods points to the current active instance
    alert(`Hello ${this.name}!`)
    // `event` is the native DOM event
    if (event) {
      alert(event.target.tagName)
    }
  }
}
```

template```
<!-- `greet` is the name of the method defined above -->
<button @click="greet">Greet</button>
```

[Try it in the Playground](https://play.vuejs.org/#eNpVj0FLxDAQhf/KMwjtXtq7dBcFQS/qzVMOrWFao2kSkkkvpf/dJIuCEBgm771vZnbx4H23JRJ3YogqaM+IxMlfpNWrd4GxI9CMA3NwK5psbaSVVjkbGXZaCediaJv3RN1XbE5FnZNVrJ3FEoi4pY0sn7BLC0yGArfjMxnjcLsXQrdNJtFxM+Ys0PcYa2CEjuBPylNYb4THtxdUobj0jH/YX3D963gKC5WyvGZ+xR7S5jf01yPzeblhWr2ZmErHw0dizivfK6PV91mKursUl6dSh/4qZ+vQ/+XE8QODonDi)
[Try it in the Playground](https://play.vuejs.org/#eNplUE1LxDAQ/StjEbYL0t5LXRQEvag3Tz00prNtNE1CMilC6X83SUkRhJDJfLz3Jm8tHo2pFo9FU7SOW2Ho0in8MdoSDHhlXhKsnQIYGLHyvL8BLJK3KmcAis3YwOnDY/XlTnt1i2G7i/eMNOnBNRkwWkQqcUFFByVAXUNPk3A9COXEgBkGRgtFDkgDTQjcWxuAwDiJBeMsMcUxszCJlsr+BaXUcLtGwiqut930579KST1IBd5Aqlgie3p/hdTIk+IK//bMGqleEbMjxjC+BZVDIv0+m9CpcNr6MDgkhLORjDBm1H56Iq3ggUvBv++7IhnUFZfnGNt6b4fRtj5wxfYL9p+Sjw==)
A method handler automatically receives the native DOM Event object that triggers it - in the example above, we are able to access the element dispatching the event via `event.target`.
See also: [Typing Event Handlers](https://vuejs.org/guide/typescript/composition-api#typing-event-handlers)
See also: [Typing Event Handlers](https://vuejs.org/guide/typescript/options-api#typing-event-handlers)
### Method vs. Inline Detection [​](https://vuejs.org/guide/essentials/event-handling.html#method-vs-inline-detection)
The template compiler detects method handlers by checking whether the `v-on` value string is a valid JavaScript identifier or property access path. For example, `foo`, `foo.bar` and `foo['bar']` are treated as method handlers, while `foo()` and `count++` are treated as inline handlers.
## Calling Methods in Inline Handlers [​](https://vuejs.org/guide/essentials/event-handling.html#calling-methods-in-inline-handlers)
Instead of binding directly to a method name, we can also call methods in an inline handler. This allows us to pass the method custom arguments instead of the native event:
js```
function say(message) {
  alert(message)
}
```

js```
methods: {
  say(message) {
    alert(message)
  }
}
```

template```
<button @click="say('hello')">Say hello</button>
<button @click="say('bye')">Say bye</button>
```

[Try it in the Playground](https://play.vuejs.org/#eNp9jTEOwjAMRa8SeSld6I5CBWdg9ZJGBiJSN2ocpKjq3UmpFDGx+Vn//b/ANYTjOxGcQEc7uyAqkqTQI98TW3ETq2jyYaQYzYNatSArZTzNUn/IK7Ludr2IBYTG4I3QRqKHJFJ6LtY7+zojbIXNk7yfmhahv5msvqS7PfnHGjJVp9w/hu7qKKwfEd1NSg==)
[Try it in the Playground](https://play.vuejs.org/#eNptjUEKwjAQRa8yZFO7sfsSi57B7WzGdjTBtA3NVC2ldzehEFwIw8D7vM9f1cX742tmVSsd2sl6aXDgjx8ngY7vNDuBFQeAnsWMXagToQAEWg49h0APLncDAIUcT5LzlKJsqRBfPF3ljQjCvXcknEj0bRYZBzi3zrbPE6o0UBhblKiaKy1grK52J/oA//23IcmNBD8dXeVBtX0BF0pXsg==)
## Accessing Event Argument in Inline Handlers [​](https://vuejs.org/guide/essentials/event-handling.html#accessing-event-argument-in-inline-handlers)
Sometimes we also need to access the original DOM event in an inline handler. You can pass it into a method using the special `$event` variable, or use an inline arrow function:
template```
<!-- using $event special variable -->
<button @click="warn('Form cannot be submitted yet.', $event)">
  Submit
</button>

<!-- using inline arrow function -->
<button @click="(event) => warn('Form cannot be submitted yet.', event)">
  Submit
</button>
```

js```
function warn(message, event) {
  // now we have access to the native event
  if (event) {
    event.preventDefault()
  }
  alert(message)
}
```

js```
methods: {
  warn(message, event) {
    // now we have access to the native event
    if (event) {
      event.preventDefault()
    }
    alert(message)
  }
}
```

## Event Modifiers [​](https://vuejs.org/guide/essentials/event-handling.html#event-modifiers)
It is a very common need to call `event.preventDefault()` or `event.stopPropagation()` inside event handlers. Although we can do this easily inside methods, it would be better if the methods can be purely about data logic rather than having to deal with DOM event details.
To address this problem, Vue provides **event modifiers** for `v-on`. Recall that modifiers are directive postfixes denoted by a dot.
  * `.stop`
  * `.prevent`
  * `.self`
  * `.capture`
  * `.once`
  * `.passive`


template```
<!-- the click event's propagation will be stopped -->
<a @click.stop="doThis"></a>

<!-- the submit event will no longer reload the page -->
<form @submit.prevent="onSubmit"></form>

<!-- modifiers can be chained -->
<a @click.stop.prevent="doThat"></a>

<!-- just the modifier -->
<form @submit.prevent></form>

<!-- only trigger handler if event.target is the element itself -->
<!-- i.e. not from a child element -->
<div @click.self="doThat">...</div>
```

TIP
Order matters when using modifiers because the relevant code is generated in the same order. Therefore using `@click.prevent.self` will prevent **click's default action on the element itself and its children** , while `@click.self.prevent` will only prevent click's default action on the element itself.
The `.capture`, `.once`, and `.passive` modifiers mirror the
template```
<!-- use capture mode when adding the event listener     -->
<!-- i.e. an event targeting an inner element is handled -->
<!-- here before being handled by that element           -->
<div @click.capture="doThis">...</div>

<!-- the click event will be triggered at most once -->
<a @click.once="doThis"></a>

<!-- the scroll event's default behavior (scrolling) will happen -->
<!-- immediately, instead of waiting for `onScroll` to complete  -->
<!-- in case it contains `event.preventDefault()`                -->
<div @scroll.passive="onScroll">...</div>
```

The `.passive` modifier is typically used with touch event listeners for
TIP
Do not use `.passive` and `.prevent` together, because `.passive` already indicates to the browser that you _do not_ intend to prevent the event's default behavior, and you will likely see a warning from the browser if you do so.
## Key Modifiers [​](https://vuejs.org/guide/essentials/event-handling.html#key-modifiers)
When listening for keyboard events, we often need to check for specific keys. Vue allows adding key modifiers for `v-on` or `@` when listening for key events:
template```
<!-- only call `submit` when the `key` is `Enter` -->
<input @keyup.enter="submit" />
```

You can directly use any valid key names exposed via
template```
<input @keyup.page-down="onPageDown" />
```

In the above example, the handler will only be called if `$event.key` is equal to `'PageDown'`.
### Key Aliases [​](https://vuejs.org/guide/essentials/event-handling.html#key-aliases)
Vue provides aliases for the most commonly used keys:
  * `.enter`
  * `.tab`
  * `.delete` (captures both "Delete" and "Backspace" keys)
  * `.esc`
  * `.space`
  * `.up`
  * `.down`
  * `.left`
  * `.right`


### System Modifier Keys [​](https://vuejs.org/guide/essentials/event-handling.html#system-modifier-keys)
You can use the following modifiers to trigger mouse or keyboard event listeners only when the corresponding modifier key is pressed:
  * `.ctrl`
  * `.alt`
  * `.shift`
  * `.meta`


Note
On Macintosh keyboards, meta is the command key (⌘). On Windows keyboards, meta is the Windows key (⊞). On Sun Microsystems keyboards, meta is marked as a solid diamond (◆). On certain keyboards, specifically MIT and Lisp machine keyboards and successors, such as the Knight keyboard, space-cadet keyboard, meta is labeled “META”. On Symbolics keyboards, meta is labeled “META” or “Meta”.
For example:
template```
<!-- Alt + Enter -->
<input @keyup.alt.enter="clear" />

<!-- Ctrl + Click -->
<div @click.ctrl="doSomething">Do something</div>
```

TIP
Note that modifier keys are different from regular keys and when used with `keyup` events, they have to be pressed when the event is emitted. In other words, `keyup.ctrl` will only trigger if you release a key while holding down `ctrl`. It won't trigger if you release the `ctrl` key alone.
###  `.exact` Modifier [​](https://vuejs.org/guide/essentials/event-handling.html#exact-modifier)
The `.exact` modifier allows control of the exact combination of system modifiers needed to trigger an event.
template```
<!-- this will fire even if Alt or Shift is also pressed -->
<button @click.ctrl="onClick">A</button>

<!-- this will only fire when Ctrl and no other keys are pressed -->
<button @click.ctrl.exact="onCtrlClick">A</button>

<!-- this will only fire when no system modifiers are pressed -->
<button @click.exact="onClick">A</button>
```

## Mouse Button Modifiers [​](https://vuejs.org/guide/essentials/event-handling.html#mouse-button-modifiers)
  * `.left`
  * `.right`
  * `.middle`


These modifiers restrict the handler to events triggered by a specific mouse button.
Note, however, that `.left`, `.right`, and `.middle` modifier names are based on the typical right-handed mouse layout, but in fact represent "main", "secondary", and "auxiliary" pointing device event triggers, respectively, and not the actual physical buttons. So that for a left-handed mouse layout the "main" button might physically be the right one but would trigger the `.left` modifier handler. Or a trackpad might trigger the `.left` handler with a one-finger tap, the `.right` handler with a two-finger tap, and the `.middle` handler with a three-finger tap. Similarly, other devices and event sources generating "mouse" events might have trigger modes that are not related to "left" and "right" whatsoever.
[List Rendering](https://vuejs.org/guide/essentials/list)[Next Form Input Bindings](https://vuejs.org/guide/essentials/forms)
Event Handling has loaded
