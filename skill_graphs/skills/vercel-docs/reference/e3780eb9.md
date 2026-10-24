##  [OIDC token anatomy](https://vercel.com/docs/audit-log#oidc-token-anatomy)[](https://vercel.com/docs/audit-log#oidc-token-anatomy)
You can validate OpenID Connect tokens by using the issuer's OpenID Connect Discovery Well Known location, which is either `https://oidc.vercel.com/.well-known/openid-configuration` or `https://oidc.vercel.com/[TEAM_SLUG]/.well-known/openid-configuration` depending on the issuer mode in your project settings. There, you can find a property called `jwks_uri` which provides a URI to Vercel's public JSON Web Keys (JWKs). You can use the corresponding JWK identified by `kid` to verify tokens that are signed with the same `kid` in the token's header.
###  [Example token](https://vercel.com/docs/audit-log#example-token)[](https://vercel.com/docs/audit-log#example-token)
```
// Header:
{
  "typ": "JWT",
  "alg": "RS256",
  "kid": "example-key-id"
}
// Claims:
{
  "iss": "https://oidc.vercel.com/acme",
  "aud": "https://vercel.com/acme",
  "sub": "owner:acme:project:acme_website:environment:production",
  "iat": 1718885593,
  "nfb": 1718885593,
  "exp": 1718889193,
  "owner": "acme",
  "owner_id": "team_7Gw5ZMzpQA8h90F832KGp7nwbuh3",
  "project": "acme_website",
  "project_id": "prj_7Gw5ZMBpQA8h9GF832KGp7nwbuh3",
  "environment": "production"
}
```

###  [Standard OpenID Connect claims](https://vercel.com/docs/audit-log#standard-openid-connect-claims)[](https://vercel.com/docs/audit-log#standard-openid-connect-claims)
This is a list of standard tokens that you can expect from an OpenID Connect JWT:
Claim | Kind | Description
---|---|---
`iss` | Issuer | When using the team issuer mode, the issuer is set to `https://oidc.vercel.com/[TEAM_SLUG]`
When using the global issuer mode, the issuer is set to `https://oidc.vercel.com`
`aud` | Audience | The audience is set to `https://vercel.com/[TEAM_SLUG]`
`sub` | Subject | The subject is set to `owner:[TEAM_SLUG]:project:[PROJECT_NAME]:environment:[ENVIRONMENT]`
`iat` | Issued at | The time the token was created
`nbf` | Not before | The token is not valid before this time
`exp` | Expires at | The time the token has or will expire. `preview` and `production` tokens expire one hour after creation, `development` tokens expire in 12 hours.
###  [Additional claims](https://vercel.com/docs/audit-log#additional-claims)[](https://vercel.com/docs/audit-log#additional-claims)
These claims provide more granular access control:
Claim | Description
---|---
`owner` | The team slug, e.g. `acme`
`owner_id` | The team ID, e.g. `team_7Gw5ZMzpQA8h90F832KGp7nwbuh3`
`project` | The project name, e.g. `acme_website`
`project_id` | The project ID, e.g. `prj_7Gw5ZMBpQA8h9GF832KGp7nwbuh3`
`environment` | The environment: `development` or `preview` or `production`
`user_id` | When environment is `development`, this is the ID of the user who was issued the token
###  [JWT headers](https://vercel.com/docs/audit-log#jwt-headers)[](https://vercel.com/docs/audit-log#jwt-headers)
These headers are standard to the JWT tokens:
Header | Kind | Description
---|---|---
`alg` | Algorithm | The algorithm used by the issuer
`kid` | Key ID | The identifier of the key used to sign the token
`typ` | Type | The type of token, this is set to `jwt`.
* * *
[ Previous Overview ](https://vercel.com/docs/security)[ Next Firewall ](https://vercel.com/docs/vercel-firewall)
Was this helpful?
Send
On this page
  * [Helper libraries](https://vercel.com/docs/audit-log#helper-libraries)
  * [AWS SDK credentials provider](https://vercel.com/docs/audit-log#aws-sdk-credentials-provider)
  * [AWS S3 usage example](https://vercel.com/docs/audit-log#aws-s3-usage-example)
  * [Other cloud providers](https://vercel.com/docs/audit-log#other-cloud-providers)
  * [Azure / CosmosDB example](https://vercel.com/docs/audit-log#azure-/-cosmosdb-example)
  * [Team and project name changes](https://vercel.com/docs/audit-log#team-and-project-name-changes)
  * [OIDC token anatomy](https://vercel.com/docs/audit-log#oidc-token-anatomy)
  * [Example token](https://vercel.com/docs/audit-log#example-token)
  * [Standard OpenID Connect claims](https://vercel.com/docs/audit-log#standard-openid-connect-claims)
  * [Additional claims](https://vercel.com/docs/audit-log#additional-claims)
  * [JWT headers](https://vercel.com/docs/audit-log#jwt-headers)


Copy as MarkdownGive feedbackAsk AI about this page
