# Set a sampling rate for traces
Source: https://docs.langchain.com/langsmith/sample-traces

When working with high-volume applications, you may not want to log every trace to LangSmith. Sampling rates allow you to control what percentage of traces are logged, helping you balance observability needs with cost considerations.

This guide shows you how to set a global sampling rate with the `LANGSMITH_TRACING_SAMPLING_RATE` environment variable, and how to apply different sampling rates per `Client` instance for finer-grained control over which operations are traced.

<Tip>
  To enable or disable tracing for specific requests based on runtime conditions (such as data sensitivity, tenant, or feature flag), refer to [Conditional tracing](/langsmith/conditional-tracing).
</Tip>

## Set a global sampling rate

<Note>
  This section is relevant for those using the [LangSmith SDK](/langsmith/reference) or [LangChain](/oss/python/langchain/overview), not for those logging directly with the LangSmith API.
</Note>

By default, all traces are logged to LangSmith. To down-sample the number of traces logged to LangSmith, set the `LANGSMITH_TRACING_SAMPLING_RATE` environment variable to any float between `0` (no traces) and `1` (all traces). For instance, setting the following environment variable will log 75% of the traces.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_TRACING_SAMPLING_RATE=0.75
```

This works for the `traceable` decorator and `RunTree` objects.

## Set different sampling rates per client

You can also set sampling rates on specific `Client` instances and use the [`tracing_context`](/langsmith/annotate-code#use-the-trace-context-manager-python-only) context manager:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import Client, tracing_context

# Create clients with different sampling rates
client_1 = Client(tracing_sampling_rate=0.5)  # 50% sampling
client_2 = Client(tracing_sampling_rate=0.25)  # 25% sampling
client_no_trace = Client(tracing_sampling_rate=0.0)  # No tracing

# Use different sampling rates for different operations
with tracing_context(client=client_1):
    # Your code here - will be traced with 50% sampling rate
    agent_1.invoke(...)

with tracing_context(client=client_2):
    # Your code here - will be traced with 25% sampling rate
    agent_1.invoke(...)

with tracing_context(client=client_no_trace):
    # Your code here - will not be traced
    agent_1.invoke(...)
```

This allows you to control sampling rates at the operation level.

## Sampling or conditional tracing

Sampling provides **probabilistic** control over trace volume, while [conditional tracing](/langsmith/conditional-tracing) provides **deterministic** control based on business logic.

Use **sampling** when you want to reduce overall trace volume while maintaining statistical representation of your application's behavior.

Use [conditional tracing](/langsmith/conditional-tracing) when you need guaranteed tracing behavior for specific requests, such as:

* Disabling tracing for clients with zero-retention policies.
* Routing traces to different projects based on tenant.
* Handling sensitive data that should never be traced.

You can combine both approaches for fine-grained control over your observability strategy.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/sample-traces.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Sandbox auth proxy
Source: https://docs.langchain.com/langsmith/sandbox-auth-proxy

Inject credentials into outbound requests and control which destinations a sandbox can reach.

The auth proxy lets sandbox code call external APIs (OpenAI, Anthropic, GitHub, etc.) without hardcoding credentials. When configured on a sandbox, a proxy sidecar automatically injects authentication headers into matching outbound requests using your workspace secrets or write-only credentials you provide in the proxy config.

