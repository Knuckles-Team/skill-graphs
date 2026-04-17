##  [Core classes](https://vercel.com/docs/vercel-sandbox/sdk-reference#core-classes)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#core-classes)
Class | What it does | Example
---|---|---
[`Sandbox`](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox-class) | Creates and manages isolated microVM environments | `const sandbox = await Sandbox.create()`
[`Command`](https://vercel.com/docs/vercel-sandbox/sdk-reference#command-class) | Handles running commands inside the sandbox | `const cmd = await sandbox.runCommand()`
[`CommandFinished`](https://vercel.com/docs/vercel-sandbox/sdk-reference#commandfinished-class) | Contains the result after a command completes | Access `cmd.exitCode` and `cmd.stdout()`
[`NetworkPolicy`](https://vercel.com/docs/vercel-sandbox/sdk-reference#networkpolicy-class) | Defines firewall rules for sandbox traffic | `Sandbox.create({networkPolicy: 'deny-all'})`
[`Snapshot`](https://vercel.com/docs/vercel-sandbox/sdk-reference#snapshot-class) | Represents a saved sandbox state for fast restarts | `const snapshot = await sandbox.snapshot()`
###  [Basic workflow](https://vercel.com/docs/vercel-sandbox/sdk-reference#basic-workflow)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#basic-workflow)
```
// 1. Create a sandbox
const sandbox = await Sandbox.create({ runtime: 'node24' });

// 2. Run a command - it waits for completion and returns the result
const result = await sandbox.runCommand('node', ['--version']);

// 3. Check the result
console.log(result.exitCode); // 0
console.log(await result.stdout()); // v22.x.x
```
