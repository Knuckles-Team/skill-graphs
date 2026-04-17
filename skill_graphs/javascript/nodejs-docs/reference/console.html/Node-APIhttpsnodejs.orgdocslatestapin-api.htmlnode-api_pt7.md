####  `node_api_is_sharedarraybuffer`[#](https://nodejs.org/docs/latest/api/n-api.html#node-api-is-sharedarraybuffer)
Added in: v24.9.0
Stability: 1 - Experimental
```
napi_status node_api_is_sharedarraybuffer(napi_env env, napi_value value, bool* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] value`: The JavaScript value to check.
  * `[out] result`: Whether the given `napi_value` represents a `SharedArrayBuffer`.


Returns `napi_ok` if the API succeeded.
This API checks if the Object passed in is a `SharedArrayBuffer`.
####  `node_api_create_sharedarraybuffer`[#](https://nodejs.org/docs/latest/api/n-api.html#node-api-create-sharedarraybuffer)
Added in: v24.9.0
Stability: 1 - Experimental
```
napi_status node_api_create_sharedarraybuffer(napi_env env,
                                             size_t byte_length,
                                             void** data,
                                             napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] byte_length`: The length in bytes of the shared array buffer to create.
  * `[out] data`: Pointer to the underlying byte buffer of the `SharedArrayBuffer`. `data` can optionally be ignored by passing `NULL`.
  * `[out] result`: A `napi_value` representing a JavaScript `SharedArrayBuffer`.


Returns `napi_ok` if the API succeeded.
This API returns a Node-API value corresponding to a JavaScript `SharedArrayBuffer`. `SharedArrayBuffer`s are used to represent fixed-length binary data buffers that can be shared across multiple workers.
The `SharedArrayBuffer` allocated will have an underlying byte buffer whose size is determined by the `byte_length` parameter that's passed in. The underlying buffer is optionally returned back to the caller in case the caller wants to directly manipulate the buffer. This buffer can only be written to directly from native code. To write to this buffer from JavaScript, a typed array or `DataView` object would need to be created.
JavaScript `SharedArrayBuffer` objects are described in
### Working with JavaScript properties[#](https://nodejs.org/docs/latest/api/n-api.html#working-with-javascript-properties)
Node-API exposes a set of APIs to get and set properties on JavaScript objects.
Properties in JavaScript are represented as a tuple of a key and a value. Fundamentally, all property keys in Node-API can be represented in one of the following forms:
  * Named: a simple UTF8-encoded string
  * Integer-Indexed: an index value represented by `uint32_t`
  * JavaScript value: these are represented in Node-API by `napi_value`. This can be a `napi_value` representing a `string`, `number`, or `symbol`.


Node-API values are represented by the type `napi_value`. Any Node-API call that requires a JavaScript value takes in a `napi_value`. However, it's the caller's responsibility to make sure that the `napi_value` in question is of the JavaScript type expected by the API.
The APIs documented in this section provide a simple interface to get and set properties on arbitrary JavaScript objects represented by `napi_value`.
For instance, consider the following JavaScript code snippet:
```
const obj = {};
obj.myProp = 123;
copy
```

The equivalent can be done using Node-API values with the following snippet:
```
napi_status status = napi_generic_failure;

// const obj = {}
napi_value obj, value;
status = napi_create_object(env, &obj);
if (status != napi_ok) return status;

// Create a napi_value for 123
status = napi_create_int32(env, 123, &value);
if (status != napi_ok) return status;

// obj.myProp = 123
status = napi_set_named_property(env, obj, "myProp", value);
if (status != napi_ok) return status;
copy
```

Indexed properties can be set in a similar manner. Consider the following JavaScript snippet:
```
const arr = [];
arr[123] = 'hello';
copy
```

The equivalent can be done using Node-API values with the following snippet:
```
napi_status status = napi_generic_failure;

// const arr = [];
napi_value arr, value;
status = napi_create_array(env, &arr);
if (status != napi_ok) return status;

// Create a napi_value for 'hello'
status = napi_create_string_utf8(env, "hello", NAPI_AUTO_LENGTH, &value);
if (status != napi_ok) return status;

// arr[123] = 'hello';
status = napi_set_element(env, arr, 123, value);
if (status != napi_ok) return status;
copy
```

