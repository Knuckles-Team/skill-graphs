  * Get information about the context in which the callback was invoked.
  * Get the arguments passed into the callback.
  * Return a `napi_value` back from the callback.


Additionally, Node-API provides a set of functions which allow calling JavaScript functions from native code. One can either call a function like a regular JavaScript function call, or as a constructor function.
Any non-`NULL` data which is passed to this API via the `data` field of the `napi_property_descriptor` items can be associated with `object` and freed whenever `object` is garbage-collected by passing both `object` and the data to [`napi_add_finalizer`](https://nodejs.org/docs/latest/api/n-api.html#napi_add_finalizer).
####  `napi_call_function`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-call-function)
Added in: v8.0.0**N-API Version:** 1
```
NAPI_EXTERN napi_status napi_call_function(napi_env env,
                                           napi_value recv,
                                           napi_value func,
                                           size_t argc,
                                           const napi_value* argv,
                                           napi_value* result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] recv`: The `this` value passed to the called function.
  * `[in] func`: `napi_value` representing the JavaScript function to be invoked.
  * `[in] argc`: The count of elements in the `argv` array.
  * `[in] argv`: Array of `napi_values` representing JavaScript values passed in as arguments to the function.
  * `[out] result`: `napi_value` representing the JavaScript object returned.


Returns `napi_ok` if the API succeeded.
This method allows a JavaScript function object to be called from a native add-on. This is the primary mechanism of calling back _from_ the add-on's native code _into_ JavaScript. For the special case of calling into JavaScript after an async operation, see [`napi_make_callback`](https://nodejs.org/docs/latest/api/n-api.html#napi_make_callback).
A sample use case might look as follows. Consider the following JavaScript snippet:
```
function AddTwo(num) {
  return num + 2;
}
global.AddTwo = AddTwo;
copy
```

Then, the above function can be invoked from a native add-on using the following code:
```
// Get the function named "AddTwo" on the global object
napi_value global, add_two, arg;
napi_status status = napi_get_global(env, &global);
if (status != napi_ok) return;

status = napi_get_named_property(env, global, "AddTwo", &add_two);
if (status != napi_ok) return;

// const arg = 1337
status = napi_create_int32(env, 1337, &arg);
if (status != napi_ok) return;

napi_value* argv = &arg;
size_t argc = 1;

// AddTwo(arg);
napi_value return_val;
status = napi_call_function(env, global, add_two, argc, argv, &return_val);
if (status != napi_ok) return;

// Convert the result back to a native type
int32_t result;
status = napi_get_value_int32(env, return_val, &result);
if (status != napi_ok) return;
copy
```

####  `napi_create_function`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-create-function)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_create_function(napi_env env,
                                 const char* utf8name,
                                 size_t length,
                                 napi_callback cb,
                                 void* data,
                                 napi_value* result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] utf8Name`: Optional name of the function encoded as UTF8. This is visible within JavaScript as the new function object's `name` property.
  * `[in] length`: The length of the `utf8name` in bytes, or `NAPI_AUTO_LENGTH` if it is null-terminated.
  * `[in] cb`: The native function which should be called when this function object is invoked. [`napi_callback`](https://nodejs.org/docs/latest/api/n-api.html#napi_callback) provides more details.
  * `[in] data`: User-provided data context. This will be passed back into the function when invoked later.
  * `[out] result`: `napi_value` representing the JavaScript function object for the newly created function.


Returns `napi_ok` if the API succeeded.
This API allows an add-on author to create a function object in native code. This is the primary mechanism to allow calling _into_ the add-on's native code _from_ JavaScript.
The newly created function is not automatically visible from script after this call. Instead, a property must be explicitly set on any object that is visible to JavaScript, in order for the function to be accessible from script.
In order to expose a function as part of the add-on's module exports, set the newly created function on the exports object. A sample module might look as follows:
```
napi_value SayHello(napi_env env, napi_callback_info info) {
  printf("Hello\n");
  return NULL;
}

napi_value Init(napi_env env, napi_value exports) {
  napi_status status;

  napi_value fn;
  status = napi_create_function(env, NULL, 0, SayHello, NULL, &fn);
  if (status != napi_ok) return NULL;

  status = napi_set_named_property(env, exports, "sayHello", fn);
  if (status != napi_ok) return NULL;

  return exports;
}

