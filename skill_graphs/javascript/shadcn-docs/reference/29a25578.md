Checkbox - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Checkbox Copy Page Previous Next A control that allows the user to toggle between checked and not checked. Radix UI Base UI Radix UI Accept terms and conditions Accept terms and conditions By clicking this checkbox, you agree to the terms. Enable notifications Enable notifications You can enable or disable notifications at any time. Copy "use client"

 import { Checkbox } from "@/components/ui/checkbox" View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add checkbox Copy
 Usage #
 Copy import { Checkbox } from &quot;@/components/ui/checkbox&quot;
 Copy &lt; Checkbox /&gt;
 Checked State #
 Use defaultChecked for uncontrolled checkboxes, or checked and
 onCheckedChange to control the state.
 Copy import * as React from &quot;react&quot;

 export function Example () {
 const [ checked , setChecked ] = React. useState ( false )

 return &lt; Checkbox checked = { checked } onCheckedChange = { setChecked } /&gt;
 }
 Invalid State #
 Set aria-invalid on the checkbox and data-invalid on the field wrapper to
show the invalid styles.
 Accept terms and conditions Copy import { Checkbox } from "@/components/ui/checkbox"
 import { Field, FieldGroup, FieldLabel } from "@/components/ui/field"
 View Code
 Examples #
 Basic #
 Pair the checkbox with Field and FieldLabel for proper layout and labeling.
 Accept terms and conditions Copy import { Checkbox } from "@/components/ui/checkbox"
 import { Field, FieldGroup, FieldLabel } from "@/components/ui/field"
 View Code
 Description #
 Use FieldContent and FieldDescription for helper text.
 Accept terms and conditions By clicking this checkbox, you agree to the terms and conditions. Copy import { Checkbox } from "@/components/ui/checkbox"
 import {
 Field, View Code
 Disabled #
 Use the disabled prop to prevent interaction and add the data-disabled attribute to the &lt;Field&gt; component for disabled styles.
 Enable notifications Copy import { Checkbox } from "@/components/ui/checkbox"
 import { Field, FieldGroup, FieldLabel } from "@/components/ui/field"
 View Code
 Group #
 Use multiple fields to create a checkbox list.
 Show these items on the desktop: Select the items you want to show on the desktop. Hard disks External disks CDs, DVDs, and iPods Connected servers Copy import { Checkbox } from "@/components/ui/checkbox"
 import {
 Field, View Code
 Table #
 Name Email Role Sarah Chen sarah.chen@example.com Admin Marcus Rodriguez marcus.rodriguez@example.com User Priya Patel priya.patel@example.com User David Kim david.kim@example.com Editor Copy "use client"

 import * as React from "react" View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle قبول الشروط والأحكام قبول الشروط والأحكام بالنقر على هذا المربع، فإنك توافق على الشروط. تفعيل الإشعارات تفعيل الإشعارات يمكنك تفعيل أو إلغاء تفعيل الإشعارات في أي وقت. Copy "use client"

 import * as React from "react" View Code
 API Reference #
 See the Radix UI documentation for more information. Chart Collapsible On This Page Installation Usage Checked State Invalid State Examples Basic Description Disabled Group Table RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
