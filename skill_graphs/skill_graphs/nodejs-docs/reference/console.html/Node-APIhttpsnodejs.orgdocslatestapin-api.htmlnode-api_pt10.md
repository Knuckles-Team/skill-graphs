```
napi_deferred deferred;
napi_value promise;
napi_status status;

// Create the promise.
status = napi_create_promise(env, &deferred, &promise);
if (status != napi_ok) return NULL;

// Pass the deferred to a function that performs an asynchronous action.
do_something_asynchronous(deferred);

// Return the promise to JS
return promise;
copy
```

The above function `do_something_asynchronous()` would perform its asynchronous action and then it would resolve or reject the deferred, thereby concluding the promise and freeing the deferred:
```
napi_deferred deferred;
napi_value undefined;
napi_status status;

// Create a value with which to conclude the deferred.
status = napi_get_undefined(env, &undefined);
if (status != napi_ok) return NULL;

// Resolve or reject the promise associated with the deferred depending on
// whether the asynchronous action succeeded.
if (asynchronous_action_succeeded) {
  status = napi_resolve_deferred(env, deferred, undefined);
} else {
  status = napi_reject_deferred(env, deferred, undefined);
}
if (status != napi_ok) return NULL;

// At this point the deferred has been freed, so we should assign NULL to it.
deferred = NULL;
copy
```

####  `napi_create_promise`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-promise)
Added in: v8.5.0**N-API Version:** 1
```
napi_status napi_create_promise(napi_env env,
                                napi_deferred* deferred,
                                napi_value* promise);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[out] deferred`: A newly created deferred object which can later be passed to `napi_resolve_deferred()` or `napi_reject_deferred()` to resolve resp. reject the associated promise.
  * `[out] promise`: The JavaScript promise associated with the deferred object.


Returns `napi_ok` if the API succeeded.
This API creates a deferred object and a JavaScript promise.
####  `napi_resolve_deferred`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-resolve-deferred)
Added in: v8.5.0**N-API Version:** 1
```
napi_status napi_resolve_deferred(napi_env env,
                                  napi_deferred deferred,
                                  napi_value resolution);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] deferred`: The deferred object whose associated promise to resolve.
  * `[in] resolution`: The value with which to resolve the promise.


This API resolves a JavaScript promise by way of the deferred object with which it is associated. Thus, it can only be used to resolve JavaScript promises for which the corresponding deferred object is available. This effectively means that the promise must have been created using `napi_create_promise()` and the deferred object returned from that call must have been retained in order to be passed to this API.
The deferred object is freed upon successful completion.
####  `napi_reject_deferred`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-reject-deferred)
Added in: v8.5.0**N-API Version:** 1
```
napi_status napi_reject_deferred(napi_env env,
                                 napi_deferred deferred,
                                 napi_value rejection);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] deferred`: The deferred object whose associated promise to resolve.
  * `[in] rejection`: The value with which to reject the promise.


