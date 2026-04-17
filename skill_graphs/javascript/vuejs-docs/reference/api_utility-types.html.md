[Skip to content](https://vuejs.org/api/utility-types.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/api/utility-types)
[日本語 ](https://ja.vuejs.org/api/utility-types)
[Українська ](https://ua.vuejs.org/api/utility-types)
[Français ](https://fr.vuejs.org/api/utility-types)
[한국어 ](https://ko.vuejs.org/api/utility-types)
[Português ](https://pt.vuejs.org/api/utility-types)
[বাংলা ](https://bn.vuejs.org/api/utility-types)
[Italiano ](https://it.vuejs.org/api/utility-types)
[فارسی ](https://fa.vuejs.org/api/utility-types)
[Русский ](https://ru.vuejs.org/api/utility-types)
[Čeština ](https://cs.vuejs.org/api/utility-types)
[繁體中文 ](https://zh-hk.vuejs.org/api/utility-types)
[Polski ](https://pl.vuejs.org/api/utility-types)
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
  * [PropType<T>](https://vuejs.org/api/utility-types.html#proptype-t)
  * [MaybeRef<T>](https://vuejs.org/api/utility-types.html#mayberef)
  * [MaybeRefOrGetter<T>](https://vuejs.org/api/utility-types.html#maybereforgetter)
  * [ExtractPropTypes<T>](https://vuejs.org/api/utility-types.html#extractproptypes)
  * [ExtractPublicPropTypes<T>](https://vuejs.org/api/utility-types.html#extractpublicproptypes)
  * [ComponentCustomProperties](https://vuejs.org/api/utility-types.html#componentcustomproperties)
  * [ComponentCustomOptions](https://vuejs.org/api/utility-types.html#componentcustomoptions)
  * [ComponentCustomProps](https://vuejs.org/api/utility-types.html#componentcustomprops)
  * [CSSProperties](https://vuejs.org/api/utility-types.html#cssproperties)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Utility Types [​](https://vuejs.org/api/utility-types.html#utility-types)
INFO
This page only lists a few commonly used utility types that may need explanation for their usage. For a full list of exported types, consult the
## PropType<T> [​](https://vuejs.org/api/utility-types.html#proptype-t)
Used to annotate a prop with more advanced types when using runtime props declarations.
  * **Example**
ts```
import type { PropType } from 'vue'

interface Book {
  title: string
  author: string
  year: number
}

export default {
  props: {
    book: {
      // provide more specific type to `Object`
      type: Object as PropType<Book>,
      required: true
    }
  }
}
```

  * **See also** [Guide - Typing Component Props](https://vuejs.org/guide/typescript/options-api#typing-component-props)


## MaybeRef<T> [​](https://vuejs.org/api/utility-types.html#mayberef)
  * Only supported in 3.3+


Alias for `T | Ref<T>`. Useful for annotating arguments of [Composables](https://vuejs.org/guide/reusability/composables).
## MaybeRefOrGetter<T> [​](https://vuejs.org/api/utility-types.html#maybereforgetter)
  * Only supported in 3.3+


Alias for `T | Ref<T> | (() => T)`. Useful for annotating arguments of [Composables](https://vuejs.org/guide/reusability/composables).
## ExtractPropTypes<T> [​](https://vuejs.org/api/utility-types.html#extractproptypes)
Extract prop types from a runtime props options object. The extracted types are internal facing - i.e. the resolved props received by the component. This means boolean props and props with default values are always defined, even if they are not required.
To extract public facing props, i.e. props that the parent is allowed to pass, use [`ExtractPublicPropTypes`](https://vuejs.org/api/utility-types.html#extractpublicproptypes).
  * **Example**
ts```
const propsOptions = {
  foo: String,
  bar: Boolean,
  baz: {
    type: Number,
    required: true
  },
  qux: {
    type: Number,
    default: 1
  }
} as const

type Props = ExtractPropTypes<typeof propsOptions>
// {
//   foo?: string,
//   bar: boolean,
//   baz: number,
//   qux: number
// }
```



## ExtractPublicPropTypes<T> [​](https://vuejs.org/api/utility-types.html#extractpublicproptypes)
  * Only supported in 3.3+


Extract prop types from a runtime props options object. The extracted types are public facing - i.e. the props that the parent is allowed to pass.
  * **Example**
ts```
const propsOptions = {
  foo: String,
  bar: Boolean,
  baz: {
    type: Number,
    required: true
  },
  qux: {
    type: Number,
    default: 1
  }
} as const

type Props = ExtractPublicPropTypes<typeof propsOptions>
// {
//   foo?: string,
//   bar?: boolean,
//   baz: number,
//   qux?: number
// }
```



## ComponentCustomProperties [​](https://vuejs.org/api/utility-types.html#componentcustomproperties)
Used to augment the component instance type to support custom global properties.
  * **Example**
ts```
import axios from 'axios'

declare module 'vue' {
  interface ComponentCustomProperties {
    $http: typeof axios
    $translate: (key: string) => string
  }
}
```

TIP
Augmentations must be placed in a module `.ts` or `.d.ts` file. See [Type Augmentation Placement](https://vuejs.org/guide/typescript/options-api#augmenting-global-properties) for more details.
  * **See also** [Guide - Augmenting Global Properties](https://vuejs.org/guide/typescript/options-api#augmenting-global-properties)


## ComponentCustomOptions [​](https://vuejs.org/api/utility-types.html#componentcustomoptions)
Used to augment the component options type to support custom options.
  * **Example**
ts```
import { Route } from 'vue-router'

declare module 'vue' {
  interface ComponentCustomOptions {
    beforeRouteEnter?(to: any, from: any, next: () => void): void
  }
}
```

TIP
Augmentations must be placed in a module `.ts` or `.d.ts` file. See [Type Augmentation Placement](https://vuejs.org/guide/typescript/options-api#augmenting-global-properties) for more details.
  * **See also** [Guide - Augmenting Custom Options](https://vuejs.org/guide/typescript/options-api#augmenting-custom-options)


## ComponentCustomProps [​](https://vuejs.org/api/utility-types.html#componentcustomprops)
Used to augment allowed TSX props in order to use non-declared props on TSX elements.
  * **Example**
ts```
declare module 'vue' {
  interface ComponentCustomProps {
    hello?: string
  }
}

export {}
```

tsx```
// now works even if hello is not a declared prop
<MyComponent hello="world" />
```

TIP
Augmentations must be placed in a module `.ts` or `.d.ts` file. See [Type Augmentation Placement](https://vuejs.org/guide/typescript/options-api#augmenting-global-properties) for more details.


## CSSProperties [​](https://vuejs.org/api/utility-types.html#cssproperties)
Used to augment allowed values in style property bindings.
  * **Example**
Allow any custom CSS property
ts```
declare module 'vue' {
  interface CSSProperties {
    [key: `--${string}`]: string
  }
}
```

tsx```
<div style={ { '--bg-color': 'blue' } }>
```

html```
<div :style="{ '--bg-color': 'blue' }"></div>
```



TIP
Augmentations must be placed in a module `.ts` or `.d.ts` file. See [Type Augmentation Placement](https://vuejs.org/guide/typescript/options-api#augmenting-global-properties) for more details.
See also
SFC `<style>` tags support linking CSS values to dynamic component state using the `v-bind` CSS function. This allows for custom properties without type augmentation.
  * [v-bind() in CSS](https://vuejs.org/api/sfc-css-features#v-bind-in-css)


[Server-Side Rendering](https://vuejs.org/api/ssr)[Next Custom Renderer](https://vuejs.org/api/custom-renderer)
Utility Types has loaded