Properties can be retrieved using the APIs described in this section. Consider the following JavaScript snippet:
```
const arr = [];
const value = arr[123];
copy
```

The following is the approximate equivalent of the Node-API counterpart:
```
napi_status status = napi_generic_failure;

// const arr = []
napi_value arr, value;
status = napi_create_array(env, &arr);
if (status != napi_ok) return status;

// const value = arr[123]
status = napi_get_element(env, arr, 123, &value);
if (status != napi_ok) return status;
copy
```

Finally, multiple properties can also be defined on an object for performance reasons. Consider the following JavaScript:
```
const obj = {};
Object.defineProperties(obj, {
  'foo': { value: 123, writable: true, configurable: true, enumerable: true },
  'bar': { value: 456, writable: true, configurable: true, enumerable: true },
});
copy
```

The following is the approximate equivalent of the Node-API counterpart:
```
napi_status status = napi_status_generic_failure;

// const obj = {};
napi_value obj;
status = napi_create_object(env, &obj);
if (status != napi_ok) return status;

// Create napi_values for 123 and 456
napi_value fooValue, barValue;
status = napi_create_int32(env, 123, &fooValue);
if (status != napi_ok) return status;
status = napi_create_int32(env, 456, &barValue);
if (status != napi_ok) return status;

// Set the properties
napi_property_descriptor descriptors[] = {
  { "foo", NULL, NULL, NULL, NULL, fooValue, napi_writable | napi_configurable, NULL },
  { "bar", NULL, NULL, NULL, NULL, barValue, napi_writable | napi_configurable, NULL }
}
status = napi_define_properties(env,
                                obj,
                                sizeof(descriptors) / sizeof(descriptors[0]),
                                descriptors);
if (status != napi_ok) return status;
copy
```

#### Structures[#](https://nodejs.org/docs/latest/api/n-api.html#structures)
#####  `napi_property_attributes`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-property-attributes)
History Version | Changes
---|---
v14.12.0 | added `napi_default_method` and `napi_default_property`.
```
typedef enum {
  napi_default = 0,
  napi_writable = 1 << 0,
  napi_enumerable = 1 << 1,
  napi_configurable = 1 << 2,

  // Used with napi_define_class to distinguish static properties
  // from instance properties. Ignored by napi_define_properties.
  napi_static = 1 << 10,

  // Default for class methods.
  napi_default_method = napi_writable | napi_configurable,

  // Default for object properties, like in JS obj[prop].
  napi_default_jsproperty = napi_writable |
                          napi_enumerable |
                          napi_configurable,
} napi_property_attributes;
copy
```

