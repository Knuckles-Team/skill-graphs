copy
```

  * **`[in] env`**: The environment that the API is invoked under.
  * **`[in] arraybuffer`**: The`ArrayBuffer` from which the buffer will be created.
  * **`[in] byte_offset`**: The byte offset within the`ArrayBuffer` from which to start creating the buffer.
  * **`[in] byte_length`**: The length in bytes of the buffer to be created from the`ArrayBuffer`.
  * **`[out] result`**: A`napi_value` representing the created JavaScript `Buffer` object.


Returns `napi_ok` if the API succeeded.
This API creates a JavaScript `Buffer` object from an existing `ArrayBuffer`. The `Buffer` object is a Node.js-specific class that provides a way to work with binary data directly in JavaScript.
The byte range `[byte_offset, byte_offset + byte_length)` must be within the bounds of the `ArrayBuffer`. If `byte_offset + byte_length` exceeds the size of the `ArrayBuffer`, a `RangeError` exception is raised.
#####  `napi_create_dataview`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-dataview)
Added in: v8.3.0**N-API Version:** 1History Version | Changes
---|---
v25.4.0 | Added support for `SharedArrayBuffer`.
```
napi_status napi_create_dataview(napi_env env,
                                 size_t byte_length,
                                 napi_value arraybuffer,
                                 size_t byte_offset,
                                 napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] length`: Number of elements in the `DataView`.
  * `[in] arraybuffer`: `ArrayBuffer` or `SharedArrayBuffer` underlying the `DataView`.
  * `[in] byte_offset`: The byte offset within the `ArrayBuffer` from which to start projecting the `DataView`.
  * `[out] result`: A `napi_value` representing a JavaScript `DataView`.


Returns `napi_ok` if the API succeeded.
This API creates a JavaScript `DataView` object over an existing `ArrayBuffer` or `SharedArrayBuffer`. `DataView` objects provide an array-like view over an underlying data buffer, but one which allows items of different size and type in the `ArrayBuffer` or `SharedArrayBuffer`.
It is required that `byte_length + byte_offset` is less than or equal to the size in bytes of the array passed in. If not, a `RangeError` exception is raised.
JavaScript `DataView` objects are described in
#### Functions to convert from C types to Node-API[#](https://nodejs.org/docs/latest/api/n-api.html#functions-to-convert-from-c-types-to-node-api)
#####  `napi_create_int32`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-int32)
Added in: v8.4.0**N-API Version:** 1
```
napi_status napi_create_int32(napi_env env, int32_t value, napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: Integer value to be represented in JavaScript.
  * `[out] result`: A `napi_value` representing a JavaScript `number`.


Returns `napi_ok` if the API succeeded.
This API is used to convert from the C `int32_t` type to the JavaScript `number` type.
The JavaScript `number` type is described in
#####  `napi_create_uint32`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-uint32)
Added in: v8.4.0**N-API Version:** 1
```
napi_status napi_create_uint32(napi_env env, uint32_t value, napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: Unsigned integer value to be represented in JavaScript.
  * `[out] result`: A `napi_value` representing a JavaScript `number`.


Returns `napi_ok` if the API succeeded.
This API is used to convert from the C `uint32_t` type to the JavaScript `number` type.
The JavaScript `number` type is described in
#####  `napi_create_int64`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-int64)
Added in: v8.4.0**N-API Version:** 1
```
napi_status napi_create_int64(napi_env env, int64_t value, napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: Integer value to be represented in JavaScript.
  * `[out] result`: A `napi_value` representing a JavaScript `number`.


Returns `napi_ok` if the API succeeded.
This API is used to convert from the C `int64_t` type to the JavaScript `number` type.
The JavaScript `number` type is described in `int64_t` cannot be represented with full precision in JavaScript. Integer values outside the range of `-(2**53 - 1)` - `(2**53 - 1)` will lose precision.
#####  `napi_create_double`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-double)
Added in: v8.4.0**N-API Version:** 1
```
napi_status napi_create_double(napi_env env, double value, napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: Double-precision value to be represented in JavaScript.
  * `[out] result`: A `napi_value` representing a JavaScript `number`.


Returns `napi_ok` if the API succeeded.
This API is used to convert from the C `double` type to the JavaScript `number` type.
The JavaScript `number` type is described in
#####  `napi_create_bigint_int64`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-bigint-int64)
Added in: v10.7.0**N-API Version:** 6
```
napi_status napi_create_bigint_int64(napi_env env,
                                     int64_t value,
                                     napi_value* result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: Integer value to be represented in JavaScript.
  * `[out] result`: A `napi_value` representing a JavaScript `BigInt`.


Returns `napi_ok` if the API succeeded.
This API converts the C `int64_t` type to the JavaScript `BigInt` type.
#####  `napi_create_bigint_uint64`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-bigint-uint64)
Added in: v10.7.0**N-API Version:** 6
```
napi_status napi_create_bigint_uint64(napi_env env,
                                      uint64_t value,
                                      napi_value* result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: Unsigned integer value to be represented in JavaScript.
  * `[out] result`: A `napi_value` representing a JavaScript `BigInt`.


Returns `napi_ok` if the API succeeded.
This API converts the C `uint64_t` type to the JavaScript `BigInt` type.
#####  `napi_create_bigint_words`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-bigint-words)
Added in: v10.7.0**N-API Version:** 6
```
napi_status napi_create_bigint_words(napi_env env,
                                     int sign_bit,
                                     size_t word_count,
                                     const uint64_t* words,
                                     napi_value* result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] sign_bit`: Determines if the resulting `BigInt` will be positive or negative.
  * `[in] word_count`: The length of the `words` array.
  * `[in] words`: An array of `uint64_t` little-endian 64-bit words.
  * `[out] result`: A `napi_value` representing a JavaScript `BigInt`.


Returns `napi_ok` if the API succeeded.
This API converts an array of unsigned 64-bit words into a single `BigInt` value.
The resulting `BigInt` is calculated as: (–1)`sign_bit` (`words[0]` × (264)0 + `words[1]` × (264)1 + …)
#####  `napi_create_string_latin1`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-string-latin1)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_create_string_latin1(napi_env env,
                                      const char* str,
                                      size_t length,
                                      napi_value* result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] str`: Character buffer representing an ISO-8859-1-encoded string.
  * `[in] length`: The length of the string in bytes, or `NAPI_AUTO_LENGTH` if it is null-terminated.
  * `[out] result`: A `napi_value` representing a JavaScript `string`.


Returns `napi_ok` if the API succeeded.
This API creates a JavaScript `string` value from an ISO-8859-1-encoded C string. The native string is copied.
The JavaScript `string` type is described in
#####  `node_api_create_external_string_latin1`[#](https://nodejs.org/docs/latest/api/n-api.html#node-api-create-external-string-latin1)
Added in: v20.4.0, v18.18.0**N-API Version:** 10
```
napi_status
node_api_create_external_string_latin1(napi_env env,
                                       char* str,
                                       size_t length,
                                       napi_finalize finalize_callback,
                                       void* finalize_hint,
                                       napi_value* result,
                                       bool* copied);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] str`: Character buffer representing an ISO-8859-1-encoded string.
  * `[in] length`: The length of the string in bytes, or `NAPI_AUTO_LENGTH` if it is null-terminated.
  * `[in] finalize_callback`: The function to call when the string is being collected. The function will be called with the following parameters:
    * `[in] env`: The environment in which the add-on is running. This value may be null if the string is being collected as part of the termination of the worker or the main Node.js instance.
    * `[in] data`: This is the value `str` as a `void*` pointer.
    * `[in] finalize_hint`: This is the value `finalize_hint` that was given to the API. [`napi_finalize`](https://nodejs.org/docs/latest/api/n-api.html#napi_finalize) provides more details. This parameter is optional. Passing a null value means that the add-on doesn't need to be notified when the corresponding JavaScript string is collected.
  * `[in] finalize_hint`: Optional hint to pass to the finalize callback during collection.
  * `[out] result`: A `napi_value` representing a JavaScript `string`.
  * `[out] copied`: Whether the string was copied. If it was, the finalizer will already have been invoked to destroy `str`.


Returns `napi_ok` if the API succeeded.
This API creates a JavaScript `string` value from an ISO-8859-1-encoded C string. The native string may not be copied and must thus exist for the entire life cycle of the JavaScript value.
The JavaScript `string` type is described in
#####  `napi_create_string_utf16`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-string-utf16)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_create_string_utf16(napi_env env,
                                     const char16_t* str,
                                     size_t length,
                                     napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] str`: Character buffer representing a UTF16-LE-encoded string.
  * `[in] length`: The length of the string in two-byte code units, or `NAPI_AUTO_LENGTH` if it is null-terminated.
  * `[out] result`: A `napi_value` representing a JavaScript `string`.


Returns `napi_ok` if the API succeeded.
This API creates a JavaScript `string` value from a UTF16-LE-encoded C string. The native string is copied.
The JavaScript `string` type is described in
#####  `node_api_create_external_string_utf16`[#](https://nodejs.org/docs/latest/api/n-api.html#node-api-create-external-string-utf16)
Added in: v20.4.0, v18.18.0**N-API Version:** 10
```
napi_status
node_api_create_external_string_utf16(napi_env env,
                                      char16_t* str,
                                      size_t length,
                                      napi_finalize finalize_callback,
                                      void* finalize_hint,
                                      napi_value* result,
                                      bool* copied);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] str`: Character buffer representing a UTF16-LE-encoded string.
  * `[in] length`: The length of the string in two-byte code units, or `NAPI_AUTO_LENGTH` if it is null-terminated.
  * `[in] finalize_callback`: The function to call when the string is being collected. The function will be called with the following parameters:
    * `[in] env`: The environment in which the add-on is running. This value may be null if the string is being collected as part of the termination of the worker or the main Node.js instance.
    * `[in] data`: This is the value `str` as a `void*` pointer.
    * `[in] finalize_hint`: This is the value `finalize_hint` that was given to the API. [`napi_finalize`](https://nodejs.org/docs/latest/api/n-api.html#napi_finalize) provides more details. This parameter is optional. Passing a null value means that the add-on doesn't need to be notified when the corresponding JavaScript string is collected.
  * `[in] finalize_hint`: Optional hint to pass to the finalize callback during collection.
  * `[out] result`: A `napi_value` representing a JavaScript `string`.
  * `[out] copied`: Whether the string was copied. If it was, the finalizer will already have been invoked to destroy `str`.


Returns `napi_ok` if the API succeeded.
This API creates a JavaScript `string` value from a UTF16-LE-encoded C string. The native string may not be copied and must thus exist for the entire life cycle of the JavaScript value.
The JavaScript `string` type is described in
#####  `napi_create_string_utf8`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-string-utf8)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_create_string_utf8(napi_env env,
                                    const char* str,
                                    size_t length,
                                    napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] str`: Character buffer representing a UTF8-encoded string.
  * `[in] length`: The length of the string in bytes, or `NAPI_AUTO_LENGTH` if it is null-terminated.
  * `[out] result`: A `napi_value` representing a JavaScript `string`.


Returns `napi_ok` if the API succeeded.
This API creates a JavaScript `string` value from a UTF8-encoded C string. The native string is copied.
The JavaScript `string` type is described in
#### Functions to create optimized property keys[#](https://nodejs.org/docs/latest/api/n-api.html#functions-to-create-optimized-property-keys)
Many JavaScript engines including V8 use internalized strings as keys to set and get property values. They typically use a hash table to create and lookup such strings. While it adds some cost per key creation, it improves the performance after that by enabling comparison of string pointers instead of the whole strings.
If a new JavaScript string is intended to be used as a property key, then for some JavaScript engines it will be more efficient to use the functions in this section. Otherwise, use the `napi_create_string_utf8` or `node_api_create_external_string_utf8` series functions as there may be additional overhead in creating/storing strings with the property key creation methods.
#####  `node_api_create_property_key_latin1`[#](https://nodejs.org/docs/latest/api/n-api.html#node-api-create-property-key-latin1)
Added in: v22.9.0, v20.18.0**N-API Version:** 10
```
napi_status NAPI_CDECL node_api_create_property_key_latin1(napi_env env,
                                                           const char* str,
                                                           size_t length,
                                                           napi_value* result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] str`: Character buffer representing an ISO-8859-1-encoded string.
  * `[in] length`: The length of the string in bytes, or `NAPI_AUTO_LENGTH` if it is null-terminated.
  * `[out] result`: A `napi_value` representing an optimized JavaScript `string` to be used as a property key for objects.


Returns `napi_ok` if the API succeeded.
This API creates an optimized JavaScript `string` value from an ISO-8859-1-encoded C string to be used as a property key for objects. The native string is copied. In contrast with `napi_create_string_latin1`, subsequent calls to this function with the same `str` pointer may benefit from a speedup in the creation of the requested `napi_value`, depending on the engine.
The JavaScript `string` type is described in
#####  `node_api_create_property_key_utf16`[#](https://nodejs.org/docs/latest/api/n-api.html#node-api-create-property-key-utf16)
Added in: v21.7.0, v20.12.0**N-API Version:** 10
```
napi_status NAPI_CDECL node_api_create_property_key_utf16(napi_env env,
                                                          const char16_t* str,
                                                          size_t length,
                                                          napi_value* result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] str`: Character buffer representing a UTF16-LE-encoded string.
  * `[in] length`: The length of the string in two-byte code units, or `NAPI_AUTO_LENGTH` if it is null-terminated.
  * `[out] result`: A `napi_value` representing an optimized JavaScript `string` to be used as a property key for objects.


Returns `napi_ok` if the API succeeded.
This API creates an optimized JavaScript `string` value from a UTF16-LE-encoded C string to be used as a property key for objects. The native string is copied.
The JavaScript `string` type is described in
#####  `node_api_create_property_key_utf8`[#](https://nodejs.org/docs/latest/api/n-api.html#node-api-create-property-key-utf8)
Added in: v22.9.0, v20.18.0**N-API Version:** 10
```
napi_status NAPI_CDECL node_api_create_property_key_utf8(napi_env env,
                                                         const char* str,
                                                         size_t length,
                                                         napi_value* result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] str`: Character buffer representing a UTF8-encoded string.
  * `[in] length`: The length of the string in two-byte code units, or `NAPI_AUTO_LENGTH` if it is null-terminated.
  * `[out] result`: A `napi_value` representing an optimized JavaScript `string` to be used as a property key for objects.


Returns `napi_ok` if the API succeeded.
This API creates an optimized JavaScript `string` value from a UTF8-encoded C string to be used as a property key for objects. The native string is copied.
The JavaScript `string` type is described in
#### Functions to convert from Node-API to C types[#](https://nodejs.org/docs/latest/api/n-api.html#functions-to-convert-from-node-api-to-c-types)
#####  `napi_get_array_length`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-array-length)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_get_array_length(napi_env env,
                                  napi_value value,
                                  uint32_t* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: `napi_value` representing the JavaScript `Array` whose length is being queried.
  * `[out] result`: `uint32` representing length of the array.


Returns `napi_ok` if the API succeeded.
This API returns the length of an array.
`Array` length is described in
#####  `napi_get_arraybuffer_info`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-arraybuffer-info)
Added in: v8.0.0**N-API Version:** 1History Version | Changes
---|---
v24.9.0 | Added support for `SharedArrayBuffer`.
```
napi_status napi_get_arraybuffer_info(napi_env env,
                                      napi_value arraybuffer,
                                      void** data,
                                      size_t* byte_length)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] arraybuffer`: `napi_value` representing the `ArrayBuffer` or `SharedArrayBuffer` being queried.
  * `[out] data`: The underlying data buffer of the `ArrayBuffer` or `SharedArrayBuffer` is `0`, this may be `NULL` or any other pointer value.
  * `[out] byte_length`: Length in bytes of the underlying data buffer.


Returns `napi_ok` if the API succeeded.
This API is used to retrieve the underlying data buffer of an `ArrayBuffer` or `SharedArrayBuffer` and its length.
_WARNING_ : Use caution while using this API. The lifetime of the underlying data buffer is managed by the `ArrayBuffer` or `SharedArrayBuffer` even after it's returned. A possible safe way to use this API is in conjunction with [`napi_create_reference`](https://nodejs.org/docs/latest/api/n-api.html#napi_create_reference), which can be used to guarantee control over the lifetime of the `ArrayBuffer` or `SharedArrayBuffer`. It's also safe to use the returned data buffer within the same callback as long as there are no calls to other APIs that might trigger a GC.
#####  `napi_get_buffer_info`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-buffer-info)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_get_buffer_info(napi_env env,
                                 napi_value value,
                                 void** data,
                                 size_t* length)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: `napi_value` representing the `node::Buffer` or `Uint8Array` being queried.
  * `[out] data`: The underlying data buffer of the `node::Buffer` or `Uint8Array`. If length is `0`, this may be `NULL` or any other pointer value.
  * `[out] length`: Length in bytes of the underlying data buffer.


Returns `napi_ok` if the API succeeded.
This method returns the identical `data` and `byte_length` as [`napi_get_typedarray_info`](https://nodejs.org/docs/latest/api/n-api.html#napi_get_typedarray_info). And `napi_get_typedarray_info` accepts a `node::Buffer` (a Uint8Array) as the value too.
This API is used to retrieve the underlying data buffer of a `node::Buffer` and its length.
_Warning_ : Use caution while using this API since the underlying data buffer's lifetime is not guaranteed if it's managed by the VM.
#####  `napi_get_prototype`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-prototype)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_get_prototype(napi_env env,
                               napi_value object,
                               napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] object`: `napi_value` representing JavaScript `Object` whose prototype to return. This returns the equivalent of `Object.getPrototypeOf` (which is not the same as the function's `prototype` property).
  * `[out] result`: `napi_value` representing prototype of the given object.


Returns `napi_ok` if the API succeeded.
#####  `napi_get_typedarray_info`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-typedarray-info)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_get_typedarray_info(napi_env env,
                                     napi_value typedarray,
                                     napi_typedarray_type* type,
                                     size_t* length,
                                     void** data,
                                     napi_value* arraybuffer,
                                     size_t* byte_offset)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] typedarray`: `napi_value` representing the `TypedArray` whose properties to query.
  * `[out] type`: Scalar datatype of the elements within the `TypedArray`.
  * `[out] length`: The number of elements in the `TypedArray`.
  * `[out] data`: The data buffer underlying the `TypedArray` adjusted by the `byte_offset` value so that it points to the first element in the `TypedArray`. If the length of the array is `0`, this may be `NULL` or any other pointer value.
  * `[out] arraybuffer`: The `ArrayBuffer` underlying the `TypedArray`.
  * `[out] byte_offset`: The byte offset within the underlying native array at which the first element of the arrays is located. The value for the data parameter has already been adjusted so that data points to the first element in the array. Therefore, the first byte of the native array would be at `data - byte_offset`.


Returns `napi_ok` if the API succeeded.
This API returns various properties of a typed array.
Any of the out parameters may be `NULL` if that property is unneeded.
_Warning_ : Use caution while using this API since the underlying data buffer is managed by the VM.
#####  `napi_get_dataview_info`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-dataview-info)
Added in: v8.3.0**N-API Version:** 1
```
napi_status napi_get_dataview_info(napi_env env,
                                   napi_value dataview,
                                   size_t* byte_length,
                                   void** data,
                                   napi_value* arraybuffer,
                                   size_t* byte_offset)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] dataview`: `napi_value` representing the `DataView` whose properties to query.
  * `[out] byte_length`: Number of bytes in the `DataView`.
  * `[out] data`: The data buffer underlying the `DataView`. If byte_length is `0`, this may be `NULL` or any other pointer value.
