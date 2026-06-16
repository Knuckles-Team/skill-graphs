# Cloud profile for Temporal Cloud
[profile.staging]
address = "your-namespace.a1b2c.tmprl.cloud:7233"
namespace = "your-namespace"
tls_client_cert_data = "your-tls-client-cert-data"
tls_client_key_path = "your-tls-client-key-path"
```

With the connections options defined in the configuration file, use the
[`connect` method](https://python.temporal.io/temporalio.client.Client.html#connect) on the `Client` class to create a
Temporal Client using the `staging` profile as follows. After loading the profile, you can also programmatically
override specific connection options before creating the client.

```python {14,23-25}

from pathlib import Path

from temporalio.client import Client
from temporalio.envconfig import ClientConfig

async def main():
    """
    Demonstrates loading a named profile and overriding values programmatically.
    """
    print("--- Loading 'staging' profile with programmatic overrides ---")

    config_file = Path(__file__).parent / "config.toml"
    profile_name = "staging"

    print(
        "The 'staging' profile in config.toml has an incorrect address (localhost:9999)."
    )
    print("We'll programmatically override it to the correct address.")

    # Load the 'staging' profile.
    connect_config = ClientConfig.load_client_connect_config(
        profile=profile_name,
        config_file=str(config_file),
    )

    # Override the target host to the correct address.
    # This is the recommended way to override configuration values.
    connect_config["target_host"] = "localhost:7233"

    print(f"\nLoaded '{profile_name}' profile from {config_file} with overrides.")
    print(
        f"  Address: {connect_config.get('target_host')} (overridden from localhost:9999)"
    )
    print(f"  Namespace: {connect_config.get('namespace')}")

    print("\nAttempting to connect to client...")
    try:
        await Client.connect(**connect_config)  # type: ignore
        print("✅ Client connected successfully!")
    except Exception as e:
        print(f"❌ Failed to connect: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

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

Ensure these environment variables exist in your environment before running your Python application.

Import the `temporalio.envconfig` package to set connection options for the Temporal Client using environment variables.
The `ClientConfig.load_client_connect_config` function will automatically load all environment variables. For a list of all available
environment variables and their default values, refer to [Environment Configuration](/develop/environment-configuration).

For example, the following code snippet loads all environment variables and creates a Temporal Client with the options
specified in those variables. If you have defined a configuration file at either the default location
(`~/.config/temporalio/temporal.toml`) or a custom location specified by the `TEMPORAL_CONFIG_FILE` environment
variable, this will also load the default profile in the configuration file. However, any options set via environment
variables will take precedence.

After setting the environment variables, use the following code to create the Temporal Client:

```python {11, 19}

from pathlib import Path

from temporalio.client import Client
from temporalio.envconfig import ClientConfig

async def main():
    # load_client_connect_config is a helper that loads a profile and prepares
    # the config dictionary for Client.connect. By default, it loads the
    # "default" profile.
    connect_config = ClientConfig.load_client_connect_config()

    print(f"  Address: {connect_config.get('target_host')}")
    print(f"  Namespace: {connect_config.get('namespace')}")
    print(f"  gRPC Metadata: {connect_config.get('rpc_metadata')}")

    print("\nAttempting to connect to client...")
    try:
        await Client.connect(**connect_config)  # type: ignore
        print("✅ Client connected successfully!")
    except Exception as e:
        print(f"❌ Failed to connect: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

</TabItem>

<TabItem value="code" label="Code">

You can also specify connection options directly in code to connect to Temporal Cloud. To create an initial connection,
provide the endpoint, Namespace and Account ID combination, and API key values to the `Client.connect` method.

```python
client = await Client.connect(
    <endpoint>,
    namespace=<namespace_id>.<account_id>,
    api_key=<APIKey>,
    tls=True,
)
```

To connect using mTLS instead of an API key, provide the mTLS certificate and private key as follows:

    View the source code
  {' '}
  in the context of the rest of the application code.

```python
from temporalio.client import Client, TLSConfig
