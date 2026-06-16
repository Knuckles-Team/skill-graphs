Dialog - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Dialog Copy Page Previous Next A window overlaid on either the primary window or another dialog window, rendering the content underneath inert. Radix UI Base UI Radix UI Open Dialog Copy import { Button } from "@/components/ui/button"
 import {
 Dialog, View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add dialog Copy
 Usage #
 Copy import {
 Dialog,
 DialogContent,
 DialogDescription,
 DialogHeader,
 DialogTitle,
 DialogTrigger,
 } from &quot;@/components/ui/dialog&quot;
 Copy &lt; Dialog &gt;
 &lt; DialogTrigger &gt;Open&lt;/ DialogTrigger &gt;
 &lt; DialogContent &gt;
 &lt; DialogHeader &gt;
 &lt; DialogTitle &gt;Are you absolutely sure?&lt;/ DialogTitle &gt;
 &lt; DialogDescription &gt;
 This action cannot be undone. This will permanently delete your account
 and remove your data from our servers.
 &lt;/ DialogDescription &gt;
 &lt;/ DialogHeader &gt;
 &lt;/ DialogContent &gt;
 &lt;/ Dialog &gt;
 Composition #
 Use the following composition to build a Dialog :
 Copy Dialog
 ├── DialogTrigger
 └── DialogContent
 ├── DialogHeader
 │ ├── DialogTitle
 │ └── DialogDescription
 └── DialogFooter
 Examples #
 Custom Close Button #
 Replace the default close control with your own button.
 Share Copy import { Button } from "@/components/ui/button"
 import {
 Dialog, View Code
 No Close Button #
 Use showCloseButton={false} to hide the close button.
 No Close Button Copy import { Button } from "@/components/ui/button"
 import {
 Dialog, View Code
 Sticky Footer #
 Keep actions visible while the content scrolls.
 Sticky Footer Copy import { Button } from "@/components/ui/button"
 import {
 Dialog, View Code
 Scrollable Content #
 Long content can scroll while the header stays in view.
 Scrollable Content Copy import { Button } from "@/components/ui/button"
 import {
 Dialog, View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle فتح الحوار Copy "use client"

 import { View Code
 API Reference #
 See the Radix UI documentation for more information. Date Picker Direction On This Page Installation Usage Composition Examples Custom Close Button No Close Button Sticky Footer Scrollable Content RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
