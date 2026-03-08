[Skip to content](https://vuejs.org/style-guide/rules-use-with-caution.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/style-guide/rules-use-with-caution)
[日本語 ](https://ja.vuejs.org/style-guide/rules-use-with-caution)
[Українська ](https://ua.vuejs.org/style-guide/rules-use-with-caution)
[Français ](https://fr.vuejs.org/style-guide/rules-use-with-caution)
[한국어 ](https://ko.vuejs.org/style-guide/rules-use-with-caution)
[Português ](https://pt.vuejs.org/style-guide/rules-use-with-caution)
[বাংলা ](https://bn.vuejs.org/style-guide/rules-use-with-caution)
[Italiano ](https://it.vuejs.org/style-guide/rules-use-with-caution)
[فارسی ](https://fa.vuejs.org/style-guide/rules-use-with-caution)
[Русский ](https://ru.vuejs.org/style-guide/rules-use-with-caution)
[Čeština ](https://cs.vuejs.org/style-guide/rules-use-with-caution)
[繁體中文 ](https://zh-hk.vuejs.org/style-guide/rules-use-with-caution)
[Polski ](https://pl.vuejs.org/style-guide/rules-use-with-caution)
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
  * [Element selectors with scoped](https://vuejs.org/style-guide/rules-use-with-caution.html#element-selectors-with-scoped)
  * [Implicit parent-child communication](https://vuejs.org/style-guide/rules-use-with-caution.html#implicit-parent-child-communication)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Priority D Rules: Use with Caution [​](https://vuejs.org/style-guide/rules-use-with-caution.html#priority-d-rules-use-with-caution)
Note
This Vue.js Style Guide is outdated and needs to be reviewed. If you have any questions or suggestions, please
Some features of Vue exist to accommodate rare edge cases or smoother migrations from a legacy code base. When overused however, they can make your code more difficult to maintain or even become a source of bugs. These rules shine a light on potentially risky features, describing when and why they should be avoided.
## Element selectors with `scoped` [​](https://vuejs.org/style-guide/rules-use-with-caution.html#element-selectors-with-scoped)
**Element selectors should be avoided with`scoped`.**
Prefer class selectors over element selectors in `scoped` styles, because large numbers of element selectors are slow.
Detailed Explanation
To scope styles, Vue adds a unique attribute to component elements, such as `data-v-f3f3eg9`. Then selectors are modified so that only matching elements with this attribute are selected (e.g. `button[data-v-f3f3eg9]`).
The problem is that large numbers of element-attribute selectors (e.g. `button[data-v-f3f3eg9]`) will be considerably slower than class-attribute selectors (e.g. `.btn-close[data-v-f3f3eg9]`), so class selectors should be preferred whenever possible.
### Bad
template```
<template>
  <button>×</button>
</template>

<style scoped>
button {
  background-color: red;
}
</style>
```

### Good
template```
<template>
  <button class="btn btn-close">×</button>
</template>

<style scoped>
.btn-close {
  background-color: red;
}
</style>
```

## Implicit parent-child communication [​](https://vuejs.org/style-guide/rules-use-with-caution.html#implicit-parent-child-communication)
**Props and events should be preferred for parent-child component communication, instead of`this.$parent` or mutating props.**
An ideal Vue application is props down, events up. Sticking to this convention makes your components much easier to understand. However, there are edge cases where prop mutation or `this.$parent` can simplify two components that are already deeply coupled.
The problem is, there are also many _simple_ cases where these patterns may offer convenience. Beware: do not be seduced into trading simplicity (being able to understand the flow of your state) for short-term convenience (writing less code).
### Bad
js```
app.component('TodoItem', {
  props: {
    todo: {
      type: Object,
      required: true
    }
  },

  template: '<input v-model="todo.text">'
})
```

js```
app.component('TodoItem', {
  props: {
    todo: {
      type: Object,
      required: true
    }
  },

  methods: {
    removeTodo() {
      this.$parent.todos = this.$parent.todos.filter(
        (todo) => todo.id !== vm.todo.id
      )
    }
  },

  template: `
    <span>
      {{ todo.text }}
      <button @click="removeTodo">
        ×
      </button>
    </span>
  `
})
```

### Good
js```
app.component('TodoItem', {
  props: {
    todo: {
      type: Object,
      required: true
    }
  },

  emits: ['input'],

  template: `
    <input
      :value="todo.text"
      @input="$emit('input', $event.target.value)"
    >
  `
})
```

js```
app.component('TodoItem', {
  props: {
    todo: {
      type: Object,
      required: true
    }
  },

  emits: ['delete'],

  template: `
    <span>
      {{ todo.text }}
      <button @click="$emit('delete')">
        ×
      </button>
    </span>
  `
})
```

### Bad
vue```
<script setup>
defineProps({
  todo: {
    type: Object,
    required: true
  }
})
</script>

<template>
  <input v-model="todo.text" />
</template>
```

vue```
<script setup>
import { getCurrentInstance } from 'vue'

const props = defineProps({
  todo: {
    type: Object,
    required: true
  }
})

const instance = getCurrentInstance()

function removeTodo() {
  const parent = instance.parent
  if (!parent) return

  parent.props.todos = parent.props.todos.filter((todo) => {
    return todo.id !== props.todo.id
  })
}
</script>

<template>
  <span>
    {{ todo.text }}
    <button @click="removeTodo">×</button>
  </span>
</template>
```

### Good
vue```
<script setup>
defineProps({
  todo: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['input'])
</script>

<template>
  <input :value="todo.text" @input="emit('input', $event.target.value)" />
</template>
```

vue```
<script setup>
defineProps({
  todo: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['delete'])
</script>

<template>
  <span>
    {{ todo.text }}
    <button @click="emit('delete')">×</button>
  </span>
</template>
```

[C - Recommended](https://vuejs.org/style-guide/rules-recommended)
Priority D Rules: Use with Caution has loaded
