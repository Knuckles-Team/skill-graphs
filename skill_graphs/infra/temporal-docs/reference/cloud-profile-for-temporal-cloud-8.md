# Cloud profile for Temporal Cloud
[profile.staging]
address = "your-namespace.a1b2c.tmprl.cloud:7233"
namespace = "your-namespace"
tls_client_cert_data = "your-tls-client-cert-data"
tls_client_key_path = "your-tls-client-key-path"
```

With the connections options defined in the configuration file, use the `loadClientConnectConfig` helper from
`@temporalio/envconfig` to load the `staging` profile from the configuration file. You can then pass the resulting
configuration to the `Connection.connect` method. After that, you then pass the `connection` object and the Namespace to
the `Client` constructor to create a Temporal Client using the `staging` profile as follows. After loading the profile,
you can also programmatically override specific connection options before creating the client.

{/* SNIPSTART typescript-env-config-load-profile-with-overrides {"highlightedLines": "15-18,30-31"} */}
[env-config/src/load-profile.ts](https://github.com/temporalio/samples-typescript/blob/main/env-config/src/load-profile.ts)
```ts {15-18,30-31}

async function main() {
  console.log("--- Loading 'staging' profile with programmatic overrides ---");

  const configFile = resolve(__dirname, '../config.toml');
  const profileName = 'staging';

  // The 'staging' profile in config.toml has an incorrect address (localhost:9999)
  // We'll programmatically override it to the correct address

  // Load the 'staging' profile.
  const config = loadClientConnectConfig({
    profile: profileName,
    configSource: { path: configFile },
  });

  // Override the target host to the correct address.
  // This is the recommended way to override configuration values.
  config.connectionOptions.address = 'localhost:7233';

  console.log(`\nLoaded '${profileName}' profile from ${configFile} with overrides.`);
  console.log(`  Address: ${config.connectionOptions.address} (overridden from localhost:9999)`);
  console.log(`  Namespace: ${config.namespace}`);

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

The following environment variables are required to connect to Temporal Cloud:

- `TEMPORAL_NAMESPACE`: Your Namespace and Account ID combination in the format `<namespace_id>.<account_id>`.
- `TEMPORAL_ADDRESS`: The gRPC endpoint for your Temporal Cloud Namespace.
- `TEMPORAL_API_KEY`: Your API key value. Required if you are using API key authentication.
- `TEMPORAL_TLS_CLIENT_CERT_DATA` or `TEMPORAL_TLS_CLIENT_CERT_PATH`: Your mTLS client certificate data or file path.
  Required if you are using mTLS authentication.
- `TEMPORAL_TLS_CLIENT_KEY_DATA` or `TEMPORAL_TLS_CLIENT_KEY_PATH`: Your mTLS client private key data or file path.
  Required if you are using mTLS authentication.

Ensure these environment variables exist in your environment before running your application.

Import the `@temporalio/envconfig` package to set connection options for the Temporal Client using environment
variables. The `loadClientConnectConfig` function will automatically load all environment variables. For a list of all
available environment variables and their default values, refer to
[Environment Configuration](/references/client-environment-configuration).

For example, the following code snippet loads all environment variables and creates a Temporal Client with the options
specified in those variables. If you have defined a configuration file at either the default location
(`~/.config/temporalio/temporal.toml`) or a custom location specified by the `TEMPORAL_CONFIG_FILE` environment
variable, this will also load the default profile in the configuration file. However, any options set via environment
variables will take precedence.

{/* SNIPSTART typescript-env-config-load-default-profile {"highlightedLines": "17-19,28-29", "selectedLines": ["1-5","17","19","22-40"]} */}
[env-config/src/load-from-file.ts](https://github.com/temporalio/samples-typescript/blob/main/env-config/src/load-from-file.ts)
```ts {17-19,28-29}

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

You can also provide connections options in your code directly. To create an initial connection, provide the Namespace
and API key values to the `Connection.connect` method.

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

To update an API key, use the `setApiKey` method on the Connection object:

```ts
connection.setApiKey(<APIKey>);
```

</TabItem>

</Tabs>

## Connect to Temporal Service from a Worker {/* #connect-to-temporal-service-from-a-worker */}

Connecting to Temporal Service from a Worker requires the same set of connections options as connecting from a Temporal
Application or from within an Activity, but the connection type is different. When connecting from a Worker, you create
a `NativeConnection` object instead of a `Connection` object. The
[`NativeConnection` class](https://typescript.temporal.io/api/classes/worker.NativeConnection) is imported from
`@temporalio/worker` instead of `@temporalio/client`. After you create the `NativeConnection` object, you pass it to
`Worker.create()` when creating the Worker.

To provide connection options to the `NativeConnection`, you can use environment variables, a configuration file, or
directly in code. The following code snippets show how to create a `NativeConnection` object using each method. Refer to
[Connect to a local development Temporal Service](#connect-to-development-service) and
[Connect to Temporal Cloud](#connect-to-temporal-cloud) for details on how to provide connection options using each
method.

<Tabs groupId="worker-connect-options" defaultValue="config-file" >

<TabItem value="config-file" label="Configuration File">

Ensure you have a TOML configuration file with the necessary connection options defined. For example, the following TOML
configuration file defines a `staging` profile with the necessary connection options to connect to Temporal Cloud via an
API key:

```toml
