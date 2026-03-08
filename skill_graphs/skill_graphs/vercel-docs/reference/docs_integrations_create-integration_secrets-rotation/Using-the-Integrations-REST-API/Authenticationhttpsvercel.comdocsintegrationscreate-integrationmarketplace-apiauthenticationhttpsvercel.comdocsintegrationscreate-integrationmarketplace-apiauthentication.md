##  [Authentication](https://vercel.com/docs/integrations/create-integration/marketplace-api#authentication)[](https://vercel.com/docs/integrations/create-integration/marketplace-api#authentication)
The authentication method depends on whether Vercel is calling the integration provider's API or the provider is calling Vercel's API.
###  [Provider API authentication](https://vercel.com/docs/integrations/create-integration/marketplace-api#provider-api-authentication)[](https://vercel.com/docs/integrations/create-integration/marketplace-api#provider-api-authentication)
There are two authentication methods available:
  * User authentication: The user initiates the action. You receive a JWT token that identifies the user making the request.
  * System authentication: Your integration performs the action automatically. You use account-level OpenID Connect (OIDC) credentials to authenticate.


System authentication uses OIDC tokens that represent your integration account, not a specific user. This lets you make API calls to Vercel without requiring user interaction.
####  [When to use system authentication](https://vercel.com/docs/integrations/create-integration/marketplace-api#when-to-use-system-authentication)[](https://vercel.com/docs/integrations/create-integration/marketplace-api#when-to-use-system-authentication)
  * Automatic balance top-ups for prepayment plans
  * Background synchronization tasks
  * Automated resource management
  * Any operation that should run without user action
  * Installation cleanup operations when the Vercel account is deleted


####  [When to use user authentication](https://vercel.com/docs/integrations/create-integration/marketplace-api#when-to-use-user-authentication)[](https://vercel.com/docs/integrations/create-integration/marketplace-api#when-to-use-user-authentication)
  * User-initiated actions
  * Operations that require user consent
  * Actions tied to a specific user's context


####  [Security best practices](https://vercel.com/docs/integrations/create-integration/marketplace-api#security-best-practices)[](https://vercel.com/docs/integrations/create-integration/marketplace-api#security-best-practices)
  * Verify the OIDC token signature and claims: Always validate the token signature using Vercel's [OIDC configuration](https://marketplace.vercel.com/.well-known/openid-configuration). Check the `aud` claim matches your integration ID, and the `sub` claim identifies the authenticated user or account.
  * For user authentication always validate the user's role.


