##  [Snapshot class](https://vercel.com/docs/vercel-sandbox/sdk-reference#snapshot-class)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#snapshot-class)
A `Snapshot` represents a saved state of a sandbox that you can use to create new sandboxes. Snapshots capture the filesystem, installed packages, and environment configuration, letting you skip setup steps and start new sandboxes faster. To learn more, see [Snapshots](https://vercel.com/docs/vercel-sandbox/concepts/snapshots).
Create snapshots with `sandbox.snapshot()` or retrieve existing ones with `Snapshot.get()`.
###  [Snapshot class accessors](https://vercel.com/docs/vercel-sandbox/sdk-reference#snapshot-class-accessors)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#snapshot-class-accessors)
####  [`snapshotId`](https://vercel.com/docs/vercel-sandbox/sdk-reference#snapshotid)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#snapshotid)
Use `snapshotId` to identify the snapshot when creating new sandboxes or retrieving it later. Store this ID to reuse the snapshot across multiple sandbox instances.
Returns: `string`.
index.ts
```
console.log(snapshot.snapshotId);
```

####  [`sourceSandboxId`](https://vercel.com/docs/vercel-sandbox/sdk-reference#sourcesandboxid)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#sourcesandboxid)
The `sourceSandboxId` accessor returns the ID of the sandbox that produced this snapshot. Use this to trace the origin of a snapshot or correlate it with sandbox logs.
Returns: `string`.
index.ts
```
console.log(snapshot.sourceSandboxId);
```

####  [`status`](https://vercel.com/docs/vercel-sandbox/sdk-reference#status)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#status)
The `status` accessor reports the current state of the snapshot. Check this value to confirm the snapshot creation succeeded before using it.
Returns: `"created" | "deleted" | "failed"`.
index.ts
```
console.log(snapshot.status);
```

####  [`sizeBytes`](https://vercel.com/docs/vercel-sandbox/sdk-reference#sizebytes)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#sizebytes)
The `sizeBytes` accessor returns the size of the snapshot in bytes. Use this to monitor storage usage.
Returns: `number`.
```
console.log(snapshot.sizeBytes);
```

####  [`createdAt`](https://vercel.com/docs/vercel-sandbox/sdk-reference#createdat)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#createdat)
The `createdAt` accessor returns the date and time when the snapshot was created.
Returns: `Date`.
```
console.log(snapshot.createdAt);
```

####  [`expiresAt`](https://vercel.com/docs/vercel-sandbox/sdk-reference#expiresat)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#expiresat)
The `expiresAt` accessor returns the date and time when the snapshot will automatically expire and be deleted. If the snapshot was created with `expiration: 0`, this value is `null`.
Returns: `Date | null`.
```
if (snapshot.expiresAt) {
  console.log(snapshot.expiresAt.toISOString());
}
```

###  [Snapshot class static methods](https://vercel.com/docs/vercel-sandbox/sdk-reference#snapshot-class-static-methods)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#snapshot-class-static-methods)
####  [`Snapshot.list()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#snapshot.list)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#snapshot.list)
Use `Snapshot.list()` to enumerate snapshots for a project, with the option to filter by time range or page size. To resume after restarts without missing entries, combine `since` and `until` with the pagination cursor and cache the last `pagination.next` value.
Returns: `Promise<Parsed<{ snapshots: SnapshotSummary[]; pagination: Pagination; }>>`.
Parameter | Type | Required | Details
---|---|---|---
`projectId` | `string` | No | Project whose snapshots you want to list.
`limit` | `number` | No | Maximum number of snapshots to return.
`since` | `number | Date` | No | List snapshots created after this time.
`until` | `number | Date` | No | List snapshots created before this time.
`signal` | `AbortSignal` | No | Cancel the request if necessary.
```
const { json: { snapshots, pagination } } = await Snapshot.list();
```

####  [`Snapshot.get()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#snapshot.get)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#snapshot.get)
Use `Snapshot.get()` to retrieve an existing snapshot by its ID.
Returns: `Promise<Snapshot>`.
Parameter | Type | Required | Details
---|---|---|---
`snapshotId` | `string` | Yes | Identifier of the snapshot to retrieve.
`signal` | `AbortSignal` | No | Cancel the request if necessary.
index.ts
```
import { Snapshot } from '@vercel/sandbox';

const snapshot = await Snapshot.get({ snapshotId: 'snap_abc123' });
console.log(snapshot.status);
```

###  [Snapshot class instance methods](https://vercel.com/docs/vercel-sandbox/sdk-reference#snapshot-class-instance-methods)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#snapshot-class-instance-methods)
####  [`snapshot.delete()`](https://vercel.com/docs/vercel-sandbox/sdk-reference#snapshot.delete)[](https://vercel.com/docs/vercel-sandbox/sdk-reference#snapshot.delete)
Call `snapshot.delete()` to remove a snapshot you no longer need. Deleting unused snapshots helps manage storage and keeps your snapshot list organized.
Returns: `Promise<void>`.
Parameter | Type | Required | Details
---|---|---|---
`opts.signal` | `AbortSignal` | No | Cancel the operation.
index.ts
```
await snapshot.delete();
```
