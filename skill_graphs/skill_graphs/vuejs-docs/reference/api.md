[Skip to content](https://vuejs.org/api/#VPContent)
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
[简体中文 ](https://cn.vuejs.org/api/)
[日本語 ](https://ja.vuejs.org/api/)
[Українська ](https://ua.vuejs.org/api/)
[Français ](https://fr.vuejs.org/api/)
[한국어 ](https://ko.vuejs.org/api/)
[Português ](https://pt.vuejs.org/api/)
[বাংলা ](https://bn.vuejs.org/api/)
[Italiano ](https://it.vuejs.org/api/)
[فارسی ](https://fa.vuejs.org/api/)
[Русский ](https://ru.vuejs.org/api/)
[Čeština ](https://cs.vuejs.org/api/)
[繁體中文 ](https://zh-hk.vuejs.org/api/)
[Polski ](https://pl.vuejs.org/api/)
Help Us Translate!
Appearance
# API Reference
Filter
## Global API
### Application
  * [createApp()](https://vuejs.org/api/application#createapp)
  * [createSSRApp()](https://vuejs.org/api/application#createssrapp)
  * [app.mount()](https://vuejs.org/api/application#app-mount)
  * [app.unmount()](https://vuejs.org/api/application#app-unmount)
  * [app.onUnmount()](https://vuejs.org/api/application#app-onunmount)
  * [app.component()](https://vuejs.org/api/application#app-component)
  * [app.directive()](https://vuejs.org/api/application#app-directive)
  * [app.use()](https://vuejs.org/api/application#app-use)
  * [app.mixin()](https://vuejs.org/api/application#app-mixin)
  * [app.provide()](https://vuejs.org/api/application#app-provide)
  * [app.runWithContext()](https://vuejs.org/api/application#app-runwithcontext)
  * [app.version](https://vuejs.org/api/application#app-version)
  * [app.config](https://vuejs.org/api/application#app-config)
  * [app.config.errorHandler](https://vuejs.org/api/application#app-config-errorhandler)
  * [app.config.warnHandler](https://vuejs.org/api/application#app-config-warnhandler)
  * [app.config.performance](https://vuejs.org/api/application#app-config-performance)
  * [app.config.compilerOptions](https://vuejs.org/api/application#app-config-compileroptions)
  * [app.config.globalProperties](https://vuejs.org/api/application#app-config-globalproperties)
  * [app.config.optionMergeStrategies](https://vuejs.org/api/application#app-config-optionmergestrategies)
  * [app.config.idPrefix](https://vuejs.org/api/application#app-config-idprefix)
  * [app.config.throwUnhandledErrorInProduction](https://vuejs.org/api/application#app-config-throwunhandlederrorinproduction)


### General
  * [version](https://vuejs.org/api/general#version)
  * [nextTick()](https://vuejs.org/api/general#nexttick)
  * [defineComponent()](https://vuejs.org/api/general#definecomponent)
  * [defineAsyncComponent()](https://vuejs.org/api/general#defineasynccomponent)


## Composition API
### setup()
  * [Basic Usage](https://vuejs.org/api/composition-api-setup#basic-usage)
  * [Accessing Props](https://vuejs.org/api/composition-api-setup#accessing-props)
  * [Setup Context](https://vuejs.org/api/composition-api-setup#setup-context)
  * [Usage with Render Functions](https://vuejs.org/api/composition-api-setup#usage-with-render-functions)


### Reactivity: Core
  * [ref()](https://vuejs.org/api/reactivity-core#ref)
  * [computed()](https://vuejs.org/api/reactivity-core#computed)
  * [reactive()](https://vuejs.org/api/reactivity-core#reactive)
  * [readonly()](https://vuejs.org/api/reactivity-core#readonly)
  * [watchEffect()](https://vuejs.org/api/reactivity-core#watcheffect)
  * [watchPostEffect()](https://vuejs.org/api/reactivity-core#watchposteffect)
  * [watchSyncEffect()](https://vuejs.org/api/reactivity-core#watchsynceffect)
  * [watch()](https://vuejs.org/api/reactivity-core#watch)
  * [onWatcherCleanup()](https://vuejs.org/api/reactivity-core#onwatchercleanup)


### Reactivity: Utilities
  * [isRef()](https://vuejs.org/api/reactivity-utilities#isref)
  * [unref()](https://vuejs.org/api/reactivity-utilities#unref)
  * [toRef()](https://vuejs.org/api/reactivity-utilities#toref)
  * [toValue()](https://vuejs.org/api/reactivity-utilities#tovalue)
  * [toRefs()](https://vuejs.org/api/reactivity-utilities#torefs)
  * [isProxy()](https://vuejs.org/api/reactivity-utilities#isproxy)
  * [isReactive()](https://vuejs.org/api/reactivity-utilities#isreactive)
  * [isReadonly()](https://vuejs.org/api/reactivity-utilities#isreadonly)


### Reactivity: Advanced
  * [shallowRef()](https://vuejs.org/api/reactivity-advanced#shallowref)
  * [triggerRef()](https://vuejs.org/api/reactivity-advanced#triggerref)
  * [customRef()](https://vuejs.org/api/reactivity-advanced#customref)
  * [shallowReactive()](https://vuejs.org/api/reactivity-advanced#shallowreactive)
  * [shallowReadonly()](https://vuejs.org/api/reactivity-advanced#shallowreadonly)
  * [toRaw()](https://vuejs.org/api/reactivity-advanced#toraw)
  * [markRaw()](https://vuejs.org/api/reactivity-advanced#markraw)
  * [effectScope()](https://vuejs.org/api/reactivity-advanced#effectscope)
  * [getCurrentScope()](https://vuejs.org/api/reactivity-advanced#getcurrentscope)
  * [onScopeDispose()](https://vuejs.org/api/reactivity-advanced#onscopedispose)


### Lifecycle Hooks
  * [onMounted()](https://vuejs.org/api/composition-api-lifecycle#onmounted)
  * [onUpdated()](https://vuejs.org/api/composition-api-lifecycle#onupdated)
  * [onUnmounted()](https://vuejs.org/api/composition-api-lifecycle#onunmounted)
  * [onBeforeMount()](https://vuejs.org/api/composition-api-lifecycle#onbeforemount)
  * [onBeforeUpdate()](https://vuejs.org/api/composition-api-lifecycle#onbeforeupdate)
  * [onBeforeUnmount()](https://vuejs.org/api/composition-api-lifecycle#onbeforeunmount)
  * [onErrorCaptured()](https://vuejs.org/api/composition-api-lifecycle#onerrorcaptured)
  * [onRenderTracked()](https://vuejs.org/api/composition-api-lifecycle#onrendertracked)
  * [onRenderTriggered()](https://vuejs.org/api/composition-api-lifecycle#onrendertriggered)
  * [onActivated()](https://vuejs.org/api/composition-api-lifecycle#onactivated)
  * [onDeactivated()](https://vuejs.org/api/composition-api-lifecycle#ondeactivated)
  * [onServerPrefetch()](https://vuejs.org/api/composition-api-lifecycle#onserverprefetch)


### Dependency Injection
  * [provide()](https://vuejs.org/api/composition-api-dependency-injection#provide)
  * [inject()](https://vuejs.org/api/composition-api-dependency-injection#inject)
  * [hasInjectionContext()](https://vuejs.org/api/composition-api-dependency-injection#has-injection-context)


### Helpers
  * [useAttrs()](https://vuejs.org/api/composition-api-helpers#useattrs)
  * [useSlots()](https://vuejs.org/api/composition-api-helpers#useslots)
  * [useModel()](https://vuejs.org/api/composition-api-helpers#usemodel)
  * [useTemplateRef()](https://vuejs.org/api/composition-api-helpers#usetemplateref)
  * [useId()](https://vuejs.org/api/composition-api-helpers#useid)


## Options API
### Options: State
  * [data](https://vuejs.org/api/options-state#data)
  * [props](https://vuejs.org/api/options-state#props)
  * [computed](https://vuejs.org/api/options-state#computed)
  * [methods](https://vuejs.org/api/options-state#methods)
  * [watch](https://vuejs.org/api/options-state#watch)
  * [emits](https://vuejs.org/api/options-state#emits)
  * [expose](https://vuejs.org/api/options-state#expose)


### Options: Rendering
  * [template](https://vuejs.org/api/options-rendering#template)
  * [render](https://vuejs.org/api/options-rendering#render)
  * [compilerOptions](https://vuejs.org/api/options-rendering#compileroptions)
  * [slots](https://vuejs.org/api/options-rendering#slots)


### Options: Lifecycle
  * [beforeCreate](https://vuejs.org/api/options-lifecycle#beforecreate)
  * [created](https://vuejs.org/api/options-lifecycle#created)
  * [beforeMount](https://vuejs.org/api/options-lifecycle#beforemount)
  * [mounted](https://vuejs.org/api/options-lifecycle#mounted)
  * [beforeUpdate](https://vuejs.org/api/options-lifecycle#beforeupdate)
  * [updated](https://vuejs.org/api/options-lifecycle#updated)
  * [beforeUnmount](https://vuejs.org/api/options-lifecycle#beforeunmount)
  * [unmounted](https://vuejs.org/api/options-lifecycle#unmounted)
  * [errorCaptured](https://vuejs.org/api/options-lifecycle#errorcaptured)
  * [renderTracked](https://vuejs.org/api/options-lifecycle#rendertracked)
  * [renderTriggered](https://vuejs.org/api/options-lifecycle#rendertriggered)
  * [activated](https://vuejs.org/api/options-lifecycle#activated)
  * [deactivated](https://vuejs.org/api/options-lifecycle#deactivated)
  * [serverPrefetch](https://vuejs.org/api/options-lifecycle#serverprefetch)


### Options: Composition
  * [provide](https://vuejs.org/api/options-composition#provide)
  * [inject](https://vuejs.org/api/options-composition#inject)
  * [mixins](https://vuejs.org/api/options-composition#mixins)
  * [extends](https://vuejs.org/api/options-composition#extends)


### Options: Misc
  * [name](https://vuejs.org/api/options-misc#name)
  * [inheritAttrs](https://vuejs.org/api/options-misc#inheritattrs)
  * [components](https://vuejs.org/api/options-misc#components)
  * [directives](https://vuejs.org/api/options-misc#directives)


### Component Instance
  * [$data](https://vuejs.org/api/component-instance#data)
  * [$props](https://vuejs.org/api/component-instance#props)
  * [$el](https://vuejs.org/api/component-instance#el)
  * [$options](https://vuejs.org/api/component-instance#options)
  * [$parent](https://vuejs.org/api/component-instance#parent)
  * [$root](https://vuejs.org/api/component-instance#root)
  * [$slots](https://vuejs.org/api/component-instance#slots)
  * [$refs](https://vuejs.org/api/component-instance#refs)
  * [$attrs](https://vuejs.org/api/component-instance#attrs)
  * [$watch()](https://vuejs.org/api/component-instance#watch)
  * [$emit()](https://vuejs.org/api/component-instance#emit)
  * [$forceUpdate()](https://vuejs.org/api/component-instance#forceupdate)
  * [$nextTick()](https://vuejs.org/api/component-instance#nexttick)


## Built-ins
### Directives
  * [v-text](https://vuejs.org/api/built-in-directives#v-text)
  * [v-html](https://vuejs.org/api/built-in-directives#v-html)
  * [v-show](https://vuejs.org/api/built-in-directives#v-show)
  * [v-if](https://vuejs.org/api/built-in-directives#v-if)
  * [v-else](https://vuejs.org/api/built-in-directives#v-else)
  * [v-else-if](https://vuejs.org/api/built-in-directives#v-else-if)
  * [v-for](https://vuejs.org/api/built-in-directives#v-for)
  * [v-on](https://vuejs.org/api/built-in-directives#v-on)
  * [v-bind](https://vuejs.org/api/built-in-directives#v-bind)
  * [v-model](https://vuejs.org/api/built-in-directives#v-model)
  * [v-slot](https://vuejs.org/api/built-in-directives#v-slot)
  * [v-pre](https://vuejs.org/api/built-in-directives#v-pre)
  * [v-once](https://vuejs.org/api/built-in-directives#v-once)
  * [v-memo](https://vuejs.org/api/built-in-directives#v-memo)
  * [v-cloak](https://vuejs.org/api/built-in-directives#v-cloak)


### Components
  * [<Transition>](https://vuejs.org/api/built-in-components#transition)
  * [<TransitionGroup>](https://vuejs.org/api/built-in-components#transitiongroup)
  * [<KeepAlive>](https://vuejs.org/api/built-in-components#keepalive)
  * [<Teleport>](https://vuejs.org/api/built-in-components#teleport)
  * [<Suspense>](https://vuejs.org/api/built-in-components#suspense)


### Special Elements
  * [<component>](https://vuejs.org/api/built-in-special-elements#component)
  * [<slot>](https://vuejs.org/api/built-in-special-elements#slot)
  * [<template>](https://vuejs.org/api/built-in-special-elements#template)


### Special Attributes
  * [key](https://vuejs.org/api/built-in-special-attributes#key)
  * [ref](https://vuejs.org/api/built-in-special-attributes#ref)
  * [is](https://vuejs.org/api/built-in-special-attributes#is)


## Single-File Component
### Syntax Specification
  * [Overview](https://vuejs.org/api/sfc-spec#overview)
  * [Language Blocks](https://vuejs.org/api/sfc-spec#language-blocks)
  * [Automatic Name Inference](https://vuejs.org/api/sfc-spec#automatic-name-inference)
  * [Pre-Processors](https://vuejs.org/api/sfc-spec#pre-processors)
  * [src Imports](https://vuejs.org/api/sfc-spec#src-imports)
  * [Comments](https://vuejs.org/api/sfc-spec#comments)


### <script setup>
  * [Basic Syntax](https://vuejs.org/api/sfc-script-setup#basic-syntax)
  * [Reactivity](https://vuejs.org/api/sfc-script-setup#reactivity)
  * [Using Components](https://vuejs.org/api/sfc-script-setup#using-components)
  * [Using Custom Directives](https://vuejs.org/api/sfc-script-setup#using-custom-directives)
  * [defineProps() & defineEmits()](https://vuejs.org/api/sfc-script-setup#defineprops-defineemits)
  * [defineModel()](https://vuejs.org/api/sfc-script-setup#definemodel)
  * [defineExpose()](https://vuejs.org/api/sfc-script-setup#defineexpose)
  * [defineOptions()](https://vuejs.org/api/sfc-script-setup#defineoptions)
  * [defineSlots()](https://vuejs.org/api/sfc-script-setup#defineslots)
  * [useSlots() & useAttrs()](https://vuejs.org/api/sfc-script-setup#useslots-useattrs)
  * [Usage alongside normal <script>](https://vuejs.org/api/sfc-script-setup#usage-alongside-normal-script)
  * [Top-level await](https://vuejs.org/api/sfc-script-setup#top-level-await)
  * [Import Statements](https://vuejs.org/api/sfc-script-setup#imports-statements)
  * [Generics](https://vuejs.org/api/sfc-script-setup#generics)
  * [Restrictions](https://vuejs.org/api/sfc-script-setup#restrictions)


### CSS Features
  * [Scoped CSS](https://vuejs.org/api/sfc-css-features#scoped-css)
  * [CSS Modules](https://vuejs.org/api/sfc-css-features#css-modules)
  * [v-bind() in CSS](https://vuejs.org/api/sfc-css-features#v-bind-in-css)


## Advanced APIs
### Custom Elements
  * [defineCustomElement()](https://vuejs.org/api/custom-elements#definecustomelement)
  * [useHost()](https://vuejs.org/api/custom-elements#usehost)
  * [useShadowRoot()](https://vuejs.org/api/custom-elements#useshadowroot)
  * [this.$host](https://vuejs.org/api/custom-elements#this-host)


### Render Function
  * [h()](https://vuejs.org/api/render-function#h)
  * [mergeProps()](https://vuejs.org/api/render-function#mergeprops)
  * [cloneVNode()](https://vuejs.org/api/render-function#clonevnode)
  * [isVNode()](https://vuejs.org/api/render-function#isvnode)
  * [resolveComponent()](https://vuejs.org/api/render-function#resolvecomponent)
  * [resolveDirective()](https://vuejs.org/api/render-function#resolvedirective)
  * [withDirectives()](https://vuejs.org/api/render-function#withdirectives)
  * [withModifiers()](https://vuejs.org/api/render-function#withmodifiers)


### Server-Side Rendering
  * [renderToString()](https://vuejs.org/api/ssr#rendertostring)
  * [renderToNodeStream()](https://vuejs.org/api/ssr#rendertonodestream)
  * [pipeToNodeWritable()](https://vuejs.org/api/ssr#pipetonodewritable)
  * [renderToWebStream()](https://vuejs.org/api/ssr#rendertowebstream)
  * [pipeToWebWritable()](https://vuejs.org/api/ssr#pipetowebwritable)
  * [renderToSimpleStream()](https://vuejs.org/api/ssr#rendertosimplestream)
  * [useSSRContext()](https://vuejs.org/api/ssr#usessrcontext)
  * [data-allow-mismatch](https://vuejs.org/api/ssr#data-allow-mismatch)


### TypeScript Utility Types
  * [PropType<T>](https://vuejs.org/api/utility-types#proptype-t)
  * [MaybeRef<T>](https://vuejs.org/api/utility-types#mayberef)
  * [MaybeRefOrGetter<T>](https://vuejs.org/api/utility-types#maybereforgetter)
  * [ExtractPropTypes<T>](https://vuejs.org/api/utility-types#extractproptypes)
  * [ExtractPublicPropTypes<T>](https://vuejs.org/api/utility-types#extractpublicproptypes)
  * [ComponentCustomProperties](https://vuejs.org/api/utility-types#componentcustomproperties)
  * [ComponentCustomOptions](https://vuejs.org/api/utility-types#componentcustomoptions)
  * [ComponentCustomProps](https://vuejs.org/api/utility-types#componentcustomprops)
  * [CSSProperties](https://vuejs.org/api/utility-types#cssproperties)


### Custom Renderer
  * [createRenderer()](https://vuejs.org/api/custom-renderer#createrenderer)


### Compile-Time Flags
  * [__VUE_OPTIONS_API__](https://vuejs.org/api/compile-time-flags#VUE_OPTIONS_API)
  * [__VUE_PROD_DEVTOOLS__](https://vuejs.org/api/compile-time-flags#VUE_PROD_DEVTOOLS)
  * [__VUE_PROD_HYDRATION_MISMATCH_DETAILS__](https://vuejs.org/api/compile-time-flags#VUE_PROD_HYDRATION_MISMATCH_DETAILS)
  * [Configuration Guides](https://vuejs.org/api/compile-time-flags#configuration-guides)


API Reference has loaded
