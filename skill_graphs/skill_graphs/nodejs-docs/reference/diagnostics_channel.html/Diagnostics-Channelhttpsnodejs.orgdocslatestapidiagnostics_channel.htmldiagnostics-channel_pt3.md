`tracing:child_process.spawn:error`
  * `process` [`<ChildProcess>`](https://nodejs.org/docs/latest/api/child_process.html#class-childprocess)
  * `error`


Emitted when [`child_process.spawn()`](https://nodejs.org/docs/latest/api/child_process.html#child_processspawncommand-args-options) encounters an error.
###### Event: `'execve'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-execve)
  * `execPath`
  * `args`
  * `env`


Emitted when [`process.execve()`](https://nodejs.org/docs/latest/api/process.html#processexecvefile-args-env) is invoked.
##### Worker Thread[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#worker-thread)
Added in: v16.18.0
Stability: 1 - Experimental
###### Event: `'worker_threads'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-worker-threads)
  * `worker` [`<Worker>`](https://nodejs.org/docs/latest/api/worker_threads.html#class-worker)


Emitted when a new thread is created.