Review the [user authentication](https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/partner#user-authentication) and [system authentication](https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/partner#system-authentication) specifications to help you implement each method.
###  [Vercel API authentication](https://vercel.com/docs/integrations/create-integration/marketplace-api#vercel-api-authentication)[](https://vercel.com/docs/integrations/create-integration/marketplace-api#vercel-api-authentication)
When your integration calls Vercel's API, you authenticate using an access token. You receive this token during the installation process when you call the [Upsert Installation API](https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/partner/upsert-installation). The response includes a `credentials` object with an `access_token` that you use as a bearer token for subsequent API calls.
You can also use OAuth2 to obtain access tokens for user-specific operations.
###  [Authentication with SSO](https://vercel.com/docs/integrations/create-integration/marketplace-api#authentication-with-sso)[](https://vercel.com/docs/integrations/create-integration/marketplace-api#authentication-with-sso)
####  [Vercel initiated SSO](https://vercel.com/docs/integrations/create-integration/marketplace-api#vercel-initiated-sso)[](https://vercel.com/docs/integrations/create-integration/marketplace-api#vercel-initiated-sso)
Vercel initiates SSO as part of the [Open in Provider flow](https://vercel.com/docs/integrations/marketplace-flows#open-in-provider-button-flow).
  1. Vercel sends the user to the provider [redirectLoginUrl](https://vercel.com/docs/integrations/create-integration/submit-integration#redirect-login-url), with the OAuth authorization `code` and other parameters
  2. The provider calls the [SSO Token Exchange](https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/vercel/exchange-sso-token), which validates the SSO request and returns OIDC and access tokens
  3. The user gains authenticated access to the requested resource.


Parameters:
The SSO request to the [redirectLoginUrl](https://vercel.com/docs/integrations/create-integration/submit-integration#redirect-login-url) will include the following authentication parameters:
  * `mode`. The mode of the OAuth authorization is always set to `sso`.
  * `code`: The OAuth authorization code.
  * `state`: The state parameter that was passed in the OAuth authorization request.


The `code` and `state` parameters will be passed back to Vercel in the [SSO Token Exchange](https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/vercel/exchange-sso-token) request.
Additionally, the SSO request to the [redirectLoginUrl](https://vercel.com/docs/integrations/create-integration/submit-integration#redirect-login-url) may include the following optional context parameters:
  * `product_id`: The ID of the provider's product
  * `resource_id`: The ID of the provider's resource
  * `check_id`: The ID of the deployment check, when the resource is associated with a deployment check. Example: "chk_abc123".
  * `project_id`: The ID of the Vercel project, for instance, when the resource is connected to the Vercel project. Example: "prj_ff7777b9".
  * `experimentation_item_id`: See [Experimentation flow](https://vercel.com/docs/integrations/create-integration/marketplace-flows#experimentation-flow).
  * `invoice_id`: The ID of the provider's invoice
  * `pr`: The URL of the pull request in the Vercel project, when known in the context. Example: `https://github.com/owner1/repo1/pull/123`.
  * `path`: Indicates the area where the user should be redirected to after SSO. The possible values are: "billing", "usage", "onboarding", "secrets", and "support".
  * `url`: The provider-specific URL to redirect the user to after SSO. Must be validated by the provider for validity. The data fields that are allowed to provide `sso:` URLs, such as `Notification.href`, will automatically propagate the provided URL in this parameter.


The provider should match the most appropriate part of their dashboard to the user's context.
Using SSO with API responses:
You can trigger SSO by using `sso:` URLs in your API responses. When users click these links, Vercel initiates the SSO flow before redirecting them to your platform. The `sso:` prefix works in any URL field that supports it, such as [installation notification](https://vercel.com/docs/integrations/create-integration/marketplace-api#sso-enabled-notification-links) links or resource URLs.
Format:
`sso:https://your-integration.com/resource-page `
When a user clicks a link with an `sso:` URL:
  1. Vercel initiates the SSO flow
  2. Your provider validates the SSO request via the [SSO Token Exchange](https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/vercel/exchange-sso-token)
  3. The user is redirected to the target URL with authenticated access


Example with notifications:
upsert-installation-with-sso.ts
```
// When creating or updating an installation, include an sso: URL
const response = await fetch(
  `https://api.vercel.com/v1/installations/${installationId}`,
  {
    method: 'PATCH',
    headers: {
      Authorization: `Bearer ${vercelToken}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      notification: {
        title: 'Review your usage',
        message: 'Your monthly usage report is ready',
        href: 'sso:https://your-integration.com/dashboard/usage',
        type: 'info',
      },
    }),
  },
);
```

####  [Provider initiated SSO](https://vercel.com/docs/integrations/create-integration/marketplace-api#provider-initiated-sso)[](https://vercel.com/docs/integrations/create-integration/marketplace-api#provider-initiated-sso)
The integration provider can initiate the SSO process from their side. This helps to streamline the authentication process for users coming from the provider's platform and provides security when a user attempts to access a resource managed by a Vercel Marketplace integration.
To initiate SSO, an integration provider needs to construct a URL using the following format:
`https://vercel.com/sso/integrations/{URLSlug}/{installationId}?{query} `
  * [`URLSlug`](https://vercel.com/docs/integrations/create-integration/submit-integration#url-slug): The unique identifier for your integration in the Vercel Integrations Marketplace
  * [`installationId`](https://vercel.com/docs/integrations/marketplace-api#installations): The ID of the specific installation for the user
  * `query`: Optional query parameters to include additional information


Example:
Let's say you have an AWS integration with the following details:
  * `URLSlug`: `aws-marketplace-integration-demo`
  * `installationId`: `icfg_PSFtkFqr5djKRtOkNtOHIfSd`
  * Additional parameter: `resource_id=123456`


The constructed URL would look like this:
`https://vercel.com/sso/integrations/aws-marketplace-integration-demo/icfg_PSFtkFqr5djKRtOkNtOHIfSd?resource_id=123456 `
Flow:
  1. The provider constructs and redirects the user to the SSO URL
  2. Vercel validates the SSO request and confirms user access
  3. After successfully validating the request, Vercel redirects the user back to the provider using the same flow described in the [Vercel Initiated SSO](https://vercel.com/docs/integrations/create-integration/marketplace-api#vercel-initiated-sso)
  4. The user gains authenticated access to the requested resource