`napi_property_attributes` are bit flags used to control the behavior of properties set on a JavaScript object. Other than `napi_static` they correspond to the attributes listed in
  * `napi_default`: No explicit attributes are set on the property. By default, a property is read only, not enumerable and not configurable.
  * `napi_writable`: The property is writable.
  * `napi_enumerable`: The property is enumerable.
  * `napi_configurable`: The property is configurable as defined in
  * `napi_static`: The property will be defined as a static property on a class as opposed to an instance property, which is the default. This is used only by [`napi_define_class`](https://nodejs.org/docs/latest/api/n-api.html#napi_define_class). It is ignored by `napi_define_properties`.
  * `napi_default_method`: Like a method in a JS class, the property is configurable and writeable, but not enumerable.
  * `napi_default_jsproperty`: Like a property set via assignment in JavaScript, the property is writable, enumerable, and configurable.


#####  `napi_property_descriptor`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-property-descriptor)
```
typedef struct {
  // One of utf8name or name should be NULL.
  const char* utf8name;
  napi_value name;

  napi_callback method;
  napi_callback getter;
  napi_callback setter;
  napi_value value;

  napi_property_attributes attributes;
  void* data;
} napi_property_descriptor;
copy
```

  * `utf8name`: Optional string describing the key for the property, encoded as UTF8. One of `utf8name` or `name` must be provided for the property.
  * `name`: Optional `napi_value` that points to a JavaScript string or symbol to be used as the key for the property. One of `utf8name` or `name` must be provided for the property.
  * `value`: The value that's retrieved by a get access of the property if the property is a data property. If this is passed in, set `getter`, `setter`, `method` and `data` to `NULL` (since these members won't be used).
  * `getter`: A function to call when a get access of the property is performed. If this is passed in, set `value` and `method` to `NULL` (since these members won't be used). The given function is called implicitly by the runtime when the property is accessed from JavaScript code (or if a get on the property is performed using a Node-API call). [`napi_callback`](https://nodejs.org/docs/latest/api/n-api.html#napi_callback) provides more details.
  * `setter`: A function to call when a set access of the property is performed. If this is passed in, set `value` and `method` to `NULL` (since these members won't be used). The given function is called implicitly by the runtime when the property is set from JavaScript code (or if a set on the property is performed using a Node-API call). [`napi_callback`](https://nodejs.org/docs/latest/api/n-api.html#napi_callback) provides more details.
  * `method`: Set this to make the property descriptor object's `value` property to be a JavaScript function represented by `method`. If this is passed in, set `value`, `getter` and `setter` to `NULL` (since these members won't be used). [`napi_callback`](https://nodejs.org/docs/latest/api/n-api.html#napi_callback) provides more details.
  * `attributes`: The attributes associated with the particular property. See [`napi_property_attributes`](https://nodejs.org/docs/latest/api/n-api.html#napi_property_attributes).
  * `data`: The callback data passed into `method`, `getter` and `setter` if this function is invoked.


#### Functions[#](https://nodejs.org/docs/latest/api/n-api.html#functions)
#####  `napi_get_property_names`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-property-names)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_get_property_names(napi_env env,
                                    napi_value object,
                                    napi_value* result);
copy
```

  * `[in] env`: The environment that the Node-API call is invoked under.
  * `[in] object`: The object from which to retrieve the properties.
  * `[out] result`: A `napi_value` representing an array of JavaScript values that represent the property names of the object. The API can be used to iterate over `result` using [`napi_get_array_length`](https://nodejs.org/docs/latest/api/n-api.html#napi_get_array_length) and [`napi_get_element`](https://nodejs.org/docs/latest/api/n-api.html#napi_get_element).


Returns `napi_ok` if the API succeeded.
This API returns the names of the enumerable properties of `object` as an array of strings. The properties of `object` whose key is a symbol will not be included.
#####  `napi_get_all_property_names`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-all-property-names)
Added in: v13.7.0, v12.17.0, v10.20.0**N-API Version:** 6
```
napi_get_all_property_names(napi_env env,
                            napi_value object,
                            napi_key_collection_mode key_mode,
                            napi_key_filter key_filter,
                            napi_key_conversion key_conversion,
                            napi_value* result);
copy
```

  * `[in] env`: The environment that the Node-API call is invoked under.
  * `[in] object`: The object from which to retrieve the properties.
  * `[in] key_mode`: Whether to retrieve prototype properties as well.
  * `[in] key_filter`: Which properties to retrieve (enumerable/readable/writable).
  * `[in] key_conversion`: Whether to convert numbered property keys to strings.
  * `[out] result`: A `napi_value` representing an array of JavaScript values that represent the property names of the object. [`napi_get_array_length`](https://nodejs.org/docs/latest/api/n-api.html#napi_get_array_length) and [`napi_get_element`](https://nodejs.org/docs/latest/api/n-api.html#napi_get_element) can be used to iterate over `result`.


Returns `napi_ok` if the API succeeded.
This API returns an array containing the names of the available properties of this object.
#####  `napi_set_property`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-set-property)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_set_property(napi_env env,
                              napi_value object,
                              napi_value key,
                              napi_value value);
copy
```

  * `[in] env`: The environment that the Node-API call is invoked under.
  * `[in] object`: The object on which to set the property.
  * `[in] key`: The name of the property to set.
  * `[in] value`: The property value.


Returns `napi_ok` if the API succeeded.
This API set a property on the `Object` passed in.
#####  `napi_get_property`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-property)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_get_property(napi_env env,
                              napi_value object,
                              napi_value key,
                              napi_value* result);
copy
```

  * `[in] env`: The environment that the Node-API call is invoked under.
  * `[in] object`: The object from which to retrieve the property.
  * `[in] key`: The name of the property to retrieve.
  * `[out] result`: The value of the property.


Returns `napi_ok` if the API succeeded.
This API gets the requested property from the `Object` passed in.
#####  `napi_has_property`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-has-property)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_has_property(napi_env env,
                              napi_value object,
                              napi_value key,
                              bool* result);
copy
```

  * `[in] env`: The environment that the Node-API call is invoked under.
  * `[in] object`: The object to query.
  * `[in] key`: The name of the property whose existence to check.
  * `[out] result`: Whether the property exists on the object or not.


Returns `napi_ok` if the API succeeded.
This API checks if the `Object` passed in has the named property.
#####  `napi_delete_property`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-delete-property)
Added in: v8.2.0**N-API Version:** 1
```
napi_status napi_delete_property(napi_env env,
                                 napi_value object,
                                 napi_value key,
                                 bool* result);
copy
```

  * `[in] env`: The environment that the Node-API call is invoked under.
  * `[in] object`: The object to query.
  * `[in] key`: The name of the property to delete.
  * `[out] result`: Whether the property deletion succeeded or not. `result` can optionally be ignored by passing `NULL`.


Returns `napi_ok` if the API succeeded.
This API attempts to delete the `key` own property from `object`.
#####  `napi_has_own_property`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-has-own-property)
Added in: v8.2.0**N-API Version:** 1
```
napi_status napi_has_own_property(napi_env env,
                                  napi_value object,
                                  napi_value key,
                                  bool* result);
copy
```

  * `[in] env`: The environment that the Node-API call is invoked under.
  * `[in] object`: The object to query.
  * `[in] key`: The name of the own property whose existence to check.
  * `[out] result`: Whether the own property exists on the object or not.


Returns `napi_ok` if the API succeeded.
This API checks if the `Object` passed in has the named own property. `key` must be a `string` or a `symbol`, or an error will be thrown. Node-API will not perform any conversion between data types.
#####  `napi_set_named_property`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-set-named-property)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_set_named_property(napi_env env,
                                    napi_value object,
                                    const char* utf8Name,
                                    napi_value value);
