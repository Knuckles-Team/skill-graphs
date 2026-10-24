[Skip to content](https://nodejs.org/docs/latest/api/inspector.html#apicontent)
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
  * [](https://nodejs.org/docs/latest/api/inspector.html#toc-picker)
    * [Inspector](https://nodejs.org/docs/latest/api/inspector.html#inspector)
      * [Promises API](https://nodejs.org/docs/latest/api/inspector.html#promises-api)
        * [Class: `inspector.Session`](https://nodejs.org/docs/latest/api/inspector.html#class-inspectorsession)
          * [`new inspector.Session()`](https://nodejs.org/docs/latest/api/inspector.html#new-inspectorsession)
          * [Event: `'inspectorNotification'`](https://nodejs.org/docs/latest/api/inspector.html#event-inspectornotification)
          * [Event: `<inspector-protocol-method>`](https://nodejs.org/docs/latest/api/inspector.html#event-inspector-protocol-method)
          * [`session.connect()`](https://nodejs.org/docs/latest/api/inspector.html#sessionconnect)
          * [`session.connectToMainThread()`](https://nodejs.org/docs/latest/api/inspector.html#sessionconnecttomainthread)
          * [`session.disconnect()`](https://nodejs.org/docs/latest/api/inspector.html#sessiondisconnect)
          * [`session.post(method[, params])`](https://nodejs.org/docs/latest/api/inspector.html#sessionpostmethod-params)
          * [Example usage](https://nodejs.org/docs/latest/api/inspector.html#example-usage)
      * [Callback API](https://nodejs.org/docs/latest/api/inspector.html#callback-api)
        * [Class: `inspector.Session`](https://nodejs.org/docs/latest/api/inspector.html#class-inspectorsession-1)
          * [`new inspector.Session()`](https://nodejs.org/docs/latest/api/inspector.html#new-inspectorsession-1)
          * [Event: `'inspectorNotification'`](https://nodejs.org/docs/latest/api/inspector.html#event-inspectornotification-1)
          * [Event: `<inspector-protocol-method>`;](https://nodejs.org/docs/latest/api/inspector.html#event-inspector-protocol-method-1)
          * [`session.connect()`](https://nodejs.org/docs/latest/api/inspector.html#sessionconnect-1)
          * [`session.connectToMainThread()`](https://nodejs.org/docs/latest/api/inspector.html#sessionconnecttomainthread-1)
          * [`session.disconnect()`](https://nodejs.org/docs/latest/api/inspector.html#sessiondisconnect-1)
          * [`session.post(method[, params][, callback])`](https://nodejs.org/docs/latest/api/inspector.html#sessionpostmethod-params-callback)
          * [Example usage](https://nodejs.org/docs/latest/api/inspector.html#example-usage-1)
      * [Common Objects](https://nodejs.org/docs/latest/api/inspector.html#common-objects)
        * [`inspector.close()`](https://nodejs.org/docs/latest/api/inspector.html#inspectorclose)
        * [`inspector.console`](https://nodejs.org/docs/latest/api/inspector.html#inspectorconsole)
        * [`inspector.open([port[, host[, wait]]])`](https://nodejs.org/docs/latest/api/inspector.html#inspectoropenport-host-wait)
        * [`inspector.url()`](https://nodejs.org/docs/latest/api/inspector.html#inspectorurl)
        * [`inspector.waitForDebugger()`](https://nodejs.org/docs/latest/api/inspector.html#inspectorwaitfordebugger)
      * [Integration with DevTools](https://nodejs.org/docs/latest/api/inspector.html#integration-with-devtools)
        * [`inspector.Network.dataReceived([params])`](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkdatareceivedparams)
        * [`inspector.Network.dataSent([params])`](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkdatasentparams)
        * [`inspector.Network.requestWillBeSent([params])`](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkrequestwillbesentparams)
        * [`inspector.Network.responseReceived([params])`](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkresponsereceivedparams)
        * [`inspector.Network.loadingFinished([params])`](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkloadingfinishedparams)
        * [`inspector.Network.loadingFailed([params])`](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkloadingfailedparams)
        * [`inspector.Network.webSocketCreated([params])`](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkwebsocketcreatedparams)
        * [`inspector.Network.webSocketHandshakeResponseReceived([params])`](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkwebsockethandshakeresponsereceivedparams)
        * [`inspector.Network.webSocketClosed([params])`](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkwebsocketclosedparams)
        * [`inspector.NetworkResources.put`](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkresourcesput)
        * [`inspector.DOMStorage.domStorageItemAdded`](https://nodejs.org/docs/latest/api/inspector.html#inspectordomstoragedomstorageitemadded)
        * [`inspector.DOMStorage.domStorageItemRemoved`](https://nodejs.org/docs/latest/api/inspector.html#inspectordomstoragedomstorageitemremoved)
        * [`inspector.DOMStorage.domStorageItemUpdated`](https://nodejs.org/docs/latest/api/inspector.html#inspectordomstoragedomstorageitemupdated)
        * [`inspector.DOMStorage.domStorageItemsCleared`](https://nodejs.org/docs/latest/api/inspector.html#inspectordomstoragedomstorageitemscleared)
        * [`inspector.DOMStorage.registerStorage`](https://nodejs.org/docs/latest/api/inspector.html#inspectordomstorageregisterstorage)
      * [Support of breakpoints](https://nodejs.org/docs/latest/api/inspector.html#support-of-breakpoints)
  * [](https://nodejs.org/docs/latest/api/inspector.html#gtoc-picker)
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
  * [](https://nodejs.org/docs/latest/api/inspector.html#alt-docs)
    1. [25.x ](https://nodejs.org/docs/latest-v25.x/api/inspector.html)
    2. [24.x ](https://nodejs.org/docs/latest-v24.x/api/inspector.html)
    3. [23.x ](https://nodejs.org/docs/latest-v23.x/api/inspector.html)
    4. [22.x **LTS**](https://nodejs.org/docs/latest-v22.x/api/inspector.html)
    5. [21.x ](https://nodejs.org/docs/latest-v21.x/api/inspector.html)
    6. [20.x **LTS**](https://nodejs.org/docs/latest-v20.x/api/inspector.html)
    7. [19.x ](https://nodejs.org/docs/latest-v19.x/api/inspector.html)
    8. [18.x ](https://nodejs.org/docs/latest-v18.x/api/inspector.html)
    9. [17.x ](https://nodejs.org/docs/latest-v17.x/api/inspector.html)
    10. [16.x ](https://nodejs.org/docs/latest-v16.x/api/inspector.html)
    11. [15.x ](https://nodejs.org/docs/latest-v15.x/api/inspector.html)
    12. [14.x ](https://nodejs.org/docs/latest-v14.x/api/inspector.html)
    13. [13.x ](https://nodejs.org/docs/latest-v13.x/api/inspector.html)
    14. [12.x ](https://nodejs.org/docs/latest-v12.x/api/inspector.html)
    15. [11.x ](https://nodejs.org/docs/latest-v11.x/api/inspector.html)
    16. [10.x ](https://nodejs.org/docs/latest-v10.x/api/inspector.html)
    17. [9.x ](https://nodejs.org/docs/latest-v9.x/api/inspector.html)
    18. [8.x ](https://nodejs.org/docs/latest-v8.x/api/inspector.html)
  * [ ](https://nodejs.org/docs/latest/api/inspector.html#options-picker)
    * [View on single page](https://nodejs.org/docs/latest/api/all.html)
    * [View as JSON](https://nodejs.org/docs/latest/api/inspector.json)


* * *
Table of contents
  * [Inspector](https://nodejs.org/docs/latest/api/inspector.html#inspector)
    * [Promises API](https://nodejs.org/docs/latest/api/inspector.html#promises-api)
      * [Class: `inspector.Session`](https://nodejs.org/docs/latest/api/inspector.html#class-inspectorsession)
        * [`new inspector.Session()`](https://nodejs.org/docs/latest/api/inspector.html#new-inspectorsession)
        * [Event: `'inspectorNotification'`](https://nodejs.org/docs/latest/api/inspector.html#event-inspectornotification)
        * [Event: `<inspector-protocol-method>`](https://nodejs.org/docs/latest/api/inspector.html#event-inspector-protocol-method)
        * [`session.connect()`](https://nodejs.org/docs/latest/api/inspector.html#sessionconnect)
        * [`session.connectToMainThread()`](https://nodejs.org/docs/latest/api/inspector.html#sessionconnecttomainthread)
        * [`session.disconnect()`](https://nodejs.org/docs/latest/api/inspector.html#sessiondisconnect)
        * [`session.post(method[, params])`](https://nodejs.org/docs/latest/api/inspector.html#sessionpostmethod-params)
        * [Example usage](https://nodejs.org/docs/latest/api/inspector.html#example-usage)
    * [Callback API](https://nodejs.org/docs/latest/api/inspector.html#callback-api)
      * [Class: `inspector.Session`](https://nodejs.org/docs/latest/api/inspector.html#class-inspectorsession-1)
        * [`new inspector.Session()`](https://nodejs.org/docs/latest/api/inspector.html#new-inspectorsession-1)
        * [Event: `'inspectorNotification'`](https://nodejs.org/docs/latest/api/inspector.html#event-inspectornotification-1)
        * [Event: `<inspector-protocol-method>`;](https://nodejs.org/docs/latest/api/inspector.html#event-inspector-protocol-method-1)
        * [`session.connect()`](https://nodejs.org/docs/latest/api/inspector.html#sessionconnect-1)
        * [`session.connectToMainThread()`](https://nodejs.org/docs/latest/api/inspector.html#sessionconnecttomainthread-1)
        * [`session.disconnect()`](https://nodejs.org/docs/latest/api/inspector.html#sessiondisconnect-1)
        * [`session.post(method[, params][, callback])`](https://nodejs.org/docs/latest/api/inspector.html#sessionpostmethod-params-callback)
        * [Example usage](https://nodejs.org/docs/latest/api/inspector.html#example-usage-1)
    * [Common Objects](https://nodejs.org/docs/latest/api/inspector.html#common-objects)
      * [`inspector.close()`](https://nodejs.org/docs/latest/api/inspector.html#inspectorclose)
      * [`inspector.console`](https://nodejs.org/docs/latest/api/inspector.html#inspectorconsole)
      * [`inspector.open([port[, host[, wait]]])`](https://nodejs.org/docs/latest/api/inspector.html#inspectoropenport-host-wait)
      * [`inspector.url()`](https://nodejs.org/docs/latest/api/inspector.html#inspectorurl)
      * [`inspector.waitForDebugger()`](https://nodejs.org/docs/latest/api/inspector.html#inspectorwaitfordebugger)
    * [Integration with DevTools](https://nodejs.org/docs/latest/api/inspector.html#integration-with-devtools)
      * [`inspector.Network.dataReceived([params])`](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkdatareceivedparams)
      * [`inspector.Network.dataSent([params])`](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkdatasentparams)
      * [`inspector.Network.requestWillBeSent([params])`](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkrequestwillbesentparams)
      * [`inspector.Network.responseReceived([params])`](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkresponsereceivedparams)
      * [`inspector.Network.loadingFinished([params])`](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkloadingfinishedparams)
      * [`inspector.Network.loadingFailed([params])`](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkloadingfailedparams)
      * [`inspector.Network.webSocketCreated([params])`](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkwebsocketcreatedparams)
      * [`inspector.Network.webSocketHandshakeResponseReceived([params])`](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkwebsockethandshakeresponsereceivedparams)
      * [`inspector.Network.webSocketClosed([params])`](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkwebsocketclosedparams)
      * [`inspector.NetworkResources.put`](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkresourcesput)
      * [`inspector.DOMStorage.domStorageItemAdded`](https://nodejs.org/docs/latest/api/inspector.html#inspectordomstoragedomstorageitemadded)
      * [`inspector.DOMStorage.domStorageItemRemoved`](https://nodejs.org/docs/latest/api/inspector.html#inspectordomstoragedomstorageitemremoved)
      * [`inspector.DOMStorage.domStorageItemUpdated`](https://nodejs.org/docs/latest/api/inspector.html#inspectordomstoragedomstorageitemupdated)
      * [`inspector.DOMStorage.domStorageItemsCleared`](https://nodejs.org/docs/latest/api/inspector.html#inspectordomstoragedomstorageitemscleared)
      * [`inspector.DOMStorage.registerStorage`](https://nodejs.org/docs/latest/api/inspector.html#inspectordomstorageregisterstorage)
    * [Support of breakpoints](https://nodejs.org/docs/latest/api/inspector.html#support-of-breakpoints)


## Inspector[#](https://nodejs.org/docs/latest/api/inspector.html#inspector)
**Source Code:**
[Stability: 2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Stable
The `node:inspector` module provides an API for interacting with the V8 inspector.
It can be accessed using:
```
import * as inspector from 'node:inspector/promises';
const inspector = require('node:inspector/promises');
copy
```

or
```
import * as inspector from 'node:inspector';
const inspector = require('node:inspector');
copy
```

### Promises API[#](https://nodejs.org/docs/latest/api/inspector.html#promises-api)
Added in: v19.0.0
Stability: 1 - Experimental
#### Class: `inspector.Session`[#](https://nodejs.org/docs/latest/api/inspector.html#class-inspectorsession)
  * Extends: [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter)


The `inspector.Session` is used for dispatching messages to the V8 inspector back-end and receiving message responses and notifications.
#####  `new inspector.Session()`[#](https://nodejs.org/docs/latest/api/inspector.html#new-inspectorsession)
Added in: v8.0.0
Create a new instance of the `inspector.Session` class. The inspector session needs to be connected through [`session.connect()`](https://nodejs.org/docs/latest/api/inspector.html#sessionconnect) before the messages can be dispatched to the inspector backend.
When using `Session`, the object outputted by the console API will not be released, unless we performed manually `Runtime.DiscardConsoleEntries` command.
##### Event: `'inspectorNotification'`[#](https://nodejs.org/docs/latest/api/inspector.html#event-inspectornotification)
Added in: v8.0.0
  * Type:


Emitted when any notification from the V8 Inspector is received.
```
session.on('inspectorNotification', (message) => console.log(message.method));
// Debugger.paused
// Debugger.resumed
copy
```

> **Caveat** Breakpoints with same-thread session is not recommended, see [support of breakpoints](https://nodejs.org/docs/latest/api/inspector.html#support-of-breakpoints).
It is also possible to subscribe only to notifications with specific method:
##### Event: `<inspector-protocol-method>`[#](https://nodejs.org/docs/latest/api/inspector.html#event-inspector-protocol-method)
Added in: v8.0.0
  * Type:


Emitted when an inspector notification is received that has its method field set to the `<inspector-protocol-method>` value.
The following snippet installs a listener on the
```
session.on('Debugger.paused', ({ params }) => {
  console.log(params.hitBreakpoints);
});
// [ '/the/file/that/has/the/breakpoint.js:11:0' ]
copy
```

> **Caveat** Breakpoints with same-thread session is not recommended, see [support of breakpoints](https://nodejs.org/docs/latest/api/inspector.html#support-of-breakpoints).
#####  `session.connect()`[#](https://nodejs.org/docs/latest/api/inspector.html#sessionconnect)
Added in: v8.0.0
Connects a session to the inspector back-end.
#####  `session.connectToMainThread()`[#](https://nodejs.org/docs/latest/api/inspector.html#sessionconnecttomainthread)
Added in: v12.11.0
Connects a session to the main thread inspector back-end. An exception will be thrown if this API was not called on a Worker thread.
#####  `session.disconnect()`[#](https://nodejs.org/docs/latest/api/inspector.html#sessiondisconnect)
Added in: v8.0.0
Immediately close the session. All pending message callbacks will be called with an error. [`session.connect()`](https://nodejs.org/docs/latest/api/inspector.html#sessionconnect) will need to be called to be able to send messages again. Reconnected session will lose all inspector state, such as enabled agents or configured breakpoints.
#####  `session.post(method[, params])`[#](https://nodejs.org/docs/latest/api/inspector.html#sessionpostmethod-params)
Added in: v19.0.0
  * `method`
  * `params`
  * Returns:


Posts a message to the inspector back-end.
```
import { Session } from 'node:inspector/promises';
try {
  const session = new Session();
  session.connect();
  const result = await session.post('Runtime.evaluate', { expression: '2 + 2' });
  console.log(result);
} catch (error) {
  console.error(error);
}
// Output: { result: { type: 'number', value: 4, description: '4' } }
copy
```

The latest version of the V8 inspector protocol is published on the
Node.js inspector supports all the Chrome DevTools Protocol domains declared by V8. Chrome DevTools Protocol domain provides an interface for interacting with one of the runtime agents used to inspect the application state and listen to the run-time events.
##### Example usage[#](https://nodejs.org/docs/latest/api/inspector.html#example-usage)
Apart from the debugger, various V8 Profilers are available through the DevTools protocol.
###### CPU profiler[#](https://nodejs.org/docs/latest/api/inspector.html#cpu-profiler)
Here's an example showing how to use the
```
import { Session } from 'node:inspector/promises';
import fs from 'node:fs';
const session = new Session();
session.connect();

await session.post('Profiler.enable');
await session.post('Profiler.start');
// Invoke business logic under measurement here...

// some time later...
const { profile } = await session.post('Profiler.stop');

// Write profile to disk, upload, etc.
fs.writeFileSync('./profile.cpuprofile', JSON.stringify(profile));
copy
```

###### Heap profiler[#](https://nodejs.org/docs/latest/api/inspector.html#heap-profiler)
Here's an example showing how to use the
```
import { Session } from 'node:inspector/promises';
import fs from 'node:fs';
const session = new Session();

const fd = fs.openSync('profile.heapsnapshot', 'w');

session.connect();

session.on('HeapProfiler.addHeapSnapshotChunk', (m) => {
  fs.writeSync(fd, m.params.chunk);
});

const result = await session.post('HeapProfiler.takeHeapSnapshot', null);
console.log('HeapProfiler.takeHeapSnapshot done:', result);
session.disconnect();
fs.closeSync(fd);
copy
```

### Callback API[#](https://nodejs.org/docs/latest/api/inspector.html#callback-api)
#### Class: `inspector.Session`[#](https://nodejs.org/docs/latest/api/inspector.html#class-inspectorsession-1)
  * Extends: [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter)


The `inspector.Session` is used for dispatching messages to the V8 inspector back-end and receiving message responses and notifications.
#####  `new inspector.Session()`[#](https://nodejs.org/docs/latest/api/inspector.html#new-inspectorsession-1)
Added in: v8.0.0
Create a new instance of the `inspector.Session` class. The inspector session needs to be connected through [`session.connect()`](https://nodejs.org/docs/latest/api/inspector.html#sessionconnect) before the messages can be dispatched to the inspector backend.
When using `Session`, the object outputted by the console API will not be released, unless we performed manually `Runtime.DiscardConsoleEntries` command.
##### Event: `'inspectorNotification'`[#](https://nodejs.org/docs/latest/api/inspector.html#event-inspectornotification-1)
Added in: v8.0.0
  * Type:


Emitted when any notification from the V8 Inspector is received.
```
session.on('inspectorNotification', (message) => console.log(message.method));
// Debugger.paused
// Debugger.resumed
copy
```

> **Caveat** Breakpoints with same-thread session is not recommended, see [support of breakpoints](https://nodejs.org/docs/latest/api/inspector.html#support-of-breakpoints).
It is also possible to subscribe only to notifications with specific method:
##### Event: `<inspector-protocol-method>`;[#](https://nodejs.org/docs/latest/api/inspector.html#event-inspector-protocol-method-1)
Added in: v8.0.0
  * Type:


Emitted when an inspector notification is received that has its method field set to the `<inspector-protocol-method>` value.
The following snippet installs a listener on the
```
session.on('Debugger.paused', ({ params }) => {
  console.log(params.hitBreakpoints);
});
// [ '/the/file/that/has/the/breakpoint.js:11:0' ]
copy
```

> **Caveat** Breakpoints with same-thread session is not recommended, see [support of breakpoints](https://nodejs.org/docs/latest/api/inspector.html#support-of-breakpoints).
#####  `session.connect()`[#](https://nodejs.org/docs/latest/api/inspector.html#sessionconnect-1)
Added in: v8.0.0
Connects a session to the inspector back-end.
#####  `session.connectToMainThread()`[#](https://nodejs.org/docs/latest/api/inspector.html#sessionconnecttomainthread-1)
Added in: v12.11.0
Connects a session to the main thread inspector back-end. An exception will be thrown if this API was not called on a Worker thread.
#####  `session.disconnect()`[#](https://nodejs.org/docs/latest/api/inspector.html#sessiondisconnect-1)
Added in: v8.0.0
Immediately close the session. All pending message callbacks will be called with an error. [`session.connect()`](https://nodejs.org/docs/latest/api/inspector.html#sessionconnect) will need to be called to be able to send messages again. Reconnected session will lose all inspector state, such as enabled agents or configured breakpoints.
#####  `session.post(method[, params][, callback])`[#](https://nodejs.org/docs/latest/api/inspector.html#sessionpostmethod-params-callback)
Added in: v8.0.0History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `method`
  * `params`
  * `callback`


Posts a message to the inspector back-end. `callback` will be notified when a response is received. `callback` is a function that accepts two optional arguments: error and message-specific result.
```
session.post('Runtime.evaluate', { expression: '2 + 2' },
             (error, { result }) => console.log(result));
// Output: { type: 'number', value: 4, description: '4' }
copy
```

The latest version of the V8 inspector protocol is published on the
Node.js inspector supports all the Chrome DevTools Protocol domains declared by V8. Chrome DevTools Protocol domain provides an interface for interacting with one of the runtime agents used to inspect the application state and listen to the run-time events.
You can not set `reportProgress` to `true` when sending a `HeapProfiler.takeHeapSnapshot` or `HeapProfiler.stopTrackingHeapObjects` command to V8.
##### Example usage[#](https://nodejs.org/docs/latest/api/inspector.html#example-usage-1)
Apart from the debugger, various V8 Profilers are available through the DevTools protocol.
###### CPU profiler[#](https://nodejs.org/docs/latest/api/inspector.html#cpu-profiler-1)
Here's an example showing how to use the
```
const inspector = require('node:inspector');
const fs = require('node:fs');
const session = new inspector.Session();
session.connect();

session.post('Profiler.enable', () => {
  session.post('Profiler.start', () => {
    // Invoke business logic under measurement here...

    // some time later...
    session.post('Profiler.stop', (err, { profile }) => {
      // Write profile to disk, upload, etc.
      if (!err) {
        fs.writeFileSync('./profile.cpuprofile', JSON.stringify(profile));
      }
    });
  });
});
copy
```

###### Heap profiler[#](https://nodejs.org/docs/latest/api/inspector.html#heap-profiler-1)
Here's an example showing how to use the
```
const inspector = require('node:inspector');
const fs = require('node:fs');
const session = new inspector.Session();

const fd = fs.openSync('profile.heapsnapshot', 'w');

session.connect();

session.on('HeapProfiler.addHeapSnapshotChunk', (m) => {
  fs.writeSync(fd, m.params.chunk);
});

session.post('HeapProfiler.takeHeapSnapshot', null, (err, r) => {
  console.log('HeapProfiler.takeHeapSnapshot done:', err, r);
  session.disconnect();
  fs.closeSync(fd);
});
copy
```

### Common Objects[#](https://nodejs.org/docs/latest/api/inspector.html#common-objects)
####  `inspector.close()`[#](https://nodejs.org/docs/latest/api/inspector.html#inspectorclose)
Added in: v9.0.0History Version | Changes
---|---
v18.10.0 | The API is exposed in the worker threads.
Attempts to close all remaining connections, blocking the event loop until all are closed. Once all connections are closed, deactivates the inspector.
####  `inspector.console`[#](https://nodejs.org/docs/latest/api/inspector.html#inspectorconsole)
  * Type:

```
require('node:inspector').console.log('a message');
copy
```

The inspector console does not have API parity with Node.js console.
####  `inspector.open([port[, host[, wait]]])`[#](https://nodejs.org/docs/latest/api/inspector.html#inspectoropenport-host-wait)
History Version | Changes
---|---
v20.6.0 | inspector.open() now returns a `Disposable` object.
  * `port` **Default:** what was specified on the CLI.
  * `host` **Default:** what was specified on the CLI.
  * `wait` **Default:** `false`.
  * Returns: [`inspector.close()`](https://nodejs.org/docs/latest/api/inspector.html#inspectorclose).


Activate inspector on host and port. Equivalent to `node --inspect=[[host:]port]`, but can be done programmatically after node has started.
If wait is `true`, will block until a client has connected to the inspect port and flow control has been passed to the debugger client.
See the [security warning](https://nodejs.org/docs/latest/api/cli.html#warning-binding-inspector-to-a-public-ipport-combination-is-insecure) regarding the `host` parameter usage.
####  `inspector.url()`[#](https://nodejs.org/docs/latest/api/inspector.html#inspectorurl)
  * Returns:


Return the URL of the active inspector, or `undefined` if there is none.
```
$ node --inspect -p 'inspector.url()'
Debugger listening on ws://127.0.0.1:9229/166e272e-7a30-4d09-97ce-f1c012b43c34
For help, see: https://nodejs.org/en/docs/inspector
ws://127.0.0.1:9229/166e272e-7a30-4d09-97ce-f1c012b43c34

$ node --inspect=localhost:3000 -p 'inspector.url()'
Debugger listening on ws://localhost:3000/51cf8d0e-3c36-4c59-8efd-54519839e56a
For help, see: https://nodejs.org/en/docs/inspector
ws://localhost:3000/51cf8d0e-3c36-4c59-8efd-54519839e56a

$ node -p 'inspector.url()'
undefined
copy
```

####  `inspector.waitForDebugger()`[#](https://nodejs.org/docs/latest/api/inspector.html#inspectorwaitfordebugger)
Added in: v12.7.0
Blocks until a client (existing or connected later) has sent `Runtime.runIfWaitingForDebugger` command.
An exception will be thrown if there is no active inspector.
### Integration with DevTools[#](https://nodejs.org/docs/latest/api/inspector.html#integration-with-devtools)
Stability: 1.1 - Active development
The `node:inspector` module provides an API for integrating with devtools that support Chrome DevTools Protocol. DevTools frontends connected to a running Node.js instance can capture protocol events emitted from the instance and display them accordingly to facilitate debugging. The following methods broadcast a protocol event to all connected frontends. The `params` passed to the methods can be optional, depending on the protocol.
```
// The `Network.requestWillBeSent` event will be fired.
inspector.Network.requestWillBeSent({
  requestId: 'request-id-1',
  timestamp: Date.now() / 1000,
  wallTime: Date.now(),
  request: {
    url: 'https://nodejs.org/en',
    method: 'GET',
  },
});
copy
```

####  `inspector.Network.dataReceived([params])`[#](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkdatareceivedparams)
Added in: v24.2.0, v22.17.0
  * `params`


This feature is only available with the `--experimental-network-inspection` flag enabled.
Broadcasts the `Network.dataReceived` event to connected frontends, or buffers the data if `Network.streamResourceContent` command was not invoked for the given request yet.
Also enables `Network.getResponseBody` command to retrieve the response data.
####  `inspector.Network.dataSent([params])`[#](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkdatasentparams)
Added in: v24.3.0, v22.18.0
  * `params`


This feature is only available with the `--experimental-network-inspection` flag enabled.
Enables `Network.getRequestPostData` command to retrieve the request data.
####  `inspector.Network.requestWillBeSent([params])`[#](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkrequestwillbesentparams)
Added in: v22.6.0, v20.18.0
  * `params`


This feature is only available with the `--experimental-network-inspection` flag enabled.
Broadcasts the `Network.requestWillBeSent` event to connected frontends. This event indicates that the application is about to send an HTTP request.
####  `inspector.Network.responseReceived([params])`[#](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkresponsereceivedparams)
Added in: v22.6.0, v20.18.0
  * `params`


This feature is only available with the `--experimental-network-inspection` flag enabled.
Broadcasts the `Network.responseReceived` event to connected frontends. This event indicates that HTTP response is available.
####  `inspector.Network.loadingFinished([params])`[#](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkloadingfinishedparams)
Added in: v22.6.0, v20.18.0
  * `params`


This feature is only available with the `--experimental-network-inspection` flag enabled.
Broadcasts the `Network.loadingFinished` event to connected frontends. This event indicates that HTTP request has finished loading.
####  `inspector.Network.loadingFailed([params])`[#](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkloadingfailedparams)
Added in: v22.7.0, v20.18.0
  * `params`


This feature is only available with the `--experimental-network-inspection` flag enabled.
Broadcasts the `Network.loadingFailed` event to connected frontends. This event indicates that HTTP request has failed to load.
####  `inspector.Network.webSocketCreated([params])`[#](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkwebsocketcreatedparams)
Added in: v24.7.0
  * `params`


This feature is only available with the `--experimental-network-inspection` flag enabled.
Broadcasts the `Network.webSocketCreated` event to connected frontends. This event indicates that a WebSocket connection has been initiated.
####  `inspector.Network.webSocketHandshakeResponseReceived([params])`[#](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkwebsockethandshakeresponsereceivedparams)
Added in: v24.7.0
  * `params`


This feature is only available with the `--experimental-network-inspection` flag enabled.
Broadcasts the `Network.webSocketHandshakeResponseReceived` event to connected frontends. This event indicates that the WebSocket handshake response has been received.
####  `inspector.Network.webSocketClosed([params])`[#](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkwebsocketclosedparams)
Added in: v24.7.0
  * `params`


This feature is only available with the `--experimental-network-inspection` flag enabled.
Broadcasts the `Network.webSocketClosed` event to connected frontends. This event indicates that a WebSocket connection has been closed.
####  `inspector.NetworkResources.put`[#](https://nodejs.org/docs/latest/api/inspector.html#inspectornetworkresourcesput)
Added in: v24.5.0, v22.19.0
Stability: 1.1 - Active Development
This feature is only available with the `--experimental-inspector-network-resource` flag enabled.
The inspector.NetworkResources.put method is used to provide a response for a loadNetworkResource request issued via the Chrome DevTools Protocol (CDP). This is typically triggered when a source map is specified by URL, and a DevTools frontend—such as Chrome—requests the resource to retrieve the source map.
This method allows developers to predefine the resource content to be served in response to such CDP requests.
```
const inspector = require('node:inspector');
// By preemptively calling put to register the resource, a source map can be resolved when
// a loadNetworkResource request is made from the frontend.
async function setNetworkResources() {
  const mapUrl = 'http://localhost:3000/dist/app.js.map';
  const tsUrl = 'http://localhost:3000/src/app.ts';
  const distAppJsMap = await fetch(mapUrl).then((res) => res.text());
  const srcAppTs = await fetch(tsUrl).then((res) => res.text());
  inspector.NetworkResources.put(mapUrl, distAppJsMap);
  inspector.NetworkResources.put(tsUrl, srcAppTs);
};
setNetworkResources().then(() => {
  require('./dist/app');
});
copy
```

For more details, see the official CDP documentation:
####  `inspector.DOMStorage.domStorageItemAdded`[#](https://nodejs.org/docs/latest/api/inspector.html#inspectordomstoragedomstorageitemadded)
Added in: v25.5.0
  * `params`
    * `storageId`
      * `securityOrigin`
      * `storageKey`
      * `isLocalStorage`
    * `key`
    * `newValue`


This feature is only available with the `--experimental-storage-inspection` flag enabled.
Broadcasts the `DOMStorage.domStorageItemAdded` event to connected frontends. This event indicates that a new item has been added to the storage.
####  `inspector.DOMStorage.domStorageItemRemoved`[#](https://nodejs.org/docs/latest/api/inspector.html#inspectordomstoragedomstorageitemremoved)
Added in: v25.5.0
  * `params`
    * `storageId`
      * `securityOrigin`
      * `storageKey`
      * `isLocalStorage`
    * `key`


This feature is only available with the `--experimental-storage-inspection` flag enabled.
Broadcasts the `DOMStorage.domStorageItemRemoved` event to connected frontends. This event indicates that an item has been removed from the storage.
####  `inspector.DOMStorage.domStorageItemUpdated`[#](https://nodejs.org/docs/latest/api/inspector.html#inspectordomstoragedomstorageitemupdated)
Added in: v25.5.0
  * `params`
    * `storageId`
      * `securityOrigin`
      * `storageKey`
      * `isLocalStorage`
    * `key`
    * `oldValue`
    * `newValue`


This feature is only available with the `--experimental-storage-inspection` flag enabled.
Broadcasts the `DOMStorage.domStorageItemUpdated` event to connected frontends. This event indicates that a storage item has been updated.
####  `inspector.DOMStorage.domStorageItemsCleared`[#](https://nodejs.org/docs/latest/api/inspector.html#inspectordomstoragedomstorageitemscleared)
Added in: v25.5.0
  * `params`
    * `storageId`
      * `securityOrigin`
      * `storageKey`
      * `isLocalStorage`


This feature is only available with the `--experimental-storage-inspection` flag enabled.
Broadcasts the `DOMStorage.domStorageItemsCleared` event to connected frontends. This event indicates that all items have been cleared from the storage.
####  `inspector.DOMStorage.registerStorage`[#](https://nodejs.org/docs/latest/api/inspector.html#inspectordomstorageregisterstorage)
Added in: v25.5.0
  * `params`
    * `isLocalStorage`
    * `storageMap`


This feature is only available with the `--experimental-storage-inspection` flag enabled.
### Support of breakpoints[#](https://nodejs.org/docs/latest/api/inspector.html#support-of-breakpoints)
The Chrome DevTools Protocol `inspector.Session` to attach to a program and set breakpoints to step through the codes.
However, setting breakpoints with a same-thread `inspector.Session`, which is connected by [`session.connect()`](https://nodejs.org/docs/latest/api/inspector.html#sessionconnect), should be avoided as the program being attached and paused is exactly the debugger itself. Instead, try connect to the main thread by [`session.connectToMainThread()`](https://nodejs.org/docs/latest/api/inspector.html#sessionconnecttomainthread) and set breakpoints in a worker thread, or connect with a [Debugger](https://nodejs.org/docs/latest/api/debugger.html) program over WebSocket connection.
