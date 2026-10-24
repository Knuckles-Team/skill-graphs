Direction - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Direction Copy Page Previous Next A provider component that sets the text direction for your application. Radix UI Base UI Radix UI The DirectionProvider component is used to set the text direction ( ltr or rtl ) for your application. This is essential for supporting right-to-left languages like Arabic, Hebrew, and Persian.
 Here&#x27;s a preview of the component in RTL mode. Use the language selector to switch the language. To see more examples, look for the RTL section on components pages.
 Arabic (العربية) ▼ Toggle تسجيل الدخول إلى حسابك أدخل بريدك الإلكتروني أدناه لتسجيل الدخول إلى حسابك إنشاء حساب البريد الإلكتروني كلمة المرور نسيت كلمة المرور؟ تسجيل الدخول تسجيل الدخول باستخدام Google
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add direction Copy
 Usage #
 Copy import { DirectionProvider } from &quot;@/components/ui/direction&quot;
 Copy &lt; html dir = &quot;rtl&quot; &gt;
 &lt; body &gt;
 &lt; DirectionProvider direction = &quot;rtl&quot; &gt;
 { /* Your app content */ }
 &lt;/ DirectionProvider &gt;
 &lt;/ body &gt;
 &lt;/ html &gt;
 useDirection #
 The useDirection hook is used to get the current direction of the application.
 Copy import { useDirection } from &quot;@/components/ui/direction&quot;

 function MyComponent () {
 const direction = useDirection ()
 return &lt; div &gt;Current direction: { direction } &lt;/ div &gt;
 } Dialog Drawer On This Page Installation Usage useDirection Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
