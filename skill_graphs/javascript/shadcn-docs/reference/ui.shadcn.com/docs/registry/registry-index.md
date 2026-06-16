Registry Directory - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Registry Directory Copy Page Previous Next Open Source Registry Index The open source registry index is a list of all the open source registries that are available to use out of the box.
 When you run shadcn add or shadcn search , the CLI will automatically check the registry index for the registry you are looking for and add it to your components.json file.
 You can see the full list at https://ui.shadcn.com/r/registries.json .
 You do not need to submit a public GitHub registry to the registry directory to
use it with owner/repo/item addresses. The registry directory is for
namespaces such as @acme .
 Adding a Registry #

 Add your registry to apps/v4/registry/directory.json
 Run pnpm validate:registries to validate the registry directory.
 Create a pull request to https://github.com/shadcn-ui/ui

 Once you have submitted your request, it will be validated and reviewed by the team.
 Requirements #

 The registry must be open source and publicly accessible.
 The registry must be a valid JSON file that conforms to the registry schema specification .
 The registry is expected to be a flat registry with no nested items i.e /registry.json and /component-name.json files are expected to be in the root of the registry.
 The files array, if present, must NOT include a content property.

 Here&#x27;s an example of a valid registry:
 registry.json Copy {
 &quot;$schema&quot; : &quot;https://ui.shadcn.com/schema/registry.json&quot; ,
 &quot;name&quot; : &quot;acme&quot; ,
 &quot;homepage&quot; : &quot;https://acme.com&quot; ,
 &quot;items&quot; : [
 {
 &quot;name&quot; : &quot;login-form&quot; ,
 &quot;type&quot; : &quot;registry:component&quot; ,
 &quot;title&quot; : &quot;Login Form&quot; ,
 &quot;description&quot; : &quot;A login form component.&quot; ,
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;registry/new-york/auth/login-form.tsx&quot; ,
 &quot;type&quot; : &quot;registry:component&quot;
 }
 ]
 },
 {
 &quot;name&quot; : &quot;example-login-form&quot; ,
 &quot;type&quot; : &quot;registry:component&quot; ,
 &quot;title&quot; : &quot;Example Login Form&quot; ,
 &quot;description&quot; : &quot;An example showing how to use the login form component.&quot; ,
 &quot;files&quot; : [
 {
 &quot;path&quot; : &quot;registry/new-york/examples/example-login-form.tsx&quot; ,
 &quot;type&quot; : &quot;registry:component&quot;
 }
 ]
 }
 ]
 } GitHub Registries Examples On This Page Adding a Registry Requirements Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