This API rejects a JavaScript promise by way of the deferred object with which it is associated. Thus, it can only be used to reject JavaScript promises for which the corresponding deferred object is available. This effectively means that the promise must have been created using `napi_create_promise()` and the deferred object returned from that call must have been retained in order to be passed to this API.
The deferred object is freed upon successful completion.
####  `napi_is_promise`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-is-promise)
Added in: v8.5.0**N-API Version:** 1
```
napi_status napi_is_promise(napi_env env,
                            napi_value value,
                            bool* is_promise);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: The value to examine
  * `[out] is_promise`: Flag indicating whether `promise` is a native promise object (that is, a promise object created by the underlying engine).


### Script execution[#](https://nodejs.org/docs/latest/api/n-api.html#script-execution)
Node-API provides an API for executing a string containing JavaScript using the underlying JavaScript engine.
####  `napi_run_script`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-run-script)
Added in: v8.5.0**N-API Version:** 1
```
NAPI_EXTERN napi_status napi_run_script(napi_env env,
                                        napi_value script,
                                        napi_value* result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] script`: A JavaScript string containing the script to execute.
  * `[out] result`: The value resulting from having executed the script.


This function executes a string of JavaScript code and returns its result with the following caveats:
  * Unlike `eval`, this function does not allow the script to access the current lexical scope, and therefore also does not allow to access the [module scope](https://nodejs.org/docs/latest/api/modules.html#the-module-scope), meaning that pseudo-globals such as `require` will not be available.
  * The script can access the [global scope](https://nodejs.org/docs/latest/api/globals.html). Function and `var` declarations in the script will be added to the [`global`](https://nodejs.org/docs/latest/api/globals.html#global) object. Variable declarations made using `let` and `const` will be visible globally, but will not be added to the [`global`](https://nodejs.org/docs/latest/api/globals.html#global) object.
  * The value of `this` is [`global`](https://nodejs.org/docs/latest/api/globals.html#global) within the script.


### libuv event loop[#](https://nodejs.org/docs/latest/api/n-api.html#libuv-event-loop)
Node-API provides a function for getting the current event loop associated with a specific `napi_env`.
####  `napi_get_uv_event_loop`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-uv-event-loop)
Added in: v9.3.0, v8.10.0**N-API Version:** 2
```
NAPI_EXTERN napi_status napi_get_uv_event_loop(node_api_basic_env env,
                                               struct uv_loop_s** loop);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[out] loop`: The current libuv loop instance.


Note: While libuv has been relatively stable over time, it does not provide an ABI stability guarantee. Use of this function should be avoided. Its use may result in an addon that does not work across Node.js versions. [asynchronous-thread-safe-function-calls](https://nodejs.org/docs/latest/api/n-api.html#asynchronous-thread-safe-function-calls) are an alternative for many use cases.
### Asynchronous thread-safe function calls[#](https://nodejs.org/docs/latest/api/n-api.html#asynchronous-thread-safe-function-calls)
JavaScript functions can normally only be called from a native addon's main thread. If an addon creates additional threads, then Node-API functions that require a `napi_env`, `napi_value`, or `napi_ref` must not be called from those threads.
When an addon has additional threads and JavaScript functions need to be invoked based on the processing completed by those threads, those threads must communicate with the addon's main thread so that the main thread can invoke the JavaScript function on their behalf. The thread-safe function APIs provide an easy way to do this.
These APIs provide the type `napi_threadsafe_function` as well as APIs to create, destroy, and call objects of this type. `napi_create_threadsafe_function()` creates a persistent reference to a `napi_value` that holds a JavaScript function which can be called from multiple threads. The calls happen asynchronously. This means that values with which the JavaScript callback is to be called will be placed in a queue, and, for each value in the queue, a call will eventually be made to the JavaScript function.
Upon creation of a `napi_threadsafe_function` a `napi_finalize` callback can be provided. This callback will be invoked on the main thread when the thread-safe function is about to be destroyed. It receives the context and the finalize data given during construction, and provides an opportunity for cleaning up after the threads e.g. by calling `uv_thread_join()`. **Aside from the main loop thread, no threads should be using the thread-safe function after the finalize callback completes.**
The `context` given during the call to `napi_create_threadsafe_function()` can be retrieved from any thread with a call to `napi_get_threadsafe_function_context()`.
#### Calling a thread-safe function[#](https://nodejs.org/docs/latest/api/n-api.html#calling-a-thread-safe-function)
`napi_call_threadsafe_function()` can be used for initiating a call into JavaScript. `napi_call_threadsafe_function()` accepts a parameter which controls whether the API behaves blockingly. If set to `napi_tsfn_nonblocking`, the API behaves non-blockingly, returning `napi_queue_full` if the queue was full, preventing data from being successfully added to the queue. If set to `napi_tsfn_blocking`, the API blocks until space becomes available in the queue. `napi_call_threadsafe_function()` never blocks if the thread-safe function was created with a maximum queue size of 0.
`napi_call_threadsafe_function()` should not be called with `napi_tsfn_blocking` from a JavaScript thread, because, if the queue is full, it may cause the JavaScript thread to deadlock.
The actual call into JavaScript is controlled by the callback given via the `call_js_cb` parameter. `call_js_cb` is invoked on the main thread once for each value that was placed into the queue by a successful call to `napi_call_threadsafe_function()`. If such a callback is not given, a default callback will be used, and the resulting JavaScript call will have no arguments. The `call_js_cb` callback receives the JavaScript function to call as a `napi_value` in its parameters, as well as the `void*` context pointer used when creating the `napi_threadsafe_function`, and the next data pointer that was created by one of the secondary threads. The callback can then use an API such as `napi_call_function()` to call into JavaScript.
The callback may also be invoked with `env` and `call_js_cb` both set to `NULL` to indicate that calls into JavaScript are no longer possible, while items remain in the queue that may need to be freed. This normally occurs when the Node.js process exits while there is a thread-safe function still active.
It is not necessary to call into JavaScript via `napi_make_callback()` because Node-API runs `call_js_cb` in a context appropriate for callbacks.
Zero or more queued items may be invoked in each tick of the event loop. Applications should not depend on a specific behavior other than progress in invoking callbacks will be made and events will be invoked as time moves forward.
#### Reference counting of thread-safe functions[#](https://nodejs.org/docs/latest/api/n-api.html#reference-counting-of-thread-safe-functions)
Threads can be added to and removed from a `napi_threadsafe_function` object during its existence. Thus, in addition to specifying an initial number of threads upon creation, `napi_acquire_threadsafe_function` can be called to indicate that a new thread will start making use of the thread-safe function. Similarly, `napi_release_threadsafe_function` can be called to indicate that an existing thread will stop making use of the thread-safe function.
`napi_threadsafe_function` objects are destroyed when every thread which uses the object has called `napi_release_threadsafe_function()` or has received a return status of `napi_closing` in response to a call to `napi_call_threadsafe_function`. The queue is emptied before the `napi_threadsafe_function` is destroyed. `napi_release_threadsafe_function()` should be the last API call made in conjunction with a given `napi_threadsafe_function`, because after the call completes, there is no guarantee that the `napi_threadsafe_function` is still allocated. For the same reason, do not use a thread-safe function after receiving a return value of `napi_closing` in response to a call to `napi_call_threadsafe_function`. Data associated with the `napi_threadsafe_function` can be freed in its `napi_finalize` callback which was passed to `napi_create_threadsafe_function()`. The parameter `initial_thread_count` of `napi_create_threadsafe_function` marks the initial number of acquisitions of the thread-safe functions, instead of calling `napi_acquire_threadsafe_function` multiple times at creation.
Once the number of threads making use of a `napi_threadsafe_function` reaches zero, no further threads can start making use of it by calling `napi_acquire_threadsafe_function()`. In fact, all subsequent API calls associated with it, except `napi_release_threadsafe_function()`, will return an error value of `napi_closing`.
The thread-safe function can be "aborted" by giving a value of `napi_tsfn_abort` to `napi_release_threadsafe_function()`. This will cause all subsequent APIs associated with the thread-safe function except `napi_release_threadsafe_function()` to return `napi_closing` even before its reference count reaches zero. In particular, `napi_call_threadsafe_function()` will return `napi_closing`, thus informing the threads that it is no longer possible to make asynchronous calls to the thread-safe function. This can be used as a criterion for terminating the thread. **Upon receiving a return value of`napi_closing` from `napi_call_threadsafe_function()` a thread must not use the thread-safe function anymore because it is no longer guaranteed to be allocated.**
#### Deciding whether to keep the process running[#](https://nodejs.org/docs/latest/api/n-api.html#deciding-whether-to-keep-the-process-running)
Similarly to libuv handles, thread-safe functions can be "referenced" and "unreferenced". A "referenced" thread-safe function will cause the event loop on the thread on which it is created to remain alive until the thread-safe function is destroyed. In contrast, an "unreferenced" thread-safe function will not prevent the event loop from exiting. The APIs `napi_ref_threadsafe_function` and `napi_unref_threadsafe_function` exist for this purpose.
Neither does `napi_unref_threadsafe_function` mark the thread-safe functions as able to be destroyed nor does `napi_ref_threadsafe_function` prevent it from being destroyed.
####  `napi_create_threadsafe_function`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-threadsafe-function)
Added in: v10.6.0**N-API Version:** 4History Version | Changes
---|---
v12.6.0, v10.17.0 | Made `func` parameter optional with custom `call_js_cb`.
```
NAPI_EXTERN napi_status
napi_create_threadsafe_function(napi_env env,
                                napi_value func,
                                napi_value async_resource,
                                napi_value async_resource_name,
                                size_t max_queue_size,
                                size_t initial_thread_count,
                                void* thread_finalize_data,
                                napi_finalize thread_finalize_cb,
                                void* context,
                                napi_threadsafe_function_call_js call_js_cb,
                                napi_threadsafe_function* result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] func`: An optional JavaScript function to call from another thread. It must be provided if `NULL` is passed to `call_js_cb`.
  * `[in] async_resource`: An optional object associated with the async work that will be passed to possible `async_hooks` [`init` hooks](https://nodejs.org/docs/latest/api/async_hooks.html#initasyncid-type-triggerasyncid-resource).
  * `[in] async_resource_name`: A JavaScript string to provide an identifier for the kind of resource that is being provided for diagnostic information exposed by the `async_hooks` API.
  * `[in] max_queue_size`: Maximum size of the queue. `0` for no limit.
  * `[in] initial_thread_count`: The initial number of acquisitions, i.e. the initial number of threads, including the main thread, which will be making use of this function.
  * `[in] thread_finalize_data`: Optional data to be passed to `thread_finalize_cb`.
  * `[in] thread_finalize_cb`: Optional function to call when the `napi_threadsafe_function` is being destroyed.
  * `[in] context`: Optional data to attach to the resulting `napi_threadsafe_function`.
  * `[in] call_js_cb`: Optional callback which calls the JavaScript function in response to a call on a different thread. This callback will be called on the main thread. If not given, the JavaScript function will be called with no parameters and with `undefined` as its `this` value. [`napi_threadsafe_function_call_js`](https://nodejs.org/docs/latest/api/n-api.html#napi_threadsafe_function_call_js) provides more details.
  * `[out] result`: The asynchronous thread-safe JavaScript function.


**Change History:**
  * Version 10 (`NAPI_VERSION` is defined as `10` or higher):
Uncaught exceptions thrown in `call_js_cb` are handled with the [`'uncaughtException'`](https://nodejs.org/docs/latest/api/process.html#event-uncaughtexception) event, instead of being ignored.


####  `napi_get_threadsafe_function_context`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-threadsafe-function-context)
Added in: v10.6.0**N-API Version:** 4
```
NAPI_EXTERN napi_status
napi_get_threadsafe_function_context(napi_threadsafe_function func,
                                     void** result);
