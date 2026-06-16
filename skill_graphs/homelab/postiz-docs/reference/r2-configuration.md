# R2 Configuration
Source: https://docs.postiz.com/configuration/r2

How to use Cloudflare R2 for file storage

If you do not wish to (or can't) use local storage, an alternative way to upload images is to configure R2. It's free.

<Steps>
  <Step title="Create account and login to the console">
    Go to the [Cloudflare Dashboard](https://dash.cloudflare.com/r2/overview), and register if needed, then login.
  </Step>

  <Step title="Create a new Bucket">
    In the dashboard sidebar, and head to the R2 page.

    <img alt="R2 Page" />

    Create a new Bucket.

    * Choose Automatic
    * Choose Standard

    <img alt="Create Bucket" />
  </Step>

  <Step title="Create your R2 Token">
    Create your R2 Token by going to R2 Object Storage:

    <img alt="R2 Object Storage" />

    Click on the API dropdown, and select [Manage API tokens](https://dash.cloudflare.com/?to=/:account/r2/api-tokens):

    <img alt="Manage API tokens" />

    Copy your Account ID for later, and click on "Create an API token":

    <img alt="Create API Token" />

    Create an Account API token:

    <img alt="Account API Token" />

    Under "Permissions" choose "Object Read & Write" and under "Specify bucket(s)" search for your created Bucket.

    <img alt="Permissions" />
  </Step>

  <Step title="Copy your credentials">
    After the R2 Token is created, copy your "Access Key ID" and "Secret Access Key":

    <img alt="Copy Credentials" />

    Paste the respective information into your .env environment.

    ```env theme={null}
    CLOUDFLARE_ACCOUNT_ID="accountId"
    CLOUDFLARE_ACCESS_KEY="accessKey"
    CLOUDFLARE_SECRET_ACCESS_KEY="secretAccessKey"
    CLOUDFLARE_BUCKETNAME="bucketName"
    CLOUDFLARE_REGION="region (like wnam)"
    ```
  </Step>

  <Step title="Configure Custom Domain and CORS policies">
    Go to configuration and connect a custom domain (if you don't have one, you can use the one that CloudFlare provides.)
    Add it to your .env file.

    ```env theme={null}
    CLOUDFLARE_BUCKET_URL="https://customdomain.com"
    ```

    <img alt="Custom Domain" />

    Click to edit the CORS policy and add the following JSON:

    ```json theme={null}
    [
      {
        "AllowedOrigins": [
          "http://localhost:4200",
          "https://yourDomain.com"
        ],
        "AllowedMethods": [
          "GET",
          "POST",
          "HEAD",
          "PUT",
          "DELETE"
        ],
        "AllowedHeaders": [
          "Authorization",
          "x-amz-date",
          "x-amz-content-sha256",
          "content-type"
        ],
        "ExposeHeaders": [
          "ETag",
          "Location"
        ],
        "MaxAgeSeconds": 3600
      }
    ]
    ```

    <img alt="CORS Policy" />
  </Step>
</Steps>
