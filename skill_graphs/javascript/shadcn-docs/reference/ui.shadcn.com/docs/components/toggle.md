Toggle - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Toggle Copy Page Previous Next A two-state button that can be either on or off. Radix UI Base UI Radix UI Bookmark Copy import { BookmarkIcon } from "lucide-react"

 import { Toggle } from "@/components/ui/toggle" View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add toggle Copy
 Usage #
 Copy import { Toggle } from &quot;@/components/ui/toggle&quot;
 Copy &lt; Toggle &gt;Toggle&lt;/ Toggle &gt;
 Examples #
 Outline #
 Use variant=&quot;outline&quot; for an outline style.
 Italic Bold Copy import { BoldIcon, ItalicIcon } from "lucide-react"

 import { Toggle } from "@/components/ui/toggle" View Code
 With Text #
 Italic Copy import { ItalicIcon } from "lucide-react"

 import { Toggle } from "@/components/ui/toggle" View Code
 Size #
 Use the size prop to change the size of the toggle.
 Small Default Large Copy import { Toggle } from "@/components/ui/toggle"

 export function ToggleSizes () { View Code
 Disabled #
 Disabled Disabled Copy import { Toggle } from "@/components/ui/toggle"

 export function ToggleDisabled () { View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle إشارة مرجعية Copy "use client"

 import * as React from "react" View Code
 API Reference #
 See the Radix Toggle documentation. Toast Toggle Group On This Page Installation Usage Examples Outline With Text Size Disabled RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