copy
```

  * `[in] func`: The thread-safe function for which to retrieve the context.
  * `[out] result`: The location where to store the context.


This API may be called from any thread which makes use of `func`.
####  `napi_call_threadsafe_function`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-call-threadsafe-function)
Added in: v10.6.0**N-API Version:** 4History Version | Changes
---|---
v14.5.0 | Support for `napi_would_deadlock` has been reverted.
v14.1.0 | Return `napi_would_deadlock` when called with `napi_tsfn_blocking` from the main thread or a worker thread and the queue is full.
```
NAPI_EXTERN napi_status
napi_call_threadsafe_function(napi_threadsafe_function func,
                              void* data,
                              napi_threadsafe_function_call_mode is_blocking);
copy
```

  * `[in] func`: The asynchronous thread-safe JavaScript function to invoke.
  * `[in] data`: Data to send into JavaScript via the callback `call_js_cb` provided during the creation of the thread-safe JavaScript function.
  * `[in] is_blocking`: Flag whose value can be either `napi_tsfn_blocking` to indicate that the call should block if the queue is full or `napi_tsfn_nonblocking` to indicate that the call should return immediately with a status of `napi_queue_full` whenever the queue is full.


This API should not be called with `napi_tsfn_blocking` from a JavaScript thread, because, if the queue is full, it may cause the JavaScript thread to deadlock.
This API will return `napi_closing` if `napi_release_threadsafe_function()` was called with `abort` set to `napi_tsfn_abort` from any thread. The value is only added to the queue if the API returns `napi_ok`.
This API may be called from any thread which makes use of `func`.
####  `napi_acquire_threadsafe_function`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-acquire-threadsafe-function)
Added in: v10.6.0**N-API Version:** 4
```
NAPI_EXTERN napi_status
napi_acquire_threadsafe_function(napi_threadsafe_function func);
copy
```

  * `[in] func`: The asynchronous thread-safe JavaScript function to start making use of.


A thread should call this API before passing `func` to any other thread-safe function APIs to indicate that it will be making use of `func`. This prevents `func` from being destroyed when all other threads have stopped making use of it.
This API may be called from any thread which will start making use of `func`.
####  `napi_release_threadsafe_function`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-release-threadsafe-function)
Added in: v10.6.0**N-API Version:** 4
```
NAPI_EXTERN napi_status
napi_release_threadsafe_function(napi_threadsafe_function func,
                                 napi_threadsafe_function_release_mode mode);
