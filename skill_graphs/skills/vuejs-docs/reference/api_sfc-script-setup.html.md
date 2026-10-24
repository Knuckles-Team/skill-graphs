[Skip to content](https://vuejs.org/api/sfc-script-setup.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/api/sfc-script-setup)
[日本語 ](https://ja.vuejs.org/api/sfc-script-setup)
[Українська ](https://ua.vuejs.org/api/sfc-script-setup)
[Français ](https://fr.vuejs.org/api/sfc-script-setup)
[한국어 ](https://ko.vuejs.org/api/sfc-script-setup)
[Português ](https://pt.vuejs.org/api/sfc-script-setup)
[বাংলা ](https://bn.vuejs.org/api/sfc-script-setup)
[Italiano ](https://it.vuejs.org/api/sfc-script-setup)
[فارسی ](https://fa.vuejs.org/api/sfc-script-setup)
[Русский ](https://ru.vuejs.org/api/sfc-script-setup)
[Čeština ](https://cs.vuejs.org/api/sfc-script-setup)
[繁體中文 ](https://zh-hk.vuejs.org/api/sfc-script-setup)
[Polski ](https://pl.vuejs.org/api/sfc-script-setup)
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
  * [Basic Syntax](https://vuejs.org/api/sfc-script-setup.html#basic-syntax)
  * [Reactivity](https://vuejs.org/api/sfc-script-setup.html#reactivity)
  * [Using Components](https://vuejs.org/api/sfc-script-setup.html#using-components)
  * [Using Custom Directives](https://vuejs.org/api/sfc-script-setup.html#using-custom-directives)
  * [defineProps() & defineEmits()](https://vuejs.org/api/sfc-script-setup.html#defineprops-defineemits)
  * [defineModel()](https://vuejs.org/api/sfc-script-setup.html#definemodel)
  * [defineExpose()](https://vuejs.org/api/sfc-script-setup.html#defineexpose)
  * [defineOptions()](https://vuejs.org/api/sfc-script-setup.html#defineoptions)
  * [defineSlots()](https://vuejs.org/api/sfc-script-setup.html#defineslots)
  * [useSlots() & useAttrs()](https://vuejs.org/api/sfc-script-setup.html#useslots-useattrs)
  * [Usage alongside normal <script>](https://vuejs.org/api/sfc-script-setup.html#usage-alongside-normal-script)
  * [Top-level await](https://vuejs.org/api/sfc-script-setup.html#top-level-await)
  * [Import Statements](https://vuejs.org/api/sfc-script-setup.html#imports-statements)
  * [Generics](https://vuejs.org/api/sfc-script-setup.html#generics)
  * [Restrictions](https://vuejs.org/api/sfc-script-setup.html#restrictions)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# <script setup> [​](https://vuejs.org/api/sfc-script-setup.html#script-setup)
`<script setup>` is a compile-time syntactic sugar for using Composition API inside Single-File Components (SFCs). It is the recommended syntax if you are using both SFCs and Composition API. It provides a number of advantages over the normal `<script>` syntax:
  * More succinct code with less boilerplate
  * Ability to declare props and emitted events using pure TypeScript
  * Better runtime performance (the template is compiled into a render function in the same scope, without an intermediate proxy)
  * Better IDE type-inference performance (less work for the language server to extract types from code)


## Basic Syntax [​](https://vuejs.org/api/sfc-script-setup.html#basic-syntax)
To opt-in to the syntax, add the `setup` attribute to the `<script>` block:
vue```
<script setup>
console.log('hello script setup')
</script>
```

The code inside is compiled as the content of the component's `setup()` function. This means that unlike normal `<script>`, which only executes once when the component is first imported, code inside `<script setup>` will **execute every time an instance of the component is created**.
### Top-level bindings are exposed to template [​](https://vuejs.org/api/sfc-script-setup.html#top-level-bindings-are-exposed-to-template)
When using `<script setup>`, any top-level bindings (including variables, function declarations, and imports) declared inside `<script setup>` are directly usable in the template:
vue```
<script setup>
// variable
const msg = 'Hello!'

// functions
function log() {
  console.log(msg)
}
</script>

<template>
  <button @click="log">{{ msg }}</button>
</template>
```

Imports are exposed in the same fashion. This means you can directly use an imported helper function in template expressions without having to expose it via the `methods` option:
vue```
<script setup>
import { capitalize } from './helpers'
</script>

<template>
  <div>{{ capitalize('hello') }}</div>
</template>
```

## Reactivity [​](https://vuejs.org/api/sfc-script-setup.html#reactivity)
Reactive state needs to be explicitly created using [Reactivity APIs](https://vuejs.org/api/reactivity-core). Similar to values returned from a `setup()` function, refs are automatically unwrapped when referenced in templates:
vue```
<script setup>
import { ref } from 'vue'

const count = ref(0)
</script>

<template>
  <button @click="count++">{{ count }}</button>
</template>
```

## Using Components [​](https://vuejs.org/api/sfc-script-setup.html#using-components)
Values in the scope of `<script setup>` can also be used directly as custom component tag names:
vue```
<script setup>
import MyComponent from './MyComponent.vue'
</script>

<template>
  <MyComponent />
</template>
```

Think of `MyComponent` as being referenced as a variable. If you have used JSX, the mental model is similar here. The kebab-case equivalent `<my-component>` also works in the template - however PascalCase component tags are strongly recommended for consistency. It also helps differentiating from native custom elements.
### Dynamic Components [​](https://vuejs.org/api/sfc-script-setup.html#dynamic-components)
Since components are referenced as variables instead of registered under string keys, we should use dynamic `:is` binding when using dynamic components inside `<script setup>`:
vue```
<script setup>
import Foo from './Foo.vue'
import Bar from './Bar.vue'
</script>

<template>
  <component :is="Foo" />
  <component :is="someCondition ? Foo : Bar" />
</template>
```

Note how the components can be used as variables in a ternary expression.
### Recursive Components [​](https://vuejs.org/api/sfc-script-setup.html#recursive-components)
An SFC can implicitly refer to itself via its filename. E.g. a file named `FooBar.vue` can refer to itself as `<FooBar/>` in its template.
Note this has lower priority than imported components. If you have a named import that conflicts with the component's inferred name, you can alias the import:
js```
import { FooBar as FooBarChild } from './components'
```

### Namespaced Components [​](https://vuejs.org/api/sfc-script-setup.html#namespaced-components)
You can use component tags with dots like `<Foo.Bar>` to refer to components nested under object properties. This is useful when you import multiple components from a single file:
vue```
<script setup>
import * as Form from './form-components'
</script>

<template>
  <Form.Input>
    <Form.Label>label</Form.Label>
  </Form.Input>
</template>
```

## Using Custom Directives [​](https://vuejs.org/api/sfc-script-setup.html#using-custom-directives)
Globally registered custom directives just work as normal. Local custom directives don't need to be explicitly registered with `<script setup>`, but they must follow the naming scheme `vNameOfDirective`:
vue```
<script setup>
const vMyDirective = {
  beforeMount: (el) => {
    // do something with the element
  }
}
</script>
<template>
  <h1 v-my-directive>This is a Heading</h1>
</template>
```

If you're importing a directive from elsewhere, it can be renamed to fit the required naming scheme:
vue```
<script setup>
import { myDirective as vMyDirective } from './MyDirective.js'
</script>
```

## defineProps() & defineEmits() [​](https://vuejs.org/api/sfc-script-setup.html#defineprops-defineemits)
To declare options like `props` and `emits` with full type inference support, we can use the `defineProps` and `defineEmits` APIs, which are automatically available inside `<script setup>`:
vue```
<script setup>
const props = defineProps({
  foo: String
})

const emit = defineEmits(['change', 'delete'])
// setup code
</script>
```

  * `defineProps` and `defineEmits` are **compiler macros** only usable inside `<script setup>`. They do not need to be imported, and are compiled away when `<script setup>` is processed.
  * `defineProps` accepts the same value as the `props` option, while `defineEmits` accepts the same value as the `emits` option.
  * `defineProps` and `defineEmits` provide proper type inference based on the options passed.
  * The options passed to `defineProps` and `defineEmits` will be hoisted out of setup into module scope. Therefore, the options cannot reference local variables declared in setup scope. Doing so will result in a compile error. However, it _can_ reference imported bindings since they are in the module scope as well.


### Type-only props/emit declarations[​](https://vuejs.org/api/sfc-script-setup.html#type-only-props-emit-declarations)
Props and emits can also be declared using pure-type syntax by passing a literal type argument to `defineProps` or `defineEmits`:
ts```
const props = defineProps<{
  foo: string
  bar?: number
}>()

const emit = defineEmits<{
  (e: 'change', id: number): void
  (e: 'update', value: string): void
}>()

// 3.3+: alternative, more succinct syntax
const emit = defineEmits<{
  change: [id: number] // named tuple syntax
  update: [value: string]
}>()
```

  * `defineProps` or `defineEmits` can only use either runtime declaration OR type declaration. Using both at the same time will result in a compile error.
  * When using type declaration, the equivalent runtime declaration is automatically generated from static analysis to remove the need for double declaration and still ensure correct runtime behavior.
    * In dev mode, the compiler will try to infer corresponding runtime validation from the types. For example here `foo: String` is inferred from the `foo: string` type. Imported types are also resolved, provided TypeScript is installed as a peer dependency.
    * In prod mode, the compiler will generate the array format declaration to reduce bundle size (the props here will be compiled into `['foo', 'bar']`)
  * In version 3.2 and below, the generic type parameter for `defineProps()` were limited to a type literal or a reference to a local interface.
This limitation was resolved in 3.3. The latest version of Vue supports referencing imported and a limited set of complex types in the type parameter position. However, because the type to runtime conversion is still AST-based, some complex types that require actual type analysis, e.g. conditional types, are not supported. You can use conditional types for the type of a single prop, but not the entire props object.


### Reactive Props Destructure [​](https://vuejs.org/api/sfc-script-setup.html#reactive-props-destructure)
In Vue 3.5 and above, variables destructured from the return value of `defineProps` are reactive. Vue's compiler automatically prepends `props.` when code in the same `<script setup>` block accesses variables destructured from `defineProps`:
ts```
const { foo } = defineProps(['foo'])

watchEffect(() => {
  // runs only once before 3.5
  // re-runs when the "foo" prop changes in 3.5+
  console.log(foo)
})
```

The above is compiled to the following equivalent:
js```
const props = defineProps(['foo'])

watchEffect(() => {
  // `foo` transformed to `props.foo` by the compiler
  console.log(props.foo)
})
```

In addition, you can use JavaScript's native default value syntax to declare default values for the props. This is particularly useful when using the type-based props declaration:
ts```
interface Props {
  msg?: string
  labels?: string[]
}

const { msg = 'hello', labels = ['one', 'two'] } = defineProps<Props>()
```

### Default props values when using type declaration [​](https://vuejs.org/api/sfc-script-setup.html#default-props-values-when-using-type-declaration)
In 3.5 and above, default values can be naturally declared when using Reactive Props Destructure. But in 3.4 and below, Reactive Props Destructure is not enabled by default. In order to declare props default values with type-based declaration, the `withDefaults` compiler macro is needed:
ts```
interface Props {
  msg?: string
  labels?: string[]
}

const props = withDefaults(defineProps<Props>(), {
  msg: 'hello',
  labels: () => ['one', 'two']
})
```

This will be compiled to equivalent runtime props `default` options. In addition, the `withDefaults` helper provides type checks for the default values, and ensures the returned `props` type has the optional flags removed for properties that do have default values declared.
INFO
Note that default values for mutable reference types (like arrays or objects) should be wrapped in functions when using `withDefaults` to avoid accidental modification and external side effects. This ensures each component instance gets its own copy of the default value. This is **not** necessary when using default values with destructure.
## defineModel() [​](https://vuejs.org/api/sfc-script-setup.html#definemodel)
  * Only available in 3.4+


This macro can be used to declare a two-way binding prop that can be consumed via `v-model` from the parent component. Example usage is also discussed in the [Component `v-model`](https://vuejs.org/guide/components/v-model) guide.
Under the hood, this macro declares a model prop and a corresponding value update event. If the first argument is a literal string, it will be used as the prop name; Otherwise the prop name will default to `"modelValue"`. In both cases, you can also pass an additional object which can include the prop's options and the model ref's value transform options.
js```
// declares "modelValue" prop, consumed by parent via v-model
const model = defineModel()
// OR: declares "modelValue" prop with options
const model = defineModel({ type: String })

// emits "update:modelValue" when mutated
model.value = 'hello'

// declares "count" prop, consumed by parent via v-model:count
const count = defineModel('count')
// OR: declares "count" prop with options
const count = defineModel('count', { type: Number, default: 0 })

function inc() {
  // emits "update:count" when mutated
  count.value++
}
```

WARNING
If you have a `default` value for `defineModel` prop and you don't provide any value for this prop from the parent component, it can cause a de-synchronization between parent and child components. In the example below, the parent's `myRef` is undefined, but the child's `model` is 1:
Child.vue
vue```
<script setup>
const model = defineModel({ default: 1 })
</script>
```

Parent.vue
vue```
<script setup>
const myRef = ref()
</script>

<template>
  <Child v-model="myRef"></Child>
</template>
```

### Modifiers and Transformers [​](https://vuejs.org/api/sfc-script-setup.html#modifiers-and-transformers)
To access modifiers used with the `v-model` directive, we can destructure the return value of `defineModel()` like this:
js```
const [modelValue, modelModifiers] = defineModel()

// corresponds to v-model.trim
if (modelModifiers.trim) {
  // ...
}
```

When a modifier is present, we likely need to transform the value when reading or syncing it back to the parent. We can achieve this by using the `get` and `set` transformer options:
js```
const [modelValue, modelModifiers] = defineModel({
  // get() omitted as it is not needed here
  set(value) {
    // if the .trim modifier is used, return trimmed value
    if (modelModifiers.trim) {
      return value.trim()
    }
    // otherwise, return the value as-is
    return value
  }
})
```

### Usage with TypeScript [​](https://vuejs.org/api/sfc-script-setup.html#usage-with-typescript)
Like `defineProps` and `defineEmits`, `defineModel` can also receive type arguments to specify the types of the model value and the modifiers:
ts```
const modelValue = defineModel<string>()
//    ^? Ref<string | undefined>

// default model with options, required removes possible undefined values
const modelValue = defineModel<string>({ required: true })
//    ^? Ref<string>

const [modelValue, modifiers] = defineModel<string, 'trim' | 'uppercase'>()
//                 ^? Record<'trim' | 'uppercase', true | undefined>
```

## defineExpose() [​](https://vuejs.org/api/sfc-script-setup.html#defineexpose)
Components using `<script setup>` are **closed by default** - i.e. the public instance of the component, which is retrieved via template refs or `$parent` chains, will **not** expose any of the bindings declared inside `<script setup>`.
To explicitly expose properties in a `<script setup>` component, use the `defineExpose` compiler macro:
vue```
<script setup>
import { ref } from 'vue'

const a = 1
const b = ref(2)

defineExpose({
  a,
  b
})
</script>
```

When a parent gets an instance of this component via template refs, the retrieved instance will be of the shape `{ a: number, b: number }` (refs are automatically unwrapped just like on normal instances).
## defineOptions() [​](https://vuejs.org/api/sfc-script-setup.html#defineoptions)
  * Only supported in 3.3+


This macro can be used to declare component options directly inside `<script setup>` without having to use a separate `<script>` block:
vue```
<script setup>
defineOptions({
  inheritAttrs: false,
  customOptions: {
    /* ... */
  }
})
</script>
```

  * This is a macro. The options will be hoisted to module scope and cannot access local variables in `<script setup>` that are not literal constants.


## defineSlots()[​](https://vuejs.org/api/sfc-script-setup.html#defineslots)
  * Only supported in 3.3+


This macro can be used to provide type hints to IDEs for slot name and props type checking.
`defineSlots()` only accepts a type parameter and no runtime arguments. The type parameter should be a type literal where the property key is the slot name, and the value type is the slot function. The first argument of the function is the props the slot expects to receive, and its type will be used for slot props in the template. The return type is currently ignored and can be `any`, but we may leverage it for slot content checking in the future.
It also returns the `slots` object, which is equivalent to the `slots` object exposed on the setup context or returned by `useSlots()`.
vue```
<script setup lang="ts">
const slots = defineSlots<{
  default(props: { msg: string }): any
}>()
</script>
```

##  `useSlots()` & `useAttrs()` [​](https://vuejs.org/api/sfc-script-setup.html#useslots-useattrs)
Usage of `slots` and `attrs` inside `<script setup>` should be relatively rare, since you can access them directly as `$slots` and `$attrs` in the template. In the rare case where you do need them, use the `useSlots` and `useAttrs` helpers respectively:
vue```
<script setup>
import { useSlots, useAttrs } from 'vue'

const slots = useSlots()
const attrs = useAttrs()
</script>
```

`useSlots` and `useAttrs` are actual runtime functions that return the equivalent of `setupContext.slots` and `setupContext.attrs`. They can be used in normal composition API functions as well.
## Usage alongside normal `<script>` [​](https://vuejs.org/api/sfc-script-setup.html#usage-alongside-normal-script)
`<script setup>` can be used alongside normal `<script>`. A normal `<script>` may be needed in cases where we need to:
  * Declare options that cannot be expressed in `<script setup>`, for example `inheritAttrs` or custom options enabled via plugins (Can be replaced by [`defineOptions`](https://vuejs.org/api/sfc-script-setup#defineoptions) in 3.3+).
  * Declaring named exports.
  * Run side effects or create objects that should only execute once.


vue```
<script>
// normal <script>, executed in module scope (only once)
runSideEffectOnce()

// declare additional options
export default {
  inheritAttrs: false,
  customOptions: {}
}
</script>

<script setup>
// executed in setup() scope (for each instance)
</script>
```

Support for combining `<script setup>` and `<script>` in the same component is limited to the scenarios described above. Specifically:
  * Do **NOT** use a separate `<script>` section for options that can already be defined using `<script setup>`, such as `props` and `emits`.
  * Variables created inside `<script setup>` are not added as properties to the component instance, making them inaccessible from the Options API. Mixing APIs in this way is strongly discouraged.


If you find yourself in one of the scenarios that is not supported then you should consider switching to an explicit [`setup()`](https://vuejs.org/api/composition-api-setup) function, instead of using `<script setup>`.
## Top-level `await` [​](https://vuejs.org/api/sfc-script-setup.html#top-level-await)
Top-level `await` can be used inside `<script setup>`. The resulting code will be compiled as `async setup()`:
vue```
<script setup>
const post = await fetch(`/api/post/1`).then((r) => r.json())
</script>
```

In addition, the awaited expression will be automatically compiled in a format that preserves the current component instance context after the `await`.
Note
`async setup()` must be used in combination with [`Suspense`](https://vuejs.org/guide/built-ins/suspense), which is currently still an experimental feature. We plan to finalize and document it in a future release - but if you are curious now, you can refer to its
## Import Statements [​](https://vuejs.org/api/sfc-script-setup.html#imports-statements)
Import statements in vue follow
vue```
<script setup>
import { ref } from 'vue'
import { componentA } from './Components'
import { componentB } from '@/Components'
import { componentC } from '~/Components'
</script>
```

## Generics [​](https://vuejs.org/api/sfc-script-setup.html#generics)
Generic type parameters can be declared using the `generic` attribute on the `<script>` tag:
vue```
<script setup lang="ts" generic="T">
defineProps<{
  items: T[]
  selected: T
}>()
</script>
```

The value of `generic` works exactly the same as the parameter list between `<...>` in TypeScript. For example, you can use multiple parameters, `extends` constraints, default types, and reference imported types:
vue```
<script
  setup
  lang="ts"
  generic="T extends string | number, U extends Item"
>
import type { Item } from './types'
defineProps<{
  id: T
  list: U[]
}>()
</script>
```

You can use `@vue-generic` the directive to pass in explicit types, for when the type cannot be inferred:
vue```
<template>
  <!-- @vue-generic {import('@/api').Actor} -->
  <ApiSelect v-model="peopleIds" endpoint="/api/actors" id-prop="actorId" />

  <!-- @vue-generic {import('@/api').Genre} -->
  <ApiSelect v-model="genreIds" endpoint="/api/genres" id-prop="genreId" />
</template>
```

In order to use a reference to a generic component in a `ref` you need to use the `InstanceType` won't work.
vue```
<script
  setup
  lang="ts"
>
import componentWithoutGenerics from '../component-without-generics.vue';
import genericComponent from '../generic-component.vue';

import type { ComponentExposed } from 'vue-component-type-helpers';

// Works for a component without generics
ref<InstanceType<typeof componentWithoutGenerics>>();

ref<ComponentExposed<typeof genericComponent>>();
```

## Restrictions [​](https://vuejs.org/api/sfc-script-setup.html#restrictions)
  * Due to the difference in module execution semantics, code inside `<script setup>` relies on the context of an SFC. When moved into external `.js` or `.ts` files, it may lead to confusion for both developers and tools. Therefore, **`<script setup>`**cannot be used with the`src` attribute.
  * `<script setup>` does not support In-DOM Root Component Template.(


[Syntax Specification](https://vuejs.org/api/sfc-spec)[Next CSS Features](https://vuejs.org/api/sfc-css-features)
<script setup> has loaded
