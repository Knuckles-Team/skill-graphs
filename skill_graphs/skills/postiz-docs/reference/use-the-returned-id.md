# Use the returned id
curl -H "Authorization: your-api-key" \
  https://api.postiz.com/public/v1/analytics/<integration-id>
```

## Common errors

* `400 Invalid integration` — the path param is the wrong shape.
* `404 Channel not found` — the integration exists but has been disconnected. Reconnect the channel from the Postiz UI.
* Empty data — some platforms (notably Google My Business) restrict analytics by date range or by profile verification status. The endpoint returns an empty payload rather than an error.
