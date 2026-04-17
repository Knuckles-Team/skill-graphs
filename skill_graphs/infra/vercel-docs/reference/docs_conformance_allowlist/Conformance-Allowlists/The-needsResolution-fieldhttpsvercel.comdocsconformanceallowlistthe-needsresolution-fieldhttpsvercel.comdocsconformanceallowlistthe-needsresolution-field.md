##  [The `needsResolution` field](https://vercel.com/docs/conformance/allowlist#the-needsresolution-field)[](https://vercel.com/docs/conformance/allowlist#the-needsresolution-field)
This field is used by the CLI and our metrics to assess if an allowlisted issue is something that needs to be resolved. The default value is `true`. When set to `false`, this issue is considered to be "accepted" by the team and will not show up in future metrics.
As this field was added after the release of Conformance, the value of this field is considered `true` when the field is missing from an allowlist entry.
