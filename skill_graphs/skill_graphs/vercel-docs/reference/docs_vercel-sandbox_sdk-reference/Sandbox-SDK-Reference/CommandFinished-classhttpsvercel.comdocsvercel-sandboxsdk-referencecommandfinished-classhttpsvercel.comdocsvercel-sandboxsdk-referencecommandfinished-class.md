##  [CommandFinished class](https://vercel.com/docs/vercel-sandbox/sdk-reference#commandfinished-class)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#commandfinished-class)
`CommandFinished` is the result you receive after a sandbox command exits. It extends the `Command` class, so you keep access to streaming helpers such as `logs()` or `stdout()`, but you also get the final exit metadata immediately. You usually receive this object from `sandbox.runCommand()` or by awaiting `command.wait()` on a detached process.
###  [CommandFinished class properties](https://vercel.com/docs/vercel-sandbox/sdk-reference#commandfinished-class-properties)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#commandfinished-class-properties)
####  [`exitCode`](https://vercel.com/docs/vercel-sandbox/sdk-reference#exitcode)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#exitcode)
The `exitCode` property reports the numeric status returned by the command. A value of `0` indicates success; any other value means the process exited with an error, so branch on it before you parse output.
```
if (result.exitCode === 0) {
  console.log('Command succeeded');
}
```

Returns: `number`.
###  [CommandFinished class accessors](https://vercel.com/docs/vercel-sandbox/sdk-reference#commandfinished-class-accessors)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#commandfinished-class-accessors)
####  [`cmdId`](https://vercel.com/docs/vercel-sandbox/sdk-reference#cmdid)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#cmdid)
Use `cmdId` to identify the specific command execution so you can reference it in logs or retrieve it later with `sandbox.getCommand()`. Store this ID whenever you need to trace command history or correlate output across retries.
```
console.log(result.cmdId);
```

Returns: `string`.
####  [`cwd`](https://vercel.com/docs/vercel-sandbox/sdk-reference#cwd)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#cwd)
The `cwd` accessor shows the working directory where the command executed. Compare this value against expected paths when debugging file-related failures or relative path issues.
```
console.log(result.cwd);
```

Returns: `string`.
####  [`startedAt`](https://vercel.com/docs/vercel-sandbox/sdk-reference#startedat)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#startedat)
`startedAt` returns the Unix timestamp (in milliseconds) when the command started executing. Subtract this from the current time or from another timestamp to measure execution duration or schedule follow-up tasks.
```
const duration = Date.now() - result.startedAt;
console.log(`Command took ${duration}ms`);
```

Returns: `number`.
###  [CommandFinished class methods](https://vercel.com/docs/vercel-sandbox/sdk-reference#commandfinished-class-methods)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#commandfinished-class-methods)
`CommandFinished` inherits all methods from `Command` including `logs()`, `output()`, `stdout()`, `stderr()`, and `kill()`. See the [Command class](https://vercel.com/docs/vercel-sandbox/sdk-reference#command-class) section for details on these methods.