NAPI_MODULE(NODE_GYP_MODULE_NAME, Init)
copy
```

Given the above code, the add-on can be used from JavaScript as follows:
```
const myaddon = require('./addon');
myaddon.sayHello();
copy
```

The string passed to `require()` is the name of the target in `binding.gyp` responsible for creating the `.node` file.
Any non-`NULL` data which is passed to this API via the `data` parameter can be associated with the resulting JavaScript function (which is returned in the `result` parameter) and freed whenever the function is garbage-collected by passing both the JavaScript function and the data to [`napi_add_finalizer`](https://nodejs.org/docs/latest/api/n-api.html#napi_add_finalizer).
JavaScript `Function`s are described in
####  `napi_get_cb_info`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-cb-info)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_get_cb_info(napi_env env,
                             napi_callback_info cbinfo,
                             size_t* argc,
                             napi_value* argv,
                             napi_value* thisArg,
                             void** data)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] cbinfo`: The callback info passed into the callback function.
  * `[in-out] argc`: Specifies the length of the provided `argv` array and receives the actual count of arguments. `argc` can optionally be ignored by passing `NULL`.
  * `[out] argv`: C array of `napi_value`s to which the arguments will be copied. If there are more arguments than the provided count, only the requested number of arguments are copied. If there are fewer arguments provided than claimed, the rest of `argv` is filled with `napi_value` values that represent `undefined`. `argv` can optionally be ignored by passing `NULL`.
  * `[out] thisArg`: Receives the JavaScript `this` argument for the call. `thisArg` can optionally be ignored by passing `NULL`.
  * `[out] data`: Receives the data pointer for the callback. `data` can optionally be ignored by passing `NULL`.


Returns `napi_ok` if the API succeeded.
This method is used within a callback function to retrieve details about the call like the arguments and the `this` pointer from a given callback info.
####  `napi_get_new_target`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-get-new-target)
Added in: v8.6.0**N-API Version:** 1
```
napi_status napi_get_new_target(napi_env env,
                                napi_callback_info cbinfo,
                                napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] cbinfo`: The callback info passed into the callback function.
  * `[out] result`: The `new.target` of the constructor call.


Returns `napi_ok` if the API succeeded.
This API returns the `new.target` of the constructor call. If the current callback is not a constructor call, the result is `NULL`.
####  `napi_new_instance`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-new-instance)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_new_instance(napi_env env,
                              napi_value cons,
                              size_t argc,
                              napi_value* argv,
                              napi_value* result)
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] cons`: `napi_value` representing the JavaScript function to be invoked as a constructor.
  * `[in] argc`: The count of elements in the `argv` array.
  * `[in] argv`: Array of JavaScript values as `napi_value` representing the arguments to the constructor. If `argc` is zero this parameter may be omitted by passing in `NULL`.
  * `[out] result`: `napi_value` representing the JavaScript object returned, which in this case is the constructed object.


This method is used to instantiate a new JavaScript value using a given `napi_value` that represents the constructor for the object. For example, consider the following snippet:
```
function MyObject(param) {
  this.param = param;
}

const arg = 'hello';
const value = new MyObject(arg);
copy
```

The following can be approximated in Node-API using the following snippet:
```
// Get the constructor function MyObject
napi_value global, constructor, arg, value;
napi_status status = napi_get_global(env, &global);
if (status != napi_ok) return;

status = napi_get_named_property(env, global, "MyObject", &constructor);
if (status != napi_ok) return;

// const arg = "hello"
status = napi_create_string_utf8(env, "hello", NAPI_AUTO_LENGTH, &arg);
if (status != napi_ok) return;

napi_value* argv = &arg;
size_t argc = 1;

