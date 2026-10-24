##  [Schema validation](https://vercel.com/docs/edge-config/edge-config-dashboard#schema-validation)[](https://vercel.com/docs/edge-config/edge-config-dashboard#schema-validation)
You can protect your Edge Config by adding a JSON schema to it. Vercel uses this schema to validate the data that is added to the store and prevent updates that fail validation. To add a schema:
  1. From your [dashboard](https://vercel.com/dashboard), open [Storage](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fstores&title=Go+to+Storage) in the sidebar and then select your Edge Config
  2. Toggle the Schema button to open the schema editing tab
  3. Enter your
  4. Click Save. This will save changes to both the schema and data


The following snippet is an example of a schema that allows you to set boolean flags and a list of redirects.
schema.json
```
{
  "$schema": "http://json-schema.org/draft-07/schema",
  "type": "object",
  "additionalProperties": false,
  "required": ["flags", "redirects"],
  "properties": {
    "flags": {
      "type": "object",
      "patternProperties": {
        "^.*$": {
          "type": "boolean"
        }
      }
    },
    "redirects": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "from": { "type": "string" },
          "to": { "type": "string" }
        }
      }
    }
  }
}
```
