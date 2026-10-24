[Skip to main content](https://gofastmcp.com/apps/low-level#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Apps
Custom HTML Apps
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
  * [How It Works](https://gofastmcp.com/apps/low-level#how-it-works)
  * [AppConfig](https://gofastmcp.com/apps/low-level#appconfig)
  * [Tool Visibility](https://gofastmcp.com/apps/low-level#tool-visibility)
  * [AppConfig Fields](https://gofastmcp.com/apps/low-level#appconfig-fields)
  * [UI Resources](https://gofastmcp.com/apps/low-level#ui-resources)
  * [Writing the App HTML](https://gofastmcp.com/apps/low-level#writing-the-app-html)
  * [Security](https://gofastmcp.com/apps/low-level#security)
  * [Content Security Policy](https://gofastmcp.com/apps/low-level#content-security-policy)
  * [Permissions](https://gofastmcp.com/apps/low-level#permissions)
  * [Example: QR Code Server](https://gofastmcp.com/apps/low-level#example-qr-code-server)
  * [Checking Client Support](https://gofastmcp.com/apps/low-level#checking-client-support)


Apps
# Custom HTML Apps
Copy page
Build apps with your own HTML, CSS, and JavaScript using the MCP Apps extension directly.
Copy page
`3.0.0` The [Prefab UI](https://gofastmcp.com/apps/prefab) builds on this protocol so you never have to think about it, but when you need full control — custom rendering, a specific JavaScript framework, maps, 3D, video — you can use the MCP Apps extension directly. This page covers how to write custom HTML apps and wire them up in FastMCP. You’ll be working with the `AppConfig` for resource and CSP management.
##
[​](https://gofastmcp.com/apps/low-level#how-it-works)
How It Works
An MCP App has two parts:
  1. A **tool** that does the work and returns data
  2. A **`ui://`resource** containing the HTML that renders that data

The tool declares which resource to use via `AppConfig`. When the host calls the tool, it also fetches the linked resource, renders it in a sandboxed iframe, and pushes the tool result into the app via `postMessage`. The app can also call tools back, enabling interactive workflows.
Copy
```
import json

from fastmcp import FastMCP
from fastmcp.server.apps import AppConfig, ResourceCSP

mcp = FastMCP("My App Server")

# The tool does the work
@mcp.tool(app=AppConfig(resource_uri="ui://my-app/view.html"))
def generate_chart(data: list[float]) -> str:
    return json.dumps({"values": data})

# The resource provides the UI
@mcp.resource("ui://my-app/view.html")
def chart_view() -> str:
    return "<html>...</html>"

```

##
[​](https://gofastmcp.com/apps/low-level#appconfig)
AppConfig
`AppConfig` controls how a tool or resource participates in the Apps extension. Import it from `fastmcp.server.apps`:
Copy
```
from fastmcp.server.apps import AppConfig

```

On **tools** , you’ll typically set `resource_uri` to point to the UI resource:
Copy
```
@mcp.tool(app=AppConfig(resource_uri="ui://my-app/view.html"))
def my_tool() -> str:
    return "result"

```

You can also pass a raw dict with camelCase keys, matching the wire format:
Copy
```
@mcp.tool(app={"resourceUri": "ui://my-app/view.html"})
def my_tool() -> str:
    return "result"

```

###
[​](https://gofastmcp.com/apps/low-level#tool-visibility)
Tool Visibility
The `visibility` field controls where a tool appears:
  * `["model"]` — visible to the LLM (the default behavior)
  * `["app"]` — only callable from within the app UI, hidden from the LLM
  * `["model", "app"]` — both

This is useful when you have tools that only make sense as part of the app’s interactive flow, not as standalone LLM actions.
Copy
```
@mcp.tool(
    app=AppConfig(
        resource_uri="ui://my-app/view.html",
        visibility=["app"],
    )
)
def refresh_data() -> str:
    """Only callable from the app UI, not by the LLM."""
    return fetch_latest()

```

###
[​](https://gofastmcp.com/apps/low-level#appconfig-fields)
AppConfig Fields
Field | Type | Description
---|---|---
`resource_uri` | `str` | URI of the UI resource. Tools only.
`visibility` | `list[str]` | Where the tool appears: `"model"`, `"app"`, or both. Tools only.
`csp` | `ResourceCSP` | Content Security Policy for the iframe.
`permissions` | `ResourcePermissions` | Iframe sandbox permissions.
`domain` | `str` | Stable sandbox origin for the iframe.
`prefers_border` | `bool` | Whether the UI prefers a visible border.
On **resources** , `resource_uri` and `visibility` must not be set — the resource _is_ the UI. Use `AppConfig` on resources only for `csp`, `permissions`, and other display settings.
##
[​](https://gofastmcp.com/apps/low-level#ui-resources)
UI Resources
Resources using the `ui://` scheme are automatically served with the MIME type `text/html;profile=mcp-app`. You don’t need to set this manually.
Copy
```
@mcp.resource("ui://my-app/view.html")
def my_view() -> str:
    return "<html>...</html>"

```

The HTML can be anything — a full single-page app, a simple display, or a complex interactive tool. The host renders it in a sandboxed iframe and establishes a `postMessage` channel for communication.
###
[​](https://gofastmcp.com/apps/low-level#writing-the-app-html)
Writing the App HTML
Your HTML app communicates with the host using the
Copy
```
<script type="module">
  import { App } from "https://unpkg.com/@modelcontextprotocol/ext-apps@0.4.0/app-with-deps";

  const app = new App({ name: "My App", version: "1.0.0" });

  // Receive tool results pushed by the host
  app.ontoolresult = ({ content }) => {
    const text = content?.find(c => c.type === 'text');
    if (text) {
      document.getElementById('output').textContent = text.text;
    }
  };

  // Connect to the host
  await app.connect();
</script>

```

The `App` object provides:
  * **`app.ontoolresult`**— callback that receives tool results pushed by the host
  * **`app.callServerTool({name, arguments})`**— call a tool on the server from within the app
  * **`app.onhostcontextchanged`**— callback for host context changes (e.g., safe area insets)
  * **`app.getHostContext()`**— get current host context


If your HTML loads external scripts, styles, or makes API calls, you need to declare those domains in the CSP configuration. See [Security](https://gofastmcp.com/apps/low-level#security) below.
##
[​](https://gofastmcp.com/apps/low-level#security)
Security
Apps run in sandboxed iframes with a deny-by-default Content Security Policy. By default, only inline scripts and styles are allowed — no external network access.
###
[​](https://gofastmcp.com/apps/low-level#content-security-policy)
Content Security Policy
If your app needs to load external resources (CDN scripts, API calls, embedded iframes), declare the allowed domains with `ResourceCSP`:
Copy
```
from fastmcp.server.apps import AppConfig, ResourceCSP

@mcp.resource(
    "ui://my-app/view.html",
    app=AppConfig(
        csp=ResourceCSP(
            resource_domains=["https://unpkg.com", "https://cdn.example.com"],
            connect_domains=["https://api.example.com"],
        )
    ),
)
def my_view() -> str:
    return "<html>...</html>"

```

CSP Field | Controls
---|---
`connect_domains` |  `fetch`, XHR, WebSocket (`connect-src`)
`resource_domains` | Scripts, images, styles, fonts (`script-src`, etc.)
`frame_domains` | Nested iframes (`frame-src`)
`base_uri_domains` | Document base URI (`base-uri`)
###
[​](https://gofastmcp.com/apps/low-level#permissions)
Permissions
If your app needs browser capabilities like camera or clipboard access, request them via `ResourcePermissions`:
Copy
```
from fastmcp.server.apps import AppConfig, ResourcePermissions

@mcp.resource(
    "ui://my-app/view.html",
    app=AppConfig(
        permissions=ResourcePermissions(
            camera={},
            clipboard_write={},
        )
    ),
)
def my_view() -> str:
    return "<html>...</html>"

```

Hosts may or may not grant these permissions. Your app should use JavaScript feature detection as a fallback.
##
[​](https://gofastmcp.com/apps/low-level#example-qr-code-server)
Example: QR Code Server
This example creates a tool that generates QR codes and an app that renders them as images. It’s based on the `qrcode[pil]` package.
Copy
```
import base64
import io

import qrcode
from mcp import types

from fastmcp import FastMCP
from fastmcp.server.apps import AppConfig, ResourceCSP
from fastmcp.tools import ToolResult

mcp = FastMCP("QR Code Server")

VIEW_URI = "ui://qr-server/view.html"


@mcp.tool(app=AppConfig(resource_uri=VIEW_URI))
def generate_qr(text: str = "https://gofastmcp.com") -> ToolResult:
    """Generate a QR code from text."""
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image()
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    b64 = base64.b64encode(buffer.getvalue()).decode()

    return ToolResult(
        content=[types.ImageContent(type="image", data=b64, mimeType="image/png")]
    )


@mcp.resource(
    VIEW_URI,
    app=AppConfig(csp=ResourceCSP(resource_domains=["https://unpkg.com"])),
)
def view() -> str:
    """Interactive QR code viewer."""
    return """\
<!DOCTYPE html>
<html>
<head>
  <meta name="color-scheme" content="light dark">
  <style>
    body { display: flex; justify-content: center;
           align-items: center; height: 340px; width: 340px;
           margin: 0; background: transparent; }
    img  { width: 300px; height: 300px; border-radius: 8px;
           box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
  </style>
</head>
<body>
  <div id="qr"></div>
  <script type="module">
    import { App } from
      "https://unpkg.com/@modelcontextprotocol/ext-apps@0.4.0/app-with-deps";

    const app = new App({ name: "QR View", version: "1.0.0" });

    app.ontoolresult = ({ content }) => {
      const img = content?.find(c => c.type === 'image');
      if (img) {
        const el = document.createElement('img');
        el.src = `data:${img.mimeType};base64,${img.data}`;
        el.alt = "QR Code";
        document.getElementById('qr').replaceChildren(el);
      }
    };

    await app.connect();
  </script>
</body>
</html>"""

```

The tool generates a QR code as a base64 PNG. The resource loads the MCP Apps JS SDK from unpkg (declared in the CSP), listens for tool results, and renders the image. The host wires them together — when the LLM calls `generate_qr`, the QR code appears in an interactive frame inside the conversation.
##
[​](https://gofastmcp.com/apps/low-level#checking-client-support)
Checking Client Support
Not all hosts support the Apps extension. You can check at runtime using the tool’s [context](https://gofastmcp.com/servers/context):
Copy
```
from fastmcp import Context
from fastmcp.server.apps import AppConfig, UI_EXTENSION_ID

@mcp.tool(app=AppConfig(resource_uri="ui://my-app/view.html"))
async def my_tool(ctx: Context) -> str:
    if ctx.client_supports_extension(UI_EXTENSION_ID):
        # Return data optimized for UI rendering
        return rich_response()
    else:
        # Fall back to plain text
        return plain_text_response()

```

[ Patterns Previous ](https://gofastmcp.com/apps/patterns)[ The FastMCP Client Next ](https://gofastmcp.com/clients/client)
Ctrl+I
