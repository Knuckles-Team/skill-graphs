##  [Base URL](https://vercel.com/docs/integrations/create-integration/submit-integration#base-url)[](https://vercel.com/docs/integrations/create-integration/submit-integration#base-url)
  * Required: If it's a product


The URL that points to the provider's integration server that implements the [Marketplace Provider API](https://vercel.com/docs/integrations/marketplace-api). To interact with the provider's application, Vercel makes a request to the base URL appended with the path for the specific endpoint.
For example, if the base url is `https://foo.bar.com/vercel-integration-server`, Vercel makes a `POST` request to something like `https://foo.bar.com/vercel-integration-server/v1/installations`.
