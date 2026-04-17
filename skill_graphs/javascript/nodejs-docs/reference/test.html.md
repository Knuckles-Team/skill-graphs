[Skip to content](https://nodejs.org/docs/latest/api/test.html#apicontent)
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
  * [](https://nodejs.org/docs/latest/api/test.html#toc-picker)
    * [Test runner](https://nodejs.org/docs/latest/api/test.html#test-runner)
      * [Subtests](https://nodejs.org/docs/latest/api/test.html#subtests)
      * [Rerunning failed tests](https://nodejs.org/docs/latest/api/test.html#rerunning-failed-tests)
      * [`describe()` and `it()` aliases](https://nodejs.org/docs/latest/api/test.html#describe-and-it-aliases)
      * [Skipping tests](https://nodejs.org/docs/latest/api/test.html#skipping-tests)
      * [TODO tests](https://nodejs.org/docs/latest/api/test.html#todo-tests)
      * [Expecting tests to fail](https://nodejs.org/docs/latest/api/test.html#expecting-tests-to-fail)
      * [`only` tests](https://nodejs.org/docs/latest/api/test.html#only-tests)
      * [Filtering tests by name](https://nodejs.org/docs/latest/api/test.html#filtering-tests-by-name)
      * [Extraneous asynchronous activity](https://nodejs.org/docs/latest/api/test.html#extraneous-asynchronous-activity)
      * [Watch mode](https://nodejs.org/docs/latest/api/test.html#watch-mode)
      * [Global setup and teardown](https://nodejs.org/docs/latest/api/test.html#global-setup-and-teardown)
      * [Running tests from the command line](https://nodejs.org/docs/latest/api/test.html#running-tests-from-the-command-line)
        * [Test runner execution model](https://nodejs.org/docs/latest/api/test.html#test-runner-execution-model)
          * [Child process option inheritance](https://nodejs.org/docs/latest/api/test.html#child-process-option-inheritance)
      * [Collecting code coverage](https://nodejs.org/docs/latest/api/test.html#collecting-code-coverage)
        * [Coverage reporters](https://nodejs.org/docs/latest/api/test.html#coverage-reporters)
      * [Mocking](https://nodejs.org/docs/latest/api/test.html#mocking)
        * [Timers](https://nodejs.org/docs/latest/api/test.html#timers)
        * [Dates](https://nodejs.org/docs/latest/api/test.html#dates)
      * [Snapshot testing](https://nodejs.org/docs/latest/api/test.html#snapshot-testing)
      * [Test reporters](https://nodejs.org/docs/latest/api/test.html#test-reporters)
        * [Custom reporters](https://nodejs.org/docs/latest/api/test.html#custom-reporters)
        * [Multiple reporters](https://nodejs.org/docs/latest/api/test.html#multiple-reporters)
      * [`run([options])`](https://nodejs.org/docs/latest/api/test.html#runoptions)
      * [`suite([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#suitename-options-fn)
      * [`suite.skip([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#suiteskipname-options-fn)
      * [`suite.todo([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#suitetodoname-options-fn)
      * [`suite.only([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#suiteonlyname-options-fn)
      * [`test([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#testname-options-fn)
      * [`test.skip([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#testskipname-options-fn)
      * [`test.todo([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#testtodoname-options-fn)
      * [`test.only([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#testonlyname-options-fn)
      * [`describe([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#describename-options-fn)
      * [`describe.skip([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#describeskipname-options-fn)
      * [`describe.todo([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#describetodoname-options-fn)
      * [`describe.only([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#describeonlyname-options-fn)
      * [`it([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#itname-options-fn)
      * [`it.skip([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#itskipname-options-fn)
      * [`it.todo([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#ittodoname-options-fn)
      * [`it.only([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#itonlyname-options-fn)
      * [`before([fn][, options])`](https://nodejs.org/docs/latest/api/test.html#beforefn-options)
      * [`after([fn][, options])`](https://nodejs.org/docs/latest/api/test.html#afterfn-options)
      * [`beforeEach([fn][, options])`](https://nodejs.org/docs/latest/api/test.html#beforeeachfn-options)
      * [`afterEach([fn][, options])`](https://nodejs.org/docs/latest/api/test.html#aftereachfn-options)
      * [`assert`](https://nodejs.org/docs/latest/api/test.html#assert)
        * [`assert.register(name, fn)`](https://nodejs.org/docs/latest/api/test.html#assertregistername-fn)
      * [`snapshot`](https://nodejs.org/docs/latest/api/test.html#snapshot)
        * [`snapshot.setDefaultSnapshotSerializers(serializers)`](https://nodejs.org/docs/latest/api/test.html#snapshotsetdefaultsnapshotserializersserializers)
        * [`snapshot.setResolveSnapshotPath(fn)`](https://nodejs.org/docs/latest/api/test.html#snapshotsetresolvesnapshotpathfn)
      * [Class: `MockFunctionContext`](https://nodejs.org/docs/latest/api/test.html#class-mockfunctioncontext)
        * [`ctx.calls`](https://nodejs.org/docs/latest/api/test.html#ctxcalls)
        * [`ctx.callCount()`](https://nodejs.org/docs/latest/api/test.html#ctxcallcount)
        * [`ctx.mockImplementation(implementation)`](https://nodejs.org/docs/latest/api/test.html#ctxmockimplementationimplementation)
        * [`ctx.mockImplementationOnce(implementation[, onCall])`](https://nodejs.org/docs/latest/api/test.html#ctxmockimplementationonceimplementation-oncall)
        * [`ctx.resetCalls()`](https://nodejs.org/docs/latest/api/test.html#ctxresetcalls)
        * [`ctx.restore()`](https://nodejs.org/docs/latest/api/test.html#ctxrestore)
      * [Class: `MockModuleContext`](https://nodejs.org/docs/latest/api/test.html#class-mockmodulecontext)
        * [`ctx.restore()`](https://nodejs.org/docs/latest/api/test.html#ctxrestore-1)
      * [Class: `MockPropertyContext`](https://nodejs.org/docs/latest/api/test.html#class-mockpropertycontext)
        * [`ctx.accesses`](https://nodejs.org/docs/latest/api/test.html#ctxaccesses)
        * [`ctx.accessCount()`](https://nodejs.org/docs/latest/api/test.html#ctxaccesscount)
        * [`ctx.mockImplementation(value)`](https://nodejs.org/docs/latest/api/test.html#ctxmockimplementationvalue)
        * [`ctx.mockImplementationOnce(value[, onAccess])`](https://nodejs.org/docs/latest/api/test.html#ctxmockimplementationoncevalue-onaccess)
          * [Caveat](https://nodejs.org/docs/latest/api/test.html#caveat)
        * [`ctx.resetAccesses()`](https://nodejs.org/docs/latest/api/test.html#ctxresetaccesses)
        * [`ctx.restore()`](https://nodejs.org/docs/latest/api/test.html#ctxrestore-2)
      * [Class: `MockTracker`](https://nodejs.org/docs/latest/api/test.html#class-mocktracker)
        * [`mock.fn([original[, implementation]][, options])`](https://nodejs.org/docs/latest/api/test.html#mockfnoriginal-implementation-options)
        * [`mock.getter(object, methodName[, implementation][, options])`](https://nodejs.org/docs/latest/api/test.html#mockgetterobject-methodname-implementation-options)
        * [`mock.method(object, methodName[, implementation][, options])`](https://nodejs.org/docs/latest/api/test.html#mockmethodobject-methodname-implementation-options)
        * [`mock.module(specifier[, options])`](https://nodejs.org/docs/latest/api/test.html#mockmodulespecifier-options)
        * [`mock.property(object, propertyName[, value])`](https://nodejs.org/docs/latest/api/test.html#mockpropertyobject-propertyname-value)
        * [`mock.reset()`](https://nodejs.org/docs/latest/api/test.html#mockreset)
        * [`mock.restoreAll()`](https://nodejs.org/docs/latest/api/test.html#mockrestoreall)
        * [`mock.setter(object, methodName[, implementation][, options])`](https://nodejs.org/docs/latest/api/test.html#mocksetterobject-methodname-implementation-options)
      * [Class: `MockTimers`](https://nodejs.org/docs/latest/api/test.html#class-mocktimers)
        * [`timers.enable([enableOptions])`](https://nodejs.org/docs/latest/api/test.html#timersenableenableoptions)
        * [`timers.reset()`](https://nodejs.org/docs/latest/api/test.html#timersreset)
        * [`timers[Symbol.dispose]()`](https://nodejs.org/docs/latest/api/test.html#timerssymboldispose)
        * [`timers.tick([milliseconds])`](https://nodejs.org/docs/latest/api/test.html#timerstickmilliseconds)
          * [Using clear functions](https://nodejs.org/docs/latest/api/test.html#using-clear-functions)
          * [Working with Node.js timers modules](https://nodejs.org/docs/latest/api/test.html#working-with-nodejs-timers-modules)
        * [`timers.runAll()`](https://nodejs.org/docs/latest/api/test.html#timersrunall)
        * [`timers.setTime(milliseconds)`](https://nodejs.org/docs/latest/api/test.html#timerssettimemilliseconds)
          * [Dates and Timers working together](https://nodejs.org/docs/latest/api/test.html#dates-and-timers-working-together)
      * [Class: `TestsStream`](https://nodejs.org/docs/latest/api/test.html#class-testsstream)
        * [Event: `'test:coverage'`](https://nodejs.org/docs/latest/api/test.html#event-testcoverage)
        * [Event: `'test:complete'`](https://nodejs.org/docs/latest/api/test.html#event-testcomplete)
        * [Event: `'test:dequeue'`](https://nodejs.org/docs/latest/api/test.html#event-testdequeue)
        * [Event: `'test:diagnostic'`](https://nodejs.org/docs/latest/api/test.html#event-testdiagnostic)
        * [Event: `'test:enqueue'`](https://nodejs.org/docs/latest/api/test.html#event-testenqueue)
        * [Event: `'test:fail'`](https://nodejs.org/docs/latest/api/test.html#event-testfail)
        * [Event: `'test:interrupted'`](https://nodejs.org/docs/latest/api/test.html#event-testinterrupted)
        * [Event: `'test:pass'`](https://nodejs.org/docs/latest/api/test.html#event-testpass)
        * [Event: `'test:plan'`](https://nodejs.org/docs/latest/api/test.html#event-testplan)
        * [Event: `'test:start'`](https://nodejs.org/docs/latest/api/test.html#event-teststart)
        * [Event: `'test:stderr'`](https://nodejs.org/docs/latest/api/test.html#event-teststderr)
        * [Event: `'test:stdout'`](https://nodejs.org/docs/latest/api/test.html#event-teststdout)
        * [Event: `'test:summary'`](https://nodejs.org/docs/latest/api/test.html#event-testsummary)
        * [Event: `'test:watch:drained'`](https://nodejs.org/docs/latest/api/test.html#event-testwatchdrained)
        * [Event: `'test:watch:restarted'`](https://nodejs.org/docs/latest/api/test.html#event-testwatchrestarted)
      * [Class: `TestContext`](https://nodejs.org/docs/latest/api/test.html#class-testcontext)
        * [`context.before([fn][, options])`](https://nodejs.org/docs/latest/api/test.html#contextbeforefn-options)
        * [`context.beforeEach([fn][, options])`](https://nodejs.org/docs/latest/api/test.html#contextbeforeeachfn-options)
        * [`context.after([fn][, options])`](https://nodejs.org/docs/latest/api/test.html#contextafterfn-options)
        * [`context.afterEach([fn][, options])`](https://nodejs.org/docs/latest/api/test.html#contextaftereachfn-options)
        * [`context.assert`](https://nodejs.org/docs/latest/api/test.html#contextassert)
          * [`context.assert.fileSnapshot(value, path[, options])`](https://nodejs.org/docs/latest/api/test.html#contextassertfilesnapshotvalue-path-options)
          * [`context.assert.snapshot(value[, options])`](https://nodejs.org/docs/latest/api/test.html#contextassertsnapshotvalue-options)
        * [`context.diagnostic(message)`](https://nodejs.org/docs/latest/api/test.html#contextdiagnosticmessage)
        * [`context.filePath`](https://nodejs.org/docs/latest/api/test.html#contextfilepath)
        * [`context.fullName`](https://nodejs.org/docs/latest/api/test.html#contextfullname)
        * [`context.name`](https://nodejs.org/docs/latest/api/test.html#contextname)
        * [`context.passed`](https://nodejs.org/docs/latest/api/test.html#contextpassed)
        * [`context.error`](https://nodejs.org/docs/latest/api/test.html#contexterror)
        * [`context.attempt`](https://nodejs.org/docs/latest/api/test.html#contextattempt)
        * [`context.workerId`](https://nodejs.org/docs/latest/api/test.html#contextworkerid)
        * [`context.plan(count[,options])`](https://nodejs.org/docs/latest/api/test.html#contextplancountoptions)
        * [`context.runOnly(shouldRunOnlyTests)`](https://nodejs.org/docs/latest/api/test.html#contextrunonlyshouldrunonlytests)
        * [`context.signal`](https://nodejs.org/docs/latest/api/test.html#contextsignal)
        * [`context.skip([message])`](https://nodejs.org/docs/latest/api/test.html#contextskipmessage)
        * [`context.todo([message])`](https://nodejs.org/docs/latest/api/test.html#contexttodomessage)
        * [`context.test([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#contexttestname-options-fn)
        * [`context.waitFor(condition[, options])`](https://nodejs.org/docs/latest/api/test.html#contextwaitforcondition-options)
      * [Class: `SuiteContext`](https://nodejs.org/docs/latest/api/test.html#class-suitecontext)
        * [`context.filePath`](https://nodejs.org/docs/latest/api/test.html#contextfilepath-1)
        * [`context.fullName`](https://nodejs.org/docs/latest/api/test.html#contextfullname-1)
        * [`context.name`](https://nodejs.org/docs/latest/api/test.html#contextname-1)
        * [`context.signal`](https://nodejs.org/docs/latest/api/test.html#contextsignal-1)
  * [](https://nodejs.org/docs/latest/api/test.html#gtoc-picker)
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
  * [](https://nodejs.org/docs/latest/api/test.html#alt-docs)
    1. [25.x ](https://nodejs.org/docs/latest-v25.x/api/test.html)
    2. [24.x ](https://nodejs.org/docs/latest-v24.x/api/test.html)
    3. [23.x ](https://nodejs.org/docs/latest-v23.x/api/test.html)
    4. [22.x **LTS**](https://nodejs.org/docs/latest-v22.x/api/test.html)
    5. [21.x ](https://nodejs.org/docs/latest-v21.x/api/test.html)
    6. [20.x **LTS**](https://nodejs.org/docs/latest-v20.x/api/test.html)
    7. [19.x ](https://nodejs.org/docs/latest-v19.x/api/test.html)
    8. [18.x ](https://nodejs.org/docs/latest-v18.x/api/test.html)
  * [ ](https://nodejs.org/docs/latest/api/test.html#options-picker)
    * [View on single page](https://nodejs.org/docs/latest/api/all.html)
    * [View as JSON](https://nodejs.org/docs/latest/api/test.json)


* * *
Table of contents
  * [Test runner](https://nodejs.org/docs/latest/api/test.html#test-runner)
    * [Subtests](https://nodejs.org/docs/latest/api/test.html#subtests)
    * [Rerunning failed tests](https://nodejs.org/docs/latest/api/test.html#rerunning-failed-tests)
    * [`describe()` and `it()` aliases](https://nodejs.org/docs/latest/api/test.html#describe-and-it-aliases)
    * [Skipping tests](https://nodejs.org/docs/latest/api/test.html#skipping-tests)
    * [TODO tests](https://nodejs.org/docs/latest/api/test.html#todo-tests)
    * [Expecting tests to fail](https://nodejs.org/docs/latest/api/test.html#expecting-tests-to-fail)
    * [`only` tests](https://nodejs.org/docs/latest/api/test.html#only-tests)
    * [Filtering tests by name](https://nodejs.org/docs/latest/api/test.html#filtering-tests-by-name)
    * [Extraneous asynchronous activity](https://nodejs.org/docs/latest/api/test.html#extraneous-asynchronous-activity)
    * [Watch mode](https://nodejs.org/docs/latest/api/test.html#watch-mode)
    * [Global setup and teardown](https://nodejs.org/docs/latest/api/test.html#global-setup-and-teardown)
    * [Running tests from the command line](https://nodejs.org/docs/latest/api/test.html#running-tests-from-the-command-line)
      * [Test runner execution model](https://nodejs.org/docs/latest/api/test.html#test-runner-execution-model)
        * [Child process option inheritance](https://nodejs.org/docs/latest/api/test.html#child-process-option-inheritance)
    * [Collecting code coverage](https://nodejs.org/docs/latest/api/test.html#collecting-code-coverage)
      * [Coverage reporters](https://nodejs.org/docs/latest/api/test.html#coverage-reporters)
    * [Mocking](https://nodejs.org/docs/latest/api/test.html#mocking)
      * [Timers](https://nodejs.org/docs/latest/api/test.html#timers)
      * [Dates](https://nodejs.org/docs/latest/api/test.html#dates)
    * [Snapshot testing](https://nodejs.org/docs/latest/api/test.html#snapshot-testing)
    * [Test reporters](https://nodejs.org/docs/latest/api/test.html#test-reporters)
      * [Custom reporters](https://nodejs.org/docs/latest/api/test.html#custom-reporters)
      * [Multiple reporters](https://nodejs.org/docs/latest/api/test.html#multiple-reporters)
    * [`run([options])`](https://nodejs.org/docs/latest/api/test.html#runoptions)
    * [`suite([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#suitename-options-fn)
    * [`suite.skip([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#suiteskipname-options-fn)
    * [`suite.todo([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#suitetodoname-options-fn)
    * [`suite.only([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#suiteonlyname-options-fn)
    * [`test([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#testname-options-fn)
    * [`test.skip([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#testskipname-options-fn)
    * [`test.todo([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#testtodoname-options-fn)
    * [`test.only([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#testonlyname-options-fn)
    * [`describe([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#describename-options-fn)
    * [`describe.skip([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#describeskipname-options-fn)
    * [`describe.todo([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#describetodoname-options-fn)
    * [`describe.only([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#describeonlyname-options-fn)
    * [`it([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#itname-options-fn)
    * [`it.skip([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#itskipname-options-fn)
    * [`it.todo([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#ittodoname-options-fn)
    * [`it.only([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#itonlyname-options-fn)
    * [`before([fn][, options])`](https://nodejs.org/docs/latest/api/test.html#beforefn-options)
    * [`after([fn][, options])`](https://nodejs.org/docs/latest/api/test.html#afterfn-options)
    * [`beforeEach([fn][, options])`](https://nodejs.org/docs/latest/api/test.html#beforeeachfn-options)
    * [`afterEach([fn][, options])`](https://nodejs.org/docs/latest/api/test.html#aftereachfn-options)
    * [`assert`](https://nodejs.org/docs/latest/api/test.html#assert)
      * [`assert.register(name, fn)`](https://nodejs.org/docs/latest/api/test.html#assertregistername-fn)
    * [`snapshot`](https://nodejs.org/docs/latest/api/test.html#snapshot)
      * [`snapshot.setDefaultSnapshotSerializers(serializers)`](https://nodejs.org/docs/latest/api/test.html#snapshotsetdefaultsnapshotserializersserializers)
      * [`snapshot.setResolveSnapshotPath(fn)`](https://nodejs.org/docs/latest/api/test.html#snapshotsetresolvesnapshotpathfn)
    * [Class: `MockFunctionContext`](https://nodejs.org/docs/latest/api/test.html#class-mockfunctioncontext)
      * [`ctx.calls`](https://nodejs.org/docs/latest/api/test.html#ctxcalls)
      * [`ctx.callCount()`](https://nodejs.org/docs/latest/api/test.html#ctxcallcount)
      * [`ctx.mockImplementation(implementation)`](https://nodejs.org/docs/latest/api/test.html#ctxmockimplementationimplementation)
      * [`ctx.mockImplementationOnce(implementation[, onCall])`](https://nodejs.org/docs/latest/api/test.html#ctxmockimplementationonceimplementation-oncall)
      * [`ctx.resetCalls()`](https://nodejs.org/docs/latest/api/test.html#ctxresetcalls)
      * [`ctx.restore()`](https://nodejs.org/docs/latest/api/test.html#ctxrestore)
    * [Class: `MockModuleContext`](https://nodejs.org/docs/latest/api/test.html#class-mockmodulecontext)
      * [`ctx.restore()`](https://nodejs.org/docs/latest/api/test.html#ctxrestore-1)
    * [Class: `MockPropertyContext`](https://nodejs.org/docs/latest/api/test.html#class-mockpropertycontext)
      * [`ctx.accesses`](https://nodejs.org/docs/latest/api/test.html#ctxaccesses)
      * [`ctx.accessCount()`](https://nodejs.org/docs/latest/api/test.html#ctxaccesscount)
      * [`ctx.mockImplementation(value)`](https://nodejs.org/docs/latest/api/test.html#ctxmockimplementationvalue)
      * [`ctx.mockImplementationOnce(value[, onAccess])`](https://nodejs.org/docs/latest/api/test.html#ctxmockimplementationoncevalue-onaccess)
        * [Caveat](https://nodejs.org/docs/latest/api/test.html#caveat)
      * [`ctx.resetAccesses()`](https://nodejs.org/docs/latest/api/test.html#ctxresetaccesses)
      * [`ctx.restore()`](https://nodejs.org/docs/latest/api/test.html#ctxrestore-2)
    * [Class: `MockTracker`](https://nodejs.org/docs/latest/api/test.html#class-mocktracker)
      * [`mock.fn([original[, implementation]][, options])`](https://nodejs.org/docs/latest/api/test.html#mockfnoriginal-implementation-options)
      * [`mock.getter(object, methodName[, implementation][, options])`](https://nodejs.org/docs/latest/api/test.html#mockgetterobject-methodname-implementation-options)
      * [`mock.method(object, methodName[, implementation][, options])`](https://nodejs.org/docs/latest/api/test.html#mockmethodobject-methodname-implementation-options)
      * [`mock.module(specifier[, options])`](https://nodejs.org/docs/latest/api/test.html#mockmodulespecifier-options)
      * [`mock.property(object, propertyName[, value])`](https://nodejs.org/docs/latest/api/test.html#mockpropertyobject-propertyname-value)
      * [`mock.reset()`](https://nodejs.org/docs/latest/api/test.html#mockreset)
      * [`mock.restoreAll()`](https://nodejs.org/docs/latest/api/test.html#mockrestoreall)
      * [`mock.setter(object, methodName[, implementation][, options])`](https://nodejs.org/docs/latest/api/test.html#mocksetterobject-methodname-implementation-options)
    * [Class: `MockTimers`](https://nodejs.org/docs/latest/api/test.html#class-mocktimers)
      * [`timers.enable([enableOptions])`](https://nodejs.org/docs/latest/api/test.html#timersenableenableoptions)
      * [`timers.reset()`](https://nodejs.org/docs/latest/api/test.html#timersreset)
      * [`timers[Symbol.dispose]()`](https://nodejs.org/docs/latest/api/test.html#timerssymboldispose)
      * [`timers.tick([milliseconds])`](https://nodejs.org/docs/latest/api/test.html#timerstickmilliseconds)
        * [Using clear functions](https://nodejs.org/docs/latest/api/test.html#using-clear-functions)
        * [Working with Node.js timers modules](https://nodejs.org/docs/latest/api/test.html#working-with-nodejs-timers-modules)
      * [`timers.runAll()`](https://nodejs.org/docs/latest/api/test.html#timersrunall)
      * [`timers.setTime(milliseconds)`](https://nodejs.org/docs/latest/api/test.html#timerssettimemilliseconds)
        * [Dates and Timers working together](https://nodejs.org/docs/latest/api/test.html#dates-and-timers-working-together)
    * [Class: `TestsStream`](https://nodejs.org/docs/latest/api/test.html#class-testsstream)
      * [Event: `'test:coverage'`](https://nodejs.org/docs/latest/api/test.html#event-testcoverage)
      * [Event: `'test:complete'`](https://nodejs.org/docs/latest/api/test.html#event-testcomplete)
      * [Event: `'test:dequeue'`](https://nodejs.org/docs/latest/api/test.html#event-testdequeue)
      * [Event: `'test:diagnostic'`](https://nodejs.org/docs/latest/api/test.html#event-testdiagnostic)
      * [Event: `'test:enqueue'`](https://nodejs.org/docs/latest/api/test.html#event-testenqueue)
      * [Event: `'test:fail'`](https://nodejs.org/docs/latest/api/test.html#event-testfail)
      * [Event: `'test:interrupted'`](https://nodejs.org/docs/latest/api/test.html#event-testinterrupted)
      * [Event: `'test:pass'`](https://nodejs.org/docs/latest/api/test.html#event-testpass)
      * [Event: `'test:plan'`](https://nodejs.org/docs/latest/api/test.html#event-testplan)
      * [Event: `'test:start'`](https://nodejs.org/docs/latest/api/test.html#event-teststart)
      * [Event: `'test:stderr'`](https://nodejs.org/docs/latest/api/test.html#event-teststderr)
      * [Event: `'test:stdout'`](https://nodejs.org/docs/latest/api/test.html#event-teststdout)
      * [Event: `'test:summary'`](https://nodejs.org/docs/latest/api/test.html#event-testsummary)
      * [Event: `'test:watch:drained'`](https://nodejs.org/docs/latest/api/test.html#event-testwatchdrained)
      * [Event: `'test:watch:restarted'`](https://nodejs.org/docs/latest/api/test.html#event-testwatchrestarted)
    * [Class: `TestContext`](https://nodejs.org/docs/latest/api/test.html#class-testcontext)
      * [`context.before([fn][, options])`](https://nodejs.org/docs/latest/api/test.html#contextbeforefn-options)
      * [`context.beforeEach([fn][, options])`](https://nodejs.org/docs/latest/api/test.html#contextbeforeeachfn-options)
      * [`context.after([fn][, options])`](https://nodejs.org/docs/latest/api/test.html#contextafterfn-options)
      * [`context.afterEach([fn][, options])`](https://nodejs.org/docs/latest/api/test.html#contextaftereachfn-options)
      * [`context.assert`](https://nodejs.org/docs/latest/api/test.html#contextassert)
        * [`context.assert.fileSnapshot(value, path[, options])`](https://nodejs.org/docs/latest/api/test.html#contextassertfilesnapshotvalue-path-options)
        * [`context.assert.snapshot(value[, options])`](https://nodejs.org/docs/latest/api/test.html#contextassertsnapshotvalue-options)
      * [`context.diagnostic(message)`](https://nodejs.org/docs/latest/api/test.html#contextdiagnosticmessage)
      * [`context.filePath`](https://nodejs.org/docs/latest/api/test.html#contextfilepath)
      * [`context.fullName`](https://nodejs.org/docs/latest/api/test.html#contextfullname)
      * [`context.name`](https://nodejs.org/docs/latest/api/test.html#contextname)
      * [`context.passed`](https://nodejs.org/docs/latest/api/test.html#contextpassed)
      * [`context.error`](https://nodejs.org/docs/latest/api/test.html#contexterror)
      * [`context.attempt`](https://nodejs.org/docs/latest/api/test.html#contextattempt)
      * [`context.workerId`](https://nodejs.org/docs/latest/api/test.html#contextworkerid)
      * [`context.plan(count[,options])`](https://nodejs.org/docs/latest/api/test.html#contextplancountoptions)
      * [`context.runOnly(shouldRunOnlyTests)`](https://nodejs.org/docs/latest/api/test.html#contextrunonlyshouldrunonlytests)
      * [`context.signal`](https://nodejs.org/docs/latest/api/test.html#contextsignal)
      * [`context.skip([message])`](https://nodejs.org/docs/latest/api/test.html#contextskipmessage)
      * [`context.todo([message])`](https://nodejs.org/docs/latest/api/test.html#contexttodomessage)
      * [`context.test([name][, options][, fn])`](https://nodejs.org/docs/latest/api/test.html#contexttestname-options-fn)
      * [`context.waitFor(condition[, options])`](https://nodejs.org/docs/latest/api/test.html#contextwaitforcondition-options)
    * [Class: `SuiteContext`](https://nodejs.org/docs/latest/api/test.html#class-suitecontext)
      * [`context.filePath`](https://nodejs.org/docs/latest/api/test.html#contextfilepath-1)
      * [`context.fullName`](https://nodejs.org/docs/latest/api/test.html#contextfullname-1)
      * [`context.name`](https://nodejs.org/docs/latest/api/test.html#contextname-1)
      * [`context.signal`](https://nodejs.org/docs/latest/api/test.html#contextsignal-1)


## Test runner[#](https://nodejs.org/docs/latest/api/test.html#test-runner)
**Source Code:** Added in: v18.0.0, v16.17.0History Version | Changes
---|---
v20.0.0 | The test runner is now stable.
[Stability: 2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Stable
The `node:test` module facilitates the creation of JavaScript tests. To access it:
```
import test from 'node:test';
const test = require('node:test');
copy
```

This module is only available under the `node:` scheme.
Tests created via the `test` module consist of a single function that is processed in one of three ways:
  1. A synchronous function that is considered failing if it throws an exception, and is considered passing otherwise.
  2. A function that returns a `Promise` that is considered failing if the `Promise` rejects, and is considered passing if the `Promise` fulfills.
  3. A function that receives a callback function. If the callback receives any truthy value as its first argument, the test is considered failing. If a falsy value is passed as the first argument to the callback, the test is considered passing. If the test function receives a callback function and also returns a `Promise`, the test will fail.


The following example illustrates how tests are written using the `test` module.
```
test('synchronous passing test', (t) => {
  // This test passes because it does not throw an exception.
  assert.strictEqual(1, 1);
});

test('synchronous failing test', (t) => {
  // This test fails because it throws an exception.
  assert.strictEqual(1, 2);
});

test('asynchronous passing test', async (t) => {
  // This test passes because the Promise returned by the async
  // function is settled and not rejected.
  assert.strictEqual(1, 1);
});

test('asynchronous failing test', async (t) => {
  // This test fails because the Promise returned by the async
  // function is rejected.
  assert.strictEqual(1, 2);
});

test('failing test using Promises', (t) => {
  // Promises can be used directly as well.
  return new Promise((resolve, reject) => {
    setImmediate(() => {
      reject(new Error('this will cause the test to fail'));
    });
  });
});

test('callback passing test', (t, done) => {
  // done() is the callback function. When the setImmediate() runs, it invokes
  // done() with no arguments.
  setImmediate(done);
});

test('callback failing test', (t, done) => {
  // When the setImmediate() runs, done() is invoked with an Error object and
  // the test fails.
  setImmediate(() => {
    done(new Error('callback failure'));
  });
});
copy
```

If any tests fail, the process exit code is set to `1`.
### Subtests[#](https://nodejs.org/docs/latest/api/test.html#subtests)
The test context's `test()` method allows subtests to be created. It allows you to structure your tests in a hierarchical manner, where you can create nested tests within a larger test. This method behaves identically to the top level `test()` function. The following example demonstrates the creation of a top level test with two subtests.
```
test('top level test', async (t) => {
  await t.test('subtest 1', (t) => {
    assert.strictEqual(1, 1);
  });

  await t.test('subtest 2', (t) => {
    assert.strictEqual(2, 2);
  });
});
copy
```

> **Note:** `beforeEach` and `afterEach` hooks are triggered between each subtest execution.
In this example, `await` is used to ensure that both subtests have completed. This is necessary because tests do not wait for their subtests to complete, unlike tests created within suites. Any subtests that are still outstanding when their parent finishes are cancelled and treated as failures. Any subtest failures cause the parent test to fail.
### Rerunning failed tests[#](https://nodejs.org/docs/latest/api/test.html#rerunning-failed-tests)
The test runner supports persisting the state of the run to a file, allowing the test runner to rerun failed tests without having to re-run the entire test suite. Use the [`--test-rerun-failures`](https://nodejs.org/docs/latest/api/cli.html#--test-rerun-failures) command-line option to specify a file path where the state of the run is stored. if the state file does not exist, the test runner will create it. the state file is a JSON file that contains an array of run attempts. Each run attempt is an object mapping successful tests to the attempt they have passed in. The key identifying a test in this map is the test file path, with the line and column where the test is defined. in a case where a test defined in a specific location is run multiple times, for example within a function or a loop, a counter will be appended to the key, to disambiguate the test runs. note changing the order of test execution or the location of a test can lead the test runner to consider tests as passed on a previous attempt, meaning `--test-rerun-failures` should be used when tests run in a deterministic order.
example of a state file:
```
[
  {
    "test.js:10:5": { "passed_on_attempt": 0, "name": "test 1" }
  },
  {
    "test.js:10:5": { "passed_on_attempt": 0, "name": "test 1" },
    "test.js:20:5": { "passed_on_attempt": 1, "name": "test 2" }
  }
]
copy
```

in this example, there are two run attempts, with two tests defined in `test.js`, the first test succeeded on the first attempt, and the second test succeeded on the second attempt.
When the `--test-rerun-failures` option is used, the test runner will only run tests that have not yet passed.
```
node --test-rerun-failures /path/to/state/file
copy
```

###  `describe()` and `it()` aliases[#](https://nodejs.org/docs/latest/api/test.html#describe-and-it-aliases)
Suites and tests can also be written using the `describe()` and `it()` functions. [`describe()`](https://nodejs.org/docs/latest/api/test.html#describename-options-fn) is an alias for [`suite()`](https://nodejs.org/docs/latest/api/test.html#suitename-options-fn), and [`it()`](https://nodejs.org/docs/latest/api/test.html#itname-options-fn) is an alias for [`test()`](https://nodejs.org/docs/latest/api/test.html#testname-options-fn).
```
describe('A thing', () => {
  it('should work', () => {
    assert.strictEqual(1, 1);
  });

  it('should be ok', () => {
    assert.strictEqual(2, 2);
  });

  describe('a nested thing', () => {
    it('should work', () => {
      assert.strictEqual(3, 3);
    });
  });
});
copy
```

`describe()` and `it()` are imported from the `node:test` module.
```
import { describe, it } from 'node:test';
const { describe, it } = require('node:test');
copy
```

### Skipping tests[#](https://nodejs.org/docs/latest/api/test.html#skipping-tests)
Individual tests can be skipped by passing the `skip` option to the test, or by calling the test context's `skip()` method as shown in the following example.
```
// The skip option is used, but no message is provided.
test('skip option', { skip: true }, (t) => {
  // This code is never executed.
});

// The skip option is used, and a message is provided.
test('skip option with message', { skip: 'this is skipped' }, (t) => {
  // This code is never executed.
});

test('skip() method', (t) => {
  // Make sure to return here as well if the test contains additional logic.
  t.skip();
});

test('skip() method with message', (t) => {
  // Make sure to return here as well if the test contains additional logic.
  t.skip('this is skipped');
});
copy
```

### TODO tests[#](https://nodejs.org/docs/latest/api/test.html#todo-tests)
Individual tests can be marked as flaky or incomplete by passing the `todo` option to the test, or by calling the test context's `todo()` method, as shown in the following example. These tests represent a pending implementation or bug that needs to be fixed. TODO tests are executed, but are not treated as test failures, and therefore do not affect the process exit code. If a test is marked as both TODO and skipped, the TODO option is ignored.
```
// The todo option is used, but no message is provided.
test('todo option', { todo: true }, (t) => {
  // This code is executed, but not treated as a failure.
  throw new Error('this does not fail the test');
});

// The todo option is used, and a message is provided.
test('todo option with message', { todo: 'this is a todo test' }, (t) => {
  // This code is executed.
});

test('todo() method', (t) => {
  t.todo();
});

test('todo() method with message', (t) => {
  t.todo('this is a todo test and is not treated as a failure');
  throw new Error('this does not fail the test');
});
copy
```

### Expecting tests to fail[#](https://nodejs.org/docs/latest/api/test.html#expecting-tests-to-fail)
Added in: v25.5.0
This flips the pass/fail reporting for a specific test or suite: a flagged test case must throw in order to pass, and a flagged test case that does not throw fails.
In each of the following, `doTheThing()` fails to return `true`, but since the tests are flagged `expectFailure`, they pass.
```
it.expectFailure('should do the thing', () => {
  assert.strictEqual(doTheThing(), true);
});

it('should do the thing', { expectFailure: true }, () => {
  assert.strictEqual(doTheThing(), true);
});

it('should do the thing', { expectFailure: 'feature not implemented' }, () => {
  assert.strictEqual(doTheThing(), true);
});
copy
```

If the value of `expectFailure` is a
