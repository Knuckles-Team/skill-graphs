The invocation of `napi_finalize` callbacks is scheduled after the manually registered cleanup hooks. In order to ensure a proper order of addon finalization during environment shutdown to avoid use-after-free in the `napi_finalize` callback, addons should register a cleanup hook with `napi_add_env_cleanup_hook` and `napi_add_async_cleanup_hook` to manually release the allocated resource in a proper order.
### Module registration[#](https://nodejs.org/docs/latest/api/n-api.html#module-registration)
Node-API modules are registered in a manner similar to other modules except that instead of using the `NODE_MODULE` macro the following is used:
```
NAPI_MODULE(NODE_GYP_MODULE_NAME, Init)
copy
```

The next difference is the signature for the `Init` method. For a Node-API module it is as follows:
```
napi_value Init(napi_env env, napi_value exports);
copy
```

The return value from `Init` is treated as the `exports` object for the module. The `Init` method is passed an empty object via the `exports` parameter as a convenience. If `Init` returns `NULL`, the parameter passed as `exports` is exported by the module. Node-API modules cannot modify the `module` object but can specify anything as the `exports` property of the module.
To add the method `hello` as a function so that it can be called as a method provided by the addon:
```
napi_value Init(napi_env env, napi_value exports) {
  napi_status status;
  napi_property_descriptor desc = {
    "hello",
    NULL,
    Method,
    NULL,
    NULL,
    NULL,
    napi_writable | napi_enumerable | napi_configurable,
    NULL
  };
  status = napi_define_properties(env, exports, 1, &desc);
  if (status != napi_ok) return NULL;
  return exports;
}
copy
```

To set a function to be returned by the `require()` for the addon:
```
napi_value Init(napi_env env, napi_value exports) {
  napi_value method;
  napi_status status;
  status = napi_create_function(env, "exports", NAPI_AUTO_LENGTH, Method, NULL, &method);
  if (status != napi_ok) return NULL;
  return method;
}
copy
```

