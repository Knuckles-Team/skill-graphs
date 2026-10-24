##  [Command class](https://vercel.com/docs/vercel-sandbox/sdk-reference#command-class)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#command-class)
`Command` instances represent processes that run inside a sandbox. Detached executions created through `sandbox.runCommand({ detached: true, ... })` return a `Command` immediately so that you can stream logs or stop the process later. Blocking executions that do not set `detached` still expose these methods through the `CommandFinished` object they resolve to.
###  [Command class properties](https://vercel.com/docs/vercel-sandbox/sdk-reference#command-class-properties)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#command-class-properties)
####  [`exitCode`](https://vercel.com/docs/vercel-sandbox/sdk-reference#exitcode)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#exitcode)
The `exitCode` property holds the process exit status once the command finishes. For detached commands, this value starts as `null` and gets populated after you await `command.wait()`, so check for `null` to determine if the command is still running.
```
if (command.exitCode !== null) {
  console.log(`Command exited with code: ${command.exitCode}`);
}
```

Returns: `number | null`.
###  [Command class accessors](https://vercel.com/docs/vercel-sandbox/sdk-reference#command-class-accessors)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#command-class-accessors)
####  [`cmdId`](https://vercel.com/docs/vercel-sandbox/sdk-reference#cmdid)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#cmdid)
Use `cmdId` to identify the specific command execution so you can look it up later with `sandbox.getCommand()`. Store this value whenever you launch detached commands so you can replay output in dashboards or correlate logs across systems.
```
console.log(command.cmdId);
```

Returns: `string`.
####  [`cwd`](https://vercel.com/docs/vercel-sandbox/sdk-reference#cwd)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#cwd)
The `cwd` accessor shows the working directory where the command is executing. Compare this value against expected paths when debugging file-related issues or verifying that relative paths resolve correctly.
```
console.log(command.cwd);
```

Returns: `string`.
####  [`startedAt`](https://vercel.com/docs/vercel-sandbox/sdk-reference#startedat)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#startedat)
`startedAt` returns the Unix timestamp (in milliseconds) when the command started executing. Subtract this from the current time to monitor execution duration or set timeout thresholds for long-running processes.
```
const duration = Date.now() - command.startedAt;
console.log(`Command has been running for ${duration}ms`);
```

Returns: `number`.
###  [Command class methods](https://vercel.com/docs/vercel-sandbox/sdk-reference#command-class-methods)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#command-class-methods)
####  [`logs()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#logs)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#logs)
Call `logs()` to stream structured log entries in real time so you can watch command output as it happens. Each entry includes the stream type (`stdout` or `stderr`) and the data chunk, so you can route logs to different destinations or stop iteration when you detect a readiness signal.
```
for await (const log of command.logs()) {
  if (log.stream === 'stdout') {
    process.stdout.write(log.data);
  } else {
    process.stderr.write(log.data);
  }
}
```

Parameter | Type | Required | Details
---|---|---|---
`opts.signal` | `AbortSignal` | No | Cancel log streaming if needed.
Returns: `AsyncGenerator<{ stream: "stdout" | "stderr"; data: string; }, void, void>`.
Note: May throw `StreamError` if the sandbox stops while streaming logs.
####  [`wait()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#wait)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#wait)
Use `wait()` to block until a detached command finishes and get the resulting `CommandFinished` object with the populated exit code. This method is essential for detached commands where you need to know when execution completes. For non-detached commands, `sandbox.runCommand()` already waits automatically.
```
const detachedCmd = await sandbox.runCommand({
  cmd: 'sleep',
  args: ['5'],
  detached: true,
});
const result = await detachedCmd.wait();
if (result.exitCode !== 0) {
  console.error('Something went wrong...');
}
```

Parameter | Type | Required | Details
---|---|---|---
`params.signal` | `AbortSignal` | No | Cancel waiting if you need to abort early.
Returns: `Promise<CommandFinished>`.
####  [`output()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#output)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#output)
Use `output()` to retrieve stdout, stderr, or both as a single string. Choose `"both"` when you want combined output for logging, or specify `"stdout"` or `"stderr"` when you need to process them separately after the command finishes.
```
const combined = await command.output('both');
const stdoutOnly = await command.output('stdout');
```

Parameter | Type | Required | Details
---|---|---|---
`stream` | `"stdout" | "stderr" | "both"` | Yes | The output stream to read.
`opts.signal` | `AbortSignal` | No | Cancel output streaming.
Returns: `Promise<string>`.
Note: This may throw string conversion errors if the command output contains invalid Unicode.
####  [`stdout()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#stdout)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#stdout)
`stdout()` collects the entire standard output stream as a string, which is handy when commands print JSON or other structured data that you need to parse after completion.
```
const output = await command.stdout();
const data = JSON.parse(output);
```

Parameter | Type | Required | Details
---|---|---|---
`opts.signal` | `AbortSignal` | No | Cancel the read while the command runs.
Returns: `Promise<string>`.
Note: This may throw string conversion errors if the command output contains invalid Unicode.
####  [`stderr()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#stderr)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#stderr)
`stderr()` gathers all error output produced by the command. Combine this with `exitCode` to build user-friendly error messages or forward failure logs to your monitoring system.
```
const errors = await command.stderr();
if (errors) {
  console.error('Command errors:', errors);
}
```

Parameter | Type | Required | Details
---|---|---|---
`opts.signal` | `AbortSignal` | No | Cancel the read while collecting error output.
Returns: `Promise<string>`.
Note: This may throw string conversion errors if the command output contains invalid Unicode.
####  [`kill()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#kill)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#kill)
Call `kill()` to terminate a running command using the specified signal. This lets you stop long-running processes without destroying the entire sandbox. Send `SIGTERM` by default for graceful shutdown, or use `SIGKILL` for immediate termination.
```
await command.kill('SIGKILL');
```

Parameter | Type | Required | Details
---|---|---|---
`signal` | `Signal` | No | The signal to send to the process. Defaults to `SIGTERM`.
`opts.abortSignal` | `AbortSignal` | No | Cancel the kill operation.
Returns: `Promise<void>`.
