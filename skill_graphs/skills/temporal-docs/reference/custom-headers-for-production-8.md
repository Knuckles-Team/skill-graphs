# Custom headers for production
[profile.prod.grpc_meta]
environment     = "production"
service-version = "v1.2.3"
```

You can create a Temporal Client using a profile from the configuration file as follows. In this example, you load the
`default` profile for local development:

{/* SNIPSTART typescript-env-config-load-default-profile {"highlightedLines": "17-19,28-29"} */}
[env-config/src/load-from-file.ts](https://github.com/temporalio/samples-typescript/blob/main/env-config/src/load-from-file.ts)
```ts {17-19,28-29}

async function main() {
  console.log('--- Loading default profile from config.toml ---');

  // For this sample to be self-contained, we explicitly provide the path to
  // the config.toml file included in this directory.
  // By default though, the config.toml file will be loaded from
  // ~/.config/temporalio/temporal.toml (or the equivalent standard config directory on your OS).
  const configFile = resolve(__dirname, '../config.toml');

  // loadClientConnectConfig is a helper that loads a profile and prepares
  // the configuration for Connection.connect and Client. By default, it loads the
  // "default" profile.
  const config = loadClientConnectConfig({
    configSource: { path: configFile },
  });

  console.log(`Loaded 'default' profile from ${configFile}.`);
  console.log(`  Address: ${config.connectionOptions.address}`);
  console.log(`  Namespace: ${config.namespace}`);
  console.log(`  gRPC Metadata: ${JSON.stringify(config.connectionOptions.metadata)}`);

  console.log('\nAttempting to connect to client...');
  try {
    const connection = await Connection.connect(config.connectionOptions);
    const client = new Client({ connection, namespace: config.namespace });
    console.log('✅ Client connected successfully!');
    await connection.close();
  } catch (err) {
    console.log(`❌ Failed to connect: ${err}`);
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
```
{/* SNIPEND */}

</TabItem>

<TabItem value="env-vars" label="Environment Variables">

Use the `@temporalio/envconfig` module to set connection options for the Temporal Client using environment variables.
For a list of all available environment variables and their default values, refer to
[Environment Configuration](/references/client-environment-configuration).

For example, the following code snippet loads all environment variables and creates a Temporal Client with the options
specified in those variables. If you have defined a configuration file at either the default location
(`~/.config/temporalio/temporal.toml`) or a custom location specified by the `TEMPORAL_CONFIG_FILE` environment
variable, this will also load the default profile in the configuration file. However, any options set via environment
variables will take precedence.

Set the following environment variables before running your application. Replace the placeholder values with your actual
configuration. Since this is for a local development Temporal Service, the values connect to `localhost:7233` and the
`default` Namespace. You may omit these variables entirely since they're the defaults.

```bash
export TEMPORAL_NAMESPACE="default"
export TEMPORAL_ADDRESS="localhost:7233"
```

After setting the environment variables, use the following code to create the Temporal Client. Since the environment
variables take precedence, they will override any values set in the configuration file. Therefore, you may leave
`loadClientConnectConfig`'s arguments empty:

{/* SNIPSTART typescript-env-config-load-default-profile {"highlightedLines": "7,17-18", "selectedLines": ["1-5","17","19","22-40"]} */}
[env-config/src/load-from-file.ts](https://github.com/temporalio/samples-typescript/blob/main/env-config/src/load-from-file.ts)
```ts {7,17-18}

async function main() {
// ...
  const config = loadClientConnectConfig({
// ...
  });
// ...
  console.log(`  Address: ${config.connectionOptions.address}`);
  console.log(`  Namespace: ${config.namespace}`);
  console.log(`  gRPC Metadata: ${JSON.stringify(config.connectionOptions.metadata)}`);

  console.log('\nAttempting to connect to client...');
  try {
    const connection = await Connection.connect(config.connectionOptions);
    const client = new Client({ connection, namespace: config.namespace });
    console.log('✅ Client connected successfully!');
    await connection.close();
  } catch (err) {
    console.log(`❌ Failed to connect: ${err}`);
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
```
{/* SNIPEND */}

</TabItem>

<TabItem value="code" label="Code">

If you don't want to use environment variables or a configuration file, you can specify connection options directly in
code. This is convenient for local development and testing. You can also load a base configuration from environment
variables or a configuration file, and then override specific options in code.

```ts
const connection = await Connection.connect({
    address: <endpoint>,
    tls: true,
    apiKey: <APIKey>,
});
const client = new Client({
    connection,
    namespace: <namespace_id>.<account_id>,
});
```

</TabItem>

</Tabs>

## Connect to Temporal Cloud {/* #connect-to-temporal-cloud */}

You can connect to Temporal Cloud using either an [API key](/cloud/api-keys) or through mTLS. Connection to Temporal
Cloud or any secured Temporal Service requires additional connection options compared to connecting to an unsecured
local development instance:

- Your credentials for authentication.
  - If you are using an API key, provide the API key value.
  - If you are using mTLS, provide the mTLS CA certificate and mTLS private key.
- Your [_Namespace Id_](/cloud/namespaces#temporal-cloud-namespace-id) and _Account Id_ combination, which follows the
  format `<namespace_id>.<account_id>`.
- The recommended _endpoint_ is the gRPC Namespace endpoint: `<namespace>.<account>.tmprl.cloud:7233`. This endpoint
  works for all Namespaces and automatically directs traffic to the active region for Namespaces with
  [High Availability](/cloud/high-availability). See [accessing Namespaces](/cloud/namespaces#access-namespaces) for
  more information on endpoint options.

You can find the Namespace and Account ID, as well as the endpoint, on the Namespaces tab:

![The Namespace and Account ID combination on the left, and the regional endpoint on the right](/img/cloud/apikeys/namespaces-and-regional-endpoints.png)

For more information about managing and generating client certificates for Temporal Cloud, see
[How to manage certificates in Temporal Cloud](/cloud/certificates).

You can provide these connection options using environment variables, a configuration file, or directly in code.

<Tabs groupId="connect-api-key-options" defaultValue="config-file" >

<TabItem value="config-file" label="Configuration File">

You can use a TOML configuration file to set connection options for the Temporal Client. The configuration file lets you
configure multiple profiles, each with its own set of connection options. You can then specify which profile to use when
creating the Temporal Client. For a list of all available configuration options you can set in the TOML file, refer to
[Environment Configuration](/references/client-environment-configuration).

You can use the environment variable `TEMPORAL_CONFIG_FILE` to specify the location of the TOML file or provide the path
to the file directly in code. If you don't provide the path to the configuration file, the SDK looks for it at the
default path `~/.config/temporalio/temporal.toml`.

:::info

The connection options set in configuration files have lower precedence than environment variables. This means that if
you set the same option in both the configuration file and as an environment variable, the environment variable value
overrides the option set in the configuration file.

:::

For example, the following TOML configuration file defines a `staging` profile with the necessary connection options to
connect to Temporal Cloud via an API key:

```toml
