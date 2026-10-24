Accordion - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Accordion Copy Page Previous Next A vertically stacked set of interactive headings that each reveal a section of content. Radix UI Base UI Radix UI What are your shipping options? We offer standard (5-7 days), express (2-3 days), and overnight shipping. Free shipping on international orders. What is your return policy? How can I contact customer support? Copy import {
 Accordion,
 AccordionContent, View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add accordion Copy
 Usage #
 Copy import {
 Accordion,
 AccordionContent,
 AccordionItem,
 AccordionTrigger,
 } from &quot;@/components/ui/accordion&quot;
 Copy &lt; Accordion type = &quot;single&quot; collapsible defaultValue = &quot;item-1&quot; &gt;
 &lt; AccordionItem value = &quot;item-1&quot; &gt;
 &lt; AccordionTrigger &gt;Is it accessible?&lt;/ AccordionTrigger &gt;
 &lt; AccordionContent &gt;
 Yes. It adheres to the WAI-ARIA design pattern.
 &lt;/ AccordionContent &gt;
 &lt;/ AccordionItem &gt;
 &lt;/ Accordion &gt;
 Composition #
 Use the following composition to build an Accordion :
 Copy Accordion
 ├── AccordionItem
 │ ├── AccordionTrigger
 │ └── AccordionContent
 └── AccordionItem
 ├── AccordionTrigger
 └── AccordionContent
 Examples #
 Basic #
 A basic accordion that shows one item at a time. The first item is open by default.
 How do I reset my password? Click on &#x27;Forgot Password&#x27; on the login page, enter your email address, and we&#x27;ll send you a link to reset your password. The link will expire in 24 hours. Can I change my subscription plan? What payment methods do you accept? Copy import {
 Accordion,
 AccordionContent, View Code
 Multiple #
 Use type=&quot;multiple&quot; to allow multiple items to be open at the same time.
 Notification Settings Manage how you receive notifications. You can enable email alerts for updates or push notifications for mobile devices. Privacy &amp; Security Billing &amp; Subscription Copy import {
 Accordion,
 AccordionContent, View Code
 Disabled #
 Use the disabled prop on AccordionItem to disable individual items.
 Can I access my account history? Premium feature information How do I update my email address? Copy import {
 Accordion,
 AccordionContent, View Code
 Borders #
 Add border to the Accordion and border-b last:border-b-0 to the AccordionItem to add borders to the items.
 How does billing work? We offer monthly and annual subscription plans. Billing is charged at the beginning of each cycle, and you can cancel anytime. All plans include automatic backups, 24/7 support, and unlimited team members. Is my data secure? What integrations do you support? Copy import {
 Accordion,
 AccordionContent, View Code
 Card #
 Wrap the Accordion in a Card component.
 Subscription &amp; Billing Common questions about your account, plans, payments and cancellations. What subscription plans do you offer? We offer three subscription tiers: Starter ($9/month), Professional ($29/month), and Enterprise ($99/month). Each plan includes increasing storage limits, API access, priority support, and team collaboration features. How does billing work? How do I cancel my subscription? Copy import {
 Accordion,
 AccordionContent, View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle كيف يمكنني إعادة تعيين كلمة المرور؟ انقر على &#x27;نسيت كلمة المرور&#x27; في صفحة تسجيل الدخول، أدخل عنوان بريدك الإلكتروني، وسنرسل لك رابطًا لإعادة تعيين كلمة المرور. سينتهي صلاحية الرابط خلال 24 ساعة. هل يمكنني تغيير خطة الاشتراك الخاصة بي؟ ما هي طرق الدفع التي تقبلونها؟ Copy "use client"

 import { View Code
 API Reference #
 See the Radix UI documentation for more information. Typography Alert On This Page Installation Usage Composition Examples Basic Multiple Disabled Borders Card RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
