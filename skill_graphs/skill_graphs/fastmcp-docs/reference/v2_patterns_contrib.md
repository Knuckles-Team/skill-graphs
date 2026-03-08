[Skip to main content](https://gofastmcp.com/v2/patterns/contrib#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v2.14.5
Search...
Navigation
Patterns
Contrib Modules
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
  * [Usage](https://gofastmcp.com/v2/patterns/contrib#usage)
  * [Important Considerations](https://gofastmcp.com/v2/patterns/contrib#important-considerations)
  * [Contributing](https://gofastmcp.com/v2/patterns/contrib#contributing)


Patterns
# Contrib Modules
Copy page
Community-contributed modules extending FastMCP
Copy page
`2.2.1` FastMCP includes a `contrib` package that holds community-contributed modules. These modules extend FastMCP’s functionality but aren’t officially maintained by the core team. Contrib modules provide additional features, integrations, or patterns that complement the core FastMCP library. They offer a way for the community to share useful extensions while keeping the core library focused and maintainable. The available modules can be viewed in the
##
[​](https://gofastmcp.com/v2/patterns/contrib#usage)
Usage
To use a contrib module, import it from the `fastmcp.contrib` package:
Copy
```
from fastmcp.contrib import my_module

```

##
[​](https://gofastmcp.com/v2/patterns/contrib#important-considerations)
Important Considerations
  * **Stability** : Modules in `contrib` may have different testing requirements or stability guarantees compared to the core library.
  * **Compatibility** : Changes to core FastMCP might break modules in `contrib` without explicit warnings in the main changelog.
  * **Dependencies** : Contrib modules may have additional dependencies not required by the core library. These dependencies are typically documented in the module’s README or separate requirements files.


##
[​](https://gofastmcp.com/v2/patterns/contrib#contributing)
Contributing
We welcome contributions to the `contrib` package! If you have a module that extends FastMCP in a useful way, consider contributing it:
  1. Create a new directory in `src/fastmcp/contrib/` for your module
  2. Add proper tests for your module in `tests/contrib/`
  3. Include comprehensive documentation in a README.md file, including usage and examples, as well as any additional dependencies or installation instructions
  4. Submit a pull request

The ideal contrib module:
  * Solves a specific use case or integration need
  * Follows FastMCP coding standards
  * Includes thorough documentation and examples
  * Has comprehensive tests
  * Specifies any additional dependencies


[ FastMCP CLI Previous ](https://gofastmcp.com/v2/patterns/cli)[ Testing your FastMCP Server Next ](https://gofastmcp.com/v2/patterns/testing)
Ctrl+I
