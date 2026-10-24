Gatsby - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Gatsby Copy Page Previous Next Install and configure shadcn/ui for Gatsby. Note: This guide is for Gatsby with Tailwind CSS v3. For new projects, we
recommend using one of the other frameworks that support Tailwind CSS v4.
 Create project # Start by creating a new Gatsby project using create-gatsby : Copy npm init gatsby Configure your Gatsby project to use TypeScript and Tailwind CSS # You will be asked a few questions to configure your project: Copy ✔ What would you like to call your site?
 · your-app-name
 ✔ What would you like to name the folder where your site will be created?
 · your-app-name
 ✔ Will you be using JavaScript or TypeScript?
 · TypeScript
 ✔ Will you be using a CMS?
 · Choose whatever you want
 ✔ Would you like to install a styling system?
 · Tailwind CSS
 ✔ Would you like to install additional features with other plugins?
 · Choose whatever you want
 ✔ Shall we do this? (Y/n) · Yes Edit tsconfig.json file # Add the following code to the tsconfig.json file to resolve paths: Copy {
 &quot;compilerOptions&quot; : {
 // ...
 &quot;baseUrl&quot; : &quot;.&quot; ,
 &quot;paths&quot; : {
 &quot;@/*&quot; : [
 &quot;./src/*&quot;
 ]
 }
 // ...
 }
 } Create gatsby-node.ts file # Create a gatsby-node.ts file at the root of your project if it doesn’t already exist, and add the code below to the gatsby-node file so your app can resolve paths: Copy import * as path from &quot;path&quot;

 export const onCreateWebpackConfig = ({ actions }) =&gt; {
 actions. setWebpackConfig ({
 resolve: {
 alias: {
 &quot;@/components&quot; : path. resolve (__dirname, &quot;src/components&quot; ),
 &quot;@/lib/utils&quot; : path. resolve (__dirname, &quot;src/lib/utils&quot; ),
 },
 },
 })
 } Run the CLI # Run the shadcn init command to set up your project: pnpm npm yarn bun pnpm dlx shadcn@latest init Copy That&#x27;s it # You can now start adding components to your project. pnpm npm yarn bun pnpm dlx shadcn@latest add button Copy The command above will add the Button component to your project. You can then import it like this: Copy import { Button } from &quot;@/components/ui/button&quot;

 export default function Home () {
 return (
 &lt; div &gt;
 &lt; Button &gt;Click me&lt;/ Button &gt;
 &lt;/ div &gt;
 )
 } Next.js FAQ On This Page Create project Configure your Gatsby project to use TypeScript and Tailwind CSS Edit tsconfig.json file Create gatsby-node.ts file Run the CLI That&#x27;s it Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
