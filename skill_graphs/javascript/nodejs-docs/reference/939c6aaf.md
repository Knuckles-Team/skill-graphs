Handle scopes are created using [`napi_open_handle_scope`](https://nodejs.org/docs/latest/api/n-api.html#napi_open_handle_scope) and are destroyed using [`napi_close_handle_scope`](https://nodejs.org/docs/latest/api/n-api.html#napi_close_handle_scope). Closing the scope can indicate to the GC that all `napi_value`s created during the lifetime of the handle scope are no longer referenced from the current stack frame.
For more details, review the [Object lifetime management](https://nodejs.org/docs/latest/api/n-api.html#object-lifetime-management).
#####  `napi_escapable_handle_scope`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-escapable-handle-scope)
Added in: v8.0.0**N-API Version:** 1
Escapable handle scopes are a special type of handle scope to return values created within a particular handle scope to a parent scope.
#####  `napi_ref`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-ref)
Added in: v8.0.0**N-API Version:** 1
This is the abstraction to use to reference a `napi_value`. This allows for users to manage the lifetimes of JavaScript values, including defining their minimum lifetimes explicitly.
For more details, review the [Object lifetime management](https://nodejs.org/docs/latest/api/n-api.html#object-lifetime-management).
#####  `napi_type_tag`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-type-tag)
Added in: v14.8.0, v12.19.0**N-API Version:** 8
A 128-bit value stored as two unsigned 64-bit integers. It serves as a UUID with which JavaScript objects or [externals](https://nodejs.org/docs/latest/api/n-api.html#napi_create_external) can be "tagged" in order to ensure that they are of a certain type. This is a stronger check than [`napi_instanceof`](https://nodejs.org/docs/latest/api/n-api.html#napi_instanceof), because the latter can report a false positive if the object's prototype has been manipulated. Type-tagging is most useful in conjunction with [`napi_wrap`](https://nodejs.org/docs/latest/api/n-api.html#napi_wrap) because it ensures that the pointer retrieved from a wrapped object can be safely cast to the native type corresponding to the type tag that had been previously applied to the JavaScript object.
```
typedef struct {
  uint64_t lower;
  uint64_t upper;
} napi_type_tag;
copy
```

#####  `napi_async_cleanup_hook_handle`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-async-cleanup-hook-handle)
Added in: v14.10.0, v12.19.0
An opaque value returned by [`napi_add_async_cleanup_hook`](https://nodejs.org/docs/latest/api/n-api.html#napi_add_async_cleanup_hook). It must be passed to [`napi_remove_async_cleanup_hook`](https://nodejs.org/docs/latest/api/n-api.html#napi_remove_async_cleanup_hook) when the chain of asynchronous cleanup events completes.
#### Node-API callback types[#](https://nodejs.org/docs/latest/api/n-api.html#node-api-callback-types)
#####  `napi_callback_info`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-callback-info)
Added in: v8.0.0**N-API Version:** 1
Opaque datatype that is passed to a callback function. It can be used for getting additional information about the context in which the callback was invoked.
#####  `napi_callback`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-callback)
Added in: v8.0.0**N-API Version:** 1
Function pointer type for user-provided native functions which are to be exposed to JavaScript via Node-API. Callback functions should satisfy the following signature:
```
typedef napi_value (*napi_callback)(napi_env, napi_callback_info);
copy
```

Unless for reasons discussed in [Object Lifetime Management](https://nodejs.org/docs/latest/api/n-api.html#object-lifetime-management), creating a handle and/or callback scope inside a `napi_callback` is not necessary.
#####  `node_api_basic_finalize`[#](https://nodejs.org/docs/latest/api/n-api.html#node-api-basic-finalize)
Added in: v21.6.0, v20.12.0, v18.20.0
Stability: 1 - Experimental
Function pointer type for add-on provided functions that allow the user to be notified when externally-owned data is ready to be cleaned up because the object it was associated with has been garbage-collected. The user must provide a function satisfying the following signature which would get called upon the object's collection. Currently, `node_api_basic_finalize` can be used for finding out when objects that have external data are collected.
```
typedef void (*node_api_basic_finalize)(node_api_basic_env env,
                                      void* finalize_data,
                                      void* finalize_hint);
copy
```

Unless for reasons discussed in [Object Lifetime Management](https://nodejs.org/docs/latest/api/n-api.html#object-lifetime-management), creating a handle and/or callback scope inside the function body is not necessary.
Since these functions may be called while the JavaScript engine is in a state where it cannot execute JavaScript code, only Node-APIs which accept a `node_api_basic_env` as their first parameter may be called. [`node_api_post_finalizer`](https://nodejs.org/docs/latest/api/n-api.html#node_api_post_finalizer) can be used to schedule Node-API calls that require access to the JavaScript engine's state to run after the current garbage collection cycle has completed.
In the case of [`node_api_create_external_string_latin1`](https://nodejs.org/docs/latest/api/n-api.html#node_api_create_external_string_latin1) and [`node_api_create_external_string_utf16`](https://nodejs.org/docs/latest/api/n-api.html#node_api_create_external_string_utf16) the `env` parameter may be null, because external strings can be collected during the latter part of environment shutdown.
Change History:
  * experimental (`NAPI_EXPERIMENTAL`):
Only Node-API calls that accept a `node_api_basic_env` as their first parameter may be called, otherwise the application will be terminated with an appropriate error message. This feature can be turned off by defining `NODE_API_EXPERIMENTAL_BASIC_ENV_OPT_OUT`.


#####  `napi_finalize`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-finalize)
Added in: v8.0.0**N-API Version:** 1
Function pointer type for add-on provided function that allow the user to schedule a group of calls to Node-APIs in response to a garbage collection event, after the garbage collection cycle has completed. These function pointers can be used with [`node_api_post_finalizer`](https://nodejs.org/docs/latest/api/n-api.html#node_api_post_finalizer).
```
typedef void (*napi_finalize)(napi_env env,
                              void* finalize_data,
                              void* finalize_hint);
copy
```

Change History:
  * experimental (`NAPI_EXPERIMENTAL` is defined):
A function of this type may no longer be used as a finalizer, except with [`node_api_post_finalizer`](https://nodejs.org/docs/latest/api/n-api.html#node_api_post_finalizer). [`node_api_basic_finalize`](https://nodejs.org/docs/latest/api/n-api.html#node_api_basic_finalize) must be used instead. This feature can be turned off by defining `NODE_API_EXPERIMENTAL_BASIC_ENV_OPT_OUT`.


#####  `napi_async_execute_callback`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-async-execute-callback)
Added in: v8.0.0**N-API Version:** 1
Function pointer used with functions that support asynchronous operations. Callback functions must satisfy the following signature:
```
typedef void (*napi_async_execute_callback)(napi_env env, void* data);
copy
```

Implementations of this function must avoid making Node-API calls that execute JavaScript or interact with JavaScript objects. Node-API calls should be in the `napi_async_complete_callback` instead. Do not use the `napi_env` parameter as it will likely result in execution of JavaScript.
#####  `napi_async_complete_callback`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-async-complete-callback)
Added in: v8.0.0**N-API Version:** 1
Function pointer used with functions that support asynchronous operations. Callback functions must satisfy the following signature:
```
typedef void (*napi_async_complete_callback)(napi_env env,
                                             napi_status status,
                                             void* data);
copy
```

Unless for reasons discussed in [Object Lifetime Management](https://nodejs.org/docs/latest/api/n-api.html#object-lifetime-management), creating a handle and/or callback scope inside the function body is not necessary.
#####  `napi_threadsafe_function_call_js`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-threadsafe-function-call-js)
Added in: v10.6.0**N-API Version:** 4
Function pointer used with asynchronous thread-safe function calls. The callback will be called on the main thread. Its purpose is to use a data item arriving via the queue from one of the secondary threads to construct the parameters necessary for a call into JavaScript, usually via `napi_call_function`, and then make the call into JavaScript.
The data arriving from the secondary thread via the queue is given in the `data` parameter and the JavaScript function to call is given in the `js_callback` parameter.
Node-API sets up the environment prior to calling this callback, so it is sufficient to call the JavaScript function via `napi_call_function` rather than via `napi_make_callback`.
Callback functions must satisfy the following signature:
```
typedef void (*napi_threadsafe_function_call_js)(napi_env env,
                                                 napi_value js_callback,
                                                 void* context,
                                                 void* data);
copy
```

  * `[in] env`: The environment to use for API calls, or `NULL` if the thread-safe function is being torn down and `data` may need to be freed.
  * `[in] js_callback`: The JavaScript function to call, or `NULL` if the thread-safe function is being torn down and `data` may need to be freed. It may also be `NULL` if the thread-safe function was created without `js_callback`.
  * `[in] context`: The optional data with which the thread-safe function was created.
  * `[in] data`: Data created by the secondary thread. It is the responsibility of the callback to convert this native data to JavaScript values (with Node-API functions) that can be passed as parameters when `js_callback` is invoked. This pointer is managed entirely by the threads and this callback. Thus this callback should free the data.


Unless for reasons discussed in [Object Lifetime Management](https://nodejs.org/docs/latest/api/n-api.html#object-lifetime-management), creating a handle and/or callback scope inside the function body is not necessary.
#####  `napi_cleanup_hook`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-cleanup-hook)
Added in: v19.2.0, v18.13.0**N-API Version:** 3
Function pointer used with [`napi_add_env_cleanup_hook`](https://nodejs.org/docs/latest/api/n-api.html#napi_add_env_cleanup_hook). It will be called when the environment is being torn down.
Callback functions must satisfy the following signature:
```
typedef void (*napi_cleanup_hook)(void* data);
copy
```

  * `[in] data`: The data that was passed to [`napi_add_env_cleanup_hook`](https://nodejs.org/docs/latest/api/n-api.html#napi_add_env_cleanup_hook).


#####  `napi_async_cleanup_hook`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-async-cleanup-hook)
Added in: v14.10.0, v12.19.0
Function pointer used with [`napi_add_async_cleanup_hook`](https://nodejs.org/docs/latest/api/n-api.html#napi_add_async_cleanup_hook). It will be called when the environment is being torn down.
Callback functions must satisfy the following signature:
```
typedef void (*napi_async_cleanup_hook)(napi_async_cleanup_hook_handle handle,
                                        void* data);
copy
```

  * `[in] handle`: The handle that must be passed to [`napi_remove_async_cleanup_hook`](https://nodejs.org/docs/latest/api/n-api.html#napi_remove_async_cleanup_hook) after completion of the asynchronous cleanup.
  * `[in] data`: The data that was passed to [`napi_add_async_cleanup_hook`](https://nodejs.org/docs/latest/api/n-api.html#napi_add_async_cleanup_hook).


The body of the function should initiate the asynchronous cleanup actions at the end of which `handle` must be passed in a call to [`napi_remove_async_cleanup_hook`](https://nodejs.org/docs/latest/api/n-api.html#napi_remove_async_cleanup_hook).
### Error handling[#](https://nodejs.org/docs/latest/api/n-api.html#error-handling)
Node-API uses both return values and JavaScript exceptions for error handling. The following sections explain the approach for each case.
#### Return values[#](https://nodejs.org/docs/latest/api/n-api.html#return-values)
Added in: v8.0.0**N-API Version:** 1
All of the Node-API functions share the same error handling pattern. The return type of all API functions is `napi_status`.
The return value will be `napi_ok` if the request was successful and no uncaught JavaScript exception was thrown. If an error occurred AND an exception was thrown, the `napi_status` value for the error will be returned. If an exception was thrown, and no error occurred, `napi_pending_exception` will be returned.
In cases where a return value other than `napi_ok` or `napi_pending_exception` is returned, [`napi_is_exception_pending`](https://nodejs.org/docs/latest/api/n-api.html#napi_is_exception_pending) must be called to check if an exception is pending. See the section on exceptions for more details.
The full set of possible `napi_status` values is defined in `napi_api_types.h`.
The `napi_status` return value provides a VM-independent representation of the error which occurred. In some cases it is useful to be able to get more detailed information, including a string representing the error as well as VM (engine)-specific information.
In order to retrieve this information [`napi_get_last_error_info`](https://nodejs.org/docs/latest/api/n-api.html#napi_get_last_error_info) is provided which returns a `napi_extended_error_info` structure. The format of the `napi_extended_error_info` structure is as follows:
```
typedef struct napi_extended_error_info {
  const char* error_message;
  void* engine_reserved;
  uint32_t engine_error_code;
  napi_status error_code;
};
copy
```

  * `error_message`: Textual representation of the error that occurred.
  * `engine_reserved`: Opaque handle reserved for engine use only.
  * `engine_error_code`: VM specific error code.
  * `error_code`: Node-API status code for the last error.


[`napi_get_last_error_info`](https://nodejs.org/docs/latest/api/n-api.html#napi_get_last_error_info) returns the information for the last Node-API call that was made.
Do not rely on the content or format of any of the extended information as it is not subject to SemVer and may change at any time. It is intended only for logging purposes.
#####  `napi_get_last_error_info`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-last-error-info)
Added in: v8.0.0**N-API Version:** 1
```
napi_status
napi_get_last_error_info(node_api_basic_env env,
                         const napi_extended_error_info** result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[out] result`: The `napi_extended_error_info` structure with more information about the error.


Returns `napi_ok` if the API succeeded.
This API retrieves a `napi_extended_error_info` structure with information about the last error that occurred.
The content of the `napi_extended_error_info` returned is only valid up until a Node-API function is called on the same `env`. This includes a call to `napi_is_exception_pending` so it may often be necessary to make a copy of the information so that it can be used later. The pointer returned in `error_message` points to a statically-defined string so it is safe to use that pointer if you have copied it out of the `error_message` field (which will be overwritten) before another Node-API function was called.
Do not rely on the content or format of any of the extended information as it is not subject to SemVer and may change at any time. It is intended only for logging purposes.
This API can be called even if there is a pending JavaScript exception.
#### Exceptions[#](https://nodejs.org/docs/latest/api/n-api.html#exceptions)
Any Node-API function call may result in a pending JavaScript exception. This is the case for any of the API functions, even those that may not cause the execution of JavaScript.
If the `napi_status` returned by a function is `napi_ok` then no exception is pending and no additional action is required. If the `napi_status` returned is anything other than `napi_ok` or `napi_pending_exception`, in order to try to recover and continue instead of simply returning immediately, [`napi_is_exception_pending`](https://nodejs.org/docs/latest/api/n-api.html#napi_is_exception_pending) must be called in order to determine if an exception is pending or not.
In many cases when a Node-API function is called and an exception is already pending, the function will return immediately with a `napi_status` of `napi_pending_exception`. However, this is not the case for all functions. Node-API allows a subset of the functions to be called to allow for some minimal cleanup before returning to JavaScript. In that case, `napi_status` will reflect the status for the function. It will not reflect previous pending exceptions. To avoid confusion, check the error status after every function call.
When an exception is pending one of two approaches can be employed.
The first approach is to do any appropriate cleanup and then return so that execution will return to JavaScript. As part of the transition back to JavaScript, the exception will be thrown at the point in the JavaScript code where the native method was invoked. The behavior of most Node-API calls is unspecified while an exception is pending, and many will simply return `napi_pending_exception`, so do as little as possible and then return to JavaScript where the exception can be handled.
The second approach is to try to handle the exception. There will be cases where the native code can catch the exception, take the appropriate action, and then continue. This is only recommended in specific cases where it is known that the exception can be safely handled. In these cases [`napi_get_and_clear_last_exception`](https://nodejs.org/docs/latest/api/n-api.html#napi_get_and_clear_last_exception) can be used to get and clear the exception. On success, result will contain the handle to the last JavaScript `Object` thrown. If it is determined, after retrieving the exception, the exception cannot be handled after all it can be re-thrown it with [`napi_throw`](https://nodejs.org/docs/latest/api/n-api.html#napi_throw) where error is the JavaScript value to be thrown.
The following utility functions are also available in case native code needs to throw an exception or determine if a `napi_value` is an instance of a JavaScript `Error` object: [`napi_throw_error`](https://nodejs.org/docs/latest/api/n-api.html#napi_throw_error), [`napi_throw_type_error`](https://nodejs.org/docs/latest/api/n-api.html#napi_throw_type_error), [`napi_throw_range_error`](https://nodejs.org/docs/latest/api/n-api.html#napi_throw_range_error), [`node_api_throw_syntax_error`](https://nodejs.org/docs/latest/api/n-api.html#node_api_throw_syntax_error) and [`napi_is_error`](https://nodejs.org/docs/latest/api/n-api.html#napi_is_error).
The following utility functions are also available in case native code needs to create an `Error` object: [`napi_create_error`](https://nodejs.org/docs/latest/api/n-api.html#napi_create_error), [`napi_create_type_error`](https://nodejs.org/docs/latest/api/n-api.html#napi_create_type_error), [`napi_create_range_error`](https://nodejs.org/docs/latest/api/n-api.html#napi_create_range_error) and [`node_api_create_syntax_error`](https://nodejs.org/docs/latest/api/n-api.html#node_api_create_syntax_error), where result is the `napi_value` that refers to the newly created JavaScript `Error` object.
The Node.js project is adding error codes to all of the errors generated internally. The goal is for applications to use these error codes for all error checking. The associated error messages will remain, but will only be meant to be used for logging and display with the expectation that the message can change without SemVer applying. In order to support this model with Node-API, both in internal functionality and for module specific functionality (as its good practice), the `throw_` and `create_` functions take an optional code parameter which is the string for the code to be added to the error object. If the optional parameter is `NULL` then no code will be associated with the error. If a code is provided, the name associated with the error is also updated to be:
```
originalName [code]
copy
```

where `originalName` is the original name associated with the error and `code` is the code that was provided. For example, if the code is `'ERR_ERROR_1'` and a `TypeError` is being created the name will be:
```
TypeError [ERR_ERROR_1]
copy
```

#####  `napi_throw`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-throw)
Added in: v8.0.0**N-API Version:** 1
```
NAPI_EXTERN napi_status napi_throw(napi_env env, napi_value error);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] error`: The JavaScript value to be thrown.


Returns `napi_ok` if the API succeeded.
This API throws the JavaScript value provided.
#####  `napi_throw_error`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-throw-error)
Added in: v8.0.0**N-API Version:** 1
```
NAPI_EXTERN napi_status napi_throw_error(napi_env env,
                                         const char* code,
                                         const char* msg);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] code`: Optional error code to be set on the error.
  * `[in] msg`: C string representing the text to be associated with the error.


Returns `napi_ok` if the API succeeded.
This API throws a JavaScript `Error` with the text provided.
#####  `napi_throw_type_error`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-throw-type-error)
Added in: v8.0.0**N-API Version:** 1
```
NAPI_EXTERN napi_status napi_throw_type_error(napi_env env,
                                              const char* code,
                                              const char* msg);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] code`: Optional error code to be set on the error.
  * `[in] msg`: C string representing the text to be associated with the error.


Returns `napi_ok` if the API succeeded.
This API throws a JavaScript `TypeError` with the text provided.
#####  `napi_throw_range_error`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-throw-range-error)
Added in: v8.0.0**N-API Version:** 1
```
NAPI_EXTERN napi_status napi_throw_range_error(napi_env env,
                                               const char* code,
                                               const char* msg);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] code`: Optional error code to be set on the error.
  * `[in] msg`: C string representing the text to be associated with the error.


Returns `napi_ok` if the API succeeded.
This API throws a JavaScript `RangeError` with the text provided.
#####  `node_api_throw_syntax_error`[#](https://nodejs.org/docs/latest/api/n-api.html#node-api-throw-syntax-error)
Added in: v17.2.0, v16.14.0**N-API Version:** 9
```
NAPI_EXTERN napi_status node_api_throw_syntax_error(napi_env env,
                                                    const char* code,
                                                    const char* msg);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] code`: Optional error code to be set on the error.
  * `[in] msg`: C string representing the text to be associated with the error.


Returns `napi_ok` if the API succeeded.
This API throws a JavaScript `SyntaxError` with the text provided.
#####  `napi_is_error`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-is-error)
Added in: v8.0.0**N-API Version:** 1
```
NAPI_EXTERN napi_status napi_is_error(napi_env env,
                                      napi_value value,
                                      bool* result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: The `napi_value` to be checked.
  * `[out] result`: Boolean value that is set to true if `napi_value` represents an error, false otherwise.


Returns `napi_ok` if the API succeeded.
This API queries a `napi_value` to check if it represents an error object.
#####  `napi_create_error`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-error)
Added in: v8.0.0**N-API Version:** 1
```
NAPI_EXTERN napi_status napi_create_error(napi_env env,
                                          napi_value code,
                                          napi_value msg,
                                          napi_value* result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] code`: Optional `napi_value` with the string for the error code to be associated with the error.
  * `[in] msg`: `napi_value` that references a JavaScript `string` to be used as the message for the `Error`.
  * `[out] result`: `napi_value` representing the error created.


Returns `napi_ok` if the API succeeded.
This API returns a JavaScript `Error` with the text provided.
#####  `napi_create_type_error`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-type-error)
