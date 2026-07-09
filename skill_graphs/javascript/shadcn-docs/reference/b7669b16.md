Next.js - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Next.js Copy Page Previous Next Create a new Next.js project with RTL support. Starting a new project? Use shadcn/create for a fully configured Next.js app with custom themes, Base UI or Radix, and icon libraries.
 Create Project # Create a new project using the --rtl flag and the next template. You can skip this step if you have already created a project using shadcn/create . pnpm npm yarn bun pnpm dlx shadcn@latest create --template next --rtl Copy This will create a components.json file with the rtl: true flag. components.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema.json&quot; ,
 &quot;style&quot; : &quot;base-nova&quot; ,
 &quot;rtl&quot; : true
 } Add DirectionProvider # Wrap your application with the DirectionProvider component with the direction=&quot;rtl&quot; prop. Then add the dir=&quot;rtl&quot; and lang=&quot;ar&quot; attributes to the html tag. Update lang=&quot;ar&quot; to your target language. app/layout.tsx Copy import { DirectionProvider } from &quot;@/components/ui/direction&quot;

 export default function RootLayout ({
 children ,
 } : {
 children : React . ReactNode
 }) {
 return (
 &lt; html lang = &quot;ar&quot; dir = &quot;rtl&quot; &gt;
 &lt; body &gt;
 &lt; DirectionProvider direction = &quot;rtl&quot; &gt; { children } &lt;/ DirectionProvider &gt;
 &lt;/ body &gt;
 &lt;/ html &gt;
 )
 } Add Font # For the best RTL experience, we recommend using fonts that have proper support for your target language. Noto is a great font family for this and it pairs well with Inter and Geist. app/layout.tsx Copy import { Noto_Sans_Arabic } from &quot;next/font/google&quot;

 import { DirectionProvider } from &quot;@/components/ui/direction&quot;

 const fontSans = Noto_Sans_Arabic ({
 subsets: [ &quot;arabic&quot; ],
 variable: &quot;--font-sans&quot; ,
 })

 export default function RootLayout ({
 children ,
 } : {
 children : React . ReactNode
 }) {
 return (
 &lt; html lang = &quot;ar&quot; dir = &quot;rtl&quot; className = { fontSans.variable } &gt;
 &lt; body &gt;
 &lt; DirectionProvider direction = &quot;rtl&quot; &gt; { children } &lt;/ DirectionProvider &gt;
 &lt;/ body &gt;
 &lt;/ html &gt;
 )
 } For other languages, eg. Hebrew, you can use the Noto_Sans_Hebrew font. Add Components # You are now ready to add components to your project. The CLI will take care of handling RTL support for you. pnpm npm yarn bun pnpm dlx shadcn@latest add item Copy RTL Vite On This Page Create Project Add DirectionProvider Add Font Add Components Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
