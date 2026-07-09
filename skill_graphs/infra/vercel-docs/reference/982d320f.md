##  [Sandbox class](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox-class)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox-class)
The `Sandbox` class gives you full control over isolated Linux microVMs. Use it to create new sandboxes, inspect active ones, stream command output, and shut everything down once your workflow is complete.
###  [Sandbox class accessors](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox-class-accessors)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox-class-accessors)
####  [`sandboxId`](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandboxid)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandboxid)
Use `sandboxId` to identify the current microVM so you can reconnect to it later with `Sandbox.get()` or trace command history. Store this ID whenever your workflow spans multiple processes or retries so you can resume log streaming after a restart.
Returns: `string`.
```
console.log(sandbox.sandboxId);
```

####  [`status`](https://vercel.com/docs/vercel-sandbox/sdk-reference#status)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#status)
The `status` accessor reports the lifecycle state of the sandbox so you can decide when to queue new work or perform cleanup. Poll this value when you need to wait for startup or confirm shutdown, and treat `failed` as a signal to create a new sandbox.
Returns: `"pending" | "running" | "stopping" | "stopped" | "failed"`.
```
console.log(sandbox.status);
```

####  [`timeout`](https://vercel.com/docs/vercel-sandbox/sdk-reference#timeout)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#timeout)
`timeout` shows how many milliseconds remain before the sandbox stops automatically. Compare the remaining time against upcoming commands and call `sandbox.extendTimeout()` if the window is too short.
Returns: `number`.
```
console.log(sandbox.timeout);
```

####  [`createdAt`](https://vercel.com/docs/vercel-sandbox/sdk-reference#createdat)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#createdat)
The `createdAt` accessor returns the date and time when the sandbox was created. Use this to track the sandbox age or calculate how long a sandbox has been running.
Returns: `Date`.
```
console.log(sandbox.createdAt);
```

####  [`activeCpuUsageMs`](https://vercel.com/docs/vercel-sandbox/sdk-reference#activecpuusagems)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#activecpuusagems)
The `activeCpuUsageMs` accessor returns the amount of CPU used for this sandbox (in milliseconds). It is only available once the sandbox VM has stopped. Use this to track the billable CPU.
Returns: `number`.
```
console.log(sandbox.activeCpuUsageMs);
```

####  [`networkUsage`](https://vercel.com/docs/vercel-sandbox/sdk-reference#networkusage)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#networkusage)
The `networkUsage` accessor returns the amount of network data used by this sandbox (in bytes). It is only available once the sandbox VM has stopped. Use this to track the billable data usage.
Returns: `{ingress: number, egress: number}`.
```
console.log(sandbox.networkUsage);
```

###  [Sandbox class static methods](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox-class-static-methods)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox-class-static-methods)
####  [`Sandbox.list()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.list)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.list)
Use `Sandbox.list()` to enumerate sandboxes for a project, optionally filtering by time range or page size. Combine `since` and `until` with the pagination cursor and cache the last `pagination.next` value so you can resume after restarts without missing entries.
Returns: `Promise<Parsed<{ sandboxes: SandboxSummary[]; pagination: Pagination; }>>`.
Parameter | Type | Required | Details
---|---|---|---
`projectId` | `string` | No | Project whose sandboxes you want to list.
`limit` | `number` | No | Maximum number of sandboxes to return.
`since` | `number | Date` | No | List sandboxes created after this time.
`until` | `number | Date` | No | List sandboxes created before this time.
`signal` | `AbortSignal` | No | Cancel the request if necessary.
```
const { json: { sandboxes, pagination } } = await Sandbox.list();
```

####  [`Sandbox.create()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.create)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.create)
`Sandbox.create()` launches a new microVM with your chosen runtime, source, and resource settings. Defaults to an empty workspace when no source is provided. Pass `source.depth` when cloning large repositories to shorten setup time.
Returns: `Promise<Sandbox>`.
Parameter | Type | Required | Details / Values
---|---|---|---
`source` | `git` | No | Clone a Git repository.
`url`: string
`username`: string
`password`: string
`depth`?: number
`revision`?: string

