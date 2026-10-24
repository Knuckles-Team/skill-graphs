##  [Configuration URL](https://vercel.com/docs/integrations/create-integration/submit-integration#configuration-url)[](https://vercel.com/docs/integrations/create-integration/submit-integration#configuration-url)
  * Required: No


To allow the developer to configure an installed integration, you can specify a Configuration URL. This URL is used for the Configure button on each configuration page. Selecting this button will redirect the developer to your specified URL with a `configurationId` query parameter. See [Interacting with Configurations](https://vercel.com/docs/rest-api/vercel-api-integrations#interacting-with-configurations) to learn more.
If you leave the Configuration URL field empty, the Configure button will default to a Website button that links to the website URL you specified on integration settings.
