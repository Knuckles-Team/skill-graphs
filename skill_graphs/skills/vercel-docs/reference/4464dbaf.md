##  [Edge Runtime supported APIs](https://vercel.com/docs/functions/runtimes/node-js#edge-runtime-supported-apis)[](https://vercel.com/docs/functions/runtimes/node-js#edge-runtime-supported-apis)
The Edge runtime is built on top of the
###  [Supported APIs](https://vercel.com/docs/functions/runtimes/node-js#supported-apis)[](https://vercel.com/docs/functions/runtimes/node-js#supported-apis)
The Edge runtime provides a subset of Web APIs such as
The following tables list the APIs that are available in the Edge runtime.
###  [Network APIs](https://vercel.com/docs/functions/runtimes/node-js#network-apis)[](https://vercel.com/docs/functions/runtimes/node-js#network-apis)
API | Description
---|---
| Fetches a resource
| Represents an HTTP request
| Represents an HTTP response
| Represents HTTP headers
| Represents form data
| Represents a file
| Represents a blob
| Represents URL search parameters
| Represents a blob
| Represents an event
| Represents an object that can handle events
| Represents an event that is sent to the global scope of a script when a JavaScript Promise is rejected
###  [Encoding APIs](https://vercel.com/docs/functions/runtimes/node-js#encoding-apis)[](https://vercel.com/docs/functions/runtimes/node-js#encoding-apis)
API | Description
---|---
| Encodes a string into a Uint8Array
| Decodes a Uint8Array into a string
| Decodes a base-64 encoded string
| Encodes a string in base-64
###  [Stream APIs](https://vercel.com/docs/functions/runtimes/node-js#stream-apis)[](https://vercel.com/docs/functions/runtimes/node-js#stream-apis)
API | Description
---|---
| Represents a readable stream
| Represents a writable stream
| Represents a writer of a WritableStream
| Represents a transform stream
| Represents a reader of a ReadableStream
| Represents a reader of a ReadableStream
###  [Crypto APIs](https://vercel.com/docs/functions/runtimes/node-js#crypto-apis)[](https://vercel.com/docs/functions/runtimes/node-js#crypto-apis)
API | Description
---|---
| Provides access to the cryptographic functionality of the platform
| Provides access to common cryptographic primitives, like hashing, signing, encryption or decryption
| Represents a cryptographic key
###  [Other Web Standard APIs](https://vercel.com/docs/functions/runtimes/node-js#other-web-standard-apis)[](https://vercel.com/docs/functions/runtimes/node-js#other-web-standard-apis)
API | Description
---|---
| Allows you to abort one or more DOM requests as and when desired
| Represents a signal object that allows you to communicate with a DOM request (such as a
| Represents an error that occurs in the DOM
| Creates a deep copy of a value
| Represents a URL pattern
| Represents an array of values
| Represents a generic, fixed-length raw binary data buffer
| Provides atomic operations as static methods
| Represents a whole number with arbitrary precision
| Represents a typed array of 64-bit signed integers
| Represents a typed array of 64-bit unsigned integers
| Represents a logical entity and can have two values: `true` and `false`
| Cancels a timed, repeating action which was previously established by a call to `setInterval()`
| Cancels a timed, repeating action which was previously established by a call to `setTimeout()`
| Provides access to the browser's debugging console
| Represents a generic view of an `ArrayBuffer`
| Represents a single moment in time in a platform-independent format
| Decodes a Uniform Resource Identifier (URI) previously created by `encodeURI` or by a similar routine
| Decodes a Uniform Resource Identifier (URI) component previously created by `encodeURIComponent` or by a similar routine
| Encodes a Uniform Resource Identifier (URI) by replacing each instance of certain characters by one, two, three, or four escape sequences representing the UTF-8 encoding of the character
| Encodes a Uniform Resource Identifier (URI) component by replacing each instance of certain characters by one, two, three, or four escape sequences representing the UTF-8 encoding of the character
| Represents an error when trying to execute a statement or accessing a property
| Represents an error that occurs regarding the global function `eval()`
| Represents a typed array of 32-bit floating point numbers
| Represents a typed array of 64-bit floating point numbers
| Represents a function
| Represents the mathematical Infinity value
| Represents a typed array of 8-bit signed integers
| Represents a typed array of 16-bit signed integers
| Represents a typed array of 32-bit signed integers
| Provides access to internationalization and localization functionality
| Determines whether a value is a finite number
| Determines whether a value is `NaN` or not
| Provides functionality to convert JavaScript values to and from the JSON format
| Represents a collection of values, where each value may occur only once
| Provides access to mathematical functions and constants
| Represents a numeric value
| Represents the object that is the base of all JavaScript objects
| Parses a string argument and returns a floating point number
| Parses a string argument and returns an integer of the specified radix
| Represents the eventual completion (or failure) of an asynchronous operation, and its resulting value
| Represents an object that is used to define custom behavior for fundamental operations (e.g. property lookup, assignment, enumeration, function invocation, etc)
| Represents an error when a value is not in the set or range of allowed values
| Represents an error when a non-existent variable is referenced
| Provides methods for interceptable JavaScript operations
| Represents a regular expression, allowing you to match combinations of characters
| Represents a collection of values, where each value may occur only once
| Repeatedly calls a function, with a fixed time delay between each call
| Calls a function or evaluates an expression after a specified number of milliseconds
| Represents a generic, fixed-length raw binary data buffer
| Represents a sequence of characters
| Represents a unique and immutable data type that is used as the key of an object property
| Represents an error when trying to interpret syntactically invalid code
| Represents an error when a value is not of the expected type
| Represents a typed array of 8-bit unsigned integers
| Represents a typed array of 8-bit unsigned integers clamped to 0-255
| Represents a typed array of 32-bit unsigned integers
| Represents an error when a global URI handling function was used in a wrong way
| Represents an object providing static methods used for creating object URLs
| Represents a collection of key/value pairs
| Represents a collection of key/value pairs in which the keys are weakly referenced
| Represents a collection of objects in which each object may occur only once
| Provides access to WebAssembly
