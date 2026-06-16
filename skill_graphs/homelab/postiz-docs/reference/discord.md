# Discord
Source: https://docs.postiz.com/providers/discord

How to add Discord to your system

<Snippet />

<Note>
  This integration requires that you have **Manage Server** permissions on the Discord server you want to integrate with.
</Note>

<Steps>
  <Step title="Create a Discord Application">
    Login to Discord on the web, and then go to the [Discord Developer Portal](https://discord.com/developers/applications) and click on "New Application".

    <img alt="New Application" />
  </Step>

  <Step title="Add an App Icon">
    <img alt="App Icon" />

    Upload the App Icon of your choice (1024x1024px max) and save your changes. If you do not do this, you will get 404 errors in logs when trying to add the Discord channel in the Postiz web interface.
  </Step>

  <Step title="Get and set your Client ID and Client Secret">
    You can find this in the **OAuth2** section of the Discord Developer Portal.

    <img alt="Copy Keys" />

    Set these in your .env file as follows;

    ```env theme={null}
    DISCORD_CLIENT_ID="your_client_id"
    DISCORD_CLIENT_SECRET="your_client_secret"
    ```
  </Step>

  <Step title="Add a Redirect URI">
    <Snippet />

    **Your Discord OAuth2 Redirect URI:**

    * Production: `https://your-postiz-domain.com/integrations/social/discord`
    * Local development: `http://localhost:4200/integrations/social/discord`
    * Docker: `http://localhost:5000/integrations/social/discord`

    You can find this in the **OAuth2** section of the Discord Developer Portal.

    <img alt="Redirect URI" />
  </Step>

  <Step title="Create a Bot">
    Navigate to the "Bot" section of the Discord Developer Portal. Fill out the bot details however you like, and then click "Reset Token".

    With the token that is generated, set it in your .env file as follows;

    ```env theme={null}
    DISCORD_BOT_TOKEN_ID="your_bot_token"
    ```

    If you do not set this, you will get 404 errors when trying to add the Discord channel in the Postiz web interface.

    Stop Postiz if it is running, and then start it using the .env file with the Discord details.
  </Step>

  <Step title="Add a Discord channel in the Postiz web interface">
    Go to the Postiz web interface, and click on the "Add Channel" button, and then select "Discord". You should be redirected to Discord to login.
  </Step>
</Steps>