// const value = new MyObject(arg)
status = napi_new_instance(env, constructor, argc, argv, &value);
copy
```

Returns `napi_ok` if the API succeeded.
### Object wrap[#](https://nodejs.org/docs/latest/api/n-api.html#object-wrap)
Node-API offers a way to "wrap" C++ classes and instances so that the class constructor and methods can be called from JavaScript.
  1. The [`napi_define_class`](https://nodejs.org/docs/latest/api/n-api.html#napi_define_class) API defines a JavaScript class with constructor, static properties and methods, and instance properties and methods that correspond to the C++ class.
  2. When JavaScript code invokes the constructor, the constructor callback uses [`napi_wrap`](https://nodejs.org/docs/latest/api/n-api.html#napi_wrap) to wrap a new C++ instance in a JavaScript object, then returns the wrapper object.
  3. When JavaScript code invokes a method or property accessor on the class, the corresponding `napi_callback` C++ function is invoked. For an instance callback, [`napi_unwrap`](https://nodejs.org/docs/latest/api/n-api.html#napi_unwrap) obtains the C++ instance that is the target of the call.


For wrapped objects it may be difficult to distinguish between a function called on a class prototype and a function called on an instance of a class. A common pattern used to address this problem is to save a persistent reference to the class constructor for later `instanceof` checks.
```
napi_value MyClass_constructor = NULL;
status = napi_get_reference_value(env, MyClass::es_constructor, &MyClass_constructor);
assert(napi_ok == status);
bool is_instance = false;
status = napi_instanceof(env, es_this, MyClass_constructor, &is_instance);
assert(napi_ok == status);
if (is_instance) {
  // napi_unwrap() ...
} else {
  // otherwise...
}
copy
```

The reference must be freed once it is no longer needed.
There are occasions where `napi_instanceof()` is insufficient for ensuring that a JavaScript object is a wrapper for a certain native type. This is the case especially when wrapped JavaScript objects are passed back into the addon via static methods rather than as the `this` value of prototype methods. In such cases there is a chance that they may be unwrapped incorrectly.
```
const myAddon = require('./build/Release/my_addon.node');

// `openDatabase()` returns a JavaScript object that wraps a native database
// handle.
const dbHandle = myAddon.openDatabase();

// `query()` returns a JavaScript object that wraps a native query handle.
const queryHandle = myAddon.query(dbHandle, 'Gimme ALL the things!');

// There is an accidental error in the line below. The first parameter to
// `myAddon.queryHasRecords()` should be the database handle (`dbHandle`), not
// the query handle (`query`), so the correct condition for the while-loop
// should be
//
// myAddon.queryHasRecords(dbHandle, queryHandle)
//
while (myAddon.queryHasRecords(queryHandle, dbHandle)) {
  // retrieve records
}
copy
```

In the above example `myAddon.queryHasRecords()` is a method that accepts two arguments. The first is a database handle and the second is a query handle. Internally, it unwraps the first argument and casts the resulting pointer to a native database handle. It then unwraps the second argument and casts the resulting pointer to a query handle. If the arguments are passed in the wrong order, the casts will work, however, there is a good chance that the underlying database operation will fail, or will even cause an invalid memory access.
To ensure that the pointer retrieved from the first argument is indeed a pointer to a database handle and, similarly, that the pointer retrieved from the second argument is indeed a pointer to a query handle, the implementation of `queryHasRecords()` has to perform a type validation. Retaining the JavaScript class constructor from which the database handle was instantiated and the constructor from which the query handle was instantiated in `napi_ref`s can help, because `napi_instanceof()` can then be used to ensure that the instances passed into `queryHashRecords()` are indeed of the correct type.
Unfortunately, `napi_instanceof()` does not protect against prototype manipulation. For example, the prototype of the database handle instance can be set to the prototype of the constructor for query handle instances. In this case, the database handle instance can appear as a query handle instance, and it will pass the `napi_instanceof()` test for a query handle instance, while still containing a pointer to a database handle.
To this end, Node-API provides type-tagging capabilities.
A type tag is a 128-bit integer unique to the addon. Node-API provides the `napi_type_tag` structure for storing a type tag. When such a value is passed along with a JavaScript object or [external](https://nodejs.org/docs/latest/api/n-api.html#napi_create_external) stored in a `napi_value` to `napi_type_tag_object()`, the JavaScript object will be "marked" with the type tag. The "mark" is invisible on the JavaScript side. When a JavaScript object arrives into a native binding, `napi_check_object_type_tag()` can be used along with the original type tag to determine whether the JavaScript object was previously "marked" with the type tag. This creates a type-checking capability of a higher fidelity than `napi_instanceof()` can provide, because such type- tagging survives prototype manipulation and addon unloading/reloading.
Continuing the above example, the following skeleton addon implementation illustrates the use of `napi_type_tag_object()` and `napi_check_object_type_tag()`.
```
// This value is the type tag for a database handle. The command
//
//   uuidgen | sed -r -e 's/-//g' -e 's/(.{16})(.*)/0x\1, 0x\2/'
//
// can be used to obtain the two values with which to initialize the structure.
static const napi_type_tag DatabaseHandleTypeTag = {
  0x1edf75a38336451d, 0xa5ed9ce2e4c00c38
};

