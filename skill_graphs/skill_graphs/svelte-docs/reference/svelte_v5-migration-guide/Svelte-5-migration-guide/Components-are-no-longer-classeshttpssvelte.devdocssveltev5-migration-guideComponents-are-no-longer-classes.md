##  Components are no longer classes[](https://svelte.dev/docs/svelte/v5-migration-guide#Components-are-no-longer-classes)
In Svelte 3 and 4, components are classes. In Svelte 5 they are functions and should be instantiated differently. If you need to manually instantiate components, you should use `mount` or `hydrate` (imported from `svelte`) instead. If you see this error using SvelteKit, try updating to the latest version of SvelteKit first, which adds support for Svelte 5. If you're using Svelte without SvelteKit, you'll likely have a `main.js` file (or similar) which you need to adjust:
```
import { function mount<Props extends Record<string, any>, Exports extends Record<string, any>>(component: ComponentType<SvelteComponent<Props>> | Component<Props, Exports, any>, options: MountOptions<Props>): Exports


Mounts a component to the given target and returns the exports and potentially the props (if compiled with accessors: true) of the component.
Transitions will play during the initial render unless the intro option is set to false.





reference[](https://svelte.dev/docs/svelte/svelte#mount)
mount } from 'svelte';
import ```
type App = SvelteComponent<Record<string, any>, any, any>
const App: LegacyComponentType
```
`App from './App.svelte' const ````
const app: {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>
```
`app = ````
mount<Record<string, any>, {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>>(component: ComponentType<SvelteComponent<Record<string, any>, any, any>> | Component<Record<string, any>, {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>, any>, options: MountOptions<...>): {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<...>
```
`
Mounts a component to the given target and returns the exports and potentially the props (if compiled with `accessors: true`) of the component. Transitions will play during the initial render unless the `intro` option is set to `false`.
[reference](https://svelte.dev/docs/svelte/svelte#mount)
mount(`const App: LegacyComponentType`App, { `target: Document | Element | ShadowRoot`
Target element where the component will be mounted.
target: `var document: Document`
**`window.document`**returns a reference to the document contained in the window.
document.`Document.getElementById(elementId: string): HTMLElement | null`
Returns the first element within node's descendants whose ID is elementId.
getElementById("app") }); export default ````
const app: {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>
```
`app;`
```

`mount` and `hydrate` have the exact same API. The difference is that `hydrate` will pick up the Svelte's server-rendered HTML inside its target and hydrate it. Both return an object with the exports of the component and potentially property accessors (if compiled with `accessors: true`). They do not come with the `$on`, `$set` and `$destroy` methods you may know from the class component API. These are its replacements:
For `$on`, instead of listening to events, pass them via the `events` property on the options argument.
```
import { function mount<Props extends Record<string, any>, Exports extends Record<string, any>>(component: ComponentType<SvelteComponent<Props>> | Component<Props, Exports, any>, options: MountOptions<Props>): Exports


Mounts a component to the given target and returns the exports and potentially the props (if compiled with accessors: true) of the component.
Transitions will play during the initial render unless the intro option is set to false.





reference[](https://svelte.dev/docs/svelte/svelte#mount)
mount } from 'svelte';
import ```
type App = SvelteComponent<Record<string, any>, any, any>
const App: LegacyComponentType
```
`App from './App.svelte' const ````
const app: {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>
```
`app = ````
mount<Record<string, any>, {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>>(component: ComponentType<SvelteComponent<Record<string, any>, any, any>> | Component<Record<string, any>, {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>, any>, options: MountOptions<...>): {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<...>
```
`
Mounts a component to the given target and returns the exports and potentially the props (if compiled with `accessors: true`) of the component. Transitions will play during the initial render unless the `intro` option is set to `false`.
[reference](https://svelte.dev/docs/svelte/svelte#mount)
mount(`const App: LegacyComponentType`App, { `target: Document | Element | ShadowRoot`
Target element where the component will be mounted.
target: `var document: Document`
**`window.document`**returns a reference to the document contained in the window.
document.`Document.getElementById(elementId: string): HTMLElement | null`
Returns the first element within node's descendants whose ID is elementId.
getElementById("app"), `events?: Record<string, (e: any) => any> | undefined`
Allows the specification of events.
@deprecatedUse callback props instead.
events: { `event: any`event: callback } });`
```

> Note that using `events` is discouraged — instead, [use callbacks](https://svelte.dev/docs/svelte/v5-migration-guide#Event-changes)
For `$set`, use `$state` instead to create a reactive property object and manipulate it. If you're doing this inside a `.js` or `.ts` file, adjust the ending to include `.svelte`, i.e. `.svelte.js` or `.svelte.ts`.
```
import { function mount<Props extends Record<string, any>, Exports extends Record<string, any>>(component: ComponentType<SvelteComponent<Props>> | Component<Props, Exports, any>, options: MountOptions<Props>): Exports


Mounts a component to the given target and returns the exports and potentially the props (if compiled with accessors: true) of the component.
Transitions will play during the initial render unless the intro option is set to false.





reference[](https://svelte.dev/docs/svelte/svelte#mount)
mount } from 'svelte';
import ```
type App = SvelteComponent<Record<string, any>, any, any>
const App: LegacyComponentType
```
`App from './App.svelte' const ````
const props: {
    foo: string;
}
```
`props = ````
function $state<{
    foo: string;
}>(initial: {
    foo: string;
}): {
    foo: string;
} (+1 overload)
namespace $state
```
`
Declares reactive state.
Example:
```
let count = $state(0);
```

@see{@link <https://svelte.dev/docs/svelte/$state> Documentation}
@paraminitial The initial value
$state({ `foo: string`foo: 'bar' }); const ````
const app: {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>
```
`app = ````
mount<Record<string, any>, {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>>(component: ComponentType<SvelteComponent<Record<string, any>, any, any>> | Component<Record<string, any>, {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>, any>, options: MountOptions<...>): {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<...>
```
`
Mounts a component to the given target and returns the exports and potentially the props (if compiled with `accessors: true`) of the component. Transitions will play during the initial render unless the `intro` option is set to `false`.
[reference](https://svelte.dev/docs/svelte/svelte#mount)
mount(`const App: LegacyComponentType`App, { `target: Document | Element | ShadowRoot`
Target element where the component will be mounted.
target: `var document: Document`
**`window.document`**returns a reference to the document contained in the window.
document.`Document.getElementById(elementId: string): HTMLElement | null`
Returns the first element within node's descendants whose ID is elementId.
getElementById("app"), `props?: Record<string, any> | undefined`
Component properties.
props }); ````
const props: {
    foo: string;
}
```
`props.`foo: string`foo = 'baz';`
```

For `$destroy`, use `unmount` instead.
```
import { function mount<Props extends Record<string, any>, Exports extends Record<string, any>>(component: ComponentType<SvelteComponent<Props>> | Component<Props, Exports, any>, options: MountOptions<Props>): Exports


Mounts a component to the given target and returns the exports and potentially the props (if compiled with accessors: true) of the component.
Transitions will play during the initial render unless the intro option is set to false.





reference[](https://svelte.dev/docs/svelte/svelte#mount)
mount, ```
function unmount(component: Record<string, any>, options?: {
    outro?: boolean;
} | undefined): Promise<void>
```
`
Unmounts a component that was previously mounted using `mount` or `hydrate`.
Since 5.13.0, if `options.outro` is `true`, [transitions](https://svelte.dev/docs/svelte/transition) will play before the component is removed from the DOM.
Returns a `Promise` that resolves after transitions have completed if `options.outro` is true, or immediately otherwise (prior to 5.13.0, returns `void`).
```
import { mount, unmount } from 'svelte';
import App from './App.svelte';

const app = mount(App, { target: document.body });

// later...
unmount(app, { outro: true });
```

[reference](https://svelte.dev/docs/svelte/svelte#unmount)
unmount } from 'svelte'; import ````
type App = SvelteComponent<Record<string, any>, any, any>
const App: LegacyComponentType
```
`App from './App.svelte' const ````
const app: {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>
```
`app = ````
mount<Record<string, any>, {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>>(component: ComponentType<SvelteComponent<Record<string, any>, any, any>> | Component<Record<string, any>, {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>, any>, options: MountOptions<...>): {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<...>
```
`
Mounts a component to the given target and returns the exports and potentially the props (if compiled with `accessors: true`) of the component. Transitions will play during the initial render unless the `intro` option is set to `false`.
[reference](https://svelte.dev/docs/svelte/svelte#mount)
mount(`const App: LegacyComponentType`App, { `target: Document | Element | ShadowRoot`
Target element where the component will be mounted.
target: `var document: Document`
**`window.document`**returns a reference to the document contained in the window.
document.`Document.getElementById(elementId: string): HTMLElement | null`
Returns the first element within node's descendants whose ID is elementId.
getElementById("app") }); ````
function unmount(component: Record<string, any>, options?: {
    outro?: boolean;
} | undefined): Promise<void>
```
`
Unmounts a component that was previously mounted using `mount` or `hydrate`.
Since 5.13.0, if `options.outro` is `true`, [transitions](https://svelte.dev/docs/svelte/transition) will play before the component is removed from the DOM.
Returns a `Promise` that resolves after transitions have completed if `options.outro` is true, or immediately otherwise (prior to 5.13.0, returns `void`).
```
import { mount, unmount } from 'svelte';
import App from './App.svelte';

const app = mount(App, { target: document.body });

// later...
unmount(app, { outro: true });
```

[reference](https://svelte.dev/docs/svelte/svelte#unmount)
unmount(````
const app: {
    $on?(type: string, callback: (e: any) => void): () => void;
    $set?(props: Partial<Record<string, any>>): void;
} & Record<string, any>
```
`app);`
```

As a stop-gap-solution, you can also use `createClassComponent` or `asClassComponent` (imported from `svelte/legacy`) instead to keep the same API known from Svelte 4 after instantiating.
```
import { ```
function createClassComponent<Props extends Record<string, any>, Exports extends Record<string, any>, Events extends Record<string, any>, Slots extends Record<string, any>>(options: ComponentConstructorOptions<Props> & {
    component: ComponentType<SvelteComponent<Props, Events, Slots>> | Component<Props>;
}): SvelteComponent<Props, Events, Slots> & Exports
```
`
Takes the same options as a Svelte 4 component and the component function and returns a Svelte 4 compatible component.
@deprecatedUse this only as a temporary solution to migrate your imperative component code to Svelte 5.
[reference](https://svelte.dev/docs/svelte/svelte-legacy#createClassComponent)
createClassComponent } from 'svelte/legacy'; import ````
type App = SvelteComponent<Record<string, any>, any, any>
const App: LegacyComponentType
```
`App from './App.svelte' const `const app: SvelteComponent<Record<string, any>, any, any> & Record<string, any>`app = ````
createClassComponent<Record<string, any>, Record<string, any>, any, any>(options: ComponentConstructorOptions<Record<string, any>> & {
    component: Component<Record<string, any>, {}, string> | ComponentType<SvelteComponent<Record<string, any>, any, any>>;
}): SvelteComponent<Record<string, any>, any, any> & Record<string, any>
```
`
Takes the same options as a Svelte 4 component and the component function and returns a Svelte 4 compatible component.
@deprecatedUse this only as a temporary solution to migrate your imperative component code to Svelte 5.
[reference](https://svelte.dev/docs/svelte/svelte-legacy#createClassComponent)
createClassComponent({ `component: Component<Record<string, any>, {}, string> | ComponentType<SvelteComponent<Record<string, any>, any, any>>`component: `const App: LegacyComponentType`App, `ComponentConstructorOptions<Props extends Record<string, any> = Record<string, any>>.target: Document | Element | ShadowRoot`target: `var document: Document`
**`window.document`**returns a reference to the document contained in the window.
document.`Document.getElementById(elementId: string): HTMLElement | null`
Returns the first element within node's descendants whose ID is elementId.
getElementById("app") }); export default `const app: SvelteComponent<Record<string, any>, any, any> & Record<string, any>`app;`
```

If this component is not under your control, you can use the `compatibility.componentApi` compiler option for auto-applied backwards compatibility, which means code using `new Component(...)` keeps working without adjustments (note that this adds a bit of overhead to each component). This will also add `$set` and `$on` methods for all component instances you get through `bind:this`.
```
/// svelte.config.js
export default {
	```
compilerOptions: {
    compatibility: {
        componentApi: number;
    };
}
```
`compilerOptions: { ````
compatibility: {
    componentApi: number;
}
```
`compatibility: { `componentApi: number`componentApi: 4 } } };`
```

Note that `mount` and `hydrate` are _not_ synchronous, so things like `onMount` won't have been called by the time the function returns and the pending block of promises will not have been rendered yet (because `#await` waits a microtask to wait for a potentially immediately-resolved promise). If you need that guarantee, call `flushSync` (import from `'svelte'`) after calling `mount/hydrate`.
###  Server API changes[](https://svelte.dev/docs/svelte/v5-migration-guide#Components-are-no-longer-classes-Server-API-changes)
Similarly, components no longer have a `render` method when compiled for server-side rendering. Instead, pass the function to `render` from `svelte/server`:
```
import { ```
function render<Comp extends SvelteComponent<any> | Component<any>, Props extends ComponentProps<Comp> = ComponentProps<Comp>>(...args: {} extends Props ? [component: Comp extends SvelteComponent<any> ? ComponentType<Comp> : Comp, options?: {
    props?: Omit<Props, "$$slots" | "$$events">;
    context?: Map<any, any>;
    idPrefix?: string;
    csp?: Csp;
    transformError?: (error: unknown) => unknown | Promise<unknown>;
}] : [component: Comp extends SvelteComponent<any> ? ComponentType<Comp> : Comp, options: {
    props: Omit<Props, "$$slots" | "$$events">;
    context?: Map<any, any>;
    idPrefix?: string;
    csp?: Csp;
    transformError?: (error: unknown) => unknown | Promise<unknown>;
}]): RenderOutput
```
`
Only available on the server and when compiling with the `server` option. Takes a component and returns an object with `body` and `head` properties on it, which you can use to populate the HTML when server-rendering your app.
[reference](https://svelte.dev/docs/svelte/svelte-server#render)
render } from 'svelte/server'; import ````
type App = SvelteComponent<Record<string, any>, any, any>
const App: LegacyComponentType
```
`App from './App.svelte'; const { `const html: string`html, `const head: string`
HTML that goes into the `<head>`
head } = ````
render<SvelteComponent<Record<string, any>, any, any>, Record<string, any>>(component: ComponentType<SvelteComponent<Record<string, any>, any, any>>, options?: {
    props?: Omit<Record<string, any>, "$$slots" | "$$events"> | undefined;
    context?: Map<any, any>;
    idPrefix?: string;
    csp?: Csp;
    transformError?: ((error: unknown) => unknown | Promise<unknown>) | undefined;
} | undefined): RenderOutput
```
`
Only available on the server and when compiling with the `server` option. Takes a component and returns an object with `body` and `head` properties on it, which you can use to populate the HTML when server-rendering your app.
[reference](https://svelte.dev/docs/svelte/svelte-server#render)
render(`const App: LegacyComponentType`App, { `props?: Omit<Record<string, any>, "$$slots" | "$$events"> | undefined`props: { `message: string`message: 'hello' }});`
```

In Svelte 4, rendering a component to a string also returned the CSS of all components. In Svelte 5, this is no longer the case by default because most of the time you're using a tooling chain that takes care of it in other ways (like SvelteKit). If you need CSS to be returned from `render`, you can set the `css` compiler option to `'injected'` and it will add `<style>` elements to the `head`.
###  Component typing changes[](https://svelte.dev/docs/svelte/v5-migration-guide#Components-are-no-longer-classes-Component-typing-changes)
The change from classes towards functions is also reflected in the typings: `SvelteComponent`, the base class from Svelte 4, is deprecated in favour of the new `Component` type which defines the function shape of a Svelte component. To manually define a component shape in a `d.ts` file:
```
import type { interface Component<Props extends Record<string, any> = {}, Exports extends Record<string, any> = {}, Bindings extends keyof Props | "" = string>


Can be used to create strongly typed Svelte components.


####
Example:[](https://svelte.dev/docs/svelte/v5-migration-guide#Example:)



You have component library on npm called component-library, from which
you export a component called MyComponent. For Svelte+TypeScript users,
you want to provide typings. Therefore you create a index.d.ts:





```
import type { Component } from 'svelte';
export declare const MyComponent: Component<{ foo: string }> {}
```

Typing this makes it possible for IDEs like VS Code with the Svelte extension to provide intellisense and to use the component like this in a Svelte file with TypeScript:
```
<script lang="ts">
	import { MyComponent } from "component-library";
</script>
<MyComponent foo={'bar'} />
```

[reference](https://svelte.dev/docs/svelte/svelte#Component)
Component } from 'svelte'; export declare const ````
const MyComponent: Component<{
    foo: string;
}, {}, string>
```
`MyComponent: `interface Component<Props extends Record<string, any> = {}, Exports extends Record<string, any> = {}, Bindings extends keyof Props | "" = string>`
Can be used to create strongly typed Svelte components.
####  Example:[](https://svelte.dev/docs/svelte/v5-migration-guide#Example:)
You have component library on npm called `component-library`, from which you export a component called `MyComponent`. For Svelte+TypeScript users, you want to provide typings. Therefore you create a `index.d.ts`:
```
import type { Component } from 'svelte';
export declare const MyComponent: Component<{ foo: string }> {}
```

Typing this makes it possible for IDEs like VS Code with the Svelte extension to provide intellisense and to use the component like this in a Svelte file with TypeScript:
```
<script lang="ts">
	import { MyComponent } from "component-library";
</script>
<MyComponent foo={'bar'} />
```

[reference](https://svelte.dev/docs/svelte/svelte#Component)
Component<{ `foo: string`foo: string; }>;`
```

To declare that a component of a certain type is required:
```
import { import ComponentAComponentA, import ComponentBComponentB } from 'component-library';

import type { interface Component<Props extends Record<string, any> = {}, Exports extends Record<string, any> = {}, Bindings extends keyof Props | "" = string>


Can be used to create strongly typed Svelte components.


####
Example:[](https://svelte.dev/docs/svelte/v5-migration-guide#Example:)



You have component library on npm called component-library, from which
you export a component called MyComponent. For Svelte+TypeScript users,
you want to provide typings. Therefore you create a index.d.ts:





```
import type { Component } from 'svelte';
export declare const MyComponent: Component<{ foo: string }> {}
```

Typing this makes it possible for IDEs like VS Code with the Svelte extension to provide intellisense and to use the component like this in a Svelte file with TypeScript:
```
<script lang="ts">
	import { MyComponent } from "component-library";
</script>
<MyComponent foo={'bar'} />
```

[reference](https://svelte.dev/docs/svelte/svelte#Component)
Component } from 'svelte'; let ````
let C: Component<{
    foo: string;
}, {}, string>
```
`C: `interface Component<Props extends Record<string, any> = {}, Exports extends Record<string, any> = {}, Bindings extends keyof Props | "" = string>`
Can be used to create strongly typed Svelte components.
####  Example:[](https://svelte.dev/docs/svelte/v5-migration-guide#Example:)
You have component library on npm called `component-library`, from which you export a component called `MyComponent`. For Svelte+TypeScript users, you want to provide typings. Therefore you create a `index.d.ts`:
```
import type { Component } from 'svelte';
export declare const MyComponent: Component<{ foo: string }> {}
```

Typing this makes it possible for IDEs like VS Code with the Svelte extension to provide intellisense and to use the component like this in a Svelte file with TypeScript:
```
<script lang="ts">
	import { MyComponent } from "component-library";
</script>
<MyComponent foo={'bar'} />
```

[reference](https://svelte.dev/docs/svelte/svelte#Component)
Component<{ `foo: string`foo: string }> = ````
function $state<any>(initial: any): any (+1 overload)
namespace $state
```
`
Declares reactive state.
Example:
```
let count = $state(0);
```

@see{@link <https://svelte.dev/docs/svelte/$state> Documentation}
@paraminitial The initial value
$state( `var Math: Math`
An intrinsic object that provides basic mathematics functionality and constants.
Math.`Math.random(): number`
Returns a pseudorandom number between 0 and 1.
random() ? `import ComponentA`ComponentA : `import ComponentB`ComponentB );`
```

The two utility types `ComponentEvents` and `ComponentType` are also deprecated. `ComponentEvents` is obsolete because events are defined as callback props now, and `ComponentType` is obsolete because the new `Component` type is the component type already (i.e. `ComponentType<SvelteComponent<{ prop: string }>>` is equivalent to `Component<{ prop: string }>`).
###  bind:this changes[](https://svelte.dev/docs/svelte/v5-migration-guide#Components-are-no-longer-classes-bind:this-changes)
Because components are no longer classes, using `bind:this` no longer returns a class instance with `$set`, `$on` and `$destroy` methods on it. It only returns the instance exports (`export function/const`) and, if you're using the `accessors` option, a getter/setter-pair for each property.
