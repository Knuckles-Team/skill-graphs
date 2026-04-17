##  [Setting a default route](https://vercel.com/docs/deployments#setting-a-default-route)[](https://vercel.com/docs/deployments#setting-a-default-route)
Some functionality in the Vercel Dashboard, such as screenshots and links to the deployment domain, automatically links to the `/` path. Microfrontends deployments may not serve any content on the `/` path so that functionality may appear broken. You can set a default route in the dashboard so that the Vercel Dashboard instead always links to a valid route in the microfrontends deployment.
To update the default route, visit the Microfrontends Settings page.
  1. Open Settings in the sidebar for your project and select [Microfrontends](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fmicrofrontends&title=Go+to+Microfrontends+settings)
  2. Search for the Default Route setting
  3. Enter a new default path (starting with `/`) such as `/docs` and click Save

![Setting to specify the default route for the project.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fmicrofrontends%2Fdefault-route-settings-light.png&w=1920&q=75)![Setting to specify the default route for the project.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fmicrofrontends%2Fdefault-route-settings-dark.png&w=1920&q=75)Setting to specify the default route for the project.
Deployments created after this change will now use the provided path as the default route.
