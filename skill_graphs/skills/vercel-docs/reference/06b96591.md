# Using the Directory Listing
Last updated November 25, 2025
The Directory Listing setting enables you to display the contents of a directory when a user visits its path. For example, if you create a directory at the root of your project called `/assets`, then when people visit `https://your-site.com/assets`, they will see the files and folders within that directory, as shown in the example below:
![The contents of a /assets directory.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fprojects%2Fdirectory-listing-page-light.png&w=1920&q=75)![The contents of a /assets directory.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fprojects%2Fdirectory-listing-dark2.png&w=1920&q=75)The contents of a /assets directory.
You can enable or disable Directory Listing from Advanced in your project sidebar settings.
![Directory Listing for an example /assets directory.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fprojects%2Fdirectory-listing-light.png&w=3840&q=75)![Directory Listing for an example /assets directory.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fprojects%2Fdirectory-listing-dark.png&w=3840&q=75)Directory Listing for an example /assets directory.
When enabled, the Directory Listing will be displayed. When disabled, a "Not Found" error will be displayed with status code `404`.
If Directory Listing isn't working, navigate to your deployment in the dashboard and open **Source** in the sidebar to view the contents of your project. Ensure the expected directory and files are listed.
###  [Disabling Directory Listing on a specific directory](https://vercel.com/docs/directory-listing#disabling-directory-listing-on-a-specific-directory)[](https://vercel.com/docs/directory-listing#disabling-directory-listing-on-a-specific-directory)
To prevent Directory Listing for a specific path, you can either:
  * Add an index file with any extension except `.css`, such as `index.html`. This file will be displayed instead of the Directory Listing
  * Or, [set up a custom 404 error](https://vercel.com/kb/guide/custom-404-page)


* * *
Was this helpful?
Send
On this page
  * [Disabling Directory Listing on a specific directory](https://vercel.com/docs/directory-listing#disabling-directory-listing-on-a-specific-directory)


Copy as MarkdownGive feedbackAsk AI about this page
