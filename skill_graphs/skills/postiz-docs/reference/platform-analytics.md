# Platform Analytics
Source: https://docs.postiz.com/public-api/analytics/platform

GET /analytics/{integration}
Get analytics data for a specific integration/channel. Returns metrics like followers, impressions, engagement, etc. depending on the platform.

## Path parameter: `integration`

The `{integration}` path parameter must be the integration's **`id`** (the UUID-shaped string returned by `GET /public/v1/integrations`).

It is **not** the platform `__type` (e.g. `x`, `linkedin`) and **not** the channel display name. Passing either of those will return `400 Invalid integration`.

```bash theme={null}
