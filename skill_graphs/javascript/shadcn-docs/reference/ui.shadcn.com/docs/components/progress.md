Progress - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Progress Copy Page Previous Next Displays an indicator showing the completion progress of a task, typically displayed as a progress bar. Radix UI Base UI Radix UI Copy "use client"

 import * as React from "react" View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add progress Copy
 Usage #
 Copy import { Progress } from &quot;@/components/ui/progress&quot;
 Copy &lt; Progress value = { 33 } /&gt;
 Examples #
 Label #
 Use a Field component to add a label to the progress bar.
 Upload progress 66% Copy import { Field, FieldLabel } from "@/components/ui/field"
 import { Progress } from "@/components/ui/progress"
 View Code
 Controlled #
 A progress bar that can be controlled by a slider.
 Copy "use client"

 import * as React from "react" View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle تقدم الرفع ٦٦ % Copy "use client"

 import * as React from "react" View Code
 API Reference #
 See the Radix UI Progress documentation. Popover Radio Group On This Page Installation Usage Examples Label Controlled RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