copy
```

  * `[in] func`: The asynchronous thread-safe JavaScript function whose reference count to decrement.
  * `[in] mode`: Flag whose value can be either `napi_tsfn_release` to indicate that the current thread will make no further calls to the thread-safe function, or `napi_tsfn_abort` to indicate that in addition to the current thread, no other thread should make any further calls to the thread-safe function. If set to `napi_tsfn_abort`, further calls to `napi_call_threadsafe_function()` will return `napi_closing`, and no further values will be placed in the queue.


A thread should call this API when it stops making use of `func`. Passing `func` to any thread-safe APIs after having called this API has undefined results, as `func` may have been destroyed.
This API may be called from any thread which will stop making use of `func`.
####  `napi_ref_threadsafe_function`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-ref-threadsafe-function)
Added in: v10.6.0**N-API Version:** 4
```
NAPI_EXTERN napi_status
napi_ref_threadsafe_function(node_api_basic_env env, napi_threadsafe_function func);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] func`: The thread-safe function to reference.


This API is used to indicate that the event loop running on the main thread should not exit until `func` has been destroyed. Similar to
Neither does `napi_unref_threadsafe_function` mark the thread-safe functions as able to be destroyed nor does `napi_ref_threadsafe_function` prevent it from being destroyed. `napi_acquire_threadsafe_function` and `napi_release_threadsafe_function` are available for that purpose.
This API may only be called from the main thread.
####  `napi_unref_threadsafe_function`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-unref-threadsafe-function)
Added in: v10.6.0**N-API Version:** 4
```
NAPI_EXTERN napi_status
napi_unref_threadsafe_function(node_api_basic_env env, napi_threadsafe_function func);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] func`: The thread-safe function to unreference.


This API is used to indicate that the event loop running on the main thread may exit before `func` is destroyed. Similar to
This API may only be called from the main thread.
### Miscellaneous utilities[#](https://nodejs.org/docs/latest/api/n-api.html#miscellaneous-utilities)
####  `node_api_get_module_file_name`[#](https://nodejs.org/docs/latest/api/n-api.html#node-api-get-module-file-name)
Added in: v15.9.0, v14.18.0, v12.22.0**N-API Version:** 9
```
NAPI_EXTERN napi_status
node_api_get_module_file_name(node_api_basic_env env, const char** result);

copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[out] result`: A URL containing the absolute path of the location from which the add-on was loaded. For a file on the local file system it will start with `file://`. The string is null-terminated and owned by `env` and must thus not be modified or freed.


`result` may be an empty string if the add-on loading process fails to establish the add-on's file name during loading.
