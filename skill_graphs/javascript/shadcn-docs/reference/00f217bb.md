Sonner - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Sonner Copy Page Previous Next An opinionated toast component for React. Radix UI Base UI Radix UI Show Toast Copy "use client"

 import { toast } from "sonner" View Code
 About #
 Sonner is built and maintained by emilkowalski .
 Installation #
 Command Manual Run the following command: pnpm npm yarn bun pnpm dlx shadcn@latest add sonner Copy Add the Toaster component app/layout.tsx Copy import { Toaster } from &quot;@/components/ui/sonner&quot;

 export default function RootLayout ({ children }) {
 return (
 &lt; html lang = &quot;en&quot; &gt;
 &lt; head /&gt;
 &lt; body &gt;
 &lt; main &gt; { children } &lt;/ main &gt;
 &lt; Toaster /&gt;
 &lt;/ body &gt;
 &lt;/ html &gt;
 )
 }
 Usage #
 Copy import { toast } from &quot;sonner&quot;
 Copy toast ( &quot;Event has been created.&quot; )
 Examples #
 Types #
 Default Success Info Warning Error Promise Copy "use client"

 import { toast } from "sonner" View Code
 Description #
 Show Toast Copy "use client"

 import { toast } from "sonner" View Code
 Position #
 Use the position prop to change the position of the toast.
 Top Left Top Center Top Right Bottom Left Bottom Center Bottom Right Copy "use client"

 import { toast } from "sonner" View Code
 API Reference #
 See the Sonner API Reference for more information. Slider Spinner On This Page About Installation Usage Examples Types Description Position API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
