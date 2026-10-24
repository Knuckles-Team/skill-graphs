##  [Getting the access token](https://vercel.com/docs#getting-the-access-token)[](https://vercel.com/docs#getting-the-access-token)
You receive an access token when a user installs your integration. Vercel calls your [Upsert Installation](https://vercel.com/partner/upsert-installation) endpoint with the token in the `credentials` field.
**Store this token securely.** You'll use it to authenticate all requests to the Vercel API for that installation.
**Example:** Using the access token
`Authorization: Bearer YOUR_ACCESS_TOKEN`
