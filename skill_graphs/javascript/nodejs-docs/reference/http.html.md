[Skip to content](https://nodejs.org/docs/latest/api/domain.html#apicontent)
[ Node.js ](https://nodejs.org/ "Go back to the home page")
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


* * *
# Node.js v25.8.0 documentation
  * Node.js v25.8.0
  * [](https://nodejs.org/docs/latest/api/domain.html#toc-picker)
    * [Domain](https://nodejs.org/docs/latest/api/domain.html#domain)
      * [Warning: Don't ignore errors!](https://nodejs.org/docs/latest/api/domain.html#warning-dont-ignore-errors)
      * [Additions to `Error` objects](https://nodejs.org/docs/latest/api/domain.html#additions-to-error-objects)
      * [Implicit binding](https://nodejs.org/docs/latest/api/domain.html#implicit-binding)
      * [Explicit binding](https://nodejs.org/docs/latest/api/domain.html#explicit-binding)
      * [`domain.create()`](https://nodejs.org/docs/latest/api/domain.html#domaincreate)
      * [Class: `Domain`](https://nodejs.org/docs/latest/api/domain.html#class-domain)
        * [`domain.members`](https://nodejs.org/docs/latest/api/domain.html#domainmembers)
        * [`domain.add(emitter)`](https://nodejs.org/docs/latest/api/domain.html#domainaddemitter)
        * [`domain.bind(callback)`](https://nodejs.org/docs/latest/api/domain.html#domainbindcallback)
        * [`domain.enter()`](https://nodejs.org/docs/latest/api/domain.html#domainenter)
        * [`domain.exit()`](https://nodejs.org/docs/latest/api/domain.html#domainexit)
        * [`domain.intercept(callback)`](https://nodejs.org/docs/latest/api/domain.html#domaininterceptcallback)
        * [`domain.remove(emitter)`](https://nodejs.org/docs/latest/api/domain.html#domainremoveemitter)
        * [`domain.run(fn[, ...args])`](https://nodejs.org/docs/latest/api/domain.html#domainrunfn-args)
      * [Domains and promises](https://nodejs.org/docs/latest/api/domain.html#domains-and-promises)
  * [](https://nodejs.org/docs/latest/api/domain.html#gtoc-picker)
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
  * [](https://nodejs.org/docs/latest/api/domain.html#alt-docs)
    1. [25.x ](https://nodejs.org/docs/latest-v25.x/api/domain.html)
    2. [24.x ](https://nodejs.org/docs/latest-v24.x/api/domain.html)
    3. [23.x ](https://nodejs.org/docs/latest-v23.x/api/domain.html)
    4. [22.x **LTS**](https://nodejs.org/docs/latest-v22.x/api/domain.html)
    5. [21.x ](https://nodejs.org/docs/latest-v21.x/api/domain.html)
    6. [20.x **LTS**](https://nodejs.org/docs/latest-v20.x/api/domain.html)
    7. [19.x ](https://nodejs.org/docs/latest-v19.x/api/domain.html)
    8. [18.x ](https://nodejs.org/docs/latest-v18.x/api/domain.html)
    9. [17.x ](https://nodejs.org/docs/latest-v17.x/api/domain.html)
    10. [16.x ](https://nodejs.org/docs/latest-v16.x/api/domain.html)
    11. [15.x ](https://nodejs.org/docs/latest-v15.x/api/domain.html)
    12. [14.x ](https://nodejs.org/docs/latest-v14.x/api/domain.html)
    13. [13.x ](https://nodejs.org/docs/latest-v13.x/api/domain.html)
    14. [12.x ](https://nodejs.org/docs/latest-v12.x/api/domain.html)
    15. [11.x ](https://nodejs.org/docs/latest-v11.x/api/domain.html)
    16. [10.x ](https://nodejs.org/docs/latest-v10.x/api/domain.html)
    17. [9.x ](https://nodejs.org/docs/latest-v9.x/api/domain.html)
    18. [8.x ](https://nodejs.org/docs/latest-v8.x/api/domain.html)
    19. [7.x ](https://nodejs.org/docs/latest-v7.x/api/domain.html)
    20. [6.x ](https://nodejs.org/docs/latest-v6.x/api/domain.html)
    21. [5.x ](https://nodejs.org/docs/latest-v5.x/api/domain.html)
    22. [4.x ](https://nodejs.org/docs/latest-v4.x/api/domain.html)
    23. [0.12.x ](https://nodejs.org/docs/latest-v0.12.x/api/domain.html)
    24. [0.10.x ](https://nodejs.org/docs/latest-v0.10.x/api/domain.html)
  * [ ](https://nodejs.org/docs/latest/api/domain.html#options-picker)
    * [View on single page](https://nodejs.org/docs/latest/api/all.html)
    * [View as JSON](https://nodejs.org/docs/latest/api/domain.json)


* * *
Table of contents
  * [Domain](https://nodejs.org/docs/latest/api/domain.html#domain)
    * [Warning: Don't ignore errors!](https://nodejs.org/docs/latest/api/domain.html#warning-dont-ignore-errors)
    * [Additions to `Error` objects](https://nodejs.org/docs/latest/api/domain.html#additions-to-error-objects)
    * [Implicit binding](https://nodejs.org/docs/latest/api/domain.html#implicit-binding)
    * [Explicit binding](https://nodejs.org/docs/latest/api/domain.html#explicit-binding)
    * [`domain.create()`](https://nodejs.org/docs/latest/api/domain.html#domaincreate)
    * [Class: `Domain`](https://nodejs.org/docs/latest/api/domain.html#class-domain)
      * [`domain.members`](https://nodejs.org/docs/latest/api/domain.html#domainmembers)
      * [`domain.add(emitter)`](https://nodejs.org/docs/latest/api/domain.html#domainaddemitter)
      * [`domain.bind(callback)`](https://nodejs.org/docs/latest/api/domain.html#domainbindcallback)
      * [`domain.enter()`](https://nodejs.org/docs/latest/api/domain.html#domainenter)
      * [`domain.exit()`](https://nodejs.org/docs/latest/api/domain.html#domainexit)
      * [`domain.intercept(callback)`](https://nodejs.org/docs/latest/api/domain.html#domaininterceptcallback)
      * [`domain.remove(emitter)`](https://nodejs.org/docs/latest/api/domain.html#domainremoveemitter)
      * [`domain.run(fn[, ...args])`](https://nodejs.org/docs/latest/api/domain.html#domainrunfn-args)
    * [Domains and promises](https://nodejs.org/docs/latest/api/domain.html#domains-and-promises)


## Domain[#](https://nodejs.org/docs/latest/api/domain.html#domain)
**Source Code:** Deprecated in: v1.4.2History Version | Changes
---|---
v8.8.0 | Any `Promise`s created in VM contexts no longer have a `.domain` property. Their handlers are still executed in the proper domain, however, and `Promise`s created in the main context still possess a `.domain` property.
v8.0.0 | Handlers for `Promise`s are now invoked in the domain in which the first promise of a chain was created.
[Stability: 0](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Deprecated
**This module is pending deprecation.** Once a replacement API has been finalized, this module will be fully deprecated. Most developers should **not** have cause to use this module. Users who absolutely must have the functionality that domains provide may rely on it for the time being but should expect to have to migrate to a different solution in the future.
Domains provide a way to handle multiple different IO operations as a single group. If any of the event emitters or callbacks registered to a domain emit an `'error'` event, or throw an error, then the domain object will be notified, rather than losing the context of the error in the `process.on('uncaughtException')` handler, or causing the program to exit immediately with an error code.
### Warning: Don't ignore errors![#](https://nodejs.org/docs/latest/api/domain.html#warning-dont-ignore-errors)
Domain error handlers are not a substitute for closing down a process when an error occurs.
By the very nature of how
The safest way to respond to a thrown error is to shut down the process. Of course, in a normal web server, there may be many open connections, and it is not reasonable to abruptly shut those down because an error was triggered by someone else.
The better approach is to send an error response to the request that triggered the error, while letting the others finish in their normal time, and stop listening for new requests in that worker.
In this way, `domain` usage goes hand-in-hand with the cluster module, since the primary process can fork a new worker when a worker encounters an error. For Node.js programs that scale to multiple machines, the terminating proxy or service registry can take note of the failure, and react accordingly.
For example, this is not a good idea:
```
// XXX WARNING! BAD IDEA!

const d = require('node:domain').create();
d.on('error', (er) => {
  // The error won't crash the process, but what it does is worse!
  // Though we've prevented abrupt process restarting, we are leaking
  // a lot of resources if this ever happens.
  // This is no better than process.on('uncaughtException')!
  console.log(`error, but oh well ${er.message}`);
});
d.run(() => {
  require('node:http').createServer((req, res) => {
    handleRequest(req, res);
  }).listen(PORT);
});
copy
```

By using the context of a domain, and the resilience of separating our program into multiple worker processes, we can react more appropriately, and handle errors with much greater safety.
```
// Much better!

const cluster = require('node:cluster');
const PORT = +process.env.PORT || 1337;

if (cluster.isPrimary) {
  // A more realistic scenario would have more than 2 workers,
  // and perhaps not put the primary and worker in the same file.
  //
  // It is also possible to get a bit fancier about logging, and
  // implement whatever custom logic is needed to prevent DoS
  // attacks and other bad behavior.
  //
  // See the options in the cluster documentation.
  //
  // The important thing is that the primary does very little,
  // increasing our resilience to unexpected errors.

  cluster.fork();
  cluster.fork();

  cluster.on('disconnect', (worker) => {
    console.error('disconnect!');
    cluster.fork();
  });

} else {
  // the worker
  //
  // This is where we put our bugs!

  const domain = require('node:domain');

  // See the cluster documentation for more details about using
  // worker processes to serve requests. How it works, caveats, etc.

  const server = require('node:http').createServer((req, res) => {
    const d = domain.create();
    d.on('error', (er) => {
      console.error(`error ${er.stack}`);

      // We're in dangerous territory!
      // By definition, something unexpected occurred,
      // which we probably didn't want.
      // Anything can happen now! Be very careful!

      try {
        // Make sure we close down within 30 seconds
        const killtimer = setTimeout(() => {
          process.exit(1);
        }, 30000);
        // But don't keep the process open just for that!
        killtimer.unref();

        // Stop taking new requests.
        server.close();

        // Let the primary know we're dead. This will trigger a
        // 'disconnect' in the cluster primary, and then it will fork
        // a new worker.
        cluster.worker.disconnect();

        // Try to send an error to the request that triggered the problem
        res.statusCode = 500;
        res.setHeader('content-type', 'text/plain');
        res.end('Oops, there was a problem!\n');
      } catch (er2) {
        // Oh well, not much we can do at this point.
        console.error(`Error sending 500! ${er2.stack}`);
      }
    });

    // Because req and res were created before this domain existed,
    // we need to explicitly add them.
    // See the explanation of implicit vs explicit binding below.
    d.add(req);
    d.add(res);

    // Now run the handler function in the domain.
    d.run(() => {
      handleRequest(req, res);
    });
  });
  server.listen(PORT);
}

// This part is not important. Just an example routing thing.
// Put fancy application logic here.
function handleRequest(req, res) {
  switch (req.url) {
    case '/error':
      // We do some async stuff, and then...
      setTimeout(() => {
        // Whoops!
        flerb.bark();
      }, timeout);
      break;
    default:
      res.end('ok');
  }
}
copy
```

### Additions to `Error` objects[#](https://nodejs.org/docs/latest/api/domain.html#additions-to-error-objects)
Any time an `Error` object is routed through a domain, a few extra fields are added to it.
  * `error.domain` The domain that first handled the error.
  * `error.domainEmitter` The event emitter that emitted an `'error'` event with the error object.
  * `error.domainBound` The callback function which was bound to the domain, and passed an error as its first argument.
  * `error.domainThrown` A boolean indicating whether the error was thrown, emitted, or passed to a bound callback function.


### Implicit binding[#](https://nodejs.org/docs/latest/api/domain.html#implicit-binding)
If domains are in use, then all **new** `EventEmitter` objects (including Stream objects, requests, responses, etc.) will be implicitly bound to the active domain at the time of their creation.
Additionally, callbacks passed to low-level event loop requests (such as to `fs.open()`, or other callback-taking methods) will automatically be bound to the active domain. If they throw, then the domain will catch the error.
In order to prevent excessive memory usage, `Domain` objects themselves are not implicitly added as children of the active domain. If they were, then it would be too easy to prevent request and response objects from being properly garbage collected.
To nest `Domain` objects as children of a parent `Domain` they must be explicitly added.
Implicit binding routes thrown errors and `'error'` events to the `Domain`'s `'error'` event, but does not register the `EventEmitter` on the `Domain`. Implicit binding only takes care of thrown errors and `'error'` events.
### Explicit binding[#](https://nodejs.org/docs/latest/api/domain.html#explicit-binding)
Sometimes, the domain in use is not the one that ought to be used for a specific event emitter. Or, the event emitter could have been created in the context of one domain, but ought to instead be bound to some other domain.
For example, there could be one domain in use for an HTTP server, but perhaps we would like to have a separate domain to use for each request.
That is possible via explicit binding.
```
// Create a top-level domain for the server
const domain = require('node:domain');
const http = require('node:http');
const serverDomain = domain.create();

serverDomain.run(() => {
  // Server is created in the scope of serverDomain
  http.createServer((req, res) => {
    // Req and res are also created in the scope of serverDomain
    // however, we'd prefer to have a separate domain for each request.
    // create it first thing, and add req and res to it.
    const reqd = domain.create();
    reqd.add(req);
    reqd.add(res);
    reqd.on('error', (er) => {
      console.error('Error', er, req.url);
      try {
        res.writeHead(500);
        res.end('Error occurred, sorry.');
      } catch (er2) {
        console.error('Error sending 500', er2, req.url);
      }
    });
  }).listen(1337);
});
copy
```

###  `domain.create()`[#](https://nodejs.org/docs/latest/api/domain.html#domaincreate)
  * Returns: [`<Domain>`](https://nodejs.org/docs/latest/api/domain.html#class-domain)


### Class: `Domain`[#](https://nodejs.org/docs/latest/api/domain.html#class-domain)
  * Extends: [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter)


The `Domain` class encapsulates the functionality of routing errors and uncaught exceptions to the active `Domain` object.
To handle the errors that it catches, listen to its `'error'` event.
####  `domain.members`[#](https://nodejs.org/docs/latest/api/domain.html#domainmembers)
  * Type:


An array of event emitters that have been explicitly added to the domain.
####  `domain.add(emitter)`[#](https://nodejs.org/docs/latest/api/domain.html#domainaddemitter)
History Version | Changes
---|---
v9.3.0 | No longer accepts timer objects.
  * `emitter` [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter) emitter to be added to the domain


Explicitly adds an emitter to the domain. If any event handlers called by the emitter throw an error, or if the emitter emits an `'error'` event, it will be routed to the domain's `'error'` event, just like with implicit binding.
If the `EventEmitter` was already bound to a domain, it is removed from that one, and bound to this one instead.
####  `domain.bind(callback)`[#](https://nodejs.org/docs/latest/api/domain.html#domainbindcallback)
  * `callback`
  * Returns:


The returned function will be a wrapper around the supplied callback function. When the returned function is called, any errors that are thrown will be routed to the domain's `'error'` event.
```
const d = domain.create();

function readSomeFile(filename, cb) {
  fs.readFile(filename, 'utf8', d.bind((er, data) => {
    // If this throws, it will also be passed to the domain.
    return cb(er, data ? JSON.parse(data) : null);
  }));
}

d.on('error', (er) => {
  // An error occurred somewhere. If we throw it now, it will crash the program
  // with the normal line number and stack message.
});
copy
```

####  `domain.enter()`[#](https://nodejs.org/docs/latest/api/domain.html#domainenter)
The `enter()` method is plumbing used by the `run()`, `bind()`, and `intercept()` methods to set the active domain. It sets `domain.active` and `process.domain` to the domain, and implicitly pushes the domain onto the domain stack managed by the domain module (see [`domain.exit()`](https://nodejs.org/docs/latest/api/domain.html#domainexit) for details on the domain stack). The call to `enter()` delimits the beginning of a chain of asynchronous calls and I/O operations bound to a domain.
Calling `enter()` changes only the active domain, and does not alter the domain itself. `enter()` and `exit()` can be called an arbitrary number of times on a single domain.
####  `domain.exit()`[#](https://nodejs.org/docs/latest/api/domain.html#domainexit)
The `exit()` method exits the current domain, popping it off the domain stack. Any time execution is going to switch to the context of a different chain of asynchronous calls, it's important to ensure that the current domain is exited. The call to `exit()` delimits either the end of or an interruption to the chain of asynchronous calls and I/O operations bound to a domain.
If there are multiple, nested domains bound to the current execution context, `exit()` will exit any domains nested within this domain.
Calling `exit()` changes only the active domain, and does not alter the domain itself. `enter()` and `exit()` can be called an arbitrary number of times on a single domain.
####  `domain.intercept(callback)`[#](https://nodejs.org/docs/latest/api/domain.html#domaininterceptcallback)
  * `callback`
  * Returns:


This method is almost identical to [`domain.bind(callback)`](https://nodejs.org/docs/latest/api/domain.html#domainbindcallback). However, in addition to catching thrown errors, it will also intercept [`Error`](https://nodejs.org/docs/latest/api/errors.html#class-error) objects sent as the first argument to the function.
In this way, the common `if (err) return callback(err);` pattern can be replaced with a single error handler in a single place.
```
const d = domain.create();

function readSomeFile(filename, cb) {
  fs.readFile(filename, 'utf8', d.intercept((data) => {
    // Note, the first argument is never passed to the
    // callback since it is assumed to be the 'Error' argument
    // and thus intercepted by the domain.

    // If this throws, it will also be passed to the domain
    // so the error-handling logic can be moved to the 'error'
    // event on the domain instead of being repeated throughout
    // the program.
    return cb(null, JSON.parse(data));
  }));
}

d.on('error', (er) => {
  // An error occurred somewhere. If we throw it now, it will crash the program
  // with the normal line number and stack message.
});
copy
```

####  `domain.remove(emitter)`[#](https://nodejs.org/docs/latest/api/domain.html#domainremoveemitter)
  * `emitter` [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter) emitter to be removed from the domain


The opposite of [`domain.add(emitter)`](https://nodejs.org/docs/latest/api/domain.html#domainaddemitter). Removes domain handling from the specified emitter.
####  `domain.run(fn[, ...args])`[#](https://nodejs.org/docs/latest/api/domain.html#domainrunfn-args)
  * `fn`
  * `...args`


Run the supplied function in the context of the domain, implicitly binding all event emitters, timers, and low-level requests that are created in that context. Optionally, arguments can be passed to the function.
This is the most basic way to use a domain.
```
const domain = require('node:domain');
const fs = require('node:fs');
const d = domain.create();
d.on('error', (er) => {
  console.error('Caught error!', er);
});
d.run(() => {
  process.nextTick(() => {
    setTimeout(() => { // Simulating some various async stuff
      fs.open('non-existent file', 'r', (er, fd) => {
        if (er) throw er;
        // proceed...
      });
    }, 100);
  });
});
copy
```

In this example, the `d.on('error')` handler will be triggered, rather than crashing the program.
### Domains and promises[#](https://nodejs.org/docs/latest/api/domain.html#domains-and-promises)
As of Node.js 8.0.0, the handlers of promises are run inside the domain in which the call to `.then()` or `.catch()` itself was made:
```
const d1 = domain.create();
const d2 = domain.create();

let p;
d1.run(() => {
  p = Promise.resolve(42);
});

d2.run(() => {
  p.then((v) => {
    // running in d2
  });
});
copy
```

A callback may be bound to a specific domain using [`domain.bind(callback)`](https://nodejs.org/docs/latest/api/domain.html#domainbindcallback):
```
const d1 = domain.create();
const d2 = domain.create();

let p;
d1.run(() => {
  p = Promise.resolve(42);
});

d2.run(() => {
  p.then(p.domain.bind((v) => {
    // running in d1
  }));
});
copy
```

Domains will not interfere with the error handling mechanisms for promises. In other words, no `'error'` event will be emitted for unhandled `Promise` rejections.
