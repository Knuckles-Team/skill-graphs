Switch - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Switch Copy Page Previous Next A control that allows the user to toggle between checked and not checked. Radix UI Base UI Radix UI Airplane Mode Copy import { Label } from "@/components/ui/label"
 import { Switch } from "@/components/ui/switch"
 View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add switch Copy
 Usage #
 Copy import { Switch } from &quot;@/components/ui/switch&quot;
 Copy &lt; Switch /&gt;
 Examples #
 Description #
 Share across devices Focus is shared across devices, and turns off when you leave the app. Copy import {
 Field,
 FieldContent, View Code
 Choice Card #
 Card-style selection where FieldLabel wraps the entire Field for a clickable card pattern.
 Share across devices Focus is shared across devices, and turns off when you leave the app. Enable notifications Receive notifications when focus mode is enabled or disabled. Copy import {
 Field,
 FieldContent, View Code
 Disabled #
 Add the disabled prop to the Switch component to disable the switch. Add the data-disabled prop to the Field component for styling.
 Disabled Copy import { Field, FieldLabel } from "@/components/ui/field"
 import { Switch } from "@/components/ui/switch"
 View Code
 Invalid #
 Add the aria-invalid prop to the Switch component to indicate an invalid state. Add the data-invalid prop to the Field component for styling.
 Accept terms and conditions You must accept the terms and conditions to continue. Copy import {
 Field,
 FieldContent, View Code
 Size #
 Use the size prop to change the size of the switch.
 Small Default Copy import { Field, FieldGroup, FieldLabel } from "@/components/ui/field"
 import { Switch } from "@/components/ui/switch"
 View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle المشاركة عبر الأجهزة يتم مشاركة التركيز عبر الأجهزة، ويتم إيقاف تشغيله عند مغادرة التطبيق. Copy "use client"

 import * as React from "react" View Code
 API Reference #
 See the Radix Switch documentation. Spinner Table On This Page Installation Usage Examples Description Choice Card Disabled Invalid Size RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
