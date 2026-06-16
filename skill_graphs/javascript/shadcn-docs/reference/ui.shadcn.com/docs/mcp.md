MCP Server - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json MCP Server Copy Page Previous Next Use the shadcn MCP server to browse, search, and install components from registries. The shadcn MCP Server allows AI assistants to interact with items from registries. You can browse available components, search for specific ones, and install them directly into your project using natural language.
 For example, you can ask an AI assistant to &quot;Build a landing page using components from the acme registry&quot; or &quot;Find me a login form from the shadcn registry&quot;.
 Registries are configured in your project&#x27;s components.json file.
 components.json Copy {
 &quot;registries&quot; : {
 &quot;@acme&quot; : &quot;https://acme.com/r/{name}.json&quot;
 }
 }

 Quick Start #
 Select your MCP client and follow the instructions to configure the shadcn MCP server. If you&#x27;d like to do it manually, see the Configuration section.
 Claude Code Cursor VS Code Codex OpenCode Run the following command in your project: pnpm npm yarn bun pnpm dlx shadcn@latest mcp init --client claude Copy Restart Claude Code and try the following prompts:
 Show me all available components in the shadcn registry
 Add the button, dialog and card components to my project
 Create a contact form using components from the shadcn registry
 Note: You can use /mcp command in Claude Code to debug the MCP server.

 What is MCP? #
 Model Context Protocol (MCP) is an open protocol that enables AI assistants to securely connect to external data sources and tools. With the shadcn MCP server, your AI assistant gains direct access to:

 Browse Components - List all available components, blocks, and templates from any configured registry
 Search Across Registries - Find specific components by name or functionality across multiple sources
 Install with Natural Language - Add components using simple conversational prompts like &quot;add a login form&quot;
 Support for Multiple Registries - Access public registries, private company libraries, and third-party sources

 How It Works #
 The MCP server acts as a bridge between your AI assistant, component registries and the shadcn CLI.

 Registry Connection - MCP connects to configured registries (shadcn/ui, private registries, third-party sources)
 Natural Language - You describe what you need in plain English
 AI Processing - The assistant translates your request into registry commands
 Component Delivery - Resources are fetched and installed in your project

 Supported Registries #
 The shadcn MCP server works out of the box with any shadcn-compatible registry.

 shadcn/ui Registry - The default registry with all shadcn/ui components
 Third-Party Registries - Any registry following the shadcn registry specification
 Private Registries - Your company&#x27;s internal component libraries
 Namespaced Registries - Multiple registries configured with @namespace syntax

 Configuration #
 You can use any MCP client to interact with the shadcn MCP server. Here are the instructions for the most popular ones.
 Claude Code #
 To use the shadcn MCP server with Claude Code, add the following configuration to your project&#x27;s .mcp.json file:
 .mcp.json Copy {
 &quot;mcpServers&quot; : {
 &quot;shadcn&quot; : {
 &quot;command&quot; : &quot;npx&quot; ,
 &quot;args&quot; : [ &quot;shadcn@latest&quot; , &quot;mcp&quot; ]
 }
 }
 }
 After adding the configuration, restart Claude Code and run /mcp to see the shadcn MCP server in the list. If you see Connected , you&#x27;re good to go.
 See the Claude Code MCP documentation for more details.
 Cursor #
 To configure MCP in Cursor, add the shadcn server to your project&#x27;s .cursor/mcp.json configuration file:
 .cursor/mcp.json Copy {
 &quot;mcpServers&quot; : {
 &quot;shadcn&quot; : {
 &quot;command&quot; : &quot;npx&quot; ,
 &quot;args&quot; : [ &quot;shadcn@latest&quot; , &quot;mcp&quot; ]
 }
 }
 }
 After adding the configuration, enable the shadcn MCP server in Cursor Settings.
 Once enabled, you should see a green dot next to the shadcn server in the MCP server list and a list of available tools.
 See the Cursor MCP documentation for more details.
 VS Code #
 To configure MCP in VS Code with GitHub Copilot, add the shadcn server to your project&#x27;s .vscode/mcp.json configuration file:
 .vscode/mcp.json Copy {
 &quot;servers&quot; : {
 &quot;shadcn&quot; : {
 &quot;command&quot; : &quot;npx&quot; ,
 &quot;args&quot; : [ &quot;shadcn@latest&quot; , &quot;mcp&quot; ]
 }
 }
 }
 After adding the configuration, open .vscode/mcp.json and click Start next to the shadcn server.
 See the VS Code MCP documentation for more details.
 Codex #
 Note: The shadcn CLI cannot automatically update ~/.codex/config.toml .
