# Node.js v25.8.0 documentation
  * Node.js v25.8.0
  * [](https://nodejs.org/docs/latest/api/repl.html#toc-picker)
    * [REPL](https://nodejs.org/docs/latest/api/repl.html#repl)
      * [Design and features](https://nodejs.org/docs/latest/api/repl.html#design-and-features)
        * [Commands and special keys](https://nodejs.org/docs/latest/api/repl.html#commands-and-special-keys)
        * [Default evaluation](https://nodejs.org/docs/latest/api/repl.html#default-evaluation)
          * [JavaScript expressions](https://nodejs.org/docs/latest/api/repl.html#javascript-expressions)
          * [Global and local scope](https://nodejs.org/docs/latest/api/repl.html#global-and-local-scope)
          * [Accessing core Node.js modules](https://nodejs.org/docs/latest/api/repl.html#accessing-core-nodejs-modules)
          * [Global uncaught exceptions](https://nodejs.org/docs/latest/api/repl.html#global-uncaught-exceptions)
          * [Assignment of the `_` (underscore) variable](https://nodejs.org/docs/latest/api/repl.html#assignment-of-the-underscore-variable)
          * [`await` keyword](https://nodejs.org/docs/latest/api/repl.html#await-keyword)
        * [Reverse-i-search](https://nodejs.org/docs/latest/api/repl.html#reverse-i-search)
        * [Custom evaluation functions](https://nodejs.org/docs/latest/api/repl.html#custom-evaluation-functions)
          * [Recoverable errors](https://nodejs.org/docs/latest/api/repl.html#recoverable-errors)
        * [Customizing REPL output](https://nodejs.org/docs/latest/api/repl.html#customizing-repl-output)
      * [Class: `REPLServer`](https://nodejs.org/docs/latest/api/repl.html#class-replserver)
        * [Event: `'exit'`](https://nodejs.org/docs/latest/api/repl.html#event-exit)
        * [Event: `'reset'`](https://nodejs.org/docs/latest/api/repl.html#event-reset)
        * [`replServer.defineCommand(keyword, cmd)`](https://nodejs.org/docs/latest/api/repl.html#replserverdefinecommandkeyword-cmd)
        * [`replServer.displayPrompt([preserveCursor])`](https://nodejs.org/docs/latest/api/repl.html#replserverdisplaypromptpreservecursor)
        * [`replServer.clearBufferedCommand()`](https://nodejs.org/docs/latest/api/repl.html#replserverclearbufferedcommand)
        * [`replServer.setupHistory(historyConfig, callback)`](https://nodejs.org/docs/latest/api/repl.html#replserversetuphistoryhistoryconfig-callback)
      * [`repl.builtinModules`](https://nodejs.org/docs/latest/api/repl.html#replbuiltinmodules)
      * [`repl.start([options])`](https://nodejs.org/docs/latest/api/repl.html#replstartoptions)
      * [The Node.js REPL](https://nodejs.org/docs/latest/api/repl.html#the-nodejs-repl)
        * [Environment variable options](https://nodejs.org/docs/latest/api/repl.html#environment-variable-options)
        * [Persistent history](https://nodejs.org/docs/latest/api/repl.html#persistent-history)
        * [Using the Node.js REPL with advanced line-editors](https://nodejs.org/docs/latest/api/repl.html#using-the-nodejs-repl-with-advanced-line-editors)
        * [Starting multiple REPL instances in the same process](https://nodejs.org/docs/latest/api/repl.html#starting-multiple-repl-instances-in-the-same-process)
        * [Examples](https://nodejs.org/docs/latest/api/repl.html#examples)
          * [Full-featured "terminal" REPL over `net.Server` and `net.Socket`](https://nodejs.org/docs/latest/api/repl.html#full-featured-terminal-repl-over-netserver-and-netsocket)
          * [REPL over `curl`](https://nodejs.org/docs/latest/api/repl.html#repl-over-curl)
  * [](https://nodejs.org/docs/latest/api/repl.html#gtoc-picker)
    * [Index](https://nodejs.org/docs/latest/api/index.html)
* * *
    * [About this documentation](https://nodejs.org/docs/latest/api/documentation.html)
    * [Usage and example](https://nodejs.org/docs/latest/api/synopsis.html)
    * [Assertion testing](https://nodejs.org/docs/latest/api/assert.html)
    * [Asynchronous context tracking](https://nodejs.org/docs/latest/api/async_context.html)
    * [Async hooks](https://nodejs.org/docs/latest/api/async_hooks.html)
    * [Buffer](https://nodejs.org/docs/latest/api/buffer.html)
    * [C++ addons](https://nodejs.org/docs/latest/api/addons.html)
    * [C/C++ addons with Node-API](https://nodejs.org/docs/latest/api/n-api.html)
    * [C++ embedder API](https://nodejs.org/docs/latest/api/embedding.html)
    * [Child processes](https://nodejs.org/docs/latest/api/child_process.html)
    * [Cluster](https://nodejs.org/docs/latest/api/cluster.html)
    * [Command-line options](https://nodejs.org/docs/latest/api/cli.html)
    * [Console](https://nodejs.org/docs/latest/api/console.html)
    * [Crypto](https://nodejs.org/docs/latest/api/crypto.html)
    * [Debugger](https://nodejs.org/docs/latest/api/debugger.html)
    * [Deprecated APIs](https://nodejs.org/docs/latest/api/deprecations.html)
    * [Diagnostics Channel](https://nodejs.org/docs/latest/api/diagnostics_channel.html)
    * [DNS](https://nodejs.org/docs/latest/api/dns.html)
    * [Domain](https://nodejs.org/docs/latest/api/domain.html)
    * [Environment Variables](https://nodejs.org/docs/latest/api/environment_variables.html)
    * [Errors](https://nodejs.org/docs/latest/api/errors.html)
    * [Events](https://nodejs.org/docs/latest/api/events.html)
    * [File system](https://nodejs.org/docs/latest/api/fs.html)
    * [Globals](https://nodejs.org/docs/latest/api/globals.html)
    * [HTTP](https://nodejs.org/docs/latest/api/http.html)
    * [HTTP/2](https://nodejs.org/docs/latest/api/http2.html)
    * [HTTPS](https://nodejs.org/docs/latest/api/https.html)
    * [Inspector](https://nodejs.org/docs/latest/api/inspector.html)
    * [Internationalization](https://nodejs.org/docs/latest/api/intl.html)
    * [Modules: CommonJS modules](https://nodejs.org/docs/latest/api/modules.html)
    * [Modules: ECMAScript modules](https://nodejs.org/docs/latest/api/esm.html)
    * [Modules: `node:module` API](https://nodejs.org/docs/latest/api/module.html)
    * [Modules: Packages](https://nodejs.org/docs/latest/api/packages.html)
    * [Modules: TypeScript](https://nodejs.org/docs/latest/api/typescript.html)
    * [Net](https://nodejs.org/docs/latest/api/net.html)
    * [OS](https://nodejs.org/docs/latest/api/os.html)
    * [Path](https://nodejs.org/docs/latest/api/path.html)
    * [Performance hooks](https://nodejs.org/docs/latest/api/perf_hooks.html)
    * [Permissions](https://nodejs.org/docs/latest/api/permissions.html)
    * [Process](https://nodejs.org/docs/latest/api/process.html)
    * [Punycode](https://nodejs.org/docs/latest/api/punycode.html)
    * [Query strings](https://nodejs.org/docs/latest/api/querystring.html)
    * [Readline](https://nodejs.org/docs/latest/api/readline.html)
    * [REPL](https://nodejs.org/docs/latest/api/repl.html)
    * [Report](https://nodejs.org/docs/latest/api/report.html)
    * [Single executable applications](https://nodejs.org/docs/latest/api/single-executable-applications.html)
    * [SQLite](https://nodejs.org/docs/latest/api/sqlite.html)
    * [Stream](https://nodejs.org/docs/latest/api/stream.html)
    * [String decoder](https://nodejs.org/docs/latest/api/string_decoder.html)
    * [Test runner](https://nodejs.org/docs/latest/api/test.html)
    * [Timers](https://nodejs.org/docs/latest/api/timers.html)
    * [TLS/SSL](https://nodejs.org/docs/latest/api/tls.html)
    * [Trace events](https://nodejs.org/docs/latest/api/tracing.html)
    * [TTY](https://nodejs.org/docs/latest/api/tty.html)
    * [UDP/datagram](https://nodejs.org/docs/latest/api/dgram.html)
    * [URL](https://nodejs.org/docs/latest/api/url.html)
    * [Utilities](https://nodejs.org/docs/latest/api/util.html)
    * [V8](https://nodejs.org/docs/latest/api/v8.html)
    * [VM](https://nodejs.org/docs/latest/api/vm.html)
    * [WASI](https://nodejs.org/docs/latest/api/wasi.html)
    * [Web Crypto API](https://nodejs.org/docs/latest/api/webcrypto.html)
    * [Web Streams API](https://nodejs.org/docs/latest/api/webstreams.html)
    * [Worker threads](https://nodejs.org/docs/latest/api/worker_threads.html)
    * [Zlib](https://nodejs.org/docs/latest/api/zlib.html)
  * [](https://nodejs.org/docs/latest/api/repl.html#alt-docs)
    1. [25.x ](https://nodejs.org/docs/latest-v25.x/api/repl.html)
    2. [24.x ](https://nodejs.org/docs/latest-v24.x/api/repl.html)
    3. [23.x ](https://nodejs.org/docs/latest-v23.x/api/repl.html)
    4. [22.x **LTS**](https://nodejs.org/docs/latest-v22.x/api/repl.html)
    5. [21.x ](https://nodejs.org/docs/latest-v21.x/api/repl.html)
    6. [20.x **LTS**](https://nodejs.org/docs/latest-v20.x/api/repl.html)
    7. [19.x ](https://nodejs.org/docs/latest-v19.x/api/repl.html)
    8. [18.x ](https://nodejs.org/docs/latest-v18.x/api/repl.html)
    9. [17.x ](https://nodejs.org/docs/latest-v17.x/api/repl.html)
    10. [16.x ](https://nodejs.org/docs/latest-v16.x/api/repl.html)
    11. [15.x ](https://nodejs.org/docs/latest-v15.x/api/repl.html)
    12. [14.x ](https://nodejs.org/docs/latest-v14.x/api/repl.html)
    13. [13.x ](https://nodejs.org/docs/latest-v13.x/api/repl.html)
    14. [12.x ](https://nodejs.org/docs/latest-v12.x/api/repl.html)
    15. [11.x ](https://nodejs.org/docs/latest-v11.x/api/repl.html)
    16. [10.x ](https://nodejs.org/docs/latest-v10.x/api/repl.html)
    17. [9.x ](https://nodejs.org/docs/latest-v9.x/api/repl.html)
    18. [8.x ](https://nodejs.org/docs/latest-v8.x/api/repl.html)
    19. [7.x ](https://nodejs.org/docs/latest-v7.x/api/repl.html)
    20. [6.x ](https://nodejs.org/docs/latest-v6.x/api/repl.html)
    21. [5.x ](https://nodejs.org/docs/latest-v5.x/api/repl.html)
    22. [4.x ](https://nodejs.org/docs/latest-v4.x/api/repl.html)
    23. [0.12.x ](https://nodejs.org/docs/latest-v0.12.x/api/repl.html)
    24. [0.10.x ](https://nodejs.org/docs/latest-v0.10.x/api/repl.html)
  * [ ](https://nodejs.org/docs/latest/api/repl.html#options-picker)
    * [View on single page](https://nodejs.org/docs/latest/api/all.html)
    * [View as JSON](https://nodejs.org/docs/latest/api/repl.json)


* * *
Table of contents
  * [REPL](https://nodejs.org/docs/latest/api/repl.html#repl)
    * [Design and features](https://nodejs.org/docs/latest/api/repl.html#design-and-features)
      * [Commands and special keys](https://nodejs.org/docs/latest/api/repl.html#commands-and-special-keys)
      * [Default evaluation](https://nodejs.org/docs/latest/api/repl.html#default-evaluation)
        * [JavaScript expressions](https://nodejs.org/docs/latest/api/repl.html#javascript-expressions)
        * [Global and local scope](https://nodejs.org/docs/latest/api/repl.html#global-and-local-scope)
        * [Accessing core Node.js modules](https://nodejs.org/docs/latest/api/repl.html#accessing-core-nodejs-modules)
        * [Global uncaught exceptions](https://nodejs.org/docs/latest/api/repl.html#global-uncaught-exceptions)
        * [Assignment of the `_` (underscore) variable](https://nodejs.org/docs/latest/api/repl.html#assignment-of-the-underscore-variable)
        * [`await` keyword](https://nodejs.org/docs/latest/api/repl.html#await-keyword)
      * [Reverse-i-search](https://nodejs.org/docs/latest/api/repl.html#reverse-i-search)
      * [Custom evaluation functions](https://nodejs.org/docs/latest/api/repl.html#custom-evaluation-functions)
        * [Recoverable errors](https://nodejs.org/docs/latest/api/repl.html#recoverable-errors)
      * [Customizing REPL output](https://nodejs.org/docs/latest/api/repl.html#customizing-repl-output)
    * [Class: `REPLServer`](https://nodejs.org/docs/latest/api/repl.html#class-replserver)
      * [Event: `'exit'`](https://nodejs.org/docs/latest/api/repl.html#event-exit)
      * [Event: `'reset'`](https://nodejs.org/docs/latest/api/repl.html#event-reset)
      * [`replServer.defineCommand(keyword, cmd)`](https://nodejs.org/docs/latest/api/repl.html#replserverdefinecommandkeyword-cmd)
      * [`replServer.displayPrompt([preserveCursor])`](https://nodejs.org/docs/latest/api/repl.html#replserverdisplaypromptpreservecursor)
      * [`replServer.clearBufferedCommand()`](https://nodejs.org/docs/latest/api/repl.html#replserverclearbufferedcommand)
      * [`replServer.setupHistory(historyConfig, callback)`](https://nodejs.org/docs/latest/api/repl.html#replserversetuphistoryhistoryconfig-callback)
    * [`repl.builtinModules`](https://nodejs.org/docs/latest/api/repl.html#replbuiltinmodules)
    * [`repl.start([options])`](https://nodejs.org/docs/latest/api/repl.html#replstartoptions)
    * [The Node.js REPL](https://nodejs.org/docs/latest/api/repl.html#the-nodejs-repl)
      * [Environment variable options](https://nodejs.org/docs/latest/api/repl.html#environment-variable-options)
      * [Persistent history](https://nodejs.org/docs/latest/api/repl.html#persistent-history)
      * [Using the Node.js REPL with advanced line-editors](https://nodejs.org/docs/latest/api/repl.html#using-the-nodejs-repl-with-advanced-line-editors)
      * [Starting multiple REPL instances in the same process](https://nodejs.org/docs/latest/api/repl.html#starting-multiple-repl-instances-in-the-same-process)
      * [Examples](https://nodejs.org/docs/latest/api/repl.html#examples)
        * [Full-featured "terminal" REPL over `net.Server` and `net.Socket`](https://nodejs.org/docs/latest/api/repl.html#full-featured-terminal-repl-over-netserver-and-netsocket)
        * [REPL over `curl`](https://nodejs.org/docs/latest/api/repl.html#repl-over-curl)


## REPL[#](https://nodejs.org/docs/latest/api/repl.html#repl)
**Source Code:**
[Stability: 2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Stable
The `node:repl` module provides a Read-Eval-Print-Loop (REPL) implementation that is available both as a standalone program or includible in other applications. It can be accessed using:
```
import repl from 'node:repl';
const repl = require('node:repl');
copy
```

### Design and features[#](https://nodejs.org/docs/latest/api/repl.html#design-and-features)
The `node:repl` module exports the [`repl.REPLServer`](https://nodejs.org/docs/latest/api/repl.html#class-replserver) class. While running, instances of [`repl.REPLServer`](https://nodejs.org/docs/latest/api/repl.html#class-replserver) will accept individual lines of user input, evaluate those according to a user-defined evaluation function, then output the result. Input and output may be from `stdin` and `stdout`, respectively, or may be connected to any Node.js [stream](https://nodejs.org/docs/latest/api/stream.html).
Instances of [`repl.REPLServer`](https://nodejs.org/docs/latest/api/repl.html#class-replserver) support automatic completion of inputs, completion preview, simplistic Emacs-style line editing, multi-line inputs,
#### Commands and special keys[#](https://nodejs.org/docs/latest/api/repl.html#commands-and-special-keys)
The following special commands are supported by all REPL instances:
  * `.break`: When in the process of inputting a multi-line expression, enter the `.break` command (or press `Ctrl`+`C`) to abort further input or processing of that expression.
  * `.clear`: Resets the REPL `context` to an empty object and clears any multi-line expression being input.
  * `.exit`: Close the I/O stream, causing the REPL to exit.
  * `.help`: Show this list of special commands.
  * `.save`: Save the current REPL session to a file: `> .save ./file/to/save.js`
  * `.load`: Load a file into the current REPL session. `> .load ./file/to/load.js`
  * `.editor`: Enter editor mode (`Ctrl`+`D` to finish, `Ctrl`+`C` to cancel).

```
> .editor
// Entering editor mode (^D to finish, ^C to cancel)
function welcome(name) {
  return `Hello ${name}!`;
}

welcome('Node.js User');

// ^D
'Hello Node.js User!'
>
copy
```

The following key combinations in the REPL have these special effects:
  * `Ctrl`+`C`: When pressed once, has the same effect as the `.break` command. When pressed twice on a blank line, has the same effect as the `.exit` command.
  * `Ctrl`+`D`: Has the same effect as the `.exit` command.
  * `Tab`: When pressed on a blank line, displays global and local (scope) variables. When pressed while entering other input, displays relevant autocompletion options.


For key bindings related to the reverse-i-search, see [`reverse-i-search`](https://nodejs.org/docs/latest/api/repl.html#reverse-i-search). For all other key bindings, see [TTY keybindings](https://nodejs.org/docs/latest/api/readline.html#tty-keybindings).
#### Default evaluation[#](https://nodejs.org/docs/latest/api/repl.html#default-evaluation)
By default, all instances of [`repl.REPLServer`](https://nodejs.org/docs/latest/api/repl.html#class-replserver) use an evaluation function that evaluates JavaScript expressions and provides access to Node.js built-in modules. This default behavior can be overridden by passing in an alternative evaluation function when the [`repl.REPLServer`](https://nodejs.org/docs/latest/api/repl.html#class-replserver) instance is created.
##### JavaScript expressions[#](https://nodejs.org/docs/latest/api/repl.html#javascript-expressions)
The default evaluator supports direct evaluation of JavaScript expressions:
```
> 1 + 1
2
> const m = 2
undefined
> m + 1
3
copy
```

Unless otherwise scoped within blocks or functions, variables declared either implicitly or using the `const`, `let`, or `var` keywords are declared at the global scope.
##### Global and local scope[#](https://nodejs.org/docs/latest/api/repl.html#global-and-local-scope)
The default evaluator provides access to any variables that exist in the global scope. It is possible to expose a variable to the REPL explicitly by assigning it to the `context` object associated with each `REPLServer`:
```
import repl from 'node:repl';
const msg = 'message';

repl.start('> ').context.m = msg;
const repl = require('node:repl');
const msg = 'message';

repl.start('> ').context.m = msg;
copy
```

Properties in the `context` object appear as local within the REPL:
```
$ node repl_test.js
> m
'message'
copy
```

Context properties are not read-only by default. To specify read-only globals, context properties must be defined using `Object.defineProperty()`:
```
import repl from 'node:repl';
const msg = 'message';

const r = repl.start('> ');
Object.defineProperty(r.context, 'm', {
  configurable: false,
  enumerable: true,
  value: msg,
});
const repl = require('node:repl');
const msg = 'message';

const r = repl.start('> ');
Object.defineProperty(r.context, 'm', {
  configurable: false,
  enumerable: true,
  value: msg,
});
copy
```

##### Accessing core Node.js modules[#](https://nodejs.org/docs/latest/api/repl.html#accessing-core-nodejs-modules)
The default evaluator will automatically load Node.js core modules into the REPL environment when used. For instance, unless otherwise declared as a global or scoped variable, the input `fs` will be evaluated on-demand as `global.fs = require('node:fs')`.
```
> fs.createReadStream('./some/file');
copy
```

##### Global uncaught exceptions[#](https://nodejs.org/docs/latest/api/repl.html#global-uncaught-exceptions)
History Version | Changes
---|---
v12.3.0 | The `'uncaughtException'` event is from now on triggered if the repl is used as standalone program.
The REPL uses the [`domain`](https://nodejs.org/docs/latest/api/domain.html) module to catch all uncaught exceptions for that REPL session.
This use of the [`domain`](https://nodejs.org/docs/latest/api/domain.html) module in the REPL has these side effects:
  * Uncaught exceptions only emit the [`'uncaughtException'`](https://nodejs.org/docs/latest/api/process.html#event-uncaughtexception) event in the standalone REPL. Adding a listener for this event in a REPL within another Node.js program results in [`ERR_INVALID_REPL_INPUT`](https://nodejs.org/docs/latest/api/errors.html#err_invalid_repl_input).
```
const r = repl.start();

r.write('process.on("uncaughtException", () => console.log("Foobar"));\n');
// Output stream includes:
//   TypeError [ERR_INVALID_REPL_INPUT]: Listeners for `uncaughtException`
//   cannot be used in the REPL

r.close();
copy
```

  * Trying to use [`process.setUncaughtExceptionCaptureCallback()`](https://nodejs.org/docs/latest/api/process.html#processsetuncaughtexceptioncapturecallbackfn) throws an [`ERR_DOMAIN_CANNOT_SET_UNCAUGHT_EXCEPTION_CAPTURE`](https://nodejs.org/docs/latest/api/errors.html#err_domain_cannot_set_uncaught_exception_capture) error.


##### Assignment of the `_` (underscore) variable[#](https://nodejs.org/docs/latest/api/repl.html#assignment-of-the-underscore-variable)
History Version | Changes
---|---
v9.8.0 | Added `_error` support.
The default evaluator will, by default, assign the result of the most recently evaluated expression to the special variable `_` (underscore). Explicitly setting `_` to a value will disable this behavior.
```
> [ 'a', 'b', 'c' ]
[ 'a', 'b', 'c' ]
> _.length
3
> _ += 1
Expression assignment to _ now disabled.
4
> 1 + 1
2
> _
4
copy
```

Similarly, `_error` will refer to the last seen error, if there was any. Explicitly setting `_error` to a value will disable this behavior.
```
> throw new Error('foo');
Uncaught Error: foo
> _error.message
'foo'
copy
```

#####  `await` keyword[#](https://nodejs.org/docs/latest/api/repl.html#await-keyword)
Support for the `await` keyword is enabled at the top level.
```
> await Promise.resolve(123)
123
> await Promise.reject(new Error('REPL await'))
Uncaught Error: REPL await
    at REPL2:1:54
> const timeout = util.promisify(setTimeout);
undefined
> const old = Date.now(); await timeout(1000); console.log(Date.now() - old);
1002
undefined
copy
```

One known limitation of using the `await` keyword in the REPL is that it will invalidate the lexical scoping of the `const` keywords.
For example:
```
> const m = await Promise.resolve(123)
undefined
> m
123
> m = await Promise.resolve(234)
234
// redeclaring the constant does error
> const m = await Promise.resolve(345)
Uncaught SyntaxError: Identifier 'm' has already been declared
copy
```

[`--no-experimental-repl-await`](https://nodejs.org/docs/latest/api/cli.html#--no-experimental-repl-await) shall disable top-level await in REPL.
#### Reverse-i-search[#](https://nodejs.org/docs/latest/api/repl.html#reverse-i-search)
Added in: v13.6.0, v12.17.0
The REPL supports bi-directional reverse-i-search similar to `Ctrl`+`R` to search backward and `Ctrl`+`S` to search forwards.
Duplicated history entries will be skipped.
Entries are accepted as soon as any key is pressed that doesn't correspond with the reverse search. Cancelling is possible by pressing `Esc` or `Ctrl`+`C`.
Changing the direction immediately searches for the next entry in the expected direction from the current position on.
#### Custom evaluation functions[#](https://nodejs.org/docs/latest/api/repl.html#custom-evaluation-functions)
When a new [`repl.REPLServer`](https://nodejs.org/docs/latest/api/repl.html#class-replserver) is created, a custom evaluation function may be provided. This can be used, for instance, to implement fully customized REPL applications.
An evaluation function accepts the following four arguments:
  * `code` `1 + 1`).
  * `context` `global` context or a context specific to the REPL instance, depending on the `useGlobal` option.
  * `replResourceName`
  * `callback`
    * An error object to provide if an error occurred during evaluation, or `null`/`undefined` if no error occurred.
    * The result of the code evaluation (this is not relevant if an error is provided).


The following illustrates an example of a REPL that squares a given number, an error is instead printed if the provided input is not actually a number:
```
import repl from 'node:repl';

function byThePowerOfTwo(number) {
  return number * number;
}

function myEval(code, context, replResourceName, callback) {
  if (isNaN(code)) {
    callback(new Error(`${code.trim()} is not a number`));
  } else {
    callback(null, byThePowerOfTwo(code));
  }
}

repl.start({ prompt: 'Enter a number: ', eval: myEval });
const repl = require('node:repl');

function byThePowerOfTwo(number) {
  return number * number;
}

function myEval(code, context, replResourceName, callback) {
  if (isNaN(code)) {
    callback(new Error(`${code.trim()} is not a number`));
  } else {
    callback(null, byThePowerOfTwo(code));
  }
}

repl.start({ prompt: 'Enter a number: ', eval: myEval });
copy
```

##### Recoverable errors[#](https://nodejs.org/docs/latest/api/repl.html#recoverable-errors)
At the REPL prompt, pressing `Enter` sends the current line of input to the `eval` function. In order to support multi-line input, the `eval` function can return an instance of `repl.Recoverable` to the provided callback function:
```
function myEval(cmd, context, filename, callback) {
  let result;
  try {
    result = vm.runInThisContext(cmd);
  } catch (e) {
    if (isRecoverableError(e)) {
      return callback(new repl.Recoverable(e));
    }
  }
  callback(null, result);
}

function isRecoverableError(error) {
  if (error.name === 'SyntaxError') {
    return /^(Unexpected end of input|Unexpected token)/.test(error.message);
  }
  return false;
}
copy
```

#### Customizing REPL output[#](https://nodejs.org/docs/latest/api/repl.html#customizing-repl-output)
By default, [`repl.REPLServer`](https://nodejs.org/docs/latest/api/repl.html#class-replserver) instances format output using the [`util.inspect()`](https://nodejs.org/docs/latest/api/util.html#utilinspectobject-options) method before writing the output to the provided `Writable` stream (`process.stdout` by default). The `showProxy` inspection option is set to true by default and the `colors` option is set to true depending on the REPL's `useColors` option.
The `useColors` boolean option can be specified at construction to instruct the default writer to use ANSI style codes to colorize the output from the `util.inspect()` method.
If the REPL is run as standalone program, it is also possible to change the REPL's [inspection defaults](https://nodejs.org/docs/latest/api/util.html#utilinspectobject-options) from inside the REPL by using the `inspect.replDefaults` property which mirrors the `defaultOptions` from [`util.inspect()`](https://nodejs.org/docs/latest/api/util.html#utilinspectobject-options).
```
> util.inspect.replDefaults.compact = false;
false
> [1]
[
  1
]
>
copy
```

To fully customize the output of a [`repl.REPLServer`](https://nodejs.org/docs/latest/api/repl.html#class-replserver) instance pass in a new function for the `writer` option on construction. The following example, for instance, simply converts any input text to upper case:
```
import repl from 'node:repl';

const r = repl.start({ prompt: '> ', eval: myEval, writer: myWriter });

function myEval(cmd, context, filename, callback) {
  callback(null, cmd);
}

function myWriter(output) {
  return output.toUpperCase();
}
const repl = require('node:repl');

const r = repl.start({ prompt: '> ', eval: myEval, writer: myWriter });

function myEval(cmd, context, filename, callback) {
  callback(null, cmd);
}

function myWriter(output) {
  return output.toUpperCase();
}
copy
```

### Class: `REPLServer`[#](https://nodejs.org/docs/latest/api/repl.html#class-replserver)
Added in: v0.1.91
  * `options` [`repl.start()`](https://nodejs.org/docs/latest/api/repl.html#replstartoptions)
  * Extends: [`<readline.Interface>`](https://nodejs.org/docs/latest/api/readline.html#class-readlineinterface)


Instances of `repl.REPLServer` are created using the [`repl.start()`](https://nodejs.org/docs/latest/api/repl.html#replstartoptions) method or directly using the JavaScript `new` keyword.
```
import repl from 'node:repl';

const options = { useColors: true };

const firstInstance = repl.start(options);
const secondInstance = new repl.REPLServer(options);
const repl = require('node:repl');

const options = { useColors: true };

const firstInstance = repl.start(options);
const secondInstance = new repl.REPLServer(options);
copy
```

#### Event: `'exit'`[#](https://nodejs.org/docs/latest/api/repl.html#event-exit)
Added in: v0.7.7
The `'exit'` event is emitted when the REPL is exited either by receiving the `.exit` command as input, the user pressing `Ctrl`+`C` twice to signal `SIGINT`, or by pressing `Ctrl`+`D` to signal `'end'` on the input stream. The listener callback is invoked without any arguments.
```
replServer.on('exit', () => {
  console.log('Received "exit" event from repl!');
  process.exit();
});
copy
```

#### Event: `'reset'`[#](https://nodejs.org/docs/latest/api/repl.html#event-reset)
Added in: v0.11.0
The `'reset'` event is emitted when the REPL's context is reset. This occurs whenever the `.clear` command is received as input _unless_ the REPL is using the default evaluator and the `repl.REPLServer` instance was created with the `useGlobal` option set to `true`. The listener callback will be called with a reference to the `context` object as the only argument.
This can be used primarily to re-initialize REPL context to some pre-defined state:
```
import repl from 'node:repl';

function initializeContext(context) {
  context.m = 'test';
}

const r = repl.start({ prompt: '> ' });
initializeContext(r.context);

r.on('reset', initializeContext);
const repl = require('node:repl');

function initializeContext(context) {
  context.m = 'test';
}

const r = repl.start({ prompt: '> ' });
initializeContext(r.context);

r.on('reset', initializeContext);
copy
```

When this code is executed, the global `'m'` variable can be modified but then reset to its initial value using the `.clear` command:
```
$ ./node example.js
> m
'test'
> m = 1
1
> m
1
> .clear
Clearing context...
> m
'test'
>
copy
```

####  `replServer.defineCommand(keyword, cmd)`[#](https://nodejs.org/docs/latest/api/repl.html#replserverdefinecommandkeyword-cmd)
Added in: v0.3.0
  * `keyword`  _without_ a leading `.` character).
  * `cmd`


The `replServer.defineCommand()` method is used to add new `.`-prefixed commands to the REPL instance. Such commands are invoked by typing a `.` followed by the `keyword`. The `cmd` is either a `Function` or an `Object` with the following properties:
  * `help` `.help` is entered (Optional).
  * `action`


The following example shows two new commands added to the REPL instance:
```
import repl from 'node:repl';

const replServer = repl.start({ prompt: '> ' });
replServer.defineCommand('sayhello', {
  help: 'Say hello',
  action(name) {
    this.clearBufferedCommand();
    console.log(`Hello, ${name}!`);
    this.displayPrompt();
  },
});
replServer.defineCommand('saybye', function saybye() {
  console.log('Goodbye!');
  this.close();
});
const repl = require('node:repl');

const replServer = repl.start({ prompt: '> ' });
replServer.defineCommand('sayhello', {
  help: 'Say hello',
  action(name) {
    this.clearBufferedCommand();
    console.log(`Hello, ${name}!`);
    this.displayPrompt();
  },
});
replServer.defineCommand('saybye', function saybye() {
  console.log('Goodbye!');
  this.close();
});
copy
```

The new commands can then be used from within the REPL instance:
```
> .sayhello Node.js User
Hello, Node.js User!
> .saybye
Goodbye!
copy
```

####  `replServer.displayPrompt([preserveCursor])`[#](https://nodejs.org/docs/latest/api/repl.html#replserverdisplaypromptpreservecursor)
Added in: v0.1.91
  * `preserveCursor`


The `replServer.displayPrompt()` method readies the REPL instance for input from the user, printing the configured `prompt` to a new line in the `output` and resuming the `input` to accept new input.
When multi-line input is being entered, a pipe `'|'` is printed rather than the 'prompt'.
When `preserveCursor` is `true`, the cursor placement will not be reset to `0`.
The `replServer.displayPrompt` method is primarily intended to be called from within the action function for commands registered using the `replServer.defineCommand()` method.
####  `replServer.clearBufferedCommand()`[#](https://nodejs.org/docs/latest/api/repl.html#replserverclearbufferedcommand)
Added in: v9.0.0
The `replServer.clearBufferedCommand()` method clears any command that has been buffered but not yet executed. This method is primarily intended to be called from within the action function for commands registered using the `replServer.defineCommand()` method.
####  `replServer.setupHistory(historyConfig, callback)`[#](https://nodejs.org/docs/latest/api/repl.html#replserversetuphistoryhistoryconfig-callback)
Added in: v11.10.0History Version | Changes
---|---
v24.2.0 | Updated the `historyConfig` parameter to accept an object with `filePath`, `size`, `removeHistoryDuplicates` and `onHistoryFileLoaded` properties.
  * `historyConfig`
    * `filePath`
    * `size` `0`. This option makes sense only if `terminal` is set to `true` by the user or by an internal `output` check, otherwise the history caching mechanism is not initialized at all. **Default:** `30`.
    * `removeHistoryDuplicates` `true`, when a new input line added to the history list duplicates an older one, this removes the older line from the list. **Default:** `false`.
    * `onHistoryFileLoaded`
      * `err`
      * `repl` [`<repl.REPLServer>`](https://nodejs.org/docs/latest/api/repl.html#replreplserver)
  * `callback` `onHistoryFileLoaded` in `historyConfig`)
    * `err`
    * `repl` [`<repl.REPLServer>`](https://nodejs.org/docs/latest/api/repl.html#replreplserver)


Initializes a history log file for the REPL instance. When executing the Node.js binary and using the command-line REPL, a history file is initialized by default. However, this is not the case when creating a REPL programmatically. Use this method to initialize a history log file when working with REPL instances programmatically.
###  `repl.builtinModules`[#](https://nodejs.org/docs/latest/api/repl.html#replbuiltinmodules)
Added in: v14.5.0Deprecated in: v24.0.0, v22.16.0
Stability: 0 - Deprecated. Use [`module.builtinModules`](https://nodejs.org/docs/latest/api/module.html#modulebuiltinmodules) instead.
  * Type:


A list of the names of some Node.js modules, e.g., `'http'`.
An automated migration is available (
```
npx codemod@latest @nodejs/repl-builtin-modules
copy
```

###  `repl.start([options])`[#](https://nodejs.org/docs/latest/api/repl.html#replstartoptions)
Added in: v0.1.91History Version | Changes
---|---
v24.1.0 | Added the possibility to add/edit/remove multilines while adding a multiline command.
v24.0.0 | The multi-line indicator is now "|" instead of "...". Added support for multi-line history. It is now possible to "fix" multi-line commands with syntax errors by visiting the history and editing the command. When visiting the multiline history from an old node version, the multiline structure is not preserved.
v13.4.0, v12.17.0 | The `preview` option is now available.
v12.0.0 | The `terminal` option now follows the default description in all cases and `useColors` checks `hasColors()` if available.
v10.0.0 | The `REPL_MAGIC_MODE` `replMode` was removed.
v6.3.0 | The `breakEvalOnSigint` option is supported now.
v5.8.0 | The `options` parameter is optional now.
  * `options`
    * `prompt` **Default:** `'> '` (with a trailing space).
    * `input` [`<stream.Readable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) The `Readable` stream from which REPL input will be read. **Default:** `process.stdin`.
    * `output` [`<stream.Writable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) The `Writable` stream to which REPL output will be written. **Default:** `process.stdout`.
    * `terminal` `true`, specifies that the `output` should be treated as a TTY terminal. **Default:** checking the value of the `isTTY` property on the `output` stream upon instantiation.
    * `eval` **Default:** an async wrapper for the JavaScript `eval()` function. An `eval` function can error with `repl.Recoverable` to indicate the input was incomplete and prompt for additional lines. See the [custom evaluation functions](https://nodejs.org/docs/latest/api/repl.html#custom-evaluation-functions) section for more details.
    * `useColors` `true`, specifies that the default `writer` function should include ANSI color styling to REPL output. If a custom `writer` function is provided then this has no effect. **Default:** checking color support on the `output` stream if the REPL instance's `terminal` value is `true`.
    * `useGlobal` `true`, specifies that the default evaluation function will use the JavaScript `global` as the context as opposed to creating a new separate context for the REPL instance. The node CLI REPL sets this value to `true`. **Default:** `false`.
    * `ignoreUndefined` `true`, specifies that the default writer will not output the return value of a command if it evaluates to `undefined`. **Default:** `false`.
    * `writer` `output`. **Default:** [`util.inspect()`](https://nodejs.org/docs/latest/api/util.html#utilinspectobject-options).
    * `completer` [`readline.InterfaceCompleter`](https://nodejs.org/docs/latest/api/readline.html#use-of-the-completer-function) for an example.
    * `replMode`
      * `repl.REPL_MODE_SLOPPY` to evaluate expressions in sloppy mode.
      * `repl.REPL_MODE_STRICT` to evaluate expressions in strict mode. This is equivalent to prefacing every repl statement with `'use strict'`.
    * `breakEvalOnSigint` `SIGINT` is received, such as when `Ctrl`+`C` is pressed. This cannot be used together with a custom `eval` function. **Default:** `false`.
    * `preview` **Default:** `true` with the default eval function and `false` in case a custom eval function is used. If `terminal` is falsy, then there are no previews and the value of `preview` has no effect.
  * Returns: [`<repl.REPLServer>`](https://nodejs.org/docs/latest/api/repl.html#replreplserver)


The `repl.start()` method creates and starts a [`repl.REPLServer`](https://nodejs.org/docs/latest/api/repl.html#class-replserver) instance.
If `options` is a string, then it specifies the input prompt:
```
import repl from 'node:repl';

// a Unix style prompt
repl.start('$ ');
const repl = require('node:repl');

// a Unix style prompt
repl.start('$ ');
copy
```

### The Node.js REPL[#](https://nodejs.org/docs/latest/api/repl.html#the-nodejs-repl)
Node.js itself uses the `node:repl` module to provide its own interactive interface for executing JavaScript. This can be used by executing the Node.js binary without passing any arguments (or by passing the `-i` argument):
```
$ node
> const a = [1, 2, 3];
undefined
> a
[ 1, 2, 3 ]
> a.forEach((v) => {
...   console.log(v);
...   });
1
2
3
copy
```

#### Environment variable options[#](https://nodejs.org/docs/latest/api/repl.html#environment-variable-options)
Various behaviors of the Node.js REPL can be customized using the following environment variables:
  * `NODE_REPL_HISTORY`: When a valid path is given, persistent REPL history will be saved to the specified file rather than `.node_repl_history` in the user's home directory. Setting this value to `''` (an empty string) will disable persistent REPL history. Whitespace will be trimmed from the value. On Windows platforms environment variables with empty values are invalid so set this variable to one or more spaces to disable persistent REPL history.
  * `NODE_REPL_HISTORY_SIZE`: Controls how many lines of history will be persisted if history is available. Must be a positive number. **Default:** `1000`.
  * `NODE_REPL_MODE`: May be either `'sloppy'` or `'strict'`. **Default:** `'sloppy'`, which will allow non-strict mode code to be run.


#### Persistent history[#](https://nodejs.org/docs/latest/api/repl.html#persistent-history)
By default, the Node.js REPL will persist history between `node` REPL sessions by saving inputs to a `.node_repl_history` file located in the user's home directory. This can be disabled by setting the environment variable `NODE_REPL_HISTORY=''`.
#### Using the Node.js REPL with advanced line-editors[#](https://nodejs.org/docs/latest/api/repl.html#using-the-nodejs-repl-with-advanced-line-editors)
For advanced line-editors, start Node.js with the environment variable `NODE_NO_READLINE=1`. This will start the main and debugger REPL in canonical terminal settings, which will allow use with `rlwrap`.
For example, the following can be added to a `.bashrc` file:
```
alias node="env NODE_NO_READLINE=1 rlwrap node"
copy
```

#### Starting multiple REPL instances in the same process[#](https://nodejs.org/docs/latest/api/repl.html#starting-multiple-repl-instances-in-the-same-process)
It is possible to create and run multiple REPL instances against a single running instance of Node.js that share a single `global` object (by setting the `useGlobal` option to `true`) but have separate I/O interfaces.
The following example, for instance, provides separate REPLs on `stdin`, a Unix socket, and a TCP socket, all sharing the same `global` object:
```
import net from 'node:net';
import repl from 'node:repl';
import process from 'node:process';
import fs from 'node:fs';

let connections = 0;

repl.start({
  prompt: 'Node.js via stdin> ',
  useGlobal: true,
  input: process.stdin,
  output: process.stdout,
});

const unixSocketPath = '/tmp/node-repl-sock';

// If the socket file already exists let's remove it
fs.rmSync(unixSocketPath, { force: true });

net.createServer((socket) => {
  connections += 1;
  repl.start({
    prompt: 'Node.js via Unix socket> ',
    useGlobal: true,
    input: socket,
    output: socket,
  }).on('exit', () => {
    socket.end();
  });
}).listen(unixSocketPath);

net.createServer((socket) => {
  connections += 1;
  repl.start({
    prompt: 'Node.js via TCP socket> ',
    useGlobal: true,
    input: socket,
    output: socket,
  }).on('exit', () => {
    socket.end();
  });
}).listen(5001);
const net = require('node:net');
const repl = require('node:repl');
const fs = require('node:fs');

let connections = 0;

repl.start({
  prompt: 'Node.js via stdin> ',
  useGlobal: true,
  input: process.stdin,
  output: process.stdout,
});

const unixSocketPath = '/tmp/node-repl-sock';

// If the socket file already exists let's remove it
fs.rmSync(unixSocketPath, { force: true });

net.createServer((socket) => {
  connections += 1;
  repl.start({
    prompt: 'Node.js via Unix socket> ',
    useGlobal: true,
    input: socket,
    output: socket,
  }).on('exit', () => {
    socket.end();
  });
}).listen(unixSocketPath);

net.createServer((socket) => {
  connections += 1;
  repl.start({
    prompt: 'Node.js via TCP socket> ',
    useGlobal: true,
    input: socket,
    output: socket,
  }).on('exit', () => {
    socket.end();
  });
}).listen(5001);
copy
```

Running this application from the command line will start a REPL on stdin. Other REPL clients may connect through the Unix socket or TCP socket. `telnet`, for instance, is useful for connecting to TCP sockets, while `socat` can be used to connect to both Unix and TCP sockets.
By starting a REPL from a Unix socket-based server instead of stdin, it is possible to connect to a long-running Node.js process without restarting it.
#### Examples[#](https://nodejs.org/docs/latest/api/repl.html#examples)
##### Full-featured "terminal" REPL over `net.Server` and `net.Socket`[#](https://nodejs.org/docs/latest/api/repl.html#full-featured-terminal-repl-over-netserver-and-netsocket)
This is an example on how to run a "full-featured" (terminal) REPL using [`net.Server`](https://nodejs.org/docs/latest/api/net.html#class-netserver) and [`net.Socket`](https://nodejs.org/docs/latest/api/net.html#class-netsocket)
The following script starts an HTTP server on port `1337` that allows clients to establish socket connections to its REPL instance.
```
// repl-server.js
import repl from 'node:repl';
import net from 'node:net';

net
  .createServer((socket) => {
    const r = repl.start({
      prompt: `socket ${socket.remoteAddress}:${socket.remotePort}> `,
      input: socket,
      output: socket,
      terminal: true,
      useGlobal: false,
    });
    r.on('exit', () => {
      socket.end();
    });
    r.context.socket = socket;
  })
  .listen(1337);
// repl-server.js
const repl = require('node:repl');
const net = require('node:net');

net
  .createServer((socket) => {
    const r = repl.start({
      prompt: `socket ${socket.remoteAddress}:${socket.remotePort}> `,
      input: socket,
      output: socket,
      terminal: true,
      useGlobal: false,
    });
    r.on('exit', () => {
      socket.end();
    });
    r.context.socket = socket;
  })
  .listen(1337);
copy
```

While the following implements a client that can create a socket connection with the above defined server over port `1337`.
```
// repl-client.js
import net from 'node:net';
import process from 'node:process';

const sock = net.connect(1337);

process.stdin.pipe(sock);
sock.pipe(process.stdout);

sock.on('connect', () => {
  process.stdin.resume();
  process.stdin.setRawMode(true);
});

sock.on('close', () => {
  process.stdin.setRawMode(false);
  process.stdin.pause();
  sock.removeListener('close', done);
});

process.stdin.on('end', () => {
  sock.destroy();
  console.log();
});

process.stdin.on('data', (b) => {
  if (b.length === 1 && b[0] === 4) {
    process.stdin.emit('end');
  }
});
// repl-client.js
const net = require('node:net');

const sock = net.connect(1337);

process.stdin.pipe(sock);
sock.pipe(process.stdout);

sock.on('connect', () => {
  process.stdin.resume();
  process.stdin.setRawMode(true);
});

sock.on('close', () => {
  process.stdin.setRawMode(false);
  process.stdin.pause();
  sock.removeListener('close', done);
});

process.stdin.on('end', () => {
  sock.destroy();
  console.log();
});

process.stdin.on('data', (b) => {
  if (b.length === 1 && b[0] === 4) {
    process.stdin.emit('end');
  }
});
copy
```

To run the example open two different terminals on your machine, start the server with `node repl-server.js` in one terminal and `node repl-client.js` on the other.
Original code from
##### REPL over `curl`[#](https://nodejs.org/docs/latest/api/repl.html#repl-over-curl)
This is an example on how to run a REPL instance over
The following script starts an HTTP server on port `8000` that can accept a connection established via
```
import http from 'node:http';
import repl from 'node:repl';

const server = http.createServer((req, res) => {
  res.setHeader('content-type', 'multipart/octet-stream');

  repl.start({
    prompt: 'curl repl> ',
    input: req,
    output: res,
    terminal: false,
    useColors: true,
    useGlobal: false,
  });
});

server.listen(8000);
const http = require('node:http');
const repl = require('node:repl');

const server = http.createServer((req, res) => {
  res.setHeader('content-type', 'multipart/octet-stream');

  repl.start({
    prompt: 'curl repl> ',
    input: req,
    output: res,
    terminal: false,
    useColors: true,
    useGlobal: false,
  });
});

server.listen(8000);
copy
```

When the above script is running you can then use `curl --no-progress-meter -sSNT. localhost:8000`.
**Warning** This example is intended purely for educational purposes to demonstrate how Node.js REPLs can be started using different I/O streams. It should **not** be used in production environments or any context where security is a concern without additional protective measures. If you need to implement REPLs in a real-world application, consider alternative approaches that mitigate these risks, such as using secure input mechanisms and avoiding open network interfaces.
Original code from