<Warning>
  You must configure your secrets (e.g., `OPENAI_API_KEY`) in your LangSmith [workspace](/langsmith/administration-overview#workspaces) settings before creating a sandbox that references them.
</Warning>

## Egress and network access control

The same `proxy_config` that injects credentials also controls which destinations a sandbox can reach.

### Default egress posture

By default (no `access_control` configured):

* **HTTP and HTTPS (ports 80 and 443) to any host are allowed.** Outbound HTTP(S) is transparently routed through the proxy, where your `rules` and `callbacks` inject credentials.
* **All other raw TCP is blocked.** Connections to non-HTTP ports—databases (`psql`/`dbt` on 5432), SSH (22), Redis (6379), and so on—are dropped unless you explicitly allow them.

This means raw protocols are not blocked because the proxy "can't speak" them—they are blocked by default and opened per host and port via `access_control`.

### Allow and deny lists

Add an `access_control` object to `proxy_config` with **either** an `allow_list` **or** a `deny_list` (not both—the request is rejected if both are set):

| Mode         | Behavior                                                                                                                                                            |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `allow_list` | **Default-deny.** Only listed destinations are reachable—including HTTP/HTTPS. If you set an `allow_list`, you must also list every HTTP(S) host the sandbox needs. |
| `deny_list`  | **Default-allow for HTTP/HTTPS.** All HTTP(S) hosts remain reachable except those listed. A `deny_list` cannot open raw TCP ports.                                  |

<Note>
  Raw TCP egress (e.g. PostgreSQL on 5432) can **only** be enabled with an `allow_list` entry that specifies an explicit non-HTTP port (`host:PORT`). The default posture and `deny_list` mode only ever permit HTTP/HTTPS.
</Note>

### Pattern syntax

Each `allow_list`/`deny_list` entry uses the following forms:

| Pattern                  | Meaning                                                                                                          |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| `host`                   | Bare host → ports **80 and 443 only** (HTTP/S).                                                                  |
| `host:PORT`              | Host on exactly `PORT`. `:22` grants only 22, **not** additive with 80/443—list the host twice if you need both. |
| `*.example.com`          | Glob (RFC 1034-style). The apex (`example.com`) is **not** included.                                             |
| `~regex`                 | Opaque regex match; no port suffix parsing.                                                                      |
| `1.2.3.4` / `10.0.0.0/8` | Literal IP or CIDR. CIDRs **cannot** carry a port (HTTP/S only in allow mode; block all ports in deny mode).     |
| `[::1]:22`               | IPv6 literal uses the bracketed form when specifying a port.                                                     |

### Connecting to a database (raw TCP)

To let sandbox code reach an external PostgreSQL database with `psql`, `dbt`, or any driver, allow-list the host on its port. Because `allow_list` is default-deny, also list any HTTP(S) hosts the sandbox needs:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl -X POST "$LANGSMITH_ENDPOINT/v2/sandboxes/boxes" \
  -H "x-api-key: $LANGSMITH_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "db-sandbox",
    "wait_for_ready": true,
    "proxy_config": {
      "access_control": {
        "allow_list": [
          "db.example.com:5432",
          "api.openai.com"
        ]
      }
    }
  }'
```

The connection to `db.example.com:5432` is passed through at the TCP layer with no interception, so the PostgreSQL wire protocol—and TLS, host-key checking, and any other end-to-end protocol on top of it—works unchanged.

### Configure via SDK

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith.sandbox import SandboxClient

  client = SandboxClient()

  client.create_sandbox(
      name="db-sandbox",
      proxy_config={
          "access_control": {
              "allow_list": ["db.example.com:5432", "api.openai.com"]
          }
      },
  )
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { SandboxClient } from "langsmith/sandbox";

  const client = new SandboxClient();

  await client.createSandbox({
    name: "db-sandbox",
    proxyConfig: {
      access_control: {
        allow_list: ["db.example.com:5432", "api.openai.com"],
      },
    },
  });
  ```
</CodeGroup>

## Configure auth proxy rules

Add a `proxy_config` when creating a sandbox, or update an existing sandbox by patching its `proxy_config`. Each rule specifies:

| Field         | Description                                                |
| ------------- | ---------------------------------------------------------- |
| `match_hosts` | Hosts to intercept (supports globs like `*.github.com`)    |
| `match_paths` | Paths to match (empty = all paths)                         |
| `headers`     | Headers to inject, each with a `name`, `type`, and `value` |
| `no_proxy`    | Hosts to bypass the proxy entirely (e.g. `localhost`)      |

### Header types

Each header has a `type` that controls how its value is stored and displayed:

| Type               | Description                                                                                           |
| ------------------ | ----------------------------------------------------------------------------------------------------- |
| `workspace_secret` | References a workspace secret using `{KEY}` syntax. Resolved when the proxy configuration is applied. |
| `plaintext`        | Value is stored and returned as-is. Use for non-sensitive headers.                                    |
| `opaque`           | Write-only. Value is encrypted at rest and never returned via the API.                                |

## Authenticate AWS requests

Use an AWS auth rule when sandbox code needs to call AWS services with an AWS SDK or CLI. The proxy keeps the real AWS credentials outside the sandbox, then signs supported outbound HTTPS requests with AWS SigV4.

This is useful when agent code needs to inspect S3 objects, call Bedrock, or use another supported AWS HTTPS endpoint without exposing long-lived AWS access keys in sandbox files, environment variables, shell history, or logs. The sandbox receives compatibility AWS credential placeholders so SDK credential detection works, while the proxy signs the outbound request with the configured credentials.

<Warning>
  Do not set real AWS access keys as sandbox environment variables. Configure them as `workspace_secret` or `opaque` proxy values. Plaintext AWS credential values are rejected.
</Warning>

AWS auth rules are different from header injection rules:

