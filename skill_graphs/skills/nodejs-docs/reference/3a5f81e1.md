  * `[out] arraybuffer`: `ArrayBuffer` underlying the `DataView`.
  * `[out] byte_offset`: The byte offset within the data buffer from which to start projecting the `DataView`.


Returns `napi_ok` if the API succeeded.
Any of the out parameters may be `NULL` if that property is unneeded.
This API returns various properties of a `DataView`.
#####  `napi_get_date_value`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-date-value)
Added in: v11.11.0, v10.17.0**N-API Version:** 5
```
napi_status napi_get_date_value(napi_env env,
                                napi_value value,
                                double* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: `napi_value` representing a JavaScript `Date`.
  * `[out] result`: Time value as a `double` represented as milliseconds since midnight at the beginning of 01 January, 1970 UTC.


This API does not observe leap seconds; they are ignored, as ECMAScript aligns with POSIX time specification.
Returns `napi_ok` if the API succeeded. If a non-date `napi_value` is passed in it returns `napi_date_expected`.
This API returns the C double primitive of time value for the given JavaScript `Date`.
#####  `napi_get_value_bool`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-value-bool)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_get_value_bool(napi_env env, napi_value value, bool* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: `napi_value` representing JavaScript `Boolean`.
  * `[out] result`: C boolean primitive equivalent of the given JavaScript `Boolean`.


Returns `napi_ok` if the API succeeded. If a non-boolean `napi_value` is passed in it returns `napi_boolean_expected`.
This API returns the C boolean primitive equivalent of the given JavaScript `Boolean`.
#####  `napi_get_value_double`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-value-double)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_get_value_double(napi_env env,
                                  napi_value value,
                                  double* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: `napi_value` representing JavaScript `number`.
  * `[out] result`: C double primitive equivalent of the given JavaScript `number`.


Returns `napi_ok` if the API succeeded. If a non-number `napi_value` is passed in it returns `napi_number_expected`.
This API returns the C double primitive equivalent of the given JavaScript `number`.
#####  `napi_get_value_bigint_int64`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-value-bigint-int64)
Added in: v10.7.0**N-API Version:** 6
```
napi_status napi_get_value_bigint_int64(napi_env env,
                                        napi_value value,
                                        int64_t* result,
                                        bool* lossless);
copy
```

  * `[in] env`: The environment that the API is invoked under
  * `[in] value`: `napi_value` representing JavaScript `BigInt`.
  * `[out] result`: C `int64_t` primitive equivalent of the given JavaScript `BigInt`.
  * `[out] lossless`: Indicates whether the `BigInt` value was converted losslessly.


Returns `napi_ok` if the API succeeded. If a non-`BigInt` is passed in it returns `napi_bigint_expected`.
This API returns the C `int64_t` primitive equivalent of the given JavaScript `BigInt`. If needed it will truncate the value, setting `lossless` to `false`.
#####  `napi_get_value_bigint_uint64`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-value-bigint-uint64)
Added in: v10.7.0**N-API Version:** 6
```
napi_status napi_get_value_bigint_uint64(napi_env env,
                                        napi_value value,
                                        uint64_t* result,
                                        bool* lossless);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: `napi_value` representing JavaScript `BigInt`.
  * `[out] result`: C `uint64_t` primitive equivalent of the given JavaScript `BigInt`.
  * `[out] lossless`: Indicates whether the `BigInt` value was converted losslessly.


