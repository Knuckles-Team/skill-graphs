Input - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Input Copy Page Previous Next A text input component for forms and user data entry with built-in styling and accessibility features. Radix UI Base UI Radix UI API Key Your API key is encrypted and stored securely. Copy import {
 Field,
 FieldDescription, View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add input Copy
 Usage #
 Copy import { Input } from &quot;@/components/ui/input&quot;
 Copy &lt; Input /&gt;
 Examples #
 Basic #
 Copy import { Input } from "@/components/ui/input"

 export function InputBasic () { View Code
 Field #
 Use Field , FieldLabel , and FieldDescription to create an input with a
label and description.
 Username Choose a unique username for your account. Copy import {
 Field,
 FieldDescription, View Code
 Field Group #
 Use FieldGroup to show multiple Field blocks and to build forms.
 Name Email We&#x27;ll send updates to this address. Reset Submit Copy import { Button } from "@/components/ui/button"
 import {
 Field, View Code
 Disabled #
 Use the disabled prop to disable the input. To style the disabled state, add the data-disabled attribute to the Field component.
 Email This field is currently disabled. Copy import {
 Field,
 FieldDescription, View Code
 Invalid #
 Use the aria-invalid prop to mark the input as invalid. To style the invalid state, add the data-invalid attribute to the Field component.
 Invalid Input This field contains validation errors. Copy import {
 Field,
 FieldDescription, View Code
 File #
 Use the type=&quot;file&quot; prop to create a file input.
 Picture Select a picture to upload. Copy import {
 Field,
 FieldDescription, View Code
 Inline #
 Use Field with orientation=&quot;horizontal&quot; to create an inline input.
Pair with Button to create a search input with a button.
 Search Copy import { Button } from "@/components/ui/button"
 import { Field } from "@/components/ui/field"
 import { Input } from "@/components/ui/input" View Code
 Grid #
 Use a grid layout to place multiple inputs side by side.
 First Name Last Name Copy import { Field, FieldGroup, FieldLabel } from "@/components/ui/field"
 import { Input } from "@/components/ui/input"
 View Code
 Required #
 Use the required attribute to indicate required inputs.
 Required Field * This field must be filled out. Copy import {
 Field,
 FieldDescription, View Code
 Badge #
 Use Badge in the label to highlight a recommended field.
 Webhook URL Beta Copy import { Badge } from "@/components/ui/badge"
 import { Field, FieldLabel } from "@/components/ui/field"
 import { Input } from "@/components/ui/input" View Code
 Input Group #
 To add icons, text, or buttons inside an input, use the InputGroup component. See the Input Group component for more examples.
 Website URL https:// Copy import { InfoIcon } from "lucide-react"

 import { Field, FieldLabel } from "@/components/ui/field" View Code
 Button Group #
 To add buttons to an input, use the ButtonGroup component. See the Button Group component for more examples.
 Search Search Copy import { Button } from "@/components/ui/button"
 import { ButtonGroup } from "@/components/ui/button-group"
 import { Field, FieldLabel } from "@/components/ui/field" View Code
 Form #
 A full form example with multiple inputs, a select, and a button.
 Name Email We&#x27;ll never share your email with anyone. Phone Country Address Cancel Submit Copy import { Button } from "@/components/ui/button"
 import {
 Field, View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle مفتاح API مفتاح API الخاص بك مشفر ومخزن بأمان. Copy "use client"

 import * as React from "react" View Code Hover Card Input Group On This Page Installation Usage Examples Basic Field Field Group Disabled Invalid File Inline Grid Required Badge Input Group Button Group Form RTL Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