* Set `type` to `aws`.
* Put credentials under the `aws` object.
* Do not set `match_hosts`, `match_paths`, or `headers`; AWS host matching is built into the proxy.
* Configure at most one AWS auth rule per sandbox.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl -X POST "$LANGSMITH_ENDPOINT/v2/sandboxes/boxes" \
  -H "x-api-key: $LANGSMITH_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "aws-sandbox",
    "wait_for_ready": true,
    "proxy_config": {
      "rules": [
        {
          "name": "aws",
          "type": "aws",
          "enabled": true,
          "aws": {
            "access_key_id": {
              "type": "workspace_secret",
              "value": "{AWS_ACCESS_KEY_ID}"
            },
            "secret_access_key": {
              "type": "workspace_secret",
              "value": "{AWS_SECRET_ACCESS_KEY}"
            }
          }
        }
      ]
    }
  }'
```

### Configure AWS auth via SDK

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith.sandbox import (
      SandboxClient,
      aws_auth_proxy_config,
      workspace_secret,
  )

  client = SandboxClient()

  client.create_sandbox(
      name="aws-sandbox",
      proxy_config=aws_auth_proxy_config(
          access_key_id=workspace_secret("AWS_ACCESS_KEY_ID"),
          secret_access_key=workspace_secret("AWS_SECRET_ACCESS_KEY"),
      ),
  )
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import {
    SandboxClient,
    awsAuthProxyConfig,
    workspaceSecret,
  } from "langsmith/sandbox";

  const client = new SandboxClient();

  await client.createSandbox({
    name: "aws-sandbox",
    proxyConfig: awsAuthProxyConfig({
      accessKeyId: workspaceSecret("AWS_ACCESS_KEY_ID"),
      secretAccessKey: workspaceSecret("AWS_SECRET_ACCESS_KEY"),
    }),
  });
  ```
</CodeGroup>

After the sandbox is ready, use AWS SDKs or CLIs normally inside the sandbox. The SDK or CLI can discover the placeholder AWS environment variables, and the proxy applies the real SigV4 signature to outbound AWS requests.

<Note>
  AWS auth proxy rules currently support access key ID and secret access key credentials. They do not include a session token or assume-role configuration.
</Note>

## Single API example

Create a sandbox that automatically injects an OpenAI API key into outbound requests:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl -X POST "$LANGSMITH_ENDPOINT/v2/sandboxes/boxes" \
  -H "x-api-key: $LANGSMITH_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "openai-sandbox",
    "wait_for_ready": true,
    "proxy_config": {
      "rules": [
        {
          "name": "openai-api",
          "match_hosts": ["api.openai.com"],
          "headers": [
            {
              "name": "Authorization",
              "type": "workspace_secret",
              "value": "Bearer {OPENAI_API_KEY}"
            }
          ]
        }
      ]
    }
  }'
```

The sandbox can now call OpenAI with no API key setup—the proxy injects it automatically.

## Multiple API example

Add multiple rules to authenticate with several services at once:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl -X POST "$LANGSMITH_ENDPOINT/v2/sandboxes/boxes" \
  -H "x-api-key: $LANGSMITH_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "multi-api-sandbox",
    "wait_for_ready": true,
    "proxy_config": {
      "rules": [
        {
          "name": "openai-api",
          "match_hosts": ["api.openai.com"],
          "headers": [
            {
              "name": "Authorization",
              "type": "workspace_secret",
              "value": "Bearer {OPENAI_API_KEY}"
            }
          ]
        },
        {
          "name": "anthropic-api",
          "match_hosts": ["api.anthropic.com"],
          "headers": [
            {
              "name": "x-api-key",
              "type": "workspace_secret",
              "value": "{ANTHROPIC_API_KEY}"
            },
            {
              "name": "anthropic-version",
              "type": "plaintext",
              "value": "2023-06-01"
            }
          ]
        },
        {
          "name": "github-api",
          "match_hosts": ["api.github.com"],
          "match_paths": ["/repos/*", "/user"],
          "headers": [
            {
              "name": "Authorization",
              "type": "workspace_secret",
              "value": "Bearer {GITHUB_TOKEN}"
            }
          ]
        }
      ],
      "no_proxy": ["localhost", "127.0.0.1"]
    }
  }'
```

## GitHub example

