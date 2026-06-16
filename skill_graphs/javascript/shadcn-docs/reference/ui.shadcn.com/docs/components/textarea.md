Textarea - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Textarea Copy Page Previous Next Displays a form textarea or a component that looks like a textarea. Radix UI Base UI Radix UI Copy import { Textarea } from "@/components/ui/textarea"

 export function TextareaDemo () { View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add textarea Copy
 Usage #
 Copy import { Textarea } from &quot;@/components/ui/textarea&quot;
 Copy &lt; Textarea /&gt;
 Examples #
 Field #
 Use Field , FieldLabel , and FieldDescription to create a textarea with a label and description.
 Message Enter your message below. Copy import {
 Field,
 FieldDescription, View Code
 Disabled #
 Use the disabled prop to disable the textarea. To style the disabled state, add the data-disabled attribute to the Field component.
 Message Copy import { Field, FieldLabel } from "@/components/ui/field"
 import { Textarea } from "@/components/ui/textarea"
 View Code
 Invalid #
 Use the aria-invalid prop to mark the textarea as invalid. To style the invalid state, add the data-invalid attribute to the Field component.
 Message Please enter a valid message. Copy import {
 Field,
 FieldDescription, View Code
 Button #
 Pair with Button to create a textarea with a submit button.
 Send message Copy import { Button } from "@/components/ui/button"
 import { Textarea } from "@/components/ui/textarea"
 View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle التعليقات شاركنا أفكارك حول خدمتنا. Copy "use client"

 import * as React from "react" View Code Tabs Toast On This Page Installation Usage Examples Field Disabled Invalid Button RTL Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
