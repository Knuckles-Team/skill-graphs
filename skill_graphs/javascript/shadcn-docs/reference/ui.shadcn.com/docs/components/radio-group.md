Radio Group - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Radio Group Copy Page Previous Next A set of checkable buttons—known as radio buttons—where no more than one of the buttons can be checked at a time. Radix UI Base UI Radix UI Default Comfortable Compact Copy import { Label } from "@/components/ui/label"
 import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
 View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add radio-group Copy
 Usage #
 Copy import { Label } from &quot;@/components/ui/label&quot;
 import { RadioGroup, RadioGroupItem } from &quot;@/components/ui/radio-group&quot;
 Copy &lt; RadioGroup defaultValue = &quot;option-one&quot; &gt;
 &lt; div className = &quot;flex items-center gap-3&quot; &gt;
 &lt; RadioGroupItem value = &quot;option-one&quot; id = &quot;option-one&quot; /&gt;
 &lt; Label htmlFor = &quot;option-one&quot; &gt;Option One&lt;/ Label &gt;
 &lt;/ div &gt;
 &lt; div className = &quot;flex items-center gap-3&quot; &gt;
 &lt; RadioGroupItem value = &quot;option-two&quot; id = &quot;option-two&quot; /&gt;
 &lt; Label htmlFor = &quot;option-two&quot; &gt;Option Two&lt;/ Label &gt;
 &lt;/ div &gt;
 &lt;/ RadioGroup &gt;
 Composition #
 Use the following composition to build a RadioGroup :
 Copy RadioGroup
 ├── RadioGroupItem
 └── RadioGroupItem
 Examples #
 Description #
 Radio group items with a description using the Field component.
 Default Standard spacing for most use cases. Comfortable More space between elements. Compact Minimal spacing for dense layouts. Copy import {
 Field,
 FieldContent, View Code
 Choice Card #
 Use FieldLabel to wrap the entire Field for a clickable card-style selection.
 Plus For individuals and small teams. Pro For growing businesses. Enterprise For large teams and enterprises. Copy import {
 Field,
 FieldContent, View Code
 Fieldset #
 Use FieldSet and FieldLegend to group radio items with a label and description.
 Subscription Plan Yearly and lifetime plans offer significant savings. Monthly ($9.99/month) Yearly ($99.99/year) Lifetime ($299.99) Copy import {
 Field,
 FieldDescription, View Code
 Disabled #
 Use the disabled prop on RadioGroupItem to disable individual items.
 Disabled Option 2 Option 3 Copy import { Field, FieldLabel } from "@/components/ui/field"
 import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
 View Code
 Invalid #
 Use aria-invalid on RadioGroupItem and data-invalid on Field to show validation errors.
 Notification Preferences Choose how you want to receive notifications. Email only SMS only Both Email &amp; SMS Copy import {
 Field,
 FieldDescription, View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle افتراضي تباعد قياسي لمعظم حالات الاستخدام. مريح مساحة أكبر بين العناصر. مضغوط تباعد أدنى للتخطيطات الكثيفة. Copy "use client"

 import * as React from "react" View Code
 API Reference #
 See the Radix UI Radio Group documentation. Progress Resizable On This Page Installation Usage Composition Examples Description Choice Card Fieldset Disabled Invalid RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