[Open SWE](https://github.com/langchain-ai/open-swe/blob/main/agent/integrations/langsmith.py) authenticates GitHub access by minting a short-lived GitHub App installation token outside the sandbox, then patching the sandbox with write-only `opaque` proxy rules. This keeps the short-lived GitHub access token out of the sandbox filesystem and out of deployment environment variables.

Configure two rules:

| Host                         | Header                                                                                                                     |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `api.github.com`             | `Authorization: Bearer <github-token>` for `gh` and REST API calls                                                         |
| `github.com`, `*.github.com` | `Authorization: Basic <base64("x-access-token:<github-token>")>` for Git over HTTPS operations like clone, fetch, and push |

```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import base64
import os
from typing import Any

import httpx

def github_proxy_rules(github_token: str) -> list[dict[str, Any]]:
    basic_auth = base64.b64encode(
        f"x-access-token:{github_token}".encode()
    ).decode()

    return [
        {
            "name": "github-api",
            "match_hosts": ["api.github.com"],
            "headers": [
                {
                    "name": "Authorization",
                    "type": "opaque",
                    "value": f"Bearer {github_token}",
                }
            ],
        },
        {
            "name": "github",
            "match_hosts": ["github.com", "*.github.com"],
            "headers": [
                {
                    "name": "Authorization",
                    "type": "opaque",
                    "value": f"Basic {basic_auth}",
                }
            ],
        },
    ]

def configure_github_proxy(sandbox_name: str, github_token: str) -> None:
    endpoint = os.environ.get(
        "LANGSMITH_ENDPOINT", "https://api.smith.langchain.com"
    )
    response = httpx.patch(
        f"{endpoint}/v2/sandboxes/boxes/{sandbox_name}",
        headers={"x-api-key": os.environ["LANGSMITH_API_KEY"]},
        json={"proxy_config": {"rules": github_proxy_rules(github_token)}},
        timeout=30.0,
    )
    response.raise_for_status()
```

Call `configure_github_proxy` after creating or reattaching to a sandbox. GitHub App installation tokens expire, so refresh the proxy config whenever you reuse a sandbox for a new run.

Inside the sandbox, set a non-secret placeholder token when a CLI requires a local credential before it sends a request:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
GH_TOKEN=dummy gh repo view langchain-ai/langchain
GH_TOKEN=dummy gh pr list --repo langchain-ai/langchain
GH_TOKEN=dummy gh repo clone langchain-ai/langchain
```

The placeholder only satisfies the `gh` CLI's local check. The proxy injects the real `Authorization` header into the outbound request.

## Configure via SDK

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith.sandbox import SandboxClient

  client = SandboxClient()

  client.create_sandbox(
      name="openai-sandbox",
      proxy_config={
          "rules": [
              {
                  "name": "openai-api",
                  "match_hosts": ["api.openai.com"],
                  "headers": [
                      {
                          "name": "Authorization",
                          "type": "workspace_secret",
                          "value": "Bearer {OPENAI_API_KEY}",
                      }
                  ],
              }
          ]
      },
  )
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { SandboxClient } from "langsmith/sandbox";

  const client = new SandboxClient();

  await client.createSandbox({
    name: "openai-sandbox",
    proxyConfig: {
      rules: [
        {
          name: "openai-api",
          match_hosts: ["api.openai.com"],
          headers: [
            {
              name: "Authorization",
              type: "workspace_secret",
              value: "Bearer {OPENAI_API_KEY}",
            },
          ],
        },
      ],
    },
  });
  ```
</CodeGroup>

## Callback credential example

Static `workspace_secret` rules pull credentials from your workspace when the proxy configuration is applied, and `opaque` rules let your application patch in short-lived credentials such as the [GitHub token example](#github-example). For credentials that must be resolved by your own service at proxy time, use a **callback**. The proxy POSTs to a URL you provide, your endpoint returns the headers to inject, and the proxy caches the result.

Callbacks are configured alongside rules under `proxy_config`:

| Field             | Description                                                                                                                                                                                           |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `match_hosts`     | Hosts to intercept (same syntax as rules; supports globs like `*.github.com`).                                                                                                                        |
| `url`             | Your callback endpoint. Must be an `http://` or `https://` URL reachable from the proxy.                                                                                                              |
| `request_headers` | Headers attached to the proxy → callback request, e.g., an HMAC or shared secret your endpoint uses to verify the request. Only `plaintext` and `opaque` types are permitted (no `workspace_secret`). |
| `ttl_seconds`     | How long resolved headers are cached before re-invoking the callback. Must be between 60 and 3600.                                                                                                    |

**Static rules win.** If any rule in `rules` matches the host, the callback is skipped for that host. Within rules, first-match-wins; the same applies between callbacks if multiple match.

### Callback contract

The proxy makes the following request whenever it needs to resolve credentials for a matched host on a cache miss:

```
POST <callback.url>
Content-Type: application/json
<request_headers from your config, attached verbatim>

{"host": "api.example.com", "port": 443}
```

Your endpoint must respond `2xx` with a JSON body:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "headers": {
    "Authorization": "Bearer <token>",
    "X-Org-Id": "..."
  }
}
```

The proxy injects every header in the response into the sandbox's outbound request and caches the response for `ttl_seconds`. Any non-2xx response, transport error, or malformed JSON fails closed: the sandbox's request is rejected with `502 callback resolution failed` (no headers injected, response not cached).

### Example

Use a callback when your OAuth tokens are minted on demand by your own service:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl -X POST "$LANGSMITH_ENDPOINT/v2/sandboxes/boxes" \
  -H "x-api-key: $LANGSMITH_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "snapshot_id": "<snapshot-uuid>",
    "name": "callback-sandbox",
    "wait_for_ready": true,
    "proxy_config": {
      "callbacks": [
        {
          "match_hosts": ["api.github.com", "*.githubusercontent.com"],
          "url": "https://auth.your-app.example.com/sandbox-credentials",
          "request_headers": [
            {
              "name": "X-Integrator-Secret",
              "type": "opaque",
              "value": "<shared-secret-your-endpoint-verifies>"
            }
          ],
          "ttl_seconds": 300
        }
      ]
    }
  }'
```

### Configure via SDK

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith.sandbox import SandboxClient

  client = SandboxClient()

  client.create_sandbox(
      name="callback-sandbox",
      proxy_config={
          "callbacks": [
              {
                  "match_hosts": ["api.github.com", "*.githubusercontent.com"],
                  "url": "https://auth.your-app.example.com/sandbox-credentials",
                  "request_headers": [
                      {
                          "name": "X-Integrator-Secret",
                          "type": "opaque",
                          "value": "<shared-secret-your-endpoint-verifies>",
                      }
                  ],
                  "ttl_seconds": 300,
              }
          ]
      },
  )
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { SandboxClient } from "langsmith/sandbox";

  const client = new SandboxClient();

  await client.createSandbox({
    name: "callback-sandbox",
    proxyConfig: {
      callbacks: [
        {
          match_hosts: ["api.github.com", "*.githubusercontent.com"],
          url: "https://auth.your-app.example.com/sandbox-credentials",
          request_headers: [
            {
              name: "X-Integrator-Secret",
              type: "opaque",
              value: "<shared-secret-your-endpoint-verifies>",
            },
          ],
          ttl_seconds: 300,
        },
      ],
    },
  });
  ```
</CodeGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/sandbox-auth-proxy.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Sandbox CLI
Source: https://docs.langchain.com/langsmith/sandbox-cli

Create, inspect, connect to, and tunnel into LangSmith sandboxes from the command line.

The [LangSmith CLI](/langsmith/langsmith-cli) includes sandbox commands for creating snapshots, booting sandboxes, running commands, opening interactive shells, and tunneling TCP connections into a sandbox.

Sandbox CLI commands require LangSmith CLI `v0.2.26` or later.

## Install and authenticate

Install or upgrade the LangSmith CLI:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl -fsSL https://cli.langsmith.com/install.sh | sh
langsmith self-update
```

Authenticate the CLI with your LangSmith API key:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_API_KEY="<LANGSMITH_API_KEY>"
```

CLI output is JSON by default. Add `--format pretty` to list commands for human-readable tables:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith --format pretty sandbox list
```

## End-to-end workflow

Create a sandbox, then run commands inside it:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith sandbox create my-vm \
  --vcpus 2 \
  --memory 1gb \
  --wait

langsmith sandbox exec my-vm -- python --version
```

When you are done with a sandbox, delete it:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith sandbox delete my-vm
```

## Manage snapshots

Build snapshots from Docker images:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith sandbox snapshot build my-snapshot \
  --docker-image ubuntu:24.04 \
  --capacity 8gb \
  --wait
```

For private registries, pass registry credentials from environment variables:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith sandbox snapshot build internal-python \
  --docker-image registry.example.com/internal/python:3.12 \
  --registry-url https://registry.example.com \
  --registry-username "$REGISTRY_USERNAME" \
  --registry-password "$REGISTRY_PASSWORD" \
  --wait
```

Capture the filesystem from a running sandbox:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith sandbox snapshot capture ml-ready \
  --box my-vm \
  --wait
```

List, inspect, wait for, and delete snapshots:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith sandbox snapshot list
langsmith sandbox snapshot get <SNAPSHOT_ID>
langsmith sandbox snapshot wait <SNAPSHOT_ID>
langsmith sandbox snapshot delete <SNAPSHOT_ID>
```

## Manage sandboxes

Create a sandbox with the default runtime. Add `--snapshot-id` only when you want to boot from a reusable custom snapshot:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith sandbox create my-vm \
  --vcpus 4 \
  --memory 1gb \
  --rootfs-capacity 8gb \
  --wait
```

List and inspect sandboxes:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith sandbox list
langsmith sandbox get my-vm
langsmith sandbox wait my-vm
```

Stop and start a sandbox while preserving its filesystem:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith sandbox stop my-vm
langsmith sandbox start my-vm --wait
```

Update resources or proxy configuration:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith sandbox update my-vm --vcpus 8 --memory 2gb
langsmith sandbox update my-vm --proxy-config @proxy.json
```

Resource changes take effect the next time the sandbox starts. Proxy configuration changes take effect immediately.

### Proxy configuration

Use `--proxy-config @proxy.json` on `create` or `update` to configure the sandbox auth proxy. Prefer workspace secrets for credential injection instead of placing raw secrets in local files.

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "rules": [
    {
      "name": "openai",
      "match_hosts": ["api.openai.com"],
      "match_paths": [],
      "headers": [
        {
          "name": "Authorization",
          "type": "workspace_secret",
          "value": "Bearer {OPENAI_API_KEY}"
        }
      ],
      "enabled": true
    }
  ],
  "access_control": {
    "allow_list": ["api.openai.com"],
    "deny_list": []
  }
}
```

For more on proxy rules, see [Sandbox auth proxy](/langsmith/sandbox-auth-proxy).

## Run commands

Use `sandbox exec` for one-off commands:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith sandbox exec my-vm -- uname -a
langsmith sandbox exec my-vm -- ls -la /
langsmith sandbox exec my-vm -- cat /etc/os-release
```

