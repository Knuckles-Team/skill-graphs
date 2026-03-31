[Skip to main content](https://docs.postiz.com/public-api/integrations/list#content-area)
[Postiz Documentation home page![light logo](https://mintcdn.com/postiz/SZ3zBABjhg7UQcI8/logo/light.png?fit=max&auto=format&n=SZ3zBABjhg7UQcI8&q=85&s=ab950a1a5aa687eb0de8156022f7c7c9)![dark logo](https://mintcdn.com/postiz/SZ3zBABjhg7UQcI8/logo/dark.png?fit=max&auto=format&n=SZ3zBABjhg7UQcI8&q=85&s=4134d88b8fc8339a26775f8e48e95f7e)](https://docs.postiz.com/)
Search...
Ctrl K
  * [Discord](https://discord.postiz.com)


##### Overview
  * [API Overview](https://docs.postiz.com/public-api/introduction)


##### Integrations
  * [GET List Integrations](https://docs.postiz.com/public-api/integrations/list)
  * [GET Connect Channel (OAuth)](https://docs.postiz.com/public-api/integrations/connect)
  * [DEL Delete Channel](https://docs.postiz.com/public-api/integrations/delete)
  * [GET Check Connection](https://docs.postiz.com/public-api/integrations/is-connected)
  * [GET Find Available Slot](https://docs.postiz.com/public-api/integrations/find-slot)


##### Posts
  * [GET List Posts](https://docs.postiz.com/public-api/posts/list)
  * [POST Create Post](https://docs.postiz.com/public-api/posts/create)
  * [DEL Delete Post](https://docs.postiz.com/public-api/posts/delete)
  * [DEL Delete Post by Group](https://docs.postiz.com/public-api/posts/delete-by-group)
  * [GET Get Missing Content](https://docs.postiz.com/public-api/posts/missing-content)
  * [PUT Update Release ID](https://docs.postiz.com/public-api/posts/update-release-id)


##### Analytics
  * [GET Platform Analytics](https://docs.postiz.com/public-api/analytics/platform)
  * [GET Post Analytics](https://docs.postiz.com/public-api/analytics/post)


##### Notifications
  * [GET List Notifications](https://docs.postiz.com/public-api/notifications/list)


##### Uploads
  * [POST Upload File](https://docs.postiz.com/public-api/uploads/upload-file)
  * [POST Upload from URL](https://docs.postiz.com/public-api/uploads/upload-from-url)


##### Video Generation
  * [POST Generate Video](https://docs.postiz.com/public-api/video/generate)
  * [POST Video Function](https://docs.postiz.com/public-api/video/function)


##### Provider Settings (25 with custom settings)
  * [X (Twitter) Settings](https://docs.postiz.com/public-api/providers/x)
  * [LinkedIn Settings](https://docs.postiz.com/public-api/providers/linkedin)
  * [Facebook Settings](https://docs.postiz.com/public-api/providers/facebook)
  * [Instagram Settings](https://docs.postiz.com/public-api/providers/instagram)
  * [Warpcast (Farcaster) Settings](https://docs.postiz.com/public-api/providers/warpcast)
  * [YouTube Settings](https://docs.postiz.com/public-api/providers/youtube)
  * [TikTok Settings](https://docs.postiz.com/public-api/providers/tiktok)
  * [Reddit Settings](https://docs.postiz.com/public-api/providers/reddit)
  * [Lemmy Settings](https://docs.postiz.com/public-api/providers/lemmy)
  * [Pinterest Settings](https://docs.postiz.com/public-api/providers/pinterest)
  * [Discord Settings](https://docs.postiz.com/public-api/providers/discord)
  * [Slack Settings](https://docs.postiz.com/public-api/providers/slack)
  * [Dribbble Settings](https://docs.postiz.com/public-api/providers/dribbble)
  * [Medium Settings](https://docs.postiz.com/public-api/providers/medium)
  * [Dev.to Settings](https://docs.postiz.com/public-api/providers/devto)
  * [Hashnode Settings](https://docs.postiz.com/public-api/providers/hashnode)
  * [WordPress Settings](https://docs.postiz.com/public-api/providers/wordpress)
  * [Listmonk Settings](https://docs.postiz.com/public-api/providers/listmonk)
  * [Google My Business Settings](https://docs.postiz.com/public-api/providers/gmb)
  * [Whop Settings](https://docs.postiz.com/public-api/providers/whop)
  * [Skool Settings](https://docs.postiz.com/public-api/providers/skool)
  * [Kick Settings](https://docs.postiz.com/public-api/providers/kick)
  * [Twitch Settings](https://docs.postiz.com/public-api/providers/twitch)
  * [Moltbook Settings](https://docs.postiz.com/public-api/providers/moltbook)


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
Integrations
List Integrations
[Documentation](https://docs.postiz.com/introduction)[Public API](https://docs.postiz.com/public-api/introduction)[CLI](https://docs.postiz.com/cli/introduction)[MCP](https://docs.postiz.com/mcp/introduction)[Developer App (oAuth2)](https://docs.postiz.com/public-api/oauth)[Contributing](https://docs.postiz.com/developer-guide)
[Documentation](https://docs.postiz.com/introduction)[Public API](https://docs.postiz.com/public-api/introduction)[CLI](https://docs.postiz.com/cli/introduction)[MCP](https://docs.postiz.com/mcp/introduction)[Developer App (oAuth2)](https://docs.postiz.com/public-api/oauth)[Contributing](https://docs.postiz.com/developer-guide)
Integrations
# List Integrations
Copy page
Returns all connected social media channels for your organization.
Copy page
GET
https://api.postiz.com/public/v1 https://{your-domain}/api/public/v1
/
integrations
Try it
List all integrations
cURL
```
curl --request GET \
  --url https://api.postiz.com/public/v1/integrations \
  --header 'Authorization: <api-key>'
```

200
```
[
  {
    "id": "cm4ean69r0003w8w1cdomox9n",
    "name": "Nevo David",
    "identifier": "x",
    "picture": "https://uploads.postiz.com/avatar.jpg",
    "disabled": false,
    "profile": "nevodavid",
    "customer": {
      "id": "customer-id",
      "name": "My Company"
    }
  }
]
```

#### Authorizations
[​](https://docs.postiz.com/public-api/integrations/list#authorization-authorization)
Authorization
string
header
required
Your Postiz API key
#### Response
200 - application/json
List of integrations
[​](https://docs.postiz.com/public-api/integrations/list#response-items-id)
id
string
Unique integration ID
[​](https://docs.postiz.com/public-api/integrations/list#response-items-name)
name
string
Display name of the account
[​](https://docs.postiz.com/public-api/integrations/list#response-items-identifier)
identifier
enum<string>
Provider identifier (27 platforms supported)
Available options:
`x`,
`linkedin`,
`linkedin-page`,
`facebook`,
`instagram`,
`instagram-standalone`,
`threads`,
`bluesky`,
`mastodon`,
`warpcast`,
`nostr`,
`vk`,
`youtube`,
`tiktok`,
`reddit`,
`lemmy`,
`discord`,
`slack`,
`telegram`,
`kick`,
`twitch`,
`pinterest`,
`dribbble`,
`medium`,
`devto`,
`hashnode`,
`wordpress`,
`gmb`,
`listmonk`,
`moltbook`,
`skool`,
`whop`
[​](https://docs.postiz.com/public-api/integrations/list#response-items-picture)
picture
string
Profile picture URL
[​](https://docs.postiz.com/public-api/integrations/list#response-items-disabled)
disabled
boolean
Whether the integration is disabled
[​](https://docs.postiz.com/public-api/integrations/list#response-items-profile)
profile
string
Profile handle/username
[​](https://docs.postiz.com/public-api/integrations/list#response-items-customer)
customer
object
Show child attributes
Was this page helpful?
YesNo
[Previous](https://docs.postiz.com/public-api/introduction)[ Connect Channel (OAuth)Generate an OAuth authorization URL for a given integration. Use this to connect a new social media channel. Only OAuth-based integrations are supported (integrations that require an external URL, such as Mastodon, are not available via this endpoint). Next ](https://docs.postiz.com/public-api/integrations/connect)
Ctrl+I
[discord](https://discord.postiz.com)
List all integrations
cURL
```
curl --request GET \
  --url https://api.postiz.com/public/v1/integrations \
  --header 'Authorization: <api-key>'
```

200
```
[
  {
    "id": "cm4ean69r0003w8w1cdomox9n",
    "name": "Nevo David",
    "identifier": "x",
    "picture": "https://uploads.postiz.com/avatar.jpg",
    "disabled": false,
    "profile": "nevodavid",
    "customer": {
      "id": "customer-id",
      "name": "My Company"
    }
  }
]
```

![Logo](https://postiz.com/favicon.ico)
Postiz
Hi! Im the Postiz AI Chatbot, ask me any question you'd like, and I will answer it the best to my abilities!
QUICK QUESTIONS
List Integrations - Postiz Documentation
← Asking about this page
Made by 
Chat