Returns `napi_ok` if the API succeeded. If a non-`BigInt` is passed in it returns `napi_bigint_expected`.
This API returns the C `uint64_t` primitive equivalent of the given JavaScript `BigInt`. If needed it will truncate the value, setting `lossless` to `false`.
#####  `napi_get_value_bigint_words`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-value-bigint-words)
Added in: v10.7.0**N-API Version:** 6
```
napi_status napi_get_value_bigint_words(napi_env env,
                                        napi_value value,
                                        int* sign_bit,
                                        size_t* word_count,
                                        uint64_t* words);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: `napi_value` representing JavaScript `BigInt`.
  * `[out] sign_bit`: Integer representing if the JavaScript `BigInt` is positive or negative.
  * `[in/out] word_count`: Must be initialized to the length of the `words` array. Upon return, it will be set to the actual number of words that would be needed to store this `BigInt`.
  * `[out] words`: Pointer to a pre-allocated 64-bit word array.


Returns `napi_ok` if the API succeeded.
This API converts a single `BigInt` value into a sign bit, 64-bit little-endian array, and the number of elements in the array. `sign_bit` and `words` may be both set to `NULL`, in order to get only `word_count`.
#####  `napi_get_value_external`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-value-external)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_get_value_external(napi_env env,
                                    napi_value value,
                                    void** result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: `napi_value` representing JavaScript external value.
  * `[out] result`: Pointer to the data wrapped by the JavaScript external value.


Returns `napi_ok` if the API succeeded. If a non-external `napi_value` is passed in it returns `napi_invalid_arg`.
This API retrieves the external data pointer that was previously passed to `napi_create_external()`.
#####  `napi_get_value_int32`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-value-int32)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_get_value_int32(napi_env env,
                                 napi_value value,
                                 int32_t* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: `napi_value` representing JavaScript `number`.
  * `[out] result`: C `int32` primitive equivalent of the given JavaScript `number`.


Returns `napi_ok` if the API succeeded. If a non-number `napi_value` is passed in `napi_number_expected`.
This API returns the C `int32` primitive equivalent of the given JavaScript `number`.
If the number exceeds the range of the 32 bit integer, then the result is truncated to the equivalent of the bottom 32 bits. This can result in a large positive number becoming a negative number if the value is > 231 - 1.
Non-finite number values (`NaN`, `+Infinity`, or `-Infinity`) set the result to zero.
#####  `napi_get_value_int64`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-value-int64)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_get_value_int64(napi_env env,
                                 napi_value value,
                                 int64_t* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: `napi_value` representing JavaScript `number`.
  * `[out] result`: C `int64` primitive equivalent of the given JavaScript `number`.


Returns `napi_ok` if the API succeeded. If a non-number `napi_value` is passed in it returns `napi_number_expected`.
This API returns the C `int64` primitive equivalent of the given JavaScript `number`.
`number` values outside the range of `-(2**53 - 1)` - `(2**53 - 1)` will lose precision.
Non-finite number values (`NaN`, `+Infinity`, or `-Infinity`) set the result to zero.
#####  `napi_get_value_string_latin1`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-value-string-latin1)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_get_value_string_latin1(napi_env env,
                                         napi_value value,
                                         char* buf,
                                         size_t bufsize,
                                         size_t* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: `napi_value` representing JavaScript string.
  * `[in] buf`: Buffer to write the ISO-8859-1-encoded string into. If `NULL` is passed in, the length of the string in bytes and excluding the null terminator is returned in `result`.
  * `[in] bufsize`: Size of the destination buffer. When this value is insufficient, the returned string is truncated and null-terminated. If this value is zero, then the string is not returned and no changes are done to the buffer.
  * `[out] result`: Number of bytes copied into the buffer, excluding the null terminator.


Returns `napi_ok` if the API succeeded. If a non-`string` `napi_value` is passed in it returns `napi_string_expected`.
This API returns the ISO-8859-1-encoded string corresponding the value passed in.
#####  `napi_get_value_string_utf8`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-value-string-utf8)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_get_value_string_utf8(napi_env env,
                                       napi_value value,
                                       char* buf,
                                       size_t bufsize,
                                       size_t* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: `napi_value` representing JavaScript string.
  * `[in] buf`: Buffer to write the UTF8-encoded string into. If `NULL` is passed in, the length of the string in bytes and excluding the null terminator is returned in `result`.
  * `[in] bufsize`: Size of the destination buffer. When this value is insufficient, the returned string is truncated and null-terminated. If this value is zero, then the string is not returned and no changes are done to the buffer.
  * `[out] result`: Number of bytes copied into the buffer, excluding the null terminator.


Returns `napi_ok` if the API succeeded. If a non-`string` `napi_value` is passed in it returns `napi_string_expected`.
This API returns the UTF8-encoded string corresponding the value passed in.
#####  `napi_get_value_string_utf16`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-value-string-utf16)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_get_value_string_utf16(napi_env env,
                                        napi_value value,
                                        char16_t* buf,
                                        size_t bufsize,
                                        size_t* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: `napi_value` representing JavaScript string.
  * `[in] buf`: Buffer to write the UTF16-LE-encoded string into. If `NULL` is passed in, the length of the string in 2-byte code units and excluding the null terminator is returned.
  * `[in] bufsize`: Size of the destination buffer. When this value is insufficient, the returned string is truncated and null-terminated. If this value is zero, then the string is not returned and no changes are done to the buffer.
  * `[out] result`: Number of 2-byte code units copied into the buffer, excluding the null terminator.


Returns `napi_ok` if the API succeeded. If a non-`string` `napi_value` is passed in it returns `napi_string_expected`.
This API returns the UTF16-encoded string corresponding the value passed in.
#####  `napi_get_value_uint32`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-value-uint32)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_get_value_uint32(napi_env env,
                                  napi_value value,
                                  uint32_t* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: `napi_value` representing JavaScript `number`.
  * `[out] result`: C primitive equivalent of the given `napi_value` as a `uint32_t`.


Returns `napi_ok` if the API succeeded. If a non-number `napi_value` is passed in it returns `napi_number_expected`.
This API returns the C primitive equivalent of the given `napi_value` as a `uint32_t`.
#### Functions to get global instances[#](https://nodejs.org/docs/latest/api/n-api.html#functions-to-get-global-instances)
#####  `napi_get_boolean`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-boolean)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_get_boolean(napi_env env, bool value, napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: The value of the boolean to retrieve.
  * `[out] result`: `napi_value` representing JavaScript `Boolean` singleton to retrieve.


Returns `napi_ok` if the API succeeded.
This API is used to return the JavaScript singleton object that is used to represent the given boolean value.
#####  `napi_get_global`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-global)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_get_global(napi_env env, napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[out] result`: `napi_value` representing JavaScript `global` object.


