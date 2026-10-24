[Skip to main content](https://gofastmcp.com/servers/telemetry#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Features
OpenTelemetry
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
  * [How It Works](https://gofastmcp.com/servers/telemetry#how-it-works)
  * [Enabling Telemetry](https://gofastmcp.com/servers/telemetry#enabling-telemetry)
  * [Tracing](https://gofastmcp.com/servers/telemetry#tracing)
  * [Server Spans](https://gofastmcp.com/servers/telemetry#server-spans)
  * [Client Spans](https://gofastmcp.com/servers/telemetry#client-spans)
  * [Span Hierarchy](https://gofastmcp.com/servers/telemetry#span-hierarchy)
  * [Programmatic Configuration](https://gofastmcp.com/servers/telemetry#programmatic-configuration)
  * [Local Development](https://gofastmcp.com/servers/telemetry#local-development)
  * [Custom Spans](https://gofastmcp.com/servers/telemetry#custom-spans)
  * [Error Handling](https://gofastmcp.com/servers/telemetry#error-handling)
  * [Attributes Reference](https://gofastmcp.com/servers/telemetry#attributes-reference)
  * [RPC Semantic Conventions](https://gofastmcp.com/servers/telemetry#rpc-semantic-conventions)
  * [MCP Semantic Conventions](https://gofastmcp.com/servers/telemetry#mcp-semantic-conventions)
  * [Auth Attributes](https://gofastmcp.com/servers/telemetry#auth-attributes)
  * [FastMCP Custom Attributes](https://gofastmcp.com/servers/telemetry#fastmcp-custom-attributes)
  * [Testing with Telemetry](https://gofastmcp.com/servers/telemetry#testing-with-telemetry)


Features
# OpenTelemetry
Copy page
Native OpenTelemetry instrumentation for distributed tracing.
Copy page
FastMCP includes native OpenTelemetry instrumentation for observability. Traces are automatically generated for tool, prompt, resource, and resource template operations, providing visibility into server behavior, request handling, and provider delegation chains.
##
[​](https://gofastmcp.com/servers/telemetry#how-it-works)
How It Works
FastMCP uses the OpenTelemetry API for instrumentation. This means:
  * **Zero configuration required** - Instrumentation is always active
  * **No overhead when unused** - Without an SDK, all operations are no-ops
  * **Bring your own SDK** - You control collection, export, and sampling
  * **Works with any OTEL backend** - Jaeger, Zipkin, Datadog, New Relic, etc.


##
[​](https://gofastmcp.com/servers/telemetry#enabling-telemetry)
Enabling Telemetry
The easiest way to export traces is using `opentelemetry-instrument`, which configures the SDK automatically:
Copy
```
pip install opentelemetry-distro opentelemetry-exporter-otlp
opentelemetry-bootstrap -a install

```

Then run your server with tracing enabled:
Copy
```
opentelemetry-instrument \
  --service_name my-fastmcp-server \
  --exporter_otlp_endpoint http://localhost:4317 \
  fastmcp run server.py

```

Or configure via environment variables:
Copy
```
export OTEL_SERVICE_NAME=my-fastmcp-server
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317

opentelemetry-instrument fastmcp run server.py

```

This works with any OTLP-compatible backend (Jaeger, Zipkin, Grafana Tempo, Datadog, etc.) and requires no changes to your FastMCP code.
##
[​](https://gofastmcp.com/servers/telemetry#tracing)
Tracing
FastMCP creates spans for all MCP operations, providing end-to-end visibility into request handling.
###
[​](https://gofastmcp.com/servers/telemetry#server-spans)
Server Spans
The server creates spans for each operation using
Span Name | Description
---|---
`tools/call {name}` | Tool execution (e.g., `tools/call get_weather`)
`resources/read {uri}` | Resource read (e.g., `resources/read config://database`)
`prompts/get {name}` | Prompt render (e.g., `prompts/get greeting`)
For mounted servers, an additional `delegate {name}` span shows the delegation to the child server.
###
[​](https://gofastmcp.com/servers/telemetry#client-spans)
Client Spans
The FastMCP client creates spans for outgoing requests with the same naming pattern (`tools/call {name}`, `resources/read {uri}`, `prompts/get {name}`).
###
[​](https://gofastmcp.com/servers/telemetry#span-hierarchy)
Span Hierarchy
Spans form a hierarchy showing the request flow. For mounted servers:
Copy
```
tools/call weather_forecast (CLIENT)
  └── tools/call weather_forecast (SERVER, provider=FastMCPProvider)
        └── delegate get_weather (INTERNAL)
              └── tools/call get_weather (SERVER, provider=LocalProvider)

```

For proxy providers connecting to remote servers:
Copy
```
tools/call remote_search (CLIENT)
  └── tools/call remote_search (SERVER, provider=ProxyProvider)
        └── [remote server spans via trace context propagation]

```

##
[​](https://gofastmcp.com/servers/telemetry#programmatic-configuration)
Programmatic Configuration
For more control, configure the SDK in your Python code before importing FastMCP:
Copy
```
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

# Configure the SDK with OTLP exporter
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://localhost:4317"))
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

# Now import and use FastMCP - traces will be exported automatically
from fastmcp import FastMCP

mcp = FastMCP("my-server")

@mcp.tool()
def greet(name: str) -> str:
    return f"Hello, {name}!"

```

The SDK must be configured **before** importing FastMCP to ensure the tracer provider is set when FastMCP initializes.
###
[​](https://gofastmcp.com/servers/telemetry#local-development)
Local Development
For quick local trace visualization,
Copy
```
# macOS
brew install nico-barbas/brew/otel-desktop-viewer

# Or download from GitHub releases

```

Run it alongside your server:
Copy
```
# Terminal 1: Start the viewer (UI at http://localhost:8000, OTLP on :4317)
otel-desktop-viewer

# Terminal 2: Run your server with tracing
opentelemetry-instrument fastmcp run server.py

```

For more features, use
Copy
```
docker run -d --name jaeger \
  -p 16686:16686 \
  -p 4317:4317 \
  jaegertracing/all-in-one:latest

```

Then view traces at
##
[​](https://gofastmcp.com/servers/telemetry#custom-spans)
Custom Spans
You can add your own spans using the FastMCP tracer:
Copy
```
from fastmcp import FastMCP
from fastmcp.telemetry import get_tracer

mcp = FastMCP("custom-spans")

@mcp.tool()
async def complex_operation(input: str) -> str:
    tracer = get_tracer()

    with tracer.start_as_current_span("parse_input") as span:
        span.set_attribute("input.length", len(input))
        parsed = parse(input)

    with tracer.start_as_current_span("process_data") as span:
        span.set_attribute("data.count", len(parsed))
        result = process(parsed)

    return result

```

##
[​](https://gofastmcp.com/servers/telemetry#error-handling)
Error Handling
When errors occur, spans are automatically marked with error status and the exception is recorded:
Copy
```
@mcp.tool()
def risky_operation() -> str:
    raise ValueError("Something went wrong")

# The span will have:
# - status = ERROR
# - exception event with stack trace

```

##
[​](https://gofastmcp.com/servers/telemetry#attributes-reference)
Attributes Reference
###
[​](https://gofastmcp.com/servers/telemetry#rpc-semantic-conventions)
RPC Semantic Conventions
Standard
Attribute | Value
---|---
`rpc.system` | `"mcp"`
`rpc.service` | Server name
`rpc.method` | MCP protocol method
###
[​](https://gofastmcp.com/servers/telemetry#mcp-semantic-conventions)
MCP Semantic Conventions
FastMCP implements the
Attribute | Description
---|---
`mcp.method.name` | The MCP method being called (`tools/call`, `resources/read`, `prompts/get`)
`mcp.session.id` | Session identifier for the MCP connection
`mcp.resource.uri` | The resource URI (for resource operations)
###
[​](https://gofastmcp.com/servers/telemetry#auth-attributes)
Auth Attributes
Standard
Attribute | Description
---|---
`enduser.id` | Client ID from access token (when authenticated)
`enduser.scope` | Space-separated OAuth scopes (when authenticated)
###
[​](https://gofastmcp.com/servers/telemetry#fastmcp-custom-attributes)
FastMCP Custom Attributes
All custom attributes use the `fastmcp.` prefix for features unique to FastMCP:
Attribute | Description
---|---
`fastmcp.server.name` | Server name
`fastmcp.component.type` |  `tool`, `resource`, `prompt`, or `resource_template`
`fastmcp.component.key` | Full component identifier (e.g., `tool:greet`)
`fastmcp.provider.type` | Provider class (`LocalProvider`, `FastMCPProvider`, `ProxyProvider`)
Provider-specific attributes for delegation context:
Attribute | Description
---|---
`fastmcp.delegate.original_name` | Original tool/prompt name before namespacing
`fastmcp.delegate.original_uri` | Original resource URI before namespacing
`fastmcp.proxy.backend_name` | Remote server tool/prompt name
`fastmcp.proxy.backend_uri` | Remote server resource URI
##
[​](https://gofastmcp.com/servers/telemetry#testing-with-telemetry)
Testing with Telemetry
For testing, use the in-memory exporter:
Copy
```
import pytest
from collections.abc import Generator
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter

from fastmcp import FastMCP

@pytest.fixture
def trace_exporter() -> Generator[InMemorySpanExporter, None, None]:
    exporter = InMemorySpanExporter()
    provider = TracerProvider()
    provider.add_span_processor(SimpleSpanProcessor(exporter))
    original_provider = trace.get_tracer_provider()
    trace.set_tracer_provider(provider)
    yield exporter
    exporter.clear()
    trace.set_tracer_provider(original_provider)

async def test_tool_creates_span(trace_exporter: InMemorySpanExporter) -> None:
    mcp = FastMCP("test")

    @mcp.tool()
    def hello() -> str:
        return "world"

    await mcp.call_tool("hello", {})

    spans = trace_exporter.get_finished_spans()
    assert any(s.name == "tools/call hello" for s in spans)

```

[ Storage Backends Previous ](https://gofastmcp.com/servers/storage-backends)[ Testing your FastMCP Server Next ](https://gofastmcp.com/servers/testing)
Ctrl+I
