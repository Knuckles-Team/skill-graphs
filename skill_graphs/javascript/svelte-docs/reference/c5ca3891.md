		 * }
		 * ```
		 */
		refreshAll: () => Promise<void>;
	};
```

</div>

## Redirect

The object returned by the [`redirect`](/docs/kit/@sveltejs-kit#redirect) function.

<div class="ts-block">

```dts
interface Redirect {/*…*/}
```

<div class="ts-block-property">

```dts
status: 300 | 301 | 302 | 303 | 304 | 305 | 306 | 307 | 308;
```

<div class="ts-block-property-details">

The [HTTP status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#redirection_messages), in the range 300-308.

</div>
</div>

<div class="ts-block-property">

```dts
location: string;
```

<div class="ts-block-property-details">

The location to redirect to.

</div>
</div></div>

## RemoteCommand

The type of a remote `command` function. See [Remote functions](/docs/kit/remote-functions#command) for full documentation.

<div class="ts-block">

```dts
type RemoteCommand<Input, Output> = {
	(
		arg: undefined extends Input ? Input | void : Input
	): Promise<Output> & {
		updates(
			...updates: RemoteQueryUpdate[]
		): Promise<Output>;
	};
	/** The number of pending command executions */
	get pending(): number;
};
```

</div>

## RemoteForm

The type of a remote `form` function. See [Remote functions](/docs/kit/remote-functions#form) for full documentation.

<div class="ts-block">

```dts
type RemoteForm<
	Input extends RemoteFormInput | void,
	Output
> = {
	/** Attachment that sets up an event handler that intercepts the form submission on the client to prevent a full page reload */
	[attachment: symbol]: (node: HTMLFormElement) => void;
	method: 'POST';
	/** The URL to send the form to. */
	action: string;
	/** The `<form>` element this instance is currently attached to, if any. */
	get element(): HTMLFormElement | null;
	/** Submit the currently attached form programmatically. */
	submit(): Promise<boolean> & {
		updates: (
			...updates: RemoteQueryUpdate[]
		) => Promise<boolean>;
	};
	/** Use the `enhance` method to influence what happens when the form is submitted. */
	enhance(
		callback: (
			form: Omit<
				RemoteForm<Input, Output>,
				'enhance' | 'element'
			> & {
				readonly element: HTMLFormElement;
			}
		) => MaybePromise<void>
	): {
		method: 'POST';
		action: string;
		[attachment: symbol]: (node: HTMLFormElement) => void;
	};
	/**
	 * Create an instance of the form for the given `id`.
	 * The `id` is stringified and used for deduplication to potentially reuse existing instances.
	 * Useful when you have multiple forms that use the same remote form action, for example in a loop.
	 * ```svelte
	 * {#each todos as todo}
	 *	{@const todoForm = updateTodo.for(todo.id)}
	 *	<form {...todoForm}>
	 *		{#if todoForm.result?.invalid}<p>Invalid data</p>{/if}
	 *		...
	 *	</form>
	 *	{/each}
	 * ```
	 */
	for(
		id: ExtractId<Input>
	): Omit<RemoteForm<Input, Output>, 'for'>;
	/** Preflight checks */
	preflight(
		schema: StandardSchemaV1<Input, any>
	): RemoteForm<Input, Output>;
	/** Validate the form contents programmatically */
	validate(options?: {
		/** Set this to `true` to also show validation issues of fields that haven't been touched yet. */
		includeUntouched?: boolean;
		/** Set this to `true` to only run the `preflight` validation. */
		preflightOnly?: boolean;
	}): Promise<void>;
	/** The result of the form submission */
	get result(): Output | undefined;
	/** The number of pending submissions */
	get pending(): number;
	/** Access form fields using object notation */
	fields: RemoteFormFieldsRoot<Input>;
};
```

</div>

## RemoteFormField

Form field accessor type that provides name(), value(), and issues() methods

<div class="ts-block">

```dts
type RemoteFormField<Value extends RemoteFormFieldValue> =
	RemoteFormFieldMethods<Value> & {
		/**
		 * Returns an object that can be spread onto an input element with the correct type attribute,
		 * aria-invalid attribute if the field is invalid, and appropriate value/checked property getters/setters.
		 * @example
		 * ```svelte
		 * <input {...myForm.fields.myString.as('text')} />
		 * <input {...myForm.fields.myNumber.as('number')} />
		 * <input {...myForm.fields.myBoolean.as('checkbox')} />
		 * ```
		 */
		as<T extends RemoteFormFieldType<Value>>(
			...args: AsArgs<T, Value>
		): InputElementProps<T>;
	};
```

</div>

## RemoteFormFieldType

<div class="ts-block">

```dts
type RemoteFormFieldType<T> = {
	[K in keyof InputTypeMap]: T extends InputTypeMap[K]
		? K
		: never;
}[keyof InputTypeMap];
```

</div>

## RemoteFormFieldValue

<div class="ts-block">

```dts
type RemoteFormFieldValue =
	| string
	| string[]
	| number
	| boolean
	| File
	| File[];
```

</div>

## RemoteFormFields

Recursive type to build form fields structure with proxy access

<div class="ts-block">

```dts
type RemoteFormFields<T> =
	WillRecurseIndefinitely<T> extends true
		? RecursiveFormFields
		: NonNullable<T> extends
					| string
					| number
					| boolean
					| File
			? RemoteFormField<NonNullable<T>>
			: // [NonNullable<T>] is used to prevent distributing over union while still allowing
				// nullable wrappers (e.g. `string[] | undefined` from a schema with `.default([])`)
				// to be treated as arrays; only the last condition should distribute over unions
				[NonNullable<T>] extends [string[] | File[]]
				? RemoteFormField<NonNullable<T>> & {
						[K in number]: RemoteFormField<
							NonNullable<T>[number]
						>;
					}
				: [NonNullable<T>] extends [Array<infer U>]
					? RemoteFormFieldContainer<NonNullable<T>> & {
							[K in number]: RemoteFormFields<U>;
						}
					: RemoteFormFieldContainer<T> & {
							[K in KeysOfUnion<T>]-?: RemoteFormFields<
								ValueOfUnionKey<T, K>
							>;
						};
```

</div>

## RemoteFormInput

<div class="ts-block">

```dts
interface RemoteFormInput {/*…*/}
```

<div class="ts-block-property">

```dts
[key: string]: MaybeArray<string | number | boolean | File | RemoteFormInput>;
```

<div class="ts-block-property-details"></div>
</div></div>

## RemoteFormIssue

<div class="ts-block">

```dts
interface RemoteFormIssue {/*…*/}
```

<div class="ts-block-property">

```dts
message: string;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
path: Array<string | number>;
```

<div class="ts-block-property-details"></div>
</div></div>

## RemoteLiveQuery

<div class="ts-block">

```dts
type RemoteLiveQuery<T> = RemoteResource<T> &
	AsyncIterable<T> & {
		/** `true` if the live stream is currently connected. */
		readonly connected: boolean;
		/** `true` once the current live stream iterator is done. */
		readonly done: boolean;
		/** Reconnects the live stream immediately. */
		reconnect(): Promise<void>;
	};
```

</div>

## RemoteLiveQueryFunction

The type of a remote `query.live` function. See [Remote functions](/docs/kit/remote-functions#query.live) for full documentation.

The optional `Validated` generic parameter represents the argument type *after* the
query's schema has validated and (optionally) transformed it, and matches the type
yielded by [`requested`](/docs/kit/$app-server#requested).

<div class="ts-block">

```dts
type RemoteLiveQueryFunction<
	Input,
	Output,
	_Validated = Input
> = (
	arg: undefined extends Input ? Input | void : Input
) => RemoteLiveQuery<Output>;
```

</div>

## RemotePrerenderFunction

The type of a remote `prerender` function. See [Remote functions](/docs/kit/remote-functions#prerender) for full documentation.

<div class="ts-block">

```dts
type RemotePrerenderFunction<Input, Output> = (
	arg: undefined extends Input ? Input | void : Input
) => RemoteResource<Output>;
```

</div>

## RemoteQuery

<div class="ts-block">

```dts
type RemoteQuery<T> = RemoteResource<T> & {
	/**
	 * On the client, this function will update the value of the query without re-fetching it.
	 *
	 * On the server, this can be called in the context of a `command` or `form` and the specified data will accompany the action response back to the client.
	 * This prevents SvelteKit needing to refresh all queries on the page in a second server round-trip.
	 */
	set(value: T): void;
	/**
	 * On the client, this function will re-fetch the query from the server.
	 *
	 * On the server, this can be called in the context of a `command` or `form` and the refreshed data will accompany the action response back to the client.
	 * This prevents SvelteKit needing to refresh all queries on the page in a second server round-trip.
	 */
	refresh(): Promise<void>;
	/**
	 * Temporarily override a query's value during a [single-flight mutation](https://svelte.dev/docs/kit/remote-functions#Single-flight-mutations) to provide optimistic updates.
	 *
	 * ```svelte
	 * <script>
	 *   import { getTodos, addTodo } from './todos.remote.js';
	 *   const todos = getTodos();
	 * </script>
	 *
	 * <form {...addTodo.enhance(async (form) => {
	 *   await form.submit().updates(
	 *     todos.withOverride((todos) => [...todos, { text: form.fields.text.value() }])
	 *   );
	 * })}>
	 *   <input type="text" name="text" />
	 *   <button type="submit">Add Todo</button>
	 * </form>
	 * ```
	 */
	withOverride(
		update: (current: T) => T
	): RemoteQueryOverride;
};
```

</div>

## RemoteQueryFunction

The return value of a remote `query` function. See [Remote functions](/docs/kit/remote-functions#query) for full documentation.

The optional `Validated` generic parameter represents the argument type *after* the
query's schema has validated and (optionally) transformed it — this is the type the
query's implementation function receives on the server, and the type yielded by
[`requested`](/docs/kit/$app-server#requested). For queries declared
with [Standard Schema](https://standardschema.dev/) it differs from `Input` when the
schema contains a transform (e.g. `v.pipe(v.number(), v.transform(String))` has
`Input = number` but `Validated = string`). For `'unchecked'` validators and queries
without arguments it defaults to `Input`.

<div class="ts-block">

```dts
type RemoteQueryFunction<
	Input,
	Output,
	_Validated = Input
> = (
	arg: undefined extends Input ? Input | void : Input
) => RemoteQuery<Output>;
```

</div>

## RemoteQueryOverride

<div class="ts-block">

```dts
type RemoteQueryOverride = () => void;
```

</div>

## RemoteQueryUpdate

<div class="ts-block">

```dts
type RemoteQueryUpdate =
	| RemoteQuery<any>
	| RemoteLiveQuery<any>
	| RemoteQueryFunction<any, any>
	| RemoteLiveQueryFunction<any, any>
	| RemoteQueryOverride;
```

</div>

## RemoteResource

<div class="ts-block">

```dts
type RemoteResource<T> = Promise<T> & {
	/** The error in case the query fails. Most often this is a [`HttpError`](https://svelte.dev/docs/kit/@sveltejs-kit#HttpError) but it isn't guaranteed to be. */
	get error(): any;
	/** `true` before the first result is available and during refreshes */
	get loading(): boolean;
} & (
		| {
				/** The current value of the query. Undefined until `ready` is `true` */
				get current(): undefined;
				ready: false;
		  }
		| {
				/** The current value of the query. Undefined until `ready` is `true` */
				get current(): T;
				ready: true;
		  }
	);
```

</div>

## RequestEvent

<div class="ts-block">

```dts
interface RequestEvent<
	Params extends AppLayoutParams<'/'> =
		AppLayoutParams<'/'>,
	RouteId extends AppRouteId | null = AppRouteId | null
> {/*…*/}
```

<div class="ts-block-property">

```dts
cookies: Cookies;
```

<div class="ts-block-property-details">

Get or set cookies related to the current request

</div>
</div>

<div class="ts-block-property">

```dts
fetch: typeof fetch;
```

<div class="ts-block-property-details">

`fetch` is equivalent to the [native `fetch` web API](https://developer.mozilla.org/en-US/docs/Web/API/fetch), with a few additional features:

- It can be used to make credentialed requests on the server, as it inherits the `cookie` and `authorization` headers for the page request.
- It can make relative requests on the server (ordinarily, `fetch` requires a URL with an origin when used in a server context).
- Internal requests (e.g. for `+server.js` routes) go directly to the handler function when running on the server, without the overhead of an HTTP call.
- During server-side rendering, the response will be captured and inlined into the rendered HTML by hooking into the `text` and `json` methods of the `Response` object. Note that headers will _not_ be serialized, unless explicitly included via [`filterSerializedResponseHeaders`](/docs/kit/hooks#Server-hooks-handle)
- During hydration, the response will be read from the HTML, guaranteeing consistency and preventing an additional network request.

You can learn more about making credentialed requests with cookies [here](/docs/kit/load#Cookies).

</div>
</div>

<div class="ts-block-property">

```dts
getClientAddress: () => string;
```

<div class="ts-block-property-details">

The client's IP address, set by the adapter.

</div>
</div>

<div class="ts-block-property">

```dts
locals: App.Locals;
```

<div class="ts-block-property-details">

Contains custom data that was added to the request within the [`server handle hook`](/docs/kit/hooks#Server-hooks-handle).

</div>
</div>

<div class="ts-block-property">

```dts
params: Params;
```

<div class="ts-block-property-details">

The parameters of the current route - e.g. for a route like `/blog/[slug]`, a `{ slug: string }` object.

In the context of a remote function request initiated by the client, this relates to the page the remote function
was called from, _not_ the URL of the endpoint SvelteKit creates for the remote function. Never use this to determine
whether or not a user is authorized to access certain data, as these values are part of the request which could be manipulated.

</div>
</div>

<div class="ts-block-property">

```dts
platform: Readonly<App.Platform> | undefined;
```

<div class="ts-block-property-details">

Additional data made available through the adapter.

</div>
</div>

<div class="ts-block-property">

```dts
request: Request;
```

<div class="ts-block-property-details">

The original request object.

</div>
</div>

<div class="ts-block-property">

```dts
route: {/*…*/}
```

<div class="ts-block-property-details">

Info about the current route.

<div class="ts-block-property-children"><div class="ts-block-property">

```dts
id: RouteId;
```

<div class="ts-block-property-details">

The ID of the current route - e.g. for `src/routes/blog/[slug]`, it would be `/blog/[slug]`. It is `null` when no route is matched.

In the context of a remote function request initiated by the client, this relates to the page the remote function
was called from, _not_ the URL of the endpoint SvelteKit creates for the remote function. Never use this to determine
whether or not a user is authorized to access certain data, as these values are part of the request which could be manipulated.

</div>
</div></div>

</div>
</div>

<div class="ts-block-property">

```dts
setHeaders: (headers: Record<string, string>) => void;
```

<div class="ts-block-property-details">

If you need to set headers for the response, you can do so using the this method. This is useful if you want the page to be cached, for example:

```js
// @errors: 7031
/// file: src/routes/blog/+page.js
export async function load({ fetch, setHeaders }) {
	const url = `https://cms.example.com/articles.json`;
	const response = await fetch(url);

	setHeaders({
		age: response.headers.get('age'),
		'cache-control': response.headers.get('cache-control')
	});

	return response.json();
}
```

Setting the same header multiple times (even in separate `load` functions) is an error — you can only set a given header once.

You cannot add a `set-cookie` header with `setHeaders` — use the [`cookies`](/docs/kit/@sveltejs-kit#Cookies) API instead.

</div>
</div>

<div class="ts-block-property">

```dts
url: URL;
```

<div class="ts-block-property-details">

The requested URL.

In the context of a remote function request initiated by the client, this relates to the page the remote function
was called from, _not_ the URL of the endpoint SvelteKit creates for the remote function. Never use this to determine
whether or not a user is authorized to access certain data, as these values are part of the request which could be manipulated.

</div>
</div>

<div class="ts-block-property">

```dts
isDataRequest: boolean;
```

<div class="ts-block-property-details">

`true` if the request comes from the client asking for `+page/layout.server.js` data. The `url` property will be stripped of the internal information
related to the data request in this case. Use this property instead if the distinction is important to you.

</div>
</div>

<div class="ts-block-property">

```dts
isSubRequest: boolean;
```

<div class="ts-block-property-details">

`true` for `+server.js` calls coming from SvelteKit without the overhead of actually making an HTTP request. This happens when you make same-origin `fetch` requests on the server.

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

The span associated with the current `handle` hook, `load` function, or form action.

</div>
</div></div>

</div>
</div>

<div class="ts-block-property">

```dts
isRemoteRequest: boolean;
```

<div class="ts-block-property-details">

`true` if the request comes from the client via a remote function. The `url` property will be stripped of the internal information
related to the data request in this case. Use this property instead if the distinction is important to you.

</div>
</div></div>

## RequestHandler

A `(event: RequestEvent) => Response` function exported from a `+server.js` file that corresponds to an HTTP verb (`GET`, `PUT`, `PATCH`, etc) and handles requests with that method.

It receives `Params` as the first generic argument, which you can skip by using [generated types](/docs/kit/types#Generated-types) instead.

<div class="ts-block">

```dts
type RequestHandler<
	Params extends AppLayoutParams<'/'> =
		AppLayoutParams<'/'>,
	RouteId extends AppRouteId | null = AppRouteId | null
> = (
	event: RequestEvent<Params, RouteId>
) => MaybePromise<Response>;
```

</div>

## RequestedEntry

A single entry yielded by [`requested`](/docs/kit/$app-server#requested)
when called with a regular `query`. `arg` is the validated argument (the input *after*
the query's schema validated and transformed it, if applicable); `query` is a
`RemoteQuery` bound to the client's original cache key, so `refresh()` / `set()` will
update the correct client entry.

<div class="ts-block">

```dts
type RequestedEntry<Validated, Output> = {
	arg: Validated;
	query: RemoteQuery<Output>;
};
```

</div>

## RequestedResult

<div class="ts-block">

```dts
type RequestedResult<Validated, Output> =
	| QueryRequestedResult<Validated, Output>
	| LiveQueryRequestedResult<Validated, Output>;
```

</div>

## Reroute

<blockquote class="since note">

Available since 2.3.0

</blockquote>

The [`reroute`](/docs/kit/hooks#Universal-hooks-reroute) hook allows you to modify the URL before it is used to determine which route to render.

<div class="ts-block">

```dts
type Reroute = (event: {
	url: URL;
	fetch: typeof fetch;
}) => MaybePromise<void | string>;
```

</div>

## ResolveOptions

<div class="ts-block">

```dts
interface ResolveOptions {/*…*/}
```

<div class="ts-block-property">

```dts
transformPageChunk?: (input: { html: string; done: boolean }) => MaybePromise<string | undefined>;
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- `input` the html chunk and the info if this is the last chunk

</div>

Applies custom transforms to HTML. If `done` is true, it's the final chunk. Chunks are not guaranteed to be well-formed HTML
(they could include an element's opening tag but not its closing tag, for example)
but they will always be split at sensible boundaries such as `%sveltekit.head%` or layout/page components.

</div>
</div>

<div class="ts-block-property">

```dts
filterSerializedResponseHeaders?: (name: string, value: string) => boolean;
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- `name` header name
- `value` header value

</div>

Determines which headers should be included in serialized responses when a `load` function loads a resource with `fetch`.
By default, none will be included.

</div>
</div>

<div class="ts-block-property">

```dts
preload?: (input: { type: 'font' | 'css' | 'js' | 'asset'; path: string }) => boolean;
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- `input` the type of the file and its path

</div>

Determines what should be added to the `<head>` tag to preload it.
By default, `js` and `css` files will be preloaded.

</div>
</div></div>

## RouteDefinition

<div class="ts-block">

```dts
interface RouteDefinition<Config = any> {/*…*/}
```

<div class="ts-block-property">

```dts
id: string;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
api: {
	methods: Array<HttpMethod | '*'>;
};
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
page: {
	methods: Array<Extract<HttpMethod, 'GET' | 'POST'>>;
};
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
pattern: RegExp;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
prerender: PrerenderOption;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
segments: RouteSegment[];
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
methods: Array<HttpMethod | '*'>;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
config: Config;
```

<div class="ts-block-property-details"></div>
</div></div>

## SSRManifest

<div class="ts-block">

```dts
interface SSRManifest {/*…*/}
```

<div class="ts-block-property">

```dts
appDir: string;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
appPath: string;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
assets: Set<string>;
```

<div class="ts-block-property-details">

Static files from `kit.config.files.assets` and the service worker (if any).

</div>
</div>

<div class="ts-block-property">

```dts
mimeTypes: Record<string, string>;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
_: {/*…*/}
```

<div class="ts-block-property-details">

private fields

<div class="ts-block-property-children"><div class="ts-block-property">

```dts
client: BuildData['client'];
```

<div class="ts-block-property-details"></div>
</div>
<div class="ts-block-property">

```dts
nodes: SSRNodeLoader[];
```

<div class="ts-block-property-details"></div>
</div>
<div class="ts-block-property">

```dts
remotes: Record<string, () => Promise<any>>;
```

<div class="ts-block-property-details">

hashed filename -> import to that file

</div>
</div>
<div class="ts-block-property">

```dts
routes: SSRRoute[];
```

<div class="ts-block-property-details"></div>
</div>
<div class="ts-block-property">

```dts
prerendered_routes: Set<string>;
```

<div class="ts-block-property-details"></div>
</div>
<div class="ts-block-property">

```dts
matchers: () => Promise<Record<string, ParamMatcher>>;
```

<div class="ts-block-property-details"></div>
</div>
<div class="ts-block-property">

```dts
server_assets: Record<string, number>;
```

<div class="ts-block-property-details">

A `[file]: size` map of all assets imported by server code.

</div>
</div></div>

</div>
</div></div>

## ServerInit

<blockquote class="since note">

Available since 2.10.0

</blockquote>

The [`init`](/docs/kit/hooks#Shared-hooks-init) will be invoked before the server responds to its first request

<div class="ts-block">

```dts
type ServerInit = () => MaybePromise<void>;
```

</div>

## ServerInitOptions

<div class="ts-block">

```dts
interface ServerInitOptions {/*…*/}
```

<div class="ts-block-property">

```dts
env: Record<string, string>;
```

<div class="ts-block-property-details">

A map of environment variables.

</div>
</div>

<div class="ts-block-property">

```dts
read?: (file: string) => MaybePromise<ReadableStream | null>;
```

<div class="ts-block-property-details">

A function that turns an asset filename into a `ReadableStream`. Required for the `read` export from `$app/server` to work.

</div>
</div></div>

## ServerLoad

The generic form of `PageServerLoad` and `LayoutServerLoad`. You should import those from `./$types` (see [generated types](/docs/kit/types#Generated-types))
rather than using `ServerLoad` directly.

<div class="ts-block">

```dts
type ServerLoad<
