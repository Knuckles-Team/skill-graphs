Tailwind v4 - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Tailwind v4 Copy Page Previous Next How to use shadcn/ui with Tailwind v4 and React 19. It’s here! Tailwind v4 and React 19. Ready for you to try out. You can start using it today.
 What&#x27;s New #

 The CLI can now initialize projects with Tailwind v4.
 Full support for the new @theme directive and @theme inline option.
 All components are updated for Tailwind v4 and React 19.
 We’ve removed the forwardRefs and adjusted the types.
 Every primitive now has a data-slot attribute for styling.
 We&#x27;ve fixed and cleaned up the style of the components.
 We&#x27;re deprecating the toast component in favor of sonner .
 Buttons now use the default cursor.
 We&#x27;re deprecating the default style. New projects will use new-york .
 HSL colors are now converted to OKLCH.

 Note: this is non-breaking. Your existing apps with Tailwind v3 and React 18 will still work. When you add new components, they&#x27;ll still be in v3 and React 18 until you upgrade. Only new projects start with Tailwind v4 and React 19.
 Try It Out #
 You can start using Tailwind v4 + React 19 today. See the framework specific guides below for how to get started.
 Next.js Next.js Vite Vite Laravel React Router Astro Astro TanStack Start Gatsby Gatsby React Manual
 Upgrade Your Project #
 Important: Before upgrading, please read the Tailwind v4 Compatibility
