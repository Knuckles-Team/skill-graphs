Spinner - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Spinner Copy Page Previous Next An indicator that can be used to show a loading state. Radix UI Base UI Radix UI Processing payment... $100.00 Copy import {
 Item,
 ItemContent, View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add spinner Copy
 Usage #
 Copy import { Spinner } from &quot;@/components/ui/spinner&quot;
 Copy &lt; Spinner /&gt;
 Customization #
 You can replace the default spinner icon with any other icon by editing the Spinner component.
 Copy import { LoaderIcon } from "lucide-react"

 import { cn } from "@/lib/utils" View Code
 components/ui/spinner.tsx Copy import { LoaderIcon } from &quot;lucide-react&quot;

 import { cn } from &quot;@/lib/utils&quot;

 function Spinner ({ className , ... props } : React . ComponentProps &lt; &quot;svg&quot; &gt;) {
 return (
 &lt; LoaderIcon
 role = &quot;status&quot;
 aria-label = &quot;Loading&quot;
 className = { cn ( &quot;size-4 animate-spin&quot; , className) }
 { ... props }
 /&gt;
 )
 }

 export { Spinner }
 Examples #
 Size #
 Use the size-* utility class to change the size of the spinner.
 Copy import { Spinner } from "@/components/ui/spinner"

 export function SpinnerSize () { View Code
 Button #
 Add a spinner to a button to indicate a loading state. Place the &lt;Spinner /&gt; before the label with data-icon=&quot;inline-start&quot; for a start position, or after the label with data-icon=&quot;inline-end&quot; for an end position.
 Loading... Please wait Processing Copy import { Button } from "@/components/ui/button"
 import { Spinner } from "@/components/ui/spinner"
 View Code
 Badge #
 Add a spinner to a badge to indicate a loading state. Place the &lt;Spinner /&gt; before the label with data-icon=&quot;inline-start&quot; for a start position, or after the label with data-icon=&quot;inline-end&quot; for an end position.
 Syncing Updating Processing Copy import { Badge } from "@/components/ui/badge"
 import { Spinner } from "@/components/ui/spinner"
 View Code
 Input Group #
 Validating... Send Copy import { ArrowUpIcon } from "lucide-react"

 import { View Code
 Empty #
 Processing your request Please wait while we process your request. Do not refresh the page. Cancel Copy import { Button } from "@/components/ui/button"
 import {
 Empty, View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle جاري معالجة الدفع... ١٠٠.٠٠ دولار Copy "use client"

 import * as React from "react" View Code Sonner Switch On This Page Installation Usage Customization Examples Size Button Badge Input Group Empty RTL Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
