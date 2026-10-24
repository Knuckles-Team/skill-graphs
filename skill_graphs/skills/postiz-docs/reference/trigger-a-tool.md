# Trigger a Tool
Source: https://docs.postiz.com/public-api/integrations/trigger

POST /integration-trigger/{id}
Executes a provider-specific tool on a connected channel, for example searching Instagram audio for Reels, listing Discord channels, or fetching Reddit flairs. Discover available tools with the integration settings endpoint.

Some providers expose helper tools for fetching dynamic data needed when
constructing post settings — for example searching
[Instagram audio](/public-api/providers/instagram#audio) to attach to a Reel,
listing Discord channels, or fetching Reddit flairs.

Discover the tools available for a channel with the
[settings endpoint](/public-api/integrations/settings) — each tool entry
contains the `methodName` to pass here together with its parameter schema.
