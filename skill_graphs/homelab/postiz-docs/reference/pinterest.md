# Pinterest
Source: https://docs.postiz.com/providers/pinterest

How to add Pinterest to your system

<Snippet />

<Note>
  This integration requires that you have a Pinterest Company Account.
</Note>

<Steps>
  <Step title="Create Pinterest App">
    Head to [Pinterest Developer Dashboard](https://developers.pinterest.com/apps/) and create your App. Fill out all required Information and wait on the App to get approved.
  </Step>

  <Step title="Copy the App ID and Secret">
    Copy the App ID at "App id" and the Secret Key at "App secret key"

    <img alt="Copy App ID and Secret" />
  </Step>

  <Step title="Configure Redirect URI">
    <Snippet />

    **Your Pinterest OAuth2 Redirect URI:**

    * Production: `https://your-postiz-domain.com/integrations/social/pinterest`
    * Local development: `http://localhost:4200/integrations/social/pinterest`
    * Docker: `http://localhost:5000/integrations/social/pinterest`

      <img alt="Setup of Redirect URIs" />
  </Step>

  <Step title="Add environment variables">
    ```env theme={null}
    PINTEREST_CLIENT_ID=""
    PINTEREST_CLIENT_SECRET=""
    ```

    You should now be able to add the Pinterest Provider to your User / Team Account.
  </Step>
</Steps>
