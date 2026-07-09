####  `napi_remove_wrap`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-remove-wrap)
Added in: v8.5.0**N-API Version:** 1
```
napi_status napi_remove_wrap(napi_env env,
                             napi_value js_object,
                             void** result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] js_object`: The object associated with the native instance.
  * `[out] result`: Pointer to the wrapped native instance.


Returns `napi_ok` if the API succeeded.
Retrieves a native instance that was previously wrapped in the JavaScript object `js_object` using `napi_wrap()` and removes the wrapping. If a finalize callback was associated with the wrapping, it will no longer be called when the JavaScript object becomes garbage-collected.
####  `napi_type_tag_object`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-type-tag-object)
Added in: v14.8.0, v12.19.0**N-API Version:** 8
```
napi_status napi_type_tag_object(napi_env env,
                                 napi_value js_object,
                                 const napi_type_tag* type_tag);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] js_object`: The JavaScript object or [external](https://nodejs.org/docs/latest/api/n-api.html#napi_create_external) to be marked.
  * `[in] type_tag`: The tag with which the object is to be marked.


Returns `napi_ok` if the API succeeded.
Associates the value of the `type_tag` pointer with the JavaScript object or [external](https://nodejs.org/docs/latest/api/n-api.html#napi_create_external). `napi_check_object_type_tag()` can then be used to compare the tag that was attached to the object with one owned by the addon to ensure that the object has the right type.
If the object already has an associated type tag, this API will return `napi_invalid_arg`.
####  `napi_check_object_type_tag`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-check-object-type-tag)
Added in: v14.8.0, v12.19.0**N-API Version:** 8
```
napi_status napi_check_object_type_tag(napi_env env,
                                       napi_value js_object,
                                       const napi_type_tag* type_tag,
                                       bool* result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] js_object`: The JavaScript object or [external](https://nodejs.org/docs/latest/api/n-api.html#napi_create_external) whose type tag to examine.
  * `[in] type_tag`: The tag with which to compare any tag found on the object.
  * `[out] result`: Whether the type tag given matched the type tag on the object. `false` is also returned if no type tag was found on the object.


Returns `napi_ok` if the API succeeded.
Compares the pointer given as `type_tag` with any that can be found on `js_object`. If no tag is found on `js_object` or, if a tag is found but it does not match `type_tag`, then `result` is set to `false`. If a tag is found and it matches `type_tag`, then `result` is set to `true`.
####  `napi_add_finalizer`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-add-finalizer)
Added in: v8.0.0**N-API Version:** 5
```
napi_status napi_add_finalizer(napi_env env,
                               napi_value js_object,
                               void* finalize_data,
                               node_api_basic_finalize finalize_cb,
                               void* finalize_hint,
                               napi_ref* result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] js_object`: The JavaScript object to which the native data will be attached.
  * `[in] finalize_data`: Optional data to be passed to `finalize_cb`.
  * `[in] finalize_cb`: Native callback that will be used to free the native data when the JavaScript object has been garbage-collected. [`napi_finalize`](https://nodejs.org/docs/latest/api/n-api.html#napi_finalize) provides more details.
  * `[in] finalize_hint`: Optional contextual hint that is passed to the finalize callback.
  * `[out] result`: Optional reference to the JavaScript object.


Returns `napi_ok` if the API succeeded.
Adds a `napi_finalize` callback which will be called when the JavaScript object in `js_object` has been garbage-collected.
This API can be called multiple times on a single JavaScript object.
_Caution_ : The optional returned reference (if obtained) should be deleted via [`napi_delete_reference`](https://nodejs.org/docs/latest/api/n-api.html#napi_delete_reference) ONLY in response to the finalize callback invocation. If it is deleted before then, then the finalize callback may never be invoked. Therefore, when obtaining a reference a finalize callback is also required in order to enable correct disposal of the reference.
#####  `node_api_post_finalizer`[#](https://nodejs.org/docs/latest/api/n-api.html#node-api-post-finalizer)
Added in: v21.0.0, v20.10.0, v18.19.0
Stability: 1 - Experimental
```
napi_status node_api_post_finalizer(node_api_basic_env env,
                                    napi_finalize finalize_cb,
                                    void* finalize_data,
                                    void* finalize_hint);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] finalize_cb`: Native callback that will be used to free the native data when the JavaScript object has been garbage-collected. [`napi_finalize`](https://nodejs.org/docs/latest/api/n-api.html#napi_finalize) provides more details.
  * `[in] finalize_data`: Optional data to be passed to `finalize_cb`.
  * `[in] finalize_hint`: Optional contextual hint that is passed to the finalize callback.


Returns `napi_ok` if the API succeeded.
Schedules a `napi_finalize` callback to be called asynchronously in the event loop.
Normally, finalizers are called while the GC (garbage collector) collects objects. At that point calling any Node-API that may cause changes in the GC state will be disabled and will crash Node.js.
`node_api_post_finalizer` helps to work around this limitation by allowing the add-on to defer calls to such Node-APIs to a point in time outside of the GC finalization.
### Simple asynchronous operations[#](https://nodejs.org/docs/latest/api/n-api.html#simple-asynchronous-operations)
Addon modules often need to leverage async helpers from libuv as part of their implementation. This allows them to schedule work to be executed asynchronously so that their methods can return in advance of the work being completed. This allows them to avoid blocking overall execution of the Node.js application.
Node-API provides an ABI-stable interface for these supporting functions which covers the most common asynchronous use cases.
Node-API defines the `napi_async_work` structure which is used to manage asynchronous workers. Instances are created/deleted with [`napi_create_async_work`](https://nodejs.org/docs/latest/api/n-api.html#napi_create_async_work) and [`napi_delete_async_work`](https://nodejs.org/docs/latest/api/n-api.html#napi_delete_async_work).
The `execute` and `complete` callbacks are functions that will be invoked when the executor is ready to execute and when it completes its task respectively.
The `execute` function should avoid making any Node-API calls that could result in the execution of JavaScript or interaction with JavaScript objects. Most often, any code that needs to make Node-API calls should be made in `complete` callback instead. Avoid using the `napi_env` parameter in the execute callback as it will likely execute JavaScript.
These functions implement the following interfaces:
```
typedef void (*napi_async_execute_callback)(napi_env env,
                                            void* data);
typedef void (*napi_async_complete_callback)(napi_env env,
                                             napi_status status,
                                             void* data);
copy
```

When these methods are invoked, the `data` parameter passed will be the addon-provided `void*` data that was passed into the `napi_create_async_work` call.
Once created the async worker can be queued for execution using the [`napi_queue_async_work`](https://nodejs.org/docs/latest/api/n-api.html#napi_queue_async_work) function:
```
napi_status napi_queue_async_work(node_api_basic_env env,
                                  napi_async_work work);
copy
```

[`napi_cancel_async_work`](https://nodejs.org/docs/latest/api/n-api.html#napi_cancel_async_work) can be used if the work needs to be cancelled before the work has started execution.
After calling [`napi_cancel_async_work`](https://nodejs.org/docs/latest/api/n-api.html#napi_cancel_async_work), the `complete` callback will be invoked with a status value of `napi_cancelled`. The work should not be deleted before the `complete` callback invocation, even when it was cancelled.
####  `napi_create_async_work`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-async-work)
Added in: v8.0.0**N-API Version:** 1History Version | Changes
---|---
v8.6.0 | Added `async_resource` and `async_resource_name` parameters.
```
napi_status napi_create_async_work(napi_env env,
                                   napi_value async_resource,
                                   napi_value async_resource_name,
                                   napi_async_execute_callback execute,
                                   napi_async_complete_callback complete,
                                   void* data,
                                   napi_async_work* result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] async_resource`: An optional object associated with the async work that will be passed to possible `async_hooks` [`init` hooks](https://nodejs.org/docs/latest/api/async_hooks.html#initasyncid-type-triggerasyncid-resource).
  * `[in] async_resource_name`: Identifier for the kind of resource that is being provided for diagnostic information exposed by the `async_hooks` API.
  * `[in] execute`: The native function which should be called to execute the logic asynchronously. The given function is called from a worker pool thread and can execute in parallel with the main event loop thread.
  * `[in] complete`: The native function which will be called when the asynchronous logic is completed or is cancelled. The given function is called from the main event loop thread. [`napi_async_complete_callback`](https://nodejs.org/docs/latest/api/n-api.html#napi_async_complete_callback) provides more details.
  * `[in] data`: User-provided data context. This will be passed back into the execute and complete functions.
  * `[out] result`: `napi_async_work*` which is the handle to the newly created async work.


Returns `napi_ok` if the API succeeded.
This API allocates a work object that is used to execute logic asynchronously. It should be freed using [`napi_delete_async_work`](https://nodejs.org/docs/latest/api/n-api.html#napi_delete_async_work) once the work is no longer required.
`async_resource_name` should be a null-terminated, UTF-8-encoded string.
The `async_resource_name` identifier is provided by the user and should be representative of the type of async work being performed. It is also recommended to apply namespacing to the identifier, e.g. by including the module name. See the [`async_hooks` documentation](https://nodejs.org/docs/latest/api/async_hooks.html#type) for more information.
####  `napi_delete_async_work`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-delete-async-work)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_delete_async_work(napi_env env,
                                   napi_async_work work);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] work`: The handle returned by the call to `napi_create_async_work`.


Returns `napi_ok` if the API succeeded.
This API frees a previously allocated work object.
This API can be called even if there is a pending JavaScript exception.
####  `napi_queue_async_work`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-queue-async-work)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_queue_async_work(node_api_basic_env env,
                                  napi_async_work work);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] work`: The handle returned by the call to `napi_create_async_work`.


Returns `napi_ok` if the API succeeded.
This API requests that the previously allocated work be scheduled for execution. Once it returns successfully, this API must not be called again with the same `napi_async_work` item or the result will be undefined.
####  `napi_cancel_async_work`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-cancel-async-work)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_cancel_async_work(node_api_basic_env env,
                                   napi_async_work work);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] work`: The handle returned by the call to `napi_create_async_work`.


Returns `napi_ok` if the API succeeded.
This API cancels queued work if it has not yet been started. If it has already started executing, it cannot be cancelled and `napi_generic_failure` will be returned. If successful, the `complete` callback will be invoked with a status value of `napi_cancelled`. The work should not be deleted before the `complete` callback invocation, even if it has been successfully cancelled.
This API can be called even if there is a pending JavaScript exception.
### Custom asynchronous operations[#](https://nodejs.org/docs/latest/api/n-api.html#custom-asynchronous-operations)
The simple asynchronous work APIs above may not be appropriate for every scenario. When using any other asynchronous mechanism, the following APIs are necessary to ensure an asynchronous operation is properly tracked by the runtime.
####  `napi_async_init`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-async-init)
Added in: v8.6.0**N-API Version:** 1History Version | Changes
---|---
v25.0.0 | The `async_resource` object will now be held as a strong reference.
```
napi_status napi_async_init(napi_env env,
                            napi_value async_resource,
                            napi_value async_resource_name,
                            napi_async_context* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] async_resource`: Object associated with the async work that will be passed to possible `async_hooks` [`init` hooks](https://nodejs.org/docs/latest/api/async_hooks.html#initasyncid-type-triggerasyncid-resource) and can be accessed by [`async_hooks.executionAsyncResource()`](https://nodejs.org/docs/latest/api/async_hooks.html#async_hooksexecutionasyncresource).
  * `[in] async_resource_name`: Identifier for the kind of resource that is being provided for diagnostic information exposed by the `async_hooks` API.
  * `[out] result`: The initialized async context.


Returns `napi_ok` if the API succeeded.
In order to retain ABI compatibility with previous versions, passing `NULL` for `async_resource` does not result in an error. However, this is not recommended as this will result in undesirable behavior with `async_hooks` [`init` hooks](https://nodejs.org/docs/latest/api/async_hooks.html#initasyncid-type-triggerasyncid-resource) and `async_hooks.executionAsyncResource()` as the resource is now required by the underlying `async_hooks` implementation in order to provide the linkage between async callbacks.
Previous versions of this API were not maintaining a strong reference to `async_resource` while the `napi_async_context` object existed and instead expected the caller to hold a strong reference. This has been changed, as a corresponding call to [`napi_async_destroy`](https://nodejs.org/docs/latest/api/n-api.html#napi_async_destroy) for every call to `napi_async_init()` is a requirement in any case to avoid memory leaks.
####  `napi_async_destroy`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-async-destroy)
Added in: v8.6.0**N-API Version:** 1
```
napi_status napi_async_destroy(napi_env env,
                               napi_async_context async_context);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] async_context`: The async context to be destroyed.


Returns `napi_ok` if the API succeeded.
This API can be called even if there is a pending JavaScript exception.
####  `napi_make_callback`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-make-callback)
Added in: v8.0.0**N-API Version:** 1History Version | Changes
---|---
v8.6.0 | Added `async_context` parameter.
```
NAPI_EXTERN napi_status napi_make_callback(napi_env env,
                                           napi_async_context async_context,
                                           napi_value recv,
                                           napi_value func,
                                           size_t argc,
                                           const napi_value* argv,
                                           napi_value* result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] async_context`: Context for the async operation that is invoking the callback. This should normally be a value previously obtained from [`napi_async_init`](https://nodejs.org/docs/latest/api/n-api.html#napi_async_init). In order to retain ABI compatibility with previous versions, passing `NULL` for `async_context` does not result in an error. However, this results in incorrect operation of async hooks. Potential issues include loss of async context when using the `AsyncLocalStorage` API.
  * `[in] recv`: The `this` value passed to the called function.
  * `[in] func`: `napi_value` representing the JavaScript function to be invoked.
  * `[in] argc`: The count of elements in the `argv` array.
  * `[in] argv`: Array of JavaScript values as `napi_value` representing the arguments to the function. If `argc` is zero this parameter may be omitted by passing in `NULL`.
  * `[out] result`: `napi_value` representing the JavaScript object returned.


Returns `napi_ok` if the API succeeded.
This method allows a JavaScript function object to be called from a native add-on. This API is similar to `napi_call_function`. However, it is used to call _from_ native code back _into_ JavaScript _after_ returning from an async operation (when there is no other script on the stack). It is a fairly simple wrapper around `node::MakeCallback`.
Note it is _not_ necessary to use `napi_make_callback` from within a `napi_async_complete_callback`; in that situation the callback's async context has already been set up, so a direct call to `napi_call_function` is sufficient and appropriate. Use of the `napi_make_callback` function may be required when implementing custom async behavior that does not use `napi_create_async_work`.
Any `process.nextTick`s or Promises scheduled on the microtask queue by JavaScript during the callback are ran before returning back to C/C++.
####  `napi_open_callback_scope`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-open-callback-scope)
Added in: v9.6.0**N-API Version:** 3
```
NAPI_EXTERN napi_status napi_open_callback_scope(napi_env env,
                                                 napi_value resource_object,
                                                 napi_async_context context,
                                                 napi_callback_scope* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] resource_object`: An object associated with the async work that will be passed to possible `async_hooks` [`init` hooks](https://nodejs.org/docs/latest/api/async_hooks.html#initasyncid-type-triggerasyncid-resource). This parameter has been deprecated and is ignored at runtime. Use the `async_resource` parameter in [`napi_async_init`](https://nodejs.org/docs/latest/api/n-api.html#napi_async_init) instead.
  * `[in] context`: Context for the async operation that is invoking the callback. This should be a value previously obtained from [`napi_async_init`](https://nodejs.org/docs/latest/api/n-api.html#napi_async_init).
  * `[out] result`: The newly created scope.


There are cases (for example, resolving promises) where it is necessary to have the equivalent of the scope associated with a callback in place when making certain Node-API calls. If there is no other script on the stack the [`napi_open_callback_scope`](https://nodejs.org/docs/latest/api/n-api.html#napi_open_callback_scope) and [`napi_close_callback_scope`](https://nodejs.org/docs/latest/api/n-api.html#napi_close_callback_scope) functions can be used to open/close the required scope.
####  `napi_close_callback_scope`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-close-callback-scope)
Added in: v9.6.0**N-API Version:** 3
```
NAPI_EXTERN napi_status napi_close_callback_scope(napi_env env,
                                                  napi_callback_scope scope)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] scope`: The scope to be closed.


This API can be called even if there is a pending JavaScript exception.
### Version management[#](https://nodejs.org/docs/latest/api/n-api.html#version-management)
####  `napi_get_node_version`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-node-version)
Added in: v8.4.0**N-API Version:** 1
```
typedef struct {
  uint32_t major;
  uint32_t minor;
  uint32_t patch;
  const char* release;
} napi_node_version;

napi_status napi_get_node_version(node_api_basic_env env,
                                  const napi_node_version** version);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[out] version`: A pointer to version information for Node.js itself.


Returns `napi_ok` if the API succeeded.
This function fills the `version` struct with the major, minor, and patch version of Node.js that is currently running, and the `release` field with the value of [`process.release.name`](https://nodejs.org/docs/latest/api/process.html#processrelease).
The returned buffer is statically allocated and does not need to be freed.
####  `napi_get_version`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-version)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_get_version(node_api_basic_env env,
                             uint32_t* result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[out] result`: The highest version of Node-API supported.


Returns `napi_ok` if the API succeeded.
This API returns the highest Node-API version supported by the Node.js runtime. Node-API is planned to be additive such that newer releases of Node.js may support additional API functions. In order to allow an addon to use a newer function when running with versions of Node.js that support it, while providing fallback behavior when running with Node.js versions that don't support it:
  * Call `napi_get_version()` to determine if the API is available.
  * If available, dynamically load a pointer to the function using `uv_dlsym()`.
  * Use the dynamically loaded pointer to invoke the function.
  * If the function is not available, provide an alternate implementation that does not use the function.


### Memory management[#](https://nodejs.org/docs/latest/api/n-api.html#memory-management)
####  `napi_adjust_external_memory`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-adjust-external-memory)
Added in: v8.5.0**N-API Version:** 1
```
NAPI_EXTERN napi_status napi_adjust_external_memory(node_api_basic_env env,
                                                    int64_t change_in_bytes,
                                                    int64_t* result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] change_in_bytes`: The change in externally allocated memory that is kept alive by JavaScript objects.
  * `[out] result`: The adjusted value. This value should reflect the total amount of external memory with the given `change_in_bytes` included. The absolute value of the returned value should not be depended on. For example, implementations may use a single counter for all addons, or a counter for each addon.


Returns `napi_ok` if the API succeeded.
This function gives the runtime an indication of the amount of externally allocated memory that is kept alive by JavaScript objects (i.e. a JavaScript object that points to its own memory allocated by a native addon). Registering externally allocated memory may, but is not guaranteed to, trigger global garbage collections more often than it would otherwise.
This function is expected to be called in a manner such that an addon does not decrease the external memory more than it has increased the external memory.
### Promises[#](https://nodejs.org/docs/latest/api/n-api.html#promises)
Node-API provides facilities for creating `Promise` objects as described in `napi_create_promise()`, a "deferred" object is created and returned alongside the `Promise`. The deferred object is bound to the created `Promise` and is the only means to resolve or reject the `Promise` using `napi_resolve_deferred()` or `napi_reject_deferred()`. The deferred object that is created by `napi_create_promise()` is freed by `napi_resolve_deferred()` or `napi_reject_deferred()`. The `Promise` object may be returned to JavaScript where it can be used in the usual fashion.
For example, to create a promise and pass it to an asynchronous worker:
