# Find the checkpoint where an interrupt occurred
interrupted = next(
    s for s in history
    if s.tasks and any(t.interrupts for t in s.tasks)
)
```

### Replay

Replay re-executes steps from a prior checkpoint. Invoke the graph with a prior `checkpoint_id` to re-run nodes after that checkpoint. Nodes before the checkpoint are skipped (their results are already saved). Nodes after the checkpoint re-execute, including any LLM calls, API requests, or [interrupts](/oss/python/langgraph/interrupts) — which are always re-triggered during replay.

See [Time travel](/oss/python/langgraph/use-time-travel) for full details and code examples on replaying past executions.

<img alt="Replay" />

### Update state

You can edit the graph state using [`update_state`](https://reference.langchain.com/python/langgraph/graphs/#langgraph.graph.state.CompiledStateGraph.update_state). This creates a new checkpoint with the updated values — it does not modify the original checkpoint. The update is treated the same as a node update: values are passed through [reducer](/oss/python/langgraph/graph-api#reducers) functions when defined, so channels with reducers *accumulate* values rather than overwrite them.

You can optionally specify `as_node` to control which node the update is treated as coming from, which affects which node executes next. See [Time travel: `as_node`](/oss/python/langgraph/use-time-travel#from-a-specific-node) for details.

<img alt="Update" />

## Durability modes

LangGraph supports three durability modes that let you balance performance and data consistency. You can specify the durability mode when calling any graph execution method:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph.stream(
    {"input": "test"},
    durability="sync"
)
```

The durability modes, from least to most durable, are as follows:

* `"exit"`: LangGraph persists changes only when graph execution exits — successfully, with an error, or due to a human-in-the-loop interrupt. This provides the best performance for long-running graphs but means intermediate state is not saved, so you cannot recover from system failures (like process crashes) mid-execution.
* `"async"`: LangGraph persists changes asynchronously while the next step executes. This provides good performance and durability, but there is a small risk that LangGraph does not write checkpoints if the process crashes during execution.
* `"sync"`: LangGraph persists changes synchronously before the next step starts. This ensures that LangGraph writes every checkpoint before continuing execution, providing high durability at the cost of some performance overhead.

## Optimize checkpoint storage

By default, LangGraph checkpoints write the full value of every state channel at each super-step. For long-running threads with large accumulations—such as multi-turn conversations—this can produce significant storage growth over time.

