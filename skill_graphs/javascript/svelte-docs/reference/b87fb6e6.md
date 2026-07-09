# @sveltejs/kit

```js
// @noErrors
import {
	Server,
	VERSION,
	error,
	fail,
	invalid,
	isActionFailure,
	isHttpError,
	isRedirect,
	isValidationError,
	json,
	normalizeUrl,
	redirect,
	text
} from '@sveltejs/kit';
```

## Server

<div class="ts-block">

```dts
class Server {/*…*/}
```

<div class="ts-block-property">

```dts
constructor(manifest: SSRManifest);
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
init(options: ServerInitOptions): Promise<void>;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
respond(request: Request, options: RequestOptions): Promise<Response>;
```

<div class="ts-block-property-details"></div>
</div></div>

## VERSION

<div class="ts-block">

```dts
const VERSION: string;
```

</div>

## error

Throws an error with a HTTP status code and an optional message.
When called during request handling, this will cause SvelteKit to
return an error response without invoking `handleError`.
Make sure you're not catching the thrown error, which would prevent SvelteKit from handling it.

<div class="ts-block">

```dts
function error(status: number, body: App.Error): never;
```

</div>

<div class="ts-block">

```dts
function error(
	status: number,
	body?: {
		message: string;
	} extends App.Error
		? App.Error | string | undefined
		: never
): never;
```

</div>

## fail

Create an `ActionFailure` object. Call when form submission fails.

<div class="ts-block">

```dts
function fail(status: number): ActionFailure<undefined>;
```

</div>

<div class="ts-block">

```dts
function fail<T = undefined>(
	status: number,
	data: T
): ActionFailure<T>;
```

</div>

## invalid

<blockquote class="since note">

Available since 2.47.3

</blockquote>

Use this to throw a validation error to imperatively fail form validation.
Can be used in combination with `issue` passed to form actions to create field-specific issues.

```ts
import { invalid } from '@sveltejs/kit';
import { form } from '$app/server';
import { tryLogin } from '$lib/server/auth';
import * as v from 'valibot';

export const login = form(
	v.object({ name: v.string(), _password: v.string() }),
	async ({ name, _password }) => {
		const success = tryLogin(name, _password);
		if (!success) {
			invalid('Incorrect username or password');
		}

		// ...
	}
);
```

<div class="ts-block">

```dts
function invalid(
	...issues: (StandardSchemaV1.Issue | string)[]
): never;
```

</div>

## isActionFailure

Checks whether this is an action failure thrown by `fail`.

<div class="ts-block">

```dts
function isActionFailure(e: unknown): e is ActionFailure;
```

</div>

## isHttpError

Checks whether this is an error thrown by `error`.

<div class="ts-block">

```dts
function isHttpError<T extends number>(
	e: unknown,
	status?: T
): e is HttpError_1 & {
	status: T extends undefined ? never : T;
};
```

</div>

## isRedirect

Checks whether this is a redirect thrown by `redirect`.

<div class="ts-block">

```dts
function isRedirect(e: unknown): e is Redirect_1;
```

</div>

## isValidationError

<blockquote class="since note">

Available since 2.47.3

</blockquote>

Checks whether this is an validation error thrown by `invalid`.

<div class="ts-block">

```dts
function isValidationError(e: unknown): e is ActionFailure;
```

</div>

## json

Create a JSON `Response` object from the supplied data.

<div class="ts-block">

```dts
function json(data: any, init?: ResponseInit): Response;
```

</div>

## normalizeUrl

<blockquote class="since note">

Available since 2.18.0

</blockquote>

Strips possible SvelteKit-internal suffixes and trailing slashes from the URL pathname.
Returns the normalized URL as well as a method for adding the potential suffix back
based on a new pathname (possibly including search) or URL.
```js
// @errors: 7031
import { normalizeUrl } from '@sveltejs/kit';

const { url, denormalize } = normalizeUrl('/blog/post/__data.json');
console.log(url.pathname); // /blog/post
console.log(denormalize('/blog/post/a')); // /blog/post/a/__data.json
```

<div class="ts-block">

```dts
function normalizeUrl(url: URL | string): {
	url: URL;
	wasNormalized: boolean;
	denormalize: (url?: string | URL) => URL;
};
```

</div>

## redirect

Redirect a request. When called during request handling, SvelteKit will return a redirect response.
Make sure you're not catching the thrown redirect, which would prevent SvelteKit from handling it.

Most common status codes:
 * `303 See Other`: redirect as a GET request (often used after a form POST request)
 * `307 Temporary Redirect`: redirect will keep the request method
 * `308 Permanent Redirect`: redirect will keep the request method, SEO will be transferred to the new page