`source` | `tarball` | No | Mount a tarball.
`url`: string

`source` | `snapshot` | No | Create from a snapshot.
`snapshotId`: string

`resources.vcpus` | `number` | No | Override CPU count (defaults to plan baseline).
`runtime` | `string` | No | Runtime image such as `"node24"`, `"node22"`, or `"python3.13"`.
`ports` | `number[]` | No | Ports to expose for `sandbox.domain()`.
`timeout` | `number` | No | Initial timeout in milliseconds.
`networkPolicy` | `NetworkPolicy` | No | Firewall rules applied to sandbox egress traffic (defaults to global Internet access).
`env` | `Record<string, string>` | No | Default environment variables for commands run in this sandbox. Per-command `runCommand({ env })` values override these defaults.
`signal` | `AbortSignal` | No | Cancel sandbox creation if needed.
```
const sandbox = await Sandbox.create({
  runtime: 'node24',
  networkPolicy: 'deny-all',
  env: { NODE_ENV: 'production' },
});
```

####  [`Sandbox.get()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.get)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.get)
`Sandbox.get()` rehydrates an active sandbox by ID so you can resume work or inspect logs. It throws if the sandbox no longer exists, so cache `sandboxId` only while the job is active and clear it once the sandbox stops.
Returns: `Promise<Sandbox>`.
Parameter | Type | Required | Details
---|---|---|---
`sandboxId` | `string` | Yes | Identifier of the sandbox to retrieve.
`signal` | `AbortSignal` | No | Cancel the request if necessary.
```
const sandbox = await Sandbox.get({ sandboxId });
```

###  [Sandbox class instance methods](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox-class-instance-methods)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox-class-instance-methods)
####  [`sandbox.getCommand()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.getcommand)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.getcommand)
Call `sandbox.getCommand()` to retrieve a previously executed command by its ID, which is especially helpful after detached executions when you want to inspect logs later.
Returns: `Promise<Command>`.
Parameter | Type | Required | Details
---|---|---|---
`cmdId` | `string` | Yes | Identifier of the command to fetch.
`opts.signal` | `AbortSignal` | No | Cancel the lookup if it takes too long.
```
const command = await sandbox.getCommand(cmdId);
```

####  [`sandbox.runCommand()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.runcommand)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.runcommand)
`sandbox.runCommand()` executes commands inside the microVM, either blocking until completion or returning immediately in detached mode. Use `detached: true` for long-running servers, stream output to local log handlers, and call `command.wait()` later for results.
Returns: `Promise<CommandFinished>` when `detached` is `false`; `Promise<Command>` when `detached` is `true`.
Parameter | Type | Required | Details
---|---|---|---
`command` | `string` | Yes | Command to execute (string overload).
`args` | `string[]` | No | Arguments for the string overload.
`opts.signal` | `AbortSignal` | No | Cancel the command (string overload).
`params.cmd` | `string` | Yes | Command to execute when using the object overload.
`params.args` | `string[]` | No | Arguments for the object overload.
`params.cwd` | `string` | No | Working directory for execution.
`params.env` | `Record<string, string>` | No | Additional environment variables.
`params.sudo` | `boolean` | No | Run the command with sudo.
`params.detached` | `boolean` | No | Return immediately with a live `Command` object.
`params.stdout` | `Writable` | No | Stream standard output to a writable.
`params.stderr` | `Writable` | No | Stream standard error to a writable.
`params.signal` | `AbortSignal` | No | Cancel the command when using the object overload.
```
const result = await sandbox.runCommand('node', ['--version']);
```

####  [`sandbox.mkDir()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.mkdir)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.mkdir)
`sandbox.mkDir()` creates a directory in the sandbox filesystem before you write files or clone repositories. Paths are relative to `/vercel/sandbox` unless you provide an absolute path. Call this before `writeFiles()` when your target directory does not exist yet.
```
await sandbox.mkDir('assets');
```

