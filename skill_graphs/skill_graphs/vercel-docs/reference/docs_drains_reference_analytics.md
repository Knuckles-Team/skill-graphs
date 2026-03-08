Drains
Drains
# Working with Drains
Last updated January 7, 2026
Drains are available on [Enterprise](https://vercel.com/docs/plans/enterprise) and [Pro](https://vercel.com/docs/plans/pro) plans
Drains let you forward observability data from your applications to external services for debugging, performance optimization, analysis, and alerting, so that you can:
  * Store observability data persistently in your preferred external services
  * Process large volumes of telemetry data using your own tools
  * Set up alerts based on application behavior patterns
  * Build custom metrics and dashboards from your data


##  [Getting started with Drains](https://vercel.com/docs/drains#getting-started-with-drains)[](https://vercel.com/docs/drains#getting-started-with-drains)
You can add Drains in two ways:
  * Custom endpoints: [Configure](https://vercel.com/docs/drains/using-drains#configuring-drains) any data type to send to a [custom HTTP endpoint](https://vercel.com/docs/drains/using-drains#custom-endpoint)
  * Native integrations: [Configure](https://vercel.com/docs/drains/using-drains#configuring-drains) logs and trace data types to send to popular services like Dash0 and Braintrust using [native integrations](https://vercel.com/docs/drains/using-drains#native-integrations)


Learn how to [manage your active drains](https://vercel.com/docs/drains/using-drains#managing-your-active-drains).
##  [Data types](https://vercel.com/docs/drains#data-types)[](https://vercel.com/docs/drains#data-types)
You can drain four types of data:
  * Logs: Runtime, build, and static logs from your deployments (supports custom endpoints and native integrations)
  * Traces: Distributed tracing data in OpenTelemetry format (supports custom endpoints and native integrations)
  * Speed Insights: Performance metrics and web vitals (custom endpoints only)
  * Web Analytics: Page views and custom events (custom endpoints only)


###  [Data type references](https://vercel.com/docs/drains#data-type-references)[](https://vercel.com/docs/drains#data-type-references)
Each drain data type has specific formats, fields, and schemas. Review the reference documentation for [logs](https://vercel.com/docs/drains/reference/logs), [traces](https://vercel.com/docs/drains/reference/traces), [speed insights](https://vercel.com/docs/drains/reference/speed-insights), and [analytics](https://vercel.com/docs/drains/reference/analytics) to understand the data structure you'll receive from each data type.
##  [REST API `schemas` property](https://vercel.com/docs/drains#rest-api-schemas-property)[](https://vercel.com/docs/drains#rest-api-schemas-property)
When you [create](https://vercel.com/docs/rest-api/drains/create-a-new-drain) or [update](https://vercel.com/docs/rest-api/drains/update-an-existing-drain) drains through the REST API, use the `schemas` property in the request body to specify which data type the drain receives. Each drain handles one data type.
The `schemas` object maps a schema name to a version object:
```
{
  schemas: {
    [schemaName: string]: {
      version: string;
    };
  }
}
```

The following table lists the available schema names:
Schema name | Version | Data type
---|---|---
`log` | `v1` | Runtime, build, and static logs
`trace` | `v1` | Distributed tracing data in OpenTelemetry format
`analytics` | `v1` | Web Analytics page views and custom events
`speed_insights` | `v1` | Performance metrics and web vitals
For example, to create a log drain, set `log` as the schema name with version `v1`:
```
{
  "schemas": {
    "log": { "version": "v1" }
  }
}
```

You also use the `schemas` property when [validating drain delivery configuration](https://vercel.com/docs/rest-api/drains/validate-drain-delivery-configuration). Pass the same `schemas` and `delivery` values you plan to use when creating the drain to verify your endpoint before the drain is live.
For details on the data each schema delivers, see the reference docs for [logs](https://vercel.com/docs/drains/reference/logs), [traces](https://vercel.com/docs/drains/reference/traces), [speed insights](https://vercel.com/docs/drains/reference/speed-insights), and [analytics](https://vercel.com/docs/drains/reference/analytics).
##  [Security](https://vercel.com/docs/drains#security)[](https://vercel.com/docs/drains#security)
You can secure your drains by checking for valid signatures and hiding IP addresses. Learn how to [add security to your drains](https://vercel.com/docs/drains/security).
##  [Usage and pricing](https://vercel.com/docs/drains#usage-and-pricing)[](https://vercel.com/docs/drains#usage-and-pricing)
Drains are available to all users on the [Pro](https://vercel.com/docs/plans/pro-plan) and [Enterprise](https://vercel.com/docs/plans/enterprise) plans. If you are on the [Hobby](https://vercel.com/docs/plans/hobby) or [Pro Trial](https://vercel.com/docs/plans/pro-plan/trials) plan, you'll need to [upgrade to Pro](https://vercel.com/docs/plans/hobby#upgrading-to-pro) to access drains.
Drains usage is billed based on the pricing table below. Pricing is the same regardless of data type:
Resource | Price | Included (Pro)
---|---|---
[Drains](https://vercel.com/docs/drains#usage-and-pricing) | $0.50 per 1 GB | N/A
See [Optimizing Drains](https://vercel.com/docs/pricing/observability#optimizing-drains-usage) for information on how to manage costs associated with Drains.
##  [More resources](https://vercel.com/docs/drains#more-resources)[](https://vercel.com/docs/drains#more-resources)
For more information on Drains, check out the following resources:
  * [Configure Drains](https://vercel.com/docs/drains/using-drains)
  * [Log Drains reference](https://vercel.com/docs/drains/reference/logs)
  * [Traces reference](https://vercel.com/docs/drains/reference/traces)
  * [Speed Insights reference](https://vercel.com/docs/drains/reference/speed-insights)
  * [Analytics reference](https://vercel.com/docs/drains/reference/analytics)
  * [Drains REST API endpoints](https://vercel.com/docs/rest-api/drains)


* * *
[ Previous Speed Insights ](https://vercel.com/docs/speed-insights)[ Next Using Drains ](https://vercel.com/docs/drains/using-drains)
Was this helpful?
Send
Drains
# Web Analytics Drains Reference
Last updated September 24, 2025
If a Web Analytics Drains has been configured, Vercel will send page views and custom events from your applications to external endpoints for storage and analysis over HTTPS when your application tracks events.
##  [Web Analytics Schema](https://vercel.com/docs/drains#web-analytics-schema)[](https://vercel.com/docs/drains#web-analytics-schema)
The following table describes the possible fields that are sent via Web Analytics Drains:
Name | Type | Description | Example
---|---|---|---
`schema` | string | Schema version identifier | `vercel.analytics.v1`
`eventType` | string | Type of analytics event |  `pageview` or `event`
`eventName` | string | Name of the custom event | `button_click`
`eventData` | string | Additional data associated with the event | `{"button": "signup"}`
`timestamp` | number | Unix timestamp when the event was recorded | 1694723400000
`projectId` | string | Identifier for the Vercel project | `Qmc52npNy86S8VV4Mt8a8dP1LEkRNbgosW3pBCQytkcgf2`
`ownerId` | string | Identifier for the project owner | `team_nLlpyC6REAqxydlFKbrMDlud`
`dataSourceName` | string | Name of the data source | `web-analytics`
`sessionId` | number | Unique session identifier | 12345
`deviceId` | number | Unique device identifier | 67890
`origin` | string | Origin URL where the event was recorded | `https://example.com`
`path` | string | URL path where the event was recorded | `/dashboard`
`referrer` | string | Referrer URL | `https://google.com`
`queryParams` | string | Query parameters from the URL | `utm_source=google&utm_medium=cpc`
`route` | string | Route pattern for the page | `/dashboard/[id]`
`country` | string | Country code of the user | `US`
`region` | string | Region code of the user | `CA`
`city` | string | City of the user | `San Francisco`
`osName` | string | Operating system name | `macOS`
`osVersion` | string | Operating system version | `13.4`
`clientName` | string | Client browser name | `Chrome`
`clientType` | string | Type of client | `browser`
`clientVersion` | string | Client browser version | `114.0.5735.90`
`deviceType` | string | Type of device | `desktop`
`deviceBrand` | string | Device brand | `Apple`
`deviceModel` | string | Device model | `MacBook Pro`
`browserEngine` | string | Browser engine name | `Blink`
`browserEngineVersion` | string | Browser engine version | `114.0.5735.90`
`sdkVersion` | string | SDK version used to track events | `2.1.0`
`sdkName` | string | SDK name used to track events | `@vercel/analytics`
`sdkVersionFull` | string | Full SDK version string | `2.1.0-beta.1`
`vercelEnvironment` | string | Vercel environment | `production`
`vercelUrl` | string | Vercel deployment URL | `*.vercel.app`
`flags` | string | Feature flags information | `{"feature_a": true}`
`deployment` | string | Identifier for the Vercel deployment | `dpl_2YZzo1cJAjijSf1hwDFK5ayu2Pid`
##  [Format](https://vercel.com/docs/drains#format)[](https://vercel.com/docs/drains#format)
Vercel supports the following formats for Web Analytics Drains, which you can configure when [setting the Drain destination](https://vercel.com/docs/drains/using-drains#configure-destination):
###  [JSON](https://vercel.com/docs/drains#json)[](https://vercel.com/docs/drains#json)
Vercel sends Web Analytics data as JSON arrays containing event objects:
```
[
  { "schema": "vercel.analytics.v1", "eventType": "pageview", "timestamp": 1694723400000, "projectId": "Qmc52npNy86S8VV4Mt8a8dP1LEkRNbgosW3pBCQytkcgf2", "ownerId": "team_nLlpyC6REAqxydlFKbrMDlud", "dataSourceName": "web-analytics", "sessionId": 12345, "deviceId": 67890, "origin": "https://example.com", "path": "/dashboard" },
  { "schema": "vercel.analytics.v1", "eventType": "event", "eventName": "button_click", "eventData": "{\"button\": \"signup\"}", "timestamp": 1694723405000, "projectId": "Qmc52npNy86S8VV4Mt8a8dP1LEkRNbgosW3pBCQytkcgf2", "ownerId": "team_nLlpyC6REAqxydlFKbrMDlud", "dataSourceName": "web-analytics", "sessionId": 12345, "deviceId": 67890, "origin": "https://example.com", "path": "/signup" }
]
```

###  [NDJSON](https://vercel.com/docs/drains#ndjson)[](https://vercel.com/docs/drains#ndjson)
Vercel sends Web Analytics data as newline-delimited JSON objects:
```
{"schema": "vercel.analytics.v1","eventType": "pageview","timestamp": 1694723400000,"projectId": "Qmc52npNy86S8VV4Mt8a8dP1LEkRNbgosW3pBCQytkcgf2","ownerId": "team_nLlpyC6REAqxydlFKbrMDlud","dataSourceName": "web-analytics","sessionId": 12345,"deviceId": 67890,"origin": "https://example.com","path": "/dashboard"}
{"schema": "vercel.analytics.v1","eventType": "event","eventName": "button_click","eventData": "{\"button\": \"signup\"}","timestamp": 1694723405000,"projectId": "Qmc52npNy86S8VV4Mt8a8dP1LEkRNbgosW3pBCQytkcgf2","ownerId": "team_nLlpyC6REAqxydlFKbrMDlud","dataSourceName": "web-analytics","sessionId": 12345,"deviceId": 67890,"origin": "https://example.com","path": "/signup"}
```

##  [Sampling Rate](https://vercel.com/docs/drains#sampling-rate)[](https://vercel.com/docs/drains#sampling-rate)
When you configure a Web Analytics Drain in the Vercel UI, you can set the sampling rate to control the volume of data sent. This helps manage costs when you have high traffic volumes.
##  [More resources](https://vercel.com/docs/drains#more-resources)[](https://vercel.com/docs/drains#more-resources)
For more information on Web Analytics Drains and how to use them, refer to the following resources:
  * [Drains overview](https://vercel.com/docs/drains)
  * [Configure Drains](https://vercel.com/docs/drains/using-drains)


* * *
[ Previous Speed Insights ](https://vercel.com/docs/speed-insights)[ Next Using Drains ](https://vercel.com/docs/drains/using-drains)
Was this helpful?
Send
