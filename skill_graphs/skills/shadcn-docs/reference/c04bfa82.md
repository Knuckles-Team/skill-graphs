Select - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Select Copy Page Previous Next Displays a list of options for the user to pick from—triggered by a button. Radix UI Base UI Radix UI Select a fruit Copy import {
 Select,
 SelectContent, View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add select Copy
 Usage #
 Copy import {
 Select,
 SelectContent,
 SelectGroup,
 SelectItem,
 SelectTrigger,
 SelectValue,
 } from &quot;@/components/ui/select&quot;
 Copy &lt; Select &gt;
 &lt; SelectTrigger className = &quot;w-[180px]&quot; &gt;
 &lt; SelectValue placeholder = &quot;Theme&quot; /&gt;
 &lt;/ SelectTrigger &gt;
 &lt; SelectContent &gt;
 &lt; SelectGroup &gt;
 &lt; SelectItem value = &quot;light&quot; &gt;Light&lt;/ SelectItem &gt;
 &lt; SelectItem value = &quot;dark&quot; &gt;Dark&lt;/ SelectItem &gt;
 &lt; SelectItem value = &quot;system&quot; &gt;System&lt;/ SelectItem &gt;
 &lt;/ SelectGroup &gt;
 &lt;/ SelectContent &gt;
 &lt;/ Select &gt;
 Composition #
 Use the following composition to build a Select :
 Copy Select
 ├── SelectTrigger
 │ └── SelectValue
 └── SelectContent
 ├── SelectGroup
 │ ├── SelectLabel
 │ ├── SelectItem
 │ └── SelectItem
 ├── SelectSeparator
 └── SelectGroup
 ├── SelectLabel
 ├── SelectItem
 └── SelectItem
 Examples #
 Align Item With Trigger #
 Use the position prop on SelectContent to control alignment. When position=&quot;item-aligned&quot; (default), the popup positions so the selected item appears over the trigger. When position=&quot;popper&quot; , the popup aligns to the trigger edge.
 Align Item Toggle to align the item with the trigger. Copy "use client"

 import * as React from "react" View Code
 Groups #
 Use SelectGroup , SelectLabel , and SelectSeparator to organize items.
 Select a fruit Copy import {
 Select,
 SelectContent, View Code
 Scrollable #
 A select with many items that scrolls.
 Select a timezone Copy import {
 Select,
 SelectContent, View Code
 Disabled #
 Select a fruit Copy import {
 Select,
 SelectContent, View Code
 Invalid #
 Add the data-invalid attribute to the Field component and the aria-invalid attribute to the SelectTrigger component to show an error state.
 Copy &lt; Field data-invalid &gt;
 &lt; FieldLabel &gt;Fruit&lt;/ FieldLabel &gt;
 &lt; SelectTrigger aria-invalid &gt;
 &lt; SelectValue /&gt;
 &lt;/ SelectTrigger &gt;
 &lt;/ Field &gt;
 Fruit Select a fruit Please select a fruit. Copy import { Field, FieldError, FieldLabel } from "@/components/ui/field"
 import {
 Select, View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle اختر فاكهة Copy "use client"

 import * as React from "react" View Code
 API Reference #
 See the Radix UI Select documentation. Scroll Area Separator On This Page Installation Usage Composition Examples Align Item With Trigger Groups Scrollable Disabled Invalid RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
