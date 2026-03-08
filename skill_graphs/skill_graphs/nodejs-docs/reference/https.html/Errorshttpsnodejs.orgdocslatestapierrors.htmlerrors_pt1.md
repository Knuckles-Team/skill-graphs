## Errors[#](https://nodejs.org/docs/latest/api/errors.html#errors)
Applications running in Node.js will generally experience the following categories of errors:
  * Standard JavaScript errors such as
  * Standard `DOMException`s.
  * System errors triggered by underlying operating system constraints such as attempting to open a file that does not exist or attempting to send data over a closed socket.
  * `AssertionError`s are a special class of error that can be triggered when Node.js detects an exceptional logic violation that should never occur. These are raised typically by the `node:assert` module.
  * User-specified errors triggered by application code.


All JavaScript and system errors raised by Node.js inherit from, or are instances of, the standard JavaScript _at least_ the properties available on that class.
The [`error.message`](https://nodejs.org/docs/latest/api/errors.html#errormessage) property of errors raised by Node.js may be changed in any versions. Use [`error.code`](https://nodejs.org/docs/latest/api/errors.html#errorcode) to identify an error instead. For a `DOMException`, use
### Error propagation and interception[#](https://nodejs.org/docs/latest/api/errors.html#error-propagation-and-interception)
Node.js supports several mechanisms for propagating and handling errors that occur while an application is running. How these errors are reported and handled depends entirely on the type of `Error` and the style of the API that is called.
All JavaScript errors are handled as exceptions that _immediately_ generate and throw an error using the standard JavaScript `throw` mechanism. These are handled using the
```
// Throws with a ReferenceError because z is not defined.
try {
  const m = 1;
  const n = m + z;
} catch (err) {
  // Handle the error here.
}
copy
```

Any use of the JavaScript `throw` mechanism will raise an exception that _must_ be handled or the Node.js process will exit immediately.
With few exceptions, _Synchronous_ APIs (any blocking method that does not return a `callback` function, such as [`fs.readFileSync`](https://nodejs.org/docs/latest/api/fs.html#fsreadfilesyncpath-options)), will use `throw` to report errors.
Errors that occur within _Asynchronous APIs_ may be reported in multiple ways:
  * Some asynchronous methods returns a [`--unhandled-rejections`](https://nodejs.org/docs/latest/api/cli.html#--unhandled-rejectionsmode) flag for how the process will react to an unhandled promise rejection.
```
const fs = require('node:fs/promises');

(async () => {
  let data;
  try {
    data = await fs.readFile('a file that does not exist');
  } catch (err) {
    console.error('There was an error reading the file!', err);
    return;
  }
  // Otherwise handle the data
})();
copy
```

  * Most asynchronous methods that accept a `callback` function will accept an `Error` object passed as the first argument to that function. If that first argument is not `null` and is an instance of `Error`, then an error occurred that should be handled.
```
const fs = require('node:fs');
fs.readFile('a file that does not exist', (err, data) => {
  if (err) {
    console.error('There was an error reading the file!', err);
    return;
  }
  // Otherwise handle the data
});
copy
```

  * When an asynchronous method is called on an object that is an [`EventEmitter`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter), errors can be routed to that object's `'error'` event.
```
const net = require('node:net');
const connection = net.connect('localhost');

// Adding an 'error' event handler to a stream:
connection.on('error', (err) => {
  // If the connection is reset by the server, or if it can't
  // connect at all, or on any sort of error encountered by
  // the connection, the error will be sent here.
  console.error(err);
});

connection.pipe(process.stdout);
copy
```

  * A handful of typically asynchronous methods in the Node.js API may still use the `throw` mechanism to raise exceptions that must be handled using `try…catch`. There is no comprehensive list of such methods; please refer to the documentation of each method to determine the appropriate error handling mechanism required.


The use of the `'error'` event mechanism is most common for [stream-based](https://nodejs.org/docs/latest/api/stream.html) and [event emitter-based](https://nodejs.org/docs/latest/api/events.html#class-eventemitter) APIs, which themselves represent a series of asynchronous operations over time (as opposed to a single operation that may pass or fail).
For _all_ [`EventEmitter`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter) objects, if an `'error'` event handler is not provided, the error will be thrown, causing the Node.js process to report an uncaught exception and crash unless either: a handler has been registered for the [`'uncaughtException'`](https://nodejs.org/docs/latest/api/process.html#event-uncaughtexception) event, or the deprecated [`node:domain`](https://nodejs.org/docs/latest/api/domain.html) module is used.
```
const EventEmitter = require('node:events');
const ee = new EventEmitter();

setImmediate(() => {
  // This will crash the process because no 'error' event
  // handler has been added.
  ee.emit('error', new Error('This will crash'));
});
copy
```

Errors generated in this way _cannot_ be intercepted using `try…catch` as they are thrown _after_ the calling code has already exited.
Developers must refer to the documentation for each method to determine exactly how errors raised by those methods are propagated.
### Class: `Error`[#](https://nodejs.org/docs/latest/api/errors.html#class-error)
A generic JavaScript `Error` objects capture a "stack trace" detailing the point in the code at which the `Error` was instantiated, and may provide a text description of the error.
All errors generated by Node.js, including all system and JavaScript errors, will either be instances of, or inherit from, the `Error` class.
####  `new Error(message[, options])`[#](https://nodejs.org/docs/latest/api/errors.html#new-errormessage-options)
  * `message`
  * `options`
    * `cause`


Creates a new `Error` object and sets the `error.message` property to the provided text message. If an object is passed as `message`, the text message is generated by calling `String(message)`. If the `cause` option is provided, it is assigned to the `error.cause` property. The `error.stack` property will represent the point in the code at which `new Error()` was called. Stack traces are dependent on _synchronous code execution_ , or (b) the number of frames given by the property `Error.stackTraceLimit`, whichever is smaller.
####  `Error.captureStackTrace(targetObject[, constructorOpt])`[#](https://nodejs.org/docs/latest/api/errors.html#errorcapturestacktracetargetobject-constructoropt)
  * `targetObject`
  * `constructorOpt`


Creates a `.stack` property on `targetObject`, which when accessed returns a string representing the location in the code at which `Error.captureStackTrace()` was called.
```
const myObject = {};
Error.captureStackTrace(myObject);
myObject.stack;  // Similar to `new Error().stack`
copy
```

The first line of the trace will be prefixed with `${myObject.name}: ${myObject.message}`.
The optional `constructorOpt` argument accepts a function. If given, all frames above `constructorOpt`, including `constructorOpt`, will be omitted from the generated stack trace.
The `constructorOpt` argument is useful for hiding implementation details of error generation from the user. For instance:
```
function a() {
  b();
}

function b() {
  c();
}

function c() {
  // Create an error without stack trace to avoid calculating the stack trace twice.
  const { stackTraceLimit } = Error;
  Error.stackTraceLimit = 0;
  const error = new Error();
  Error.stackTraceLimit = stackTraceLimit;

  // Capture the stack trace above function b
  Error.captureStackTrace(error, b); // Neither function c, nor b is included in the stack trace
  throw error;
}

a();
copy
```

####  `Error.stackTraceLimit`[#](https://nodejs.org/docs/latest/api/errors.html#errorstacktracelimit)
  * Type:


The `Error.stackTraceLimit` property specifies the number of stack frames collected by a stack trace (whether generated by `new Error().stack` or `Error.captureStackTrace(obj)`).
The default value is `10` but may be set to any valid JavaScript number. Changes will affect any stack trace captured _after_ the value has been changed.
If set to a non-number value, or set to a negative number, stack traces will not capture any frames.
####  `error.cause`[#](https://nodejs.org/docs/latest/api/errors.html#errorcause)
Added in: v16.9.0
  * Type:


If present, the `error.cause` property is the underlying cause of the `Error`. It is used when catching an error and throwing a new one with a different message or code in order to still have access to the original error.
The `error.cause` property is typically set by calling `new Error(message, { cause })`. It is not set by the constructor if the `cause` option is not provided.
This property allows errors to be chained. When serializing `Error` objects, [`util.inspect()`](https://nodejs.org/docs/latest/api/util.html#utilinspectobject-options) recursively serializes `error.cause` if it is set.
```
const cause = new Error('The remote HTTP server responded with a 500 status');
const symptom = new Error('The message failed to send', { cause });

console.log(symptom);
// Prints:
//   Error: The message failed to send
//       at REPL2:1:17
//       at Script.runInThisContext (node:vm:130:12)
//       ... 7 lines matching cause stack trace ...
//       at [_line] [as _line] (node:internal/readline/interface:886:18) {
//     [cause]: Error: The remote HTTP server responded with a 500 status
//         at REPL1:1:15
//         at Script.runInThisContext (node:vm:130:12)
//         at REPLServer.defaultEval (node:repl:574:29)
//         at bound (node:domain:426:15)
//         at REPLServer.runBound [as eval] (node:domain:437:12)
//         at REPLServer.onLine (node:repl:902:10)
//         at REPLServer.emit (node:events:549:35)
//         at REPLServer.emit (node:domain:482:12)
//         at [_onLine] [as _onLine] (node:internal/readline/interface:425:12)
//         at [_line] [as _line] (node:internal/readline/interface:886:18)
copy
```

####  `error.code`[#](https://nodejs.org/docs/latest/api/errors.html#errorcode)
  * Type:


The `error.code` property is a string label that identifies the kind of error. `error.code` is the most stable way to identify an error. It will only change between major versions of Node.js. In contrast, `error.message` strings may change between any versions of Node.js. See [Node.js error codes](https://nodejs.org/docs/latest/api/errors.html#nodejs-error-codes) for details about specific codes.
####  `error.message`[#](https://nodejs.org/docs/latest/api/errors.html#errormessage)
  * Type:


The `error.message` property is the string description of the error as set by calling `new Error(message)`. The `message` passed to the constructor will also appear in the first line of the stack trace of the `Error`, however changing this property after the `Error` object is created _may not_ change the first line of the stack trace (for example, when `error.stack` is read before this property is changed).
```
const err = new Error('The message');
console.error(err.message);
// Prints: The message
copy
```

####  `error.stack`[#](https://nodejs.org/docs/latest/api/errors.html#errorstack)
  * Type:


The `error.stack` property is a string describing the point in the code at which the `Error` was instantiated.
```
Error: Things keep happening!
   at /home/gbusey/file.js:525:2
   at Frobnicator.refrobulate (/home/gbusey/business-logic.js:424:21)
   at Actor.<anonymous> (/home/gbusey/actors.js:400:8)
   at increaseSynergy (/home/gbusey/actors.js:701:6)
copy
```

The first line is formatted as `<error class name>: <error message>`, and is followed by a series of stack frames (each line beginning with "at "). Each frame describes a call site within the code that lead to the error being generated. V8 attempts to display a name for each function (by variable name, function name, or object method name), but occasionally it will not be able to find a suitable name. If V8 cannot determine a name for the function, only location information will be displayed for that frame. Otherwise, the determined function name will be displayed with location information appended in parentheses.
Frames are only generated for JavaScript functions. If, for example, execution synchronously passes through a C++ addon function called `cheetahify` which itself calls a JavaScript function, the frame representing the `cheetahify` call will not be present in the stack traces:
```
const cheetahify = require('./native-binding.node');

function makeFaster() {
  // `cheetahify()` *synchronously* calls speedy.
  cheetahify(function speedy() {
    throw new Error('oh no!');
  });
}

makeFaster();
// will throw:
//   /home/gbusey/file.js:6
//       throw new Error('oh no!');
//           ^
//   Error: oh no!
//       at speedy (/home/gbusey/file.js:6:11)
//       at makeFaster (/home/gbusey/file.js:5:3)
//       at Object.<anonymous> (/home/gbusey/file.js:10:1)
//       at Module._compile (module.js:456:26)
//       at Object.Module._extensions..js (module.js:474:10)
//       at Module.load (module.js:356:32)
//       at Function.Module._load (module.js:312:12)
//       at Function.Module.runMain (module.js:497:10)
//       at startup (node.js:119:16)
//       at node.js:906:3
copy
```

The location information will be one of:
  * `native`, if the frame represents a call internal to V8 (as in `[].forEach`).
  * `plain-filename.js:line:column`, if the frame represents a call internal to Node.js.
  * `/absolute/path/to/file.js:line:column`, if the frame represents a call in a user program (using CommonJS module system), or its dependencies.
  * `<transport-protocol>:///url/to/module/file.mjs:line:column`, if the frame represents a call in a user program (using ES module system), or its dependencies.


The number of frames captured by the stack trace is bounded by the smaller of `Error.stackTraceLimit` or the number of available frames on the current event loop tick.
`error.stack` is a getter/setter for a hidden internal property which is only present on builtin `Error` objects (those for which `error` is not a builtin error object, then the `error.stack` getter will always return `undefined`, and the setter will do nothing. This can occur if the accessor is manually invoked with a `this` value that is not a builtin error object, such as a
### Class: `AssertionError`[#](https://nodejs.org/docs/latest/api/errors.html#class-assertionerror)
  * Extends: [`<errors.Error>`](https://nodejs.org/docs/latest/api/errors.html#class-errorserror)


Indicates the failure of an assertion. For details, see [`Class: assert.AssertionError`](https://nodejs.org/docs/latest/api/assert.html#class-assertassertionerror).
### Class: `RangeError`[#](https://nodejs.org/docs/latest/api/errors.html#class-rangeerror)
  * Extends: [`<errors.Error>`](https://nodejs.org/docs/latest/api/errors.html#class-errorserror)


Indicates that a provided argument was not within the set or range of acceptable values for a function; whether that is a numeric range, or outside the set of options for a given function parameter.
```
require('node:net').connect(-1);
// Throws "RangeError: "port" option should be >= 0 and < 65536: -1"
copy
```

Node.js will generate and throw `RangeError` instances _immediately_ as a form of argument validation.
### Class: `ReferenceError`[#](https://nodejs.org/docs/latest/api/errors.html#class-referenceerror)
  * Extends: [`<errors.Error>`](https://nodejs.org/docs/latest/api/errors.html#class-errorserror)


Indicates that an attempt is being made to access a variable that is not defined. Such errors commonly indicate typos in code, or an otherwise broken program.
While client code may generate and propagate these errors, in practice, only V8 will do so.
```
doesNotExist;
// Throws ReferenceError, doesNotExist is not a variable in this program.
copy
```

Unless an application is dynamically generating and running code, `ReferenceError` instances indicate a bug in the code or its dependencies.
### Class: `SyntaxError`[#](https://nodejs.org/docs/latest/api/errors.html#class-syntaxerror)
  * Extends: [`<errors.Error>`](https://nodejs.org/docs/latest/api/errors.html#class-errorserror)


Indicates that a program is not valid JavaScript. These errors may only be generated and propagated as a result of code evaluation. Code evaluation may happen as a result of `eval`, `Function`, `require`, or [vm](https://nodejs.org/docs/latest/api/vm.html). These errors are almost always indicative of a broken program.
```
try {
  require('node:vm').runInThisContext('binary ! isNotOk');
} catch (err) {
  // 'err' will be a SyntaxError.
}
copy
```

`SyntaxError` instances are unrecoverable in the context that created them – they may only be caught by other contexts.
### Class: `SystemError`[#](https://nodejs.org/docs/latest/api/errors.html#class-systemerror)
  * Extends: [`<errors.Error>`](https://nodejs.org/docs/latest/api/errors.html#class-errorserror)


Node.js generates system errors when exceptions occur within its runtime environment. These usually occur when an application violates an operating system constraint. For example, a system error will occur if an application attempts to read a file that does not exist.
  * `address`
  * `code`
  * `dest`
  * `errno`
  * `info`
  * `message`
  * `path`
  * `port`
  * `syscall`


####  `error.address`[#](https://nodejs.org/docs/latest/api/errors.html#erroraddress)
  * Type:


If present, `error.address` is a string describing the address to which a network connection failed.
####  `error.code`[#](https://nodejs.org/docs/latest/api/errors.html#errorcode-1)
  * Type:


The `error.code` property is a string representing the error code.
####  `error.dest`[#](https://nodejs.org/docs/latest/api/errors.html#errordest)
  * Type:


If present, `error.dest` is the file path destination when reporting a file system error.
####  `error.errno`[#](https://nodejs.org/docs/latest/api/errors.html#errorerrno)
  * Type:


The `error.errno` property is a negative number which corresponds to the error code defined in
On Windows the error number provided by the system will be normalized by libuv.
To get the string representation of the error code, use [`util.getSystemErrorName(error.errno)`](https://nodejs.org/docs/latest/api/util.html#utilgetsystemerrornameerr).
####  `error.info`[#](https://nodejs.org/docs/latest/api/errors.html#errorinfo)
  * Type:


If present, `error.info` is an object with details about the error condition.
####  `error.message`[#](https://nodejs.org/docs/latest/api/errors.html#errormessage-1)
  * Type:


`error.message` is a system-provided human-readable description of the error.
####  `error.path`[#](https://nodejs.org/docs/latest/api/errors.html#errorpath)
  * Type:


If present, `error.path` is a string containing a relevant invalid pathname.
####  `error.port`[#](https://nodejs.org/docs/latest/api/errors.html#errorport)
  * Type:


If present, `error.port` is the network connection port that is not available.
####  `error.syscall`[#](https://nodejs.org/docs/latest/api/errors.html#errorsyscall)
  * Type:


The `error.syscall` property is a string describing the
#### Common system errors[#](https://nodejs.org/docs/latest/api/errors.html#common-system-errors)
This is a list of system errors commonly-encountered when writing a Node.js program. For a comprehensive list, see the
  * `EACCES` (Permission denied): An attempt was made to access a file in a way forbidden by its file access permissions.
  * `EADDRINUSE` (Address already in use): An attempt to bind a server ([`net`](https://nodejs.org/docs/latest/api/net.html), [`http`](https://nodejs.org/docs/latest/api/http.html), or [`https`](https://nodejs.org/docs/latest/api/https.html)) to a local address failed due to another server on the local system already occupying that address.
  * `ECONNREFUSED` (Connection refused): No connection could be made because the target machine actively refused it. This usually results from trying to connect to a service that is inactive on the foreign host.
  * `ECONNRESET` (Connection reset by peer): A connection was forcibly closed by a peer. This normally results from a loss of the connection on the remote socket due to a timeout or reboot. Commonly encountered via the [`http`](https://nodejs.org/docs/latest/api/http.html) and [`net`](https://nodejs.org/docs/latest/api/net.html) modules.
  * `EEXIST` (File exists): An existing file was the target of an operation that required that the target not exist.
  * `EISDIR` (Is a directory): An operation expected a file, but the given pathname was a directory.
  * `EMFILE` (Too many open files in system): Maximum number of `ulimit -n 2048` in the same shell that will run the Node.js process.
  * `ENOENT` (No such file or directory): Commonly raised by [`fs`](https://nodejs.org/docs/latest/api/fs.html) operations to indicate that a component of the specified pathname does not exist. No entity (file or directory) could be found by the given path.
  * `ENOTDIR` (Not a directory): A component of the given pathname existed, but was not a directory as expected. Commonly raised by [`fs.readdir`](https://nodejs.org/docs/latest/api/fs.html#fsreaddirpath-options-callback).
  * `ENOTEMPTY` (Directory not empty): A directory with entries was the target of an operation that requires an empty directory, usually [`fs.unlink`](https://nodejs.org/docs/latest/api/fs.html#fsunlinkpath-callback).
  * `ENOTFOUND` (DNS lookup failed): Indicates a DNS failure of either `EAI_NODATA` or `EAI_NONAME`. This is not a standard POSIX error.
  * `EPERM` (Operation not permitted): An attempt was made to perform an operation that requires elevated privileges.
  * `EPIPE` (Broken pipe): A write on a pipe, socket, or FIFO for which there is no process to read the data. Commonly encountered at the [`net`](https://nodejs.org/docs/latest/api/net.html) and [`http`](https://nodejs.org/docs/latest/api/http.html) layers, indicative that the remote side of the stream being written to has been closed.
  * `ETIMEDOUT` (Operation timed out): A connect or send request failed because the connected party did not properly respond after a period of time. Usually encountered by [`http`](https://nodejs.org/docs/latest/api/http.html) or [`net`](https://nodejs.org/docs/latest/api/net.html). Often a sign that a `socket.end()` was not properly called.


### Class: `TypeError`[#](https://nodejs.org/docs/latest/api/errors.html#class-typeerror)
  * Extends [`<errors.Error>`](https://nodejs.org/docs/latest/api/errors.html#class-errorserror)


Indicates that a provided argument is not an allowable type. For example, passing a function to a parameter which expects a string would be a `TypeError`.
```
require('node:url').parse(() => { });
// Throws TypeError, since it expected a string.
copy
```

Node.js will generate and throw `TypeError` instances _immediately_ as a form of argument validation.
### Exceptions vs. errors[#](https://nodejs.org/docs/latest/api/errors.html#exceptions-vs-errors)
A JavaScript exception is a value that is thrown as a result of an invalid operation or as the target of a `throw` statement. While it is not required that these values are instances of `Error` or classes which inherit from `Error`, all exceptions thrown by Node.js or the JavaScript runtime _will_ be instances of `Error`.
Some exceptions are _unrecoverable_ at the JavaScript layer. Such exceptions will _always_ cause the Node.js process to crash. Examples include `assert()` checks or `abort()` calls in the C++ layer.
### OpenSSL errors[#](https://nodejs.org/docs/latest/api/errors.html#openssl-errors)
Errors originating in `crypto` or `tls` are of class `Error`, and in addition to the standard `.code` and `.message` properties, may have some additional OpenSSL-specific properties.
####  `error.opensslErrorStack`[#](https://nodejs.org/docs/latest/api/errors.html#erroropensslerrorstack)
An array of errors that can give context to where in the OpenSSL library an error originates from.
####  `error.function`[#](https://nodejs.org/docs/latest/api/errors.html#errorfunction)
The OpenSSL function the error originates in.
####  `error.library`[#](https://nodejs.org/docs/latest/api/errors.html#errorlibrary)
The OpenSSL library the error originates in.
####  `error.reason`[#](https://nodejs.org/docs/latest/api/errors.html#errorreason)
A human-readable string describing the reason for the error.
### Node.js error codes[#](https://nodejs.org/docs/latest/api/errors.html#nodejs-error-codes)
####  `ABORT_ERR`[#](https://nodejs.org/docs/latest/api/errors.html#abort-err)
Added in: v15.0.0
Used when an operation has been aborted (typically using an `AbortController`).
APIs _not_ using `AbortSignal`s typically do not raise an error with this code.
This code does not use the regular `ERR_*` convention Node.js errors use in order to be compatible with the web platform's `AbortError`.
####  `ERR_ACCESS_DENIED`[#](https://nodejs.org/docs/latest/api/errors.html#err-access-denied)
A special type of error that is triggered whenever Node.js tries to get access to a resource restricted by the [Permission Model](https://nodejs.org/docs/latest/api/permissions.html#permission-model).
