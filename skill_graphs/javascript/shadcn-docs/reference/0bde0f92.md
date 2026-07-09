Alert - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Alert Copy Page Previous Next Displays a callout for user attention. Radix UI Base UI Radix UI Payment successful Your payment of $29.99 has been processed. A receipt has been sent to your email address. New feature available We&#x27;ve added dark mode support. You can enable it in your account settings. Copy import { CheckCircle2Icon, InfoIcon } from "lucide-react"

 import { View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add alert Copy
 Usage #
 Copy import {
 Alert,
 AlertAction,
 AlertDescription,
 AlertTitle,
 } from &quot;@/components/ui/alert&quot;
 Copy &lt; Alert &gt;
 &lt; InfoIcon /&gt;
 &lt; AlertTitle &gt;Heads up!&lt;/ AlertTitle &gt;
 &lt; AlertDescription &gt;
 You can add components and dependencies to your app using the cli.
 &lt;/ AlertDescription &gt;
 &lt; AlertAction &gt;
 &lt; Button variant = &quot;outline&quot; &gt;Enable&lt;/ Button &gt;
 &lt;/ AlertAction &gt;
 &lt;/ Alert &gt;
 Composition #
 Use the following composition to build an Alert :
 Copy Alert
 ├── Icon
 ├── AlertTitle
 ├── AlertDescription
 └── AlertAction
 Examples #
 Basic #
 A basic alert with an icon, title and description.
 Account updated successfully Your profile information has been saved. Changes will be reflected immediately. Copy import { CheckCircle2Icon } from "lucide-react"

 import { View Code
 Destructive #
 Use variant=&quot;destructive&quot; to create a destructive alert.
 Payment failed Your payment could not be processed. Please check your payment method and try again. Copy import { AlertCircleIcon } from "lucide-react"

 import { View Code
 Action #
 Use AlertAction to add a button or other action element to the alert.
 Dark mode is now available Enable it under your profile settings to get started. Enable Copy import {
 Alert,
 AlertAction, View Code
 Custom Colors #
 You can customize the alert colors by adding custom classes such as bg-amber-50 dark:bg-amber-950 to the Alert component.
 Your subscription will expire in 3 days. Renew now to avoid service interruption or upgrade to a paid plan to continue using the service. Copy import { AlertTriangleIcon } from "lucide-react"

 import { View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle تم الدفع بنجاح تمت معالجة دفعتك البالغة 29.99 دولارًا. تم إرسال إيصال إلى عنوان بريدك الإلكتروني. ميزة جديدة متاحة لقد أضفنا دعم الوضع الداكن. يمكنك تفعيله في إعدادات حسابك. Copy "use client"

 import * as React from "react" View Code
 API Reference #
 Alert #
 The Alert component displays a callout for user attention.
 Prop Type Default variant &quot;default&quot; | &quot;destructive&quot; &quot;default&quot;
 AlertTitle #
 The AlertTitle component displays the title of the alert.
 Prop Type Default className string -
 AlertDescription #
 The AlertDescription component displays the description or content of the alert.
 Prop Type Default className string -
 AlertAction #
 The AlertAction component displays an action element (like a button) positioned absolutely in the top-right corner of the alert.
 Prop Type Default className string - Accordion Alert Dialog On This Page Installation Usage Composition Examples Basic Destructive Action Custom Colors RTL API Reference Alert AlertTitle AlertDescription AlertAction Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
