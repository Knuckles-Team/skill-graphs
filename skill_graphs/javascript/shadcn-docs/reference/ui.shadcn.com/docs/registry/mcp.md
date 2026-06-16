MCP Server - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json MCP Server Copy Page Previous Next MCP support for registry developers The shadcn MCP server works out of the box with any shadcn-compatible registry. You do not need to do anything special to enable MCP support for your registry.

 Prerequisites #
 The MCP server works by requesting your registry index. Make sure you have a registry item file at the root of your registry named registry .
 For example, if your registry is hosted at https://acme.com/r/[name].json , you should have a file at https://acme.com/r/registry.json or https://acme.com/r/registry if you&#x27;re using a JSON file extension.
 This file must be a valid JSON file that conforms to the registry schema .

 Configuring MCP #
 Ask your registry consumers to configure your registry in their components.json file and install the shadcn MCP server:
 Claude Code Cursor VS Code Codex OpenCode Configure your registry in your components.json file: components.json Copy {
 &quot;registries&quot; : {
 &quot;@acme&quot; : &quot;https://acme.com/r/{name}.json&quot;
 }
 } Run the following command in your project: pnpm npm yarn bun pnpm dlx shadcn@latest mcp init --client claude Copy Restart Claude Code and try the following prompts:
 Show me the components in the acme registry
 Create a landing page using items from the acme registry
 Note: You can use /mcp command in Claude Code to debug the MCP server.
 You can read more about the MCP server in the MCP documentation .

 Best Practices #
 Here are some best practices for MCP-compatible registries:

 Clear Descriptions : Add concise, informative descriptions that help AI assistants understand what a registry item is for and how to use it.
 Proper Dependencies : List all dependencies accurately so MCP can install them automatically.
 Registry Dependencies : Use registryDependencies to indicate relationships between items.
 Consistent Naming : Use kebab-case for component names and maintain consistency across your registry.
 Authentication Open in v0 On This Page Prerequisites Configuring MCP Best Practices Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