Parameter | Type | Required | Details
---|---|---|---
`path` | `string` | Yes | Directory to create.
`opts.signal` | `AbortSignal` | No | Cancel the operation.
Returns: `Promise<void>`.
####  [`sandbox.readFile()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.readfile)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.readfile)
Use `sandbox.readFile()` to pull file contents from the sandbox to a `ReadableStream`. The promise resolves to `null` when the file does not exist. You can use [`sandbox.readFileToBuffer()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.readfiletobuffer) directly if you prefer receiving a `Buffer`.
```
const stream = await sandbox.readFile({ path: 'package.json' });
```

Parameter | Type | Required | Details
---|---|---|---
`file.path` | `string` | Yes | Path to the file inside the sandbox.
`file.cwd` | `string` | No | Base directory for resolving `file.path`.
`opts.signal` | `AbortSignal` | No | Cancel the read operation.
Returns: `Promise<null | ReadableStream>`.
####  [`sandbox.readFileToBuffer()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.readfiletobuffer)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.readfiletobuffer)
Use `sandbox.readFileToBuffer()` to pull entire file contents from the sandbox to an in-memory buffer. The promise resolves to `null` when the file does not exist.
```
const buffer = await sandbox.readFileToBuffer({ path: 'package.json' });
```

Parameter | Type | Required | Details
---|---|---|---
`file.path` | `string` | Yes | Path to the file inside the sandbox.
`file.cwd` | `string` | No | Base directory for resolving `file.path`.
`opts.signal` | `AbortSignal` | No | Cancel the read operation.
Returns: `Promise<null | Buffer>`.
####  [`sandbox.downloadFile()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.downloadfile)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.downloadfile)
Use `sandbox.downloadFile()` to pull file contents from the sandbox to a local destination. The promise resolves to the absolute destination path or `null` when the source file does not exist.
```
const dstPath = await sandbox.downloadFile(
  { path: 'package.json', cwd: '/vercel/sandbox' },
  { path: 'local-package.json', cwd: '/tmp' }
);
```

Parameter | Type | Required | Details
---|---|---|---
`src.path` | `string` | Yes | Path to the file inside the sandbox.
`src.cwd` | `string` | No | Base directory for resolving `src.path`.
`dst.path` | `string` | Yes | Path to local destination.
`dst.cwd` | `string` | No | Base directory for resolving `dst.path`.
`opts.signal` | `AbortSignal` | No | Cancel the download operation.
`opts.mkdirRecursive` | `boolean` | No | Create destination directories recursively if they do not exist.
Returns: `Promise<null | string>`.
####  [`sandbox.writeFiles()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.writefiles)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.writefiles)
`sandbox.writeFiles()` uploads one or more files into the sandbox filesystem. Paths default to `/vercel/sandbox`; use absolute paths for custom locations and bundle related files into a single call to reduce round trips.
```
await sandbox.writeFiles([{ path: 'hello.txt', content: Buffer.from('hi') }]);
```

Parameter | Type | Required | Details
---|---|---|---
`files` | `{ path: string; content: Buffer; }[]` | Yes | File descriptors to write.
`opts.signal` | `AbortSignal` | No | Cancel the write operation.
Returns: `Promise<void>`.
####  [`sandbox.domain()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.domain)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.domain)
`sandbox.domain()` resolves a publicly accessible URL for a port you exposed during creation. It throws if the port is not registered to a route, so include the port in the `ports` array when creating the sandbox and cache the returned URL so you can share it quickly with collaborators.
```
const previewUrl = sandbox.domain(3000);
```

Parameter | Type | Required | Details
---|---|---|---
`p` | `number` | Yes | Port number declared in `ports`.
Returns: `string`.
####  [`sandbox.stop()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.stop)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.stop)
Call `sandbox.stop()` to terminate the microVM and free resources immediately. It's safe to call multiple times; subsequent calls resolve once the sandbox is already stopped, so invoke it as soon as you collect artifacts to control costs.
```
// Trigger sandbox shutdown asynchronously
await sandbox.stop();

// Trigger sandbox shutdown synchronously.
const stoppedSandbox = await sandbox.stop({ blocking: true });
```

