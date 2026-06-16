Sidebar - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Sidebar Copy Page Previous Next A composable, themeable and customizable sidebar component. Radix UI Base UI Radix UI A sidebar that collapses to icons.
 Sidebars are one of the most complex components to build. They are central
to any application and often contain a lot of moving parts.
 We now have a solid foundation to build on top of. Composable. Themeable.
Customizable.
 Browse the Blocks Library .
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add sidebar Copy
 Usage #
 app/layout.tsx Copy import { SidebarProvider, SidebarTrigger } from &quot;@/components/ui/sidebar&quot;
 import { AppSidebar } from &quot;@/components/app-sidebar&quot;

 export default function Layout ({ children } : { children : React . ReactNode }) {
 return (
 &lt; SidebarProvider &gt;
 &lt; AppSidebar /&gt;
 &lt; main &gt;
 &lt; SidebarTrigger /&gt;
 { children }
 &lt;/ main &gt;
 &lt;/ SidebarProvider &gt;
 )
 }
 components/app-sidebar.tsx Copy import {
 Sidebar,
 SidebarContent,
 SidebarFooter,
 SidebarGroup,
 SidebarHeader,
 } from &quot;@/components/ui/sidebar&quot;

 export function AppSidebar () {
 return (
 &lt; Sidebar &gt;
 &lt; SidebarHeader /&gt;
 &lt; SidebarContent &gt;
 &lt; SidebarGroup /&gt;
 &lt; SidebarGroup /&gt;
 &lt;/ SidebarContent &gt;
 &lt; SidebarFooter /&gt;
 &lt;/ Sidebar &gt;
 )
 }
 Composition #
 Use the following composition to build a Sidebar layout:
 Copy SidebarProvider
 ├── Sidebar
 │ ├── SidebarHeader
 │ ├── SidebarContent
 │ │ ├── SidebarGroup
 │ │ │ ├── SidebarGroupLabel
 │ │ │ ├── SidebarGroupAction
 │ │ │ ├── SidebarGroupContent
 │ │ │ └── SidebarMenu
 │ │ │ ├── SidebarMenuItem
 │ │ │ │ ├── SidebarMenuButton
 │ │ │ │ ├── SidebarMenuAction
 │ │ │ │ └── SidebarMenuBadge
 │ │ │ └── SidebarMenuItem
 │ │ │ ├── SidebarMenuButton
 │ │ │ └── SidebarMenuSub
 │ │ │ ├── SidebarMenuSubItem
 │ │ │ └── SidebarMenuSubItem
 │ │ └── SidebarGroup
 │ │ └── SidebarMenu
 │ │ ├── SidebarMenuItem
 │ │ └── SidebarMenuItem
 │ ├── SidebarFooter
 │ └── SidebarRail
 ├── SidebarInset
 └── SidebarTrigger
 Structure #

 SidebarProvider — Handles collapsible state and provides sidebar context to child components.
 Sidebar — The main collapsible sidebar panel.
 SidebarHeader — Sticky at the top; use for branding, titles, or workspace switchers.
 SidebarFooter — Sticky at the bottom; use for user menus, settings, or actions.
 SidebarContent — Scrollable region between the header and footer.
 SidebarGroup — Groups related navigation with optional label, action, and content areas.
 SidebarMenu / SidebarMenuItem — Menu structure for links, badges, actions, and nested submenus.
 SidebarRail — Resize handle for adjusting sidebar width when applicable.
 SidebarInset — Wraps main content when using the inset variant.
 SidebarTrigger — Control that toggles the sidebar open or collapsed.

 SidebarProvider #
 The SidebarProvider component is used to provide the sidebar context to the Sidebar component. You should always wrap your application in a SidebarProvider component.
 Props #
 Name Type Description defaultOpen boolean Default open state of the sidebar. open boolean Open state of the sidebar (controlled). onOpenChange (open: boolean) =&gt; void Sets open state of the sidebar (controlled).
 Width #
 If you have a single sidebar in your application, you can use the SIDEBAR_WIDTH and SIDEBAR_WIDTH_MOBILE variables in sidebar.tsx to set the width of the sidebar.
 components/ui/sidebar.tsx Copy const SIDEBAR_WIDTH = &quot;16rem&quot;
 const SIDEBAR_WIDTH_MOBILE = &quot;18rem&quot;
 For multiple sidebars in your application, you can use the --sidebar-width and --sidebar-width-mobile CSS variables in the style prop.
 Copy &lt; SidebarProvider
 style = {
 {
 &quot;--sidebar-width&quot; : &quot;20rem&quot; ,
 &quot;--sidebar-width-mobile&quot; : &quot;20rem&quot; ,
 } as React . CSSProperties
 }
 &gt;
 &lt; Sidebar /&gt;
 &lt;/ SidebarProvider &gt;
 Keyboard Shortcut #
 To trigger the sidebar, you use the cmd+b keyboard shortcut on Mac and ctrl+b on Windows.
 components/ui/sidebar.tsx Copy const SIDEBAR_KEYBOARD_SHORTCUT = &quot;b&quot;
 Sidebar #
 The main Sidebar component used to render a collapsible sidebar.
 Props #
 Property Type Description side left or right The side of the sidebar. variant sidebar , floating , or inset The variant of the sidebar. collapsible offcanvas , icon , or none Collapsible state of the sidebar.
 Prop Description offcanvas A collapsible sidebar that slides in from the left or right. icon A sidebar that collapses to icons. none A non-collapsible sidebar.
 Note: If you use the inset variant, remember to wrap your main content
