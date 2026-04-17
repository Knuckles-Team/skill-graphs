## Examples[](https://nextjs.org/docs/app/getting-started/project-structure#examples)
The following section lists a very high-level overview of common strategies. The simplest takeaway is to choose a strategy that works for you and your team and be consistent across the project.
> **Good to know** : In our examples below, we're using `components` and `lib` folders as generalized placeholders, their naming has no special framework significance and your projects might use other folders like `ui`, `utils`, `hooks`, `styles`, etc.
### Store project files outside of `app`[](https://nextjs.org/docs/app/getting-started/project-structure#store-project-files-outside-of-app)
This strategy stores all application code in shared folders in the **root of your project** and keeps the `app` directory purely for routing purposes.
![An example folder structure with project files outside of app](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-project-root.png&w=3840&q=75)![An example folder structure with project files outside of app](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-project-root.png&w=3840&q=75)
### Store project files in top-level folders inside of `app`[](https://nextjs.org/docs/app/getting-started/project-structure#store-project-files-in-top-level-folders-inside-of-app)
This strategy stores all application code in shared folders in the **root of the`app` directory**.
![An example folder structure with project files inside app](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-app-root.png&w=3840&q=75)![An example folder structure with project files inside app](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-app-root.png&w=3840&q=75)
### Split project files by feature or route[](https://nextjs.org/docs/app/getting-started/project-structure#split-project-files-by-feature-or-route)
This strategy stores globally shared application code in the root `app` directory and **splits** more specific application code into the route segments that use them.
![An example folder structure with project files split by feature or route](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-app-root-split.png&w=3840&q=75)![An example folder structure with project files split by feature or route](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-app-root-split.png&w=3840&q=75)
### Organize routes without affecting the URL path[](https://nextjs.org/docs/app/getting-started/project-structure#organize-routes-without-affecting-the-url-path)
To organize routes without affecting the URL, create a group to keep related routes together. The folders in parenthesis will be omitted from the URL (e.g. `(marketing)` or `(shop)`).
![Organizing Routes with Route Groups](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Froute-group-organisation.png&w=3840&q=75)![Organizing Routes with Route Groups](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Froute-group-organisation.png&w=3840&q=75)
Even though routes inside `(marketing)` and `(shop)` share the same URL hierarchy, you can create a different layout for each group by adding a `layout.js` file inside their folders.
![Route Groups with Multiple Layouts](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Froute-group-multiple-layouts.png&w=3840&q=75)![Route Groups with Multiple Layouts](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Froute-group-multiple-layouts.png&w=3840&q=75)
### Opting specific segments into a layout[](https://nextjs.org/docs/app/getting-started/project-structure#opting-specific-segments-into-a-layout)
To opt specific routes into a layout, create a new route group (e.g. `(shop)`) and move the routes that share the same layout into the group (e.g. `account` and `cart`). The routes outside of the group will not share the layout (e.g. `checkout`).
![Route Groups with Opt-in Layouts](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Froute-group-opt-in-layouts.png&w=3840&q=75)![Route Groups with Opt-in Layouts](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Froute-group-opt-in-layouts.png&w=3840&q=75)
### Opting for loading skeletons on a specific route[](https://nextjs.org/docs/app/getting-started/project-structure#opting-for-loading-skeletons-on-a-specific-route)
To apply a [loading skeleton](https://nextjs.org/docs/app/api-reference/file-conventions/loading) via a `loading.js` file to a specific route, create a new route group (e.g., `/(overview)`) and then move your `loading.tsx` inside that route group.
![Folder structure showing a loading.tsx and a page.tsx inside the route group](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Froute-group-loading.png&w=3840&q=75)![Folder structure showing a loading.tsx and a page.tsx inside the route group](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Froute-group-loading.png&w=3840&q=75)
Now, the `loading.tsx` file will only apply to your dashboard → overview page instead of all your dashboard pages without affecting the URL path structure.
### Creating multiple root layouts[](https://nextjs.org/docs/app/getting-started/project-structure#creating-multiple-root-layouts)
To create multiple [root layouts](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout), remove the top-level `layout.js` file, and add a `layout.js` file inside each route group. This is useful for partitioning an application into sections that have a completely different UI or experience. The `<html>` and `<body>` tags need to be added to each root layout.
![Route Groups with Multiple Root Layouts](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Froute-group-multiple-root-layouts.png&w=3840&q=75)![Route Groups with Multiple Root Layouts](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Froute-group-multiple-root-layouts.png&w=3840&q=75)
In the example above, both `(marketing)` and `(shop)` have their own root layout.
[PreviousInstallation](https://nextjs.org/docs/app/getting-started/installation)[NextLayouts and Pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages)
Was this helpful?
Send
* * *
* * *
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Next.js Conf](https://nextjs.org/conf)[Evals](https://nextjs.org/evals)
#### More
[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)
#### About Vercel
#### Legal
Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
* * *
* * *