Everything after `--` is sent to the sandbox as the command. The CLI prints stdout to stdout, stderr to stderr, and exits with the sandbox command's exit code.

## Open an interactive console

Use `sandbox console` for a PTY-backed interactive shell:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith sandbox console my-vm
langsmith sandbox console my-vm --shell /bin/sh
```

You can forward your local SSH agent into the console session:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith sandbox console my-vm --forward-ssh-agent
```

`--forward-ssh-agent` requires `SSH_AUTH_SOCK` to be set locally. Interactive console sessions are not supported on Windows; use SSH access instead.

## Tunnel TCP ports

Use `sandbox tunnel` when you need a local TCP port that forwards to a service listening inside the sandbox. This is useful for databases, language servers, custom protocols, or local tools that expect `localhost`.

Start a service in the sandbox, then tunnel to it:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith sandbox exec my-vm -- sh -c 'cd /tmp && nohup python -m http.server 8000 > /tmp/http.log 2>&1 &'
langsmith sandbox tunnel my-vm --remote-port 8000 --local-port 18000
```

Then connect locally:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl http://127.0.0.1:18000
```

If you omit `--local-port`, the CLI uses the same value as `--remote-port`:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith sandbox tunnel my-vm --remote-port 5432
```

The tunnel process stays in the foreground. Stop it with `Ctrl+C`.

You can also tunnel by sandbox URL instead of name:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith sandbox tunnel \
  --url <SANDBOX_URL> \
  --remote-port 5432
```

