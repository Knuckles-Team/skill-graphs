Examples - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Examples Copy Page Previous Next Examples of registry items: styles, components, css vars, etc. registry:style #
 Custom style that extends shadcn/ui #
 The following registry item is a custom style that extends shadcn/ui. On npx shadcn init , it will:

 Install @tabler/icons-react as a dependency.
 Add the login-01 block and calendar component to the project.
 Add the editor from a remote registry.
 Set the font-sans variable to Inter, sans-serif .
 Install a brand color in light and dark mode.

 example-style.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;example-style&quot; ,
 &quot;type&quot; : &quot;registry:style&quot; ,
 &quot;dependencies&quot; : [ &quot;@tabler/icons-react&quot; ],
 &quot;registryDependencies&quot; : [
 &quot;login-01&quot; ,
 &quot;calendar&quot; ,
 &quot;https://example.com/r/editor.json&quot;
 ],
 &quot;cssVars&quot; : {
 &quot;theme&quot; : {
 &quot;font-sans&quot; : &quot;Inter, sans-serif&quot;
 },
 &quot;light&quot; : {
 &quot;brand&quot; : &quot;20 14.3% 4.1%&quot;
 },
 &quot;dark&quot; : {
 &quot;brand&quot; : &quot;20 14.3% 4.1%&quot;
 }
 }
 }
 Custom style from scratch #
 The following registry item is a custom style that doesn&#x27;t extend shadcn/ui. See the extends: none field.
 It can be used to create a new style from scratch, i.e. custom components, css vars, dependencies, etc.
 On npx shadcn add , the following will:

 Install tailwind-merge and clsx as dependencies.
 Add the utils registry item from the shadcn/ui registry.
 Add the button , input , label , and select components from a remote registry.
 Install new css vars: main , bg , border , text , ring .

 example-style.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;extends&quot; : &quot;none&quot; ,
 &quot;name&quot; : &quot;new-style&quot; ,
 &quot;type&quot; : &quot;registry:style&quot; ,
 &quot;dependencies&quot; : [ &quot;tailwind-merge&quot; , &quot;clsx&quot; ],
 &quot;registryDependencies&quot; : [
 &quot;utils&quot; ,
 &quot;https://example.com/r/button.json&quot; ,
 &quot;https://example.com/r/input.json&quot; ,
 &quot;https://example.com/r/label.json&quot; ,
 &quot;https://example.com/r/select.json&quot;
 ],
 &quot;cssVars&quot; : {
 &quot;theme&quot; : {
 &quot;font-sans&quot; : &quot;Inter, sans-serif&quot;
 },
 &quot;light&quot; : {
 &quot;main&quot; : &quot;#88aaee&quot; ,
 &quot;bg&quot; : &quot;#dfe5f2&quot; ,
 &quot;border&quot; : &quot;#000&quot; ,
 &quot;text&quot; : &quot;#000&quot; ,
 &quot;ring&quot; : &quot;#000&quot;
 },
 &quot;dark&quot; : {
 &quot;main&quot; : &quot;#88aaee&quot; ,
 &quot;bg&quot; : &quot;#272933&quot; ,
 &quot;border&quot; : &quot;#000&quot; ,
 &quot;text&quot; : &quot;#e6e6e6&quot; ,
 &quot;ring&quot; : &quot;#fff&quot;
 }
 }
 }
 registry:theme #
 Custom theme #
 example-theme.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;custom-theme&quot; ,
 &quot;type&quot; : &quot;registry:theme&quot; ,
 &quot;cssVars&quot; : {
 &quot;light&quot; : {
 &quot;background&quot; : &quot;oklch(1 0 0)&quot; ,
 &quot;foreground&quot; : &quot;oklch(0.141 0.005 285.823)&quot; ,
 &quot;primary&quot; : &quot;oklch(0.546 0.245 262.881)&quot; ,
 &quot;primary-foreground&quot; : &quot;oklch(0.97 0.014 254.604)&quot; ,
 &quot;ring&quot; : &quot;oklch(0.746 0.16 232.661)&quot; ,
 &quot;sidebar-primary&quot; : &quot;oklch(0.546 0.245 262.881)&quot; ,
 &quot;sidebar-primary-foreground&quot; : &quot;oklch(0.97 0.014 254.604)&quot; ,
 &quot;sidebar-ring&quot; : &quot;oklch(0.746 0.16 232.661)&quot;
 },
 &quot;dark&quot; : {
 &quot;background&quot; : &quot;oklch(1 0 0)&quot; ,
 &quot;foreground&quot; : &quot;oklch(0.141 0.005 285.823)&quot; ,
 &quot;primary&quot; : &quot;oklch(0.707 0.165 254.624)&quot; ,
 &quot;primary-foreground&quot; : &quot;oklch(0.97 0.014 254.604)&quot; ,
 &quot;ring&quot; : &quot;oklch(0.707 0.165 254.624)&quot; ,
 &quot;sidebar-primary&quot; : &quot;oklch(0.707 0.165 254.624)&quot; ,
 &quot;sidebar-primary-foreground&quot; : &quot;oklch(0.97 0.014 254.604)&quot; ,
 &quot;sidebar-ring&quot; : &quot;oklch(0.707 0.165 254.624)&quot;
 }
 }
 }
 Custom colors #
 The following style will init using shadcn/ui defaults and then add a custom brand color.
 example-style.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;custom-style&quot; ,
 &quot;type&quot; : &quot;registry:style&quot; ,
 &quot;cssVars&quot; : {
 &quot;light&quot; : {
 &quot;brand&quot; : &quot;oklch(0.99 0.00 0)&quot;
 },
 &quot;dark&quot; : {
 &quot;brand&quot; : &quot;oklch(0.14 0.00 286)&quot;
 }
 }
 }
 registry:block #
 Custom block #
 This block installs the login-01 block from the shadcn/ui registry.
 login-01.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;login-01&quot; ,
 &quot;type&quot; : &quot;registry:block&quot; ,
 &quot;description&quot; : &quot;A simple login form.&quot; ,
 &quot;registryDependencies&quot; : [ &quot;button&quot; , &quot;card&quot; , &quot;input&quot; , &quot;label&quot; ],
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;blocks/login-01/page.tsx&quot; ,
 &quot;content&quot; : &quot;import { LoginForm } ...&quot; ,
 &quot;type&quot; : &quot;registry:page&quot; ,
 &quot;target&quot; : &quot;app/login/page.tsx&quot;
 },
 {
 &quot;path&quot; : &quot;blocks/login-01/components/login-form.tsx&quot; ,
 &quot;content&quot; : &quot;...&quot; ,
 &quot;type&quot; : &quot;registry:component&quot;
 }
 ]
 }
 Install a block and override primitives #
 You can install a block from the shadcn/ui registry and override the primitives using your custom ones.
 On npx shadcn add , the following will:

 Add the login-01 block from the shadcn/ui registry.
 Override the button , input , and label primitives with the ones from the remote registry.

 example-style.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;custom-login&quot; ,
 &quot;type&quot; : &quot;registry:block&quot; ,
 &quot;registryDependencies&quot; : [
 &quot;login-01&quot; ,
 &quot;https://example.com/r/button.json&quot; ,
 &quot;https://example.com/r/input.json&quot; ,
 &quot;https://example.com/r/label.json&quot;
 ]
 }
 registry:ui #
 UI component #
 A registry:ui item is a reusable UI component. It can have dependencies, registry dependencies, and CSS variables.
 button.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;button&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot; ,
 &quot;dependencies&quot; : [ &quot;radix-ui&quot; ],
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;ui/button.tsx&quot; ,
 &quot;content&quot; : &quot;...&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot;
 }
 ]
 }
 UI component with CSS variables #
 sidebar.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;sidebar&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot; ,
 &quot;dependencies&quot; : [ &quot;radix-ui&quot; ],
 &quot;registryDependencies&quot; : [ &quot;button&quot; , &quot;separator&quot; , &quot;sheet&quot; , &quot;tooltip&quot; ],
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;ui/sidebar.tsx&quot; ,
 &quot;content&quot; : &quot;...&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot;
 }
 ],
 &quot;cssVars&quot; : {
 &quot;light&quot; : {
 &quot;sidebar-background&quot; : &quot;oklch(0.985 0 0)&quot; ,
 &quot;sidebar-foreground&quot; : &quot;oklch(0.141 0.005 285.823)&quot; ,
 &quot;sidebar-border&quot; : &quot;oklch(0.92 0.004 286.32)&quot;
 },
 &quot;dark&quot; : {
 &quot;sidebar-background&quot; : &quot;oklch(0.141 0.005 285.823)&quot; ,
 &quot;sidebar-foreground&quot; : &quot;oklch(0.985 0 0)&quot; ,
 &quot;sidebar-border&quot; : &quot;oklch(0.274 0.006 286.033)&quot;
 }
 }
 }
 registry:lib #
 Utility library #
 A registry:lib item is a utility library. Use it to share helper functions, constants, or other non-component code.
 utils.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;utils&quot; ,
 &quot;type&quot; : &quot;registry:lib&quot; ,
 &quot;dependencies&quot; : [ &quot;clsx&quot; , &quot;tailwind-merge&quot; ],
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;lib/utils.ts&quot; ,
 &quot;content&quot; : &quot;import { clsx, type ClassValue } from \&quot; clsx \&quot;\n import { twMerge } from \&quot; tailwind-merge \&quot;\n\n export function cn(...inputs: ClassValue[]) { \n return twMerge(clsx(inputs)) \n }&quot; ,
 &quot;type&quot; : &quot;registry:lib&quot;
 }
 ]
 }
 registry:hook #
 Custom hook #
 A registry:hook item is a custom React hook.
 use-mobile.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;use-mobile&quot; ,
 &quot;type&quot; : &quot;registry:hook&quot; ,
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;hooks/use-mobile.ts&quot; ,
 &quot;content&quot; : &quot;...&quot; ,
 &quot;type&quot; : &quot;registry:hook&quot;
 }
 ]
 }
 Hook with dependencies #
 use-debounce.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;use-debounce&quot; ,
 &quot;type&quot; : &quot;registry:hook&quot; ,
 &quot;dependencies&quot; : [ &quot;react&quot; ],
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;hooks/use-debounce.ts&quot; ,
 &quot;content&quot; : &quot;...&quot; ,
 &quot;type&quot; : &quot;registry:hook&quot;
 }
 ]
 }
 Target Placeholders #
 Use files[].target placeholders when a registry item should install files
