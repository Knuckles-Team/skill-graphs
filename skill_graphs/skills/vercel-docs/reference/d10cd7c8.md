##  [Environment variable prefixes](https://vercel.com/docs/integrations/create-integration/marketplace-api#environment-variable-prefixes)[](https://vercel.com/docs/integrations/create-integration/marketplace-api#environment-variable-prefixes)
When you provision a resource or update secrets, you can include an optional `prefix` field for each secret. Vercel prepends this prefix to the secret name when creating environment variables in connected projects. This lets users connect the same resource type to multiple projects, or multiple resources to one project, without name collisions.
For example, to return secrets with a prefix during provisioning:
Provision resource response with prefixes
```
{
  "secrets": [
    {
      "name": "PGHOST",
      "value": "db.example.com",
      "prefix": "ACME"
    },
    {
      "name": "PGPASSWORD",
      "value": "your_password_here",
      "prefix": "ACME"
    }
  ]
}
```

This creates `ACME_PGHOST` and `ACME_PGPASSWORD` as environment variables in the connected project.
Vercel normalizes hyphens and spaces in prefix values to underscores. For example, a prefix of `MY-DB` becomes `MY_DB`. If a secret name already starts with the prefix (for example, `ACME_PGHOST` with prefix `ACME`), Vercel skips prefixing to avoid duplication.
Users can also set a custom prefix when connecting a resource to a project. Learn more about [how prefixes work](https://vercel.com/docs/integrations/create-integration/native-integration#differentiate-variables-with-prefixes).
