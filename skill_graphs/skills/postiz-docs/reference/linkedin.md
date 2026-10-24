# LinkedIn
Source: https://docs.postiz.com/providers/linkedin

How to add LinkedIn to your system

<Snippet />

<Steps>
  <Step title="Create a new app">
    Head over to [LinkedIn developers](https://www.linkedin.com/developers/apps) and create a new app.

    <img alt="LinkedIn" />
  </Step>

  <Step title="Add required products">
    Fill in all the details, once created head over to Products and make sure you add all the required products.

    <img alt="LinkedIn" />

    <Warning>
      It is important to request the Advertising API permissions and fill up the request form, or you will not have the ability to refresh your tokens.
    </Warning>
  </Step>

  <Step title="Configure OAuth2 Redirect URI">
    <Snippet />

    **Your LinkedIn OAuth2 Redirect URI:**

    * Production: `https://your-postiz-domain.com/integrations/social/linkedin`
    * Local development: `http://localhost:4200/integrations/social/linkedin`
    * Docker: `http://localhost:5000/integrations/social/linkedin`

    <Note>
      If you are using the "LinkedIn Page" provider, replace `linkedin` with `linkedin-page` in the redirect URI.
    </Note>
  </Step>

  <Step title="Copy your credentials">
    Copy the created `Client ID` and `Client Secret` and add them to your `.env` file.

    ```env theme={null}
    LINKEDIN_CLIENT_ID=""
    LINKEDIN_CLIENT_SECRET=""
    ```

    You can find those under the Auth Tab of your LinkedIn App in the developer portal.
  </Step>
</Steps>
