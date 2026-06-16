Use the `clientCAFiles`/ `clientCAData` and `requireClientAuth` properties in both the `internode` and `frontend` sections of the [mTLS configuration](/references/configuration#tls).

### Users

To restrict access to specific users, authentication and authorization is performed through extensibility points and plugins as described in the [Authorization](#authorization) section below.

#### Authorization

:::note
Information regarding [`Authorizer`](#authorizer-plugin) and [`ClaimMapper`](#claim-mapper) has been moved to another location.
:::

Temporal offers two plugin interfaces for implementing API call authorization:

- [`ClaimMapper`](#claim-mapper)
- [`Authorizer`](#authorizer-plugin)

The authorization and claim mapping logic is customizable, making it available to a variety of use cases and identity schemes.
When these are provided the frontend invokes the implementation of these interfaces before executing the requested operation.

See https://github.com/temporalio/samples-server/blob/main/extensibility/authorizer for a sample implementation.

<CaptionedImage
    src="/diagrams/frontend-authorization-order-of-operations.png"
    title="Front-end authorization order of operations"
/>

### Single sign-on integration

Temporal can be integrated with a single sign-on (SSO) experience by using the `ClaimMapper` and `Authorizer` plugins.
The default JWT `ClaimMapper` implementation can be used as is or as a base for a custom implementation of a similar plugin.

### Temporal UI

To enable SSO authentication in the Temporal UI using environment credentials, you need to configure the UI container with specific environment variables that define your identity provider and OAuth settings.
In your docker-compose.yaml, set `TEMPORAL_AUTH_ENABLED=true` to activate authentication.
Next, specify the required OAuth credentials and endpoints using environment variables such as:

- `TEMPORAL_AUTH_CLIENT_ID`
- `TEMPORAL_AUTH_CLIENT_SECRET`
- `TEMPORAL_AUTH_PROVIDER_URL`
- `TEMPORAL_AUTH_CALLBACK_URL`

These values correspond to the client credentials and endpoints provided by your OAuth identity provider (such as Google, Auth0, Okta).
When properly configured, Temporal UI will redirect users to your SSO login page and enforce authentication on access.
This approach does not require any additional configuration files, making it ideal for containerized environments using secure environment variable injection.

```yaml
temporal-ui:
  container_name: temporal-ui
  depends_on:
    - temporal
  environment:
    - TEMPORAL_GRPC_ENDPOINT=temporal:7233
    - TEMPORAL_ADDRESS=temporal:7233
    - TEMPORAL_AUTH_ENABLED=true
    - TEMPORAL_AUTH_PROVIDER_URL=https://example.com
    - TEMPORAL_AUTH_CLIENT_ID=xxxxxxxxxxxxxx
    - TEMPORAL_AUTH_CLIENT_SECRET=xxxxxxxxxxxxxx
    - TEMPORAL_AUTH_CALLBACK_URL=https://your-domain/auth/sso/callback
    - TEMPORAL_AUTH_SCOPES=openid profile email
  image: temporalio/ui:latest
  networks:
    - temporal-network
  ports:
    - 8080:8080
```

For more general guidance for configuration, refer to the [Temporal UI README](https://github.com/temporalio/ui?tab=readme-ov-file#configuration).
For more details on configuration with Docker, refer to [Temporal UI Config](https://github.com/temporalio/ui/blob/c95265ee6431fd0f6cf78ae06373885d66a8ee0c/server/docker/config-template.yaml).

## Temporal Service plugins {/* #plugins */}

The Temporal Service supports some pluggable components.

### What is a ClaimMapper Plugin? {/* #claim-mapper */}

The Claim Mapper component is a pluggable component that extracts Claims from JSON Web Tokens (JWTs).

This process is achieved with the method `GetClaims`, which translates `AuthInfo` structs from the caller into `Claims` about the caller's roles within Temporal.

A `Role` (within Temporal) is a bit mask that combines one or more of the role constants.
In the following example, the role is assigned constants that allow the caller to read and write information.

```go
role := authorization.RoleReader | authorization.RoleWriter
```

`GetClaims` is customizable and can be modified with the `temporal.WithClaimMapper` server option.
Temporal also offers a default JWT `ClaimMapper` for your use.

A typical approach is for `ClaimMapper` to interpret custom `Claims` from a caller's JWT, such as membership in groups, and map them to Temporal roles for the user.
The subject information from the caller's mTLS certificate can also be a parameter in determining roles.

#### `AuthInfo`

`AuthInfo` is a struct that is passed to `GetClaims`. `AuthInfo` contains an authorization token extracted from the `authorization` header of the gRPC request.

`AuthInfo` includes a pointer to the `pkix.Name` struct.
This struct contains an [x.509](https://www.ibm.com/docs/en/ibm-mq/7.5?topic=certificates-distinguished-names) Distinguished Name from the caller's mTLS certificate.

#### `Claims`

`Claims` is a struct that contains information about permission claims granted to the caller.

`Authorizer` assumes that the caller has been properly authenticated, and trusts the `Claims` when making an authorization decision.

#### Default JWT ClaimMapper

Temporal offers a default JWT `ClaimMapper` that extracts the information needed to form Temporal `Claims`.
This plugin requires a public key to validate digital signatures.

To get an instance of the default JWT `ClaimMapper`, call `NewDefaultJWTClaimMapper` and provide it with the following:

- a `TokenKeyProvider` instance
- a `config.Authorization` pointer
- a logger

The code for the default `ClaimMapper` can also be used to build a custom `ClaimMapper`.

#### Token key provider

A `TokenKeyProvider` obtains public keys from specified issuers' URIs that adhere to a specific format.
The default JWT `ClaimMapper` uses this component to obtain and refresh public keys over time.

Temporal provides a `defaultTokenKeyProvider`.
This component dynamically obtains public keys that follow the [JWKS format](https://tools.ietf.org/html/rfc7517).
It supports formats such as `RSA` and `ECDSA`.

```go
provider := authorization.NewDefaultTokenKeyProvider(cfg, logger)
```

:::note

`KeySourceURIs` are the HTTP endpoints that return public keys of token issuers in the [JWKS format](https://tools.ietf.org/html/rfc7517).
`RefreshInterval` defines how frequently keys should be refreshed.
For example, [Auth0](https://auth0.com/) exposes endpoints such as `https://YOUR_DOMAIN/.well-known/jwks.json`.

:::

By default, "permissions" is used to name the `permissionsClaimName` value.

Configure the plugin with `config.Config.Global.Authorization.JWTKeyProvider`.

#### JSON Web Token format

The default JWT `ClaimMapper` expects authorization tokens to be formatted as follows:

```
Bearer <token>
```

The Permissions Claim in the JWT Token is expected to be a collection of Individual Permission Claims.
Each Individual Permission Claim must be formatted as follows:

```
<namespace> : <permission>
```

These permissions are then converted into Temporal roles for the caller.
This can be one of Temporal's four values:

- read
- write
- worker
- admin

Multiple permissions for the same Namespace are overridden by the `ClaimMapper`.

##### Example of a payload for the default JWT ClaimMapper

```
{
   "permissions":[
      "temporal-system:read",
      "namespace1:write"
   ],
   "aud":[
      "audience"
   ],
   "exp":1630295722,
   "iss":"Issuer"
}
```

### What is an Authorizer Plugin? {/* #authorizer-plugin */}

The `Authorizer` plugin contains a single `Authorize` method, which is invoked for each incoming API call.
`Authorize` receives information about the API call, along with the role and permission claims of the caller.

`Authorizer` allows for a wide range of authorization logic, including call target, role/permissions claims, and other data available to the system.

#### Configuration

The following arguments must be passed to `Authorizer`:

- `context.Context`: General context of the call.
- `authorization.Claims`: Claims about the roles assigned to the caller. Its intended use is described in the [`Claims`](#claims) section earlier on this page.
- `authorization.CallTarget`: Target of the API call.

`Authorizer` then returns one of two decisions:

- `DecisionDeny`: the requested API call is not invoked and an error is returned to the caller.
- `DecisionAllow`: the requested API call is invoked.

:::warning Security Warning

If you do **not** explicitly configure an `Authorizer`, Temporal uses the default `noopAuthorizer`. This default allows **every** API request,
with no authentication or access control. Anyone who can reach your Temporal Server can invoke any API, including sensitive administrative operations.
This is **not secure** for production or for any environment that is accessible to untrusted clients (such as over the internet).

**To protect your Temporal Server, you must configure an `Authorizer` plugin with a corresponding `ClaimMapper`.** Without this, your deployment is
effectively open to anyone with network access.

:::

Configure your `Authorizer` with the [`temporal.WithAuthorizer`](/references/server-options#withauthorizer) server option, and your `ClaimMapper` with
the [`temporal.WithClaimMapper`](/references/server-options#withclaimmapper) server option.

```go
temporalServer, err := temporal.NewServer(
	temporal.WithAuthorizer(newCustomAuthorizer()),
	temporal.WithClaimMapper(func(cfg *config.Config) authorization.ClaimMapper {
		return newCustomClaimMapper(cfg)
	}),
)
```

#### How to authorize SDK API calls {/* #authorize-api-calls */}

When authentication is enabled, you can authorize API calls made to the Frontend Service.

The Temporal Server [expects](#authentication) an `authorization` gRPC header with an authorization token to be passed with API calls if [requests authorization](#authorization) is configured.

Authorization Tokens may be provided to the Temporal Java SDK by implementing a `io.temporal.authorization.AuthorizationTokenSupplier` interface.
The implementation should be used to create `io.temporal.authorization.AuthorizationGrpcMetadataProvider` that may be configured on ServiceStub gRPC interceptors list.

The implementation is called for each SDK gRPC request and may supply dynamic tokens.

**JWT**

One of the token types that may be passed this way are JWT tokens.
Temporal Server provides a [default implementation of JWT authentication](#default-jwt-claimmapper).

**Example**

```java
AuthorizationTokenSupplier tokenSupplier =
  //your implementation of token supplier
  () -> "Bearer <Base64 url-encoded value of the token for default JWT ClaimMapper>";
WorkflowServiceStubsOptions serviceStubOptions =
  WorkflowServiceStubsOptions.newBuilder()
    //other service stub options
    .addGrpcMetadataProvider(new AuthorizationGrpcMetadataProvider(tokenSupplier))
    .build();
WorkflowServiceStubs service = WorkflowServiceStubs.newServiceStubs(serviceStubOptions);
WorkflowClient client = WorkflowClient.newInstance(service);
```

Related read:

- [How to secure a Temporal Service](/security)

## Data Converter {/* #data-converter */}

Each Temporal SDK provides a [Data Converter](/dataconversion) that can be customized with a custom [Payload Codec](/payload-codec) to encode and secure your data.

For details on what data can be encoded, how to secure it, and what to consider when using encryption, see [Data encryption](/production-deployment/data-encryption).

#### Codec Server

You can use a [Codec Server](/codec-server) with your custom Payload Codec to decode the data you see on your Web UI and CLI locally through remote endpoints.
However, ensure that you consider all security implications of [remote data encoding](/remote-data-encoding) before using a Codec Server.

For details on how to set up a Codec Server, see [Codec Server setup](/production-deployment/data-encryption#codec-server-setup).

## Configuration Options for Restricting and Securing Access

Temporal provides extensive configuration options to limit and control which callers can access your services and how those services behave in different environments. These options help you enforce stricter security boundaries in self-hosted deployments and tune behavior for production use cases. For more details on available settings and how to configure them, see the following references:

- [Cluster & Server configuration](/references/configuration) — Static configuration settings for servers and services.

- [Dynamic configuration](/references/dynamic-configuration) — Runtime-updatable settings for tuning and behavior control.

- [Client environment configuration](/references/client-environment-configuration) — Environment variable settings for configuring Temporal clients.

---

## Temporal Platform security

Find security information for your Temporal deployment, whether you're using Temporal Cloud or self-hosting.

<PatternCards items={[
  {
    href: "https://trust.temporal.io",
    title: "Company Security",
    description: "Learn about Temporal Technologies' general security practices, compliance certifications, and organizational security measures.",
    external: true,
  },
  {
    href: "/cloud/security",
    title: "Temporal Cloud Security",
    description: "Explore the security features of our SaaS offering, including mTLS, end-to-end encryption, and enterprise compliance.",
  },
  {
    href: "/self-hosted-guide/security",
    title: "Self-Hosted Security",
    description: "Discover how to deploy and secure your own Temporal Platform infrastructure with production-ready best practices.",
  },
  {
    href: "https://temporal.io/pages/cloud-security-white-paper",
    title: "Temporal Cloud Security Whitepaper",
    description: "Learn how Temporal Cloud provides provable security by design - orchestrating encrypted workflows without ever accessing your sensitive data.",
    external: true,
  },
]} />

---

## Temporal Web UI configuration reference

The Temporal Web UI Server uses a configuration file for many of the UI's settings.

An example development.yaml file can be found in the [temporalio/ui-server repo](https://github.com/temporalio/ui-server/blob/main/config/development.yaml).

Multiple configuration files can be created for configuring specific areas of the UI, such as Auth or TLS.

## auth

Configures authorization for the Temporal Server.
Settings apply when Auth is enabled.

```yaml
auth:
  enabled: true
  providers:
    label: sso # for internal use; in future may expose as button text
    type: oidc
    providerUrl: https://accounts.google.com
    issuerUrl:
    clientId: xxxxx-xxxx.apps.googleusercontent.com
    clientSecret: xxxxxxxxxxxxxxxxxxxx
    callbackUrl: https://xxxx.com:8080/auth/sso/callback
    scopes:
      - openid
      - profile
      - email
```

## batchActionsDisabled

Prevents the execution of Batch actions.

```yaml
batchActionsDisabled: false
```

## cloudUi

Enables the Cloud UI.

```yaml
cloudUi: false
```

## codec

Codec Server configuration.

```yaml
codec:
  endpoint: http://your-codec-server-endpoint
  passAccessToken: false
  includeCredentials: false
  decodeEventHistoryDownload: false
```

## cors

The name of the `cors` field stands for Cross-Origin Resource Sharing.
Use this field to provide a list of domains that are authorized to access the UI Server APIs.

```yaml
cors:
  cookieInsecure: false
  allowOrigins:
    - http://localhost:3000 # used at development by https://github.com/temporalio/ui
```

## defaultNamespace

The default Namespace that the UI loads data for.
Defaults to `default`.

```yaml
defaultNamespace: default
```

## disableWriteActions

Prevents the user from executing Workflow Actions on the Web UI.

This option affects Bulk Actions for Recent Workflows as well as Workflow Actions on the Workflow Details page.

```yaml
disableWriteActions: false
```

:::note
`disableWriteActions` overrides the configuration values of each individual Workflow Action.
Setting this variable to `true` disables all Workflow Actions on the Web UI.
:::

## enableUi

Enables the browser UI.
This configuration can be set dynamically with the [TEMPORAL_UI_ENABLED](/references/web-ui-environment-variables#temporal_ui_enabled) environment variable.
If disabled—that is, set to `false`—the UI server APIs remain available.

```yaml
enableUi: true
```

## feedbackUrl

The URL to direct users to when they click on the Feedback button in the UI.
If not specified, it defaults to the UI's GitHub Issue page.

```yaml
feedbackUrl: https://github.com/temporalio/ui/issues/new/choose
```

## forwardHeaders

Configures headers for forwarding.

```yaml
forwardHeaders:
  -
```

## hideLogs

If enabled, disables any server logs from being printed to the console.

```yaml
hideLogs: true
```

## hideWorkflowQueryErrors

Hides any errors resulting from a Query to the Workflow.

```yaml
hideWorkflowQueryErrors: false
```

## notifyOnNewVersion

When enabled—that is, when set to `true`—a notification appears in the UI when a newer version of the [Temporal Server](/temporal-service/temporal-server) is available.

```yaml
notifyOnNewVersion: true
```

## port

The port used by the Temporal Web UI Server and any APIs.

```yaml
port: 8080
```

## publicPath

The path used by the Temporal Web UI Server and any APIs.

```yaml
publicPath: ''
```

## refreshInterval

How often the configuration UI Server reads the configuration file for new values.
Currently, only [tls](#tls) configuration values are propagated during a refresh.

```yaml
refreshInterval: 1m
```

## showTemporalSystemNamespace

When enabled—that is, when set to `true`—the Temporal System Namespace becomes visible in the UI.
The Temporal System Namespace lists Workflow Executions used by the Temporal Platform.

```yaml
showTemporalSystemNamespace: false
```

## temporalGrpcAddress

The frontend address for the Temporal Cluster.

The default address is localhost (127.0.0.1:7233).

```yaml
temporalGrpcAddress: default
```

## tls

Transport Layer Security (TLS) configuration for the Temporal Server.
Settings apply when TLS is enabled.

```yaml
tls:
  caFile: ../ca.cert
  certFile: ../cluster.pem
  keyFile: ../cluster.key
  caData:
  certData:
  keyData:
  enableHostVerification: true
  serverName: tls-server
```

## workflowCancelDisabled

Prevents the user from canceling Workflow Executions from the Web UI.

```yaml
workflowCancelDisabled: false
```

## workflowResetDisabled

Prevents the user from resetting Workflows from the Web UI.

```yaml
workflowResetDisabled: false
```

## workflowSignalDisabled

Prevents the user from signaling Workflow Executions from the Web UI.

```yaml
workflowSignalDisabled: false
```

## workflowTerminateDisabled

Prevents the user from terminating Workflow Executions from the Web UI.

```yaml
workflowTerminateDisabled: false
```

---

## Temporal Web UI environment variables reference

You can use environment variables to dynamically alter the configuration of your Temporal Web UI.

These can be used in many environments, such as with Docker. For example:

```
docker run\
-e TEMPORAL_ADDRESS=127.0.0.1:7233\
-e TEMPORAL_UI_PORT=8080\
-e TEMPORAL_UI_PUBLIC_PATH=path/to/webui\
-e TEMPORAL_UI_ENABLED=true\
-e TEMPORAL_CLOUD_UI=false\
-e TEMPORAL_DEFAULT_NAMESPACE=default\
-e TEMPORAL_FEEDBACK_URL=https://feedback.here\
-e TEMPORAL_CONFIG_REFRESH_INTERVAL=0s\
-e TEMPORAL_SHOW_TEMPORAL_SYSTEM_NAMESPACE=false\
-e TEMPORAL_DISABLE_WRITE_ACTIONS=false\
-e TEMPORAL_AUTH_ENABLED=true\
-e TEMPORAL_AUTH_TYPE=oidc\
-e TEMPORAL_AUTH_PROVIDER_URL=https://accounts.google.com\
-e TEMPORAL_AUTH_ISSUER_URL=https://accounts.google.com\
-e TEMPORAL_AUTH_CLIENT_ID=xxxxx-xxxx.apps.googleusercontent.com\
-e TEMPORAL_AUTH_CLIENT_SECRET=xxxxxxxxxxxxxxx\
-e TEMPORAL_AUTH_CALLBACK_URL=https://xxxx.com:8080/auth/sso/callback\
-e TEMPORAL_AUTH_SCOPES=openid,email,profile\
-e TEMPORAL_TLS_CA=../ca.cert\
-e TEMPORAL_TLS_CERT=../cluster.pem\
-e TEMPORAL_TLS_KEY=../cluster.key\
-e TEMPORAL_TLS_ENABLE_HOST_VERIFICATION=true\
-e TEMPORAL_TLS_SERVER_NAME=tls-server\
-e TEMPORAL_CODEC_ENDPOINT=https://codec.server\
-e TEMPORAL_CODEC_PASS_ACCESS_TOKEN=false\
-e TEMPORAL_CODEC_INCLUDE_CREDENTIALS=false\
-e TEMPORAL_HIDE_LOGS=false\
temporalio/ui:<tag>
```

The environment variables are defined in the
[UI server configuration template file](https://github.com/temporalio/ui-server/blob/main/config/docker.yaml) and
described in more detail below.

## `TEMPORAL_ADDRESS`

The [Frontend Service](/temporal-service/temporal-server#frontend-service) address for the Temporal Cluster. This
variable can be set [in the base configuration file](/references/web-ui-configuration#temporalgrpcaddress) using
`temporalGrpcAddress`.

This variable is required for setting other environment variables.

## `TEMPORAL_UI_PORT`

The port used by the Temporal WebUI Server and the HTTP API.

This variable is needed for `TEMPORAL_OPENAPI_ENABLED` and all auth-related settings to work properly.

## `TEMPORAL_UI_PUBLIC_PATH`

Stores a value such as "" or "/custom-path" that allows the UI to be served from a subpath.

## `TEMPORAL_UI_ENABLED`

Enables or disables the [browser UI](/references/web-ui-configuration#enableui) for the Temporal Cluster.

Enabling the browser UI allows the Server to be accessed from your web browser. If disabled, the server cannot be viewed
on the web, but the UI server APIs remain available for use.

## `TEMPORAL_CLOUD_UI`

If enabled, use the alternate UI from Temporal Cloud.

## `TEMPORAL_DEFAULT_NAMESPACE`

The default [Namespace](/namespaces) that the Web UI opens first.

## `TEMPORAL_FEEDBACK_URL`

The URL that users are directed to when they click the Feedback button in the UI.

If not specified, this variable defaults to the UI's GitHub Issue page.

## `TEMPORAL_CONFIG_REFRESH_INTERVAL`

Determines how often the UI Server reads the configuration file for new values.

## `TEMPORAL_SHOW_TEMPORAL_SYSTEM_NAMESPACE`

If enabled, shows the System Namespace that handles internal Temporal Workflows in the Web UI.

## `TEMPORAL_DISABLE_WRITE_ACTIONS`

Disables any button in the UI that allows the user to modify Workflows or Activities.

## `TEMPORAL_AUTH_ENABLED`

Enables or disables Web UI authentication and authorization methods.

When enabled, the Web UI will use the provider information in the
[UI configuration file](/references/web-ui-configuration#auth) to verify the identity of users.

All auth-related variables can be defined when `TEMPORAL_AUTH_ENABLED` is set to "true". Disabling the variable will
retain given values.

## `TEMPORAL_AUTH_TYPE`

Specifies the type of authentication. Defaults to `oidc`.

## `TEMPORAL_AUTH_PROVIDER_URL`

The .well-known IDP discovery URL for authentication and authorization.

This can be set as in the UI server configuration with [auth](/references/web-ui-configuration#auth).

## `TEMPORAL_AUTH_ISSUER_URL`

The URL for the authentication or authorization issuer.

This value is only needed when the issuer differs from the auth provider URL.

## `TEMPORAL_AUTH_CLIENT_ID`

The client ID used for authentication or authorization.

This value is a required parameter.

## `TEMPORAL_AUTH_CLIENT_SECRET`

The client secret used for authentication and authorization.

Client Secrets are used by the oAuth Client for authentication.

## `TEMPORAL_AUTH_CALLBACK_URL`

The callback URL used by Temporal for authentication and authorization.

Callback URLs are invoked by IDP after user has finished authenticating in IDP.

## `TEMPORAL_AUTH_SCOPES`

Specifies a set of scopes for auth. Typically, this is `openid`, `profile`, `email`.

## `TEMPORAL_TLS_CA`

The path for the Transport Layer Security (TLS) Certificate Authority file.

In order to [configure TLS for your server](/references/web-ui-configuration#tls), you'll need a CA certificate issued
by a trusted Certificate Authority. Set this variable to properly locate and use the file.

## `TEMPORAL_TLS_CERT`

The path for the Transport Layer Security (TLS) Certificate.

In order to [configure TLS for your server](/references/web-ui-configuration#tls), you'll need a self-signed
certificate. Set the path to allow the environment to locate and use the certificate.

## `TEMPORAL_TLS_KEY`

The path for the Transport Layer Security (TLS) [key file](/references/web-ui-configuration#tls).

A key file is used to create private and public keys for encryption and signing. Together, these keys are used to create
certificates.

## `TEMPORAL_TLS_CA_DATA`

Stores the data for a TLS CA file.

This variable can be used instead of providing a path for `TEMPORAL_TLS_CA`.

## `TEMPORAL_TLS_CERT_DATA`

Stores the data for a TLS cert file.

This variable can be used instead of providing a path for `TEMPORAL_TLS_CERT`.

## `TEMPORAL_TLS_KEY_DATA`

Stores the data for a TLS key file.

This variable can be used instead of providing a path for `TEMPORAL_TLS_KEY`.

## `TEMPORAL_TLS_ENABLE_HOST_VERIFICATION`

Enables or disables [Transport Layer Security (TLS) host verification](/references/web-ui-configuration#tls).

When enabled, TLS checks the Host Server to ensure that files are being sent to and from the correct URL.

## `TEMPORAL_TLS_SERVER_NAME`

The server on which to operate [Transport Layer Security (TLS) protocols](/references/web-ui-configuration#tls).

TLS allows the current server to transmit encrypted files to other URLs without having to reveal itself. Because of
this, TLS operates a go-between server.

## `TEMPORAL_CODEC_ENDPOINT`

The endpoint for the [Codec Server](/codec-server), if configured.

## `TEMPORAL_CODEC_PASS_ACCESS_TOKEN`
