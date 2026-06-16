
The [`handle`](/docs/kit/hooks#Server-hooks-handle) hook runs every time the SvelteKit server receives a [request](/docs/kit/web-standards#Fetch-APIs-Request) and
determines the [response](/docs/kit/web-standards#Fetch-APIs-Response).
It receives an `event` object representing the request and a function called `resolve`, which renders the route and generates a `Response`.
This allows you to modify response headers or bodies, or bypass SvelteKit entirely (for implementing routes programmatically, for example).

<div class="ts-block">

```dts
type Handle = (input: {
	event: RequestEvent;
	resolve: (
		event: RequestEvent,
		opts?: ResolveOptions
	) => MaybePromise<Response>;
}) => MaybePromise<Response>;
```

</div>

## HandleClientError

The client-side [`handleError`](/docs/kit/hooks#Shared-hooks-handleError) hook runs when an unexpected error is thrown while navigating.

If an unexpected error is thrown during loading or the following render, this function will be called with the error and the event.
Make sure that this function _never_ throws an error.

<div class="ts-block">

```dts
type HandleClientError = (input: {
	error: unknown;
	event: NavigationEvent;
	status: number;
	message: string;
}) => MaybePromise<void | App.Error>;
```

</div>

## HandleFetch

The [`handleFetch`](/docs/kit/hooks#Server-hooks-handleFetch) hook allows you to modify (or replace) the result of an [`event.fetch`](/docs/kit/load#Making-fetch-requests) call that runs on the server (or during prerendering) inside an endpoint, `load`, `action`, `handle`, `handleError` or `reroute`.

<div class="ts-block">

```dts
type HandleFetch = (input: {
	event: RequestEvent;
	request: Request;
	fetch: typeof fetch;
}) => MaybePromise<Response>;
```

</div>

## HandleServerError

The server-side [`handleError`](/docs/kit/hooks#Shared-hooks-handleError) hook runs when an unexpected error is thrown while responding to a request.

If an unexpected error is thrown during loading or rendering, this function will be called with the error and the event.
Make sure that this function _never_ throws an error.

<div class="ts-block">

```dts
type HandleServerError = (input: {
	error: unknown;
	event: RequestEvent;
	status: number;
	message: string;
}) => MaybePromise<void | App.Error>;
```

</div>

## HandleValidationError

The [`handleValidationError`](/docs/kit/hooks#Server-hooks-handleValidationError) hook runs when the argument to a remote function fails validation.

It will be called with the validation issues and the event, and must return an object shape that matches `App.Error`.

<div class="ts-block">

```dts
type HandleValidationError<
	Issue extends StandardSchemaV1.Issue =
		StandardSchemaV1.Issue
> = (input: {
	issues: Issue[];
	event: RequestEvent;
}) => MaybePromise<App.Error>;
```

</div>

## HttpError

The object returned by the [`error`](/docs/kit/@sveltejs-kit#error) function.

<div class="ts-block">

```dts
interface HttpError {/*…*/}
```

<div class="ts-block-property">

```dts
status: number;
```

<div class="ts-block-property-details">

The [HTTP status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#client_error_responses), in the range 400-599.

</div>
</div>

<div class="ts-block-property">

```dts
body: App.Error;
```

<div class="ts-block-property-details">

The content of the error.

</div>
</div></div>

## InvalidField

A function and proxy object used to imperatively create validation errors in form handlers.

Access properties to create field-specific issues: `issue.fieldName('message')`.
The type structure mirrors the input data structure for type-safe field access.
Call `invalid(issue.foo(...), issue.nested.bar(...))` to throw a validation error.

<div class="ts-block">

```dts
type InvalidField<T> =
	WillRecurseIndefinitely<T> extends true
		? Record<string | number, any>
		: NonNullable<T> extends
					| string
					| number
					| boolean
					| File
			? (message: string) => StandardSchemaV1.Issue
			: NonNullable<T> extends Array<infer U>
				? {
						[K in number]: InvalidField<U>;
					} & ((message: string) => StandardSchemaV1.Issue)
				: NonNullable<T> extends RemoteFormInput
					? {
							[K in keyof T]-?: InvalidField<T[K]>;
						} & ((
							message: string
						) => StandardSchemaV1.Issue)
					: Record<string, never>;
```

</div>

## KitConfig

See the [configuration reference](/docs/kit/configuration) for details.

## LessThan

<div class="ts-block">

```dts
type LessThan<
	TNumber extends number,
	TArray extends any[] = []
> = TNumber extends TArray['length']
	? TArray[number]
	: LessThan<TNumber, [...TArray, TArray['length']]>;
```

</div>

## LiveQueryRequestedResult

<div class="ts-block">

```dts
type LiveQueryRequestedResult<Validated, Output> = Iterable<
	LiveRequestedEntry<Validated, Output>
> &
	AsyncIterable<LiveRequestedEntry<Validated, Output>> & {
		/**
		 * Call `reconnect` on all live queries selected by this `requested` invocation.
		 * This is identical to:
		 * ```ts
		 * import { requested } from '$app/server';
		 *
		 * for await (const { query } of requested(liveQuery, ...)) {
		 *   void query.reconnect();
		 * }
		 * ```
		 */
		reconnectAll: () => Promise<void>;
	};
```

</div>

## LiveRequestedEntry

A single entry yielded by [`requested`](/docs/kit/$app-server#requested)
when called with a `query.live`. `arg` is the validated argument; `query` is a
`RemoteLiveQuery` bound to the client's original cache key, so `reconnect()` targets
the correct client subscription.

<div class="ts-block">

```dts
type LiveRequestedEntry<Validated, Output> = {
	arg: Validated;
	query: RemoteLiveQuery<Output>;
};
```

</div>

## Load

The generic form of `PageLoad` and `LayoutLoad`. You should import those from `./$types` (see [generated types](/docs/kit/types#Generated-types))
rather than using `Load` directly.

<div class="ts-block">

```dts
type Load<
	Params extends AppLayoutParams<'/'> =
		AppLayoutParams<'/'>,
	InputData extends Record<string, unknown> | null = Record<
		string,
		any
	> | null,
	ParentData extends Record<string, unknown> = Record<
		string,
		any
	>,
	OutputData extends Record<string, unknown> | void =
		Record<string, any> | void,
	RouteId extends AppRouteId | null = AppRouteId | null
> = (
	event: LoadEvent<Params, InputData, ParentData, RouteId>
) => MaybePromise<OutputData>;
```

</div>

## LoadEvent

The generic form of `PageLoadEvent` and `LayoutLoadEvent`. You should import those from `./$types` (see [generated types](/docs/kit/types#Generated-types))
rather than using `LoadEvent` directly.

<div class="ts-block">

```dts
interface LoadEvent<
	Params extends AppLayoutParams<'/'> =
		AppLayoutParams<'/'>,
	Data extends Record<string, unknown> | null = Record<
		string,
		any
	> | null,
	ParentData extends Record<string, unknown> = Record<
		string,
		any
	>,
	RouteId extends AppRouteId | null = AppRouteId | null
> extends NavigationEvent<Params, RouteId> {/*…*/}
```

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

You can learn more about making credentialed requests with cookies [here](/docs/kit/load#Cookies)

</div>
</div>

<div class="ts-block-property">

```dts
data: Data;
```

<div class="ts-block-property-details">

Contains the data returned by the route's server `load` function (in `+layout.server.js` or `+page.server.js`), if any.

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

You cannot add a `set-cookie` header with `setHeaders` — use the [`cookies`](/docs/kit/@sveltejs-kit#Cookies) API in a server-only `load` function instead.

`setHeaders` has no effect when a `load` function runs in the browser.

</div>
</div>

<div class="ts-block-property">

```dts
parent: () => Promise<ParentData>;
```

<div class="ts-block-property-details">

`await parent()` returns data from parent `+layout.js` `load` functions.
Implicitly, a missing `+layout.js` is treated as a `({ data }) => data` function, meaning that it will return and forward data from parent `+layout.server.js` files.

Be careful not to introduce accidental waterfalls when using `await parent()`. If for example you only want to merge parent data into the returned output, call it _after_ fetching your other data.

</div>
</div>

<div class="ts-block-property">

```dts
depends: (...deps: Array<`${string}:${string}`>) => void;
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
/// file: src/routes/+page.server.js
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

Access to spans for tracing. If tracing is not enabled or the function is being run in the browser, these spans will do nothing.

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

The span associated with the current `load` function.

</div>
</div></div>

</div>
</div></div>

## LoadProperties

<div class="ts-block">

```dts
type LoadProperties<
	input extends Record<string, any> | void
> = input extends void
	? undefined // needs to be undefined, because void will break intellisense
	: input extends Record<string, any>
		? input
		: unknown;
```

</div>

## Navigation

<div class="ts-block">

```dts
type Navigation =
	| NavigationExternal
	| NavigationFormSubmit
	| NavigationPopState
	| NavigationLink;
```

</div>

## NavigationBase

<div class="ts-block">

```dts
interface NavigationBase {/*…*/}
```

<div class="ts-block-property">

```dts
from: NavigationTarget | null;
```

<div class="ts-block-property-details">

Where navigation was triggered from

</div>
</div>

<div class="ts-block-property">

```dts
to: NavigationTarget | null;
```

<div class="ts-block-property-details">

Where navigation is going to/has gone to

</div>
</div>

<div class="ts-block-property">

```dts
willUnload: boolean;
```

<div class="ts-block-property-details">

Whether or not the navigation will result in the page being unloaded (i.e. not a client-side navigation).

</div>
</div>

<div class="ts-block-property">

```dts
complete: Promise<void>;
```

<div class="ts-block-property-details">

A promise that resolves once the navigation is complete, and rejects if the navigation
fails or is aborted. In the case of a `willUnload` navigation, the promise will never resolve

</div>
</div></div>

## NavigationEnter

<div class="ts-block">

```dts
interface NavigationEnter extends NavigationBase {/*…*/}
```

<div class="ts-block-property">

```dts
type: 'enter';
```

<div class="ts-block-property-details">

The type of navigation:
- `enter`: The app has hydrated/started

</div>
</div>

<div class="ts-block-property">

```dts
delta?: undefined;
```

<div class="ts-block-property-details">

In case of a history back/forward navigation, the number of steps to go back/forward

</div>
</div>

<div class="ts-block-property">

```dts
event?: undefined;
```

<div class="ts-block-property-details">

Dispatched `Event` object when navigation occurred by `popstate` or `link`.

</div>
</div></div>

## NavigationEvent

<div class="ts-block">

```dts
interface NavigationEvent<
	Params extends AppLayoutParams<'/'> =
		AppLayoutParams<'/'>,
	RouteId extends AppRouteId | null = AppRouteId | null
> {/*…*/}
```

<div class="ts-block-property">

```dts
params: Params;
```

<div class="ts-block-property-details">

The parameters of the current page - e.g. for a route like `/blog/[slug]`, a `{ slug: string }` object

</div>
</div>

<div class="ts-block-property">

```dts
route: {/*…*/}
```

<div class="ts-block-property-details">

Info about the current route

<div class="ts-block-property-children"><div class="ts-block-property">

```dts
id: RouteId;
```

<div class="ts-block-property-details">

The ID of the current route - e.g. for `src/routes/blog/[slug]`, it would be `/blog/[slug]`. It is `null` when no route is matched.

</div>
</div></div>

</div>
</div>

<div class="ts-block-property">

```dts
url: URL;
```

<div class="ts-block-property-details">

The URL of the current page

</div>
</div></div>

## NavigationExternal

<div class="ts-block">

```dts
type NavigationExternal = NavigationGoto | NavigationLeave;
```

</div>

## NavigationFormSubmit

<div class="ts-block">

```dts
interface NavigationFormSubmit extends NavigationBase {/*…*/}
```

<div class="ts-block-property">

```dts
type: 'form';
```

<div class="ts-block-property-details">

The type of navigation:
- `form`: The user submitted a `<form method="GET">`

</div>
</div>

<div class="ts-block-property">

```dts
event: SubmitEvent;
```

<div class="ts-block-property-details">

The `SubmitEvent` that caused the navigation

</div>
</div>

<div class="ts-block-property">

```dts
delta?: undefined;
```

<div class="ts-block-property-details">

In case of a history back/forward navigation, the number of steps to go back/forward

</div>
</div></div>

## NavigationGoto

<div class="ts-block">

```dts
interface NavigationGoto extends NavigationBase {/*…*/}
```

<div class="ts-block-property">

```dts
type: 'goto';
```

<div class="ts-block-property-details">

The type of navigation:
- `goto`: Navigation was triggered by a `goto(...)` call or a redirect

</div>
</div>

<div class="ts-block-property">

```dts
delta?: undefined;
```

<div class="ts-block-property-details">

In case of a history back/forward navigation, the number of steps to go back/forward

</div>
</div></div>

## NavigationLeave

<div class="ts-block">

```dts
interface NavigationLeave extends NavigationBase {/*…*/}
```

<div class="ts-block-property">

```dts
type: 'leave';
```

<div class="ts-block-property-details">

The type of navigation:
- `leave`: The app is being left either because the tab is being closed or a navigation to a different document is occurring

</div>
</div>

<div class="ts-block-property">

```dts
delta?: undefined;
```

<div class="ts-block-property-details">

In case of a history back/forward navigation, the number of steps to go back/forward

</div>
</div></div>

## NavigationLink

<div class="ts-block">

```dts
interface NavigationLink extends NavigationBase {/*…*/}
```

<div class="ts-block-property">

```dts
type: 'link';
```

<div class="ts-block-property-details">

The type of navigation:
- `link`: Navigation was triggered by a link click

</div>
</div>

<div class="ts-block-property">

```dts
event: PointerEvent;
```

<div class="ts-block-property-details">

The `PointerEvent` that caused the navigation

</div>
</div>

<div class="ts-block-property">

```dts
delta?: undefined;
```

<div class="ts-block-property-details">

In case of a history back/forward navigation, the number of steps to go back/forward

</div>
</div></div>

## NavigationPopState

<div class="ts-block">

```dts
interface NavigationPopState extends NavigationBase {/*…*/}
```

<div class="ts-block-property">

```dts
type: 'popstate';
```

<div class="ts-block-property-details">

The type of navigation:
- `popstate`: Navigation was triggered by back/forward navigation

</div>
</div>

<div class="ts-block-property">

```dts
delta: number;
```

<div class="ts-block-property-details">

In case of a history back/forward navigation, the number of steps to go back/forward

</div>
</div>

<div class="ts-block-property">

```dts
event: PopStateEvent;
```

<div class="ts-block-property-details">

The `PopStateEvent` that caused the navigation

</div>
</div></div>

## NavigationTarget

Information about the target of a specific navigation.

<div class="ts-block">

```dts
interface NavigationTarget<
	Params extends AppLayoutParams<'/'> =
		AppLayoutParams<'/'>,
	RouteId extends AppRouteId | null = AppRouteId | null
> {/*…*/}
```

<div class="ts-block-property">

```dts
params: Params | null;
```

<div class="ts-block-property-details">

Parameters of the target page - e.g. for a route like `/blog/[slug]`, a `{ slug: string }` object.
Is `null` if the target is not part of the SvelteKit app (could not be resolved to a route).

</div>
</div>

<div class="ts-block-property">

```dts
route: {/*…*/}
```

<div class="ts-block-property-details">

Info about the target route

<div class="ts-block-property-children"><div class="ts-block-property">

```dts
id: RouteId | null;
```

<div class="ts-block-property-details">

The ID of the current route - e.g. for `src/routes/blog/[slug]`, it would be `/blog/[slug]`. It is `null` when no route is matched.

</div>
</div></div>

</div>
</div>

<div class="ts-block-property">

```dts
url: URL;
```

<div class="ts-block-property-details">

The URL that is navigated to

</div>
</div>

<div class="ts-block-property">

```dts
scroll: { x: number; y: number } | null;
```

<div class="ts-block-property-details">

The scroll position associated with this navigation.

For the `from` target, this is the scroll position at the moment of navigation.

For the `to` target, this represents the scroll position that will be or was restored:
- In `beforeNavigate` and `onNavigate`, this is only available for `popstate` navigations (back/forward button)
	and will be `null` for other navigation types, since the final scroll position isn't known
	ahead of time.
- In `afterNavigate`, this is always the scroll position that was applied after the navigation
	completed.

</div>
</div></div>

## NavigationType

- `enter`: The app has hydrated/started
- `form`: The user submitted a `<form method="GET">`
- `leave`: The app is being left either because the tab is being closed or a navigation to a different document is occurring
- `link`: Navigation was triggered by a link click
- `goto`: Navigation was triggered by a `goto(...)` call or a redirect
- `popstate`: Navigation was triggered by back/forward navigation

<div class="ts-block">

```dts
type NavigationType =
	| 'enter'
	| 'form'
	| 'leave'
	| 'link'
	| 'goto'
	| 'popstate';
```

</div>

## NumericRange

<div class="ts-block">

```dts
type NumericRange<
	TStart extends number,
	TEnd extends number
> = Exclude<TEnd | LessThan<TEnd>, LessThan<TStart>>;
```

</div>

## OnNavigate

The argument passed to [`onNavigate`](/docs/kit/$app-navigation#onNavigate) callbacks.

<div class="ts-block">

```dts
type OnNavigate = Navigation & {
	type: Exclude<NavigationType, 'enter' | 'leave'>;
	/**
	 * Since `onNavigate` callbacks are called immediately before a client-side navigation, they will never be called with a navigation that unloads the page.
	 */
	willUnload: false;
};
```

</div>

## Page

The shape of the [`page`](/docs/kit/$app-state#page) reactive object and the [`$page`](/docs/kit/$app-stores) store.

<div class="ts-block">

```dts
interface Page<
	Params extends AppLayoutParams<'/'> =
		AppLayoutParams<'/'>,
	RouteId extends AppRouteId | null = AppRouteId | null
> {/*…*/}
```

<div class="ts-block-property">

```dts
url: URL & { pathname: ResolvedPathname };
```

<div class="ts-block-property-details">

The URL of the current page.

</div>
</div>

<div class="ts-block-property">

```dts
params: Params;
```

<div class="ts-block-property-details">

The parameters of the current page - e.g. for a route like `/blog/[slug]`, a `{ slug: string }` object.

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

</div>
</div></div>

</div>
</div>

<div class="ts-block-property">

```dts
status: number;
```

<div class="ts-block-property-details">

HTTP status code of the current page.

</div>
</div>

<div class="ts-block-property">

```dts
error: App.Error | null;
```

<div class="ts-block-property-details">

The error object of the current page, if any. Filled from the `handleError` hooks.

</div>
</div>

<div class="ts-block-property">

```dts
data: App.PageData & Record<string, any>;
```

<div class="ts-block-property-details">

The merged result of all data from all `load` functions on the current page. You can type a common denominator through `App.PageData`.

</div>
</div>

<div class="ts-block-property">

```dts
state: App.PageState;
```

<div class="ts-block-property-details">

The page state, which can be manipulated using the [`pushState`](/docs/kit/$app-navigation#pushState) and [`replaceState`](/docs/kit/$app-navigation#replaceState) functions from `$app/navigation`.

</div>
</div>

<div class="ts-block-property">

```dts
form: any;
```

<div class="ts-block-property-details">

Filled only after a form submission. See [form actions](/docs/kit/form-actions) for more info.

</div>
</div></div>

## ParamMatcher

The shape of a param matcher. See [matching](/docs/kit/advanced-routing#Matching) for more info.

<div class="ts-block">

```dts
type ParamMatcher = (param: string) => boolean;
```

</div>

## PrerenderOption

<div class="ts-block">

```dts
type PrerenderOption = boolean | 'auto';
```

</div>

## QueryRequestedResult

<div class="ts-block">

```dts
type QueryRequestedResult<Validated, Output> = Iterable<
	RequestedEntry<Validated, Output>
> &
	AsyncIterable<RequestedEntry<Validated, Output>> & {
		/**
		 * Call `refresh` on all queries selected by this `requested` invocation.
		 * This is identical to:
		 * ```ts
		 * import { requested } from '$app/server';
		 *
		 * for await (const { query } of requested(getPost, ...)) {
		 *   void query.refresh();
