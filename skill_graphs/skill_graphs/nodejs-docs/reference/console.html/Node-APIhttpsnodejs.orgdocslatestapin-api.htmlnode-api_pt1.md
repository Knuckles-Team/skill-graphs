## Node-API[#](https://nodejs.org/docs/latest/api/n-api.html#node-api)
[Stability: 2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Stable
Node-API (formerly N-API) is an API for building native Addons. It is independent from the underlying JavaScript runtime (for example, V8) and is maintained as part of Node.js itself. This API will be Application Binary Interface (ABI) stable across versions of Node.js. It is intended to insulate addons from changes in the underlying JavaScript engine and allow modules compiled for one major version to run on later major versions of Node.js without recompilation. The [ABI Stability](https://nodejs.org/en/docs/guides/abi-stability/) guide provides a more in-depth explanation.
Addons are built/packaged with the same approach/tools outlined in the section titled [C++ Addons](https://nodejs.org/docs/latest/api/addons.html). The only difference is the set of APIs that are used by the native code. Instead of using the V8 or
APIs exposed by Node-API are generally used to create and manipulate JavaScript values. Concepts and operations generally map to ideas specified in the ECMA-262 Language Specification. The APIs have the following properties:
  * All Node-API calls return a status code of type `napi_status`. This status indicates whether the API call succeeded or failed.
  * The API's return value is passed via an out parameter.
  * All JavaScript values are abstracted behind an opaque type named `napi_value`.
  * In case of an error status code, additional information can be obtained using `napi_get_last_error_info`. More information can be found in the error handling section [Error handling](https://nodejs.org/docs/latest/api/n-api.html#error-handling).


### Writing addons in various programming languages[#](https://nodejs.org/docs/latest/api/n-api.html#writing-addons-in-various-programming-languages)
Node-API is a C API that ensures ABI stability across Node.js versions and different compiler levels. With this stability guarantee, it is possible to write addons in other programming languages on top of Node-API. Refer to
`node-addon-api` will depend on the symbols of the Node-API C-based functions exported by Node.js. The following code snippet is an example of `node-addon-api`:
```
Object obj = Object::New(env);
obj["foo"] = String::New(env, "bar");
copy
```

The above `node-addon-api` C++ code is equivalent to the following C-based Node-API code:
```
napi_status status;
napi_value object, string;
status = napi_create_object(env, &object);
if (status != napi_ok) {
  napi_throw_error(env, ...);
  return;
}

status = napi_create_string_utf8(env, "bar", NAPI_AUTO_LENGTH, &string);
if (status != napi_ok) {
  napi_throw_error(env, ...);
  return;
}

status = napi_set_named_property(env, object, "foo", string);
if (status != napi_ok) {
  napi_throw_error(env, ...);
  return;
}
copy
```

The end result is that the addon only uses the exported C APIs. Even though the addon is written in C++, it still gets the benefits of the ABI stability provided by the C Node-API.
When using `node-addon-api` instead of the C APIs, start with the API `node-addon-api`.
The `node-addon-api`. Additional media resources can be found on the
### Implications of ABI stability[#](https://nodejs.org/docs/latest/api/n-api.html#implications-of-abi-stability)
Although Node-API provides an ABI stability guarantee, other parts of Node.js do not, and any external libraries used from the addon may not. In particular, none of the following APIs provide an ABI stability guarantee across major versions:
  * the Node.js C++ APIs available via any of
```
#include <node.h>
#include <node_buffer.h>
#include <node_version.h>
#include <node_object_wrap.h>
copy
```

  * the libuv APIs which are also included with Node.js and available via
```
#include <uv.h>
copy
```

  * the V8 API available via
```
#include <v8.h>
copy
```



Thus, for an addon to remain ABI-compatible across Node.js major versions, it must use Node-API exclusively by restricting itself to using
```
#include <node_api.h>
copy
```

and by checking, for all external libraries that it uses, that the external library makes ABI stability guarantees similar to Node-API.
#### Enum values in ABI stability[#](https://nodejs.org/docs/latest/api/n-api.html#enum-values-in-abi-stability)
All enum data types defined in Node-API should be considered as a fixed size `int32_t` value. Bit flag enum types should be explicitly documented, and they work with bit operators like bit-OR (`|`) as a bit value. Unless otherwise documented, an enum type should be considered to be extensible.
A new enum value will be added at the end of the enum definition. An enum value will not be removed or renamed.
For an enum type returned from a Node-API function, or provided as an out parameter of a Node-API function, the value is an integer value and an addon should handle unknown values. New values are allowed to be introduced without a version guard. For example, when checking `napi_status` in switch statements, an addon should include a default branch, as new status codes may be introduced in newer Node.js versions.
For an enum type used in an in-parameter, the result of passing an unknown integer value to Node-API functions is undefined unless otherwise documented. A new value is added with a version guard to indicate the Node-API version in which it was introduced. For example, `napi_get_all_property_names` can be extended with new enum value of `napi_key_filter`.
For an enum type used in both in-parameters and out-parameters, new values are allowed to be introduced without a version guard.
### Building[#](https://nodejs.org/docs/latest/api/n-api.html#building)
Unlike modules written in JavaScript, developing and deploying Node.js native addons using Node-API requires an additional set of tools. Besides the basic tools required to develop for Node.js, the native addon developer requires a toolchain that can compile C and C++ code into a binary. In addition, depending upon how the native addon is deployed, the _user_ of the native addon will also need to have a C/C++ toolchain installed.
For Linux developers, the necessary C/C++ toolchain packages are readily available.
For Mac developers,
```
xcode-select --install
copy
```

For Windows developers,
```
npm install --global windows-build-tools
copy
```

The sections below describe the additional tools available for developing and deploying Node.js native addons.
#### Build tools[#](https://nodejs.org/docs/latest/api/n-api.html#build-tools)
Both the tools listed here require that _users_ of the native addon have a C/C++ toolchain installed in order to successfully install the native addon.
##### node-gyp[#](https://nodejs.org/docs/latest/api/n-api.html#node-gyp)
Historically, node-gyp has been the tool of choice for building native addons. It has widespread adoption and documentation. However, some developers have run into limitations in node-gyp.
##### CMake.js[#](https://nodejs.org/docs/latest/api/n-api.html#cmakejs)
CMake.js is a good choice for projects that already use CMake or for developers affected by limitations in node-gyp.
#### Uploading precompiled binaries[#](https://nodejs.org/docs/latest/api/n-api.html#uploading-precompiled-binaries)
The three tools listed here permit native addon developers and maintainers to create and upload binaries to public or private servers. These tools are typically integrated with CI/CD build systems like
##### node-pre-gyp[#](https://nodejs.org/docs/latest/api/n-api.html#node-pre-gyp)
##### prebuild[#](https://nodejs.org/docs/latest/api/n-api.html#prebuild)
##### prebuildify[#](https://nodejs.org/docs/latest/api/n-api.html#prebuildify)
### Usage[#](https://nodejs.org/docs/latest/api/n-api.html#usage)
In order to use the Node-API functions, include the file
```
#include <node_api.h>
copy
```

This will opt into the default `NAPI_VERSION` for the given release of Node.js. In order to ensure compatibility with specific versions of Node-API, the version can be specified explicitly when including the header:
```
#define NAPI_VERSION 3
#include <node_api.h>
copy
```

This restricts the Node-API surface to just the functionality that was available in the specified (and earlier) versions.
Some of the Node-API surface is experimental and requires explicit opt-in:
```
#define NAPI_EXPERIMENTAL
#include <node_api.h>
copy
```

In this case the entire API surface, including any experimental APIs, will be available to the module code.
Occasionally, experimental features are introduced that affect already-released and stable APIs. These features can be disabled by an opt-out:
```
#define NAPI_EXPERIMENTAL
#define NODE_API_EXPERIMENTAL_<FEATURE_NAME>_OPT_OUT
#include <node_api.h>
copy
```

where `<FEATURE_NAME>` is the name of an experimental feature that affects both experimental and stable APIs.
### Node-API version matrix[#](https://nodejs.org/docs/latest/api/n-api.html#node-api-version-matrix)
Up until version 9, Node-API versions were additive and versioned independently from Node.js. This meant that any version was an extension to the previous version in that it had all of the APIs from the previous version with some additions. Each Node.js version only supported a single Node-API version. For example v18.15.0 supports only Node-API version 8. ABI stability was achieved because 8 was a strict superset of all previous versions.
As of version 9, while Node-API versions continue to be versioned independently, an add-on that ran with Node-API version 9 may need code updates to run with Node-API version 10. ABI stability is maintained, however, because Node.js versions that support Node-API versions higher than 8 will support all versions between 8 and the highest version they support and will default to providing the version 8 APIs unless an add-on opts into a higher Node-API version. This approach provides the flexibility of better optimizing existing Node-API functions while maintaining ABI stability. Existing add-ons can continue to run without recompilation using an earlier version of Node-API. If an add-on needs functionality from a newer Node-API version, changes to existing code and recompilation will be needed to use those new functions anyway.
In versions of Node.js that support Node-API version 9 and later, defining `NAPI_VERSION=X` and using the existing add-on initialization macros will bake in the requested Node-API version that will be used at runtime into the add-on. If `NAPI_VERSION` is not set it will default to 8.
This table may not be up to date in older streams, the most up to date information is in the latest API documentation in: [Node-API version matrix](https://nodejs.org/docs/latest/api/n-api.html#node-api-version-matrix)
Node-API version | Supported In
---|---
10 | v22.14.0+, 23.6.0+ and all later versions
9 | v18.17.0+, 20.3.0+, 21.0.0 and all later versions
8 | v12.22.0+, v14.17.0+, v15.12.0+, 16.0.0 and all later versions
7 | v10.23.0+, v12.19.0+, v14.12.0+, 15.0.0 and all later versions
6 | v10.20.0+, v12.17.0+, 14.0.0 and all later versions
5 | v10.17.0+, v12.11.0+, 13.0.0 and all later versions
4 | v10.16.0+, v11.8.0+, 12.0.0 and all later versions
3 | v6.14.2*, 8.11.2+, v9.11.0+*, 10.0.0 and all later versions
2 | v8.10.0+*, v9.3.0+*, 10.0.0 and all later versions
1 | v8.6.0+**, v9.0.0+*, 10.0.0 and all later versions
* Node-API was experimental.
** Node.js 8.0.0 included Node-API as experimental. It was released as Node-API version 1 but continued to evolve until Node.js 8.6.0. The API is different in versions prior to Node.js 8.6.0. We recommend Node-API version 3 or later.
Each API documented for Node-API will have a header named `added in:`, and APIs which are stable will have the additional header `Node-API version:`. APIs are directly usable when using a Node.js version which supports the Node-API version shown in `Node-API version:` or higher. When using a Node.js version that does not support the `Node-API version:` listed or if there is no `Node-API version:` listed, then the API will only be available if `#define NAPI_EXPERIMENTAL` precedes the inclusion of `node_api.h` or `js_native_api.h`. If an API appears not to be available on a version of Node.js which is later than the one shown in `added in:` then this is most likely the reason for the apparent absence.
The Node-APIs associated strictly with accessing ECMAScript features from native code can be found separately in `js_native_api.h` and `js_native_api_types.h`. The APIs defined in these headers are included in `node_api.h` and `node_api_types.h`. The headers are structured in this way in order to allow implementations of Node-API outside of Node.js. For those implementations the Node.js specific APIs may not be applicable.
The Node.js-specific parts of an addon can be separated from the code that exposes the actual functionality to the JavaScript environment so that the latter may be used with multiple implementations of Node-API. In the example below, `addon.c` and `addon.h` refer only to `js_native_api.h`. This ensures that `addon.c` can be reused to compile against either the Node.js implementation of Node-API or any implementation of Node-API outside of Node.js.
`addon_node.c` is a separate file that contains the Node.js specific entry point to the addon and which instantiates the addon by calling into `addon.c` when the addon is loaded into a Node.js environment.
```
// addon.h
#ifndef _ADDON_H_
#define _ADDON_H_
#include <js_native_api.h>
napi_value create_addon(napi_env env);
#endif  // _ADDON_H_
copy
```
```
// addon.c
#include "addon.h"

#define NODE_API_CALL(env, call)                                  \
  do {                                                            \
    napi_status status = (call);                                  \
    if (status != napi_ok) {                                      \
      const napi_extended_error_info* error_info = NULL;          \
      napi_get_last_error_info((env), &error_info);               \
      const char* err_message = error_info->error_message;        \
      bool is_pending;                                            \
      napi_is_exception_pending((env), &is_pending);              \
      /* If an exception is already pending, don't rethrow it */  \
      if (!is_pending) {                                          \
        const char* message = (err_message == NULL)               \
            ? "empty error message"                               \
            : err_message;                                        \
        napi_throw_error((env), NULL, message);                   \
      }                                                           \
      return NULL;                                                \
    }                                                             \
  } while(0)

static napi_value
DoSomethingUseful(napi_env env, napi_callback_info info) {
  // Do something useful.
  return NULL;
}

napi_value create_addon(napi_env env) {
  napi_value result;
  NODE_API_CALL(env, napi_create_object(env, &result));

  napi_value exported_function;
  NODE_API_CALL(env, napi_create_function(env,
                                          "doSomethingUseful",
                                          NAPI_AUTO_LENGTH,
                                          DoSomethingUseful,
                                          NULL,
                                          &exported_function));

  NODE_API_CALL(env, napi_set_named_property(env,
                                             result,
                                             "doSomethingUseful",
                                             exported_function));

  return result;
}
copy
```
```
// addon_node.c
#include <node_api.h>
#include "addon.h"

NAPI_MODULE_INIT(/* napi_env env, napi_value exports */) {
  // This function body is expected to return a `napi_value`.
  // The variables `napi_env env` and `napi_value exports` may be used within
  // the body, as they are provided by the definition of `NAPI_MODULE_INIT()`.
  return create_addon(env);
}
copy
```

### Environment life cycle APIs[#](https://nodejs.org/docs/latest/api/n-api.html#environment-life-cycle-apis)
A Node.js environment corresponds to an ECMAScript Agent. In the main process, an environment is created at startup, and additional environments can be created on separate threads to serve as [worker threads](https://nodejs.org/api/worker_threads.html). When Node.js is embedded in another application, the main thread of the application may also construct and destroy a Node.js environment multiple times during the life cycle of the application process such that each Node.js environment created by the application may, in turn, during its life cycle create and destroy additional environments as worker threads.
From the perspective of a native addon this means that the bindings it provides may be called multiple times, from multiple contexts, and even concurrently from multiple threads.
Native addons may need to allocate global state which they use during their life cycle of an Node.js environment such that the state can be unique to each instance of the addon.
To this end, Node-API provides a way to associate data such that its life cycle is tied to the life cycle of a Node.js environment.
####  `napi_set_instance_data`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-set-instance-data)
Added in: v12.8.0, v10.20.0**N-API Version:** 6
```
napi_status napi_set_instance_data(node_api_basic_env env,
                                   void* data,
                                   napi_finalize finalize_cb,
                                   void* finalize_hint);
copy
```

  * `[in] env`: The environment that the Node-API call is invoked under.
  * `[in] data`: The data item to make available to bindings of this instance.
  * `[in] finalize_cb`: The function to call when the environment is being torn down. The function receives `data` so that it might free it. [`napi_finalize`](https://nodejs.org/docs/latest/api/n-api.html#napi_finalize) provides more details.
  * `[in] finalize_hint`: Optional hint to pass to the finalize callback during collection.


Returns `napi_ok` if the API succeeded.
This API associates `data` with the currently running Node.js environment. `data` can later be retrieved using `napi_get_instance_data()`. Any existing data associated with the currently running Node.js environment which was set by means of a previous call to `napi_set_instance_data()` will be overwritten. If a `finalize_cb` was provided by the previous call, it will not be called.
####  `napi_get_instance_data`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-instance-data)
Added in: v12.8.0, v10.20.0**N-API Version:** 6
```
napi_status napi_get_instance_data(node_api_basic_env env,
                                   void** data);
copy
```

  * `[in] env`: The environment that the Node-API call is invoked under.
  * `[out] data`: The data item that was previously associated with the currently running Node.js environment by a call to `napi_set_instance_data()`.


Returns `napi_ok` if the API succeeded.
This API retrieves data that was previously associated with the currently running Node.js environment via `napi_set_instance_data()`. If no data is set, the call will succeed and `data` will be set to `NULL`.
### Basic Node-API data types[#](https://nodejs.org/docs/latest/api/n-api.html#basic-node-api-data-types)
Node-API exposes the following fundamental data types as abstractions that are consumed by the various APIs. These APIs should be treated as opaque, introspectable only with other Node-API calls.
####  `napi_status`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-status)
Added in: v8.0.0**N-API Version:** 1
Integral status code indicating the success or failure of a Node-API call. Currently, the following status codes are supported.
```
typedef enum {
  napi_ok,
  napi_invalid_arg,
  napi_object_expected,
  napi_string_expected,
  napi_name_expected,
  napi_function_expected,
  napi_number_expected,
  napi_boolean_expected,
  napi_array_expected,
  napi_generic_failure,
  napi_pending_exception,
  napi_cancelled,
  napi_escape_called_twice,
  napi_handle_scope_mismatch,
  napi_callback_scope_mismatch,
  napi_queue_full,
  napi_closing,
  napi_bigint_expected,
  napi_date_expected,
  napi_arraybuffer_expected,
  napi_detachable_arraybuffer_expected,
  napi_would_deadlock,  /* unused */
  napi_no_external_buffers_allowed,
  napi_cannot_run_js
} napi_status;
copy
```

If additional information is required upon an API returning a failed status, it can be obtained by calling `napi_get_last_error_info`.
####  `napi_extended_error_info`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-extended-error-info)
Added in: v8.0.0**N-API Version:** 1
```
typedef struct {
  const char* error_message;
  void* engine_reserved;
  uint32_t engine_error_code;
  napi_status error_code;
} napi_extended_error_info;
copy
```

  * `error_message`: UTF8-encoded string containing a VM-neutral description of the error.
  * `engine_reserved`: Reserved for VM-specific error details. This is currently not implemented for any VM.
  * `engine_error_code`: VM-specific error code. This is currently not implemented for any VM.
  * `error_code`: The Node-API status code that originated with the last error.


See the [Error handling](https://nodejs.org/docs/latest/api/n-api.html#error-handling) section for additional information.
####  `napi_env`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-env)
`napi_env` is used to represent a context that the underlying Node-API implementation can use to persist VM-specific state. This structure is passed to native functions when they're invoked, and it must be passed back when making Node-API calls. Specifically, the same `napi_env` that was passed in when the initial native function was called must be passed to any subsequent nested Node-API calls. Caching the `napi_env` for the purpose of general reuse, and passing the `napi_env` between instances of the same addon running on different [`Worker`](https://nodejs.org/docs/latest/api/worker_threads.html#class-worker) threads is not allowed. The `napi_env` becomes invalid when an instance of a native addon is unloaded. Notification of this event is delivered through the callbacks given to [`napi_add_env_cleanup_hook`](https://nodejs.org/docs/latest/api/n-api.html#napi_add_env_cleanup_hook) and [`napi_set_instance_data`](https://nodejs.org/docs/latest/api/n-api.html#napi_set_instance_data).
####  `node_api_basic_env`[#](https://nodejs.org/docs/latest/api/n-api.html#node-api-basic-env)
Stability: 1 - Experimental
This variant of `napi_env` is passed to synchronous finalizers ([`node_api_basic_finalize`](https://nodejs.org/docs/latest/api/n-api.html#node_api_basic_finalize)). There is a subset of Node-APIs which accept a parameter of type `node_api_basic_env` as their first argument. These APIs do not access the state of the JavaScript engine and are thus safe to call from synchronous finalizers. Passing a parameter of type `napi_env` to these APIs is allowed, however, passing a parameter of type `node_api_basic_env` to APIs that access the JavaScript engine state is not allowed. Attempting to do so without a cast will produce a compiler warning or an error when add-ons are compiled with flags which cause them to emit warnings and/or errors when incorrect pointer types are passed into a function. Calling such APIs from a synchronous finalizer will ultimately result in the termination of the application.
####  `napi_value`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-value)
This is an opaque pointer that is used to represent a JavaScript value.
####  `napi_threadsafe_function`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-threadsafe-function)
Added in: v10.6.0**N-API Version:** 4
This is an opaque pointer that represents a JavaScript function which can be called asynchronously from multiple threads via `napi_call_threadsafe_function()`.
####  `napi_threadsafe_function_release_mode`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-threadsafe-function-release-mode)
Added in: v10.6.0**N-API Version:** 4
A value to be given to `napi_release_threadsafe_function()` to indicate whether the thread-safe function is to be closed immediately (`napi_tsfn_abort`) or merely released (`napi_tsfn_release`) and thus available for subsequent use via `napi_acquire_threadsafe_function()` and `napi_call_threadsafe_function()`.
```
typedef enum {
  napi_tsfn_release,
  napi_tsfn_abort
} napi_threadsafe_function_release_mode;
copy
```

####  `napi_threadsafe_function_call_mode`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-threadsafe-function-call-mode)
Added in: v10.6.0**N-API Version:** 4
A value to be given to `napi_call_threadsafe_function()` to indicate whether the call should block whenever the queue associated with the thread-safe function is full.
```
typedef enum {
  napi_tsfn_nonblocking,
  napi_tsfn_blocking
} napi_threadsafe_function_call_mode;
copy
```

#### Node-API memory management types[#](https://nodejs.org/docs/latest/api/n-api.html#node-api-memory-management-types)
#####  `napi_handle_scope`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-handle-scope)
This is an abstraction used to control and modify the lifetime of objects created within a particular scope. In general, Node-API values are created within the context of a handle scope. When a native method is called from JavaScript, a default handle scope will exist. If the user does not explicitly create a new handle scope, Node-API values will be created in the default handle scope. For any invocations of code outside the execution of a native method (for instance, during a libuv callback invocation), the module is required to create a scope before invoking any functions that can result in the creation of JavaScript values.