Docs and make sure your project
is ready for the upgrade. Tailwind v4 uses bleeding-edge browser features and
is designed for modern browsers.
 One of the major advantages of using shadcn/ui is that the code you end up with is exactly what you&#x27;d write yourself. There are no hidden abstractions.
 This means when a dependency has a new release, you can just follow the official upgrade paths.
 Here&#x27;s how to upgrade your existing projects (full docs are on the way):
 1. Follow the Tailwind v4 Upgrade Guide #

 Upgrade to Tailwind v4 by following the official upgrade guide: https://tailwindcss.com/docs/upgrade-guide
 Use the @tailwindcss/upgrade@next codemod to remove deprecated utility classes and update tailwind config.

 2. Update your CSS variables #
 The codemod will migrate your CSS variables as references under the @theme directive.
 Copy @layer base {
 :root {
 --background : 0 0 % 100 % ;
 --foreground : 0 0 % 3.9 % ;
 }
 }

 @theme {
 --color-background: hsl(var(--background));
 --color-foreground: hsl(var(--foreground));
 }
 This works. But to make it easier to work with colors and other variables, we&#x27;ll need to move the hsl wrappers and use @theme inline .
 Here&#x27;s how you do it:

 Move :root and .dark out of the @layer base.
 Wrap the color values in hsl()
 Add the inline option to @theme i.e @theme inline
 Remove the hsl() wrappers from @theme

 Copy :root {
 --background : hsl ( 0 0 % 100 % ); // &lt; -- Wrap in hsl
 --foreground : hsl ( 0 0 % 3.9 % );
 }

 .dark {
 --background : hsl ( 0 0 % 3.9 % ); // &lt; -- Wrap in hsl
 --foreground : hsl ( 0 0 % 98 % );
 }

 @theme inline {
 --color-background: var(--background); // &lt;-- Remove hsl
 --color-foreground: var(--foreground);
 }
 This change makes it much simpler to access your theme variables in both utility classes and outside of CSS, e.g. using color values in JavaScript.
 3. Update colors for charts #
 Now that the theme colors come with hsl() , you can remove the wrapper in your chartConfig :
 Copy const chartConfig = {
 desktop: {
 label: &quot;Desktop&quot;,
 - color: &quot;hsl(var(--chart-1))&quot;,
 + color: &quot;var(--chart-1)&quot;,
 },
 mobile: {
 label: &quot;Mobile&quot;,
 - color: &quot;hsl(var(--chart-2))&quot;,
 + color: &quot;var(--chart-2)&quot;,
 },
 } satisfies ChartConfig
 4. Use new size-* utility #
 The new size-* utility (added in Tailwind v3.4), is now fully supported by tailwind-merge . You can replace w-* h-* with the new size-* utility:
 Copy - w-4 h-4
 + size-4
 5. Update your dependencies #
 Copy pnpm up &quot;@radix-ui/*&quot; cmdk lucide-react recharts tailwind-merge clsx --latest
 6. Remove forwardRef #
 You can use the remove-forward-ref codemod to migrate your forwardRef to props or manually update the primitives.
 For the codemod, see https://github.com/reactjs/react-codemod#remove-forward-ref .
 If you want to do it manually, here&#x27;s how to do it step by step:

 Replace React.forwardRef&lt;...&gt; with React.ComponentProps&lt;...&gt;
 Remove ref={ref} from the component.
 Add a data-slot attribute. This will come in handy for styling with Tailwind.
 You can optionally convert to a named function and remove the displayName .

 Before #
 Copy const AccordionItem = React.forwardRef &lt;
 React.ElementRef &lt;typeof AccordionPrimitive.Item &gt; ,
 React.ComponentPropsWithoutRef &lt;typeof AccordionPrimitive.Item &gt;
 &gt; (({ className , ... props }, ref ) =&gt; (
 &lt; AccordionPrimitive.Item
 ref = { ref }
 className = { cn ( &quot;border-b last:border-b-0&quot; , className) }
 { ... props }
 /&gt;
 ))
 AccordionItem.displayName = &quot;AccordionItem&quot;
 After #
 Copy function AccordionItem ({
 className ,
 ... props
 } : React . ComponentProps &lt; typeof AccordionPrimitive.Item&gt;) {
 return (
 &lt; AccordionPrimitive.Item
 data-slot = &quot;accordion-item&quot;
 className = { cn ( &quot;border-b last:border-b-0&quot; , className) }
 { ... props }
 /&gt;
 )
 }
 Changelog #
 March 19, 2025 - Deprecate tailwindcss-animate #
 We&#x27;ve deprecated tailwindcss-animate in favor of tw-animate-css .
 New projects will have tw-animate-css installed by default.
 For existing projects, follow the steps below to migrate.

 Remove tailwindcss-animate from your dependencies.
 Remove the @plugin &#x27;tailwindcss-animate&#x27; from your globals.css file.
 Install tw-animate-css as a dev dependency.
 Add the @import &quot;tw-animate-css&quot; to your globals.css file.

 Copy - @plugin &#x27;tailwindcss-animate&#x27;;
 + @import &quot;tw-animate-css&quot;;
 March 12, 2025 - New Dark Mode Colors #
 We&#x27;ve revisited the dark mode colors and updated them to be more accessible.
 If you&#x27;re running an existing Tailwind v4 project ( not an upgraded one 1 ), you can update your components to use the new dark mode colors by re-adding your components using the CLI 2 .
 Commit any changes The CLI will overwrite your existing components. We recommend committing any changes you&#x27;ve made to your components before running the CLI. Copy git add .
 git commit -m &quot;...&quot; Update components pnpm npm yarn bun pnpm dlx shadcn@latest add --all --overwrite Copy Update colors Update the dark mode colors in your globals.css file to new OKLCH colors. See the Base Colors reference for a list of colors. Review changes Review and re-apply any changes you made to your components.
 Footnotes #

 Upgraded projects are not affected by this change. You can continue using the old dark mode colors. ↩

 Updating your components will overwrite your existing components. ↩

 Next.js 15 + React 19 June 2023 - New CLI, Styles and more On This Page What&#x27;s New Try It Out Upgrade Your Project 1. Follow the Tailwind v4 Upgrade Guide 2. Update your CSS variables 3. Update colors for charts 4. Use new size-* utility 5. Update your dependencies 6. Remove forwardRef Before After Changelog March 19, 2025 - Deprecate tailwindcss-animate March 12, 2025 - New Dark Mode Colors Footnotes Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
