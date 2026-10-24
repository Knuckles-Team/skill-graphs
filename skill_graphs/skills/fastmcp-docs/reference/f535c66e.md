# Changelog
Copy page
Copy page
[​](https://gofastmcp.com/changelog#v3-0-2)
v3.0.2
2026-02-22
Two community-contributed fixes: auth headers from MCP transport no longer leak through to downstream OpenAPI APIs, and background task workers now correctly receive the originating request ID. Plus a new docs example for context-aware tool factories.
###
[​](https://gofastmcp.com/changelog#fixes-)
Fixes 🐞
  * fix: prevent MCP transport auth header from leaking to downstream OpenAPI APIs by
  * fix: propagate origin_request_id to background task workers by


###
[​](https://gofastmcp.com/changelog#docs-)
Docs 📚
  * Add v3.0.1 release notes by
  * docs: add context-aware tool factory example by

**Full Changelog** :
[​](https://gofastmcp.com/changelog#v3-0-1)
v3.0.1
2026-02-20
First patch after 3.0 — mostly smoothing out rough edges discovered in the wild. The big ones: middleware state that wasn’t surviving the trip to tool handlers now does, `Tool.from_tool()` accepts callables again, OpenAPI schemas with circular references no longer crash discovery, and decorator overloads now return the correct types in function mode. Also adds `verify_id_token` to OIDCProxy for providers (like some Azure AD configs) that issue opaque access tokens but standard JWT id_tokens.
###
[​](https://gofastmcp.com/changelog#enhancements-)
Enhancements 🔧
  * Add verify_id_token option to OIDCProxy by


###
[​](https://gofastmcp.com/changelog#fixes--2)
Fixes 🐞
  * Fix v3.0.0 changelog compare link by
  * Fix MDX parse error in upgrade guide prompts by
  * Fix non-serializable state lost between middleware and tools by
  * Accept callables in Tool.from_tool() by
  * Preserve skill metadata through provider wrapping by
  * Fix circular reference crash in OpenAPI schemas by
  * Fix NameError with future annotations and Context/Depends parameters by
  * Fix ty ignore syntax in OpenAPI provider by
  * Use max_completion_tokens instead of deprecated max_tokens in OpenAI handler by
  * Fix ty compatibility with upgraded deps by
  * Fix decorator overload return types for function mode by


###
[​](https://gofastmcp.com/changelog#docs--2)
Docs 📚
  * Sync README with welcome.mdx, fix install count by
  * Document dict-to-Message prompt migration in upgrade guides by
  * Fix v2 upgrade guide: remove incorrect v1 import advice by
  * Animated banner by
  * Document mounted server state store isolation in upgrade guide by

**Full Changelog** :
[​](https://gofastmcp.com/changelog#v3-0-0)
v3.0.0
2026-02-18
FastMCP 3.0 is stable. Two betas, two release candidates, 21 new contributors, and more than 100,000 pre-release installs later — the architecture held up, the upgrade path was smooth, and we’re shipping it.The surface API is largely unchanged — `@mcp.tool()` still works exactly as before. What changed is everything underneath: a provider/transform architecture that makes FastMCP extensible, observable, and composable in ways v2 couldn’t support. If we did our jobs right, you’ll barely notice the redesign. You’ll just notice that more is possible.This is also the release where FastMCP moves from
###
[​](https://gofastmcp.com/changelog#build-servers-from-anything)
Build servers from anything
🔌 Components no longer have to live in one file with one server. `FileSystemProvider` discovers tools from directories with hot-reload. `OpenAPIProvider` wraps REST APIs. `ProxyProvider` proxies remote MCP servers. `SkillsProvider` delivers agent skills as resources. Write your own provider for whatever source makes sense. Compose multiple providers into one server, share one across many, or chain them with **transforms** that rename, namespace, filter, version, and secure components as they flow to clients. `ResourcesAsTools` and `PromptsAsTools` expose non-tool components to tool-only clients.
###
[​](https://gofastmcp.com/changelog#ship-to-production)
Ship to production
🔐 Component versioning: serve `@tool(version="2.0")` alongside older versions from one codebase. Granular authorization on individual components with async auth checks, server-wide policies via `AuthMiddleware`, and scope-based access control. OAuth gets CIMD, Static Client Registration, Azure OBO via dependency injection, JWT audience validation, and confused-deputy protections. OpenTelemetry tracing with MCP semantic conventions. Response size limiting. Background tasks with distributed Redis notification and `ctx.elicit()` relay. Security fixes include dropping `diskcache` (CVE-2025-69872) and upgrading `python-multipart` and `protobuf` for additional CVEs.
###
[​](https://gofastmcp.com/changelog#adapt-per-session)
Adapt per session
💾 Session state persists across requests via `ctx.set_state()` / `ctx.get_state()`. `ctx.enable_components()` and `ctx.disable_components()` let servers adapt dynamically per client — show admin tools after authentication, progressively reveal capabilities, or scope access by role.
###
[​](https://gofastmcp.com/changelog#develop-faster)
Develop faster
⚡ `--reload` auto-restarts on file changes. Standalone decorators return the original function, so decorated tools stay callable in tests and non-MCP contexts. Sync functions auto-dispatch to a threadpool. Tool timeouts, MCP-compliant pagination, composable lifespans, `PingMiddleware` for keepalive, and concurrent tool execution when the LLM returns multiple calls in one response.
###
[​](https://gofastmcp.com/changelog#use-fastmcp-as-a-cli)
Use FastMCP as a CLI
🖥️ `fastmcp list` and `fastmcp call` query and invoke tools on any server from a terminal. `fastmcp discover` scans your editor configs (Claude Desktop, Cursor, Goose, Gemini CLI) and finds configured servers by name. `fastmcp generate-cli` writes a standalone typed CLI where every tool is a subcommand. `fastmcp install` registers your server with Claude Desktop, Cursor, or Goose in one command.
###
[​](https://gofastmcp.com/changelog#build-apps-3-1-preview)
Build apps (3.1 preview)
📱 Spec-level support for MCP Apps is in: `ui://` resource scheme, typed UI metadata via `AppConfig`, extension negotiation, and runtime detection. The full Apps experience lands in 3.1.
* * *
If you hit 3.0 because you didn’t pin your dependencies and something breaks — the [upgrade guides](https://gofastmcp.com/getting-started/upgrading/from-fastmcp-2) will get you sorted. We minimized breaking changes, but a major version is a major version.
Copy
```
pip install fastmcp -U

```

📖 [Documentation](https://gofastmcp.com) 🚀 [Upgrade from FastMCP v2](https://gofastmcp.com/getting-started/upgrading/from-fastmcp-2) 🔀 [Upgrade from MCP Python SDK](https://gofastmcp.com/getting-started/upgrading/from-mcp-sdk)