under the user&#x27;s configured shadcn directories. The available placeholders are
 @components/ , @ui/ , @lib/ and @hooks/ .
 The placeholders are resolved from components.json , so the same registry item
works in projects using @/ , custom TypeScript aliases, package imports or
workspace package exports.
 Anything after the placeholder is preserved. For example,
 @ui/ai/prompt-input.tsx installs under the user&#x27;s configured ui directory
at ai/prompt-input.tsx .
 alias-child.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;alias-child&quot; ,
 &quot;type&quot; : &quot;registry:item&quot; ,
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;registry/new-york/alias/target-alias-button.tsx&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot; ,
 &quot;target&quot; : &quot;@ui/target-alias-button.tsx&quot; ,
 &quot;content&quot; : &quot;...&quot;
 },
 {
 &quot;path&quot; : &quot;registry/new-york/alias/target-alias-helper.ts&quot; ,
 &quot;type&quot; : &quot;registry:lib&quot; ,
 &quot;target&quot; : &quot;@lib/target-alias-helper.ts&quot; ,
 &quot;content&quot; : &quot;...&quot;
 },
 {
 &quot;path&quot; : &quot;registry/new-york/alias/prompt-input.tsx&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot; ,
 &quot;target&quot; : &quot;@ui/ai/prompt-input.tsx&quot; ,
 &quot;content&quot; : &quot;...&quot;
 }
 ]
 }
 Registry dependencies can use target placeholders too. In the following example,
