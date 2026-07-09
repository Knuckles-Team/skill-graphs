# How to build micro-frontends using multi-zones and Next.js
Last updated February 27, 2026
Examples
Multi-Zones are an approach to micro-frontends that separate a large application on a domain into smaller Next.js applications that each serve a set of paths. This is useful when there are collections of pages unrelated to the other pages in the application. By moving those pages to a separate zone (i.e., a separate application), you can reduce the size of each application which improves build times and removes code that is only necessary for one of the zones. Since applications are decoupled, Multi-Zones also allows other applications on the domain to use their own choice of framework.
For example, let's say you have the following set of pages that you would like to split up:
  * `/blog/*` for all blog posts
  * `/dashboard/*` for all pages when the user is logged-in to the dashboard
  * `/*` for the rest of your website not covered by other zones


With Multi-Zones support, you can create three applications that all are served on the same domain and look the same to the user, but you can develop and deploy each of the applications independently.
![Three zones: A, B, C. Showing a hard navigation between routes from different zones, and soft navigations between routes within the same zone.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fmulti-zones.png&w=3840&q=75)![Three zones: A, B, C. Showing a hard navigation between routes from different zones, and soft navigations between routes within the same zone.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fmulti-zones.png&w=3840&q=75)
Navigating between pages in the same zone will perform soft navigations, a navigation that does not require reloading the page. For example, in this diagram, navigating from `/` to `/products` will be a soft navigation.
Navigating from a page in one zone to a page in another zone, such as from `/` to `/dashboard`, will perform a hard navigation, unloading the resources of the current page and loading the resources of the new page. Pages that are frequently visited together should live in the same zone to avoid hard navigations.
