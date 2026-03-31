[Skip to main content](https://docs.postiz.com/public-api/oauth#content-area)
[Postiz Documentation home page![light logo](https://mintcdn.com/postiz/SZ3zBABjhg7UQcI8/logo/light.png?fit=max&auto=format&n=SZ3zBABjhg7UQcI8&q=85&s=ab950a1a5aa687eb0de8156022f7c7c9)![dark logo](https://mintcdn.com/postiz/SZ3zBABjhg7UQcI8/logo/dark.png?fit=max&auto=format&n=SZ3zBABjhg7UQcI8&q=85&s=4134d88b8fc8339a26775f8e48e95f7e)](https://docs.postiz.com/)
Search...
Ctrl K
  * [Discord](https://discord.postiz.com)


##### OAuth2
  * [OAuth2 Authentication](https://docs.postiz.com/public-api/oauth)


  * [Discord](https://discord.postiz.com)
  * [Register to the cloud](https://postiz.com)


[Postiz Documentation home page![light logo](https://mintcdn.com/postiz/SZ3zBABjhg7UQcI8/logo/light.png?fit=max&auto=format&n=SZ3zBABjhg7UQcI8&q=85&s=ab950a1a5aa687eb0de8156022f7c7c9)![dark logo](https://mintcdn.com/postiz/SZ3zBABjhg7UQcI8/logo/dark.png?fit=max&auto=format&n=SZ3zBABjhg7UQcI8&q=85&s=4134d88b8fc8339a26775f8e48e95f7e)](https://docs.postiz.com/)
Search...
Ctrl K
  * [](https://discord.postiz.com)
  * [Register to the cloud](https://postiz.com)
  * [Register to the cloud](https://postiz.com)


Search...
Navigation
OAuth2
OAuth2 Authentication
[Documentation](https://docs.postiz.com/introduction)[Public API](https://docs.postiz.com/public-api/introduction)[CLI](https://docs.postiz.com/cli/introduction)[MCP](https://docs.postiz.com/mcp/introduction)[Developer App (oAuth2)](https://docs.postiz.com/public-api/oauth)[Contributing](https://docs.postiz.com/developer-guide)
[Documentation](https://docs.postiz.com/introduction)[Public API](https://docs.postiz.com/public-api/introduction)[CLI](https://docs.postiz.com/cli/introduction)[MCP](https://docs.postiz.com/mcp/introduction)[Developer App (oAuth2)](https://docs.postiz.com/public-api/oauth)[Contributing](https://docs.postiz.com/developer-guide)
OAuth2
# OAuth2 Authentication
Copy page
Let users authorize your app to access Postiz on their behalf
Copy page
## 
[​](https://docs.postiz.com/public-api/oauth#overview)
Overview
Postiz supports OAuth2 Authorization Code flow, allowing you to build third-party applications that act on behalf of Postiz users. Instead of asking users for their API key, your app redirects them to Postiz where they approve access, and you receive a token to make API calls on their behalf.
OAuth tokens work with all the same Public API endpoints as API keys. The only difference is how the token is obtained.
## 
[​](https://docs.postiz.com/public-api/oauth#how-it-works)
How It Works
PostizYourAppUserPostizYourAppUserClicks "Connect with Postiz"Redirect to /oauth/authorizeShows consent screenApproves accessRedirects with ?code=...POST /oauth/token (exchange code)Returns access_tokenAPI calls with access_token
## 
[​](https://docs.postiz.com/public-api/oauth#implementation)
Implementation
1
[](https://docs.postiz.com/public-api/oauth)
Register Your OAuth App
Go to **Settings > Developers > Apps** in your Postiz dashboard and create an OAuth application.You will need to provide:
  * **App Name** - displayed to users on the consent screen
  * **Description** (optional) - explains what your app does
  * **Profile Picture** (optional) - shown on the consent screen
  * **Redirect URL** - where Postiz sends users after they approve/deny access

After creating the app, you will receive:
  * **Client ID** - a public identifier for your app (starts with `pca_`)
  * **Client Secret** - a secret key for token exchange (starts with `pcs_`)


The client secret is only shown once on creation. Copy it immediately and store it securely. If you lose it, you can rotate it from the settings page.
2
[](https://docs.postiz.com/public-api/oauth)
Redirect Users to Authorize
When a user wants to connect their Postiz account to your app, redirect them to:
```
https://{FRONTEND_URL}/oauth/authorize?client_id={CLIENT_ID}&response_type=code&state={STATE}

```

Parameter | Required | Description  
---|---|---  
`client_id` | Yes | Your app’s Client ID  
`response_type` | Yes | Must be `code`  
`state` | No | A random string to prevent CSRF attacks. Recommended.  
**Example:**
```
https://platform.postiz.com/oauth/authorize?client_id=pca_VklHTpdEJ6dJ73FHQEJ97qVA0lcMDsrs&response_type=code&state=random123

```

The user will see a consent screen showing your app’s name, description, and the permissions being requested. They can choose to **Authorize** or **Deny**.
3
[](https://docs.postiz.com/public-api/oauth)
Handle the Callback
After the user makes a decision, Postiz redirects them to your **Redirect URL** with query parameters.**If approved:**
```
https://yourapp.com/callback?code=abc123&state=random123

```

Parameter | Description  
---|---  
`code` | Authorization code to exchange for a token (expires in 10 minutes)  
`state` | The same state value you sent in the previous step  
**If denied:**
```
https://yourapp.com/callback?error=access_denied&state=random123

```

Always verify that the `state` parameter matches what you originally sent to prevent CSRF attacks.
4
[](https://docs.postiz.com/public-api/oauth)
Exchange Code for Token
Make a server-side `POST` request to exchange the authorization code for an access token:
```
curl -X POST https://{BACKEND_URL}/oauth/token \
  -H "Content-Type: application/json" \
  -d '{
    "grant_type": "authorization_code",
    "code": "abc123",
    "client_id": "pca_VklHTpdEJ6dJ73FHQEJ97qVA0lcMDsrs",
    "client_secret": "pcs_your_client_secret"
  }'

```

Parameter | Required | Description  
---|---|---  
`grant_type` | Yes | Must be `authorization_code`  
`code` | Yes | The authorization code from the previous step  
`client_id` | Yes | Your app’s Client ID  
`client_secret` | Yes | Your app’s Client Secret  
**Response:**
```
{
  "id": "org_abc123",
  "cus": "cus_stripe_customer_id",
  "access_token": "pos_aBcDeFgHiJkLmNoPqRsTuVwXyZ1234567890abcd",
  "token_type": "bearer"
}

```

Field | Description  
---|---  
`id` | The organization ID associated with the authorized user  
`cus` | The Stripe customer ID for the organization (useful for billing integrations)  
`access_token` | The token to use for subsequent API calls  
`token_type` | Always `bearer`  
The authorization code expires after **10 minutes** and can only be used once. If it expires, the user must go through the authorization flow again.
5
[](https://docs.postiz.com/public-api/oauth)
Make API Calls
Use the access token in the `Authorization` header, just like you would with an API key:
```
curl -H "Authorization: pos_aBcDeFgHiJkLmNoPqRsTuVwXyZ1234567890abcd" \
  https://{BACKEND_URL}/public/v1/integrations

```

The token works with all Public API endpoints:
  * [List Integrations](https://docs.postiz.com/public-api/integrations/list)
  * [Create Posts](https://docs.postiz.com/public-api/posts/create)
  * [View Analytics](https://docs.postiz.com/public-api/analytics/platform)
  * And all other endpoints documented in this API reference


OAuth tokens do not expire. Users can revoke access at any time from **Settings > Approved Apps** in their Postiz dashboard.
* * *
## 
[​](https://docs.postiz.com/public-api/oauth#managing-your-app)
Managing Your App
### 
[​](https://docs.postiz.com/public-api/oauth#rotate-client-secret)
Rotate Client Secret
If your client secret is compromised, go to **Settings > Developers > Apps** and click **Rotate Secret**. This invalidates the old secret immediately — any token exchange requests using the old secret will fail.
Rotating the secret does **not** invalidate existing access tokens. Only new token exchange requests require the new secret.
### 
[​](https://docs.postiz.com/public-api/oauth#delete-your-app)
Delete Your App
Deleting your OAuth app will:
  * Revoke **all** access tokens issued to users
  * Remove the app from all users’ Approved Apps list
  * This action cannot be undone


* * *
## 
[​](https://docs.postiz.com/public-api/oauth#full-example-node-js)
Full Example (Node.js)
```
const express = require('express');
const crypto = require('crypto');
const app = express();

const CLIENT_ID = 'pca_your_client_id';
const CLIENT_SECRET = 'pcs_your_client_secret';
const POSTIZ_URL = 'https://platform.postiz.com';
const BACKEND_URL = 'https://api.postiz.com';
const REDIRECT_URL = 'https://yourapp.com/callback';

// Step 2: Redirect user to Postiz
app.get('/connect', (req, res) => {
  const state = crypto.randomBytes(16).toString('hex');
  // Store state in session for CSRF verification
  req.session.oauthState = state;

  const params = new URLSearchParams({
    client_id: CLIENT_ID,
    response_type: 'code',
    state,
  });

  res.redirect(`${POSTIZ_URL}/oauth/authorize?${params}`);
});

// Step 3 & 4: Handle callback and exchange code
app.get('/callback', async (req, res) => {
  const { code, state, error } = req.query;

  // Check for denial
  if (error === 'access_denied') {
    return res.send('User denied access');
  }

  // Verify state
  if (state !== req.session.oauthState) {
    return res.status(403).send('Invalid state');
  }

  // Exchange code for token
  const response = await fetch(`${BACKEND_URL}/oauth/token`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      grant_type: 'authorization_code',
      code,
      client_id: CLIENT_ID,
      client_secret: CLIENT_SECRET,
    }),
  });

  const { id, cus, access_token } = await response.json();

  // Store access_token securely and use it for API calls
  // Example: fetch user's integrations
  const integrations = await fetch(
    `${BACKEND_URL}/public/v1/integrations`,
    { headers: { Authorization: access_token } }
  ).then(r => r.json());

  res.json({ connected: true, integrations });
});

app.listen(3000);

```

* * *
## 
[​](https://docs.postiz.com/public-api/oauth#error-reference)
Error Reference
Error | When | Description  
---|---|---  
`invalid_client` | Token exchange | Client ID or Client Secret is wrong  
`invalid_grant` | Token exchange | Code is invalid, expired, or already used  
`unsupported_grant_type` | Token exchange |  `grant_type` is not `authorization_code`  
`access_denied` | Callback | User denied the authorization request  
Was this page helpful?
YesNo
Ctrl+I
[discord](https://discord.postiz.com)
On this page
  * [Overview](https://docs.postiz.com/public-api/oauth#overview)
  * [How It Works](https://docs.postiz.com/public-api/oauth#how-it-works)
  * [Implementation](https://docs.postiz.com/public-api/oauth#implementation)
  * [Managing Your App](https://docs.postiz.com/public-api/oauth#managing-your-app)
  * [Rotate Client Secret](https://docs.postiz.com/public-api/oauth#rotate-client-secret)
  * [Delete Your App](https://docs.postiz.com/public-api/oauth#delete-your-app)
  * [Full Example (Node.js)](https://docs.postiz.com/public-api/oauth#full-example-node-js)
  * [Error Reference](https://docs.postiz.com/public-api/oauth#error-reference)


![Logo](https://postiz.com/favicon.ico)
Postiz
Hi! Im the Postiz AI Chatbot, ask me any question you'd like, and I will answer it the best to my abilities!
QUICK QUESTIONS
Made by 
Chat