copy
```

  * `[in] env`: The environment that the Node-API call is invoked under.
  * `[in] object`: The object on which to set the property.
  * `[in] utf8Name`: The name of the property to set.
  * `[in] value`: The property value.


Returns `napi_ok` if the API succeeded.
This method is equivalent to calling [`napi_set_property`](https://nodejs.org/docs/latest/api/n-api.html#napi_set_property) with a `napi_value` created from the string passed in as `utf8Name`.
#####  `napi_get_named_property`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-named-property)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_get_named_property(napi_env env,
                                    napi_value object,
                                    const char* utf8Name,
                                    napi_value* result);
copy
```

  * `[in] env`: The environment that the Node-API call is invoked under.
  * `[in] object`: The object from which to retrieve the property.
  * `[in] utf8Name`: The name of the property to get.
  * `[out] result`: The value of the property.


Returns `napi_ok` if the API succeeded.
This method is equivalent to calling [`napi_get_property`](https://nodejs.org/docs/latest/api/n-api.html#napi_get_property) with a `napi_value` created from the string passed in as `utf8Name`.
#####  `napi_has_named_property`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-has-named-property)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_has_named_property(napi_env env,
                                    napi_value object,
                                    const char* utf8Name,
                                    bool* result);
copy
```

  * `[in] env`: The environment that the Node-API call is invoked under.
  * `[in] object`: The object to query.
  * `[in] utf8Name`: The name of the property whose existence to check.
  * `[out] result`: Whether the property exists on the object or not.


Returns `napi_ok` if the API succeeded.
This method is equivalent to calling [`napi_has_property`](https://nodejs.org/docs/latest/api/n-api.html#napi_has_property) with a `napi_value` created from the string passed in as `utf8Name`.
#####  `napi_set_element`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-set-element)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_set_element(napi_env env,
                             napi_value object,
                             uint32_t index,
                             napi_value value);
copy
```

  * `[in] env`: The environment that the Node-API call is invoked under.
  * `[in] object`: The object from which to set the properties.
  * `[in] index`: The index of the property to set.
  * `[in] value`: The property value.


Returns `napi_ok` if the API succeeded.
This API sets an element on the `Object` passed in.
#####  `napi_get_element`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-element)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_get_element(napi_env env,
                             napi_value object,
                             uint32_t index,
                             napi_value* result);
