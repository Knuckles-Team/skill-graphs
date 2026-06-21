# Example of providing certificate data directly (base64 or PEM format)
client_cert_data = """-----BEGIN CERTIFICATE-----
MIICertificateDataHere...
-----END CERTIFICATE-----"""
client_key_data = """-----BEGIN PRIVATE KEY-----
MIIPrivateKeyDataHere...
-----END PRIVATE KEY-----"""
```

The [`temporal cloud login`](/cli/cloud#interactive-login) command also writes to this file. When you run `temporal cloud login --profile prod`, the OAuth token is stored in the specified profile automatically. Subsequent commands that use that profile read the token from the TOML file to authenticate with Temporal Cloud.

## CLI integration

The Temporal CLI tool includes `temporal config` commands that allow you to read and write to the TOML configuration
file. This provides a convenient way to manage your connection profiles without manually editing the file. Refer to
[Temporal CLI Reference - `temporal config`](../cli/command-reference/config.mdx) for more details.

- `temporal config get <property>`: Reads a specific value from the current profile.
- `temporal config set <property> <value>`: Sets a property in the current profile.
- `temporal config delete <property>`: Deletes a property from the current profile.
- `temporal config list`: Lists all available profiles in the config file.

These CLI commands directly manipulate the `temporal.toml` file. This differs from the SDKs, which only _read_ from the
file and environment at runtime to establish a client connection. You can select a profile for the CLI to use with the
`--profile` flag. For example, `temporal --profile prod ...`.

The following code blocks provide copy-paste-friendly examples for setting up CLI profiles for both local development
and Temporal Cloud.

<Tabs groupId="cli-profile-setup" defaultValue="api-key-basic">
  <TabItem value="api-key-basic" label="Local + Prod with Cloud API key">

This example shows how to set up a default profile for local development and a `prod` profile for Temporal Cloud using
an API key.

```bash
