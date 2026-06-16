# after
import chromadb
client = chromadb.HttpClient(host="localhost", port="8000")

```

You can still also access the underlying `.Client()` method. If you want to turn off telemetry, all clients support custom settings:

```python theme={null}
import chromadb
from chromadb.config import Settings
client = chromadb.PersistentClient(
    path="/path/to/persist/directory",
    settings=Settings(anonymized_telemetry=False))
```

**New data layout**

This version of Chroma drops `duckdb` and `clickhouse` in favor of `sqlite` for metadata storage. This means migrating data over. We have created a migration CLI utility to do this.

If you upgrade to `0.4.0` and try to access data stored in the old way, you will see this error message

> You are using a deprecated configuration of Chroma. Please pip install chroma-migrate and run `chroma-migrate` to upgrade your configuration. See [https://docs.trychroma.com/deployment/migration](https://docs.trychroma.com/deployment/migration) for more information or join our discord at [https://discord.gg/MMeYNTmh3x](https://discord.gg/MMeYNTmh3x) for help!

Here is how to install and use the CLI:

```bash theme={null}
pip install chroma-migrate
chroma-migrate
```

If you need any help with this migration, please reach out! We are on [Discord](https://discord.com/channels/1073293645303795742/1129286514845691975) ready to help.

**Persist & Reset**

`.persist()` was in the old version of Chroma because writes were only flushed when forced to. Chroma `0.4.0` saves all writes to disk instantly and so `persist` is no longer needed.

`.reset()`, which resets the entire database, used to by enabled-by-default which felt wrong. `0.4.0` has it disabled-by-default. You can enable it again by passing `allow_reset=True` to a Settings object. For example:

```python theme={null}
import chromadb
from chromadb.config import Settings
client = chromadb.PersistentClient(path="./path/to/chroma", settings=Settings(allow_reset=True))
```