in a SidebarInset component.
 Copy &lt; SidebarProvider &gt;
 &lt; Sidebar variant = &quot;inset&quot; /&gt;
 &lt; SidebarInset &gt;
 &lt; main &gt; { children } &lt;/ main &gt;
 &lt;/ SidebarInset &gt;
 &lt;/ SidebarProvider &gt;
 useSidebar #
 The useSidebar hook is used to control the sidebar.
 Copy import { useSidebar } from &quot;@/components/ui/sidebar&quot;

 export function AppSidebar () {
 const {
 state ,
 open ,
 setOpen ,
 openMobile ,
 setOpenMobile ,
 isMobile ,
 toggleSidebar ,
 } = useSidebar ()
 }
 Property Type Description state expanded or collapsed The current state of the sidebar. open boolean Whether the sidebar is open. setOpen (open: boolean) =&gt; void Sets the open state of the sidebar. openMobile boolean Whether the sidebar is open on mobile. setOpenMobile (open: boolean) =&gt; void Sets the open state of the sidebar on mobile. isMobile boolean Whether the sidebar is on mobile. toggleSidebar () =&gt; void Toggles the sidebar. Desktop and mobile.
 SidebarHeader #
 Use the SidebarHeader component to add a sticky header to the sidebar.
 components/app-sidebar.tsx Copy &lt; Sidebar &gt;
 &lt; SidebarHeader &gt;
 &lt; SidebarMenu &gt;
 &lt; SidebarMenuItem &gt;
 &lt; DropdownMenu &gt;
 &lt; DropdownMenuTrigger asChild &gt;
 &lt; SidebarMenuButton &gt;
 Select Workspace
 &lt; ChevronDown className = &quot;ml-auto&quot; /&gt;
 &lt;/ SidebarMenuButton &gt;
 &lt;/ DropdownMenuTrigger &gt;
 &lt; DropdownMenuContent className = &quot;w-[--radix-popper-anchor-width]&quot; &gt;
 &lt; DropdownMenuItem &gt;
 &lt; span &gt;Acme Inc&lt;/ span &gt;
 &lt;/ DropdownMenuItem &gt;
 &lt;/ DropdownMenuContent &gt;
 &lt;/ DropdownMenu &gt;
 &lt;/ SidebarMenuItem &gt;
 &lt;/ SidebarMenu &gt;
 &lt;/ SidebarHeader &gt;
 &lt;/ Sidebar &gt;
 SidebarFooter #
 Use the SidebarFooter component to add a sticky footer to the sidebar.
 Copy &lt; Sidebar &gt;
 &lt; SidebarFooter &gt;
 &lt; SidebarMenu &gt;
 &lt; SidebarMenuItem &gt;
 &lt; SidebarMenuButton &gt;
 &lt; User2 /&gt; Username
 &lt;/ SidebarMenuButton &gt;
 &lt;/ SidebarMenuItem &gt;
 &lt;/ SidebarMenu &gt;
 &lt;/ SidebarFooter &gt;
 &lt;/ Sidebar &gt;
 SidebarContent #
 The SidebarContent component is used to wrap the content of the sidebar. This is where you add your SidebarGroup components. It is scrollable.
 Copy &lt; Sidebar &gt;
 &lt; SidebarContent &gt;
 &lt; SidebarGroup /&gt;
 &lt; SidebarGroup /&gt;
 &lt;/ SidebarContent &gt;
 &lt;/ Sidebar &gt;
 SidebarGroup #
 Use the SidebarGroup component to create a section within the sidebar.
 A SidebarGroup has a SidebarGroupLabel , a SidebarGroupContent and an optional SidebarGroupAction .
 Copy &lt; SidebarGroup &gt;
 &lt; SidebarGroupLabel &gt;Application&lt;/ SidebarGroupLabel &gt;
 &lt; SidebarGroupAction &gt;
 &lt; Plus /&gt; &lt; span className = &quot;sr-only&quot; &gt;Add Project&lt;/ span &gt;
 &lt;/ SidebarGroupAction &gt;
 &lt; SidebarGroupContent &gt;&lt;/ SidebarGroupContent &gt;
 &lt;/ SidebarGroup &gt;
 To make a SidebarGroup collapsible, wrap it in a Collapsible .
 Copy &lt; Collapsible defaultOpen className = &quot;group/collapsible&quot; &gt;
 &lt; SidebarGroup &gt;
 &lt; SidebarGroupLabel asChild &gt;
 &lt; CollapsibleTrigger &gt;
 Help
 &lt; ChevronDown className = &quot;ml-auto transition-transform group-data-[state=open]/collapsible:rotate-180&quot; /&gt;
 &lt;/ CollapsibleTrigger &gt;
 &lt;/ SidebarGroupLabel &gt;
 &lt; CollapsibleContent &gt;
 &lt; SidebarGroupContent /&gt;
 &lt;/ CollapsibleContent &gt;
 &lt;/ SidebarGroup &gt;
 &lt;/ Collapsible &gt;
 SidebarMenu #
 The SidebarMenu component is used for building a menu within a SidebarGroup .

 Copy &lt; SidebarMenu &gt;
 { projects. map (( project ) =&gt; (
 &lt; SidebarMenuItem key = { project.name } &gt;
 &lt; SidebarMenuButton asChild &gt;
 &lt; a href = { project.url } &gt;
 &lt; project.icon /&gt;
 &lt; span &gt; { project.name } &lt;/ span &gt;
 &lt;/ a &gt;
 &lt;/ SidebarMenuButton &gt;
 &lt;/ SidebarMenuItem &gt;
 )) }
 &lt;/ SidebarMenu &gt;
 SidebarMenuButton #
 The SidebarMenuButton component is used to render a menu button within a SidebarMenuItem .
 By default, the SidebarMenuButton renders a button but you can use the asChild prop to render a different component such as a Link or an a tag.
 Use the isActive prop to mark a menu item as active.
 Copy &lt; SidebarMenuButton asChild isActive &gt;
 &lt; a href = &quot;#&quot; &gt;Home&lt;/ a &gt;
 &lt;/ SidebarMenuButton &gt;
 SidebarMenuAction #
 The SidebarMenuAction component is used to render a menu action within a SidebarMenuItem .
 Copy &lt; SidebarMenuItem &gt;
 &lt; SidebarMenuButton asChild &gt;
 &lt; a href = &quot;#&quot; &gt;
 &lt; Home /&gt;
 &lt; span &gt;Home&lt;/ span &gt;
 &lt;/ a &gt;
 &lt;/ SidebarMenuButton &gt;
 &lt; SidebarMenuAction &gt;
 &lt; Plus /&gt; &lt; span className = &quot;sr-only&quot; &gt;Add Project&lt;/ span &gt;
 &lt;/ SidebarMenuAction &gt;
 &lt;/ SidebarMenuItem &gt;
 SidebarMenuSub #
 The SidebarMenuSub component is used to render a submenu within a SidebarMenu .
 Copy &lt; SidebarMenuItem &gt;
 &lt; SidebarMenuButton /&gt;
 &lt; SidebarMenuSub &gt;
 &lt; SidebarMenuSubItem &gt;
 &lt; SidebarMenuSubButton /&gt;
 &lt;/ SidebarMenuSubItem &gt;
 &lt;/ SidebarMenuSub &gt;
 &lt;/ SidebarMenuItem &gt;
 SidebarMenuBadge #
 The SidebarMenuBadge component is used to render a badge within a SidebarMenuItem .
 Copy &lt; SidebarMenuItem &gt;
 &lt; SidebarMenuButton /&gt;
 &lt; SidebarMenuBadge &gt;24&lt;/ SidebarMenuBadge &gt;
 &lt;/ SidebarMenuItem &gt;
 SidebarMenuSkeleton #
 The SidebarMenuSkeleton component is used to render a skeleton for a SidebarMenu .
 Copy &lt; SidebarMenu &gt;
 { Array. from ({ length: 5 }). map (( _ , index ) =&gt; (
 &lt; SidebarMenuItem key = { index } &gt;
 &lt; SidebarMenuSkeleton /&gt;
 &lt;/ SidebarMenuItem &gt;
 )) }
 &lt;/ SidebarMenu &gt;
 SidebarTrigger #
 Use the SidebarTrigger component to render a button that toggles the sidebar.
 Copy import { useSidebar } from &quot;@/components/ui/sidebar&quot;

 export function CustomTrigger () {
 const { toggleSidebar } = useSidebar ()

 return &lt; button onClick = { toggleSidebar } &gt;Toggle Sidebar&lt;/ button &gt;
 }
 SidebarRail #
 The SidebarRail component is used to render a rail within a Sidebar . This rail can be used to toggle the sidebar.
 Copy &lt; Sidebar &gt;
 &lt; SidebarHeader /&gt;
 &lt; SidebarContent &gt;
 &lt; SidebarGroup /&gt;
 &lt;/ SidebarContent &gt;
 &lt; SidebarFooter /&gt;
 &lt; SidebarRail /&gt;
 &lt;/ Sidebar &gt;
 Controlled Sidebar #
 Use the open and onOpenChange props to control the sidebar.
 Copy export function AppSidebar () {
 const [ open , setOpen ] = React. useState ( false )

 return (
 &lt; SidebarProvider open = { open } onOpenChange = { setOpen } &gt;
 &lt; Sidebar /&gt;
 &lt;/ SidebarProvider &gt;
 )
 }
 Theming #
 We use the following CSS variables to theme the sidebar.
 Copy @layer base {
 :root {
 --sidebar-background : 0 0 % 98 % ;
 --sidebar-foreground : 240 5.3 % 26.1 % ;
 --sidebar-primary : 240 5.9 % 10 % ;
 --sidebar-primary-foreground : 0 0 % 98 % ;
 --sidebar-accent : 240 4.8 % 95.9 % ;
 --sidebar-accent-foreground : 240 5.9 % 10 % ;
 --sidebar-border : 220 13 % 91 % ;
 --sidebar-ring : 217.2 91.2 % 59.8 % ;
 }

 .dark {
 --sidebar-background : 240 5.9 % 10 % ;
 --sidebar-foreground : 240 4.8 % 95.9 % ;
 --sidebar-primary : 0 0 % 98 % ;
 --sidebar-primary-foreground : 240 5.9 % 10 % ;
 --sidebar-accent : 240 3.7 % 15.9 % ;
 --sidebar-accent-foreground : 240 4.8 % 95.9 % ;
 --sidebar-border : 240 3.7 % 15.9 % ;
 --sidebar-ring : 217.2 91.2 % 59.8 % ;
 }
 }
 Styling #
 Here are some tips for styling the sidebar based on different states.
 Copy &lt; Sidebar collapsible = &quot;icon&quot; &gt;
 &lt; SidebarContent &gt;
 &lt; SidebarGroup className = &quot;group-data-[collapsible=icon]:hidden&quot; /&gt;
 &lt;/ SidebarContent &gt;
 &lt;/ Sidebar &gt;
 Copy &lt; SidebarMenuItem &gt;
 &lt; SidebarMenuButton /&gt;
 &lt; SidebarMenuAction className = &quot;peer-data-[active=true]/menu-button:opacity-100&quot; /&gt;
 &lt;/ SidebarMenuItem &gt;
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .

 View RTL Sidebar
 Changelog #
 RTL Support #
 If you&#x27;re upgrading from a previous version of the Sidebar component, you&#x27;ll need to apply the following updates to add RTL support:
 Add dir prop to Sidebar component. Add dir to the destructured props and pass it to SheetContent for mobile: Copy function Sidebar({
 side = &quot;left&quot;,
 variant = &quot;sidebar&quot;,
 collapsible = &quot;offcanvas&quot;,
 className,
 children,
 + dir,
 ...props
 }: React.ComponentProps&lt;&quot;div&quot;&gt; &amp; {
 side?: &quot;left&quot; | &quot;right&quot;
 variant?: &quot;sidebar&quot; | &quot;floating&quot; | &quot;inset&quot;
 collapsible?: &quot;offcanvas&quot; | &quot;icon&quot; | &quot;none&quot;
 }) { Then pass it to SheetContent in the mobile view: Copy &lt;Sheet open={openMobile} onOpenChange={setOpenMobile} {...props}&gt;
 &lt;SheetContent
 + dir={dir}
 data-sidebar=&quot;sidebar&quot;
 data-slot=&quot;sidebar&quot;
 data-mobile=&quot;true&quot; Add data-side attribute to sidebar container. Add data-side={side} to the sidebar container element: Copy &lt;div
 data-slot=&quot;sidebar-container&quot;
 + data-side={side}
 className={cn( Update sidebar container positioning classes. Replace JavaScript ternary conditional classes with CSS data attribute selectors: Copy className={cn(
 - &quot;fixed inset-y-0 z-10 hidden h-svh w-(--sidebar-width) transition-[left,right,width] duration-200 ease-linear md:flex&quot;,
 - side === &quot;left&quot;
 - ? &quot;left-0 group-data-[collapsible=offcanvas]:left-[calc(var(--sidebar-width)*-1)]&quot;
 - : &quot;right-0 group-data-[collapsible=offcanvas]:right-[calc(var(--sidebar-width)*-1)]&quot;,
 + &quot;fixed inset-y-0 z-10 hidden h-svh w-(--sidebar-width) transition-[left,right,width] duration-200 ease-linear md:flex data-[side=left]:left-0 data-[side=right]:right-0 data-[side=left]:group-data-[collapsible=offcanvas]:left-[calc(var(--sidebar-width)*-1)] data-[side=right]:group-data-[collapsible=offcanvas]:right-[calc(var(--sidebar-width)*-1)]&quot;, Update SidebarRail positioning classes. Update the SidebarRail component to use physical positioning for the rail: Copy className={cn(
 - &quot;hover:after:bg-sidebar-border absolute inset-y-0 z-20 hidden w-4 -translate-x-1/2 transition-all ease-linear group-data-[side=left]:-end-4 group-data-[side=right]:start-0 after:absolute after:inset-y-0 after:start-1/2 after:w-[2px] sm:flex&quot;,
 + &quot;hover:after:bg-sidebar-border absolute inset-y-0 z-20 hidden w-4 ltr:-translate-x-1/2 rtl:-translate-x-1/2 transition-all ease-linear group-data-[side=left]:-right-4 group-data-[side=right]:left-0 after:absolute after:inset-y-0 after:start-1/2 after:w-[2px] sm:flex&quot;, Add RTL flip to SidebarTrigger icon. Add className=&quot;rtl:rotate-180&quot; to the icon in SidebarTrigger to flip it in RTL mode: Copy &lt;Button ...&gt;
 - &lt;PanelLeftIcon /&gt;
 + &lt;PanelLeftIcon className=&quot;rtl:rotate-180&quot; /&gt;
 &lt;span className=&quot;sr-only&quot;&gt;Toggle Sidebar&lt;/span&gt;
 &lt;/Button&gt;
 After applying these changes, you can use the dir prop to set the direction:
 Copy &lt; Sidebar dir = &quot;rtl&quot; side = &quot;right&quot; &gt;
 { /* ... */ }
 &lt;/ Sidebar &gt;
 The sidebar will correctly position itself and handle interactions in both LTR and RTL layouts. Sheet Skeleton On This Page Installation Usage Composition Structure SidebarProvider Props Width Keyboard Shortcut Sidebar Props useSidebar SidebarHeader SidebarFooter SidebarContent SidebarGroup SidebarMenu SidebarMenuButton SidebarMenuAction SidebarMenuSub SidebarMenuBadge SidebarMenuSkeleton SidebarTrigger SidebarRail Controlled Sidebar Theming Styling RTL Changelog RTL Support Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
