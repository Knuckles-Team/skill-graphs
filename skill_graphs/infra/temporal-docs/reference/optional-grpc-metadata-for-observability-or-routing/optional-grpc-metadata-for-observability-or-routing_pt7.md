[`Client`](https://pkg.go.dev/go.temporal.io/sdk/client#Client). The `Dial()` API expects connection options such as the
Temporal Server address, the Namespace to connect to, and Transport Layer Security (TLS) configuration. You can specify
these options in the function call, or specify them using environment variables or a configuration file. We recommend
you use environment variables or a configuration file to manage these connection options securely.

:::info Versioning Requirements

Environment variable and configuration file support were added in Go SDK v1.28.0.

:::

When you are running a Temporal Service locally, such as the
[Temporal CLI](https://docs.temporal.io/cli/command-reference/server#start-dev), the connection options you must provide are minimal.

If you don't provide [`HostPort`](https://pkg.go.dev/go.temporal.io/sdk/internal#ClientOptions), the Client defaults the
address and port number to `127.0.0.1:7233`, which is the port of the development Temporal Service. If you don't set a
custom Namespace name in the Namespace field, the client connects to the default Namespace.

<Tabs groupId="connect-options" defaultValue="env-vars" >

<TabItem value="config-file" label="Configuration File">

You can use a TOML configuration file to set connection options for the Temporal Client. The configuration file lets you
configure multiple profiles, each with its own set of connection options. You can then specify which profile to use when
creating the Temporal Client. You can use the environment variable `TEMPORAL_CONFIG_FILE` to specify the location of the
TOML file or provide the path to the file directly in code. If you don't provide the configuration file path, the SDK
looks for it at the path `~/.config/temporalio/temporal.toml`. For a list of all available configuration options, refer
to [Environment Configuration](/references/client-environment-configuration)

:::info

The connection options set in configuration files have lower precedence than environment variables. This means that if
you set the same option in both the configuration file and as an environment variable, the environment variable value
overrides the option set in the configuration file.

:::

For example, the following TOML configuration file defines two profiles: `default` and `prod`. Each profile has its own
set of connection options.

```toml
