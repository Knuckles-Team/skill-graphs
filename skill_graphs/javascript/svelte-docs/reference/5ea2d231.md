	Params extends AppLayoutParams<'/'> =
		AppLayoutParams<'/'>,
	ParentData extends Record<string, any> = Record<
		string,
		any
	>,
	OutputData extends Record<string, any> | void = Record<
		string,
		any
	> | void,
	RouteId extends AppRouteId | null = AppRouteId | null
> = (
	event: ServerLoadEvent<Params, ParentData, RouteId>
) => MaybePromise<OutputData>;
```

</div>

## ServerLoadEvent

<div class="ts-block">

```dts
interface ServerLoadEvent<
	Params extends AppLayoutParams<'/'> =
		AppLayoutParams<'/'>,
	ParentData extends Record<string, any> = Record<
		string,
		any
	>,
	RouteId extends AppRouteId | null = AppRouteId | null
> extends RequestEvent<Params, RouteId> {/*…*/}
```

<div class="ts-block-property">

```dts
parent: () => Promise<ParentData>;
```

<div class="ts-block-property-details">

`await parent()` returns data from parent `+layout.server.js` `load` functions.

Be careful not to introduce accidental waterfalls when using `await parent()`. If for example you only want to merge parent data into the returned output, call it _after_ fetching your other data.

</div>
</div>

<div class="ts-block-property">

```dts
depends: (...deps: string[]) => void;
```

<div class="ts-block-property-details">

This function declares that the `load` function has a _dependency_ on one or more URLs or custom identifiers, which can subsequently be used with [`invalidate()`](/docs/kit/$app-navigation#invalidate) to cause `load` to rerun.

Most of the time you won't need this, as `fetch` calls `depends` on your behalf — it's only necessary if you're using a custom API client that bypasses `fetch`.

URLs can be absolute or relative to the page being loaded, and must be [encoded](https://developer.mozilla.org/en-US/docs/Glossary/percent-encoding).

Custom identifiers have to be prefixed with one or more lowercase letters followed by a colon to conform to the [URI specification](https://www.rfc-editor.org/rfc/rfc3986.html).

The following example shows how to use `depends` to register a dependency on a custom identifier, which is `invalidate`d after a button click, making the `load` function rerun.

```js
// @errors: 7031
/// file: src/routes/+page.js
let count = 0;
export async function load({ depends }) {
	depends('increase:count');

	return { count: count++ };
}
```

```html
/// file: src/routes/+page.svelte
<script>
	import { invalidate } from '$app/navigation';

	let { data } = $props();

	const increase = async () => {
		await invalidate('increase:count');
	}
</script>

<p>{data.count}<p>
<button on:click={increase}>Increase Count</button>
```

</div>
</div>

<div class="ts-block-property">

```dts
untrack: <T>(fn: () => T) => T;
```

<div class="ts-block-property-details">

Use this function to opt out of dependency tracking for everything that is synchronously called within the callback. Example:

```js
// @errors: 7031
/// file: src/routes/+page.js
export async function load({ untrack, url }) {
	// Untrack url.pathname so that path changes don't trigger a rerun
	if (untrack(() => url.pathname === '/')) {
		return { message: 'Welcome!' };
	}
}
```

</div>
</div>

<div class="ts-block-property">

```dts
tracing: {/*…*/}
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- <span class="tag since">available since</span> v2.31.0

</div>

Access to spans for tracing. If tracing is not enabled, these spans will do nothing.

<div class="ts-block-property-children"><div class="ts-block-property">

```dts
enabled: boolean;
```

<div class="ts-block-property-details">

Whether tracing is enabled.

</div>
</div>
<div class="ts-block-property">

```dts
root: Span;
```

<div class="ts-block-property-details">

The root span for the request. This span is named `sveltekit.handle.root`.

</div>
</div>
<div class="ts-block-property">

```dts
current: Span;
```

<div class="ts-block-property-details">

The span associated with the current server `load` function.

</div>
</div></div>

</div>
</div></div>

## Snapshot

The type of `export const snapshot` exported from a page or layout component.

<div class="ts-block">

```dts
interface Snapshot<T = any> {/*…*/}
```

<div class="ts-block-property">

```dts
capture: () => T;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
restore: (snapshot: T) => void;
```

<div class="ts-block-property-details"></div>
</div></div>

## SubmitFunction

<div class="ts-block">

