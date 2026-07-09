Skills - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Skills Copy Page Previous Next Give your AI assistant deep knowledge of shadcn/ui components, patterns, and best practices. Skills give AI assistants like Claude Code project-aware context about shadcn/ui. When installed, your AI assistant knows how to find, install, compose, and customize components using the correct APIs and patterns for your project.
 For example, you can ask your AI assistant to:

 &quot;Add a login form with email and password fields.&quot;
 &quot;Create a settings page with a form for updating profile information.&quot;
 &quot;Build a dashboard with a sidebar, stats cards, and a data table.&quot;
 &quot;Switch to --preset [CODE]&quot;
 &quot;Can you add a hero from @tailark?&quot;

 The skill reads your project&#x27;s components.json and provides the assistant with your framework, aliases, installed components, icon library, and base library so it can generate correct code on the first try.

 Install #
 pnpm npm yarn bun pnpm dlx skills add shadcn/ui Copy
 This installs the shadcn skill into your project. Once installed, your AI assistant automatically loads it when working with shadcn/ui components.
 Learn more about skills at skills.sh .

 What&#x27;s Included #
 The skill provides your AI assistant with the following knowledge:
 Project Context #
 On every interaction, the skill runs shadcn info --json to get your project&#x27;s configuration: framework, Tailwind version, aliases, base library ( radix or base ), icon library, installed components, and resolved file paths.
 CLI Commands #
 Full reference for all CLI commands: init , add , search , view , docs , diff , info , and build . Includes flags, dry-run mode, smart merge workflows, presets, and templates.
 Theming and Customization #
 How CSS variables, OKLCH colors, dark mode, custom colors, border radius, and component variants work. Includes guidance for both Tailwind v3 and v4.
 Registry Authoring #
 How to build and publish custom component registries: registry.json format, item types, file objects, dependencies, CSS variables, building, hosting, and user configuration.
 MCP Server #
 Setup and tools for the shadcn MCP server, which lets AI assistants search, browse, and install components from registries.

 How It Works #

 Project detection — The skill activates when it finds a components.json file in your project.
 Context injection — It runs shadcn info --json to read your project configuration and injects the result into the assistant&#x27;s context.
 Pattern enforcement — The assistant follows shadcn/ui composition rules: using FieldGroup for forms, ToggleGroup for option sets, semantic colors, and correct base-specific APIs.
 Component discovery — The assistant uses shadcn docs , shadcn search , or MCP tools to find components and their documentation before generating code.

 Learn More #

 CLI — Full CLI command reference
 MCP Server — Connect the MCP server for registry access
 Theming — CSS variables and customization
 Registry — Building and publishing custom registries
 skills.sh — Learn more about AI skills
 Monorepo JavaScript On This Page Install What&#x27;s Included Project Context CLI Commands Theming and Customization Registry Authoring MCP Server How It Works Learn More Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