<Tip>
  For HTTP applications you want to open in a browser or share with teammates, use [Sandbox service URLs](/langsmith/sandbox-service-urls). Use tunnels for raw TCP protocols or local development tools.
</Tip>

## Set up SSH access

Use `sandbox ssh-setup` to configure standard SSH tools such as `ssh`, `scp`, `rsync`, and `sftp` through a sandbox tunnel.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith sandbox ssh-setup my-vm
langsmith sandbox ssh-setup my-vm --identity ~/.ssh/id_ed25519.pub
```

The command uploads your SSH public key to the sandbox, fetches the sandbox host key when available, writes a `Host sandbox-<name>` block to `~/.ssh/config`, and writes sandbox host keys to `~/.ssh/known_hosts_sandboxes`.

After setup, connect with:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
ssh sandbox-my-vm
```

The sandbox image must run `sshd` on port `22`. If `sshd` is not running, `ssh-setup` warns and the SSH connection will not work until you start it inside the sandbox.

<Warning>
  `ssh-setup` modifies local SSH configuration and writes a `ProxyCommand` that calls `langsmith sandbox tunnel`. Depending on how the CLI is authenticated, the generated block may contain credentials or references to credentials. Run it only on trusted machines and do not commit or share the generated SSH config block.
</Warning>

## Command reference

