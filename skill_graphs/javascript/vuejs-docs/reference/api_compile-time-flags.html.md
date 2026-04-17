[Skip to content](https://vuejs.org/api/compile-time-flags.html#VPContent)
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
[简体中文 ](https://cn.vuejs.org/api/compile-time-flags)
[日本語 ](https://ja.vuejs.org/api/compile-time-flags)
[Українська ](https://ua.vuejs.org/api/compile-time-flags)
[Français ](https://fr.vuejs.org/api/compile-time-flags)
[한국어 ](https://ko.vuejs.org/api/compile-time-flags)
[Português ](https://pt.vuejs.org/api/compile-time-flags)
[বাংলা ](https://bn.vuejs.org/api/compile-time-flags)
[Italiano ](https://it.vuejs.org/api/compile-time-flags)
[فارسی ](https://fa.vuejs.org/api/compile-time-flags)
[Русский ](https://ru.vuejs.org/api/compile-time-flags)
[Čeština ](https://cs.vuejs.org/api/compile-time-flags)
[繁體中文 ](https://zh-hk.vuejs.org/api/compile-time-flags)
[Polski ](https://pl.vuejs.org/api/compile-time-flags)
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
  * [__VUE_OPTIONS_API__](https://vuejs.org/api/compile-time-flags.html#VUE_OPTIONS_API)
  * [__VUE_PROD_DEVTOOLS__](https://vuejs.org/api/compile-time-flags.html#VUE_PROD_DEVTOOLS)
  * [__VUE_PROD_HYDRATION_MISMATCH_DETAILS__](https://vuejs.org/api/compile-time-flags.html#VUE_PROD_HYDRATION_MISMATCH_DETAILS)
  * [Configuration Guides](https://vuejs.org/api/compile-time-flags.html#configuration-guides)
    * [Vite](https://vuejs.org/api/compile-time-flags.html#vite)
    * [vue-cli](https://vuejs.org/api/compile-time-flags.html#vue-cli)
    * [webpack](https://vuejs.org/api/compile-time-flags.html#webpack)
    * [Rollup](https://vuejs.org/api/compile-time-flags.html#rollup)


[Sponsors](https://vuejs.org/sponsor/)
[Inquire about Special Sponsorship](https://vuejs.org/sponsor/#tier-benefits)
[Become a Sponsor](https://vuejs.org/sponsor/)
# Compile-Time Flags [​](https://vuejs.org/api/compile-time-flags.html#compile-time-flags)
TIP
Compile-time flags only apply when using the `esm-bundler` build of Vue (i.e. `vue/dist/vue.esm-bundler.js`).
When using Vue with a build step, it is possible to configure a number of compile-time flags to enable / disable certain features. The benefit of using compile-time flags is that features disabled this way can be removed from the final bundle via tree-shaking.
Vue will work even if these flags are not explicitly configured. However, it is recommended to always configure them so that the relevant features can be properly removed when possible.
See [Configuration Guides](https://vuejs.org/api/compile-time-flags.html#configuration-guides) on how to configure them depending on your build tool.
##  `__VUE_OPTIONS_API__` [​](https://vuejs.org/api/compile-time-flags.html#VUE_OPTIONS_API)
  * **Default:** `true`
Enable / disable Options API support. Disabling this will result in smaller bundles, but may affect compatibility with 3rd party libraries if they rely on Options API.


##  `__VUE_PROD_DEVTOOLS__` [​](https://vuejs.org/api/compile-time-flags.html#VUE_PROD_DEVTOOLS)
  * **Default:** `false`
Enable / disable devtools support in production builds. This will result in more code included in the bundle, so it is recommended to only enable this for debugging purposes.


##  `__VUE_PROD_HYDRATION_MISMATCH_DETAILS__` [​](https://vuejs.org/api/compile-time-flags.html#VUE_PROD_HYDRATION_MISMATCH_DETAILS)
  * **Default:** `false`
Enable/disable detailed warnings for hydration mismatches in production builds. This will result in more code included in the bundle, so it is recommended to only enable this for debugging purposes.
  * Only available in 3.4+


## Configuration Guides [​](https://vuejs.org/api/compile-time-flags.html#configuration-guides)
### Vite [​](https://vuejs.org/api/compile-time-flags.html#vite)
`@vitejs/plugin-vue` automatically provides default values for these flags. To change the default values, use Vite's
vite.config.js
js```
import { defineConfig } from 'vite'

export default defineConfig({
  define: {
    // enable hydration mismatch details in production build
    __VUE_PROD_HYDRATION_MISMATCH_DETAILS__: 'true'
  }
})
```

### vue-cli [​](https://vuejs.org/api/compile-time-flags.html#vue-cli)
`@vue/cli-service` automatically provides default values for some of these flags. To configure /change the values:
vue.config.js
js```
module.exports = {
  chainWebpack: (config) => {
    config.plugin('define').tap((definitions) => {
      Object.assign(definitions[0], {
        __VUE_OPTIONS_API__: 'true',
        __VUE_PROD_DEVTOOLS__: 'false',
        __VUE_PROD_HYDRATION_MISMATCH_DETAILS__: 'false'
      })
      return definitions
    })
  }
}
```

### webpack [​](https://vuejs.org/api/compile-time-flags.html#webpack)
Flags should be defined using webpack's
webpack.config.js
js```
module.exports = {
  // ...
  plugins: [
    new webpack.DefinePlugin({
      __VUE_OPTIONS_API__: 'true',
      __VUE_PROD_DEVTOOLS__: 'false',
      __VUE_PROD_HYDRATION_MISMATCH_DETAILS__: 'false'
    })
  ]
}
```

### Rollup [​](https://vuejs.org/api/compile-time-flags.html#rollup)
Flags should be defined using
rollup.config.js
js```
import replace from '@rollup/plugin-replace'

export default {
  plugins: [
    replace({
      __VUE_OPTIONS_API__: 'true',
      __VUE_PROD_DEVTOOLS__: 'false',
      __VUE_PROD_HYDRATION_MISMATCH_DETAILS__: 'false'
    })
  ]
}
```

[Custom Renderer](https://vuejs.org/api/custom-renderer)
Compile-Time Flags has loaded