[See all redirect status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#redirection_messages)

<div class="ts-block">

```dts
function redirect(
	status:
		| 300
		| 301
		| 302
		| 303
		| 304
		| 305
		| 306
		| 307
		| 308
		| ({} & number),
	location: string | URL
): never;
```

</div>

## text

Create a `Response` object from the supplied body.

<div class="ts-block">

```dts
function text(body: string, init?: ResponseInit): Response;
```

</div>

## Action

Shape of a form action method that is part of `export const actions = {...}` in `+page.server.js`.
See [form actions](/docs/kit/form-actions) for more information.

<div class="ts-block">

```dts
type Action<
	Params extends AppLayoutParams<'/'> =
		AppLayoutParams<'/'>,
	OutputData extends Record<string, any> | void = Record<
		string,
		any
	> | void,
	RouteId extends AppRouteId | null = AppRouteId | null
> = (
	event: RequestEvent<Params, RouteId>
) => MaybePromise<OutputData>;
```

</div>

## ActionFailure

<div class="ts-block">

```dts
interface ActionFailure<T = undefined> {/*…*/}
```

<div class="ts-block-property">

```dts
status: number;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
data: T;
```

<div class="ts-block-property-details"></div>
</div>

<div class="ts-block-property">

```dts
[uniqueSymbol]: true;
```

<div class="ts-block-property-details"></div>
</div></div>

## ActionResult

When calling a form action via fetch, the response will be one of these shapes.
```svelte
<form method="post" use:enhance={() => {
	return ({ result }) => {
		// result is of type ActionResult
	};
}}
```

<div class="ts-block">

```dts
type ActionResult<
	Success extends Record<string, unknown> | undefined =
		Record<string, any>,
	Failure extends Record<string, unknown> | undefined =
		Record<string, any>
> =
	| { type: 'success'; status: number; data?: Success }
	| { type: 'failure'; status: number; data?: Failure }
	| { type: 'redirect'; status: number; location: string }
	| { type: 'error'; status?: number; error: any };
```

</div>

## Actions

Shape of the `export const actions = {...}` object in `+page.server.js`.
See [form actions](/docs/kit/form-actions) for more information.

<div class="ts-block">

```dts
type Actions<
	Params extends AppLayoutParams<'/'> =
		AppLayoutParams<'/'>,
	OutputData extends Record<string, any> | void = Record<
		string,
		any
	> | void,
	RouteId extends AppRouteId | null = AppRouteId | null
> = Record<string, Action<Params, OutputData, RouteId>>;
```

</div>

## Adapter

[Adapters](/docs/kit/adapters) are responsible for taking the production build and turning it into something that can be deployed to a platform of your choosing.

<div class="ts-block">

```dts
interface Adapter {/*…*/}
```

<div class="ts-block-property">

```dts
name: string;
```

<div class="ts-block-property-details">

The name of the adapter, using for logging. Will typically correspond to the package name.

</div>
</div>

<div class="ts-block-property">

```dts
adapt: (builder: Builder) => MaybePromise<void>;
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- `builder` An object provided by SvelteKit that contains methods for adapting the app

</div>

This function is called after SvelteKit has built your app.

</div>
</div>

<div class="ts-block-property">

```dts
supports?: {/*…*/}
```

<div class="ts-block-property-details">

Checks called during dev and build to determine whether specific features will work in production with this adapter.

<div class="ts-block-property-children"><div class="ts-block-property">

```dts
read?: (details: { config: any; route: { id: string } }) => boolean;
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- `details.config` The merged adapter-specific route config exported from the route with `export const config`

</div>

Test support for `read` from `$app/server`.

</div>
</div>
<div class="ts-block-property">

```dts
instrumentation?: () => boolean;
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- <span class="tag since">available since</span> v2.31.0

</div>

Test support for `instrumentation.server.js`. To pass, the adapter must support running `instrumentation.server.js` prior to the application code.

</div>
</div></div>

</div>
</div>

<div class="ts-block-property">

```dts
emulate?: () => MaybePromise<Emulator>;
```

<div class="ts-block-property-details">

Creates an `Emulator`, which allows the adapter to influence the environment
during dev, build and prerendering.

</div>
</div></div>

## AfterNavigate

The argument passed to [`afterNavigate`](/docs/kit/$app-navigation#afterNavigate) callbacks.

<div class="ts-block">

```dts
type AfterNavigate = (Navigation | NavigationEnter) & {
	type: Exclude<NavigationType, 'leave'>;
	/**
	 * Since `afterNavigate` callbacks are called after a navigation completes, they will never be called with a navigation that unloads the page.
	 */
	willUnload: false;
};
```

</div>

## AwaitedActions

<div class="ts-block">

```dts
type AwaitedActions<
	T extends Record<string, (...args: any) => any>
> = OptionalUnion<
	{
		[Key in keyof T]: UnpackValidationError<
			Awaited<ReturnType<T[Key]>>
		>;
	}[keyof T]
>;
```

</div>

## BeforeNavigate

The argument passed to [`beforeNavigate`](/docs/kit/$app-navigation#beforeNavigate) callbacks.

<div class="ts-block">

```dts
type BeforeNavigate = Navigation & {
	/**
	 * Call this to prevent the navigation from starting.
	 */
	cancel: () => void;
};
```

</div>

## Builder

This object is passed to the `adapt` function of adapters.
It contains various methods and properties that are useful for adapting the app.

<div class="ts-block">

```dts
interface Builder {/*…*/}
```

<div class="ts-block-property">

```dts
log: Logger;
```

<div class="ts-block-property-details">

Print messages to the console. `log.info` and `log.minor` are silent unless Vite's `logLevel` is `info`.

</div>
</div>

<div class="ts-block-property">

```dts
rimraf: (dir: string) => void;
```

<div class="ts-block-property-details">

Remove `dir` and all its contents.

</div>
</div>

<div class="ts-block-property">

```dts
mkdirp: (dir: string) => void;
```

<div class="ts-block-property-details">

Create `dir` and any required parent directories.

</div>
</div>

<div class="ts-block-property">

```dts
config: ValidatedConfig;
```

<div class="ts-block-property-details">

The fully resolved Svelte config.

</div>
</div>

<div class="ts-block-property">

```dts
prerendered: Prerendered;
```

<div class="ts-block-property-details">

Information about prerendered pages and assets, if any.

</div>
</div>

<div class="ts-block-property">

```dts
routes: RouteDefinition[];
```

<div class="ts-block-property-details">

An array of all routes (including prerendered)

</div>
</div>

<div class="ts-block-property">

```dts
createEntries: (fn: (route: RouteDefinition) => AdapterEntry) => Promise<void>;
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- `fn` A function that groups a set of routes into an entry point
- <span class="tag deprecated">deprecated</span> Use `builder.routes` instead

</div>

Create separate functions that map to one or more routes of your app.

</div>
</div>

<div class="ts-block-property">

```dts
findServerAssets: (routes: RouteDefinition[]) => string[];
```

<div class="ts-block-property-details">

Find all the assets imported by server files belonging to `routes`

</div>
</div>

<div class="ts-block-property">

```dts
generateFallback: (dest: string) => Promise<void>;
```

<div class="ts-block-property-details">

Generate a fallback page for a static webserver to use when no route is matched. Useful for single-page apps.

</div>
</div>

<div class="ts-block-property">

```dts
generateEnvModule: () => void;
```

<div class="ts-block-property-details">

Generate a module exposing build-time environment variables as `$env/dynamic/public` if the app uses it.

</div>
</div>

<div class="ts-block-property">

```dts
generateManifest: (opts: { relativePath: string; routes?: RouteDefinition[] }) => string;
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- `opts` a relative path to the base directory of the app and optionally in which format (esm or cjs) the manifest should be generated

</div>

Generate a server-side manifest to initialise the SvelteKit [server](/docs/kit/@sveltejs-kit#Server) with.

</div>
</div>

<div class="ts-block-property">

```dts
getBuildDirectory: (name: string) => string;
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- `name` path to the file, relative to the build directory

</div>

Resolve a path to the `name` directory inside `outDir`, e.g. `/path/to/.svelte-kit/my-adapter`.

</div>
</div>

<div class="ts-block-property">

```dts
getClientDirectory: () => string;
```

<div class="ts-block-property-details">

Get the fully resolved path to the directory containing client-side assets, including the contents of your `static` directory.

</div>
</div>

<div class="ts-block-property">

```dts
getServerDirectory: () => string;
```

<div class="ts-block-property-details">

Get the fully resolved path to the directory containing server-side code.

</div>
</div>

<div class="ts-block-property">

```dts
getAppPath: () => string;
```

<div class="ts-block-property-details">

Get the application path including any configured `base` path, e.g. `my-base-path/_app`.

</div>
</div>

<div class="ts-block-property">

```dts
writeClient: (dest: string) => string[];
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- `dest` the destination folder
- <span class="tag">returns</span> an array of files written to `dest`

</div>

Write client assets to `dest`.

</div>
</div>

<div class="ts-block-property">

```dts
writePrerendered: (dest: string) => string[];
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- `dest` the destination folder
- <span class="tag">returns</span> an array of files written to `dest`

</div>

Write prerendered files to `dest`.

</div>
</div>

<div class="ts-block-property">

```dts
writeServer: (dest: string) => string[];
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- `dest` the destination folder
- <span class="tag">returns</span> an array of files written to `dest`

</div>

Write server-side code to `dest`.

</div>
</div>

<div class="ts-block-property">

```dts
copy: (
	from: string,
	to: string,
	opts?: {
		filter?(basename: string): boolean;
		replace?: Record<string, string>;
	}
) => string[];
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- `from` the source file or directory
- `to` the destination file or directory
- `opts.filter` a function to determine whether a file or directory should be copied
- `opts.replace` a map of strings to replace
- <span class="tag">returns</span> an array of files that were copied

</div>

Copy a file or directory.

</div>
</div>

<div class="ts-block-property">

```dts
hasServerInstrumentationFile: () => boolean;
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- <span class="tag">returns</span> true if the server instrumentation file exists, false otherwise
- <span class="tag since">available since</span> v2.31.0

</div>

Check if the server instrumentation file exists.

</div>
</div>

<div class="ts-block-property">

```dts
instrument: (args: {
	entrypoint: string;
	instrumentation: string;
	start?: string;
	module?:
		| {
				exports: string[];
		  }
		| {
				generateText: (args: { instrumentation: string; start: string }) => string;
		  };
}) => void;
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- `options` an object containing the following properties:
- `options.entrypoint` the path to the entrypoint to trace.
- `options.instrumentation` the path to the instrumentation file.
- `options.start` the name of the start file. This is what `entrypoint` will be renamed to.
- `options.module` configuration for the resulting entrypoint module.
- `options.module.generateText` a function that receives the relative paths to the instrumentation and start files, and generates the text of the module to be traced. If not provided, the default implementation will be used, which uses top-level await.
- <span class="tag since">available since</span> v2.31.0

</div>

Instrument `entrypoint` with `instrumentation`.

Renames `entrypoint` to `start` and creates a new module at
`entrypoint` which imports `instrumentation` and then dynamically imports `start`. This allows
the module hooks necessary for instrumentation libraries to be loaded prior to any application code.

Caveats:
- "Live exports" will not work. If your adapter uses live exports, your users will need to manually import the server instrumentation on startup.
- If `tla` is `false`, OTEL auto-instrumentation may not work properly. Use it if your environment supports it.
- Use `hasServerInstrumentationFile` to check if the user has a server instrumentation file; if they don't, you shouldn't do this.

</div>
</div>

<div class="ts-block-property">

```dts
compress: (directory: string) => Promise<void>;
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- `directory` The directory containing the files to be compressed

</div>

Compress files in `directory` with gzip and brotli, where appropriate. Generates `.gz` and `.br` files alongside the originals.

</div>
</div></div>

## ClientInit

<blockquote class="since note">

Available since 2.10.0

</blockquote>

The [`init`](/docs/kit/hooks#Shared-hooks-init) will be invoked once the app starts in the browser

<div class="ts-block">

```dts
type ClientInit = () => MaybePromise<void>;
```

</div>

## Config

See the [configuration reference](/docs/kit/configuration) for details.

## Cookies

<div class="ts-block">

```dts
interface Cookies {/*…*/}
```

<div class="ts-block-property">

```dts
get: (name: string, opts?: import('cookie').CookieParseOptions) => string | undefined;
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- `name` the name of the cookie
- `opts` the options, passed directly to `cookie.parse`. See documentation [here](https://github.com/jshttp/cookie#cookieparsestr-options)

</div>

Gets a cookie that was previously set with `cookies.set`, or from the request headers.

</div>
</div>

<div class="ts-block-property">

```dts
getAll: (opts?: import('cookie').CookieParseOptions) => Array<{ name: string; value: string }>;
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- `opts` the options, passed directly to `cookie.parse`. See documentation [here](https://github.com/jshttp/cookie#cookieparsestr-options)

</div>

Gets all cookies that were previously set with `cookies.set`, or from the request headers.

</div>
</div>

<div class="ts-block-property">

```dts
set: (
	name: string,
	value: string,
	opts: import('cookie').CookieSerializeOptions & { path: string }
) => void;
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- `name` the name of the cookie
- `value` the cookie value
- `opts` the options, passed directly to `cookie.serialize`. See documentation [here](https://github.com/jshttp/cookie#cookieserializename-value-options)

</div>

Sets a cookie. This will add a `set-cookie` header to the response, but also make the cookie available via `cookies.get` or `cookies.getAll` during the current request.

The `httpOnly` and `secure` options are `true` by default (except on http://localhost, where `secure` is `false`), and must be explicitly disabled if you want cookies to be readable by client-side JavaScript and/or transmitted over HTTP. The `sameSite` option defaults to `lax`.

You must specify a `path` for the cookie. In most cases you should explicitly set `path: '/'` to make the cookie available throughout your app. You can use relative paths, or set `path: ''` to make the cookie only available on the current path and its children

</div>
</div>

<div class="ts-block-property">

```dts
delete: (name: string, opts: import('cookie').CookieSerializeOptions & { path: string }) => void;
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- `name` the name of the cookie
- `opts` the options, passed directly to `cookie.serialize`. The `path` must match the path of the cookie you want to delete. See documentation [here](https://github.com/jshttp/cookie#cookieserializename-value-options)

</div>

Deletes a cookie by setting its value to an empty string and setting the expiry date in the past.

You must specify a `path` for the cookie. In most cases you should explicitly set `path: '/'` to make the cookie available throughout your app. You can use relative paths, or set `path: ''` to make the cookie only available on the current path and its children

</div>
</div>

<div class="ts-block-property">

```dts
serialize: (
	name: string,
	value: string,
	opts: import('cookie').CookieSerializeOptions & { path: string }
) => string;
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- `name` the name of the cookie
- `value` the cookie value
- `opts` the options, passed directly to `cookie.serialize`. See documentation [here](https://github.com/jshttp/cookie#cookieserializename-value-options)

</div>

Serialize a cookie name-value pair into a `Set-Cookie` header string, but don't apply it to the response.

The `httpOnly` and `secure` options are `true` by default (except on http://localhost, where `secure` is `false`), and must be explicitly disabled if you want cookies to be readable by client-side JavaScript and/or transmitted over HTTP. The `sameSite` option defaults to `lax`.

You must specify a `path` for the cookie. In most cases you should explicitly set `path: '/'` to make the cookie available throughout your app. You can use relative paths, or set `path: ''` to make the cookie only available on the current path and its children

</div>
</div></div>

## Emulator

A collection of functions that influence the environment during dev, build and prerendering

<div class="ts-block">

```dts
interface Emulator {/*…*/}
```

<div class="ts-block-property">

```dts
platform?(details: { config: any; prerender: PrerenderOption }): MaybePromise<App.Platform>;
```

<div class="ts-block-property-details">

A function that is called with the current route `config` and `prerender` option
and returns an `App.Platform` object

</div>
</div></div>

## EnvVarConfig

[Environment variables](/docs/kit/environment-variables) can be configured by exporting
a `variables` object from `src/env.ts`, using [`defineEnvVars`](/docs/kit/@sveltejs-kit-hooks#defineEnvVars).

<div class="ts-block">

```dts
interface EnvVarConfig<T> {/*…*/}
```

<div class="ts-block-property">

```dts
public?: boolean;
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- <span class="tag">default</span> `false`

</div>

Whether the environment variable can be accessed by client-side code.
- if `true`, it can be imported from `$app/env/public`
- if `false`, it can be imported from `$app/env/private`, which is a [server-only module](/docs/kit/server-only-modules)

</div>
</div>

<div class="ts-block-property">

```dts
static?: boolean;
```

<div class="ts-block-property-details">

<div class="ts-block-property-bullets">

- <span class="tag">default</span> `false`

</div>

Whether the value is determined at build time or when the app runs.
- if `true`, the build time value is inlined into the bundle. This enables optimisations like dead-code elimination
- if `false`, the value is read from the environment when the app starts

</div>
</div>

<div class="ts-block-property">

```dts
schema?: StandardSchemaV1<string | undefined, T>;
```

<div class="ts-block-property-details">

A [Standard Schema](https://standardschema.dev/) validator that is applied to the value when the app starts.
The validator can output any value — not necessarily a string — but public, non-static values must be
serializable by [devalue](https://github.com/sveltejs/devalue) so that they can be sent to the browser.

If omitted, the value must be a non-empty string.

</div>
</div>

<div class="ts-block-property">

```dts
description?: string;
```

<div class="ts-block-property-details">

A description of the variable that will be used for inline documentation on hover.

</div>
</div></div>

## Handle
