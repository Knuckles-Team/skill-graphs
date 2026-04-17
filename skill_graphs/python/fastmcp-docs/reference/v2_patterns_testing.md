[Skip to main content](https://gofastmcp.com/v2/patterns/testing#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v2.14.5
Search...
Navigation
Patterns
Testing your FastMCP Server
Search the docs...
Ctrl K
Documentation
##### Get Started
  * [Welcome!](https://gofastmcp.com/v2/getting-started/welcome)
  * [Installation](https://gofastmcp.com/v2/getting-started/installation)
  * [Quickstart](https://gofastmcp.com/v2/getting-started/quickstart)
  * [ Updates NEW ](https://gofastmcp.com/v2/updates)


##### Servers
  * [Overview](https://gofastmcp.com/v2/servers/server)
  * Core Components
  * Advanced Features
  * Authentication
  * Deployment


##### Clients
  * Essentials
  * Core Operations
  * Advanced Features
  * Authentication


##### Integrations
  * Authentication
  * Authorization
  * AI Assistants
  * AI SDKs
  * API Integration


##### Patterns
  * [Tool Transformation](https://gofastmcp.com/v2/patterns/tool-transformation)
  * [Decorating Methods](https://gofastmcp.com/v2/patterns/decorating-methods)
  * [CLI](https://gofastmcp.com/v2/patterns/cli)
  * [Contrib Modules](https://gofastmcp.com/v2/patterns/contrib)
  * [Testing](https://gofastmcp.com/v2/patterns/testing)


##### Development
  * [Contributing](https://gofastmcp.com/v2/development/contributing)
  * [Tests](https://gofastmcp.com/v2/development/tests)
  * [Releases](https://gofastmcp.com/v2/development/releases)
  * [ Upgrade Guide NEW ](https://gofastmcp.com/v2/development/upgrade-guide)
  * [Changelog](https://gofastmcp.com/v2/changelog)


These are the docs for FastMCP 2.0. [FastMCP 3.0](https://gofastmcp.com/getting-started/welcome) is now available.
On this page
  * [Prerequisites](https://gofastmcp.com/v2/patterns/testing#prerequisites)
  * [Testing with Pytest Fixtures](https://gofastmcp.com/v2/patterns/testing#testing-with-pytest-fixtures)


Patterns
# Testing your FastMCP Server
Copy page
How to test your FastMCP server.
Copy page
The best way to ensure a reliable and maintainable FastMCP Server is to test it! The FastMCP Client combined with Pytest provides a simple and powerful way to test your FastMCP servers.
##
[​](https://gofastmcp.com/v2/patterns/testing#prerequisites)
Prerequisites
Testing FastMCP servers requires `pytest-asyncio` to handle async test functions and fixtures. Install it as a development dependency:
Copy
```
pip install pytest-asyncio

```

We recommend configuring pytest to automatically handle async tests by setting the asyncio mode to `auto` in your `pyproject.toml`:
Copy
```
[tool.pytest.ini_options]
asyncio_mode = "auto"

```

This eliminates the need to decorate every async test with `@pytest.mark.asyncio`.
##
[​](https://gofastmcp.com/v2/patterns/testing#testing-with-pytest-fixtures)
Testing with Pytest Fixtures
Using Pytest Fixtures, you can wrap your FastMCP Server in a Client instance that makes interacting with your server fast and easy. This is especially useful when building your own MCP Servers and enables a tight development loop by allowing you to avoid using a separate tool like MCP Inspector during development:
Copy
```
import pytest
from fastmcp.client import Client
from fastmcp.client.transports import FastMCPTransport

from my_project.main import mcp

@pytest.fixture
async def main_mcp_client():
    async with Client(transport=mcp) as mcp_client:
        yield mcp_client

async def test_list_tools(main_mcp_client: Client[FastMCPTransport]):
    list_tools = await main_mcp_client.list_tools()

    assert len(list_tools) == 5

```

We recommend the
Copy
```
from inline_snapshot import snapshot

async def test_list_tools(main_mcp_client: Client[FastMCPTransport]):
    list_tools = await main_mcp_client.list_tools()

    assert list_tools == snapshot()

```

Simply run `pytest --inline-snapshot=fix,create` to fill in the `snapshot()` with actual data.
For values that change you can leverage the
Using the pytest `parametrize` decorator, you can easily test your tools with a wide variety of inputs.
Copy
```
import pytest
from my_project.main import mcp

from fastmcp.client import Client
from fastmcp.client.transports import FastMCPTransport
@pytest.fixture
async def main_mcp_client():
    async with Client(mcp) as client:
        yield client


@pytest.mark.parametrize(
    "first_number, second_number, expected",
    [
        (1, 2, 3),
        (2, 3, 5),
        (3, 4, 7),
    ],
)
async def test_add(
    first_number: int,
    second_number: int,
    expected: int,
    main_mcp_client: Client[FastMCPTransport],
):
    result = await main_mcp_client.call_tool(
        name="add", arguments={"x": first_number, "y": second_number}
    )
    assert result.data is not None
    assert isinstance(result.data, int)
    assert result.data == expected

```

The
[ Contrib Modules Previous ](https://gofastmcp.com/v2/patterns/contrib)[ Contributing Next ](https://gofastmcp.com/v2/development/contributing)
Ctrl+I