To define a class so that new instances can be created (often used with [Object wrap](https://nodejs.org/docs/latest/api/n-api.html#object-wrap)):
```
// NOTE: partial example, not all referenced code is included
napi_value Init(napi_env env, napi_value exports) {
  napi_status status;
  napi_property_descriptor properties[] = {
    { "value", NULL, NULL, GetValue, SetValue, NULL, napi_writable | napi_configurable, NULL },
    DECLARE_NAPI_METHOD("plusOne", PlusOne),
    DECLARE_NAPI_METHOD("multiply", Multiply),
  };

  napi_value cons;
  status =
      napi_define_class(env, "MyObject", New, NULL, 3, properties, &cons);
  if (status != napi_ok) return NULL;

  status = napi_create_reference(env, cons, 1, &constructor);
  if (status != napi_ok) return NULL;

  status = napi_set_named_property(env, exports, "MyObject", cons);
  if (status != napi_ok) return NULL;

  return exports;
}
copy
```

You can also use the `NAPI_MODULE_INIT` macro, which acts as a shorthand for `NAPI_MODULE` and defining an `Init` function:
```
NAPI_MODULE_INIT(/* napi_env env, napi_value exports */) {
  napi_value answer;
  napi_status result;

  status = napi_create_int64(env, 42, &answer);
  if (status != napi_ok) return NULL;

  status = napi_set_named_property(env, exports, "answer", answer);
  if (status != napi_ok) return NULL;

  return exports;
}
copy
```

The parameters `env` and `exports` are provided to the body of the `NAPI_MODULE_INIT` macro.
All Node-API addons are context-aware, meaning they may be loaded multiple times. There are a few design considerations when declaring such a module. The documentation on [context-aware addons](https://nodejs.org/docs/latest/api/addons.html#context-aware-addons) provides more details.
The variables `env` and `exports` will be available inside the function body following the macro invocation.
For more details on setting properties on objects, see the section on [Working with JavaScript properties](https://nodejs.org/docs/latest/api/n-api.html#working-with-javascript-properties).
For more details on building addon modules in general, refer to the existing API.
### Working with JavaScript values[#](https://nodejs.org/docs/latest/api/n-api.html#working-with-javascript-values)
Node-API exposes a set of APIs to create all types of JavaScript values. Some of these types are documented under
Fundamentally, these APIs are used to do one of the following:
  1. Create a new JavaScript object
  2. Convert from a primitive C type to a Node-API value
  3. Convert from Node-API value to a primitive C type
  4. Get global instances including `undefined` and `null`


Node-API values are represented by the type `napi_value`. Any Node-API call that requires a JavaScript value takes in a `napi_value`. In some cases, the API does check the type of the `napi_value` up-front. However, for better performance, it's better for the caller to make sure that the `napi_value` in question is of the JavaScript type expected by the API.
#### Enum types[#](https://nodejs.org/docs/latest/api/n-api.html#enum-types)
#####  `napi_key_collection_mode`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-key-collection-mode)
Added in: v13.7.0, v12.17.0, v10.20.0**N-API Version:** 6
```
typedef enum {
  napi_key_include_prototypes,
  napi_key_own_only
} napi_key_collection_mode;
copy
```

Describes the `Keys/Properties` filter enums:
`napi_key_collection_mode` limits the range of collected properties.
`napi_key_own_only` limits the collected properties to the given object only. `napi_key_include_prototypes` will include all keys of the objects's prototype chain as well.
#####  `napi_key_filter`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-key-filter)
Added in: v13.7.0, v12.17.0, v10.20.0**N-API Version:** 6
```
typedef enum {
  napi_key_all_properties = 0,
  napi_key_writable = 1,
  napi_key_enumerable = 1 << 1,
  napi_key_configurable = 1 << 2,
  napi_key_skip_strings = 1 << 3,
  napi_key_skip_symbols = 1 << 4
} napi_key_filter;
copy
```

Property filter bit flag. This works with bit operators to build a composite filter.
#####  `napi_key_conversion`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-key-conversion)
Added in: v13.7.0, v12.17.0, v10.20.0**N-API Version:** 6
```
typedef enum {
  napi_key_keep_numbers,
  napi_key_numbers_to_strings
} napi_key_conversion;
copy
```

`napi_key_numbers_to_strings` will convert integer indexes to strings. `napi_key_keep_numbers` will return numbers for integer indexes.
#####  `napi_valuetype`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-valuetype)
```
typedef enum {
  // ES6 types (corresponds to typeof)
  napi_undefined,
  napi_null,
  napi_boolean,
  napi_number,
  napi_string,
  napi_symbol,
  napi_object,
  napi_function,
  napi_external,
  napi_bigint,
} napi_valuetype;
copy
```

Describes the type of a `napi_value`. This generally corresponds to the types described in `napi_valuetype` can also represent `Function`s and `Object`s with external data.
A JavaScript value of type `napi_external` appears in JavaScript as a plain object such that no properties can be set on it, and no prototype.
#####  `napi_typedarray_type`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-typedarray-type)
History Version | Changes
---|---
v25.4.0 | Added `napi_float16_array` for Float16Array support.
```
typedef enum {
  napi_int8_array,
  napi_uint8_array,
  napi_uint8_clamped_array,
  napi_int16_array,
  napi_uint16_array,
  napi_int32_array,
  napi_uint32_array,
  napi_float32_array,
  napi_float64_array,
  napi_bigint64_array,
  napi_biguint64_array,
  napi_float16_array,
} napi_typedarray_type;
copy
```

This represents the underlying binary scalar datatype of the `TypedArray`. Elements of this enum correspond to
#### Object creation functions[#](https://nodejs.org/docs/latest/api/n-api.html#object-creation-functions)
#####  `napi_create_array`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-array)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_create_array(napi_env env, napi_value* result)
copy
```

  * `[in] env`: The environment that the Node-API call is invoked under.
  * `[out] result`: A `napi_value` representing a JavaScript `Array`.


Returns `napi_ok` if the API succeeded.
This API returns a Node-API value corresponding to a JavaScript `Array` type. JavaScript arrays are described in
#####  `napi_create_array_with_length`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-array-with-length)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_create_array_with_length(napi_env env,
                                          size_t length,
                                          napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] length`: The initial length of the `Array`.
  * `[out] result`: A `napi_value` representing a JavaScript `Array`.


Returns `napi_ok` if the API succeeded.
This API returns a Node-API value corresponding to a JavaScript `Array` type. The `Array`'s length property is set to the passed-in length parameter. However, the underlying buffer is not guaranteed to be pre-allocated by the VM when the array is created. That behavior is left to the underlying VM implementation. If the buffer must be a contiguous block of memory that can be directly read and/or written via C, consider using [`napi_create_external_arraybuffer`](https://nodejs.org/docs/latest/api/n-api.html#napi_create_external_arraybuffer).
JavaScript arrays are described in
#####  `napi_create_arraybuffer`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-arraybuffer)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_create_arraybuffer(napi_env env,
                                    size_t byte_length,
                                    void** data,
                                    napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] length`: The length in bytes of the array buffer to create.
  * `[out] data`: Pointer to the underlying byte buffer of the `ArrayBuffer`. `data` can optionally be ignored by passing `NULL`.
  * `[out] result`: A `napi_value` representing a JavaScript `ArrayBuffer`.


Returns `napi_ok` if the API succeeded.
This API returns a Node-API value corresponding to a JavaScript `ArrayBuffer`. `ArrayBuffer`s are used to represent fixed-length binary data buffers. They are normally used as a backing-buffer for `TypedArray` objects. The `ArrayBuffer` allocated will have an underlying byte buffer whose size is determined by the `length` parameter that's passed in. The underlying buffer is optionally returned back to the caller in case the caller wants to directly manipulate the buffer. This buffer can only be written to directly from native code. To write to this buffer from JavaScript, a typed array or `DataView` object would need to be created.
JavaScript `ArrayBuffer` objects are described in
#####  `napi_create_buffer`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-buffer)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_create_buffer(napi_env env,
                               size_t size,
                               void** data,
                               napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] size`: Size in bytes of the underlying buffer.
  * `[out] data`: Raw pointer to the underlying buffer. `data` can optionally be ignored by passing `NULL`.
  * `[out] result`: A `napi_value` representing a `node::Buffer`.


Returns `napi_ok` if the API succeeded.
This API allocates a `node::Buffer` object. While this is still a fully-supported data structure, in most cases using a `TypedArray` will suffice.
#####  `napi_create_buffer_copy`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-buffer-copy)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_create_buffer_copy(napi_env env,
                                    size_t length,
                                    const void* data,
                                    void** result_data,
                                    napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] size`: Size in bytes of the input buffer (should be the same as the size of the new buffer).
  * `[in] data`: Raw pointer to the underlying buffer to copy from.
  * `[out] result_data`: Pointer to the new `Buffer`'s underlying data buffer. `result_data` can optionally be ignored by passing `NULL`.
  * `[out] result`: A `napi_value` representing a `node::Buffer`.


Returns `napi_ok` if the API succeeded.
This API allocates a `node::Buffer` object and initializes it with data copied from the passed-in buffer. While this is still a fully-supported data structure, in most cases using a `TypedArray` will suffice.
#####  `napi_create_date`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-date)
Added in: v11.11.0, v10.17.0**N-API Version:** 5
```
napi_status napi_create_date(napi_env env,
                             double time,
                             napi_value* result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] time`: ECMAScript time value in milliseconds since 01 January, 1970 UTC.
  * `[out] result`: A `napi_value` representing a JavaScript `Date`.


Returns `napi_ok` if the API succeeded.
This API does not observe leap seconds; they are ignored, as ECMAScript aligns with POSIX time specification.
This API allocates a JavaScript `Date` object.
JavaScript `Date` objects are described in
#####  `napi_create_external`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-external)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_create_external(napi_env env,
                                 void* data,
                                 napi_finalize finalize_cb,
                                 void* finalize_hint,
                                 napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] data`: Raw pointer to the external data.
  * `[in] finalize_cb`: Optional callback to call when the external value is being collected. [`napi_finalize`](https://nodejs.org/docs/latest/api/n-api.html#napi_finalize) provides more details.
  * `[in] finalize_hint`: Optional hint to pass to the finalize callback during collection.
  * `[out] result`: A `napi_value` representing an external value.


Returns `napi_ok` if the API succeeded.
This API allocates a JavaScript value with external data attached to it. This is used to pass external data through JavaScript code, so it can be retrieved later by native code using [`napi_get_value_external`](https://nodejs.org/docs/latest/api/n-api.html#napi_get_value_external).
The API adds a `napi_finalize` callback which will be called when the JavaScript object just created has been garbage collected.
The created value is not an object, and therefore does not support additional properties. It is considered a distinct value type: calling `napi_typeof()` with an external value yields `napi_external`.
#####  `napi_create_external_arraybuffer`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-external-arraybuffer)
Added in: v8.0.0**N-API Version:** 1
```
napi_status
napi_create_external_arraybuffer(napi_env env,
                                 void* external_data,
                                 size_t byte_length,
                                 napi_finalize finalize_cb,
                                 void* finalize_hint,
                                 napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] external_data`: Pointer to the underlying byte buffer of the `ArrayBuffer`.
  * `[in] byte_length`: The length in bytes of the underlying buffer.
  * `[in] finalize_cb`: Optional callback to call when the `ArrayBuffer` is being collected. [`napi_finalize`](https://nodejs.org/docs/latest/api/n-api.html#napi_finalize) provides more details.
  * `[in] finalize_hint`: Optional hint to pass to the finalize callback during collection.
  * `[out] result`: A `napi_value` representing a JavaScript `ArrayBuffer`.


Returns `napi_ok` if the API succeeded.
**Some runtimes other than Node.js have dropped support for external buffers**. On runtimes other than Node.js this method may return `napi_no_external_buffers_allowed` to indicate that external buffers are not supported. One such runtime is Electron as described in this issue
In order to maintain broadest compatibility with all runtimes you may define `NODE_API_NO_EXTERNAL_BUFFERS_ALLOWED` in your addon before includes for the node-api headers. Doing so will hide the 2 functions that create external buffers. This will ensure a compilation error occurs if you accidentally use one of these methods.
This API returns a Node-API value corresponding to a JavaScript `ArrayBuffer`. The underlying byte buffer of the `ArrayBuffer` is externally allocated and managed. The caller must ensure that the byte buffer remains valid until the finalize callback is called.
The API adds a `napi_finalize` callback which will be called when the JavaScript object just created has been garbage collected.
JavaScript `ArrayBuffer`s are described in
#####  `napi_create_external_buffer`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-external-buffer)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_create_external_buffer(napi_env env,
                                        size_t length,
                                        void* data,
                                        napi_finalize finalize_cb,
                                        void* finalize_hint,
                                        napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] length`: Size in bytes of the input buffer (should be the same as the size of the new buffer).
  * `[in] data`: Raw pointer to the underlying buffer to expose to JavaScript.
  * `[in] finalize_cb`: Optional callback to call when the `ArrayBuffer` is being collected. [`napi_finalize`](https://nodejs.org/docs/latest/api/n-api.html#napi_finalize) provides more details.
  * `[in] finalize_hint`: Optional hint to pass to the finalize callback during collection.
  * `[out] result`: A `napi_value` representing a `node::Buffer`.


Returns `napi_ok` if the API succeeded.
**Some runtimes other than Node.js have dropped support for external buffers**. On runtimes other than Node.js this method may return `napi_no_external_buffers_allowed` to indicate that external buffers are not supported. One such runtime is Electron as described in this issue
In order to maintain broadest compatibility with all runtimes you may define `NODE_API_NO_EXTERNAL_BUFFERS_ALLOWED` in your addon before includes for the node-api headers. Doing so will hide the 2 functions that create external buffers. This will ensure a compilation error occurs if you accidentally use one of these methods.
This API allocates a `node::Buffer` object and initializes it with data backed by the passed in buffer. While this is still a fully-supported data structure, in most cases using a `TypedArray` will suffice.
The API adds a `napi_finalize` callback which will be called when the JavaScript object just created has been garbage collected.
For Node.js >=4 `Buffers` are `Uint8Array`s.
#####  `napi_create_object`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-object)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_create_object(napi_env env, napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[out] result`: A `napi_value` representing a JavaScript `Object`.


Returns `napi_ok` if the API succeeded.
This API allocates a default JavaScript `Object`. It is the equivalent of doing `new Object()` in JavaScript.
The JavaScript `Object` type is described in
#####  `node_api_create_object_with_properties`[#](https://nodejs.org/docs/latest/api/n-api.html#node-api-create-object-with-properties)
Added in: v25.2.0
Stability: 1 - Experimental
```
napi_status node_api_create_object_with_properties(napi_env env,
                                                   napi_value prototype_or_null,
                                                   const napi_value* property_names,
                                                   const napi_value* property_values,
                                                   size_t property_count,
                                                   napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] prototype_or_null`: The prototype object for the new object. Can be a `napi_value` representing a JavaScript object to use as the prototype, a `napi_value` representing JavaScript `null`, or a `nullptr` that will be converted to `null`.
  * `[in] property_names`: Array of `napi_value` representing the property names.
  * `[in] property_values`: Array of `napi_value` representing the property values.
  * `[in] property_count`: Number of properties in the arrays.
  * `[out] result`: A `napi_value` representing a JavaScript `Object`.


Returns `napi_ok` if the API succeeded.
This API creates a JavaScript `Object` with the specified prototype and properties. This is more efficient than calling `napi_create_object` followed by multiple `napi_set_property` calls, as it can create the object with all properties atomically, avoiding potential V8 map transitions.
The arrays `property_names` and `property_values` must have the same length specified by `property_count`. The properties are added to the object in the order they appear in the arrays.
#####  `napi_create_symbol`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-symbol)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_create_symbol(napi_env env,
                               napi_value description,
                               napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] description`: Optional `napi_value` which refers to a JavaScript `string` to be set as the description for the symbol.
  * `[out] result`: A `napi_value` representing a JavaScript `symbol`.


Returns `napi_ok` if the API succeeded.
This API creates a JavaScript `symbol` value from a UTF8-encoded C string.
The JavaScript `symbol` type is described in
#####  `node_api_symbol_for`[#](https://nodejs.org/docs/latest/api/n-api.html#node-api-symbol-for)
Added in: v17.5.0, v16.15.0**N-API Version:** 9
```
napi_status node_api_symbol_for(napi_env env,
                                const char* utf8description,
                                size_t length,
                                napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] utf8description`: UTF-8 C string representing the text to be used as the description for the symbol.
  * `[in] length`: The length of the description string in bytes, or `NAPI_AUTO_LENGTH` if it is null-terminated.
  * `[out] result`: A `napi_value` representing a JavaScript `symbol`.


Returns `napi_ok` if the API succeeded.
This API searches in the global registry for an existing symbol with the given description. If the symbol already exists it will be returned, otherwise a new symbol will be created in the registry.
The JavaScript `symbol` type is described in
#####  `napi_create_typedarray`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-typedarray)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_create_typedarray(napi_env env,
                                   napi_typedarray_type type,
                                   size_t length,
                                   napi_value arraybuffer,
                                   size_t byte_offset,
                                   napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] type`: Scalar datatype of the elements within the `TypedArray`.
  * `[in] length`: Number of elements in the `TypedArray`.
  * `[in] arraybuffer`: `ArrayBuffer` underlying the typed array.
  * `[in] byte_offset`: The byte offset within the `ArrayBuffer` from which to start projecting the `TypedArray`.
  * `[out] result`: A `napi_value` representing a JavaScript `TypedArray`.


Returns `napi_ok` if the API succeeded.
This API creates a JavaScript `TypedArray` object over an existing `ArrayBuffer`. `TypedArray` objects provide an array-like view over an underlying data buffer where each element has the same underlying binary scalar datatype.
It's required that `(length * size_of_element) + byte_offset` should be <= the size in bytes of the array passed in. If not, a `RangeError` exception is raised.
JavaScript `TypedArray` objects are described in
#####  `node_api_create_buffer_from_arraybuffer`[#](https://nodejs.org/docs/latest/api/n-api.html#node-api-create-buffer-from-arraybuffer)
Added in: v23.0.0, v22.12.0**N-API Version:** 10
```
napi_status NAPI_CDECL node_api_create_buffer_from_arraybuffer(napi_env env,
                                                              napi_value arraybuffer,
                                                              size_t byte_offset,
                                                              size_t byte_length,
                                                              napi_value* result)
