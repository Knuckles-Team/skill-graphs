Carousel - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Carousel Copy Page Previous Next A carousel with motion and swipe built using Embla. Radix UI Base UI Radix UI 1 2 3 4 5 Previous slide Next slide Copy import * as React from "react"

 import { Card, CardContent } from "@/components/ui/card" View Code
 About #
 The carousel component is built using the Embla Carousel library.
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add carousel Copy
 Usage #
 Copy import {
 Carousel,
 CarouselContent,
 CarouselItem,
 CarouselNext,
 CarouselPrevious,
 } from &quot;@/components/ui/carousel&quot;
 Copy &lt; Carousel &gt;
 &lt; CarouselContent &gt;
 &lt; CarouselItem &gt;...&lt;/ CarouselItem &gt;
 &lt; CarouselItem &gt;...&lt;/ CarouselItem &gt;
 &lt; CarouselItem &gt;...&lt;/ CarouselItem &gt;
 &lt;/ CarouselContent &gt;
 &lt; CarouselPrevious /&gt;
 &lt; CarouselNext /&gt;
 &lt;/ Carousel &gt;
 Composition #
 Use the following composition to build a Carousel :
 Copy Carousel
 ├── CarouselContent
 │ ├── CarouselItem
 │ └── CarouselItem
 ├── CarouselPrevious
 └── CarouselNext
 Examples #
 Sizes #
 To set the size of the items, you can use the basis utility class on the &lt;CarouselItem /&gt; .
 1 2 3 4 5 Previous slide Next slide Copy import * as React from "react"

 import { Card, CardContent } from "@/components/ui/card" View Code
 Copy // 33% of the carousel width.
 &lt; Carousel &gt;
 &lt; CarouselContent &gt;
 &lt; CarouselItem className = &quot;basis-1/3&quot; &gt;...&lt;/ CarouselItem &gt;
 &lt; CarouselItem className = &quot;basis-1/3&quot; &gt;...&lt;/ CarouselItem &gt;
 &lt; CarouselItem className = &quot;basis-1/3&quot; &gt;...&lt;/ CarouselItem &gt;
 &lt;/ CarouselContent &gt;
 &lt;/ Carousel &gt;
 Copy // 50% on small screens and 33% on larger screens.
 &lt; Carousel &gt;
 &lt; CarouselContent &gt;
 &lt; CarouselItem className = &quot;md:basis-1/2 lg:basis-1/3&quot; &gt;...&lt;/ CarouselItem &gt;
 &lt; CarouselItem className = &quot;md:basis-1/2 lg:basis-1/3&quot; &gt;...&lt;/ CarouselItem &gt;
 &lt; CarouselItem className = &quot;md:basis-1/2 lg:basis-1/3&quot; &gt;...&lt;/ CarouselItem &gt;
 &lt;/ CarouselContent &gt;
 &lt;/ Carousel &gt;
 Spacing #
 To set the spacing between the items, we use a pl-[VALUE] utility on the &lt;CarouselItem /&gt; and a negative -ml-[VALUE] on the &lt;CarouselContent /&gt; .
 1 2 3 4 5 Previous slide Next slide Copy import * as React from "react"

 import { Card, CardContent } from "@/components/ui/card" View Code
 Copy &lt; Carousel &gt;
 &lt; CarouselContent className = &quot; -ml-4 &quot; &gt;
 &lt; CarouselItem className = &quot; pl-4 &quot; &gt;...&lt;/ CarouselItem &gt;
 &lt; CarouselItem className = &quot; pl-4 &quot; &gt;...&lt;/ CarouselItem &gt;
 &lt; CarouselItem className = &quot; pl-4 &quot; &gt;...&lt;/ CarouselItem &gt;
 &lt;/ CarouselContent &gt;
 &lt;/ Carousel &gt;
 Copy &lt; Carousel &gt;
 &lt; CarouselContent className = &quot; -ml-2 md:-ml-4 &quot; &gt;
 &lt; CarouselItem className = &quot; pl-2 md:pl-4 &quot; &gt;...&lt;/ CarouselItem &gt;
 &lt; CarouselItem className = &quot; pl-2 md:pl-4 &quot; &gt;...&lt;/ CarouselItem &gt;
 &lt; CarouselItem className = &quot; pl-2 md:pl-4 &quot; &gt;...&lt;/ CarouselItem &gt;
 &lt;/ CarouselContent &gt;
 &lt;/ Carousel &gt;
 Orientation #
 Use the orientation prop to set the orientation of the carousel.
 1 2 3 4 5 Previous slide Next slide Copy import * as React from "react"

 import { Card, CardContent } from "@/components/ui/card" View Code
 Copy &lt; Carousel orientation = &quot; vertical | horizontal &quot; &gt;
 &lt; CarouselContent &gt;
 &lt; CarouselItem &gt;...&lt;/ CarouselItem &gt;
 &lt; CarouselItem &gt;...&lt;/ CarouselItem &gt;
 &lt; CarouselItem &gt;...&lt;/ CarouselItem &gt;
 &lt;/ CarouselContent &gt;
 &lt;/ Carousel &gt;
 Options #
 You can pass options to the carousel using the opts prop. See the Embla Carousel docs for more information.
 Copy &lt; Carousel
 opts = { {
 align: &quot;start&quot; ,
 loop: true ,
 } }
 &gt;
 &lt; CarouselContent &gt;
 &lt; CarouselItem &gt;...&lt;/ CarouselItem &gt;
 &lt; CarouselItem &gt;...&lt;/ CarouselItem &gt;
 &lt; CarouselItem &gt;...&lt;/ CarouselItem &gt;
 &lt;/ CarouselContent &gt;
 &lt;/ Carousel &gt;
 API #
 Use a state and the setApi props to get an instance of the carousel API.
 1 2 3 4 5 Previous slide Next slide Slide 0 of 0 Copy "use client"

 import * as React from "react" View Code
 Copy import { type CarouselApi } from &quot;@/components/ui/carousel&quot;

 export function Example () {
 const [ api , setApi ] = React. useState &lt; CarouselApi &gt;()
 const [ current , setCurrent ] = React. useState ( 0 )
 const [ count , setCount ] = React. useState ( 0 )

 React. useEffect (() =&gt; {
 if ( ! api) {
 return
 }

 setCount (api. scrollSnapList (). length )
 setCurrent (api. selectedScrollSnap () + 1 )

 api. on ( &quot;select&quot; , () =&gt; {
 setCurrent (api. selectedScrollSnap () + 1 )
 })
 }, [api])

 return (
 &lt; Carousel setApi = { setApi } &gt;
 &lt; CarouselContent &gt;
 &lt; CarouselItem &gt;...&lt;/ CarouselItem &gt;
 &lt; CarouselItem &gt;...&lt;/ CarouselItem &gt;
 &lt; CarouselItem &gt;...&lt;/ CarouselItem &gt;
 &lt;/ CarouselContent &gt;
 &lt;/ Carousel &gt;
 )
 }
 Events #
 You can listen to events using the api instance from setApi .
 Copy import { type CarouselApi } from &quot;@/components/ui/carousel&quot;

 export function Example () {
 const [ api , setApi ] = React. useState &lt; CarouselApi &gt;()

 React. useEffect (() =&gt; {
 if ( ! api) {
 return
 }

 api. on ( &quot;select&quot; , () =&gt; {
 // Do something on select.
 })
 }, [api])

 return (
 &lt; Carousel setApi = { setApi } &gt;
 &lt; CarouselContent &gt;
 &lt; CarouselItem &gt;...&lt;/ CarouselItem &gt;
 &lt; CarouselItem &gt;...&lt;/ CarouselItem &gt;
 &lt; CarouselItem &gt;...&lt;/ CarouselItem &gt;
 &lt;/ CarouselContent &gt;
 &lt;/ Carousel &gt;
 )
 }
 See the Embla Carousel docs for more information on using events.
 Plugins #
 You can use the plugins prop to add plugins to the carousel.
 Copy import Autoplay from &quot;embla-carousel-autoplay&quot;

 export function Example () {
 return (
 &lt; Carousel
 plugins = {[
 Autoplay ({
 delay: 2000 ,
 }),
 ]}
 &gt;
 // ...
 &lt;/Carousel&gt;
 )
 }
 1 2 3 4 5 Previous slide Next slide Copy "use client"

 import * as React from "react" View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle ١ ٢ ٣ ٤ ٥ Previous slide Next slide Copy "use client"

 import { View Code
 When localizing the carousel for RTL languages, you need to set the direction option in the opts prop to match the text direction. This ensures the carousel scrolls in the correct direction.
 Copy &lt; Carousel
 dir = { dir }
 opts = { {
 direction: dir,
 } }
 &gt;
 &lt; CarouselContent &gt;
 &lt; CarouselItem &gt;...&lt;/ CarouselItem &gt;
 &lt; CarouselItem &gt;...&lt;/ CarouselItem &gt;
 &lt; CarouselItem &gt;...&lt;/ CarouselItem &gt;
 &lt;/ CarouselContent &gt;
 &lt; CarouselPrevious className = &quot;rtl:rotate-180&quot; /&gt;
 &lt; CarouselNext className = &quot;rtl:rotate-180&quot; /&gt;
 &lt;/ Carousel &gt;
 The direction option accepts &quot;ltr&quot; or &quot;rtl&quot; and should match the dir prop value. You may also want to rotate the navigation buttons using the rtl:rotate-180 class to ensure they point in the correct direction.
 API Reference #
 See the Embla Carousel docs for more information on props and plugins. Card Chart On This Page About Installation Usage Composition Examples Sizes Spacing Orientation Options API Events Plugins RTL API Reference Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
