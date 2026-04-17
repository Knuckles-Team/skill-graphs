## Organizing your project[](https://nextjs.org/docs/app/getting-started/project-structure#organizing-your-project)
Next.js is **unopinionated** about how you organize and colocate your project files. But it does provide several features to help you organize your project.
### Component hierarchy[](https://nextjs.org/docs/app/getting-started/project-structure#component-hierarchy)
The components defined in special files are rendered in a specific hierarchy:
  * `layout.js`
  * `template.js`
  * `error.js` (React error boundary)
  * `loading.js` (React suspense boundary)
  * `not-found.js` (React error boundary for "not found" UI)
  * `page.js` or nested `layout.js`

![Component Hierarchy for File Conventions](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Ffile-conventions-component-hierarchy.png&w=3840&q=75)![Component Hierarchy for File Conventions](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Ffile-conventions-component-hierarchy.png&w=3840&q=75)
The components are rendered recursively in nested routes, meaning the components of a route segment will be nested **inside** the components of its parent segment.
![Nested File Conventions Component Hierarchy](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fnested-file-conventions-component-hierarchy.png&w=3840&q=75)![Nested File Conventions Component Hierarchy](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fnested-file-conventions-component-hierarchy.png&w=3840&q=75)
### Colocation[](https://nextjs.org/docs/app/getting-started/project-structure#colocation)
In the `app` directory, nested folders define route structure. Each folder represents a route segment that is mapped to a corresponding segment in a URL path.
However, even though route structure is defined through folders, a route is **not publicly accessible** until a `page.js` or `route.js` file is added to a route segment.
![A diagram showing how a route is not publicly accessible until a page.js or route.js file is added to a route segment.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-not-routable.png&w=3840&q=75)![A diagram showing how a route is not publicly accessible until a page.js or route.js file is added to a route segment.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-not-routable.png&w=3840&q=75)
And, even when a route is made publicly accessible, only the **content returned** by `page.js` or `route.js` is sent to the client.
![A diagram showing how page.js and route.js files make routes publicly accessible.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-routable.png&w=3840&q=75)![A diagram showing how page.js and route.js files make routes publicly accessible.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-routable.png&w=3840&q=75)
This means that **project files** can be **safely colocated** inside route segments in the `app` directory without accidentally being routable.
![A diagram showing colocated project files are not routable even when a segment contains a page.js or route.js file.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-colocation.png&w=3840&q=75)![A diagram showing colocated project files are not routable even when a segment contains a page.js or route.js file.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-colocation.png&w=3840&q=75)
> **Good to know** : While you **can** colocate your project files in `app` you don't **have** to. If you prefer, you can [keep them outside the `app` directory](https://nextjs.org/docs/app/getting-started/project-structure#store-project-files-outside-of-app).
### Private folders[](https://nextjs.org/docs/app/getting-started/project-structure#private-folders)
Private folders can be created by prefixing a folder with an underscore: `_folderName`
This indicates the folder is a private implementation detail and should not be considered by the routing system, thereby **opting the folder and all its subfolders** out of routing.
![An example folder structure using private folders](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-private-folders.png&w=3840&q=75)![An example folder structure using private folders](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-private-folders.png&w=3840&q=75)
Since files in the `app` directory can be [safely colocated by default](https://nextjs.org/docs/app/getting-started/project-structure#colocation), private folders are not required for colocation. However, they can be useful for:
  * Separating UI logic from routing logic.
  * Consistently organizing internal files across a project and the Next.js ecosystem.
  * Sorting and grouping files in code editors.
  * Avoiding potential naming conflicts with future Next.js file conventions.


> **Good to know** :
>   * While not a framework convention, you might also consider marking files outside private folders as "private" using the same underscore pattern.
>   * You can create URL segments that start with an underscore by prefixing the folder name with `%5F` (the URL-encoded form of an underscore): `%5FfolderName`.
>   * If you don't use private folders, it would be helpful to know Next.js [special file conventions](https://nextjs.org/docs/app/getting-started/project-structure#routing-files) to prevent unexpected naming conflicts.
>

### Route groups[](https://nextjs.org/docs/app/getting-started/project-structure#route-groups)
Route groups can be created by wrapping a folder in parenthesis: `(folderName)`
This indicates the folder is for organizational purposes and should **not be included** in the route's URL path.
![An example folder structure using route groups](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-route-groups.png&w=3840&q=75)![An example folder structure using route groups](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-route-groups.png&w=3840&q=75)
Route groups are useful for:
  * Organizing routes by site section, intent, or team. e.g. marketing pages, admin pages, etc.
  * Enabling nested layouts in the same route segment level:
    * [Creating multiple nested layouts in the same segment, including multiple root layouts](https://nextjs.org/docs/app/getting-started/project-structure#creating-multiple-root-layouts)
    * [Adding a layout to a subset of routes in a common segment](https://nextjs.org/docs/app/getting-started/project-structure#opting-specific-segments-into-a-layout)


###  `src` folder[](https://nextjs.org/docs/app/getting-started/project-structure#src-folder)
Next.js supports storing application code (including `app`) inside an optional [`src` folder](https://nextjs.org/docs/app/api-reference/file-conventions/src-folder). This separates application code from project configuration files which mostly live in the root of a project.
![An example folder structure with the `src` folder](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-src-directory.png&w=3840&q=75)![An example folder structure with the `src` folder](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-src-directory.png&w=3840&q=75)
