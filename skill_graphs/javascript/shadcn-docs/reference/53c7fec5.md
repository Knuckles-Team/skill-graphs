RTL - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json RTL Copy Page Previous Next Right-to-left support for shadcn/ui components. shadcn/ui components have first-class support for right-to-left (RTL) layouts. Text alignment, positioning, and directional styles automatically adapt for languages like Arabic, Hebrew, and Persian.
 Arabic (العربية) ▼ Toggle تسجيل الدخول إلى حسابك أدخل بريدك الإلكتروني أدناه لتسجيل الدخول إلى حسابك إنشاء حساب البريد الإلكتروني كلمة المرور نسيت كلمة المرور؟ تسجيل الدخول تسجيل الدخول باستخدام Google A card component in RTL mode.
 When you install components, the CLI automatically transforms physical positioning classes to logical equivalents, so your components work seamlessly in both LTR and RTL contexts.
 Get Started #
 Select your framework to get started with RTL support.
 Next.js Next.js Vite Vite TanStack Start
 How it works #
 When you add components with rtl: true set in your components.json , the shadcn CLI automatically transforms classes and props to be RTL compatible:

 Physical positioning classes like left-* and right-* are converted to logical equivalents like start-* and end-* .
 Directional props are updated to use logical values.
 Text alignment and spacing classes are adjusted accordingly.
 Supported icons are automatically flipped using rtl:rotate-180 .

 Try it out #
 Click the link below to open a Next.js project with RTL support in v0.

 Supported Styles #
 Automatic RTL transformation via the CLI is only available for projects created using shadcn create with the new styles ( base-nova , radix-nova , etc.).
 For other styles, see the Migration Guide .
 Font Recommendations #
 For the best RTL experience, we recommend using fonts that have proper support for your target language. Noto is a great font family for this and it pairs well with Inter and Geist.
 See your framework&#x27;s RTL guide under Get Started for details on installing and configuring RTL fonts.
 Animations #
 The CLI also handles animation classes, automatically transforming physical directional animations to their logical equivalents. For example, slide-in-from-right becomes slide-in-from-end .
 This ensures animations like dropdowns, popovers, and tooltips animate in the correct direction based on the document&#x27;s text direction.
 A note on tw-animate-css:
 There is a known issue with the tw-animate-css library where the logical slide utilities are not working as expected. For now, make sure you pass in the dir prop to portal elements.
 Copy &lt; Popover &gt;
 &lt; PopoverTrigger &gt;Open&lt;/ PopoverTrigger &gt;
 &lt; PopoverContent dir = &quot;rtl&quot; &gt;
 &lt; div &gt;Content&lt;/ div &gt;
 &lt;/ PopoverContent &gt;
 &lt;/ Popover &gt;
 Copy &lt; Tooltip &gt;
 &lt; TooltipTrigger &gt;Open&lt;/ TooltipTrigger &gt;
 &lt; TooltipContent dir = &quot;rtl&quot; &gt;
 &lt; div &gt;Content&lt;/ div &gt;
 &lt;/ TooltipContent &gt;
 &lt;/ Tooltip &gt;
 Migrating existing components #
 If you have existing components installed before enabling RTL, you can migrate them using the CLI as follows:
 Run the migrate command pnpm npm yarn bun pnpm dlx shadcn@latest migrate rtl [path] Copy [path] accepts a path or glob pattern to migrate. If you don&#x27;t provide a path, it will migrate all the files in the ui directory. Manual Migration (Optional) # The following components are not automatically migrated by the CLI. Follow the RTL support section for each component to manually migrate them.
 Calendar
 Pagination
 Sidebar
 Migrate Icons # Some icons like ArrowRightIcon or ChevronLeftIcon might need the rtl:rotate-180 class to be flipped correctly. Add the rtl:rotate-180 class to the icon component to flip it correctly. Copy &lt; ArrowRightIcon className = &quot; rtl:rotate-180 &quot; /&gt; Add direction component # Add the direction component to your project. pnpm npm yarn bun pnpm dlx shadcn@latest add direction Copy Add DirectionProvider # Follow your framework&#x27;s documentation for details on how to add the DirectionProvider component to your project. See the Get Started section for details on how to add the DirectionProvider component to your project. Dark Mode CLI On This Page Get Started How it works Try it out Supported Styles Font Recommendations Animations Migrating existing components Manual Migration (Optional) Migrate Icons Add direction component Add DirectionProvider Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
