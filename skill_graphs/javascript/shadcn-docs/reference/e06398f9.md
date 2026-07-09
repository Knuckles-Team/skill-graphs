Open in v0 - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Open in v0 Copy Page Previous Next Integrate your registry with Open in v0. If your registry is hosted and publicly accessible via a URL, you can open a registry item in v0 by using the https://v0.dev/chat/api/open?url=[URL] endpoint.
 eg. https://v0.dev/chat/api/open?url=https://ui.shadcn.com/r/styles/new-york/login-01.json
 Important: Open in v0 does not support cssVars , css , envVars ,
namespaced registries, or advanced authentication methods.
 Button #
 See Build your Open in v0 button for more information on how to build your own Open in v0 button.
 Here&#x27;s a simple example of how to add a Open in v0 button to your site.
 Copy import { Button } from &quot;@/components/ui/button&quot;

 export function OpenInV0Button ({ url } : { url : string }) {
 return (
 &lt; Button
 aria-label = &quot;Open in v0&quot;
 className = &quot;h-8 gap-1 rounded-[6px] bg-black px-3 text-xs text-white hover:bg-black hover:text-white dark:bg-white dark:text-black&quot;
 asChild
 &gt;
 &lt; a
 href = { `https://v0.dev/chat/api/open?url=${ url }` }
 target = &quot;_blank&quot;
 rel = &quot;noreferrer&quot;
 &gt;
 Open in { &quot; &quot; }
 &lt; svg
 viewBox = &quot;0 0 40 20&quot;
 fill = &quot;none&quot;
 xmlns = &quot;http://www.w3.org/2000/svg&quot;
 className = &quot;h-5 w-5 text-current&quot;
 &gt;
 &lt; path
 d = &quot;M23.3919 0H32.9188C36.7819 0 39.9136 3.13165 39.9136 6.99475V16.0805H36.0006V6.99475C36.0006 6.90167 35.9969 6.80925 35.9898 6.71766L26.4628 16.079C26.4949 16.08 26.5272 16.0805 26.5595 16.0805H36.0006V19.7762H26.5595C22.6964 19.7762 19.4788 16.6139 19.4788 12.7508V3.68923H23.3919V12.7508C23.3919 12.9253 23.4054 13.0977 23.4316 13.2668L33.1682 3.6995C33.0861 3.6927 33.003 3.68923 32.9188 3.68923H23.3919V0Z&quot;
 fill = &quot;currentColor&quot;
 &gt;&lt;/ path &gt;
 &lt; path
 d = &quot;M13.7688 19.0956L0 3.68759H5.53933L13.6231 12.7337V3.68759H17.7535V17.5746C17.7535 19.6705 15.1654 20.6584 13.7688 19.0956Z&quot;
 fill = &quot;currentColor&quot;
 &gt;&lt;/ path &gt;
 &lt;/ svg &gt;
 &lt;/ a &gt;
 &lt;/ Button &gt;
 )
 }
 Copy &lt; OpenInV0Button url = &quot;https://example.com/r/hello-world.json&quot; /&gt;
 Authentication #
 Open in v0 only supports query parameter authentication. It does not support namespaced registries or advanced authentication methods like Bearer tokens or API keys in headers.
 Using Query Parameter Authentication #
 To add authentication to your registry for Open in v0, use a token query parameter:
 https://registry.company.com/r/hello-world.json?token=your_secure_token_here

 When implementing this on your registry server:

 Check for the token query parameter
 Validate the token against your authentication system
 Return a 401 Unauthorized response if the token is invalid or missing
 Both the shadcn CLI and Open in v0 will handle the 401 response and display an appropriate message to users

 Example Implementation #
 Copy // Next.js API route example
 export async function GET ( request : NextRequest ) {
 const token = request.nextUrl.searchParams. get ( &quot;token&quot; )

 if ( ! isValidToken (token)) {
 return NextResponse. json (
 {
 error: &quot;Unauthorized&quot; ,
 message: &quot;Invalid or missing token&quot; ,
 },
 { status: 401 }
 )
 }

 // Return the registry item
 return NextResponse. json (registryItem)
 }
 Security Note: Make sure to encrypt and expire tokens. Never expose
production tokens in documentation or examples. MCP Server API Reference On This Page Button Authentication Using Query Parameter Authentication Example Implementation Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