// This value is the type tag for a query handle.
static const napi_type_tag QueryHandleTypeTag = {
  0x9c73317f9fad44a3, 0x93c3920bf3b0ad6a
};

static napi_value
openDatabase(napi_env env, napi_callback_info info) {
  napi_status status;
  napi_value result;

  // Perform the underlying action which results in a database handle.
  DatabaseHandle* dbHandle = open_database();

  // Create a new, empty JS object.
  status = napi_create_object(env, &result);
  if (status != napi_ok) return NULL;

  // Tag the object to indicate that it holds a pointer to a `DatabaseHandle`.
  status = napi_type_tag_object(env, result, &DatabaseHandleTypeTag);
  if (status != napi_ok) return NULL;

  // Store the pointer to the `DatabaseHandle` structure inside the JS object.
  status = napi_wrap(env, result, dbHandle, NULL, NULL, NULL);
  if (status != napi_ok) return NULL;

  return result;
}

// Later when we receive a JavaScript object purporting to be a database handle
// we can use `napi_check_object_type_tag()` to ensure that it is indeed such a
// handle.

static napi_value
query(napi_env env, napi_callback_info info) {
  napi_status status;
  size_t argc = 2;
  napi_value argv[2];
  bool is_db_handle;

  status = napi_get_cb_info(env, info, &argc, argv, NULL, NULL);
  if (status != napi_ok) return NULL;

  // Check that the object passed as the first parameter has the previously
  // applied tag.
  status = napi_check_object_type_tag(env,
                                      argv[0],
                                      &DatabaseHandleTypeTag,
                                      &is_db_handle);
  if (status != napi_ok) return NULL;

  // Throw a `TypeError` if it doesn't.
  if (!is_db_handle) {
    // Throw a TypeError.
    return NULL;
  }
}
copy
```

####  `napi_define_class`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-define-class)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_define_class(napi_env env,
                              const char* utf8name,
                              size_t length,
                              napi_callback constructor,
                              void* data,
                              size_t property_count,
                              const napi_property_descriptor* properties,
                              napi_value* result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] utf8name`: Name of the JavaScript constructor function. For clarity, it is recommended to use the C++ class name when wrapping a C++ class.
  * `[in] length`: The length of the `utf8name` in bytes, or `NAPI_AUTO_LENGTH` if it is null-terminated.
  * `[in] constructor`: Callback function that handles constructing instances of the class. When wrapping a C++ class, this method must be a static member with the [`napi_callback`](https://nodejs.org/docs/latest/api/n-api.html#napi_callback) signature. A C++ class constructor cannot be used. [`napi_callback`](https://nodejs.org/docs/latest/api/n-api.html#napi_callback) provides more details.
  * `[in] data`: Optional data to be passed to the constructor callback as the `data` property of the callback info.
  * `[in] property_count`: Number of items in the `properties` array argument.
  * `[in] properties`: Array of property descriptors describing static and instance data properties, accessors, and methods on the class See `napi_property_descriptor`.
  * `[out] result`: A `napi_value` representing the constructor function for the class.


Returns `napi_ok` if the API succeeded.
Defines a JavaScript class, including:
  * A JavaScript constructor function that has the class name. When wrapping a corresponding C++ class, the callback passed via `constructor` can be used to instantiate a new C++ class instance, which can then be placed inside the JavaScript object instance being constructed using [`napi_wrap`](https://nodejs.org/docs/latest/api/n-api.html#napi_wrap).
  * Properties on the constructor function whose implementation can call corresponding _static_ data properties, accessors, and methods of the C++ class (defined by property descriptors with the `napi_static` attribute).
  * Properties on the constructor function's `prototype` object. When wrapping a C++ class, _non-static_ data properties, accessors, and methods of the C++ class can be called from the static functions given in the property descriptors without the `napi_static` attribute after retrieving the C++ class instance placed inside the JavaScript object instance by using [`napi_unwrap`](https://nodejs.org/docs/latest/api/n-api.html#napi_unwrap).


When wrapping a C++ class, the C++ constructor callback passed via `constructor` should be a static method on the class that calls the actual class constructor, then wraps the new C++ instance in a JavaScript object, and returns the wrapper object. See [`napi_wrap`](https://nodejs.org/docs/latest/api/n-api.html#napi_wrap) for details.
The JavaScript constructor function returned from [`napi_define_class`](https://nodejs.org/docs/latest/api/n-api.html#napi_define_class) is often saved and used later to construct new instances of the class from native code, and/or to check whether provided values are instances of the class. In that case, to prevent the function value from being garbage-collected, a strong persistent reference to it can be created using [`napi_create_reference`](https://nodejs.org/docs/latest/api/n-api.html#napi_create_reference), ensuring that the reference count is kept >= 1.
Any non-`NULL` data which is passed to this API via the `data` parameter or via the `data` field of the `napi_property_descriptor` array items can be associated with the resulting JavaScript constructor (which is returned in the `result` parameter) and freed whenever the class is garbage-collected by passing both the JavaScript function and the data to [`napi_add_finalizer`](https://nodejs.org/docs/latest/api/n-api.html#napi_add_finalizer).
####  `napi_wrap`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-wrap)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_wrap(napi_env env,
                      napi_value js_object,
                      void* native_object,
                      napi_finalize finalize_cb,
                      void* finalize_hint,
                      napi_ref* result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] js_object`: The JavaScript object that will be the wrapper for the native object.
  * `[in] native_object`: The native instance that will be wrapped in the JavaScript object.
  * `[in] finalize_cb`: Optional native callback that can be used to free the native instance when the JavaScript object has been garbage-collected. [`napi_finalize`](https://nodejs.org/docs/latest/api/n-api.html#napi_finalize) provides more details.
  * `[in] finalize_hint`: Optional contextual hint that is passed to the finalize callback.
  * `[out] result`: Optional reference to the wrapped object.


Returns `napi_ok` if the API succeeded.
Wraps a native instance in a JavaScript object. The native instance can be retrieved later using `napi_unwrap()`.
When JavaScript code invokes a constructor for a class that was defined using `napi_define_class()`, the `napi_callback` for the constructor is invoked. After constructing an instance of the native class, the callback must then call `napi_wrap()` to wrap the newly constructed instance in the already-created JavaScript object that is the `this` argument to the constructor callback. (That `this` object was created from the constructor function's `prototype`, so it already has definitions of all the instance properties and methods.)
Typically when wrapping a class instance, a finalize callback should be provided that simply deletes the native instance that is received as the `data` argument to the finalize callback.
The optional returned reference is initially a weak reference, meaning it has a reference count of 0. Typically this reference count would be incremented temporarily during async operations that require the instance to remain valid.
_Caution_ : The optional returned reference (if obtained) should be deleted via [`napi_delete_reference`](https://nodejs.org/docs/latest/api/n-api.html#napi_delete_reference) ONLY in response to the finalize callback invocation. If it is deleted before then, then the finalize callback may never be invoked. Therefore, when obtaining a reference a finalize callback is also required in order to enable correct disposal of the reference.
Finalizer callbacks may be deferred, leaving a window where the object has been garbage collected (and the weak reference is invalid) but the finalizer hasn't been called yet. When using `napi_get_reference_value()` on weak references returned by `napi_wrap()`, you should still handle an empty result.
Calling `napi_wrap()` a second time on an object will return an error. To associate another native instance with the object, use `napi_remove_wrap()` first.
####  `napi_unwrap`[#](https://nodejs.org/docs/latest/api/n-api.html#napi-unwrap)
Added in: v8.0.0**N-API Version:** 1
```
napi_status napi_unwrap(napi_env env,
                        napi_value js_object,
                        void** result);
copy
```

  * `[in] env`: The environment that the API is invoked under.
  * `[in] js_object`: The object associated with the native instance.
  * `[out] result`: Pointer to the wrapped native instance.


Returns `napi_ok` if the API succeeded.
Retrieves a native instance that was previously wrapped in a JavaScript object using `napi_wrap()`.
When JavaScript code invokes a method or property accessor on the class, the corresponding `napi_callback` is invoked. If the callback is for an instance method or accessor, then the `this` argument to the callback is the wrapper object; the wrapped C++ instance that is the target of the call can be obtained then by calling `napi_unwrap()` on the wrapper object.
