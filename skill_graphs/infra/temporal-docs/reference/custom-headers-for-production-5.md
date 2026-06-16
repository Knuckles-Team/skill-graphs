# Custom headers for production
[profile.prod.grpc_meta]
environment     = "production"
service-version = "v1.2.3"
```

You can create a Temporal Client using a profile from the configuration file using the
`ClientConfig.load_client_connect_config` function as follows. In this example, you load the `default` profile for local
development:

```python {23-25}

from pathlib import Path

from temporalio.client import Client
from temporalio.envconfig import ClientConfig

async def main():
    """
    Loads the default profile from the config.toml file in this directory.
    """
    print("--- Loading default profile from config.toml ---")

    # For this sample to be self-contained, we explicitly provide the path to
    # the config.toml file included in this directory.
    # By default though, the config.toml file will be loaded from
    # ~/.config/temporalio/temporal.toml (or the equivalent standard config directory on your OS).
    config_file = Path(__file__).parent / "config.toml"

    # load_client_connect_config is a helper that loads a profile and prepares
    # the config dictionary for Client.connect. By default, it loads the
    # "default" profile.
    connect_config = ClientConfig.load_client_connect_config(
        config_file=str(config_file)
    )

    print(f"Loaded 'default' profile from {config_file}.")
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

<TabItem value="env-vars" label="Environment Variables">

Use the `envconfig` package to set connection options for the Temporal Client using environment variables. For a list of
all available environment variables and their default values, refer to
[Environment Configuration](/references/client-environment-configuration).

For example, the following code snippet loads all environment variables and creates a Temporal Client with the options
specified in those variables. If you have defined a configuration file at either the default location
(`~/.config/temporalio/temporal.toml`) or a custom location specified by the `TEMPORAL_CONFIG_FILE` environment
variable, this will also load the default profile in the configuration file. However, any options set via environment
variables will take precedence.

Set the following environment variables before running your Python application. Replace the placeholder values with your
actual configuration. Since this is for a local development Temporal Service, the values connect to `localhost:7233` and
the `default` Namespace. You may omit these variables entirely since they're the defaults.

```bash
export TEMPORAL_NAMESPACE="default"
export TEMPORAL_ADDRESS="localhost:7233"
```

After setting the environment variables, you can create a Temporal Client as follows:

```python {11,19}

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

If you don't want to use environment variables or a configuration file, you can specify connection options directly in
code. This is convenient for local development and testing. You can also load a base configuration from environment
variables or a configuration file, and then override specific options in code.

Use the `connect()` method on the `Client` class to create and connect to a Temporal Client to the Temporal Service.

    View the source code
  {' '}
  in the context of the rest of the application code.

```python
