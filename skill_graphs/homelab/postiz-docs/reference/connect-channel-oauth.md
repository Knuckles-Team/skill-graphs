# Connect Channel (OAuth)
Source: https://docs.postiz.com/public-api/integrations/connect

GET /social/{integration}
Generate an OAuth authorization URL for a given integration. Use this to connect a new social media channel. Only OAuth-based integrations are supported (integrations that require an external URL, such as Mastodon, are not available via this endpoint).
