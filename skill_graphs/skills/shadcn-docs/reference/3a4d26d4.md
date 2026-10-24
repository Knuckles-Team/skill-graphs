Input OTP - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Input OTP Copy Page Previous Next Accessible one-time password component with copy-paste functionality. Radix UI Base UI Radix UI 1 2 3 4 5 6 Copy import {
 InputOTP,
 InputOTPGroup, View Code
 About #
 Input OTP is built on top of input-otp by @guilherme_rodz .
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add input-otp Copy
 Usage #
 Copy import {
 InputOTP,
 InputOTPGroup,
 InputOTPSeparator,
 InputOTPSlot,
 } from &quot;@/components/ui/input-otp&quot;
 Copy &lt; InputOTP maxLength = { 6 } &gt;
 &lt; InputOTPGroup &gt;
 &lt; InputOTPSlot index = { 0 } /&gt;
 &lt; InputOTPSlot index = { 1 } /&gt;
 &lt; InputOTPSlot index = { 2 } /&gt;
 &lt;/ InputOTPGroup &gt;
 &lt; InputOTPSeparator /&gt;
 &lt; InputOTPGroup &gt;
 &lt; InputOTPSlot index = { 3 } /&gt;
 &lt; InputOTPSlot index = { 4 } /&gt;
 &lt; InputOTPSlot index = { 5 } /&gt;
 &lt;/ InputOTPGroup &gt;
 &lt;/ InputOTP &gt;
 Composition #
 Use the following composition to build an InputOTP :
 Copy InputOTP
 ├── InputOTPGroup
 │ ├── InputOTPSlot
 │ ├── InputOTPSlot
 │ └── InputOTPSlot
 ├── InputOTPSeparator
 ├── InputOTPGroup
 │ ├── InputOTPSlot
 │ ├── InputOTPSlot
 │ └── InputOTPSlot
 ├── InputOTPSeparator
 └── InputOTPGroup
 ├── InputOTPSlot
 └── InputOTPSlot
 Pattern #
 Use the pattern prop to define a custom pattern for the OTP input.
 Copy import { REGEXP_ONLY_DIGITS_AND_CHARS } from &quot;input-otp&quot;

 ; &lt; InputOTP maxLength = { 6 } pattern = {REGEXP_ONLY_DIGITS_AND_CHARS} &gt;
 ...
 &lt;/ InputOTP &gt;
 Digits Only Copy "use client"

 import { REGEXP_ONLY_DIGITS } from "input-otp" View Code
 Examples #
 Separator #
 Use the &lt;InputOTPSeparator /&gt; component to add a separator between input groups.
 Copy import {
 InputOTP,
 InputOTPGroup, View Code
 Disabled #
 Use the disabled prop to disable the input.
 1 2 3 4 5 6 Copy import {
 InputOTP,
 InputOTPGroup, View Code
 Controlled #
 Use the value and onChange props to control the input value.
 Enter your one-time password. Copy "use client"

 import * as React from "react" View Code
 Invalid #
 Use aria-invalid on the slots to show an error state.
 0 0 0 0 0 0 Copy "use client"

 import * as React from "react" View Code
 Four Digits #
 A common pattern for PIN codes. This uses the pattern={REGEXP_ONLY_DIGITS} prop.
 Copy "use client"

 import { REGEXP_ONLY_DIGITS } from "input-otp" View Code
 Alphanumeric #
 Use REGEXP_ONLY_DIGITS_AND_CHARS to accept both letters and numbers.
 Copy "use client"

 import { REGEXP_ONLY_DIGITS_AND_CHARS } from "input-otp" View Code
 Form #
 Verify your login Enter the verification code we sent to your email address: m@example.com . Verification code Resend Code I no longer have access to this email address. Verify Having trouble signing in? Contact support Copy import { RefreshCwIcon } from "lucide-react"

 import { Button } from "@/components/ui/button" View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle رمز التحقق 1 2 3 4 5 6 Copy "use client"

 import * as React from "react" View Code
 API Reference #
 See the input-otp documentation for more information. Input Group Item On This Page About Installation Usage Composition Pattern Examples Separator Disabled Controlled Invalid Four Digits Alphanumeric Form RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
