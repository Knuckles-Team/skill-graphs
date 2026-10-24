FAQ - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json FAQ Copy Page Previous Frequently asked questions about running a registry. Frequently asked questions #
 What does a complex component look like? #
 Here&#x27;s an example of a complex component that installs a page, two components, a hook, a format-date utils and a config file.
 Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;hello-world&quot; ,
 &quot;title&quot; : &quot;Hello World&quot; ,
 &quot;type&quot; : &quot;registry:block&quot; ,
 &quot;description&quot; : &quot;A complex hello world component&quot; ,
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;registry/new-york/hello-world/page.tsx&quot; ,
 &quot;type&quot; : &quot;registry:page&quot; ,
 &quot;target&quot; : &quot;app/hello/page.tsx&quot;
 },
 {
 &quot;path&quot; : &quot;registry/new-york/hello-world/components/hello-world.tsx&quot; ,
 &quot;type&quot; : &quot;registry:component&quot;
 },
 {
 &quot;path&quot; : &quot;registry/new-york/hello-world/components/formatted-message.tsx&quot; ,
 &quot;type&quot; : &quot;registry:component&quot;
 },
 {
 &quot;path&quot; : &quot;registry/new-york/hello-world/hooks/use-hello.ts&quot; ,
 &quot;type&quot; : &quot;registry:hook&quot;
 },
 {
 &quot;path&quot; : &quot;registry/new-york/hello-world/lib/format-date.ts&quot; ,
 &quot;type&quot; : &quot;registry:lib&quot;
 },
 {
 &quot;path&quot; : &quot;registry/new-york/hello-world/hello.config.ts&quot; ,
 &quot;type&quot; : &quot;registry:file&quot; ,
 &quot;target&quot; : &quot;~/hello.config.ts&quot;
 }
 ]
 }
 How do I add a new Tailwind color? #
 To add a new color you need to add it to cssVars under light and dark keys.
 Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;hello-world&quot; ,
 &quot;title&quot; : &quot;Hello World&quot; ,
 &quot;type&quot; : &quot;registry:block&quot; ,
 &quot;description&quot; : &quot;A complex hello world component&quot; ,
 &quot;files&quot; : [
 // ...
 ],
 &quot;cssVars&quot; : {
 &quot;light&quot; : {
 &quot;brand-background&quot; : &quot;oklch(0.205 0.015 18)&quot; ,
 &quot;brand-accent&quot; : &quot;oklch(0.205 0.015 18)&quot;
 },
 &quot;dark&quot; : {
 &quot;brand-background&quot; : &quot;oklch(0.205 0.015 18)&quot; ,
 &quot;brand-accent&quot; : &quot;oklch(0.205 0.015 18)&quot;
 }
 }
 }
 The CLI will update the project CSS file. Once updated, the new colors will be available to be used as utility classes: bg-brand and text-brand-accent .
 Why does button in registryDependencies not resolve to my GitHub repository? #
 Bare registry dependency names keep the existing shadcn behavior. button
means the built-in shadcn button item.
 For a dependency from a GitHub repository, use the full GitHub item address.
 registry-item.json Copy {
 &quot;registryDependencies&quot; : [ &quot;acme/ui/button&quot; ]
 }
 How do I pin a GitHub registry item? #
 Add #ref to the GitHub item address. The ref can be a branch, tag or full
commit SHA.
 pnpm npm yarn bun pnpm dlx shadcn@latest add acme/ui/button#v1.2.0 Copy
 For published registries, prefer tags or full commit SHAs.
 Can GitHub registry addresses use private repositories? #
 Not currently. GitHub registry addresses support public github.com
repositories. For private registries, use a namespace with authenticated URLs.
 How do I add or override a Tailwind theme variable? #
 To add or override a theme variable you add it to cssVars.theme under the key you want to add or override.
 Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;hello-world&quot; ,
 &quot;title&quot; : &quot;Hello World&quot; ,
 &quot;type&quot; : &quot;registry:block&quot; ,
 &quot;description&quot; : &quot;A complex hello world component&quot; ,
 &quot;files&quot; : [
 // ...
 ],
 &quot;cssVars&quot; : {
 &quot;theme&quot; : {
 &quot;text-base&quot; : &quot;3rem&quot; ,
 &quot;ease-in-out&quot; : &quot;cubic-bezier(0.4, 0, 0.2, 1)&quot; ,
 &quot;font-heading&quot; : &quot;Poppins, sans-serif&quot;
 }
 }
 } Gatsby On This Page Frequently asked questions What does a complex component look like? How do I add a new Tailwind color? Why does button in registryDependencies not resolve to my GitHub repository? How do I pin a GitHub registry item? Can GitHub registry addresses use private repositories? How do I add or override a Tailwind theme variable? Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
