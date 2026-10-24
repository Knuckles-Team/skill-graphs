##  [Redirect URL](https://vercel.com/docs/integrations/create-integration/submit-integration#redirect-url)[](https://vercel.com/docs/integrations/create-integration/submit-integration#redirect-url)
  * Required: Yes


The Redirect URL is an HTTP endpoint that handles the installation process by exchanging a code for an API token, serving a user interface, and managing project connections:
  * Token Exchange: Exchanges a provided code for a [Vercel REST API access token](https://vercel.com/docs/rest-api/vercel-api-integrations#exchange-code-for-access-token)
  * User Interface: Displays a responsive UI in a popup window during the installation
  * Project Provisioning: Allows users to create new projects or connect existing ones in your system to their Vercel Projects
  * Completion: Redirects the user back to Vercel upon successful installation


Important considerations:
  * If your application uses the `Cross-Origin-Opener-Policy` header, use the value `unsafe-none` to allow the Vercel dashboard to monitor the popup's closed state. dashboard to monitor the popup's closed state.
  * For local development and testing, you can specify a URL on `localhost`.