Returns `napi_ok` if the API succeeded.
This API returns the `global` object.
#####  `napi_get_null`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-null)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_get_null(napi_env env, napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[out] result`: `napi_value` representing JavaScript `null` object.


Returns `napi_ok` if the API succeeded.
This API returns the `null` object.
#####  `napi_get_undefined`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-undefined)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_get_undefined(napi_env env, napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[out] result`: `napi_value` representing JavaScript Undefined value.


Returns `napi_ok` if the API succeeded.
This API returns the Undefined object.
### Working with JavaScript values and abstract operations[#](https://nodejs.org/docs/latest/api/n-api.html#working-with-javascript-values-and-abstract-operations)
Node-API exposes a set of APIs to perform some abstract operations on JavaScript values.
These APIs support doing one of the following:
  1. Coerce JavaScript values to specific JavaScript types (such as `number` or `string`).
  2. Check the type of a JavaScript value.
  3. Check for equality between two JavaScript values.


####  `napi_coerce_to_bool`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-coerce-to-bool)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_coerce_to_bool(napi_env env,
                                napi_value value,
                                napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: The JavaScript value to coerce.
  * `[out] result`: `napi_value` representing the coerced JavaScript `Boolean`.


Returns `napi_ok` if the API succeeded.
This API implements the abstract operation `ToBoolean()` as defined in
####  `napi_coerce_to_number`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-coerce-to-number)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_coerce_to_number(napi_env env,
                                  napi_value value,
                                  napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: The JavaScript value to coerce.
  * `[out] result`: `napi_value` representing the coerced JavaScript `number`.


Returns `napi_ok` if the API succeeded.
This API implements the abstract operation `ToNumber()` as defined in
####  `napi_coerce_to_object`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-coerce-to-object)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_coerce_to_object(napi_env env,
                                  napi_value value,
                                  napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: The JavaScript value to coerce.
  * `[out] result`: `napi_value` representing the coerced JavaScript `Object`.


Returns `napi_ok` if the API succeeded.
This API implements the abstract operation `ToObject()` as defined in
####  `napi_coerce_to_string`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-coerce-to-string)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_coerce_to_string(napi_env env,
                                  napi_value value,
                                  napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: The JavaScript value to coerce.
  * `[out] result`: `napi_value` representing the coerced JavaScript `string`.


Returns `napi_ok` if the API succeeded.
This API implements the abstract operation `ToString()` as defined in
####  `napi_typeof`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-typeof)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_typeof(napi_env env, napi_value value, napi_valuetype* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: The JavaScript value whose type to query.
  * `[out] result`: The type of the JavaScript value.


Returns `napi_ok` if the API succeeded.
  * `napi_invalid_arg` if the type of `value` is not a known ECMAScript type and `value` is not an External value.


This API represents behavior similar to invoking the `typeof` Operator on the object as defined in
  1. It has support for detecting an External value.
  2. It detects `null` as a separate type, while ECMAScript `typeof` would detect `object`.


