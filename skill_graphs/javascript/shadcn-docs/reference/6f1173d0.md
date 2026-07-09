Command - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Command Copy Page Previous Next Command menu for search and quick actions. Radix UI Base UI Radix UI No results found. Suggestions Calendar Search Emoji Calculator Settings Profile ⌘P Billing ⌘B Settings ⌘S Copy import {
 Calculator,
 Calendar, View Code
 About #
 The &lt;Command /&gt; component uses the cmdk component by Dip .
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add command Copy
 Usage #
 Copy import {
 Command,
 CommandDialog,
 CommandEmpty,
 CommandGroup,
 CommandInput,
 CommandItem,
 CommandList,
 CommandSeparator,
 CommandShortcut,
 } from &quot;@/components/ui/command&quot;
 Copy &lt; Command className = &quot;max-w-sm rounded-lg border&quot; &gt;
 &lt; CommandInput placeholder = &quot;Type a command or search...&quot; /&gt;
 &lt; CommandList &gt;
 &lt; CommandEmpty &gt;No results found.&lt;/ CommandEmpty &gt;
 &lt; CommandGroup heading = &quot;Suggestions&quot; &gt;
 &lt; CommandItem &gt;Calendar&lt;/ CommandItem &gt;
 &lt; CommandItem &gt;Search Emoji&lt;/ CommandItem &gt;
 &lt; CommandItem &gt;Calculator&lt;/ CommandItem &gt;
 &lt;/ CommandGroup &gt;
 &lt; CommandSeparator /&gt;
 &lt; CommandGroup heading = &quot;Settings&quot; &gt;
 &lt; CommandItem &gt;Profile&lt;/ CommandItem &gt;
 &lt; CommandItem &gt;Billing&lt;/ CommandItem &gt;
 &lt; CommandItem &gt;Settings&lt;/ CommandItem &gt;
 &lt;/ CommandGroup &gt;
 &lt;/ CommandList &gt;
 &lt;/ Command &gt;
 Composition #
 Use the following composition to build a Command :
 Copy Command
 ├── CommandInput
 └── CommandList
 ├── CommandEmpty
 ├── CommandGroup
 │ ├── CommandItem
 │ └── CommandItem
 ├── CommandSeparator
 └── CommandGroup
 ├── CommandItem
 └── CommandItem
 Examples #
 Basic #
 A simple command menu in a dialog.
 Open Menu Command Palette Search for a command to run... Copy "use client"

 import * as React from "react" View Code
 Shortcuts #
 Open Menu Command Palette Search for a command to run... Copy "use client"

 import * as React from "react" View Code
 Groups #
 A command menu with groups, icons and separators.
 Open Menu Command Palette Search for a command to run... Copy "use client"

 import * as React from "react" View Code
 Scrollable #
 Scrollable command menu with multiple items.
 Open Menu Command Palette Search for a command to run... Copy "use client"

 import * as React from "react" View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle لم يتم العثور على نتائج. اقتراحات التقويم البحث عن الرموز التعبيرية الآلة الحاسبة الإعدادات الملف الشخصي ⌘P الفوترة ⌘B الإعدادات ⌘S Copy "use client"

 import * as React from "react" View Code
 API Reference #
 See the cmdk documentation for more information. Combobox Context Menu On This Page About Installation Usage Composition Examples Basic Shortcuts Groups Scrollable RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