You&#x27;ll need to add the configuration manually.
 To configure MCP in Codex, add the shadcn server to ~/.codex/config.toml :
 ~/.codex/config.toml Copy [ mcp_servers . shadcn ]
 command = &quot;npx&quot;
 args = [ &quot;shadcn@latest&quot; , &quot;mcp&quot; ]
 After adding the configuration, restart Codex to load the MCP server.

 Configuring Registries #
 The MCP server supports multiple registries through your project&#x27;s components.json configuration. This allows you to access components from various sources including private registries and third-party providers.
 Configure additional registries in your components.json :
 components.json Copy {
 &quot;registries&quot; : {
 &quot;@acme&quot; : &quot;https://registry.acme.com/{name}.json&quot; ,
 &quot;@internal&quot; : {
 &quot;url&quot; : &quot;https://internal.company.com/{name}.json&quot; ,
 &quot;headers&quot; : {
 &quot;Authorization&quot; : &quot;Bearer ${REGISTRY_TOKEN}&quot;
 }
 }
 }
 }
 Note: No configuration is needed to access the standard shadcn/ui
registry.

 Authentication #
 For private registries requiring authentication, set environment variables in your .env.local :
 .env.local Copy REGISTRY_TOKEN = your_token_here
 API_KEY = your_api_key_here
 For more details on registry authentication, see the Authentication documentation .

 Example Prompts #
 Once the MCP server is configured, you can use natural language to interact with registries. Try one of the following prompts:
 Browse &amp; Search #

 Show me all available components in the shadcn registry
 Find me a login form from the shadcn registry

 Install Items #

 Add the button component to my project
 Create a login form using shadcn components
 Install the Cursor rules from the acme registry

 Work with Namespaces #

 Show me components from acme registry
 Install @internal/auth-form
 Build me a landing page using hero, features and testimonials sections from the acme registry

 Troubleshooting #
 MCP Not Responding #
 If the MCP server isn&#x27;t responding to prompts:

 Check Configuration - Verify the MCP server is properly configured and enabled in your MCP client
 Restart MCP Client - Restart your MCP client after configuration changes
 Verify Installation - Ensure shadcn is installed in your project
 Check Network - Confirm you can access the configured registries

 Registry Access Issues #
 If components aren&#x27;t loading from registries:

 Check components.json - Verify registry URLs are correct
 Test Authentication - Ensure environment variables are set for private registries
 Verify Registry - Confirm the registry is online and accessible
 Check Namespace - Ensure namespace syntax is correct ( @namespace/component )

 Installation Failures #
 If components fail to install:

 Check Project Setup - Ensure you have a valid components.json file
 Verify Paths - Confirm the target directories exist
 Check Permissions - Ensure write permissions for component directories
 Review Dependencies - Check that required dependencies are installed

 No Tools or Prompts #
 If you see the No tools or prompts message, try the following:

 Clear the npx cache - Run npx clear-npx-cache
 Re-enable the MCP server - Try to re-enable the MCP server in your MCP client
 Check Logs - In Cursor, you can see the logs under View -&gt; Output and select MCP: project-* in the dropdown.

 Learn More #

 Registry Documentation - Complete guide to shadcn registries
 Namespaces - Configure multiple registry sources
 Authentication - Secure your private registries
 MCP Specification - Learn about Model Context Protocol
 Registry Directory Your project is ready! On This Page Quick Start What is MCP? How It Works Supported Registries Configuration Claude Code Cursor VS Code Codex Configuring Registries Authentication Example Prompts Browse &amp; Search Install Items Work with Namespaces Troubleshooting MCP Not Responding Registry Access Issues Installation Failures No Tools or Prompts Learn More Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
