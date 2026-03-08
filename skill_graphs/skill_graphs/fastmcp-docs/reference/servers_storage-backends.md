[Skip to main content](https://gofastmcp.com/servers/storage-backends#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Features
Storage Backends
Search the docs...
Ctrl K
Documentation
##### Get Started
  * [Welcome!](https://gofastmcp.com/getting-started/welcome)
  * [Installation](https://gofastmcp.com/getting-started/installation)
  * [Quickstart](https://gofastmcp.com/getting-started/quickstart)


##### Servers
  * [Overview](https://gofastmcp.com/servers/server)
  * Core Components
  * FeaturesUPDATED
    * [ Background Tasks NEW ](https://gofastmcp.com/servers/tasks)
    * [Composition](https://gofastmcp.com/servers/composition)
    * [ Dependencies NEW ](https://gofastmcp.com/servers/dependency-injection)
    * [Elicitation](https://gofastmcp.com/servers/elicitation)
    * [Icons](https://gofastmcp.com/servers/icons)
    * [ Lifespan NEW ](https://gofastmcp.com/servers/lifespan)
    * [Logging](https://gofastmcp.com/servers/logging)
    * [Middleware](https://gofastmcp.com/servers/middleware)
    * [ Pagination NEW ](https://gofastmcp.com/servers/pagination)
    * [Progress](https://gofastmcp.com/servers/progress)
    * [Sampling](https://gofastmcp.com/servers/sampling)
    * [ Storage Backends NEW ](https://gofastmcp.com/servers/storage-backends)
    * [ Telemetry NEW ](https://gofastmcp.com/servers/telemetry)
    * [Testing](https://gofastmcp.com/servers/testing)
    * [ Versioning NEW ](https://gofastmcp.com/servers/versioning)
  * ProvidersNEW
  * TransformsNEW
  * AuthenticationUPDATED
  * [ Authorization NEW ](https://gofastmcp.com/servers/authorization)
  * Deployment


##### Apps
  * [ Overview NEW ](https://gofastmcp.com/apps/overview)
  * [ Prefab Apps SOON ](https://gofastmcp.com/apps/prefab)
  * [ Patterns SOON ](https://gofastmcp.com/apps/patterns)
  * [ Custom HTML NEW ](https://gofastmcp.com/apps/low-level)


##### Clients
  * [Overview](https://gofastmcp.com/clients/client)
  * [Transports](https://gofastmcp.com/clients/transports)
  * Core Operations
  * HandlersUPDATED
  * AuthenticationUPDATED


##### Integrations
  * Auth
  * Web Frameworks
  * AI Assistants
  * AI SDKs
  * [MCP.json](https://gofastmcp.com/integrations/mcp-json-configuration)


##### CLI
  * [Overview](https://gofastmcp.com/cli/overview)
  * [Running](https://gofastmcp.com/cli/running)
  * [Install MCPs](https://gofastmcp.com/cli/install-mcp)
  * [Inspecting](https://gofastmcp.com/cli/inspecting)
  * [Client](https://gofastmcp.com/cli/client)
  * [Generate CLI](https://gofastmcp.com/cli/generate-cli)
  * [Auth](https://gofastmcp.com/cli/auth)


##### More
  * Upgrading
  * Development
  * What's New


On this page
  * [Available Backends](https://gofastmcp.com/servers/storage-backends#available-backends)
  * [In-Memory Storage](https://gofastmcp.com/servers/storage-backends#in-memory-storage)
  * [File Storage](https://gofastmcp.com/servers/storage-backends#file-storage)
  * [Redis](https://gofastmcp.com/servers/storage-backends#redis)
  * [Other Backends from py-key-value-aio](https://gofastmcp.com/servers/storage-backends#other-backends-from-py-key-value-aio)
  * [Use Cases in FastMCP](https://gofastmcp.com/servers/storage-backends#use-cases-in-fastmcp)
  * [Server-Side OAuth Token Storage](https://gofastmcp.com/servers/storage-backends#server-side-oauth-token-storage)
  * [Response Caching Middleware](https://gofastmcp.com/servers/storage-backends#response-caching-middleware)
  * [Client-Side OAuth Token Storage](https://gofastmcp.com/servers/storage-backends#client-side-oauth-token-storage)
  * [Choosing a Backend](https://gofastmcp.com/servers/storage-backends#choosing-a-backend)
  * [More Resources](https://gofastmcp.com/servers/storage-backends#more-resources)


Features
# Storage Backends
Copy page
Configure persistent and distributed storage for caching and OAuth state management
Copy page
`2.13.0` FastMCP uses pluggable storage backends for caching responses and managing OAuth state. By default, all storage is in-memory, which is perfect for development but doesn’t persist across restarts. FastMCP includes support for multiple storage backends, and you can easily extend it with custom implementations.
The storage layer is powered by
##
[​](https://gofastmcp.com/servers/storage-backends#available-backends)
Available Backends
###
[​](https://gofastmcp.com/servers/storage-backends#in-memory-storage)
In-Memory Storage
**Best for:** Development, testing, single-process deployments In-memory storage is the default for all FastMCP storage needs. It’s fast, requires no setup, and is perfect for getting started.
Copy
```
from key_value.aio.stores.memory import MemoryStore

# Used by default - no configuration needed
# But you can also be explicit:
cache_store = MemoryStore()

```

**Characteristics:**
  * ✅ No setup required
  * ✅ Very fast
  * ❌ Data lost on restart
  * ❌ Not suitable for multi-process deployments


###
[​](https://gofastmcp.com/servers/storage-backends#file-storage)
File Storage
**Best for:** Single-server production deployments, persistent caching File storage persists data to the filesystem as one JSON file per key, allowing it to survive server restarts. This is the default backend for OAuth storage on Mac and Windows.
Copy
```
from pathlib import Path
from key_value.aio.stores.filetree import (
    FileTreeStore,
    FileTreeV1KeySanitizationStrategy,
    FileTreeV1CollectionSanitizationStrategy,
)
from fastmcp.server.middleware.caching import ResponseCachingMiddleware

storage_dir = Path("/var/cache/fastmcp")
store = FileTreeStore(
    data_directory=storage_dir,
    key_sanitization_strategy=FileTreeV1KeySanitizationStrategy(storage_dir),
    collection_sanitization_strategy=FileTreeV1CollectionSanitizationStrategy(storage_dir),
)

# Persistent response cache
middleware = ResponseCachingMiddleware(cache_storage=store)

```

The sanitization strategies ensure keys and collection names are safe for the filesystem — alphanumeric names pass through as-is for readability, while special characters are hashed to prevent path traversal. **Characteristics:**
  * ✅ Data persists across restarts
  * ✅ No external dependencies
  * ✅ Human-readable files on disk
  * ❌ Not suitable for distributed deployments
  * ❌ Filesystem access required


###
[​](https://gofastmcp.com/servers/storage-backends#redis)
Redis
**Best for:** Distributed production deployments, shared caching across multiple servers
Redis support requires an optional dependency: `pip install 'py-key-value-aio[redis]'`
Redis provides distributed caching and state management, ideal for production deployments with multiple server instances.
Copy
```
from key_value.aio.stores.redis import RedisStore
from fastmcp.server.middleware.caching import ResponseCachingMiddleware

# Distributed response cache
middleware = ResponseCachingMiddleware(
    cache_storage=RedisStore(host="redis.example.com", port=6379)
)

```

With authentication:
Copy
```
from key_value.aio.stores.redis import RedisStore

cache_store = RedisStore(
    host="redis.example.com",
    port=6379,
    password="your-redis-password"
)

```

For OAuth token storage:
Copy
```
import os
from fastmcp.server.auth.providers.github import GitHubProvider
from key_value.aio.stores.redis import RedisStore

auth = GitHubProvider(
    client_id=os.environ["GITHUB_CLIENT_ID"],
    client_secret=os.environ["GITHUB_CLIENT_SECRET"],
    base_url="https://your-server.com",
    jwt_signing_key=os.environ["JWT_SIGNING_KEY"],
    client_storage=RedisStore(host="redis.example.com", port=6379)
)

```

**Characteristics:**
  * ✅ Distributed and highly available
  * ✅ Fast in-memory performance
  * ✅ Works across multiple server instances
  * ✅ Built-in TTL support
  * ❌ Requires Redis infrastructure
  * ❌ Network latency vs local storage


###
[​](https://gofastmcp.com/servers/storage-backends#other-backends-from-py-key-value-aio)
Other Backends from py-key-value-aio
The py-key-value-aio library includes additional implementations for various storage systems:
  * **DynamoDB** - AWS distributed database
  * **MongoDB** - NoSQL document store
  * **Elasticsearch** - Distributed search and analytics
  * **Memcached** - Distributed memory caching
  * **RocksDB** - Embedded high-performance key-value store
  * **Valkey** - Redis-compatible server

For configuration details on these backends, consult the
Before using these backends in production, review the
##
[​](https://gofastmcp.com/servers/storage-backends#use-cases-in-fastmcp)
Use Cases in FastMCP
###
[​](https://gofastmcp.com/servers/storage-backends#server-side-oauth-token-storage)
Server-Side OAuth Token Storage
The [OAuth Proxy](https://gofastmcp.com/servers/auth/oauth-proxy) and OAuth auth providers use storage for persisting OAuth client registrations and upstream tokens. **By default, storage is automatically encrypted using`FernetEncryptionWrapper`.** When providing custom storage, wrap it in `FernetEncryptionWrapper` to encrypt sensitive OAuth tokens at rest. **Development (default behavior):** By default, FastMCP automatically manages keys and storage based on your platform:
  * **Mac/Windows** : Keys are auto-managed via system keyring, storage defaults to disk. Suitable **only** for development and local testing.
  * **Linux** : Keys are ephemeral, storage defaults to memory.

No configuration needed:
Copy
```
from fastmcp.server.auth.providers.github import GitHubProvider

auth = GitHubProvider(
    client_id="your-id",
    client_secret="your-secret",
    base_url="https://your-server.com"
)

```

**Production:** For production deployments, configure explicit keys and persistent network-accessible storage with encryption:
Copy
```
import os
from fastmcp.server.auth.providers.github import GitHubProvider
from key_value.aio.stores.redis import RedisStore
from key_value.aio.wrappers.encryption import FernetEncryptionWrapper
from cryptography.fernet import Fernet

auth = GitHubProvider(
    client_id=os.environ["GITHUB_CLIENT_ID"],
    client_secret=os.environ["GITHUB_CLIENT_SECRET"],
    base_url="https://your-server.com",
    # Explicit JWT signing key (required for production)
    jwt_signing_key=os.environ["JWT_SIGNING_KEY"],
    # Encrypted persistent storage (required for production)
    client_storage=FernetEncryptionWrapper(
        key_value=RedisStore(host="redis.example.com", port=6379),
        fernet=Fernet(os.environ["STORAGE_ENCRYPTION_KEY"])
    )
)

```

Both parameters are required for production. **Wrap your storage in`FernetEncryptionWrapper` to encrypt sensitive OAuth tokens at rest** - without it, tokens are stored in plaintext. See [OAuth Token Security](https://gofastmcp.com/deployment/http#oauth-token-security) and [Key and Storage Management](https://gofastmcp.com/servers/auth/oauth-proxy#key-and-storage-management) for complete setup details.
###
[​](https://gofastmcp.com/servers/storage-backends#response-caching-middleware)
Response Caching Middleware
The [Response Caching Middleware](https://gofastmcp.com/servers/middleware#caching-middleware) caches tool calls, resource reads, and prompt requests. Storage configuration is passed via the `cache_storage` parameter:
Copy
```
from pathlib import Path
from fastmcp import FastMCP
from fastmcp.server.middleware.caching import ResponseCachingMiddleware
from key_value.aio.stores.filetree import (
    FileTreeStore,
    FileTreeV1KeySanitizationStrategy,
    FileTreeV1CollectionSanitizationStrategy,
)

mcp = FastMCP("My Server")

cache_dir = Path("cache")
cache_store = FileTreeStore(
    data_directory=cache_dir,
    key_sanitization_strategy=FileTreeV1KeySanitizationStrategy(cache_dir),
    collection_sanitization_strategy=FileTreeV1CollectionSanitizationStrategy(cache_dir),
)

# Cache to disk instead of memory
mcp.add_middleware(ResponseCachingMiddleware(cache_storage=cache_store))

```

For multi-server deployments sharing a Redis instance:
Copy
```
from fastmcp.server.middleware.caching import ResponseCachingMiddleware
from key_value.aio.stores.redis import RedisStore
from key_value.aio.wrappers.prefix_collections import PrefixCollectionsWrapper

base_store = RedisStore(host="redis.example.com")
namespaced_store = PrefixCollectionsWrapper(
    key_value=base_store,
    prefix="my-server"
)

middleware = ResponseCachingMiddleware(cache_storage=namespaced_store)

```

###
[​](https://gofastmcp.com/servers/storage-backends#client-side-oauth-token-storage)
Client-Side OAuth Token Storage
The [FastMCP Client](https://gofastmcp.com/clients/client) uses storage for persisting OAuth tokens locally. By default, tokens are stored in memory:
Copy
```
from pathlib import Path
from fastmcp.client.auth import OAuthClientProvider
from key_value.aio.stores.filetree import (
    FileTreeStore,
    FileTreeV1KeySanitizationStrategy,
    FileTreeV1CollectionSanitizationStrategy,
)

# Store tokens on disk for persistence across restarts
token_dir = Path("~/.local/share/fastmcp/tokens").expanduser()
token_storage = FileTreeStore(
    data_directory=token_dir,
    key_sanitization_strategy=FileTreeV1KeySanitizationStrategy(token_dir),
    collection_sanitization_strategy=FileTreeV1CollectionSanitizationStrategy(token_dir),
)

oauth_provider = OAuthClientProvider(
    mcp_url="https://your-mcp-server.com/mcp/sse",
    token_storage=token_storage
)

```

This allows clients to reconnect without re-authenticating after restarts.
##
[​](https://gofastmcp.com/servers/storage-backends#choosing-a-backend)
Choosing a Backend
Backend | Development | Single Server | Multi-Server | Cloud Native
---|---|---|---|---
Memory | ✅ Best | ⚠️ Limited | ❌ | ❌
File | ✅ Good | ✅ Recommended | ❌ | ⚠️
Redis | ⚠️ Overkill | ✅ Good | ✅ Best | ✅ Best
DynamoDB | ❌ | ⚠️ | ✅ | ✅ Best (AWS)
MongoDB | ❌ | ⚠️ | ✅ | ✅ Good
**Decision tree:**
  1. **Just starting?** Use **Memory** (default) - no configuration needed
  2. **Single server, needs persistence?** Use **File**
  3. **Multiple servers or cloud deployment?** Use **Redis** or **DynamoDB**
  4. **Existing infrastructure?** Look for a matching py-key-value-aio backend


##
[​](https://gofastmcp.com/servers/storage-backends#more-resources)
More Resources
  * [Response Caching Middleware](https://gofastmcp.com/servers/middleware#caching-middleware) - Using storage for caching
  * [OAuth Token Security](https://gofastmcp.com/deployment/http#oauth-token-security) - Production OAuth configuration
  * [HTTP Deployment](https://gofastmcp.com/deployment/http) - Complete deployment guide


[ Sampling Previous ](https://gofastmcp.com/servers/sampling)[ OpenTelemetry Next ](https://gofastmcp.com/servers/telemetry)
Ctrl+I