[`DeltaChannel`](https://reference.langchain.com/python/langgraph/channels/delta/DeltaChannel) stores only incremental deltas instead of the full accumulated value, substantially reducing checkpoint size for append-heavy channels. See [DeltaChannel](/oss/python/langgraph/pregel#deltachannel) for usage and the storage-vs-latency tradeoff.

<Warning>
  `DeltaChannel` requires `langgraph>=1.2` and is currently in beta. The API may change in future releases.
</Warning>

## Checkpointer libraries

Under the hood, checkpointing is powered by checkpointer objects that conform to [`BaseCheckpointSaver`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver) interface. LangGraph provides several checkpointer implementations, all implemented via standalone, installable libraries.

<Note>
  See [checkpointer integrations](/oss/python/integrations/checkpointers/index) for available providers.
</Note>

* `langgraph-checkpoint`: The base interface for checkpointer savers ([`BaseCheckpointSaver`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver)) and serialization/deserialization interface ([`SerializerProtocol`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.serde.base.SerializerProtocol)). Includes in-memory checkpointer implementation ([`InMemorySaver`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.memory.InMemorySaver)) for experimentation. LangGraph comes with `langgraph-checkpoint` included.
* `langgraph-checkpoint-sqlite`: An implementation of LangGraph checkpointer that uses SQLite database ([`SqliteSaver`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.sqlite.SqliteSaver) / [`AsyncSqliteSaver`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver)). Ideal for experimentation and local workflows. Needs to be installed separately.
* `langgraph-checkpoint-postgres`: An advanced checkpointer that uses Postgres database ([`PostgresSaver`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.postgres.PostgresSaver) / [`AsyncPostgresSaver`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver)), used in LangSmith. Ideal for using in production. Needs to be installed separately.
* `langchain-azure-cosmosdb`: An implementation of LangGraph checkpointer that uses Azure Cosmos DB for NoSQL ([`CosmosDBSaverSync`](https://reference.langchain.com/python/langchain-azure-cosmosdb/) / [`CosmosDBSaver`](https://reference.langchain.com/python/langchain-azure-cosmosdb/)). Ideal for using in production with Azure. Supports both sync and async operations, with Microsoft Entra ID authentication. Needs to be installed separately.

### Checkpointer interface

Each checkpointer conforms to [`BaseCheckpointSaver`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver) interface and implements the following methods:

* `.put` - Store a checkpoint with its configuration and metadata.
* `.put_writes` - Store intermediate writes linked to a checkpoint (i.e. [pending writes](#pending-writes)).
* `.get_tuple` - Fetch a checkpoint tuple using for a given configuration (`thread_id` and `checkpoint_id`). This is used to populate `StateSnapshot` in `graph.get_state()`.
* `.list` - List checkpoints that match a given configuration and filter criteria. This is used to populate state history in `graph.get_state_history()`

If the checkpointer is used with asynchronous graph execution (i.e. executing the graph via `.ainvoke`, `.astream`, `.abatch`), asynchronous versions of the above methods will be used (`.aput`, `.aput_writes`, `.aget_tuple`, `.alist`).

<Note>
  For running your graph asynchronously, you can use [`InMemorySaver`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.memory.InMemorySaver), or async versions of Sqlite/Postgres checkpointers -- [`AsyncSqliteSaver`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.sqlite.aio.AsyncSqliteSaver) / [`AsyncPostgresSaver`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver) checkpointers.
</Note>

### Serializer

When checkpointers save the graph state, they need to serialize the channel values in the state. This is done using serializer objects.

`langgraph_checkpoint` defines [protocol](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.serde.base.SerializerProtocol) for implementing serializers provides a default implementation ([`JsonPlusSerializer`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.serde.jsonplus.JsonPlusSerializer)) that handles a wide variety of types, including LangChain and LangGraph primitives, datetimes, enums and more.

#### Serialization with `pickle`

The default serializer, [`JsonPlusSerializer`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.serde.jsonplus.JsonPlusSerializer), uses ormsgpack and JSON under the hood, which is not suitable for all types of objects.

If you want to fallback to pickle for objects not currently supported by the msgpack encoder (such as Pandas dataframes),
you can use the `pickle_fallback` argument of the [`JsonPlusSerializer`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.serde.jsonplus.JsonPlusSerializer):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.serde.jsonplus import JsonPlusSerializer

# ... Define the graph ...
graph.compile(
    checkpointer=InMemorySaver(serde=JsonPlusSerializer(pickle_fallback=True))
)
```

#### Encryption

Checkpointers can optionally encrypt all persisted state. To enable this, pass an instance of [`EncryptedSerializer`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.serde.encrypted.EncryptedSerializer) to the `serde` argument of any [`BaseCheckpointSaver`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver) implementation. The easiest way to create an encrypted serializer is via [`from_pycryptodome_aes`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.serde.encrypted.EncryptedSerializer.from_pycryptodome_aes), which reads the AES key from the `LANGGRAPH_AES_KEY` environment variable (or accepts a `key` argument):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import sqlite3

from langgraph.checkpoint.serde.encrypted import EncryptedSerializer
from langgraph.checkpoint.sqlite import SqliteSaver

serde = EncryptedSerializer.from_pycryptodome_aes()  # reads LANGGRAPH_AES_KEY
checkpointer = SqliteSaver(sqlite3.connect("checkpoint.db"), serde=serde)
```

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.checkpoint.serde.encrypted import EncryptedSerializer
from langgraph.checkpoint.postgres import PostgresSaver

serde = EncryptedSerializer.from_pycryptodome_aes()
checkpointer = PostgresSaver.from_conn_string("postgresql://...", serde=serde)
checkpointer.setup()
```

When running on LangSmith, encryption is automatically enabled whenever `LANGGRAPH_AES_KEY` is present, so you only need to provide the environment variable. Other encryption schemes can be used by implementing [`CipherProtocol`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.serde.base.CipherProtocol) and supplying it to [`EncryptedSerializer`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.serde.encrypted.EncryptedSerializer).

## Build a custom checkpointer

<Tip>
  Validate your implementation as you build using the [conformance test suite](#testing-with-the-conformance-suite). It covers all five base methods and extended capabilities including delta channels. Run it in CI before shipping.
</Tip>

This section covers implementing `BaseCheckpointSaver` from scratch for a custom storage backend. If you already have a working checkpointer and only need to add delta channel support, jump to [Delta channel support](#delta-channel-support).

### Overview

LangGraph's persistence layer is built on two storage abstractions:

* **Checkpoints table** — one row per superstep; stores the serialized graph state (`channel_values`, `channel_versions`, `versions_seen`) and links to its parent checkpoint.
* **Writes table** — one row per node output within a superstep; stores `(task_id, channel, value)` tuples linked to a checkpoint.

Your checkpointer manages both tables. `put` writes a checkpoint row; `put_writes` writes node-output rows; `get_tuple` reads both back into a `CheckpointTuple`.

### Base contract

Subclass `BaseCheckpointSaver` and implement these five methods. All are required — a missing base method raises `NotImplementedError` at runtime.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from collections.abc import AsyncIterator, Iterator, Sequence
from typing import Any
from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.base import (
    BaseCheckpointSaver,
    ChannelVersions,
    Checkpoint,
    CheckpointMetadata,
    CheckpointTuple,
)

class MyCheckpointer(BaseCheckpointSaver):
    async def aput(
        self,
        config: RunnableConfig,
        checkpoint: Checkpoint,
        metadata: CheckpointMetadata,
        new_versions: ChannelVersions,
    ) -> RunnableConfig:
        ...

    async def aput_writes(
        self,
        config: RunnableConfig,
        writes: Sequence[tuple[str, Any]],
        task_id: str,
        task_path: str = "",
    ) -> None:
        ...

    async def aget_tuple(self, config: RunnableConfig) -> CheckpointTuple | None:
        ...

    async def alist(
        self,
        config: RunnableConfig | None,
        *,
        filter: dict[str, Any] | None = None,
        before: RunnableConfig | None = None,
        limit: int | None = None,
    ) -> AsyncIterator[CheckpointTuple]:
        ...
        yield  # make this an async generator

    async def adelete_thread(self, thread_id: str) -> None:
        ...
```

#### put / aput

Store one checkpoint row. Return an updated config with the stored `checkpoint_id`.

Key requirements:

* Serialize the checkpoint using `self.serde.dumps_typed(checkpoint)` — this handles all LangGraph-native types including `_DeltaSnapshot` blobs used by delta channels.
* Store `metadata` in full — do not strip unknown keys. LangGraph adds new metadata fields (such as `counters_since_delta_snapshot` for delta channels) in minor releases; discarding them silently breaks features.
* Store `config["configurable"].get("checkpoint_id")` as the parent checkpoint ID so `get_tuple` can populate `parent_config`.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
async def aput(self, config, checkpoint, metadata, new_versions):
    thread_id = config["configurable"]["thread_id"]
    checkpoint_ns = config["configurable"]["checkpoint_ns"]
    checkpoint_id = checkpoint["id"]
    parent_id = config["configurable"].get("checkpoint_id")

    type_, blob = self.serde.dumps_typed(checkpoint)
    serialized_metadata = self.serde.dumps_typed(metadata)

    await self.db.execute(
        "INSERT INTO checkpoints (...) VALUES (...)",
        thread_id, checkpoint_ns, checkpoint_id, parent_id,
        type_, blob, *serialized_metadata,
    )
    return {
        "configurable": {
            "thread_id": thread_id,
            "checkpoint_ns": checkpoint_ns,
            "checkpoint_id": checkpoint_id,
        }
    }
```

#### put\_writes / aput\_writes

Store node-output rows for a single task within the current superstep. These rows are linked to the checkpoint by `(thread_id, checkpoint_ns, checkpoint_id)`.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
async def aput_writes(self, config, writes, task_id, task_path=""):
    thread_id = config["configurable"]["thread_id"]
    checkpoint_ns = config["configurable"]["checkpoint_ns"]
    checkpoint_id = config["configurable"]["checkpoint_id"]

    rows = []
    for idx, (channel, value) in enumerate(writes):
        type_, blob = self.serde.dumps_typed(value)
        final_idx = WRITES_IDX_MAP.get(channel, idx)
        rows.append((thread_id, checkpoint_ns, checkpoint_id,
                      task_id, task_path, final_idx, channel, type_, blob))

    await self.db.executemany("INSERT INTO writes (...) VALUES (...)", rows)
```

Import `WRITES_IDX_MAP` from `langgraph.checkpoint.base`. It maps special channels (`__error__`, `__interrupt__`, etc.) to reserved negative indices so they do not collide with regular write indices.

#### get\_tuple / aget\_tuple

Retrieve a checkpoint. The config may contain:

* **No `checkpoint_id`** — return the latest checkpoint for the thread + namespace.
* **A specific `checkpoint_id`** — return that exact checkpoint.

**Both paths must work correctly.** The specific-id path is used for time travel and — critically — for delta channel state reconstruction on every graph invocation (see [Delta channel support](#delta-channel-support)). A broken specific-id lookup silently corrupts delta channel state.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
async def aget_tuple(self, config):
    thread_id = config["configurable"]["thread_id"]
    checkpoint_ns = config["configurable"].get("checkpoint_ns", "")
    checkpoint_id = config["configurable"].get("checkpoint_id")

    if checkpoint_id:
        row = await self.db.fetchone(
            "SELECT * FROM checkpoints "
            "WHERE thread_id=? AND checkpoint_ns=? AND checkpoint_id=?",
            thread_id, checkpoint_ns, checkpoint_id,
        )
    else:
        row = await self.db.fetchone(
            "SELECT * FROM checkpoints "
            "WHERE thread_id=? AND checkpoint_ns=? "
            "ORDER BY checkpoint_id DESC LIMIT 1",
            thread_id, checkpoint_ns,
        )

    if row is None:
        return None

    writes = await self.db.fetchall(
        "SELECT task_id, channel, type, value FROM writes "
        "WHERE thread_id=? AND checkpoint_ns=? AND checkpoint_id=? "
        "ORDER BY task_id, idx",
        thread_id, checkpoint_ns, row["checkpoint_id"],
    )
    pending_writes = [
        (w["task_id"], w["channel"], self.serde.loads_typed((w["type"], w["value"])))
        for w in writes
    ]

    checkpoint = self.serde.loads_typed((row["type"], row["blob"]))
    metadata = self.serde.loads_typed((row["metadata_type"], row["metadata"]))

    parent_config = None
    if row["parent_checkpoint_id"]:
        parent_config = {
            "configurable": {
                "thread_id": thread_id,
                "checkpoint_ns": checkpoint_ns,
                "checkpoint_id": row["parent_checkpoint_id"],
            }
        }

    return CheckpointTuple(
        config={
            "configurable": {
                "thread_id": thread_id,
                "checkpoint_ns": checkpoint_ns,
                "checkpoint_id": row["checkpoint_id"],
            }
        },
        checkpoint=checkpoint,
        metadata=metadata,
        parent_config=parent_config,
        pending_writes=pending_writes,
    )
```

<Warning>
  **Row key / index design matters for the specific-id lookup.** If your storage uses a time-ordered key (e.g., a reversed timestamp) that does not embed `checkpoint_id`, you cannot do a direct row read by id. You must either encode `checkpoint_id` in the row key, or build a secondary index. A scan with a value filter on every lookup works but does not scale.
</Warning>

#### list / alist

Return checkpoints for a thread, newest first. Respect `before` (return only checkpoints older than that config's `checkpoint_id`) and `limit`.

#### delete\_thread / adelete\_thread

Delete all checkpoints and writes for a thread. Both checkpoint rows and write rows must be deleted.

### Row key / index design

How you store and index checkpoints directly affects correctness and performance.

**Recommended schema (SQL):**

```sql theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
CREATE TABLE checkpoints (
    thread_id          TEXT NOT NULL,
    checkpoint_ns      TEXT NOT NULL DEFAULT '',
    checkpoint_id      TEXT NOT NULL,   -- ULID, lexicographically sortable newest-last
    parent_checkpoint_id TEXT,
    type               TEXT,
    checkpoint         BYTEA,
    metadata           JSONB,
    PRIMARY KEY (thread_id, checkpoint_ns, checkpoint_id)
);

CREATE TABLE writes (
    thread_id     TEXT NOT NULL,
    checkpoint_ns TEXT NOT NULL DEFAULT '',
    checkpoint_id TEXT NOT NULL,
    task_id       TEXT NOT NULL,
    task_path     TEXT NOT NULL DEFAULT '',
    idx           INTEGER NOT NULL,
    channel       TEXT NOT NULL,
    type          TEXT,
    value         BYTEA,
    PRIMARY KEY (thread_id, checkpoint_ns, checkpoint_id, task_id, task_path, idx)
);
```

Because `checkpoint_id` is a ULID, it sorts lexicographically — larger values are newer. "Get latest" is `ORDER BY checkpoint_id DESC LIMIT 1`; "get by id" is an equality lookup on the primary key.

**For non-SQL stores:** the same principle applies. Whatever key scheme you use, direct lookup by `(thread_id, checkpoint_ns, checkpoint_id)` must be O(1) or close to it. Avoid designs where the only way to find a checkpoint by id is to scan all rows for a thread.

### Serialization

Always use `self.serde` (inherited from `BaseCheckpointSaver`, defaults to `JsonPlusSerializer`) for checkpoints, writes, and metadata. Do not use `pickle` directly for metadata — it works, but `JsonPlusSerializer` produces human-readable output and handles versioning better.

`JsonPlusSerializer` handles all LangGraph-native types automatically:

* `_DeltaSnapshot` — the sentinel blob used by delta channels (msgpack ext code 7)
* Pydantic v2 models, dataclasses, numpy arrays, datetimes, enums, and more

If you write a custom serializer, make sure it can round-trip `_DeltaSnapshot` from `langgraph.checkpoint.serde.types`.

### Extended capabilities

These methods are optional but unlock additional Agent Server features. Implement them if your storage backend can support them efficiently.

| Method                       | What it enables                                          |
| ---------------------------- | -------------------------------------------------------- |
| `adelete_for_runs`           | Rollback multitask strategy                              |
| `acopy_thread`               | Efficient thread forking                                 |
| `aprune`                     | Thread history pruning                                   |
| `aget_delta_channel_history` | Efficient delta channel state reconstruction (see below) |

Agent Server auto-detects which capabilities your checkpointer implements at startup and activates the corresponding features.

### Delta channel support

<Info>
  **DeltaChannel is in beta.** The API and on-disk representation may change while the design stabilizes.
</Info>

`DeltaChannel` is a reducer channel that stores only a sentinel (`MISSING`) in checkpoint blobs instead of the full channel value. State is reconstructed by replaying ancestor writes through the reducer. This makes checkpoint blobs O(1) per step instead of O(N) for channels like `messages` that accumulate over time.

#### What the runtime needs

When loading a checkpoint whose delta channels are absent from `channel_values`, LangGraph calls `saver.get_delta_channel_history(config=config, channels=[...])`. This returns, for each channel:

* **`writes`** — all writes to that channel in the ancestor chain, oldest first, up to the nearest snapshot.
* **`seed`** (optional) — the stored `_DeltaSnapshot` blob at the nearest ancestor that has one; absent if the walk reaches the root without finding a snapshot.

The runtime then calls `channel.from_checkpoint(seed)` and `channel.replay_writes(writes)` to reconstruct the live value.

#### Default implementation

`BaseCheckpointSaver` provides a default `get_delta_channel_history` that works with any correct `get_tuple` implementation:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Simplified from BaseCheckpointSaver
def get_delta_channel_history(self, *, config, channels):
    target = self.get_tuple(config)          # load the head checkpoint
    cursor = target.parent_config            # walk from its parent
    collected = {ch: [] for ch in channels}
    seed = {}
    remaining = set(channels)

    while cursor and remaining:
        tup = self.get_tuple(cursor)         # ← requires correct by-id lookup
        if tup is None:
            break
        for write in reversed(tup.pending_writes or []):
            if write[1] in remaining:
                collected[write[1]].append(write)
        for ch in list(remaining):
            if ch in tup.checkpoint["channel_values"]:
                seed[ch] = tup.checkpoint["channel_values"][ch]
                remaining.discard(ch)
        cursor = tup.parent_config

    return {
        ch: {"writes": list(reversed(collected[ch])), **({"seed": seed[ch]} if ch in seed else {})}
        for ch in channels
    }
```

**The critical dependency:** `get_tuple(cursor)` is always called with a specific `checkpoint_id` (the parent's id). If that lookup returns `None`, the walk stops immediately and every delta channel reconstructs as empty — silently, with no error. This is why the specific-id path in `get_tuple` must be correct.

#### Performance override

The default walk issues one `get_tuple` call per ancestor checkpoint. For backends with good query support, override `get_delta_channel_history` (and its async twin) to retrieve the ancestor chain and writes in two queries:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
async def aget_delta_channel_history(self, *, config, channels):
    if not channels:
        return {}

    thread_id = config["configurable"]["thread_id"]
    checkpoint_ns = config["configurable"].get("checkpoint_ns", "")
    checkpoint_id = config["configurable"]["checkpoint_id"]

    # Stage 1: stream ancestors newest-first until every channel has a seed
    ancestors = await self.db.fetchall(
        "SELECT checkpoint_id, parent_checkpoint_id, type, checkpoint "
        "FROM checkpoints "
        "WHERE thread_id=? AND checkpoint_ns=? AND checkpoint_id < ? "
        "ORDER BY checkpoint_id DESC",
        thread_id, checkpoint_ns, checkpoint_id,
    )

    chain_by_ch: dict[str, list[str]] = {ch: [] for ch in channels}
    seed_by_ch: dict[str, Any] = {}
    remaining = set(channels)
    cur_id = config["configurable"]["checkpoint_id"]

    for row in ancestors:
        if not remaining:
            break
        parent_id = row["parent_checkpoint_id"]
        ckpt = self.serde.loads_typed((row["type"], row["checkpoint"]))
        cv = ckpt.get("channel_values") or {}
        for ch in list(remaining):
            chain_by_ch[ch].append(row["checkpoint_id"])
            if ch in cv:
                seed_by_ch[ch] = cv[ch]
                remaining.discard(ch)
        cur_id = parent_id

    # Stage 2: fetch writes for each channel's ancestor chain in one query
    result: dict[str, DeltaChannelHistory] = {}
    for ch in channels:
        chain = chain_by_ch[ch]
        if not chain:
            entry: DeltaChannelHistory = {"writes": []}
            if ch in seed_by_ch:
                entry["seed"] = seed_by_ch[ch]
            result[ch] = entry
            continue

        write_rows = await self.db.fetchall(
            f"SELECT checkpoint_id, task_id, idx, type, value FROM writes "
            f"WHERE thread_id=? AND checkpoint_ns=? AND channel=? "
            f"AND checkpoint_id IN ({','.join('?' * len(chain))})"
            f"ORDER BY checkpoint_id, task_id, idx",
            thread_id, checkpoint_ns, ch, *chain,
        )
        writes_by_cid: dict[str, list[PendingWrite]] = {}
        for row in write_rows:
            cid = row["checkpoint_id"]
            value = self.serde.loads_typed((row["type"], row["value"]))
            writes_by_cid.setdefault(cid, []).append((row["task_id"], ch, value))

        # chain is newest-first; iterate oldest-first to get correct replay order
        collected: list[PendingWrite] = []
        for cid in reversed(chain):
            collected.extend(writes_by_cid.get(cid, []))

        entry = {"writes": collected}
        if ch in seed_by_ch:
            entry["seed"] = seed_by_ch[ch]
        result[ch] = entry

    return result
```

#### Pruning with delta channels

`DeltaChannel` state is not self-contained in a single checkpoint — it depends on the ancestor write chain back to the nearest `_DeltaSnapshot`. If you implement `prune` or `delete_for_runs`, you must not delete write rows that a surviving checkpoint's delta channels depend on.

Safe options:

1. **Walk before pruning** — for each checkpoint you intend to keep, walk its ancestor chain and mark all write rows up to the nearest `_DeltaSnapshot` as non-deletable.
2. **Force a snapshot before pruning** — rewrite `channel_values[ch] = _DeltaSnapshot(reconstructed_value)` on the checkpoint you are keeping, then delete ancestors freely.
3. **Skip pruning for delta-channel threads** — the safest short-term option if you do not yet need pruning.

#### Copy thread with delta channels

When implementing `copy_thread`, copy the complete ancestor chain — not just the head checkpoint. The target thread must have write rows going back to at least one `_DeltaSnapshot` for every delta channel, or those channels will reconstruct as empty after the copy.

### Testing with the conformance suite

`langgraph-checkpoint-conformance` validates your implementation against the full contract, including delta channel history:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
pip install langgraph-checkpoint-conformance
```

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import asyncio
from langgraph.checkpoint.conformance import checkpointer_test, validate

@checkpointer_test(name="MyCheckpointer")
async def my_checkpointer():
    async with MyCheckpointer.create() as saver:
        yield saver

async def main():
    report = await validate(my_checkpointer)
    report.print_report()
    # Fails the process if any base capability is missing or broken
    if not report.passed_all_base():
        raise RuntimeError("Checkpointer failed conformance suite")

asyncio.run(main())
```

The suite auto-detects which extended capabilities your checkpointer implements (including `aget_delta_channel_history`) and runs the relevant tests for each. Run it as part of your CI before shipping.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/checkpointers.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Choosing between Graph and Functional APIs
Source: https://docs.langchain.com/oss/python/langgraph/choosing-apis

LangGraph provides two different APIs to build agent workflows: the **Graph API** and the **Functional API**. Both APIs share the same underlying runtime and can be used together in the same application, but they are designed for different use cases and development preferences.

This guide will help you understand when to use each API based on your specific requirements.

## Quick decision guide

Use the **Graph API** when you need:

* **Complex workflow visualization** for debugging and documentation
* **Explicit state management** with shared data across multiple nodes
* **Conditional branching** with multiple decision points
* **Parallel execution paths** that need to merge later
* **Team collaboration** where visual representation aids understanding

Use the **Functional API** when you want:

* **Minimal code changes** to existing procedural code
* **Standard control flow** (if/else, loops, function calls)
* **Function-scoped state** without explicit state management
* **Rapid prototyping** with less boilerplate
* **Linear workflows** with simple branching logic

## Detailed comparison

### When to use the Graph API

The [Graph API](/oss/python/langgraph/graph-api) uses a declarative approach where you define nodes, edges, and shared state to create a visual graph structure.

**1. Complex decision trees and branching logic**

When your workflow has multiple decision points that depend on various conditions, the Graph API makes these branches explicit and easy to visualize.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Graph API: Clear visualization of decision paths
from langgraph.graph import StateGraph
from typing import TypedDict

class AgentState(TypedDict):
    messages: list
    current_tool: str
    retry_count: int

def should_continue(state):
    if state["retry_count"] > 3:
        return "end"
    elif state["current_tool"] == "search":
        return "process_search"
    else:
        return "call_llm"

workflow = StateGraph(AgentState)
workflow.add_node("call_llm", call_llm_node)
workflow.add_node("process_search", search_node)
workflow.add_conditional_edges("call_llm", should_continue)
```

**2. State management across multiple components**

When you need to share and coordinate state between different parts of your workflow, the Graph API's explicit state management is beneficial.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Multiple nodes can access and modify shared state
class WorkflowState(TypedDict):
    user_input: str
    search_results: list
    generated_response: str
    validation_status: str

def search_node(state):
    # Access shared state
    results = search(state["user_input"])
    return {"search_results": results}

def validation_node(state):
    # Access results from previous node
    is_valid = validate(state["generated_response"])
    return {"validation_status": "valid" if is_valid else "invalid"}
```

**3. Parallel processing with synchronization**

When you need to run multiple operations in parallel and then combine their results, the Graph API handles this naturally.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Parallel processing of multiple data sources
workflow.add_node("fetch_news", fetch_news)
workflow.add_node("fetch_weather", fetch_weather)
workflow.add_node("fetch_stocks", fetch_stocks)
workflow.add_node("combine_data", combine_all_data)

# All fetch operations run in parallel
workflow.add_edge(START, "fetch_news")
workflow.add_edge(START, "fetch_weather")
workflow.add_edge(START, "fetch_stocks")

# Combine waits for all parallel operations to complete
workflow.add_edge("fetch_news", "combine_data")
workflow.add_edge("fetch_weather", "combine_data")
workflow.add_edge("fetch_stocks", "combine_data")
```

**4. Team development and documentation**

The visual nature of the Graph API makes it easier for teams to understand, document, and maintain complex workflows.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Clear separation of concerns - each team member can work on different nodes
workflow.add_node("data_ingestion", data_team_function)
workflow.add_node("ml_processing", ml_team_function)
workflow.add_node("business_logic", product_team_function)
workflow.add_node("output_formatting", frontend_team_function)
```

### When to use the Functional API

The [Functional API](/oss/python/langgraph/functional-api) uses an imperative approach that integrates LangGraph features into standard procedural code.

**1. Existing procedural code**

When you have existing code that uses standard control flow and want to add LangGraph features with minimal refactoring.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Functional API: Minimal changes to existing code
from langgraph.func import entrypoint, task

@task
def process_user_input(user_input: str) -> dict:
    # Existing function with minimal changes
    return {"processed": user_input.lower().strip()}

@entrypoint(checkpointer=checkpointer)
def workflow(user_input: str) -> str:
    # Standard Python control flow
    processed = process_user_input(user_input).result()

    if "urgent" in processed["processed"]:
        response = handle_urgent_request(processed).result()
    else:
        response = handle_normal_request(processed).result()

    return response
```

**2. Linear workflows with simple logic**

When your workflow is primarily sequential with straightforward conditional logic.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
@entrypoint(checkpointer=checkpointer)
def essay_workflow(topic: str) -> dict:
    # Linear flow with simple branching
    outline = create_outline(topic).result()

    if len(outline["points"]) < 3:
        outline = expand_outline(outline).result()

    draft = write_draft(outline).result()

    # Human review checkpoint
    feedback = interrupt({"draft": draft, "action": "Please review"})

    if feedback == "approve":
        final_essay = draft
    else:
        final_essay = revise_essay(draft, feedback).result()

    return {"essay": final_essay}
```

**3. Rapid prototyping**

When you want to quickly test ideas without the overhead of defining state schemas and graph structures.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
@entrypoint(checkpointer=checkpointer)
def quick_prototype(data: dict) -> dict:
    # Fast iteration - no state schema needed
    step1_result = process_step1(data).result()
    step2_result = process_step2(step1_result).result()

    return {"final_result": step2_result}
```

**4. Function-scoped state management**

When your state is naturally scoped to individual functions and doesn't need to be shared broadly.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
@task
def analyze_document(document: str) -> dict:
    # Local state management within function
    sections = extract_sections(document)
    summaries = [summarize(section) for section in sections]
    key_points = extract_key_points(summaries)

    return {
        "sections": len(sections),
        "summaries": summaries,
        "key_points": key_points
    }

@entrypoint(checkpointer=checkpointer)
def document_processor(document: str) -> dict:
    analysis = analyze_document(document).result()
    # State is passed between functions as needed
    return generate_report(analysis).result()
```

## Combining both APIs

You can use both APIs together in the same application. This is useful when different parts of your system have different requirements.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.graph import StateGraph
from langgraph.func import entrypoint

# Complex multi-agent coordination using Graph API
coordination_graph = StateGraph(CoordinationState)
coordination_graph.add_node("orchestrator", orchestrator_node)
coordination_graph.add_node("agent_a", agent_a_node)
coordination_graph.add_node("agent_b", agent_b_node)

# Simple data processing using Functional API
@entrypoint()
def data_processor(raw_data: dict) -> dict:
    cleaned = clean_data(raw_data).result()
    transformed = transform_data(cleaned).result()
    return transformed

# Use the functional API result in the graph
def orchestrator_node(state):
    processed_data = data_processor.invoke(state["raw_data"])
    return {"processed_data": processed_data}
```

## Migration between APIs

### From Functional to Graph API

When your functional workflow grows complex, you can migrate to the Graph API:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Before: Functional API
@entrypoint(checkpointer=checkpointer)
def complex_workflow(input_data: dict) -> dict:
    step1 = process_step1(input_data).result()

    if step1["needs_analysis"]:
        analysis = analyze_data(step1).result()
        if analysis["confidence"] > 0.8:
            result = high_confidence_path(analysis).result()
        else:
            result = low_confidence_path(analysis).result()
    else:
        result = simple_path(step1).result()

    return result

# After: Graph API
class WorkflowState(TypedDict):
    input_data: dict
    step1_result: dict
    analysis: dict
    final_result: dict

def should_analyze(state):
    return "analyze" if state["step1_result"]["needs_analysis"] else "simple_path"

def confidence_check(state):
    return "high_confidence" if state["analysis"]["confidence"] > 0.8 else "low_confidence"

workflow = StateGraph(WorkflowState)
workflow.add_node("step1", process_step1_node)
workflow.add_conditional_edges("step1", should_analyze)
workflow.add_node("analyze", analyze_data_node)
workflow.add_conditional_edges("analyze", confidence_check)

# ... add remaining nodes and edges
```

### From Graph to Functional API

When your graph becomes overly complex for simple linear processes:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Before: Over-engineered Graph API
class SimpleState(TypedDict):
    input: str
    step1: str
    step2: str
    result: str

# After: Simplified Functional API
@entrypoint(checkpointer=checkpointer)
def simple_workflow(input_data: str) -> str:
    step1 = process_step1(input_data).result()
    step2 = process_step2(step1).result()
    return finalize_result(step2).result()
```

## Summary

Choose the **Graph API** when you need explicit control over workflow structure, complex branching, parallel processing, or team collaboration benefits.

Choose the **Functional API** when you want to add LangGraph features to existing code with minimal changes, have simple linear workflows, or need rapid prototyping capabilities.

Both APIs provide the same core LangGraph features (persistence, streaming, human-in-the-loop, memory) but package them in different paradigms to suit different development styles and use cases.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/choosing-apis.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith Deployment
Source: https://docs.langchain.com/oss/python/langgraph/deploy

This guide shows you how to deploy your agent to **[LangSmith Cloud](/langsmith/deploy-to-cloud)**, a fully managed hosting platform designed for agent workloads. With Cloud deployment, you can deploy directly from your GitHub repository—LangSmith handles the infrastructure, scaling, and operational concerns.

Traditional hosting platforms are built for stateless, short-lived web applications. LangSmith Cloud is **purpose-built for stateful, long-running agents** that require persistent state and background execution.

<Tip>
  LangSmith offers multiple deployment options beyond Cloud, including [hybrid](/langsmith/hybrid), [standalone servers](/langsmith/deploy-standalone-server), and [self-hosted with control plane](/langsmith/deploy-with-control-plane). For more information, refer to the [Deployment overview](/langsmith/deployment).
</Tip>

## Prerequisites

Before you begin, ensure you have the following:

* A [GitHub account](https://github.com/)
* A [LangSmith account](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langgraph-deploy) (free to sign up)

## Deploy your agent

### 1. Create a repository on GitHub

Your application's code must reside in a GitHub repository to be deployed on LangSmith. Both public and private repositories are supported. For this quickstart, first make sure your app is LangGraph-compatible by following the [local server setup guide](/oss/python/langgraph/studio#set-up-local-agent-server). Then, push your code to the repository.

### 2. Deploy to LangSmith

<Steps>
  <Step title="Navigate to LangSmith Deployment">
    Log in to [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langgraph-deploy). In the left sidebar, select **Deployments**.
  </Step>

  <Step title="Create new deployment">
    Click the **+ New Deployment** button. A pane will open where you can fill in the required fields.
  </Step>

  <Step title="Link repository">
    If you are a first time user or adding a private repository that has not been previously connected, click the **Add new account** button and follow the instructions to connect your GitHub account.
  </Step>

  <Step title="Deploy repository">
    Select your application's repository. Click **Submit** to deploy. This may take about 15 minutes to complete. You can check the status in the **Deployment details** view.
  </Step>
</Steps>

### 3. Test your application in Studio

Once your application is deployed:

1. Select the deployment you just created to view more details.
2. Click the **Studio** button in the top right corner. Studio will open to display your graph.

### 4. Get the API URL for your deployment

1. In the **Deployment details** view in LangGraph, click the **API URL** to copy it to your clipboard.
2. Click the `URL` to copy it to the clipboard.

### 5. Test the API

You can now test the API:

<Tabs>
  <Tab title="Python">
    1. Install LangGraph SDK:

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install langgraph-sdk
    ```

    2. Send a message to the agent:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph_sdk import get_sync_client # or get_client for async

    client = get_sync_client(url="your-deployment-url", api_key="your-langsmith-api-key")

    for chunk in client.runs.stream(
        None,    # Threadless run
        "agent", # Name of agent. Defined in langgraph.json.
        input={
            "messages": [{
                "role": "human",
                "content": "What is LangGraph?",
            }],
        },
        stream_mode="updates",
    ):
        print(f"Receiving new event of type: {chunk.event}...")
        print(chunk.data)
        print("\n\n")
    ```
  </Tab>

  <Tab title="Rest API">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl -s --request POST \
        --url <DEPLOYMENT_URL>/runs/stream \
        --header 'Content-Type: application/json' \
        --header "X-Api-Key: <LANGSMITH API KEY> \
        --data "{
            \"assistant_id\": \"agent\", `# Name of agent. Defined in langgraph.json.`
            \"input\": {
                \"messages\": [
                    {
                        \"role\": \"human\",
                        \"content\": \"What is LangGraph?\"
                    }
                ]
            },
            \"stream_mode\": \"updates\"
        }"
    ```
  </Tab>
</Tabs>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/deploy.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
