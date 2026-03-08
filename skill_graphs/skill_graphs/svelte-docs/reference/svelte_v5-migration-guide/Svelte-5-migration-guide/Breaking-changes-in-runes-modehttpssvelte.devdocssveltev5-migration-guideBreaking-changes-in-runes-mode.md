##  Breaking changes in runes mode[](https://svelte.dev/docs/svelte/v5-migration-guide#Breaking-changes-in-runes-mode)
Some breaking changes only apply once your component is in runes mode.
###  Bindings to component exports are not allowed[](https://svelte.dev/docs/svelte/v5-migration-guide#Breaking-changes-in-runes-mode-Bindings-to-component-exports-are-not-allowed)
Exports from runes mode components cannot be bound to directly. For example, having `export const foo = ...` in component `A` and then doing `<A bind:foo />` causes an error. Use `bind:this` instead — `<A bind:this={a} />` — and access the export as `a.foo`. This change makes things easier to reason about, as it enforces a clear separation between props and exports.
###  Bindings need to be explicitly defined using $bindable()[](https://svelte.dev/docs/svelte/v5-migration-guide#Breaking-changes-in-runes-mode-Bindings-need-to-be-explicitly-defined-using-$bindable\(\))
In Svelte 4 syntax, every property (declared via `export let`) is bindable, meaning you can `bind:` to it. In runes mode, properties are not bindable by default: you need to denote bindable props with the `$bindable` rune.
If a bindable property has a default value (e.g. `let { foo = $bindable('bar') } = $props();`), you need to pass a non-`undefined` value to that property if you're binding to it. This prevents ambiguous behavior — the parent and child must have the same value — and results in better performance (in Svelte 4, the default value was reflected back to the parent, resulting in wasteful additional render cycles).
###  accessors option is ignored[](https://svelte.dev/docs/svelte/v5-migration-guide#Breaking-changes-in-runes-mode-accessors-option-is-ignored)
Setting the `accessors` option to `true` makes properties of a component directly accessible on the component instance.
```
<svelte:options accessors={true} />

<script>
	// available via componentInstance.name
	export let name;
</script>
```

In runes mode, properties are never accessible on the component instance. You can use component exports instead if you need to expose them.
```
<script>
	let { name } = $props();
	// available via componentInstance.getName()
	export const getName = () => name;
</script>
```

Alternatively, if the place where they are instantiated is under your control, you can also make use of runes inside `.js/.ts` files by adjusting their ending to include `.svelte`, i.e. `.svelte.js` or `.svelte.ts`, and then use `$state`:
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

###  immutable option is ignored[](https://svelte.dev/docs/svelte/v5-migration-guide#Breaking-changes-in-runes-mode-immutable-option-is-ignored)
Setting the `immutable` option has no effect in runes mode. This concept is replaced by how `$state` and its variations work.
###  Classes are no longer "auto-reactive"[](https://svelte.dev/docs/svelte/v5-migration-guide#Breaking-changes-in-runes-mode-Classes-are-no-longer-auto-reactive)
In Svelte 4, doing the following triggered reactivity:
```
<script>
	let foo = new Foo();
</script>

<button on:click={() => (foo.value = 1)}>{foo.value}</button
>
```

This is because the Svelte compiler treated the assignment to `foo.value` as an instruction to update anything that referenced `foo`. In Svelte 5, reactivity is determined at runtime rather than compile time, so you should define `value` as a reactive `$state` field on the `Foo` class. Wrapping `new Foo()` with `$state(...)` will have no effect — only vanilla objects and arrays are made deeply reactive.
###  Touch events are passive[](https://svelte.dev/docs/svelte/v5-migration-guide#Breaking-changes-in-runes-mode-Touch-events-are-passive)
When using `ontouchstart` and `ontouchmove` event attributes, the handlers are `event.preventDefault()`.
In the very rare cases that you need to prevent these event defaults, you should use [`on`](https://svelte.dev/docs/svelte/svelte-events#on) instead (for example inside an action).
###  Attribute/prop syntax is stricter[](https://svelte.dev/docs/svelte/v5-migration-guide#Breaking-changes-in-runes-mode-Attribute-prop-syntax-is-stricter)
In Svelte 4, complex attribute values needn't be quoted:
```
<Component prop=this{is}valid />
```

This is a footgun. In runes mode, if you want to concatenate stuff you must wrap the value in quotes:
```
<Component prop="this{is}valid" />
```

Note that Svelte 5 will also warn if you have a single expression wrapped in quotes, like `answer="{42}"` — in Svelte 6, that will cause the value to be converted to a string, rather than passed as a number.
###  HTML structure is stricter[](https://svelte.dev/docs/svelte/v5-migration-guide#Breaking-changes-in-runes-mode-HTML-structure-is-stricter)
In Svelte 4, you were allowed to write HTML code that would be repaired by the browser when server-side rendering it. For example you could write this...
```
<table>
	<tr>
		<td>hi</td>
	</tr>
</table>
```

... and the browser would auto-insert a `<tbody>` element:
```
<table>
	<tbody>
		<tr>
			<td>hi</td>
		</tr>
	</tbody>
</table>
```

Svelte 5 is more strict about the HTML structure and will throw a compiler error in cases where the browser would repair the DOM.
