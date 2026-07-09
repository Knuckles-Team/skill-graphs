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
