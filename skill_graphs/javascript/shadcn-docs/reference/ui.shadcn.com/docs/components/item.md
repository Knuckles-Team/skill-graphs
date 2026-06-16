Item - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Item Copy Page Previous Next A versatile component for displaying content with media, title, description, and actions. Radix UI Base UI Radix UI Basic Item A simple item with title and description. Action Your profile has been verified. Copy import { BadgeCheckIcon, ChevronRightIcon } from "lucide-react"

 import { Button } from "@/components/ui/button" View Code
 The Item component is a straightforward flex container that can house nearly any type of content. Use it to display a title, description, and actions. Group it with the ItemGroup component to create a list of items.
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add item Copy
 Usage #
 Copy import {
 Item,
 ItemActions,
 ItemContent,
 ItemDescription,
 ItemMedia,
 ItemTitle,
 } from &quot;@/components/ui/item&quot;
 Copy &lt; Item &gt;
 &lt; ItemMedia variant = &quot;icon&quot; &gt;
 &lt; Icon /&gt;
 &lt;/ ItemMedia &gt;
 &lt; ItemContent &gt;
 &lt; ItemTitle &gt;Title&lt;/ ItemTitle &gt;
 &lt; ItemDescription &gt;Description&lt;/ ItemDescription &gt;
 &lt;/ ItemContent &gt;
 &lt; ItemActions &gt;
 &lt; Button &gt;Action&lt;/ Button &gt;
 &lt;/ ItemActions &gt;
 &lt;/ Item &gt;
 Composition #
 Use the following composition to build an Item :
 Copy ItemGroup
 └── Item
 ├── ItemHeader
 ├── ItemMedia
 ├── ItemContent
 │ ├── ItemTitle
 │ └── ItemDescription
 ├── ItemActions
 └── ItemFooter
 Item vs Field #
 Use Field if you need to display a form input such as a checkbox, input, radio, or select.
 If you only need to display content such as a title, description, and actions, use Item .
 Variant #
 Use the variant prop to change the visual style of the item.
 Default Variant Transparent background with no border. Outline Variant Outlined style with a visible border. Muted Variant Muted background for secondary content. Copy import { InboxIcon } from "lucide-react"

 import { View Code
 Size #
 Use the size prop to change the size of the item. Available sizes are default , sm , and xs .
 Default Size The standard size for most use cases. Small Size A compact size for dense layouts. Extra Small Size The most compact size available. Copy import { InboxIcon } from "lucide-react"

 import { View Code
 Examples #
 Icon #
 Use ItemMedia with variant=&quot;icon&quot; to display an icon.
 Security Alert New login detected from unknown device. Review Copy import { ShieldAlertIcon } from "lucide-react"

 import { Button } from "@/components/ui/button" View Code
 Avatar #
 You can use ItemMedia with variant=&quot;avatar&quot; to display an avatar.
 ER Evil Rabbit Last seen 5 months ago CN LR ER No Team Members Invite your team to collaborate on this project. Invite Copy import { Plus } from "lucide-react"

 import { View Code
 Image #
 Use ItemMedia with variant=&quot;image&quot; to display an image.
 Midnight City Lights - Electric Nights Neon Dreams 3:45 Coffee Shop Conversations - Urban Stories The Morning Brew 4:05 Digital Rain - Binary Beats Cyber Symphony 3:30 Copy import Image from "next/image"

 import { View Code
 Group #
 Use ItemGroup to group related items together.
 s shadcn shadcn@vercel.com m maxleiter maxleiter@vercel.com e evilrabbit evilrabbit@vercel.com Copy import * as React from "react"
 import { PlusIcon } from "lucide-react"
 View Code
 Header #
 Use ItemHeader to add a header above the item content.
 v0-1.5-sm Everyday tasks and UI generation. v0-1.5-lg Advanced thinking or reasoning. v0-2.0-mini Open Source model for everyone. Copy import Image from "next/image"

 import { View Code
 Link #
 Use the asChild prop to render the item as a link. The hover and focus states will be applied to the anchor element.
 Visit our documentation Learn how to get started with our components. External resource Opens in a new tab with security attributes. Copy import { ChevronRightIcon, ExternalLinkIcon } from "lucide-react"

 import { View Code
 Copy &lt; Item asChild &gt;
 &lt; a href = &quot;/dashboard&quot; &gt;
 &lt; ItemMedia variant = &quot;icon&quot; &gt;
 &lt; HomeIcon /&gt;
 &lt;/ ItemMedia &gt;
 &lt; ItemContent &gt;
 &lt; ItemTitle &gt;Dashboard&lt;/ ItemTitle &gt;
 &lt; ItemDescription &gt;Overview of your account and activity.&lt;/ ItemDescription &gt;
 &lt;/ ItemContent &gt;
 &lt;/ a &gt;
 &lt;/ Item &gt;
 Dropdown #
 Select Copy "use client"

 import { ChevronDownIcon } from "lucide-react" View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle عنصر أساسي عنصر بسيط يحتوي على عنوان ووصف. إجراء تم التحقق من ملفك الشخصي. Copy "use client"

 import * as React from "react" View Code
 API Reference #
 Item #
 The main component for displaying content with media, title, description, and actions.
 Prop Type Default variant &quot;default&quot; | &quot;outline&quot; | &quot;muted&quot; &quot;default&quot; size &quot;default&quot; | &quot;sm&quot; | &quot;xs&quot; &quot;default&quot; asChild boolean false
 ItemGroup #
 A container that groups related items together with consistent styling.
 Copy &lt; ItemGroup &gt;
 &lt; Item /&gt;
 &lt; Item /&gt;
 &lt;/ ItemGroup &gt;
 ItemSeparator #
 A separator between items in a group.
 Copy &lt; ItemGroup &gt;
 &lt; Item /&gt;
 &lt; ItemSeparator /&gt;
 &lt; Item /&gt;
 &lt;/ ItemGroup &gt;
 ItemMedia #
 Use ItemMedia to display media content such as icons, images, or avatars.
 Prop Type Default variant &quot;default&quot; | &quot;icon&quot; | &quot;image&quot; &quot;default&quot;
 Copy &lt; ItemMedia variant = &quot;icon&quot; &gt;
 &lt; Icon /&gt;
 &lt;/ ItemMedia &gt;
 Copy &lt; ItemMedia variant = &quot;image&quot; &gt;
 &lt; img src = &quot;...&quot; alt = &quot;...&quot; /&gt;
 &lt;/ ItemMedia &gt;
 ItemContent #
 Wraps the title and description of the item.
 Copy &lt; ItemContent &gt;
 &lt; ItemTitle &gt;Title&lt;/ ItemTitle &gt;
 &lt; ItemDescription &gt;Description&lt;/ ItemDescription &gt;
 &lt;/ ItemContent &gt;
 ItemTitle #
 Displays the title of the item.
 Copy &lt; ItemTitle &gt;Item Title&lt;/ ItemTitle &gt;
 ItemDescription #
 Displays the description of the item.
 Copy &lt; ItemDescription &gt;Item description&lt;/ ItemDescription &gt;
 ItemActions #
 Container for action buttons or other interactive elements.
 Copy &lt; ItemActions &gt;
 &lt; Button &gt;Action&lt;/ Button &gt;
 &lt;/ ItemActions &gt;
 ItemHeader #
 Displays a header above the item content.
 Copy &lt; Item &gt;
 &lt; ItemHeader &gt;Header&lt;/ ItemHeader &gt;
 &lt; ItemContent &gt;...&lt;/ ItemContent &gt;
 &lt;/ Item &gt;
 ItemFooter #
 Displays a footer below the item content.
 Copy &lt; Item &gt;
 &lt; ItemContent &gt;...&lt;/ ItemContent &gt;
 &lt; ItemFooter &gt;Footer&lt;/ ItemFooter &gt;
 &lt;/ Item &gt; Input OTP Kbd On This Page Installation Usage Composition Item vs Field Variant Size Examples Icon Avatar Image Group Header Link Dropdown RTL API Reference Item ItemGroup ItemSeparator ItemMedia ItemContent ItemTitle ItemDescription ItemActions ItemHeader ItemFooter Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