| Command                                                          | Description                                                  |
| ---------------------------------------------------------------- | ------------------------------------------------------------ |
| `langsmith sandbox snapshot list`                                | List snapshots.                                              |
| `langsmith sandbox snapshot build <name> --docker-image <image>` | Build a snapshot from a Docker image.                        |
| `langsmith sandbox snapshot capture <name> --box <sandbox>`      | Capture a snapshot from a running sandbox.                   |
| `langsmith sandbox snapshot get <snapshot-id>`                   | Inspect a snapshot.                                          |
| `langsmith sandbox snapshot wait <snapshot-id>`                  | Wait for a snapshot to become ready.                         |
| `langsmith sandbox snapshot delete <snapshot-id>`                | Delete a snapshot.                                           |
| `langsmith sandbox create <name>`                                | Create a sandbox with the default runtime.                   |
| `langsmith sandbox list`                                         | List sandboxes.                                              |
| `langsmith sandbox get <name>`                                   | Inspect a sandbox.                                           |
| `langsmith sandbox update <name>`                                | Update sandbox resources or proxy config.                    |
| `langsmith sandbox wait <name>`                                  | Wait for a sandbox to become ready.                          |
| `langsmith sandbox start <name>`                                 | Start a stopped sandbox.                                     |
| `langsmith sandbox stop <name>`                                  | Stop a running sandbox while preserving filesystem state.    |
| `langsmith sandbox delete <name>`                                | Delete a sandbox.                                            |
| `langsmith sandbox exec <name> -- <command>`                     | Run a one-off command inside a sandbox.                      |
| `langsmith sandbox console <name>`                               | Open an interactive shell inside a sandbox.                  |
| `langsmith sandbox tunnel <name> --remote-port <port>`           | Forward a local TCP port to a sandbox port.                  |
| `langsmith sandbox ssh-setup <name>`                             | Configure local SSH access through `sandbox tunnel --stdio`. |

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/sandbox-cli.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Run evaluations with Harbor
Source: https://docs.langchain.com/langsmith/sandbox-harbor

Run Harbor evaluations and rollouts on LangSmith sandboxes with the harbor[langsmith] extra.