the child item installs a UI component and a helper, while the parent item
installs an app component and a hook.
 alias-parent.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;alias-parent&quot; ,
 &quot;type&quot; : &quot;registry:item&quot; ,
 &quot;registryDependencies&quot; : [ &quot;https://example.com/r/alias-child.json&quot; ],
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;registry/new-york/alias/target-alias-panel.tsx&quot; ,
 &quot;type&quot; : &quot;registry:component&quot; ,
 &quot;target&quot; : &quot;@components/target-alias-panel.tsx&quot; ,
 &quot;content&quot; : &quot;...&quot;
 },
 {
 &quot;path&quot; : &quot;registry/new-york/alias/use-target-alias.ts&quot; ,
 &quot;type&quot; : &quot;registry:hook&quot; ,
 &quot;target&quot; : &quot;@hooks/use-target-alias.ts&quot; ,
 &quot;content&quot; : &quot;...&quot;
 }
 ]
 }
 The target controls where the file is written, even when it differs from the
file type .
 type-mismatch.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;type-mismatch&quot; ,
 &quot;type&quot; : &quot;registry:item&quot; ,
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;registry/new-york/example/format-date.ts&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot; ,
 &quot;target&quot; : &quot;@lib/format-date.ts&quot; ,
 &quot;content&quot; : &quot;...&quot;
 }
 ]
 }
 registry:font #
 Custom font #
 A registry:font item installs a Google Font. The font field is required and configures the font family, provider, import name, and CSS variable.
 font-inter.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;font-inter&quot; ,
 &quot;type&quot; : &quot;registry:font&quot; ,
 &quot;font&quot; : {
 &quot;family&quot; : &quot;&#x27;Inter Variable&#x27;, sans-serif&quot; ,
 &quot;provider&quot; : &quot;google&quot; ,
 &quot;import&quot; : &quot;Inter&quot; ,
 &quot;variable&quot; : &quot;--font-sans&quot; ,
 &quot;subsets&quot; : [ &quot;latin&quot; ],
 &quot;dependency&quot; : &quot;@fontsource-variable/inter&quot;
 }
 }
 Monospace font #
 font-jetbrains-mono.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;font-jetbrains-mono&quot; ,
 &quot;type&quot; : &quot;registry:font&quot; ,
 &quot;font&quot; : {
 &quot;family&quot; : &quot;&#x27;JetBrains Mono Variable&#x27;, monospace&quot; ,
 &quot;provider&quot; : &quot;google&quot; ,
 &quot;import&quot; : &quot;JetBrains_Mono&quot; ,
 &quot;variable&quot; : &quot;--font-mono&quot; ,
 &quot;weight&quot; : [ &quot;400&quot; , &quot;500&quot; , &quot;600&quot; , &quot;700&quot; ],
 &quot;subsets&quot; : [ &quot;latin&quot; ],
 &quot;dependency&quot; : &quot;@fontsource-variable/jetbrains-mono&quot;
 }
 }
 Serif font #
 font-lora.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;font-lora&quot; ,
 &quot;type&quot; : &quot;registry:font&quot; ,
 &quot;font&quot; : {
 &quot;family&quot; : &quot;&#x27;Lora Variable&#x27;, serif&quot; ,
 &quot;provider&quot; : &quot;google&quot; ,
 &quot;import&quot; : &quot;Lora&quot; ,
 &quot;variable&quot; : &quot;--font-serif&quot; ,
 &quot;subsets&quot; : [ &quot;latin&quot; ],
 &quot;dependency&quot; : &quot;@fontsource-variable/lora&quot;
 }
 }
 Font with custom selector #
 Use the selector field to apply a font to specific CSS selectors instead of globally on html . This is useful for heading fonts or other targeted font applications.
 font-playfair-display.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;font-playfair-display&quot; ,
 &quot;type&quot; : &quot;registry:font&quot; ,
 &quot;font&quot; : {
 &quot;family&quot; : &quot;&#x27;Playfair Display Variable&#x27;, serif&quot; ,
 &quot;provider&quot; : &quot;google&quot; ,
 &quot;import&quot; : &quot;Playfair_Display&quot; ,
 &quot;variable&quot; : &quot;--font-heading&quot; ,
 &quot;subsets&quot; : [ &quot;latin&quot; ],
 &quot;selector&quot; : &quot;h1, h2, h3, h4, h5, h6&quot; ,
 &quot;dependency&quot; : &quot;@fontsource-variable/playfair-display&quot;
 }
 }
 When selector is set, the font utility class (e.g. font-heading ) is applied via CSS @apply on the specified selector within @layer base , instead of being added to the &lt;html&gt; element. The CSS variable is still injected on &lt;html&gt; so it&#x27;s available globally.
 registry:base #
 Custom base #
 A registry:base item is a complete design system base. It defines the full set of dependencies, CSS variables, and configuration for a project. The config field is unique to registry:base items.
 The config field accepts the following properties (all optional):
 Property Type Description style string The style name for the base. iconLibrary string The icon library to use (e.g. lucide ). rsc boolean Whether to enable React Server Components. Defaults to false . tsx boolean Whether to use TypeScript. Defaults to true . rtl boolean Whether to enable right-to-left support. Defaults to false . menuColor &quot;default&quot; | &quot;inverted&quot; | &quot;default-translucent&quot; | &quot;inverted-translucent&quot; The menu color scheme. Defaults to &quot;default&quot; . menuAccent &quot;subtle&quot; | &quot;bold&quot; The menu accent style. Defaults to &quot;subtle&quot; . tailwind.baseColor string The base color name (e.g. neutral , slate , zinc ). tailwind.css string Path to the Tailwind CSS file. tailwind.prefix string A prefix to add to all Tailwind classes. aliases.components string Import alias for components. aliases.utils string Import alias for utilities. aliases.ui string Import alias for UI components. aliases.lib string Import alias for lib. aliases.hooks string Import alias for hooks. registries Record&lt;string, string | object&gt; Custom registry URLs. Keys must start with @ .
 custom-base.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;custom-base&quot; ,
 &quot;type&quot; : &quot;registry:base&quot; ,
 &quot;config&quot; : {
 &quot;style&quot; : &quot;custom-base&quot; ,
 &quot;iconLibrary&quot; : &quot;lucide&quot; ,
 &quot;tailwind&quot; : {
 &quot;baseColor&quot; : &quot;neutral&quot;
 }
 },
 &quot;dependencies&quot; : [
 &quot;class-variance-authority&quot; ,
 &quot;tw-animate-css&quot; ,
 &quot;lucide-react&quot;
 ],
 &quot;registryDependencies&quot; : [ &quot;utils&quot; , &quot;font-inter&quot; ],
 &quot;cssVars&quot; : {
 &quot;light&quot; : {
 &quot;background&quot; : &quot;oklch(1 0 0)&quot; ,
 &quot;foreground&quot; : &quot;oklch(0.141 0.005 285.823)&quot; ,
 &quot;primary&quot; : &quot;oklch(0.21 0.006 285.885)&quot; ,
 &quot;primary-foreground&quot; : &quot;oklch(0.985 0 0)&quot;
 },
 &quot;dark&quot; : {
 &quot;background&quot; : &quot;oklch(0.141 0.005 285.823)&quot; ,
 &quot;foreground&quot; : &quot;oklch(0.985 0 0)&quot; ,
 &quot;primary&quot; : &quot;oklch(0.985 0 0)&quot; ,
 &quot;primary-foreground&quot; : &quot;oklch(0.21 0.006 285.885)&quot;
 }
 },
 &quot;css&quot; : {
 &quot;@import \&quot; tw-animate-css \&quot; &quot; : {},
 &quot;@layer base&quot; : {
 &quot;*&quot; : {
 &quot;@apply border-border outline-ring/50&quot; : {}
 },
 &quot;body&quot; : {
 &quot;@apply bg-background text-foreground&quot; : {}
 }
 }
 }
 }
 Base from scratch #
 Use extends: none to create a base that doesn&#x27;t extend shadcn/ui defaults.
 custom-base.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;my-design-system&quot; ,
 &quot;extends&quot; : &quot;none&quot; ,
 &quot;type&quot; : &quot;registry:base&quot; ,
 &quot;config&quot; : {
 &quot;style&quot; : &quot;my-design-system&quot; ,
 &quot;iconLibrary&quot; : &quot;lucide&quot; ,
 &quot;tailwind&quot; : {
 &quot;baseColor&quot; : &quot;slate&quot;
 }
 },
 &quot;dependencies&quot; : [ &quot;tailwind-merge&quot; , &quot;clsx&quot; , &quot;tw-animate-css&quot; , &quot;lucide-react&quot; ],
 &quot;registryDependencies&quot; : [ &quot;utils&quot; , &quot;font-geist&quot; ],
 &quot;cssVars&quot; : {
 &quot;light&quot; : {
 &quot;background&quot; : &quot;oklch(1 0 0)&quot; ,
 &quot;foreground&quot; : &quot;oklch(0.141 0.005 285.823)&quot;
 },
 &quot;dark&quot; : {
 &quot;background&quot; : &quot;oklch(0.141 0.005 285.823)&quot; ,
 &quot;foreground&quot; : &quot;oklch(0.985 0 0)&quot;
 }
 }
 }
 Common Fields #
 Author #
 Use the author field to add attribution to your registry items.
 example-item.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;custom-component&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot; ,
 &quot;author&quot; : &quot;shadcn&quot; ,
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;ui/custom-component.tsx&quot; ,
 &quot;content&quot; : &quot;...&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot;
 }
 ]
 }
 Dev dependencies #
 Use the devDependencies field to install packages as dev dependencies.
 example-item.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;custom-item&quot; ,
 &quot;type&quot; : &quot;registry:item&quot; ,
 &quot;devDependencies&quot; : [ &quot;@types/mdx&quot; ],
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;lib/mdx.ts&quot; ,
 &quot;content&quot; : &quot;...&quot; ,
 &quot;type&quot; : &quot;registry:lib&quot;
 }
 ]
 }
 Metadata #
 Use the meta field to attach arbitrary metadata to your registry items. This can be used to store custom data that your tools or scripts can use.
 example-item.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;custom-component&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot; ,
 &quot;meta&quot; : {
 &quot;category&quot; : &quot;forms&quot; ,
 &quot;version&quot; : &quot;2.0.0&quot;
 },
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;ui/custom-component.tsx&quot; ,
 &quot;content&quot; : &quot;...&quot; ,
 &quot;type&quot; : &quot;registry:ui&quot;
 }
 ]
 }
 CSS Variables #
 Custom Theme Variables #
 Add custom theme variables to the theme object.
 example-theme.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;custom-theme&quot; ,
 &quot;type&quot; : &quot;registry:theme&quot; ,
 &quot;cssVars&quot; : {
 &quot;theme&quot; : {
 &quot;font-heading&quot; : &quot;Inter, sans-serif&quot; ,
 &quot;shadow-card&quot; : &quot;0 0 0 1px rgba(0, 0, 0, 0.1)&quot;
 }
 }
 }
 Override Tailwind CSS variables #
 example-theme.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;custom-theme&quot; ,
 &quot;type&quot; : &quot;registry:theme&quot; ,
 &quot;cssVars&quot; : {
 &quot;theme&quot; : {
 &quot;spacing&quot; : &quot;0.2rem&quot; ,
 &quot;breakpoint-sm&quot; : &quot;640px&quot; ,
 &quot;breakpoint-md&quot; : &quot;768px&quot; ,
 &quot;breakpoint-lg&quot; : &quot;1024px&quot; ,
 &quot;breakpoint-xl&quot; : &quot;1280px&quot; ,
 &quot;breakpoint-2xl&quot; : &quot;1536px&quot;
 }
 }
 }
 Add custom CSS #
 Base styles #
 example-base.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;custom-style&quot; ,
 &quot;type&quot; : &quot;registry:style&quot; ,
 &quot;css&quot; : {
 &quot;@layer base&quot; : {
 &quot;h1&quot; : {
 &quot;font-size&quot; : &quot;var(--text-2xl)&quot;
 },
 &quot;h2&quot; : {
 &quot;font-size&quot; : &quot;var(--text-xl)&quot;
 }
 }
 }
 }
 Components #
 example-card.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;custom-card&quot; ,
 &quot;type&quot; : &quot;registry:component&quot; ,
 &quot;css&quot; : {
 &quot;@layer components&quot; : {
 &quot;card&quot; : {
 &quot;background-color&quot; : &quot;var(--color-white)&quot; ,
 &quot;border-radius&quot; : &quot;var(--rounded-lg)&quot; ,
 &quot;padding&quot; : &quot;var(--spacing-6)&quot; ,
 &quot;box-shadow&quot; : &quot;var(--shadow-xl)&quot;
 }
 }
 }
 }
 Add custom utilities #
 Simple utility #
 example-component.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;custom-component&quot; ,
 &quot;type&quot; : &quot;registry:component&quot; ,
 &quot;css&quot; : {
 &quot;@utility content-auto&quot; : {
 &quot;content-visibility&quot; : &quot;auto&quot;
 }
 }
 }
 Complex utility #
 example-utility.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;custom-component&quot; ,
 &quot;type&quot; : &quot;registry:component&quot; ,
 &quot;css&quot; : {
 &quot;@utility scrollbar-hidden&quot; : {
 &quot;scrollbar-hidden&quot; : {
 &quot;&amp;::-webkit-scrollbar&quot; : {
 &quot;display&quot; : &quot;none&quot;
 }
 }
 }
 }
 }
 Functional utilities #
 example-functional.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;custom-component&quot; ,
 &quot;type&quot; : &quot;registry:component&quot; ,
 &quot;css&quot; : {
 &quot;@utility tab-*&quot; : {
 &quot;tab-size&quot; : &quot;var(--tab-size-*)&quot;
 }
 }
 }
 Add CSS imports #
 Use @import to add CSS imports to your registry item. The imports will be placed at the top of the CSS file.
 Basic import #
 example-import.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;custom-import&quot; ,
 &quot;type&quot; : &quot;registry:component&quot; ,
 &quot;css&quot; : {
 &quot;@import \&quot; tailwindcss \&quot; &quot; : {},
 &quot;@import \&quot; ./styles/base.css \&quot; &quot; : {}
 }
 }
 Import with url() syntax #
 example-url-import.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;font-import&quot; ,
 &quot;type&quot; : &quot;registry:item&quot; ,
 &quot;css&quot; : {
 &quot;@import url( \&quot; https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;display=swap \&quot; )&quot; : {},
 &quot;@import url(&#x27;./local-styles.css&#x27;)&quot; : {}
 }
 }
 Import with media queries #
 example-media-import.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;responsive-import&quot; ,
 &quot;type&quot; : &quot;registry:item&quot; ,
 &quot;css&quot; : {
 &quot;@import \&quot; print-styles.css \&quot; print&quot; : {},
 &quot;@import url( \&quot; mobile.css \&quot; ) screen and (max-width: 768px)&quot; : {}
 }
 }
 Add custom plugins #
 Use @plugin to add Tailwind plugins to your registry item. Plugins will be automatically placed after imports and before other content.
 Important: When using plugins from npm packages, you must also add them to the dependencies array.
 Basic plugin usage #
 example-plugin.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;custom-plugin&quot; ,
 &quot;type&quot; : &quot;registry:item&quot; ,
 &quot;css&quot; : {
 &quot;@plugin \&quot; @tailwindcss/typography \&quot; &quot; : {},
 &quot;@plugin \&quot; foo \&quot; &quot; : {}
 }
 }
 Plugin with npm dependency #
 When using plugins from npm packages like @tailwindcss/typography , include them in the dependencies.
 example-typography.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;typography-component&quot; ,
 &quot;type&quot; : &quot;registry:item&quot; ,
 &quot;dependencies&quot; : [ &quot;@tailwindcss/typography&quot; ],
 &quot;css&quot; : {
 &quot;@plugin \&quot; @tailwindcss/typography \&quot; &quot; : {},
 &quot;@layer components&quot; : {
 &quot;.prose&quot; : {
 &quot;max-width&quot; : &quot;65ch&quot;
 }
 }
 }
 }
 Scoped and file-based plugins #
 example-scoped-plugin.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;scoped-plugins&quot; ,
 &quot;type&quot; : &quot;registry:component&quot; ,
 &quot;css&quot; : {
 &quot;@plugin \&quot; @headlessui/tailwindcss \&quot; &quot; : {},
 &quot;@plugin \&quot; tailwindcss/plugin \&quot; &quot; : {},
 &quot;@plugin \&quot; ./custom-plugin.js \&quot; &quot; : {}
 }
 }
 Multiple plugins with automatic ordering #
 When you add multiple plugins, they are automatically grouped together and deduplicated.
 example-multiple-plugins.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;multiple-plugins&quot; ,
 &quot;type&quot; : &quot;registry:item&quot; ,
 &quot;dependencies&quot; : [
 &quot;@tailwindcss/typography&quot; ,
 &quot;@tailwindcss/forms&quot; ,
 &quot;tw-animate-css&quot;
 ],
 &quot;css&quot; : {
 &quot;@plugin \&quot; @tailwindcss/typography \&quot; &quot; : {},
 &quot;@plugin \&quot; @tailwindcss/forms \&quot; &quot; : {},
 &quot;@plugin \&quot; tw-animate-css \&quot; &quot; : {}
 }
 }
 Combined imports and plugins #
 When using both @import and @plugin directives, imports are placed first, followed by plugins, then other CSS content.
 example-combined.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;combined-example&quot; ,
 &quot;type&quot; : &quot;registry:item&quot; ,
 &quot;dependencies&quot; : [ &quot;@tailwindcss/typography&quot; , &quot;tw-animate-css&quot; ],
 &quot;css&quot; : {
 &quot;@import \&quot; tailwindcss \&quot; &quot; : {},
 &quot;@import url( \&quot; https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;display=swap \&quot; )&quot; : {},
 &quot;@plugin \&quot; @tailwindcss/typography \&quot; &quot; : {},
 &quot;@plugin \&quot; tw-animate-css \&quot; &quot; : {},
 &quot;@layer base&quot; : {
 &quot;body&quot; : {
 &quot;font-family&quot; : &quot;Inter, sans-serif&quot;
 }
 },
 &quot;@utility content-auto&quot; : {
 &quot;content-visibility&quot; : &quot;auto&quot;
 }
 }
 }
 Add custom animations #
 Note: you need to define both @keyframes in css and theme in cssVars to use animations.
 example-component.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;custom-component&quot; ,
 &quot;type&quot; : &quot;registry:component&quot; ,
 &quot;cssVars&quot; : {
 &quot;theme&quot; : {
 &quot;--animate-wiggle&quot; : &quot;wiggle 1s ease-in-out infinite&quot;
 }
 },
 &quot;css&quot; : {
 &quot;@keyframes wiggle&quot; : {
 &quot;0%, 100%&quot; : {
 &quot;transform&quot; : &quot;rotate(-3deg)&quot;
 },
 &quot;50%&quot; : {
 &quot;transform&quot; : &quot;rotate(3deg)&quot;
 }
 }
 }
 }
 Add environment variables #
 You can add environment variables using the envVars field.
 example-item.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;custom-item&quot; ,
 &quot;type&quot; : &quot;registry:item&quot; ,
 &quot;envVars&quot; : {
 &quot;NEXT_PUBLIC_APP_URL&quot; : &quot;http://localhost:4000&quot; ,
 &quot;DATABASE_URL&quot; : &quot;postgresql://postgres:postgres@localhost:5432/postgres&quot; ,
 &quot;OPENAI_API_KEY&quot; : &quot;&quot;
 }
 }
 Environment variables are added to the .env.local or .env file. Existing variables are not overwritten.
 IMPORTANT: Use envVars to add development or example variables. Do NOT use it to add production variables.
 Universal Items #
 As of 2.9.0 , you can create universal items that can be installed without framework detection or components.json.
 To make an item universal i.e framework agnostic, all the files in the item must have an explicit target.
 Here&#x27;s an example of a registry item that installs custom Cursor rules for python :
 .cursor/rules/custom-python.mdc Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;python-rules&quot; ,
 &quot;type&quot; : &quot;registry:item&quot; ,
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;/path/to/your/registry/default/custom-python.mdc&quot; ,
 &quot;type&quot; : &quot;registry:file&quot; ,
 &quot;target&quot; : &quot;~/.cursor/rules/custom-python.mdc&quot; ,
 &quot;content&quot; : &quot;...&quot;
 }
 ]
 }
 Here&#x27;s another example for installing a custom ESLint config:
 .eslintrc.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;my-eslint-config&quot; ,
 &quot;type&quot; : &quot;registry:item&quot; ,
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;/path/to/your/registry/default/custom-eslint.json&quot; ,
 &quot;type&quot; : &quot;registry:file&quot; ,
 &quot;target&quot; : &quot;~/.eslintrc.json&quot; ,
 &quot;content&quot; : &quot;...&quot;
 }
 ]
 }
 You can also have a universal item that installs multiple files:
 my-custom-starter-template.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry-item.json&quot; ,
 &quot;name&quot; : &quot;my-custom-starter-template&quot; ,
 &quot;type&quot; : &quot;registry:item&quot; ,
 &quot;dependencies&quot; : [ &quot;better-auth&quot; ],
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;/path/to/file-01.json&quot; ,
 &quot;type&quot; : &quot;registry:file&quot; ,
 &quot;target&quot; : &quot;~/file-01.json&quot; ,
 &quot;content&quot; : &quot;...&quot;
 },
 {
 &quot;path&quot; : &quot;/path/to/file-02.vue&quot; ,
 &quot;type&quot; : &quot;registry:file&quot; ,
 &quot;target&quot; : &quot;~/pages/file-02.vue&quot; ,
 &quot;content&quot; : &quot;...&quot;
 }
 ]
 } Registry Directory Namespaces On This Page registry:style Custom style that extends shadcn/ui Custom style from scratch registry:theme Custom theme Custom colors registry:block Custom block Install a block and override primitives registry:ui UI component UI component with CSS variables registry:lib Utility library registry:hook Custom hook Hook with dependencies Target Placeholders registry:font Custom font Monospace font Serif font Font with custom selector registry:base Custom base Base from scratch Common Fields Author Dev dependencies Metadata CSS Variables Custom Theme Variables Override Tailwind CSS variables Add custom CSS Base styles Components Add custom utilities Simple utility Complex utility Functional utilities Add CSS imports Basic import Import with url() syntax Import with media queries Add custom plugins Basic plugin usage Plugin with npm dependency Scoped and file-based plugins Multiple plugins with automatic ordering Combined imports and plugins Add custom animations Add environment variables Universal Items Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
