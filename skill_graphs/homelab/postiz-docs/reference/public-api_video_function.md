[Skip to main content](https://docs.postiz.com/public-api/uploads/upload-file#content-area)
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
  * [School Settings](https://docs.postiz.com/public-api/providers/school)
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
Uploads
Upload File
[Documentation](https://docs.postiz.com/introduction)[Public API](https://docs.postiz.com/public-api/introduction)[CLI](https://docs.postiz.com/cli/introduction)[MCP](https://docs.postiz.com/mcp/introduction)[Developer App (oAuth2)](https://docs.postiz.com/public-api/oauth)[Contributing](https://docs.postiz.com/developer-guide)
[Documentation](https://docs.postiz.com/introduction)[Public API](https://docs.postiz.com/public-api/introduction)[CLI](https://docs.postiz.com/cli/introduction)[MCP](https://docs.postiz.com/mcp/introduction)[Developer App (oAuth2)](https://docs.postiz.com/public-api/oauth)[Contributing](https://docs.postiz.com/developer-guide)
Uploads
# Upload File
Copy page
Upload a media file using multipart form data.
Copy page
POST
https://api.postiz.com/public/v1 https://{your-domain}/api/public/v1
/
upload
Try it
Upload a file
cURL
```
curl --request POST \
  --url https://api.postiz.com/public/v1/upload \
  --header 'Authorization: <api-key>' \
  --header 'Content-Type: multipart/form-data' \
  --form file='@example-file'
```

200
```
{
  "id": "e639003b-f727-4a1e-87bd-74a2c48ae41e",
  "name": "image.png",
  "path": "https://uploads.postiz.com/image.png",
  "organizationId": "85460a39-6329-4cf4-a252-187ce89a3480",
  "createdAt": "2024-12-14T08:18:54.274Z",
  "updatedAt": "2024-12-14T08:18:54.274Z"
}
```

##
[​](https://docs.postiz.com/public-api/uploads/upload-file#usage)
Usage
After uploading, use the returned `id` and `path` in your post’s `image` array:
```
{
  "image": [
    {
      "id": "returned-id",
      "path": "returned-path-url"
    }
  ]
}

```

#### Authorizations
[​](https://docs.postiz.com/public-api/uploads/upload-file#authorization-authorization)
Authorization
string
header
required
Your Postiz API key
#### Body
multipart/form-data
[​](https://docs.postiz.com/public-api/uploads/upload-file#body-file)
file
file
required
The file to upload
#### Response
200 - application/json
File uploaded successfully
[​](https://docs.postiz.com/public-api/uploads/upload-file#response-id)
id
string
Unique file ID
[​](https://docs.postiz.com/public-api/uploads/upload-file#response-name)
name
string
File name
[​](https://docs.postiz.com/public-api/uploads/upload-file#response-path)
path
string
File URL
[​](https://docs.postiz.com/public-api/uploads/upload-file#response-organization-id)
organizationId
string
[​](https://docs.postiz.com/public-api/uploads/upload-file#response-created-at)
createdAt
string<date-time>
[​](https://docs.postiz.com/public-api/uploads/upload-file#response-updated-at)
updatedAt
string<date-time>
Was this page helpful?
YesNo
[Previous](https://docs.postiz.com/public-api/notifications/list)[ Upload from URLUpload a file from an existing URL. Next ](https://docs.postiz.com/public-api/uploads/upload-from-url)
Ctrl+I
[discord](https://discord.postiz.com)
Upload a file
cURL
```
curl --request POST \
  --url https://api.postiz.com/public/v1/upload \
  --header 'Authorization: <api-key>' \
  --header 'Content-Type: multipart/form-data' \
  --form file='@example-file'
```

200
```
{
  "id": "e639003b-f727-4a1e-87bd-74a2c48ae41e",
  "name": "image.png",
  "path": "https://uploads.postiz.com/image.png",
  "organizationId": "85460a39-6329-4cf4-a252-187ce89a3480",
  "createdAt": "2024-12-14T08:18:54.274Z",
  "updatedAt": "2024-12-14T08:18:54.274Z"
}
```

![Logo](https://postiz.com/favicon.ico)
Postiz
Hi! Im the Postiz AI Chatbot, ask me any question you'd like, and I will answer it the best to my abilities!
QUICK QUESTIONS
Made by
Chat
