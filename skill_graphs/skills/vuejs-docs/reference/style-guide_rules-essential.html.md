[Skip to content](https://vuejs.org/style-guide/rules-essential.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/style-guide/rules-essential)
[日本語 ](https://ja.vuejs.org/style-guide/rules-essential)
[Українська ](https://ua.vuejs.org/style-guide/rules-essential)
[Français ](https://fr.vuejs.org/style-guide/rules-essential)
[한국어 ](https://ko.vuejs.org/style-guide/rules-essential)
[Português ](https://pt.vuejs.org/style-guide/rules-essential)
[বাংলা ](https://bn.vuejs.org/style-guide/rules-essential)
[Italiano ](https://it.vuejs.org/style-guide/rules-essential)
[فارسی ](https://fa.vuejs.org/style-guide/rules-essential)
[Русский ](https://ru.vuejs.org/style-guide/rules-essential)
[Čeština ](https://cs.vuejs.org/style-guide/rules-essential)
[繁體中文 ](https://zh-hk.vuejs.org/style-guide/rules-essential)
[Polski ](https://pl.vuejs.org/style-guide/rules-essential)
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
  * [Use multi-word component names](https://vuejs.org/style-guide/rules-essential.html#use-multi-word-component-names)
  * [Use detailed prop definitions](https://vuejs.org/style-guide/rules-essential.html#use-detailed-prop-definitions)
  * [Use keyed v-for](https://vuejs.org/style-guide/rules-essential.html#use-keyed-v-for)
  * [Avoid v-if with v-for](https://vuejs.org/style-guide/rules-essential.html#avoid-v-if-with-v-for)
  * [Use component-scoped styling](https://vuejs.org/style-guide/rules-essential.html#use-component-scoped-styling)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Priority A Rules: Essential [​](https://vuejs.org/style-guide/rules-essential.html#priority-a-rules-essential)
Note
This Vue.js Style Guide is outdated and needs to be reviewed. If you have any questions or suggestions, please
These rules help prevent errors, so learn and abide by them at all costs. Exceptions may exist, but should be very rare and only be made by those with expert knowledge of both JavaScript and Vue.
## Use multi-word component names [​](https://vuejs.org/style-guide/rules-essential.html#use-multi-word-component-names)
User component names should always be multi-word, except for root `App` components. This
### Bad
template```
<!-- in pre-compiled templates -->
<Item />

<!-- in in-DOM templates -->
<item></item>
```

### Good
template```
<!-- in pre-compiled templates -->
<TodoItem />

<!-- in in-DOM templates -->
<todo-item></todo-item>
```

## Use detailed prop definitions [​](https://vuejs.org/style-guide/rules-essential.html#use-detailed-prop-definitions)
In committed code, prop definitions should always be as detailed as possible, specifying at least type(s).
Detailed Explanation
Detailed [prop definitions](https://vuejs.org/guide/components/props#prop-validation) have two advantages:
  * They document the API of the component, so that it's easy to see how the component is meant to be used.
  * In development, Vue will warn you if a component is ever provided incorrectly formatted props, helping you catch potential sources of error.


### Bad
js```
// This is only OK when prototyping
props: ['status']
```

### Good
js```
props: {
  status: String
}
```

js```
// Even better!
props: {
  status: {
    type: String,
    required: true,

    validator: value => {
      return [
        'syncing',
        'synced',
        'version-conflict',
        'error'
      ].includes(value)
    }
  }
}
```

### Bad
js```
// This is only OK when prototyping
const props = defineProps(['status'])
```

### Good
js```
const props = defineProps({
  status: String
})
```

js```
// Even better!

const props = defineProps({
  status: {
    type: String,
    required: true,

    validator: (value) => {
      return ['syncing', 'synced', 'version-conflict', 'error'].includes(
        value
      )
    }
  }
})
```

## Use keyed `v-for` [​](https://vuejs.org/style-guide/rules-essential.html#use-keyed-v-for)
`key` with `v-for` is _always_ required on components, in order to maintain internal component state down the subtree. Even for elements though, it's a good practice to maintain predictable behavior, such as
Detailed Explanation
Let's say you have a list of todos:
js```
data() {
  return {
    todos: [
      {
        id: 1,
        text: 'Learn to use v-for'
      },
      {
        id: 2,
        text: 'Learn to use key'
      }
    ]
  }
}
```

js```
const todos = ref([
  {
    id: 1,
    text: 'Learn to use v-for'
  },
  {
    id: 2,
    text: 'Learn to use key'
  }
])
```

Then you sort them alphabetically. When updating the DOM, Vue will optimize rendering to perform the cheapest DOM mutations possible. That might mean deleting the first todo element, then adding it again at the end of the list.
The problem is, there are cases where it's important not to delete elements that will remain in the DOM. For example, you may want to use `<transition-group>` to animate list sorting, or maintain focus if the rendered element is an `<input>`. In these cases, adding a unique key for each item (e.g. `:key="todo.id"`) will tell Vue how to behave more predictably.
In our experience, it's better to _always_ add a unique key, so that you and your team simply never have to worry about these edge cases. Then in the rare, performance-critical scenarios where object constancy isn't necessary, you can make a conscious exception.
### Bad
template```
<ul>
  <li v-for="todo in todos">
    {{ todo.text }}
  </li>
</ul>
```

### Good
template```
<ul>
  <li
    v-for="todo in todos"
    :key="todo.id"
  >
    {{ todo.text }}
  </li>
</ul>
```

## Avoid `v-if` with `v-for` [​](https://vuejs.org/style-guide/rules-essential.html#avoid-v-if-with-v-for)
**Never use`v-if` on the same element as `v-for`.**
There are two common cases where this can be tempting:
  * To filter items in a list (e.g. `v-for="user in users" v-if="user.isActive"`). In these cases, replace `users` with a new computed property that returns your filtered list (e.g. `activeUsers`).
  * To avoid rendering a list if it should be hidden (e.g. `v-for="user in users" v-if="shouldShowUsers"`). In these cases, move the `v-if` to a container element (e.g. `ul`, `ol`).

Detailed Explanation
When Vue processes directives, `v-if` has a higher priority than `v-for`, so that this template:
template```
<ul>
  <li
    v-for="user in users"
    v-if="user.isActive"
    :key="user.id"
  >
    {{ user.name }}
  </li>
</ul>
```

Will throw an error, because the `v-if` directive will be evaluated first and the iteration variable `user` does not exist at this moment.
This could be fixed by iterating over a computed property instead, like this:
js```
computed: {
  activeUsers() {
    return this.users.filter(user => user.isActive)
  }
}
```

js```
const activeUsers = computed(() => {
  return users.filter((user) => user.isActive)
})
```

template```
<ul>
  <li
    v-for="user in activeUsers"
    :key="user.id"
  >
    {{ user.name }}
  </li>
</ul>
```

Alternatively, we can use a `<template>` tag with `v-for` to wrap the `<li>` element:
template```
<ul>
  <template v-for="user in users" :key="user.id">
    <li v-if="user.isActive">
      {{ user.name }}
    </li>
  </template>
</ul>
```

### Bad
template```
<ul>
  <li
    v-for="user in users"
    v-if="user.isActive"
    :key="user.id"
  >
    {{ user.name }}
  </li>
</ul>
```

### Good
template```
<ul>
  <li
    v-for="user in activeUsers"
    :key="user.id"
  >
    {{ user.name }}
  </li>
</ul>
```

template```
<ul>
  <template v-for="user in users" :key="user.id">
    <li v-if="user.isActive">
      {{ user.name }}
    </li>
  </template>
</ul>
```

## Use component-scoped styling [​](https://vuejs.org/style-guide/rules-essential.html#use-component-scoped-styling)
For applications, styles in a top-level `App` component and in layout components may be global, but all other components should always be scoped.
This is only relevant for [Single-File Components](https://vuejs.org/guide/scaling-up/sfc). It does _not_ require that the [`scoped` attribute](https://vue-loader.vuejs.org/guide/scoped-css.html) be used. Scoping could be through [CSS modules](https://vue-loader.vuejs.org/guide/css-modules.html), a class-based strategy such as
**Component libraries, however, should prefer a class-based strategy instead of using the`scoped` attribute.**
This makes overriding internal styles easier, with human-readable class names that don't have too high specificity, but are still very unlikely to result in a conflict.
Detailed Explanation
If you are developing a large project, working with other developers, or sometimes include 3rd-party HTML/CSS (e.g. from Auth0), consistent scoping will ensure that your styles only apply to the components they are meant for.
Beyond the `scoped` attribute, using unique class names can help ensure that 3rd-party CSS does not apply to your own HTML. For example, many projects use the `button`, `btn`, or `icon` class names, so even if not using a strategy such as BEM, adding an app-specific and/or component-specific prefix (e.g. `ButtonClose-icon`) can provide some protection.
### Bad
template```
<template>
  <button class="btn btn-close">×</button>
</template>

<style>
.btn-close {
  background-color: red;
}
</style>
```

### Good
template```
<template>
  <button class="button button-close">×</button>
</template>

<!-- Using the `scoped` attribute -->
<style scoped>
.button {
  border: none;
  border-radius: 2px;
}

.button-close {
  background-color: red;
}
</style>
```

template```
<template>
  <button :class="[$style.button, $style.buttonClose]">×</button>
</template>

<!-- Using CSS modules -->
<style module>
.button {
  border: none;
  border-radius: 2px;
}

.buttonClose {
  background-color: red;
}
</style>
```

template```
<template>
  <button class="c-Button c-Button--close">×</button>
</template>

<!-- Using the BEM convention -->
<style>
.c-Button {
  border: none;
  border-radius: 2px;
}

.c-Button--close {
  background-color: red;
}
</style>
```

[Overview](https://vuejs.org/style-guide/)[Next B - Strongly Recommended](https://vuejs.org/style-guide/rules-strongly-recommended)
Priority A Rules: Essential has loaded
