[Skip to main content](https://gofastmcp.com/clients/resources#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Core Operations
Reading Resources
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
    * [Tools](https://gofastmcp.com/clients/tools)
    * [Resources](https://gofastmcp.com/clients/resources)
    * [Prompts](https://gofastmcp.com/clients/prompts)
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
  * [Reading Resources](https://gofastmcp.com/clients/resources#reading-resources)
  * [Content Types](https://gofastmcp.com/clients/resources#content-types)
  * [Multi-Server Clients](https://gofastmcp.com/clients/resources#multi-server-clients)
  * [Version Selection](https://gofastmcp.com/clients/resources#version-selection)
  * [Raw Protocol Access](https://gofastmcp.com/clients/resources#raw-protocol-access)


Core Operations
# Reading Resources
Copy page
Access static and templated data sources from MCP servers.
Copy page
`2.0.0` Use this when you need to read data from server-exposed resources like configuration files, generated content, or external data sources. Resources are data sources exposed by MCP servers. They can be static files with fixed content, or dynamic templates that generate content based on parameters in the URI.
##
[​](https://gofastmcp.com/clients/resources#reading-resources)
Reading Resources
Read a resource using its URI:
Copy
```
async with client:
    content = await client.read_resource("file:///path/to/README.md")
    # content -> list[TextResourceContents | BlobResourceContents]

    # Access text content
    if hasattr(content[0], 'text'):
        print(content[0].text)

    # Access binary content
    if hasattr(content[0], 'blob'):
        print(f"Binary data: {len(content[0].blob)} bytes")

```

Resource templates generate content based on URI parameters. The template defines a pattern like `weather://{{city}}/current`, and you fill in the parameters when reading:
Copy
```
async with client:
    # Read from a resource template
    weather_content = await client.read_resource("weather://london/current")
    print(weather_content[0].text)

```

##
[​](https://gofastmcp.com/clients/resources#content-types)
Content Types
Resources return different content types depending on what they expose. Text resources include configuration files, JSON data, and other human-readable content:
Copy
```
async with client:
    content = await client.read_resource("resource://config/settings.json")

    for item in content:
        if hasattr(item, 'text'):
            print(f"Text content: {item.text}")
            print(f"MIME type: {item.mimeType}")

```

Binary resources include images, PDFs, and other non-text data:
Copy
```
async with client:
    content = await client.read_resource("resource://images/logo.png")

    for item in content:
        if hasattr(item, 'blob'):
            print(f"Binary content: {len(item.blob)} bytes")
            print(f"MIME type: {item.mimeType}")

            # Save to file
            with open("downloaded_logo.png", "wb") as f:
                f.write(item.blob)

```

##
[​](https://gofastmcp.com/clients/resources#multi-server-clients)
Multi-Server Clients
When using multi-server clients, resource URIs are prefixed with the server name:
Copy
```
async with client:  # Multi-server client
    weather_icons = await client.read_resource("weather://weather/icons/sunny")
    templates = await client.read_resource("resource://assistant/templates/list")

```

##
[​](https://gofastmcp.com/clients/resources#version-selection)
Version Selection
`3.0.0` When a server exposes multiple versions of a resource, you can request a specific version:
Copy
```
async with client:
    # Read the highest version (default)
    content = await client.read_resource("data://config")

    # Read a specific version
    content_v1 = await client.read_resource("data://config", version="1.0")

```

See [Metadata](https://gofastmcp.com/servers/versioning#version-discovery) for how to discover available versions.
##
[​](https://gofastmcp.com/clients/resources#raw-protocol-access)
Raw Protocol Access
For complete control, use `read_resource_mcp()` which returns the full MCP protocol object:
Copy
```
async with client:
    result = await client.read_resource_mcp("resource://example")
    # result -> mcp.types.ReadResourceResult

```

[ Calling Tools Previous ](https://gofastmcp.com/clients/tools)[ Getting Prompts Next ](https://gofastmcp.com/clients/prompts)
Ctrl+I