Parameter | Type | Required | Details
---|---|---|---
`opts.blocking` | `boolean` | No | Wait for the sandbox to be marked stopped.
`opts.signal` | `AbortSignal` | No | Cancel the stop operation.
Returns: `Promise<Sandbox>`.
####  [`sandbox.updateNetworkPolicy()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.updatenetworkpolicy)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.updatenetworkpolicy)
Use `sandbox.updateNetworkPolicy()` to update the firewall settings applied to the sandbox egress traffic. The provided configuration fully replaces the pre-existing one. This allows for instance a user to start a sandbox, gather data, then run some untrusted program on it without risking data exfiltration.
```
await sandbox.updateNetworkPolicy('allow-all'); // Allow all egress from the sandbox

await sandbox.updateNetworkPolicy('deny-all'); // Block all egress from the sandbox

await sandbox.updateNetworkPolicy({allow: ["google.com", "ai-gateway.vercel.sh"]}); // Allow traffic to specific websites only

// Allow traffic to specific websites and private network
await sandbox.updateNetworkPolicy({
  allow: ["google.com", "ai-gateway.vercel.sh"],
  subnets: {
    allow: ["10.0.0.0/8"],
  },
});

// Allow traffic to the Internet while blocking private network
await sandbox.updateNetworkPolicy({
  subnets: {
    deny: ["10.0.0.0/8"],
  },
});

// Allow traffic to a specific website with credential brokering
await sandbox.updateNetworkPolicy({
  allow: {
    "ai-gateway.vercel.sh": [{
      transform: [{
        headers: {
          "x-api-key": "secret-key"
        }
      }]
    }]
  }
});
```

Parameter | Type | Required | Details
---|---|---|---
`networkPolicy` | `NetworkPolicy` | Yes | New firewall setup. Will fully replace the existing one.
`opts.signal` | `AbortSignal` | No | Cancel the operation.
Returns: `Promise<void>`.
####  [`sandbox.extendTimeout()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.extendtimeout)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.extendtimeout)
Use `sandbox.extendTimeout()` to extend the sandbox lifetime by the specified duration. This lets you keep the sandbox running up to the maximum execution timeout for your plan, so check `sandbox.timeout` first and extend only when necessary to avoid premature shutdown.
```
await sandbox.extendTimeout(60000); // Extend by 60 seconds
```

Parameter | Type | Required | Details
---|---|---|---
`duration` | `number` | Yes | Duration in milliseconds to extend the timeout by.
`opts.signal` | `AbortSignal` | No | Cancel the operation.
Returns: `Promise<void>`.
####  [`sandbox.snapshot()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.snapshot)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox.snapshot)
Call `sandbox.snapshot()` to capture the current state of the sandbox, including the filesystem and installed packages. Use snapshots to skip lengthy setup steps when creating new sandboxes. To learn more, see [Snapshots](https://vercel.com/docs/vercel-sandbox/concepts/snapshots).
The sandbox must be running to create a snapshot. Once you call this method, the sandbox shuts down automatically and becomes unreachable. You do not need to call `stop()` afterwards, and any subsequent commands to the sandbox will fail.
Snapshots expire after 30 days by default. Set `expiration` to `0` to disable expiration, or choose a custom duration in milliseconds (e.g., `ms('14d')`) to fit your workflow.
index.ts
```
const snapshot = await sandbox.snapshot({ expiration: ms('14d') });
console.log(snapshot.snapshotId);

// Later, create a new sandbox from the snapshot
const newSandbox = await Sandbox.create({
  source: { type: 'snapshot', snapshotId: snapshot.snapshotId },
});
```

Parameter | Type | Required | Details
---|---|---|---
`opts.expiration` | `number` | No | Optional expiration time in milliseconds. Use 0 for no expiration at all.
`opts.signal` | `AbortSignal` | No | Cancel the operation.
Returns: `Promise<Snapshot>`.
