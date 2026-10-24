Authentication - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Authentication Copy Page Previous Next Secure your registry with authentication for private and personalized components. Authentication lets you run private registries, control who can access your components, and give different teams or users different content. This guide shows common authentication patterns and how to set them up.
 Authentication enables these use cases:

 Private Components : Keep your business logic and internal components secure
 Team-Specific Resources : Give different teams different components
 Access Control : Limit who can see sensitive or experimental components
 Usage Analytics : See who&#x27;s using which components in your organization
 Licensing : Control who gets premium or licensed components

 Common Authentication Patterns #
 Token-Based Authentication #
 The most common approach uses Bearer tokens or API keys:
 components.json Copy {
 &quot;registries&quot; : {
 &quot;@private&quot; : {
 &quot;url&quot; : &quot;https://registry.company.com/{name}.json&quot; ,
 &quot;headers&quot; : {
 &quot;Authorization&quot; : &quot;Bearer ${REGISTRY_TOKEN}&quot;
 }
 }
 }
 }
 Set your token in environment variables:
 .env.local Copy REGISTRY_TOKEN = your_secret_token_here
 API Key Authentication #
 Some registries use API keys in headers:
 components.json Copy {
 &quot;registries&quot; : {
 &quot;@company&quot; : {
 &quot;url&quot; : &quot;https://api.company.com/registry/{name}.json&quot; ,
 &quot;headers&quot; : {
 &quot;X-API-Key&quot; : &quot;${API_KEY}&quot; ,
 &quot;X-Workspace-Id&quot; : &quot;${WORKSPACE_ID}&quot;
 }
 }
 }
 }
 Query Parameter Authentication #
 For simpler setups, use query parameters:
 components.json Copy {
 &quot;registries&quot; : {
 &quot;@internal&quot; : {
 &quot;url&quot; : &quot;https://registry.company.com/{name}.json&quot; ,
 &quot;params&quot; : {
 &quot;token&quot; : &quot;${ACCESS_TOKEN}&quot;
 }
 }
 }
 }
 This creates: https://registry.company.com/button.json?token=your_token
 Server-Side Implementation #
 Here&#x27;s how to add authentication to your registry server:
 Next.js API Route Example #
 app/api/registry/[name]/route.ts Copy import { NextRequest, NextResponse } from &quot;next/server&quot;

 export async function GET (
 request : NextRequest ,
 { params } : { params : { name : string } }
 ) {
 // Get token from Authorization header.
 const authHeader = request.headers. get ( &quot;authorization&quot; )
 const token = authHeader?. replace ( &quot;Bearer &quot; , &quot;&quot; )

 // Or from query parameters.
 const queryToken = request.nextUrl.searchParams. get ( &quot;token&quot; )

 // Check if token is valid.
 if ( ! isValidToken (token || queryToken)) {
 return NextResponse. json ({ error: &quot;Unauthorized&quot; }, { status: 401 })
 }

 // Check if token can access this component.
 if ( ! hasAccessToComponent (token, params.name)) {
 return NextResponse. json ({ error: &quot;Forbidden&quot; }, { status: 403 })
 }

 // Return the component.
 const component = await getComponent (params.name)
 return NextResponse. json (component)
 }

 function isValidToken ( token : string | null ) {
 // Add your token validation logic here.
 // Check against database, JWT validation, etc.
 return token === process.env. VALID_TOKEN
 }

 function hasAccessToComponent ( token : string , componentName : string ) {
 // Add role-based access control here.
 // Check if token can access specific component.
 return true // Your logic here.
 }
 Express.js Example #
 server.js Copy app. get ( &quot;/registry/:name.json&quot; , ( req , res ) =&gt; {
 const token = req.headers.authorization?. replace ( &quot;Bearer &quot; , &quot;&quot; )

 if ( ! isValidToken (token)) {
 return res. status ( 401 ). json ({ error: &quot;Unauthorized&quot; })
 }

 const component = getComponent (req.params.name)
 if ( ! component) {
 return res. status ( 404 ). json ({ error: &quot;Component not found&quot; })
 }

 res. json (component)
 })
 Advanced Authentication Patterns #
 Team-Based Access #
 Give different teams different components:
 api/registry/route.ts Copy async function GET ( request : NextRequest ) {
 const token = extractToken (request)
 const team = await getTeamFromToken (token)

 // Get components for this team.
 const components = await getComponentsForTeam (team)
 return NextResponse. json (components)
 }
 User-Personalized Registries #
 Give users components based on their preferences:
 Copy async function GET ( request : NextRequest ) {
 const user = await authenticateUser (request)

 // Get user&#x27;s style and framework preferences.
 const preferences = await getUserPreferences (user.id)

 // Get personalized component version.
 const component = await getPersonalizedComponent (params.name, preferences)

 return NextResponse. json (component)
 }
 Temporary Access Tokens #
 Use expiring tokens for better security:
 Copy interface TemporaryToken {
 token : string
 expiresAt : Date
 scope : string []
 }

 async function validateTemporaryToken ( token : string ) {
 const tokenData = await getTokenData (token)

 if ( ! tokenData) return false
 if ( new Date () &gt; tokenData.expiresAt) return false

 return true
 }
 Multi-Registry Authentication #
 With namespaced registries , you can set up multiple registries with different authentication:
 components.json Copy {
 &quot;registries&quot; : {
 &quot;@public&quot; : &quot;https://public.company.com/{name}.json&quot; ,
 &quot;@internal&quot; : {
 &quot;url&quot; : &quot;https://internal.company.com/{name}.json&quot; ,
 &quot;headers&quot; : {
 &quot;Authorization&quot; : &quot;Bearer ${INTERNAL_TOKEN}&quot;
 }
 },
 &quot;@premium&quot; : {
 &quot;url&quot; : &quot;https://premium.company.com/{name}.json&quot; ,
 &quot;headers&quot; : {
 &quot;X-License-Key&quot; : &quot;${LICENSE_KEY}&quot;
 }
 }
 }
 }
 This lets you:

 Mix public and private registries
 Use different authentication per registry
 Organize components by access level

 Security Best Practices #
 Use Environment Variables #
 Never commit tokens to version control. Always use environment variables:
 .env.local Copy REGISTRY_TOKEN = your_secret_token_here
 API_KEY = your_api_key_here
 Then reference them in components.json :
 Copy {
 &quot;registries&quot; : {
 &quot;@private&quot; : {
 &quot;url&quot; : &quot;https://registry.company.com/{name}.json&quot; ,
 &quot;headers&quot; : {
 &quot;Authorization&quot; : &quot;Bearer ${REGISTRY_TOKEN}&quot;
 }
 }
 }
 }
 Use HTTPS #
 Always use HTTPS URLs for registries to protect your tokens in transit:
 Copy {
 &quot;@secure&quot; : &quot;https://registry.company.com/{name}.json&quot; // ✅
 &quot;@insecure&quot; : &quot;http://registry.company.com/{name}.json&quot; // ❌
 }
 Add Rate Limiting #
 Protect your registry from abuse:
 Copy import rateLimit from &quot;express-rate-limit&quot;

 const limiter = rateLimit ({
 windowMs: 15 * 60 * 1000 , // 15 minutes
 max: 100 , // limit each IP to 100 requests per windowMs
 })

 app. use ( &quot;/registry&quot; , limiter)
 Rotate Tokens #
 Change access tokens regularly:
 Copy // Create new token with expiration.
 function generateToken () {
 const token = crypto. randomBytes ( 32 ). toString ( &quot;hex&quot; )
 const expiresAt = new Date (Date. now () + 30 * 24 * 60 * 60 * 1000 ) // 30 days.

 return { token, expiresAt }
 }
 Log Access #
 Track registry access for security and analytics:
 Copy async function logAccess ( request : Request , component : string , userId : string ) {
 await db.accessLog. create ({
 timestamp: new Date (),
 userId,
 component,
 ip: request.ip,
 userAgent: request.headers[ &quot;user-agent&quot; ],
 })
 }
 Testing Authentication #
 Test your authenticated registry locally:
 Copy # Test with curl.
 curl -H &quot;Authorization: Bearer your_token&quot; \
 https://registry.company.com/button.json

 # Test with the CLI.
 REGISTRY_TOKEN = your_token npx shadcn@latest add @private/button
 Error Handling #
 The shadcn CLI handles authentication errors gracefully:

 401 Unauthorized : Token is invalid or missing
 403 Forbidden : Token lacks permission for this resource
 429 Too Many Requests : Rate limit exceeded

 Custom Error Messages #
 Your registry server can return custom error messages in the response body, and the CLI will display them to users:
 Copy // Registry server returns custom error
 return NextResponse. json (
 {
 error: &quot;Unauthorized&quot; ,
 message:
 &quot;Your subscription has expired. Please renew at company.com/billing&quot; ,
 },
 { status: 403 }
 )
 The user will see:
 Copy Your subscription has expired. Please renew at company.com/billing
 This helps provide context-specific guidance:
 Copy // Different error messages for different scenarios
 if ( ! token) {
 return NextResponse. json (
 {
 error: &quot;Unauthorized&quot; ,
 message:
 &quot;Authentication required. Set REGISTRY_TOKEN in your .env.local file&quot; ,
 },
 { status: 401 }
 )
 }

 if ( isExpiredToken (token)) {
 return NextResponse. json (
 {
 error: &quot;Unauthorized&quot; ,
 message: &quot;Token expired. Request a new token at company.com/tokens&quot; ,
 },
 { status: 401 }
 )
 }

 if ( ! hasTeamAccess (token, component)) {
 return NextResponse. json (
 {
 error: &quot;Forbidden&quot; ,
 message: `Component &#x27;${ component }&#x27; is restricted to the Design team` ,
 },
 { status: 403 }
 )
 }
 Next Steps #
 To set up authentication with multiple registries and advanced patterns, see the Namespaced Registries documentation. It covers:

 Setting up multiple authenticated registries
 Using different authentication per namespace
 Cross-registry dependency resolution
 Advanced authentication patterns
 Namespaces MCP Server On This Page Common Authentication Patterns Token-Based Authentication API Key Authentication Query Parameter Authentication Server-Side Implementation Next.js API Route Example Express.js Example Advanced Authentication Patterns Team-Based Access User-Personalized Registries Temporary Access Tokens Multi-Registry Authentication Security Best Practices Use Environment Variables Use HTTPS Add Rate Limiting Rotate Tokens Log Access Testing Authentication Error Handling Custom Error Messages Next Steps Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