[Harbor](https://harborframework.com/docs) is a framework for evaluating and optimizing agents and language models in sandboxed environments, from the creators of [Terminal-Bench](https://www.tbench.ai). Harbor runs each trial in an isolated container, so you can parallelize evaluations and rollouts across many environments at once.

The `langsmith` Harbor environment runs those trials on LangSmith sandboxes. Select it with `-e langsmith` to execute Harbor jobs on LangSmith infrastructure, alongside providers such as Daytona, Modal, and E2B.

## Prerequisites

* A [LangSmith account](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-sandbox-harbor) and an API key.
* Python with `pip`.

## Install

Install Harbor with the `langsmith` extra:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
pip install "harbor[langsmith]"
```

## Authenticate

Harbor authenticates with your LangSmith credentials. Set an API key:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_API_KEY="<LANGSMITH_API_KEY>"
```

`LANGCHAIN_API_KEY` works as well. Alternatively, select a [LangSmith SDK profile](/langsmith/profile-configuration) instead of exporting a key:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_PROFILE=prod
```

## Run an evaluation

Run a Harbor job and select the LangSmith environment with `-e langsmith`:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
harbor run -d "<org/name>" \
  -m "<model>" \
  -a "<agent>" \
  -e langsmith \
  -n "<n-parallel-trials>"
```

Harbor creates one LangSmith sandbox per trial, runs the agent and verifier inside it, then tears the sandbox down when the trial finishes.

## Configure the sandbox environment

The LangSmith environment boots each sandbox from a filesystem snapshot. Provide one of the following in your Harbor task:

* **Prebuilt image**: set `[environment].docker_image` in `task.toml`. Harbor reuses or creates a snapshot from that image.
* **Existing snapshot**: pass `environment.kwargs.snapshot_name` to boot from a [snapshot](/langsmith/sandbox-snapshots) you already created.
* **Dockerfile**: include an `environment/Dockerfile`. Harbor builds a snapshot from it with the [build-from-Dockerfile flow](/langsmith/sandbox-snapshots#build-a-snapshot-from-a-dockerfile), using the task `environment/` directory as the build context.

Tune the sandbox lifecycle with environment kwargs, passed on the command line with `--ek`:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
harbor run -d "<org/name>" \
  -m "<model>" \
  -a "<agent>" \
  -e langsmith \
  -n "<n-parallel-trials>" \
  --ek idle_ttl_seconds=0 \
  --ek delete_after_stop_seconds=7200
```

* `idle_ttl_seconds`: stops an idle sandbox after this many seconds. Set `0` to disable the idle timeout.
* `delete_after_stop_seconds`: deletes a stopped sandbox after this many seconds.

## Run Deep Agents on LangSmith

Deep Agents runs against the LangSmith environment as a custom Harbor agent. To build and run a Deep Agent, see the [Deep Agents documentation](/oss/python/deepagents/overview). The Harbor wrapper ships in the [`deepagents-evals` package](https://github.com/langchain-ai/deepagents/tree/main/libs/evals), which exposes `deepagents_harbor:DeepAgentsWrapper` and includes ready-made `make run-terminal-bench-*` targets. Install it in the same environment as Harbor:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
pip install "harbor[langsmith]"

# From a checkout of langchain-ai/deepagents:
pip install -e libs/evals
```

Set your LangSmith and model credentials, then run Harbor with the wrapper:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_PROFILE=prod
export LANGSMITH_TRACING_V2=true
export LANGSMITH_PROJECT=harbor-deepagents
export ANTHROPIC_API_KEY="<ANTHROPIC_API_KEY>"

harbor run -d "terminal-bench@2.0" \
  --agent-import-path deepagents_harbor:DeepAgentsWrapper \
  --model anthropic:claude-opus-4-8 \
  -e langsmith \
  -n 10 \
  -l 10 \
  --yes \
  --ek idle_ttl_seconds=0 \
  --ek delete_after_stop_seconds=7200
```

Keep API keys in your shell environment rather than in a job config file.

## Use a config file

Capture the same run in a Harbor job config:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
jobs_dir: jobs/deepagents-langsmith
n_attempts: 1
n_concurrent_trials: 10
environment:
  type: langsmith
  delete: true
  kwargs:
    idle_ttl_seconds: 0
    delete_after_stop_seconds: 7200
agents:
  - import_path: deepagents_harbor:DeepAgentsWrapper
    model_name: anthropic:claude-opus-4-8
datasets:
  - name: terminal-bench
    version: "2.0"
    n_tasks: 10
```

## Multi-container tasks

The LangSmith environment supports multi-container tasks. Include an `environment/docker-compose.yaml` file in your task definition to run several containers per trial. See the [Harbor sandbox documentation](https://harborframework.com/docs/run-jobs/cloud-sandboxes) for details.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/sandbox-harbor.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Sandbox access permissions
Source: https://docs.langchain.com/langsmith/sandbox-permissions

Control who in your workspace can interact with a sandbox after it has been created.

Each sandbox has a recorded **creator**, the workspace member whose API key or session created it. By default, only the creator can run commands, read or write files, open tunnels, or reach service URLs on that sandbox. Other workspace members need the `sandboxes:exec` [permission](/langsmith/rbac) to interact with sandboxes they did not create. Sandboxes are never reachable from workspaces other than the one they were created in.

## Who can do what

| Caller                 | Default                         | With `sandboxes:exec`           |
| ---------------------- | ------------------------------- | ------------------------------- |
| Sandbox creator        | ✅ All runtime actions           | ✅ All runtime actions           |
| Other workspace member | ❌ Denied                        | ✅ All runtime actions           |
| Different workspace    | ❌ Hidden (treated as not found) | ❌ Hidden (treated as not found) |

"Runtime actions" covers the four ways you interact with a running sandbox after creation:

* **Execute** a command (`langsmith sandbox exec`, `SandboxClient.exec`)
* **File** operations (read, write, list paths inside the sandbox)
* **Tunnel** a TCP port back to your machine (`langsmith sandbox tunnel`)
* **Proxy** requests through a [service URL](/langsmith/sandbox-service-urls)

Lifecycle operations—creating, listing, updating, deleting sandboxes—continue to use the existing `sandboxes:create` / `sandboxes:read` / `sandboxes:update` / `sandboxes:delete` permissions. Those are unchanged.

## Denied requests

When a request is denied, the sandbox returns `HTTP 403` with a body that names the rule that fired:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "detail": {
    "error": "Forbidden",
    "message": "sandbox access denied: not the creator and missing sandboxes:exec"
  }
}
```

Requests for a sandbox that exists in another workspace return `404 Not Found` rather than `403`, so the response does not reveal whether the sandbox exists elsewhere.

## Sharing a sandbox

You have two ways to let teammates work with a sandbox you own:

1. **Grant `sandboxes:exec`** to a custom role and assign that role in the workspace. Anyone with the role can interact with every sandbox in the workspace.
2. **Use a [service URL](/langsmith/sandbox-service-urls)** for HTTP services running inside the sandbox. Service URLs use their own access tokens and do not require the recipient to be a workspace member.

For ad-hoc collaboration the service-URL approach is usually simpler; reach for `sandboxes:exec` when a teammate needs broad access to operate sandboxes they did not create.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/sandbox-permissions.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