copy
```

  * `[in] env`: The environment that the Node-API call is invoked under.
  * `[in] object`: The object from which to retrieve the property.
  * `[in] index`: The index of the property to get.
  * `[out] result`: The value of the property.


Returns `napi_ok` if the API succeeded.
This API gets the element at the requested index.
#####  `napi_has_element`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-has-element)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_has_element(napi_env env,
                             napi_value object,
                             uint32_t index,
                             bool* result);
copy
```

  * `[in] env`: The environment that the Node-API call is invoked under.
  * `[in] object`: The object to query.
  * `[in] index`: The index of the property whose existence to check.
  * `[out] result`: Whether the property exists on the object or not.


Returns `napi_ok` if the API succeeded.
This API returns if the `Object` passed in has an element at the requested index.
#####  `napi_delete_element`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-delete-element)
Added in: v8.2.0**N-API Version:** 1
```
napi_status napi_delete_element(napi_env env,
                                napi_value object,
                                uint32_t index,
                                bool* result);
copy
```

  * `[in] env`: The environment that the Node-API call is invoked under.
  * `[in] object`: The object to query.
  * `[in] index`: The index of the property to delete.
  * `[out] result`: Whether the element deletion succeeded or not. `result` can optionally be ignored by passing `NULL`.


Returns `napi_ok` if the API succeeded.
This API attempts to delete the specified `index` from `object`.
#####  `napi_define_properties`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-define-properties)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_define_properties(napi_env env,
                                   napi_value object,
                                   size_t property_count,
                                   const napi_property_descriptor* properties);
copy
```

  * `[in] env`: The environment that the Node-API call is invoked under.
  * `[in] object`: The object from which to retrieve the properties.
  * `[in] property_count`: The number of elements in the `properties` array.
  * `[in] properties`: The array of property descriptors.


Returns `napi_ok` if the API succeeded.
This method allows the efficient definition of multiple properties on a given object. The properties are defined using property descriptors (see [`napi_property_descriptor`](https://nodejs.org/docs/latest/api/n-api.html#napi_property_descriptor)). Given an array of such property descriptors, this API will set the properties on the object one at a time, as defined by `DefineOwnProperty()` (described in
#####  `napi_object_freeze`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-object-freeze)
Added in: v14.14.0, v12.20.0**N-API Version:** 8
```
napi_status napi_object_freeze(napi_env env,
                               napi_value object);
copy
```

  * `[in] env`: The environment that the Node-API call is invoked under.
  * `[in] object`: The object to freeze.


Returns `napi_ok` if the API succeeded.
This method freezes a given object. This prevents new properties from being added to it, existing properties from being removed, prevents changing the enumerability, configurability, or writability of existing properties, and prevents the values of existing properties from being changed. It also prevents the object's prototype from being changed. This is described in
#####  `napi_object_seal`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-object-seal)
Added in: v14.14.0, v12.20.0**N-API Version:** 8
```
napi_status napi_object_seal(napi_env env,
                             napi_value object);
copy
```

  * `[in] env`: The environment that the Node-API call is invoked under.
  * `[in] object`: The object to seal.


Returns `napi_ok` if the API succeeded.
This method seals a given object. This prevents new properties from being added to it, as well as marking all existing properties as non-configurable. This is described in
#####  `node_api_set_prototype`[#](https://nodejs.org/docs/latest/api/n-api.html#node-api-set-prototype)
Added in: v25.4.0
Stability: 1 - Experimental
```
napi_status node_api_set_prototype(napi_env env,
                                   napi_value object,
                                   napi_value value);
copy
```

  * `[in] env`: The environment that the Node-API call is invoked under.
  * `[in] object`: The object on which to set the prototype.
  * `[in] value`: The prototype value.


Returns `napi_ok` if the API succeeded.
This API sets the prototype of the `Object` passed in.
### Working with JavaScript functions[#](https://nodejs.org/docs/latest/api/n-api.html#working-with-javascript-functions)
Node-API provides a set of APIs that allow JavaScript code to call back into native code. Node-APIs that support calling back into native code take in a callback functions represented by the `napi_callback` type. When the JavaScript VM calls back to native code, the `napi_callback` function provided is invoked. The APIs documented in this section allow the callback function to do the following:
