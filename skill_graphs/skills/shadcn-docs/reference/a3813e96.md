Field - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Field Copy Page Previous Next Combine labels, controls, and help text to compose accessible form fields and grouped inputs. Radix UI Base UI Radix UI Payment Method All transactions are secure and encrypted Name on Card Card Number Enter your 16-digit card number Month MM Year YYYY CVV Billing Address The billing address associated with your payment method Same as shipping address Comments Submit Cancel Copy import { Button } from "@/components/ui/button"
 import { Checkbox } from "@/components/ui/checkbox"
 import { View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add field Copy
 Usage #
 Copy import {
 Field,
 FieldContent,
 FieldDescription,
 FieldError,
 FieldGroup,
 FieldLabel,
 FieldLegend,
 FieldSeparator,
 FieldSet,
 FieldTitle,
 } from &quot;@/components/ui/field&quot;
 Copy &lt; FieldSet &gt;
 &lt; FieldLegend &gt;Profile&lt;/ FieldLegend &gt;
 &lt; FieldDescription &gt;This appears on invoices and emails.&lt;/ FieldDescription &gt;
 &lt; FieldGroup &gt;
 &lt; Field &gt;
 &lt; FieldLabel htmlFor = &quot;name&quot; &gt;Full name&lt;/ FieldLabel &gt;
 &lt; Input id = &quot;name&quot; autoComplete = &quot;off&quot; placeholder = &quot;Evil Rabbit&quot; /&gt;
 &lt; FieldDescription &gt;This appears on invoices and emails.&lt;/ FieldDescription &gt;
 &lt;/ Field &gt;
 &lt; Field &gt;
 &lt; FieldLabel htmlFor = &quot;username&quot; &gt;Username&lt;/ FieldLabel &gt;
 &lt; Input id = &quot;username&quot; autoComplete = &quot;off&quot; aria-invalid /&gt;
 &lt; FieldError &gt;Choose another username.&lt;/ FieldError &gt;
 &lt;/ Field &gt;
 &lt; Field orientation = &quot;horizontal&quot; &gt;
 &lt; Switch id = &quot;newsletter&quot; /&gt;
 &lt; FieldLabel htmlFor = &quot;newsletter&quot; &gt;Subscribe to the newsletter&lt;/ FieldLabel &gt;
 &lt;/ Field &gt;
 &lt;/ FieldGroup &gt;
 &lt;/ FieldSet &gt;
 Composition #
 Field #
 A single control with label, helper text, and validation.
 Copy Field
 ├── FieldLabel
 ├── Input / Textarea / Switch / Select
 ├── FieldDescription
 └── FieldError
 FieldGroup #
 Related fields in one group. Use FieldSeparator between sections when needed.
 Copy FieldGroup
 ├── Field
 │ ├── FieldLabel
 │ ├── Input / Textarea / Switch / Select
 │ ├── FieldDescription
 │ └── FieldError
 ├── FieldSeparator
 └── Field
 ├── FieldLabel
 └── Input / Textarea / Switch / Select
 FieldSet #
 Semantic grouping with a legend and description, usually containing a FieldGroup .
 Copy FieldSet
 ├── FieldLegend
 ├── FieldDescription
 └── FieldGroup
 ├── Field
 │ ├── FieldLabel
 │ ├── Input / Textarea / Switch / Select
 │ ├── FieldDescription
 │ └── FieldError
 └── Field
 ├── FieldLabel
 └── Input / Textarea / Switch / Select
 Anatomy #
 The Field family is designed for composing accessible forms. A typical field is structured as follows:
 Copy &lt; Field &gt;
 &lt; FieldLabel htmlFor = &quot;input-id&quot; &gt;Label&lt;/ FieldLabel &gt;
 { /* Input, Select, Switch, etc. */ }
 &lt; FieldDescription &gt;Optional helper text.&lt;/ FieldDescription &gt;
 &lt; FieldError &gt;Validation message.&lt;/ FieldError &gt;
 &lt;/ Field &gt;

 Field is the core wrapper for a single field.
 FieldContent is a flex column that groups label and description. Not required if you have no description.
 Wrap related fields with FieldGroup , and use FieldSet with FieldLegend for semantic grouping.

 Form #
 See the Form documentation for building forms with the Field component and React Hook Form , Tanstack Form , or Formisch .
 Examples #
 Input #
 Username Choose a unique username for your account. Password Must be at least 8 characters long. Copy import {
 Field,
 FieldDescription, View Code
 Textarea #
 Feedback Share your thoughts about our service. Copy import {
 Field,
 FieldDescription, View Code
 Select #
 Department Choose department Select your department or area of work. Copy import {
 Field,
 FieldDescription, View Code
 Slider #
 Price Range Set your budget range ($ 200 - 800 ). Copy "use client"

 import * as React from "react" View Code
 Fieldset #
 Address Information We need your address to deliver your order. Street Address City Postal Code Copy import {
 Field,
 FieldDescription, View Code
 Checkbox #
 Show these items on the desktop Select the items you want to show on the desktop. Hard disks External disks CDs, DVDs, and iPods Connected servers Sync Desktop &amp; Documents folders Your Desktop &amp; Documents folders are being synced with iCloud Drive. You can access them from other devices. Copy import { Checkbox } from "@/components/ui/checkbox"
 import {
 Field, View Code
 Radio #
 Subscription Plan Yearly and lifetime plans offer significant savings. Monthly ($9.99/month) Yearly ($99.99/year) Lifetime ($299.99) Copy import {
 Field,
 FieldDescription, View Code
 Switch #
 Multi-factor authentication Copy import { Field, FieldLabel } from "@/components/ui/field"
 import { Switch } from "@/components/ui/switch"
 View Code
 Choice Card #
 Wrap Field components inside FieldLabel to create selectable field groups. This works with RadioItem , Checkbox and Switch components.
 Compute Environment Select the compute environment for your cluster. Kubernetes Run GPU workloads on a K8s cluster. Virtual Machine Access a cluster to run GPU workloads. Copy import {
 Field,
 FieldContent, View Code
 Field Group #
 Stack Field components with FieldGroup . Add FieldSeparator to divide them.
 Responses Get notified when ChatGPT responds to requests that take time, like research or image generation. Push notifications Tasks Get notified when tasks you&#x27;ve created have updates. Manage tasks Push notifications Email notifications Copy import { Checkbox } from "@/components/ui/checkbox"
 import {
 Field, View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle طريقة الدفع جميع المعاملات آمنة ومشفرة الاسم على البطاقة رقم البطاقة أدخل رقم البطاقة المكون من 16 رقمًا الشهر السنة CVV عنوان الفوترة عنوان الفوترة المرتبط بطريقة الدفع الخاصة بك نفس عنوان الشحن تعليقات إرسال إلغاء Copy "use client"

 import { View Code
 Responsive Layout #

 Vertical fields: Default orientation stacks label, control, and helper text—ideal for mobile-first layouts.
 Horizontal fields: Set orientation=&quot;horizontal&quot; on Field to align the label and control side-by-side. Pair with FieldContent to keep descriptions aligned.
 Responsive fields: Set orientation=&quot;responsive&quot; for automatic column layouts inside container-aware parents. Apply @container/field-group classes on FieldGroup to switch orientations at specific breakpoints.

 Profile Fill in your profile information. Name Provide your full name for identification Submit Cancel Copy import { Button } from "@/components/ui/button"
 import {
 Field, View Code
 Validation and Errors #

 Add data-invalid to Field to switch the entire block into an error state.
 Add aria-invalid on the input itself for assistive technologies.
 Render FieldError immediately after the control or inside FieldContent to keep error messages aligned with the field.

 Copy &lt; Field data-invalid &gt;
 &lt; FieldLabel htmlFor = &quot;email&quot; &gt;Email&lt;/ FieldLabel &gt;
 &lt; Input id = &quot;email&quot; type = &quot;email&quot; aria-invalid /&gt;
 &lt; FieldError &gt;Enter a valid email address.&lt;/ FieldError &gt;
 &lt;/ Field &gt;
 Accessibility #

 FieldSet and FieldLegend keep related controls grouped for keyboard and assistive tech users.
 Field outputs role=&quot;group&quot; so nested controls inherit labeling from FieldLabel and FieldLegend when combined.
 Apply FieldSeparator sparingly to ensure screen readers encounter clear section boundaries.

 API Reference #
 FieldSet #
 Container that renders a semantic fieldset with spacing presets.
 Prop Type Default className string
 Copy &lt; FieldSet &gt;
 &lt; FieldLegend &gt;Delivery&lt;/ FieldLegend &gt;
 &lt; FieldGroup &gt; { /* Fields */ } &lt;/ FieldGroup &gt;
 &lt;/ FieldSet &gt;
 FieldLegend #
 Legend element for a FieldSet . Switch to the label variant to align with label sizing.
 Prop Type Default variant &quot;legend&quot; | &quot;label&quot; &quot;legend&quot; className string
 Copy &lt; FieldLegend variant = &quot;label&quot; &gt;Notification Preferences&lt;/ FieldLegend &gt;
 The FieldLegend has two variants: legend and label . The label variant applies label sizing and alignment. Handy if you have nested FieldSet .
 FieldGroup #
 Layout wrapper that stacks Field components and enables container queries for responsive orientations.
 Prop Type Default className string
 Copy &lt; FieldGroup className = &quot;@container/field-group flex flex-col gap-6&quot; &gt;
 &lt; Field &gt; { /* ... */ } &lt;/ Field &gt;
 &lt; Field &gt; { /* ... */ } &lt;/ Field &gt;
 &lt;/ FieldGroup &gt;
 Field #
 The core wrapper for a single field. Provides orientation control, invalid state styling, and spacing.
 Prop Type Default orientation &quot;vertical&quot; | &quot;horizontal&quot; | &quot;responsive&quot; &quot;vertical&quot; className string data-invalid boolean
 Copy &lt; Field orientation = &quot;horizontal&quot; &gt;
 &lt; FieldLabel htmlFor = &quot;remember&quot; &gt;Remember me&lt;/ FieldLabel &gt;
 &lt; Switch id = &quot;remember&quot; /&gt;
 &lt;/ Field &gt;
 FieldContent #
 Flex column that groups control and descriptions when the label sits beside the control. Not required if you have no description.
 Prop Type Default className string
 Copy &lt; Field &gt;
 &lt; Checkbox id = &quot;notifications&quot; /&gt;
 &lt; FieldContent &gt;
 &lt; FieldLabel htmlFor = &quot;notifications&quot; &gt;Notifications&lt;/ FieldLabel &gt;
 &lt; FieldDescription &gt;Email, SMS, and push options.&lt;/ FieldDescription &gt;
 &lt;/ FieldContent &gt;
 &lt;/ Field &gt;
 FieldLabel #
 Label styled for both direct inputs and nested Field children.
 Prop Type Default className string asChild boolean false
 Copy &lt; FieldLabel htmlFor = &quot;email&quot; &gt;Email&lt;/ FieldLabel &gt;
 FieldTitle #
 Renders a title with label styling inside FieldContent .
 Prop Type Default className string
 Copy &lt; FieldContent &gt;
 &lt; FieldTitle &gt;Enable Touch ID&lt;/ FieldTitle &gt;
 &lt; FieldDescription &gt;Unlock your device faster.&lt;/ FieldDescription &gt;
 &lt;/ FieldContent &gt;
 FieldDescription #
 Helper text slot that automatically balances long lines in horizontal layouts.
 Prop Type Default className string
 Copy &lt; FieldDescription &gt;We never share your email with anyone.&lt;/ FieldDescription &gt;
 FieldSeparator #
 Visual divider to separate sections inside a FieldGroup . Accepts optional inline content.
 Prop Type Default className string
 Copy &lt; FieldSeparator &gt;Or continue with&lt;/ FieldSeparator &gt;
 FieldError #
 Accessible error container that accepts children or an errors array (e.g., from react-hook-form ).
 Prop Type Default errors Array&lt;{ message?: string } | undefined&gt; className string
 Copy &lt; FieldError errors = { errors.username } /&gt;
 When the errors array contains multiple messages, the component renders a list automatically.
 FieldError also accepts issues produced by any validator that implements Standard Schema , including Zod, Valibot, and ArkType. Pass the issues array from the schema result directly to render a unified error list across libraries. Empty Hover Card On This Page Installation Usage Composition Field FieldGroup FieldSet Anatomy Form Examples Input Textarea Select Slider Fieldset Checkbox Radio Switch Choice Card Field Group RTL Responsive Layout Validation and Errors Accessibility API Reference FieldSet FieldLegend FieldGroup Field FieldContent FieldLabel FieldTitle FieldDescription FieldSeparator FieldError Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
