##  [High level overview](https://vercel.com/docs/getting-started-with-vercel#high-level-overview)[](https://vercel.com/docs/getting-started-with-vercel#high-level-overview)
Sign in with Vercel is based on the OAuth 2.0 authorization framework, which allows your application to request access to user data from Vercel's Identity Provider (IdP). The IdP is a secure way to authenticate users without managing their credentials.
  1. A user clicks the Sign in with Vercel button in your application
  2. Your application redirects the user to Vercel's IdP consent page (or opens it in a popup window)
  3. They review the permissions and click Allow
  4. After approval by the user, Vercel sends your application a short lived `code` to your pre-registered callback URL
  5. Your application swaps the `code` for tokens
  6. Your application uses those tokens to identify the user and log them into your application


###  [Tokens](https://vercel.com/docs/getting-started-with-vercel#tokens)[](https://vercel.com/docs/getting-started-with-vercel#tokens)
  * ID Token: A signed JWT that proves who the user is. Your application verifies its signature and read claims to identify the user
  * Access Token: A bearer token your application uses to call the Vercel REST API for the permissions the user grants. This lasts for 1 hour
  * Refresh Token: This token lets your application get a new Access Token without asking the user to sign in again. This lasts for 30 days and rotates each time it's used


Learn more about each token in the [tokens](https://vercel.com/docs/sign-in-with-vercel/tokens) documentation.
###  [Scopes and permissions](https://vercel.com/docs/getting-started-with-vercel#scopes-and-permissions)[](https://vercel.com/docs/getting-started-with-vercel#scopes-and-permissions)
Scopes decide what identity information from the user goes into the ID Token and whether to issue a Refresh Token.
Learn more about scopes and permissions in the [scopes and permissions](https://vercel.com/docs/sign-in-with-vercel/scopes-and-permissions) documentation.
###  [Consent page](https://vercel.com/docs/getting-started-with-vercel#consent-page)[](https://vercel.com/docs/getting-started-with-vercel#consent-page)
The first time someone tries to sign in to your application, Vercel will show them a consent page to review the permissions your application is requesting. This page includes your application's name, logo, and the requested permissions.
If the user grants access, they are redirected back to your application where you can use the tokens to identify the user and log them into your application.
If they cancel the sign in, they are redirected back to your application where you can handle the failed sign in state in your application (for example with a custom error page).
Learn more about the consent page in the [consent page](https://vercel.com/docs/sign-in-with-vercel/consent-page) documentation.
