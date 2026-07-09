Empty - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Empty Copy Page Previous Next Use the Empty component to display an empty state. Radix UI Base UI Radix UI No Projects Yet You haven&#x27;t created any projects yet. Get started by creating your first project. Create Project Import Project Learn More Copy import { IconFolderCode } from "@tabler/icons-react"
 import { ArrowUpRightIcon } from "lucide-react"
 View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add empty Copy
 Usage #
 Copy import {
 Empty,
 EmptyContent,
 EmptyDescription,
 EmptyHeader,
 EmptyMedia,
 EmptyTitle,
 } from &quot;@/components/ui/empty&quot;
 Copy &lt; Empty &gt;
 &lt; EmptyHeader &gt;
 &lt; EmptyMedia variant = &quot;icon&quot; &gt;
 &lt; Icon /&gt;
 &lt;/ EmptyMedia &gt;
 &lt; EmptyTitle &gt;No data&lt;/ EmptyTitle &gt;
 &lt; EmptyDescription &gt;No data found&lt;/ EmptyDescription &gt;
 &lt;/ EmptyHeader &gt;
 &lt; EmptyContent &gt;
 &lt; Button &gt;Add data&lt;/ Button &gt;
 &lt;/ EmptyContent &gt;
 &lt;/ Empty &gt;
 Composition #
 Use the following composition to build an Empty state:
 Copy Empty
 ├── EmptyHeader
 │ ├── EmptyMedia
 │ ├── EmptyTitle
 │ └── EmptyDescription
 └── EmptyContent
 Examples #
 Outline #
 Use the border utility class to create an outline empty state.
 Cloud Storage Empty Upload files to your cloud storage to access them anywhere. Upload Files Copy import { IconCloud } from "@tabler/icons-react"

 import { Button } from "@/components/ui/button" View Code
 Background #
 Use the bg-* and bg-gradient-* utilities to add a background to the empty state.
 No Notifications You&#x27;re all caught up. New notifications will appear here. Refresh Copy import { IconBell } from "@tabler/icons-react"
 import { RefreshCcwIcon } from "lucide-react"
 View Code
 Avatar #
 Use the EmptyMedia component to display an avatar in the empty state.
 LR User Offline This user is currently offline. You can leave a message to notify them or try again later. Leave Message Copy import {
 Avatar,
 AvatarFallback, View Code
 Avatar Group #
 Use the EmptyMedia component to display an avatar group in the empty state.
 CN LR ER No Team Members Invite your team to collaborate on this project. Invite Members Copy import { PlusIcon } from "lucide-react"

 import { View Code
 InputGroup #
 You can add an InputGroup component to the EmptyContent component.
 404 - Not Found The page you&#x27;re looking for doesn&#x27;t exist. Try searching for what you need below. / Need help? Contact support Copy import { SearchIcon } from "lucide-react"

 import { View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle لا توجد مشاريع بعد لم تقم بإنشاء أي مشاريع بعد. ابدأ بإنشاء مشروعك الأول. إنشاء مشروع استيراد مشروع تعرف على المزيد Copy "use client"

 import * as React from "react" View Code
 API Reference #
 Empty #
 The main component of the empty state. Wraps the EmptyHeader and EmptyContent components.
 Prop Type Default className string
 Copy &lt; Empty &gt;
 &lt; EmptyHeader /&gt;
 &lt; EmptyContent /&gt;
 &lt;/ Empty &gt;
 EmptyHeader #
 The EmptyHeader component wraps the empty media, title, and description.
 Prop Type Default className string
 Copy &lt; EmptyHeader &gt;
 &lt; EmptyMedia /&gt;
 &lt; EmptyTitle /&gt;
 &lt; EmptyDescription /&gt;
 &lt;/ EmptyHeader &gt;
 EmptyMedia #
 Use the EmptyMedia component to display the media of the empty state such as an icon or an image. You can also use it to display other components such as an avatar.
 Prop Type Default variant &quot;default&quot; | &quot;icon&quot; default className string
 Copy &lt; EmptyMedia variant = &quot;icon&quot; &gt;
 &lt; Icon /&gt;
 &lt;/ EmptyMedia &gt;
 Copy &lt; EmptyMedia &gt;
 &lt; Avatar &gt;
 &lt; AvatarImage src = &quot;...&quot; /&gt;
 &lt; AvatarFallback &gt;CN&lt;/ AvatarFallback &gt;
 &lt;/ Avatar &gt;
 &lt;/ EmptyMedia &gt;
 EmptyTitle #
 Use the EmptyTitle component to display the title of the empty state.
 Prop Type Default className string
 Copy &lt; EmptyTitle &gt;No data&lt;/ EmptyTitle &gt;
 EmptyDescription #
 Use the EmptyDescription component to display the description of the empty state.
 Prop Type Default className string
 Copy &lt; EmptyDescription &gt;You do not have any notifications.&lt;/ EmptyDescription &gt;
 EmptyContent #
 Use the EmptyContent component to display the content of the empty state such as a button, input or a link.
 Prop Type Default className string
 Copy &lt; EmptyContent &gt;
 &lt; Button &gt;Add Project&lt;/ Button &gt;
 &lt;/ EmptyContent &gt; Dropdown Menu Field On This Page Installation Usage Composition Examples Outline Background Avatar Avatar Group InputGroup RTL API Reference Empty EmptyHeader EmptyMedia EmptyTitle EmptyDescription EmptyContent Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
