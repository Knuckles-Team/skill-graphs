Tooltip - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Tooltip Copy Page Previous Next A popup that displays information related to an element when the element receives keyboard focus or the mouse hovers over it. Radix UI Base UI Radix UI Hover Copy import { Button } from "@/components/ui/button"
 import {
 Tooltip, View Code
 Installation #
 Command Manual Run the following command: pnpm npm yarn bun pnpm dlx shadcn@latest add tooltip Copy Add the TooltipProvider to the root of your app. app/layout.tsx Copy import { TooltipProvider } from &quot;@/components/ui/tooltip&quot;

 export default function RootLayout ({ children }) {
 return (
 &lt; html lang = &quot;en&quot; &gt;
 &lt; body &gt;
 &lt; TooltipProvider &gt; { children } &lt;/ TooltipProvider &gt;
 &lt;/ body &gt;
 &lt;/ html &gt;
 )
 }
 Usage #
 Copy import {
 Tooltip,
 TooltipContent,
 TooltipTrigger,
 } from &quot;@/components/ui/tooltip&quot;
 Copy &lt; Tooltip &gt;
 &lt; TooltipTrigger &gt;Hover&lt;/ TooltipTrigger &gt;
 &lt; TooltipContent &gt;
 &lt; p &gt;Add to library&lt;/ p &gt;
 &lt;/ TooltipContent &gt;
 &lt;/ Tooltip &gt;
 Composition #
 Use the following composition to build a Tooltip :
 Copy Tooltip
 ├── TooltipTrigger
 └── TooltipContent
 Examples #
 Side #
 Use the side prop to change the position of the tooltip.
 left top bottom right Copy import { Button } from "@/components/ui/button"
 import {
 Tooltip, View Code
 With Keyboard Shortcut #
 Copy import { SaveIcon } from "lucide-react"

 import { Button } from "@/components/ui/button" View Code
 Disabled Button #
 Show a tooltip on a disabled button by wrapping it with a span.
 Disabled Copy import { Button } from "@/components/ui/button"
 import {
 Tooltip, View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle يسار أعلى أسفل يمين Copy "use client"

 import { View Code
 API Reference #
 See the Radix Tooltip documentation. Toggle Group Typography On This Page Installation Usage Composition Examples Side With Keyboard Shortcut Disabled Button RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
