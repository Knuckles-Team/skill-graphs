##  [Anatomy of an allowlist entry](https://vercel.com/docs/conformance/allowlist#anatomy-of-an-allowlist-entry)[](https://vercel.com/docs/conformance/allowlist#anatomy-of-an-allowlist-entry)
An allowlist entry looks like the following:
my-site/.allowlists
```
{
  "testName": "NEXTJS_MISSING_SECURITY_HEADERS",
  "entries": [
    {
      "testName": "NEXTJS_MISSING_SECURITY_HEADERS",
      "reason": "TODO: This existed before the Conformance test was added but should be fixed.",
      "location": {
        "workspace": "dashboard",
        "filePath": "next.config.js"
      },
      "details": {
        "missingField": "headers"
      }
    }
  ]
}
```

The allowlist entry contains the following fields:
  * `testName`: The name of the triggered test
  * `needsResolution`: Whether the allowlist entry needs to be resolved
  * `reason`: Why this code instance is allowed despite Conformance catching it
  * `location`: The file path containing the error
  * `details` (optionally): Details about the Conformance error


An allowlist entry will match an existing one when the `testName`, `location`, and `details` fields all match. The `reason` is only used for documentation purposes.
