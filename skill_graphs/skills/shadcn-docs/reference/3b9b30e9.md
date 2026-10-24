Vite - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Vite Copy Page Previous Next Create a new Vite project with RTL support. Starting a new project? Use shadcn/create for a fully configured Vite app with custom themes, Base UI or Radix, and icon libraries.
 Create Project # Create a new project using the --rtl flag and the vite template. You can skip this step if you have already created a project using shadcn/create . pnpm npm yarn bun pnpm dlx shadcn@latest create --template vite --rtl Copy This will create a components.json file with the rtl: true flag. components.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema.json&quot; ,
 &quot;style&quot; : &quot;base-nova&quot; ,
 &quot;rtl&quot; : true
 } Add DirectionProvider # Add the dir=&quot;rtl&quot; and lang=&quot;ar&quot; attributes to the html tag in your index.html . Update lang=&quot;ar&quot; to your target language. index.html Copy &lt;! doctype html &gt;
 &lt; html lang = &quot;ar&quot; dir = &quot;rtl&quot; &gt;
 &lt; head &gt;
 &lt; meta charset = &quot;UTF-8&quot; /&gt;
 &lt; meta name = &quot;viewport&quot; content = &quot;width=device-width, initial-scale=1.0&quot; /&gt;
 &lt; title &gt;Vite App&lt;/ title &gt;
 &lt;/ head &gt;
 &lt; body &gt;
 &lt; div id = &quot;root&quot; &gt;&lt;/ div &gt;
 &lt; script type = &quot;module&quot; src = &quot;/src/main.tsx&quot; &gt;&lt;/ script &gt;
 &lt;/ body &gt;
 &lt;/ html &gt; Then wrap your app with the DirectionProvider component with the direction=&quot;rtl&quot; prop in your main.tsx : src/main.tsx Copy import { StrictMode } from &quot;react&quot;
 import { createRoot } from &quot;react-dom/client&quot;

 import { DirectionProvider } from &quot;@/components/ui/direction&quot;

 import App from &quot;./App&quot;

 import &quot;./index.css&quot;

 createRoot (document. getElementById ( &quot;root&quot; ) ! ). render (
 &lt; StrictMode &gt;
 &lt; DirectionProvider direction = &quot;rtl&quot; &gt;
 &lt; App /&gt;
 &lt;/ DirectionProvider &gt;
 &lt;/ StrictMode &gt;
 ) Add Font # For the best RTL experience, we recommend using fonts that have proper support for your target language. Noto is a great font family for this and it pairs well with Inter and Geist. Install the font using Fontsource : pnpm npm yarn bun pnpm add @fontsource-variable/noto-sans-arabic Copy Import the font in your index.css : src/index.css Copy @import &quot;tailwindcss&quot; ;
 @import &quot;tw-animate-css&quot; ;
 @import &quot;shadcn/tailwind.css&quot; ;
 @import &quot;@fontsource-variable/noto-sans-arabic&quot; ;

 @theme inline {
 --font-sans: &quot;Noto Sans Arabic Variable&quot;, sans-serif ;
 } For other languages, eg. Hebrew, you can use @fontsource-variable/noto-sans-hebrew . Add Components # You are now ready to add components to your project. The CLI will take care of handling RTL support for you. pnpm npm yarn bun pnpm dlx shadcn@latest add item Copy Next.js TanStack Start On This Page Create Project Add DirectionProvider Add Font Add Components Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
