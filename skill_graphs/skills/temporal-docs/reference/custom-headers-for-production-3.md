# Custom headers for production
[profile.prod.grpc_meta]
environment = "production"
service-version = "v1.2.3"
```

You can create a Temporal Client using a specific profile from the configuration file as follows:

```go
package main

	"fmt"
	"log"

	"go.temporal.io/sdk/client"
	"go.temporal.io/sdk/contrib/envconfig"
)

func main() {
	// Load a specific profile from the TOML config file.
	// This requires a [profile.prod] section in your config.
	opts, err := envconfig.LoadClientOptions(envconfig.LoadClientOptionsRequest{
		ConfigFileProfile: "prod",
	})
	if err != nil {
		log.Fatalf("Failed to load 'prod' profile: %v", err)
	}

	c, err := client.Dial(opts)
	if err != nil {
		log.Fatalf("Failed to connect using 'prod' profile: %v", err)
	}
	defer c.Close()

	fmt.Printf("✅ Connected to Temporal namespace %q on %s using 'prod' profile\n", c.Options().Namespace, c.Options().HostPort)
}
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

```go
package main

	"fmt"
	"log"

	"go.temporal.io/sdk/client"
	"go.temporal.io/sdk/contrib/envconfig"
)

func main() {
	// Loads the "default" profile from the standard location and environment variables.
	c, err := client.Dial(envconfig.MustLoadDefaultClientOptions())
	if err != nil {
		log.Fatalf("Failed to create client: %v", err)
	}
	defer c.Close()

	fmt.Printf("✅ Connected to Temporal namespace %q on %s\n", c.Options().Namespace, c.Options().HostPort)
}

```

</TabItem>

<TabItem value="code" label="Code">

If you don't want to use environment variables or a configuration file, you can specify connection options directly in
code. This is convenient for local development and testing. You can also load a base configuration from environment
variables or a configuration file, and then override specific options in code.

{/* SNIPSTART samples-apps-go-yourapp-gateway {"selectedLines": ["1-23", "32"]} */}
[sample-apps/go/yourapp/gateway/main.go](https://github.com/temporalio/documentation/blob/main/sample-apps/go/yourapp/gateway/main.go)
```go
package main

	"context"
	"encoding/json"
	"log"
	"net/http"

	"documentation-samples-go/yourapp"

	"go.temporal.io/sdk/client"
)

func main() {
	// Create a Temporal Client to communicate with the Temporal Cluster.
	// A Temporal Client is a heavyweight object that should be created just once per process.
	temporalClient, err := client.Dial(client.Options{
		HostPort: client.DefaultHostPort,
	})
	if err != nil {
		log.Fatalln("Unable to create Temporal Client", err)
	}
	defer temporalClient.Close()
// ...
}
```
{/* SNIPEND */}

</TabItem>

</Tabs>

## Connect to Temporal Cloud {/* #connect-to-temporal-cloud */}

You can connect to Temporal Cloud using either an [API key](/cloud/api-keys) or through mTLS. Connection to Temporal
Cloud or any secured Temporal Service requires additional connection options compared to connecting to an unsecured
local development instance:

- Your credentials for authentication.
  - If you are using an API key, provide the API key value.
  - If you are using mTLS, provide the mTLS CA certificate and mTLS private key.
- Your _Namespace and Account ID_ combination, which follows the format `<namespace_id>.<account_id>`.
- The recommended _endpoint_ is the gRPC Namespace endpoint: `<namespace>.<account>.tmprl.cloud:7233`.
  This endpoint works for all Namespaces and automatically directs traffic to the active region for Namespaces with [High Availability](/cloud/high-availability).
  See [accessing Namespaces](/cloud/namespaces#access-namespaces) for more information on endpoint options.

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

For example, the following TOML configuration file defines a `cloud` profile with the necessary connection options to
connect to Temporal Cloud via an API key:

```toml
