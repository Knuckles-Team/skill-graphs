Card - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Card Copy Page Previous Next Displays a card with header, content, and footer. Radix UI Base UI Radix UI Login to your account Enter your email below to login to your account Sign Up Email Password Forgot your password? Login Login with Google Copy import { Button } from "@/components/ui/button"
 import {
 Card, View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add card Copy
 Usage #
 Copy import {
 Card,
 CardAction,
 CardContent,
 CardDescription,
 CardFooter,
 CardHeader,
 CardTitle,
 } from &quot;@/components/ui/card&quot;
 Copy &lt; Card &gt;
 &lt; CardHeader &gt;
 &lt; CardTitle &gt;Card Title&lt;/ CardTitle &gt;
 &lt; CardDescription &gt;Card Description&lt;/ CardDescription &gt;
 &lt; CardAction &gt;Card Action&lt;/ CardAction &gt;
 &lt;/ CardHeader &gt;
 &lt; CardContent &gt;
 &lt; p &gt;Card Content&lt;/ p &gt;
 &lt;/ CardContent &gt;
 &lt; CardFooter &gt;
 &lt; p &gt;Card Footer&lt;/ p &gt;
 &lt;/ CardFooter &gt;
 &lt;/ Card &gt;
 Composition #
 Use the following composition to build a Card :
 Copy Card
 ├── CardHeader
 │ ├── CardTitle
 │ ├── CardDescription
 │ └── CardAction
 ├── CardContent
 └── CardFooter
 Examples #
 Size #
 Use the size=&quot;sm&quot; prop to set the size of the card to small. The small size variant uses smaller spacing.
 Small Card This card uses the small size variant. The card component supports a size prop that can be set to &quot;sm&quot; for a more compact appearance. Action Copy import { Button } from "@/components/ui/button"
 import {
 Card, View Code
 Spacing #
 In addition to the size prop, you can use the --card-spacing CSS variable to control the spacing between sections and the inset of card parts.
 16px 20px 24px 32px Login to your account Enter your email below to login to your account Sign Up Email Password Forgot your password? Login Login with Google Copy "use client"

 import * as React from "react" View Code
 Use negative margins with -mx-(--card-spacing) to make content go edge to edge while keeping it aligned with the card inset. When the edge-to-edge content sits above a footer, use -mb-(--card-spacing) on CardContent to remove the section gap.
 Terms of Service Review the terms before accepting the agreement. These terms govern your use of the workspace, including access to shared documents, project files, and collaboration tools. You are responsible for the content you upload and for ensuring that your team has the appropriate permissions to view or edit it. We may update features or limits as the service evolves. When those changes materially affect your workflow, we will notify your workspace administrators. By continuing, you agree to keep your account credentials secure and to follow your organization&#x27;s acceptable use policies. Decline Accept Copy import { Button } from "@/components/ui/button"
 import {
 Card, View Code
 Image #
 Add an image before the card header to create a card with an image.
 Featured Design systems meetup A practical talk on component APIs, accessibility, and shipping faster. View Event Copy import { Badge } from "@/components/ui/badge"
 import { Button } from "@/components/ui/button"
 import { View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle تسجيل الدخول إلى حسابك أدخل بريدك الإلكتروني أدناه لتسجيل الدخول إلى حسابك إنشاء حساب البريد الإلكتروني كلمة المرور نسيت كلمة المرور؟ تسجيل الدخول تسجيل الدخول باستخدام Google Copy "use client"

 import * as React from "react" View Code
 API Reference #
 Card #
 The Card component is the root container for card content.
 Prop Type Default size &quot;default&quot; | &quot;sm&quot; &quot;default&quot; className string -
 CardHeader #
 The CardHeader component is used for a title, description, and optional action.
 Prop Type Default className string -
 CardTitle #
 The CardTitle component is used for the card title.
 Prop Type Default className string -
 CardDescription #
 The CardDescription component is used for helper text under the title.
 Prop Type Default className string -
 CardAction #
 The CardAction component places content in the top-right of the header (for example, a button or a badge).
 Prop Type Default className string -
 CardContent #
 The CardContent component is used for the main card body.
 Prop Type Default className string -
 CardFooter #
 The CardFooter component is used for actions and secondary content at the bottom of the card.
 Prop Type Default className string -
 Changelog #
 Spacing Variable #
 If you&#x27;re upgrading from a previous version of the Card component, you&#x27;ll need to apply the following updates to use the --card-spacing variable:
 Update the Card root spacing classes. Replace the hard-coded gap and vertical padding with --card-spacing , and set the default and small size values on the root: Copy className={cn(
 - &quot;group/card flex flex-col gap-4 overflow-hidden rounded-xl bg-card py-4 text-sm text-card-foreground ring-1 ring-foreground/10 has-data-[slot=card-footer]:pb-0 has-[&gt;img:first-child]:pt-0 data-[size=sm]:gap-3 data-[size=sm]:py-3 data-[size=sm]:has-data-[slot=card-footer]:pb-0 *:[img:first-child]:rounded-t-xl *:[img:last-child]:rounded-b-xl&quot;,
 + &quot;group/card flex flex-col gap-(--card-spacing) overflow-hidden rounded-xl bg-card py-(--card-spacing) text-sm text-card-foreground ring-1 ring-foreground/10 [--card-spacing:--spacing(4)] has-data-[slot=card-footer]:pb-0 has-[&gt;img:first-child]:pt-0 data-[size=sm]:[--card-spacing:--spacing(3)] data-[size=sm]:has-data-[slot=card-footer]:pb-0 *:[img:first-child]:rounded-t-xl *:[img:last-child]:rounded-b-xl&quot;,
 className
 )} Update CardHeader spacing classes. Replace the horizontal padding and border spacing with the shared variable: Copy className={cn(
 - &quot;group/card-header @container/card-header grid auto-rows-min items-start gap-1 rounded-t-xl px-4 group-data-[size=sm]/card:px-3 has-data-[slot=card-action]:grid-cols-[1fr_auto] has-data-[slot=card-description]:grid-rows-[auto_auto] [.border-b]:pb-4 group-data-[size=sm]/card:[.border-b]:pb-3&quot;,
 + &quot;group/card-header @container/card-header grid auto-rows-min items-start gap-1 rounded-t-xl px-(--card-spacing) has-data-[slot=card-action]:grid-cols-[1fr_auto] has-data-[slot=card-description]:grid-rows-[auto_auto] [.border-b]:pb-(--card-spacing)&quot;,
 className
 )} Update CardContent and CardFooter spacing classes. Use --card-spacing for the content inset and footer padding: Copy function CardContent({ className, ...props }: React.ComponentProps&lt;&quot;div&quot;&gt;) {
 return (
 &lt;div
 data-slot=&quot;card-content&quot;
 - className={cn(&quot;px-4 group-data-[size=sm]/card:px-3&quot;, className)}
 + className={cn(&quot;px-(--card-spacing)&quot;, className)}
 {...props}
 /&gt;
 )
 } Copy className={cn(
 - &quot;flex items-center rounded-b-xl border-t bg-muted/50 p-4 group-data-[size=sm]/card:p-3&quot;,
 + &quot;flex items-center rounded-b-xl border-t bg-muted/50 p-(--card-spacing)&quot;,
 className
 )}
 After applying these changes, you can customize card spacing by setting --card-spacing on the Card with an arbitrary property class:
 Copy function Example () {
 return &lt; Card className = &quot;[--card-spacing:--spacing(6)]&quot; &gt;...&lt;/ Card &gt;
 } Calendar Carousel On This Page Installation Usage Composition Examples Size Spacing Image RTL API Reference Card CardHeader CardTitle CardDescription CardAction CardContent CardFooter Changelog Spacing Variable Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
