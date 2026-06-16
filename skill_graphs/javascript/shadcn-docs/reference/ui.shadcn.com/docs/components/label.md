Label - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Label Copy Page Previous Next Renders an accessible label associated with controls. Radix UI Base UI Radix UI Accept terms and conditions Copy import { Checkbox } from "@/components/ui/checkbox"
 import { Label } from "@/components/ui/label"
 View Code
 For form fields, use the Field component which
includes built-in label, description, and error handling.
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add label Copy
 Usage #
 Copy import { Label } from &quot;@/components/ui/label&quot;
 Copy &lt; Label htmlFor = &quot;email&quot; &gt;Your email address&lt;/ Label &gt;
 Label in Field #
 For form fields, use the Field component which
includes built-in FieldLabel , FieldDescription , and FieldError components.
 Copy &lt; Field &gt;
 &lt; FieldLabel htmlFor = &quot;email&quot; &gt;Your email address&lt;/ FieldLabel &gt;
 &lt; Input id = &quot;email&quot; /&gt;
 &lt;/ Field &gt;
 Payment Method All transactions are secure and encrypted Name on Card Card Number Enter your 16-digit card number Month MM Year YYYY CVV Billing Address The billing address associated with your payment method Same as shipping address Comments Submit Cancel Copy import { Button } from "@/components/ui/button"
 import { Checkbox } from "@/components/ui/checkbox"
 import { View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle قبول الشروط والأحكام Copy "use client"

 import * as React from "react" View Code
 API Reference #
 See the Radix UI Label documentation for more information. Kbd Menubar On This Page Installation Usage Label in Field RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
