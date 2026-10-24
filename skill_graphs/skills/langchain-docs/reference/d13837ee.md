    * Documents missing specified fields will still be stored but won't have embeddings for those fields
    * You can still override which fields to embed on a specific item at `put` time using the `index` parameter

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "dependencies": ["."],
      "graphs": {
        "memory_agent": "./agent/graph.py:graph"
      },
      "store": {
        "index": {
          "embed": "openai:text-embedding-3-small",
          "dims": 1536,
          "fields": ["$"]
        }
      }
    }
    ```

    <Note>
      **Common model dimensions**

      * `openai:text-embedding-3-large`: 3072
      * `openai:text-embedding-3-small`: 1536
      * `openai:text-embedding-ada-002`: 1536
      * `cohere:embed-english-v3.0`: 1024
      * `cohere:embed-english-light-v3.0`: 384
      * `cohere:embed-multilingual-v3.0`: 1024
      * `cohere:embed-multilingual-light-v3.0`: 384
    </Note>

    #### Semantic search with a custom embedding function

    If you want to use semantic search with a custom embedding function, you can pass a path to a custom embedding function:

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "dependencies": ["."],
      "graphs": {
        "memory_agent": "./agent/graph.py:graph"
      },
      "store": {
        "index": {
          "embed": "./embeddings.py:embed_texts",
          "dims": 768,
          "fields": ["text", "summary"]
        }
      }
    }
    ```

    The `embed` field in store configuration can reference a custom function that takes a list of strings and returns a list of embeddings. Example implementation:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # embeddings.py
    def embed_texts(texts: list[str]) -> list[list[float]]:
        """Custom embedding function for semantic search."""
        # Implementation using your preferred embedding model
        return [[0.1, 0.2, ...] for _ in texts]  # dims-dimensional vectors
    ```

    #### Adding custom authentication

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "$schema": "https://langgra.ph/schema.json",
      "dependencies": ["."],
      "graphs": {
        "chat": "chat.graph:graph"
      },
      "auth": {
        "path": "./auth.py:auth",
        "openapi": {
          "securitySchemes": {
            "apiKeyAuth": {
              "type": "apiKey",
              "in": "header",
              "name": "X-API-Key"
            }
          },
          "security": [{ "apiKeyAuth": [] }]
        },
        "disable_studio_auth": false
      }
    }
    ```

    See the [authentication conceptual guide](/langsmith/auth) for details, and the [setting up custom authentication](/langsmith/set-up-custom-auth) guide for a practical walk through of the process.

    <a />

    #### Configuring store item Time-to-Live

    You can configure default data expiration for items/memories in the BaseStore using the `store.ttl` key. This determines how long items are retained after they are last accessed (with reads potentially refreshing the timer based on `refresh_on_read`). Note that these defaults can be overwritten on a per-call basis by modifying the corresponding arguments in `get`, `search`, etc.

    The `ttl` configuration is an object containing optional fields:

    * `refresh_on_read`: If `true` (the default), accessing an item via `get` or `search` resets its expiration timer. Set to `false` to only refresh TTL on writes (`put`).
    * `default_ttl`: The default lifespan of an item in **minutes**. Applies only to newly created items; existing items are not modified. If not set, items do not expire by default.
    * `sweep_interval_minutes`: How frequently (in minutes) the system should run a background process to delete expired items. If not set, sweeping does not occur automatically.

    Here is an example enabling a 7-day TTL (10080 minutes), refreshing on reads, and sweeping every hour:

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "$schema": "https://langgra.ph/schema.json",
      "dependencies": ["."],
      "graphs": {
        "memory_agent": "./agent/graph.py:graph"
      },
      "store": {
        "ttl": {
          "refresh_on_read": true,
          "sweep_interval_minutes": 60,
          "default_ttl": 10080
        }
      }
    }
    ```

    <a />

    #### Configuring checkpoint Time-to-Live

    You can configure the time-to-live (TTL) for checkpoints using the `checkpointer` key. This determines how long checkpoint data is retained before being automatically handled according to the specified strategy (e.g., deletion). Two optional sub-objects are supported:

    * `ttl`: Includes `strategy`, `sweep_interval_minutes`, and `default_ttl`, which collectively set how checkpoints expire.
    * `serde` *(Agent server 0.5+)* : Lets you control deserialization behavior for checkpoint payloads.

    Here's an example setting a default TTL of 30 days (43200 minutes):

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "$schema": "https://langgra.ph/schema.json",
      "dependencies": ["."],
      "graphs": {
        "chat": "chat.graph:graph"
      },
      "checkpointer": {
        "ttl": {
          "strategy": "delete",
          "sweep_interval_minutes": 10,
          "default_ttl": 43200
        }
      }
    }
    ```

    In this example, checkpoints older than 30 days will be deleted, and the check runs every 10 minutes.

    #### Configuring checkpointer serde

    The `checkpointer.serde` object shapes deserialization:

    * `allowed_json_modules` defines an allow list for custom Python objects you want the server to be able to deserialize from payloads saved in "json" mode. This is a list of `[path, to, module, file, symbol]` sequences. If omitted, only LangChain-safe defaults are allowed. You can unsafely set to `true` to allow any module to be deserialized.
    * `pickle_fallback`: Whether to fall back to pickle deserialization when JSON decoding fails.

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "checkpointer": {
        "serde": {
          "allowed_json_modules": [
            ["my_agent", "auth", "SessionState"]
          ]
        }
      }
    }
    ```

    #### Customizing HTTP middleware and headers

    The `http` block lets you fine-tune request handling:

    * `middleware_order`: Choose `"auth_first"` to run authentication before your middleware, or `"middleware_first"` (default) to invert that order.
    * `enable_custom_route_auth`: Extend authentication to routes you mount through `http.app`.
    * `configurable_headers` / `logging_headers`: Each accepts an object with optional `includes` and `excludes` arrays; wildcards are supported and exclusions run before inclusions.
    * `cors`: Customize your server's CORS (Cross-Origin Resource Sharing) configuration. Example `langgraph.json` file for configuring CORS:

      ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      {
        ...
        "http": {
          "cors": {
            "allow_origins": ["https://example.com", "https://app.example.com"],
            "allow_methods": ["GET", "POST"],
            "allow_headers": ["Authorization", "Content-Type"],
            "allow_credentials": true,
            "allow_origin_regex": "^https://.*\\.example\\.com$",
            "expose_headers": ["x-pagination-total", "x-pagination-next", "x-request-id"],
            "max_age": 600
          }
        },
        ...
      }
      ```

      <Note>
        Customizing your server's CORS configuration will override the functionality of setting the [`CORS_ALLOW_ORIGINS` environment variable](/langsmith/env-var#cors_allow_origins).
      </Note>

    #### Configuring webhooks

    You can configure custom headers and URL restrictions for outbound webhook requests:

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "$schema": "https://langgra.ph/schema.json",
      "dependencies": ["."],
      "graphs": {
        "chat": "chat.graph:graph"
      },
      "webhooks": {
        "headers": {
          "Authorization": "Bearer ${{ env.LG_WEBHOOK_TOKEN }}"
        },
        "url": {
          "allowed_domains": ["*.mycompany.com"],
          "require_https": true
        }
      }
    }
    ```

    See [Use webhooks](/langsmith/use-webhooks#add-headers-to-webhook-requests) for details on header configuration, environment variable templating, and URL restrictions.

    <a />

    #### Pinning API version

    *(Added in v0.3.7)*

    You can pin the API version of the Agent Server by using the `api_version` key. This is useful if you want to ensure that your server uses a specific version of the API.
    By default, builds in Cloud deployments use the latest stable version of the server. This can be pinned by setting the `api_version` key to a specific version.

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "$schema": "https://langgra.ph/schema.json",
      "dependencies": ["."],
      "graphs": {
        "chat": "chat.graph:graph"
      },
      "api_version": "0.2"
    }
    ```

    #### Disabling built-in routes

    You can selectively disable groups of built-in HTTP routes using boolean flags in the `http` configuration block. This is useful for production deployments where you want to minimize the server's exposed surface area.

    For example, to disable the system information and documentation routes:

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "$schema": "https://langgra.ph/schema.json",
      "dependencies": ["."],
      "graphs": {
        "chat": "chat.graph:graph"
      },
      "http": {
        "disable_meta": true
      }
    }
    ```

    Setting `disable_meta` to `true` disables the following routes:

    * `/` — root health check
    * `/info` — server version and configuration info
    * `/metrics` — Prometheus and JSON metrics
    * `/docs` — API documentation UI
    * `/openapi.json` — OpenAPI specification

    The `/ok` health check endpoint remains available even when `disable_meta` is set, so orchestrators like Kubernetes can still perform liveness and readiness probes.

    Other route disable flags include `disable_assistants`, `disable_runs`, `disable_threads`, `disable_store`, and `disable_ui`. For MCP, A2A, and webhooks, see their respective guides: [Disable MCP](/langsmith/server-mcp#disable-mcp), [Disable A2A](/langsmith/server-a2a#disable-a2a), [Disable webhooks](/langsmith/use-webhooks#disable-webhooks).
  </Tab>

  <Tab title="JS">
    #### Basic configuration

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "$schema": "https://langgra.ph/schema.json",
      "graphs": {
        "chat": "./src/graph.ts:graph"
      }
    }
    ```

    <a />

    #### Pinning API version

    *(Added in v0.3.7)*

    You can pin the API version of the Agent Server by using the `api_version` key. This is useful if you want to ensure that your server uses a specific version of the API.
    By default, builds in Cloud deployments use the latest stable version of the server. This can be pinned by setting the `api_version` key to a specific version.

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "$schema": "https://langgra.ph/schema.json",
      "dependencies": ["."],
      "graphs": {
        "chat": "./src/chat/graph.ts:graph"
      },
      "api_version": "0.2"
    }
    ```

    #### Disabling built-in routes

    You can selectively disable groups of built-in HTTP routes using boolean flags in the `http` configuration block. This is useful for production deployments where you want to minimize the server's exposed surface area.

    For example, to disable the system information and documentation routes:

    ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
      "$schema": "https://langgra.ph/schema.json",
      "graphs": {
        "chat": "./src/chat/graph.ts:graph"
      },
      "http": {
        "disable_meta": true
      }
    }
    ```

    Setting `disable_meta` to `true` disables the following routes:

    * `/` — root health check
    * `/info` — server version and configuration info
    * `/metrics` — Prometheus and JSON metrics
    * `/docs` — API documentation UI
    * `/openapi.json` — OpenAPI specification

    The `/ok` health check endpoint remains available even when `disable_meta` is set, so orchestrators like Kubernetes can still perform liveness and readiness probes.

    Other route disable flags include `disable_assistants`, `disable_runs`, `disable_threads`, `disable_store`, and `disable_ui`. For MCP, A2A, and webhooks, see their respective guides: [Disable MCP](/langsmith/server-mcp#disable-mcp), [Disable A2A](/langsmith/server-a2a#disable-a2a), [Disable webhooks](/langsmith/use-webhooks#disable-webhooks).
  </Tab>
</Tabs>

## Commands

**Usage**

<Tabs>
  <Tab title="Python">
    The base command for the LangGraph CLI is `langgraph`.

    ```
    langgraph [OPTIONS] COMMAND [ARGS]
    ```
  </Tab>

  <Tab title="JS">
    The base command for the LangGraph.js CLI is `langgraphjs`.

    ```
    npx @langchain/langgraph-cli [OPTIONS] COMMAND [ARGS]
    ```

    We recommend using `npx` to always use the latest version of the CLI.
  </Tab>
</Tabs>

### `dev`

<Tabs>
  <Tab title="Python">
    Run LangGraph API server in development mode with hot reloading and debugging capabilities. This lightweight server requires no Docker installation and is suitable for development and testing. State is persisted to a local directory.

    <Note>Currently, the CLI only supports Python >= 3.11.</Note>

    <Tip>
      If you need more information on when to use `langgraph dev` vs `langgraph up`, refer to the [Local development & testing guide](/langsmith/local-dev-testing) for a detailed comparison.
    </Tip>

    **Installation**

    This command requires the "inmem" extra to be installed:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install -U "langgraph-cli[inmem]"
    ```

    **Usage**

    ```
    langgraph dev [OPTIONS]
    ```

    **Options**

    | Option                        | Default          | Description                                                                                                                                                                  |
    | ----------------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `-c, --config FILE`           | `langgraph.json` | Path to configuration file declaring dependencies, graphs and environment variables                                                                                          |
    | `--host TEXT`                 | `127.0.0.1`      | Host to bind the server to                                                                                                                                                   |
    | `--port INTEGER`              | `2024`           | Port to bind the server to                                                                                                                                                   |
    | `--no-reload`                 |                  | Disable auto-reload                                                                                                                                                          |
    | `--n-jobs-per-worker INTEGER` |                  | Number of jobs per worker. Default is 10                                                                                                                                     |
    | `--debug-port INTEGER`        |                  | Port for debugger to listen on                                                                                                                                               |
    | `--wait-for-client`           | `False`          | Wait for a debugger client to connect to the debug port before starting the server                                                                                           |
    | `--no-browser`                |                  | Skip automatically opening the browser when the server starts                                                                                                                |
    | `--studio-url TEXT`           |                  | URL of the Studio instance to connect to. Defaults to [https://smith.langchain.com](https://smith.langchain.com)                                                             |
    | `--allow-blocking`            | `False`          | Do not raise errors for synchronous I/O blocking operations in your code (added in `0.2.6`)                                                                                  |
    | `--tunnel`                    | `False`          | Expose the local server via a public tunnel (Cloudflare) for remote frontend access. This avoids issues with browsers like Safari or networks blocking localhost connections |
    | `--help`                      |                  | Display command documentation                                                                                                                                                |
  </Tab>

  <Tab title="JS">
    Run LangGraph API server in development mode with hot reloading capabilities. This lightweight server requires no Docker installation and is suitable for development and testing. State is persisted to a local directory.

    **Usage**

    ```
    npx @langchain/langgraph-cli dev [OPTIONS]
    ```

    **Options**

    | Option                        | Default          | Description                                                                                                                                                      |
    | ----------------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `-c, --config FILE`           | `langgraph.json` | Path to configuration file declaring dependencies, graphs and environment variables                                                                              |
    | `--host TEXT`                 | `127.0.0.1`      | Host to bind the server to                                                                                                                                       |
    | `--port INTEGER`              | `2024`           | Port to bind the server to                                                                                                                                       |
    | `--no-reload`                 |                  | Disable auto-reload                                                                                                                                              |
    | `--n-jobs-per-worker INTEGER` |                  | Number of jobs per worker. Default is 10                                                                                                                         |
    | `--debug-port INTEGER`        |                  | Port for debugger to listen on                                                                                                                                   |
    | `--wait-for-client`           | `False`          | Wait for a debugger client to connect to the debug port before starting the server                                                                               |
    | `--no-browser`                |                  | Skip automatically opening the browser when the server starts                                                                                                    |
    | `--studio-url TEXT`           |                  | URL of the Studio instance to connect to. Defaults to [https://smith.langchain.com](https://smith.langchain.com)                                                 |
    | `--allow-blocking`            | `False`          | Do not raise errors for synchronous I/O blocking operations in your code                                                                                         |
    | `--tunnel`                    | `False`          | Expose the local server via a public tunnel (Cloudflare) for remote frontend access. This avoids issues with browsers or networks blocking localhost connections |
    | `--help`                      |                  | Display command documentation                                                                                                                                    |
  </Tab>
</Tabs>

### `build`

<Tabs>
  <Tab title="Python">
    Build LangSmith API server Docker image.

    **Usage**

    ```
    langgraph build [OPTIONS]
    ```

    **Options**

    | Option                                | Default          | Description                                                                                                                                             |
    | ------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `--platform TEXT`                     |                  | Target platform(s) to build the Docker image for. Example: `langgraph build --platform linux/amd64,linux/arm64`                                         |
    | `-t, --tag TEXT`                      |                  | **Required**. Tag for the Docker image. Example: `langgraph build -t my-image`                                                                          |
    | `--pull / --no-pull`                  | `--pull`         | Build with latest remote Docker image. Use `--no-pull` for running the LangSmith API server with locally built images.                                  |
    | `-c, --config FILE`                   | `langgraph.json` | Path to configuration file declaring dependencies, graphs and environment variables.                                                                    |
    | `--build-command TEXT`<sup>\*</sup>   |                  | Build command to run. Runs from the directory where your `langgraph.json` file lives. Example: `langgraph build --build-command "yarn run turbo build"` |
    | `--install-command TEXT`<sup>\*</sup> |                  | Install command to run. Runs from the directory where you call `langgraph build` from. Example: `langgraph build --install-command "yarn install"`      |
    | `--help`                              |                  | Display command documentation.                                                                                                                          |

    <sup>\*</sup>Only supported for JS deployments, will have no impact on Python deployments.
  </Tab>

  <Tab title="JS">
    Build LangSmith API server Docker image.

    **Usage**

    ```
    npx @langchain/langgraph-cli build [OPTIONS]
    ```

    **Options**

    | Option              | Default          | Description                                                                                                     |
    | ------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------- |
    | `--platform TEXT`   |                  | Target platform(s) to build the Docker image for. Example: `langgraph build --platform linux/amd64,linux/arm64` |
    | `-t, --tag TEXT`    |                  | **Required**. Tag for the Docker image. Example: `langgraph build -t my-image`                                  |
    | `--no-pull`         |                  | Use locally built images. Defaults to `false` to build with latest remote Docker image.                         |
    | `-c, --config FILE` | `langgraph.json` | Path to configuration file declaring dependencies, graphs and environment variables.                            |
    | `--help`            |                  | Display command documentation.                                                                                  |
  </Tab>
</Tabs>

### `deploy`

<Tabs>
  <Tab title="Python">
    <Note>This command is in beta and under active development. Expect frequent updates and improvements.</Note>

    Build and deploy a LangGraph image directly to [LangSmith Deployments](/langsmith/deployment). This command builds a Docker image locally, pushes it to a managed registry, and creates or updates a deployment—all in a single step. If Docker is not installed, it triggers a remote build.

    **Prerequisites**

    * A [**LangSmith API key**](/langsmith/create-account-api-key) with access to Deployments.
    * (Optional) **Docker** must be installed and the Docker daemon must be running for local builds. Not required for remote builds. [Install Docker Desktop](https://docs.docker.com/get-docker/).

    <Note>Works only with LangSmith Cloud.</Note>