```dts
type SubmitFunction<
	Success extends Record<string, unknown> | undefined =
		Record<string, any>,
	Failure extends Record<string, unknown> | undefined =
		Record<string, any>
> = (input: {
	action: URL;
	formData: FormData;
	formElement: HTMLFormElement;
	controller: AbortController;
	submitter: HTMLElement | null;
	cancel: () => void;
}) => MaybePromise<
	| void
	| ((opts: {
			formData: FormData;
			formElement: HTMLFormElement;
			action: URL;
			result: ActionResult<Success, Failure>;
			/**
			 * Call this to get the default behavior of a form submission response.
			 * @param options Set `reset: false` if you don't want the `<form>` values to be reset after a successful submission.
			 * @param invalidateAll Set `invalidateAll: false` if you don't want the action to call `invalidateAll` after submission.
			 */
			update: (options?: {
				reset?: boolean;
				invalidateAll?: boolean;
			}) => Promise<void>;
	  }) => MaybePromise<void>)
>;
```

</div>

## Transport

<blockquote class="since note">

Available since 2.11.0

</blockquote>

The [`transport`](/docs/kit/hooks#Universal-hooks-transport) hook allows you to transport custom types across the server/client boundary.

Each transporter has a pair of `encode` and `decode` functions. On the server, `encode` determines whether a value is an instance of the custom type and, if so, returns a non-falsy encoding of the value which can be an object or an array (or `false` otherwise).

In the browser, `decode` turns the encoding back into an instance of the custom type.

```ts
import type { Transport } from '@sveltejs/kit';

declare class MyCustomType {
	data: any
}

// hooks.js
export const transport: Transport = {
	MyCustomType: {
		encode: (value) => value instanceof MyCustomType && [value.data],
		decode: ([data]) => new MyCustomType(data)
	}
};
```

<div class="ts-block">

```dts
type Transport = Record<string, Transporter>;
```

</div>

## Transporter

A member of the [`transport`](/docs/kit/hooks#Universal-hooks-transport) hook.

<div class="ts-block">

```dts
interface Transporter<
	T = any,
	U = Exclude<
		any,
		false | 0 | '' | null | undefined | typeof NaN
	>
> {/*…*/}
```

<div class="ts-block-property">

```dts
encode: (value: T) => false | U;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
decode: (data: U) => T;
```

<div class="ts-block-property-details"></div>
</div></div>

## ValidationError

A validation error thrown by `invalid`.

<div class="ts-block">

```dts
interface ValidationError {/*…*/}
```

<div class="ts-block-property">

```dts
issues: StandardSchemaV1.Issue[];
```

<div class="ts-block-property-details">

The validation issues

</div>
</div></div>

## Private types

The following are referenced by the public types documented above, but cannot be imported directly:

## AdapterEntry

<div class="ts-block">

```dts
interface AdapterEntry {/*…*/}
```

<div class="ts-block-property">

```dts
id: string;
```

<div class="ts-block-property-details">

A string that uniquely identifies an HTTP service (e.g. serverless function) and is used for deduplication.
For example, `/foo/a-[b]` and `/foo/[c]` are different routes, but would both
be represented in a Netlify _redirects file as `/foo/:param`, so they share an ID

</div>
</div>

<div class="ts-block-property">

```dts
filter(route: RouteDefinition): boolean;
```

<div class="ts-block-property-details">

A function that compares the candidate route with the current route to determine
if it should be grouped with the current route.

Use cases:
- Fallback pages: `/foo/[c]` is a fallback for `/foo/a-[b]`, and `/[...catchall]` is a fallback for all routes
- Grouping routes that share a common `config`: `/foo` should be deployed to the edge, `/bar` and `/baz` should be deployed to a serverless function

</div>
</div>

<div class="ts-block-property">

```dts
complete(entry: { generateManifest(opts: { relativePath: string }): string }): MaybePromise<void>;
```

<div class="ts-block-property-details">

A function that is invoked once the entry has been created. This is where you
should write the function to the filesystem and generate redirect manifests.

</div>
</div></div>

## Csp

<div class="ts-block">

```dts
namespace Csp {
	type ActionSource = 'strict-dynamic' | 'report-sample';
	type BaseSource =
		| 'self'
		| 'unsafe-eval'
		| 'unsafe-hashes'
		| 'unsafe-inline'
		| 'wasm-unsafe-eval'
		| 'none';
	type CryptoSource =
		`${'nonce' | 'sha256' | 'sha384' | 'sha512'}-${string}`;
	type FrameSource =
		| HostSource
		| SchemeSource
		| 'self'
		| 'none';
	type HostNameScheme = `${string}.${string}` | 'localhost';
	type HostSource =
		`${HostProtocolSchemes}${HostNameScheme}${PortScheme}`;
	type HostProtocolSchemes = `${string}://` | '';
	type HttpDelineator = '/' | '?' | '#' | '\\';
	type PortScheme = `:${number}` | '' | ':*';
	type SchemeSource =
		| 'http:'
		| 'https:'
		| 'data:'
		| 'mediastream:'
		| 'blob:'
		| 'filesystem:';
	type Source =
		| HostSource
		| SchemeSource
		| CryptoSource
		| BaseSource;
	type Sources = Source[];
}
```

</div>

## CspDirectives

<div class="ts-block">

```dts
interface CspDirectives {/*…*/}
```

<div class="ts-block-property">

```dts
'child-src'?: Csp.Sources;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'default-src'?: Array<Csp.Source | Csp.ActionSource>;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'frame-src'?: Csp.Sources;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'worker-src'?: Csp.Sources;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'connect-src'?: Csp.Sources;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'font-src'?: Csp.Sources;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'img-src'?: Csp.Sources;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'manifest-src'?: Csp.Sources;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'media-src'?: Csp.Sources;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'object-src'?: Csp.Sources;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'prefetch-src'?: Csp.Sources;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'script-src'?: Array<Csp.Source | Csp.ActionSource>;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'script-src-elem'?: Csp.Sources;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'script-src-attr'?: Csp.Sources;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'style-src'?: Array<Csp.Source | Csp.ActionSource>;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'style-src-elem'?: Csp.Sources;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'style-src-attr'?: Csp.Sources;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'base-uri'?: Array<Csp.Source | Csp.ActionSource>;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
sandbox?: Array<
| 'allow-downloads-without-user-activation'
| 'allow-forms'
| 'allow-modals'
| 'allow-orientation-lock'
| 'allow-pointer-lock'
| 'allow-popups'
| 'allow-popups-to-escape-sandbox'
| 'allow-presentation'
| 'allow-same-origin'
| 'allow-scripts'
| 'allow-storage-access-by-user-activation'
| 'allow-top-navigation'
| 'allow-top-navigation-by-user-activation'
>;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'form-action'?: Array<Csp.Source | Csp.ActionSource>;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'frame-ancestors'?: Array<Csp.HostSource | Csp.SchemeSource | Csp.FrameSource>;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'navigate-to'?: Array<Csp.Source | Csp.ActionSource>;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'report-uri'?: string[];
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'report-to'?: string[];
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'require-trusted-types-for'?: Array<'script'>;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'trusted-types'?: Array<'none' | 'allow-duplicates' | '*' | string>;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'upgrade-insecure-requests'?: boolean;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
'require-sri-for'?: Array<'script' | 'style' | 'script style'>;
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- <span class="tag deprecated">deprecated</span>

</div>

</div>
</div>

<div class="ts-block-property">

```dts
'block-all-mixed-content'?: boolean;
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- <span class="tag deprecated">deprecated</span>

</div>

</div>
</div>

<div class="ts-block-property">

```dts
'plugin-types'?: Array<`${string}/${string}` | 'none'>;
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- <span class="tag deprecated">deprecated</span>

</div>

</div>
</div>

<div class="ts-block-property">

```dts
referrer?: Array<
| 'no-referrer'
| 'no-referrer-when-downgrade'
| 'origin'
| 'origin-when-cross-origin'
| 'same-origin'
| 'strict-origin'
| 'strict-origin-when-cross-origin'
| 'unsafe-url'
| 'none'
>;
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- <span class="tag deprecated">deprecated</span>

</div>

</div>
</div></div>

## DeepPartial

<div class="ts-block">

```dts
type DeepPartial<T> = T extends
	| Record<PropertyKey, unknown>
	| unknown[]
	? {
			[K in keyof T]?: T[K] extends
				| Record<PropertyKey, unknown>
				| unknown[]
				? DeepPartial<T[K]>
				: T[K];
		}
	: T | undefined;
```

</div>

## HttpMethod

<div class="ts-block">

```dts
type HttpMethod =
	| 'GET'
	| 'HEAD'
	| 'POST'
	| 'PUT'
	| 'DELETE'
	| 'PATCH'
	| 'OPTIONS';
```

</div>

## IsAny

<div class="ts-block">

```dts
type IsAny<T> = 0 extends 1 & T ? true : false;
```

</div>

## Logger

<div class="ts-block">

```dts
interface Logger {/*…*/}
```

<div class="ts-block-property">

```dts
(msg: string): void;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
success(msg: string): void;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
error(msg: string): void;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
warn(msg: string): void;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
minor(msg: string): void;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
info(msg: string): void;
```

<div class="ts-block-property-details"></div>
</div></div>

## MaybePromise

<div class="ts-block">

```dts
type MaybePromise<T> = T | Promise<T>;
```

</div>

## PrerenderEntryGeneratorMismatchHandler

<div class="ts-block">

```dts
interface PrerenderEntryGeneratorMismatchHandler {/*…*/}
```

<div class="ts-block-property">

```dts
(details: { generatedFromId: string; entry: string; matchedId: string; message: string }): void;
```

<div class="ts-block-property-details"></div>
</div></div>

## PrerenderEntryGeneratorMismatchHandlerValue

<div class="ts-block">

```dts
type PrerenderEntryGeneratorMismatchHandlerValue =
	| 'fail'
	| 'warn'
	| 'ignore'
	| PrerenderEntryGeneratorMismatchHandler;
```

</div>

## PrerenderHttpErrorHandler

<div class="ts-block">

```dts
interface PrerenderHttpErrorHandler {/*…*/}
```

<div class="ts-block-property">

```dts
(details: {
status: number;
path: string;
referrer: string | null;
referenceType: 'linked' | 'fetched';
message: string;
}): void;
```

<div class="ts-block-property-details"></div>
</div></div>

## PrerenderHttpErrorHandlerValue

<div class="ts-block">

```dts
type PrerenderHttpErrorHandlerValue =
	| 'fail'
	| 'warn'
	| 'ignore'
	| PrerenderHttpErrorHandler;
```

</div>

## PrerenderMap

<div class="ts-block">

```dts
type PrerenderMap = Map<string, PrerenderOption>;
```

</div>

## PrerenderMissingIdHandler

<div class="ts-block">

```dts
interface PrerenderMissingIdHandler {/*…*/}
```

<div class="ts-block-property">

```dts
(details: { path: string; id: string; referrers: string[]; message: string }): void;
```

<div class="ts-block-property-details"></div>
</div></div>

## PrerenderMissingIdHandlerValue

<div class="ts-block">

```dts
type PrerenderMissingIdHandlerValue =
	| 'fail'
	| 'warn'
	| 'ignore'
	| PrerenderMissingIdHandler;
```

</div>

## PrerenderOption

<div class="ts-block">

```dts
type PrerenderOption = boolean | 'auto';
```

</div>

## PrerenderUnseenRoutesHandler

<div class="ts-block">

```dts
interface PrerenderUnseenRoutesHandler {/*…*/}
```

<div class="ts-block-property">

```dts
(details: { routes: string[]; message: string }): void;
```

<div class="ts-block-property-details"></div>
</div></div>

## PrerenderUnseenRoutesHandlerValue

<div class="ts-block">

```dts
type PrerenderUnseenRoutesHandlerValue =
	| 'fail'
	| 'warn'
	| 'ignore'
	| PrerenderUnseenRoutesHandler;
```

</div>

## Prerendered

<div class="ts-block">

```dts
interface Prerendered {/*…*/}
```

<div class="ts-block-property">

```dts
pages: Map<
string,
{
	/** The location of the .html file relative to the output directory */
	file: string;
}
>;
```

<div class="ts-block-property-details">

A map of `path` to `{ file }` objects, where a path like `/foo` corresponds to `foo.html` and a path like `/bar/` corresponds to `bar/index.html`.

</div>
</div>

<div class="ts-block-property">

```dts
assets: Map<
string,
{
	/** The MIME type of the asset */
	type: string;
}
>;
```

<div class="ts-block-property-details">

A map of `path` to `{ type }` objects.

</div>
</div>

<div class="ts-block-property">

```dts
redirects: Map<
string,
{
	status: number;
	location: string;
}
>;
```

<div class="ts-block-property-details">

A map of redirects encountered during prerendering.

</div>
</div>

<div class="ts-block-property">

```dts
paths: string[];
```

<div class="ts-block-property-details">

An array of prerendered paths (without trailing slashes, regardless of the trailingSlash config)

</div>
</div></div>

## RequestOptions

<div class="ts-block">

```dts
interface RequestOptions {/*…*/}
```

<div class="ts-block-property">

```dts
getClientAddress(): string;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
platform?: App.Platform;
```

<div class="ts-block-property-details"></div>
</div></div>

## RouteSegment

<div class="ts-block">

```dts
interface RouteSegment {/*…*/}
```

<div class="ts-block-property">

```dts
content: string;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
dynamic: boolean;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
rest: boolean;
```

<div class="ts-block-property-details"></div>
</div></div>

## TrailingSlash

<div class="ts-block">

```dts
type TrailingSlash = 'never' | 'always' | 'ignore';
```

</div>
