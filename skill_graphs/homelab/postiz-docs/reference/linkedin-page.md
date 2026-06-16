# LinkedIn Page
Source: https://docs.postiz.com/providers/linkedin-page

How to add a LinkedIn Page to your system

<Snippet />

<Steps>
  <Step title="Create a new app">
    Head over to [LinkedIn developers](https://www.linkedin.com/developers/apps) and create a new app.

    <img alt="LinkedIn" />
  </Step>

  <Step title="Verify your app">
    Verify your app with LinkedIn

    <img alt="LinkedIn" />

    You will need to follow the verification process to request the necessary permissions listed below.
  </Step>

  <Step title="Add required products">
    Fill in all the details, once created head over to Products and make sure you add all the required products:

    * Share on LinkedIn
    * Advertising API
    * Sign in with LinkedIn using OpenID connect

    <Warning>
      It is important to request the Advertising API permissions and fill up the request form, or you will not have the ability to refresh your tokens.
    </Warning>
  </Step>

  <Step title="Configure OAuth2 Redirect URI">
    <Snippet />

    **Your LinkedIn Page OAuth2 Redirect URI:**

    * Production: `https://your-postiz-domain.com/integrations/social/linkedin-page`
    * Local development: `http://localhost:4200/integrations/social/linkedin-page`
    * Docker: `http://localhost:5000/integrations/social/linkedin-page`
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

## Posting PDFs / document carousels

LinkedIn is the only provider Postiz supports PDF posting on, and only through document-carousel posts. When you create a carousel of images on a LinkedIn Page, Postiz combines the images into a PDF document and uploads it as a LinkedIn document share. You don't upload a PDF directly — Postiz produces the PDF from your images.

This is not supported on other platforms; the public-API upload endpoint does not accept `application/pdf`.