If `value` has a type that is invalid, an error is returned.
####  `napi_instanceof`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-instanceof)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_instanceof(napi_env env,
                            napi_value object,
                            napi_value constructor,
                            bool* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] object`: The JavaScript value to check.
  * `[in] constructor`: The JavaScript function object of the constructor function to check against.
  * `[out] result`: Boolean that is set to true if `object instanceof constructor` is true.


Returns `napi_ok` if the API succeeded.
This API represents invoking the `instanceof` Operator on the object as defined in
####  `napi_is_array`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-is-array)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_is_array(napi_env env, napi_value value, bool* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: The JavaScript value to check.
  * `[out] result`: Whether the given object is an array.


Returns `napi_ok` if the API succeeded.
This API represents invoking the `IsArray` operation on the object as defined in
####  `napi_is_arraybuffer`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-is-arraybuffer)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_is_arraybuffer(napi_env env, napi_value value, bool* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: The JavaScript value to check.
  * `[out] result`: Whether the given object is an `ArrayBuffer`.


Returns `napi_ok` if the API succeeded.
This API checks if the `Object` passed in is an array buffer.
####  `napi_is_buffer`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-is-buffer)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_is_buffer(napi_env env, napi_value value, bool* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: The JavaScript value to check.
  * `[out] result`: Whether the given `napi_value` represents a `node::Buffer` or `Uint8Array` object.


Returns `napi_ok` if the API succeeded.
This API checks if the `Object` passed in is a buffer or Uint8Array. [`napi_is_typedarray`](https://nodejs.org/docs/latest/api/n-api.html#napi_is_typedarray) should be preferred if the caller needs to check if the value is a Uint8Array.
####  `napi_is_date`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-is-date)
Added in: v11.11.0, v10.17.0**N-API Version:** 5
```
napi_status napi_is_date(napi_env env, napi_value value, bool* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: The JavaScript value to check.
  * `[out] result`: Whether the given `napi_value` represents a JavaScript `Date` object.


Returns `napi_ok` if the API succeeded.
This API checks if the `Object` passed in is a date.
####  `napi_is_error`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-is-error-1)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_is_error(napi_env env, napi_value value, bool* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: The JavaScript value to check.
  * `[out] result`: Whether the given `napi_value` represents an `Error` object.


Returns `napi_ok` if the API succeeded.
This API checks if the `Object` passed in is an `Error`.
####  `napi_is_typedarray`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-is-typedarray)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_is_typedarray(napi_env env, napi_value value, bool* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: The JavaScript value to check.
  * `[out] result`: Whether the given `napi_value` represents a `TypedArray`.


Returns `napi_ok` if the API succeeded.
This API checks if the `Object` passed in is a typed array.
####  `napi_is_dataview`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-is-dataview)
Added in: v8.3.0**N-API Version:** 1
```
napi_status napi_is_dataview(napi_env env, napi_value value, bool* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: The JavaScript value to check.
  * `[out] result`: Whether the given `napi_value` represents a `DataView`.


Returns `napi_ok` if the API succeeded.
This API checks if the `Object` passed in is a `DataView`.
####  `napi_strict_equals`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-strict-equals)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_strict_equals(napi_env env,
                               napi_value lhs,
                               napi_value rhs,
                               bool* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] lhs`: The JavaScript value to check.
  * `[in] rhs`: The JavaScript value to check against.
  * `[out] result`: Whether the two `napi_value` objects are equal.


Returns `napi_ok` if the API succeeded.
This API represents the invocation of the Strict Equality algorithm as defined in
####  `napi_detach_arraybuffer`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-detach-arraybuffer)
Added in: v13.0.0, v12.16.0, v10.22.0**N-API Version:** 7
```
napi_status napi_detach_arraybuffer(napi_env env,
                                    napi_value arraybuffer)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] arraybuffer`: The JavaScript `ArrayBuffer` to be detached.


Returns `napi_ok` if the API succeeded. If a non-detachable `ArrayBuffer` is passed in it returns `napi_detachable_arraybuffer_expected`.
Generally, an `ArrayBuffer` is non-detachable if it has been detached before. The engine may impose additional conditions on whether an `ArrayBuffer` is detachable. For example, V8 requires that the `ArrayBuffer` be external, that is, created with [`napi_create_external_arraybuffer`](https://nodejs.org/docs/latest/api/n-api.html#napi_create_external_arraybuffer).
This API represents the invocation of the `ArrayBuffer` detach operation as defined in
####  `napi_is_detached_arraybuffer`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-is-detached-arraybuffer)
Added in: v13.3.0, v12.16.0, v10.22.0**N-API Version:** 7
```
napi_status napi_is_detached_arraybuffer(napi_env env,
                                         napi_value arraybuffer,
                                         bool* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] arraybuffer`: The JavaScript `ArrayBuffer` to be checked.
  * `[out] result`: Whether the `arraybuffer` is detached.


Returns `napi_ok` if the API succeeded.
The `ArrayBuffer` is considered detached if its internal data is `null`.
This API represents the invocation of the `ArrayBuffer` `IsDetachedBuffer` operation as defined in
