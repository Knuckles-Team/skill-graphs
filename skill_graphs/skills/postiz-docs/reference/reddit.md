# Reddit
Source: https://docs.postiz.com/providers/reddit

How to add Reddit to your system

<Snippet />

<Steps>
  <Step title="Create an app on Reddit Developers">
    Head over to [Reddit developers](https://www.reddit.com/prefs/apps) and click on **create a new app**.

    * **Name:** `MyPostizInstance` (or whatever you like)
    * **App type:** `web app`
    * **Redirect URI:** (see below)

    <Snippet />

    **Your Reddit OAuth2 Redirect URI:**

    * Production: `https://your-postiz-domain.com/integrations/social/reddit`
    * Local development: `http://localhost:4200/integrations/social/reddit`
    * Docker: `http://localhost:5000/integrations/social/reddit`
  </Step>

  <Step title="Set environment variables">
    Copy the Reddit client id and client secret and add them to your `.env` file.

    <img alt="Reddit" />

    ```env theme={null}
    REDDIT_CLIENT_ID=""
    REDDIT_CLIENT_SECRET=""
    ```
  </Step>
</Steps>
