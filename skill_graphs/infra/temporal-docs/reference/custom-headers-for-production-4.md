# Custom headers for production
[profile.prod.grpc_meta]
environment = "production"
service-version = "v1.2.3"
```

You can create a Temporal Client using a specific profile from the configuration file as follows. First use
`ClientConfigProfile.load` to load the profile from the configuration file. Then use
`profile.toWorkflowServiceStubsOptions` and `profile.toWorkflowClientOptions` to convert the profile to
`WorkflowServiceStubsOptions` and `WorkflowClientOptions` respectively. Then use `WorkflowClient.newInstance` to create
a Temporal Client.

```java {21-25,32-34}

public class LoadFromFile {

  private static final Logger logger = LoggerFactory.getLogger(LoadFromFile.class);

  public static void main(String[] args) {
    try {

      String configFilePath =
          Paths.get(LoadFromFile.class.getResource("/config.toml").toURI()).toString();

      ClientConfigProfile profile =
          ClientConfigProfile.load(
              LoadClientConfigProfileOptions.newBuilder()
                  .setConfigFilePath(configFilePath)
                  .build());

      WorkflowServiceStubsOptions serviceStubsOptions = profile.toWorkflowServiceStubsOptions();
      WorkflowClientOptions clientOptions = profile.toWorkflowClientOptions();

      try {
        // Create the workflow client using the loaded configuration
        WorkflowClient client =
            WorkflowClient.newInstance(
                WorkflowServiceStubs.newServiceStubs(serviceStubsOptions), clientOptions);

        // Test the connection by getting system info
        var systemInfo =
            client
                .getWorkflowServiceStubs()
                .blockingStub()
                .getSystemInfo(
                    io.temporal.api.workflowservice.v1.GetSystemInfoRequest.getDefaultInstance());

        logger.info("✅ Client connected successfully!");
        logger.info("   Server version: {}", systemInfo.getServerVersion());

      } catch (Exception e) {
        logger.error("❌ Failed to connect: {}", e.getMessage());
      }

    } catch (Exception e) {
      logger.error("Failed to load configuration: {}", e.getMessage(), e);
      System.exit(1);
    }
  }
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

```java {18-19,26-28}

public class LoadFromFile {

  private static final Logger logger = LoggerFactory.getLogger(LoadFromFile.class);

  public static void main(String[] args) {
    try {

      ClientConfigProfile profile =
          ClientConfigProfile.load(LoadClientConfigProfileOptions.newBuilder().build());

      WorkflowServiceStubsOptions serviceStubsOptions = profile.toWorkflowServiceStubsOptions();
      WorkflowClientOptions clientOptions = profile.toWorkflowClientOptions();

      try {
        // Create the workflow client using the loaded configuration
        WorkflowClient client =
            WorkflowClient.newInstance(
                WorkflowServiceStubs.newServiceStubs(serviceStubsOptions), clientOptions);

        // Test the connection by getting system info
        var systemInfo =
            client
                .getWorkflowServiceStubs()
                .blockingStub()
                .getSystemInfo(
                    io.temporal.api.workflowservice.v1.GetSystemInfoRequest.getDefaultInstance());

        logger.info("✅ Client connected successfully!");
        logger.info("   Server version: {}", systemInfo.getServerVersion());

      } catch (Exception e) {
        logger.error("❌ Failed to connect: {}", e.getMessage());
      }

    } catch (Exception e) {
      logger.error("Failed to load configuration: {}", e.getMessage(), e);
      System.exit(1);
    }
  }
}
```

</TabItem>

<TabItem value="code" label="Code">

If you don't want to use environment variables or a configuration file, you can specify connection options directly in
code. This is convenient for local development and testing. You can also load a base configuration from environment
variables or a configuration file, and then override specific options in code.

<!--SNIPSTART javasdk-build-caller-app-using-local-client-custom-namespace {"selectedLines": ["23-31"]}-->
[sample-apps/java/client/devserver-namespace-client-sample/src/main/java/clientsample/YourCallerApp.java](https://github.com/temporalio/documentation/blob/main/sample-apps/java/client/devserver-namespace-client-sample/src/main/java/clientsample/YourCallerApp.java)
```java
// ...
        // Add the Namespace as a Client Option
        WorkflowClientOptions clientOptions = WorkflowClientOptions
            .newBuilder()
            .setNamespace(namespace)
            .build();

        // Initialize the Temporal Client
        // This application uses the Client to communicate with the Temporal Service
        WorkflowClient client = WorkflowClient.newInstance(service, clientOptions);
```
<!--SNIPEND-->

</TabItem>
</Tabs>

## Connect to Temporal Cloud {/* #connect-to-temporal-cloud */}

You can connect to Temporal Cloud using either an [API key](/cloud/api-keys) or through [mTLS](/cloud/certificates).
Connection to Temporal Cloud or any secured Temporal Service requires additional connection options compared to
connecting to an unsecured local development instance:

- Your credentials for authentication.
  - If you are using an API key, provide the API key value.
  - If you are using mTLS, provide the mTLS CA certificate and mTLS private key.
- Your _Namespace and Account ID_ combination, which follows the format `<namespace_id>.<account_id>`.
- The recommended _endpoint_ is the gRPC Namespace endpoint: `<namespace>.<account>.tmprl.cloud:7233`.
  This endpoint works for all Namespaces and automatically directs traffic to the active region for Namespaces with [High Availability](/cloud/high-availability).
  See [accessing Namespaces](/cloud/namespaces#access-namespaces) for more information on endpoint options.

You can find the Namespace and Account ID, as well as the endpoint, on the Namespaces tab:

![The Namespace and Account ID combination on the left, and the regional endpoint on the right](/img/cloud/apikeys/namespaces-and-regional-endpoints.png)

You can provide these connection options using environment variables, a configuration file, or directly in code.

<Tabs groupId="connect-options" defaultValue="config-file" >

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
