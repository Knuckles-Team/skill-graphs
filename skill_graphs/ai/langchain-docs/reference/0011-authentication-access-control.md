# Authentication & access control
Source: https://docs.langchain.com/langsmith/auth

LangSmith provides a flexible authentication and authorization system that can integrate with most authentication schemes.

## Core concepts

### Authentication vs authorization

While often used interchangeably, these terms represent distinct security concepts:

* [**Authentication**](#authentication) ("AuthN") verifies *who* you are. This runs as middleware for every request.
* [**Authorization**](#authorization) ("AuthZ") determines *what you can do*. This validates the user's privileges and roles on a per-resource basis.

In LangSmith, authentication is handled by your [`@auth.authenticate`](https://reference.langchain.com/python/langgraph-sdk/auth/Auth/authenticate) handler, and authorization is handled by your [`@auth.on`](https://reference.langchain.com/python/langgraph-sdk/auth/Auth/on) handlers.

## Default security models

LangSmith provides different security defaults:

### LangSmith

* Uses LangSmith API keys by default
* Requires valid API key in `x-api-key` header
* Can be customized with your auth handler

<Note>
  **Custom auth**
  Custom auth **is supported** for all plans in LangSmith.
</Note>

### Self-hosted

* No default authentication
* Complete flexibility to implement your security model
* You control all aspects of authentication and authorization

## System architecture

A typical authentication setup involves three main components:

1. **Authentication Provider** (Identity Provider/IdP)
   * A dedicated service that manages user identities and credentials
   * Handles user registration, login, password resets, etc.
   * Issues tokens (JWT, session tokens, etc.) after successful authentication
   * Examples: Auth0, Supabase Auth, Okta, or your own auth server
2. **Agent Server** (Resource Server)
   * Your agent or LangGraph application, which contains business logic and protected resources
   * Validates tokens with the auth provider
   * Enforces access control based on user identity and permissions
   * Doesn't store user credentials directly
3. **Client Application** (Frontend)
   * Web app, mobile app, or API client
   * Collects time-sensitive user credentials and sends to auth provider
   * Receives tokens from auth provider
   * Includes these tokens in requests to the Agent Server

Here's how these components typically interact:

```mermaid actions={false} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sequenceDiagram
    participant Client as Client App
    participant Auth as Auth Provider
    participant LG as Agent Server

    Client->>Auth: 1. Login (username/password)
    Auth-->>Client: 2. Return token
    Client->>LG: 3. Request with token
    Note over LG: 4. Validate token (@auth.authenticate)
    LG-->>Auth:  5. Fetch user info
    Auth-->>LG: 6. Confirm validity
    Note over LG: 7. Apply access control (@auth.on.*)
    LG-->>Client: 8. Return resources
```

Your [`@auth.authenticate`](https://reference.langchain.com/python/langgraph-sdk/auth/Auth/authenticate) handler in LangGraph handles steps 4-6, while your [`@auth.on`](https://reference.langchain.com/python/langgraph-sdk/auth/Auth/on) handlers implement step 7.

## Authentication

Authentication in LangGraph runs as middleware on every request. Your [`@auth.authenticate`](https://reference.langchain.com/python/langgraph-sdk/auth/Auth/authenticate) handler receives request information and should:

1. Validate the credentials
2. Return [user info](https://reference.langchain.com/python/langgraph-sdk/auth/types/MinimalUserDict) containing the user's identity and user information if valid
3. Raise an [HTTP exception](https://reference.langchain.com/python/langgraph-sdk/auth/exceptions/HTTPException) or AssertionError if invalid

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph_sdk import Auth

auth = Auth()

@auth.authenticate
async def authenticate(headers: dict) -> Auth.types.MinimalUserDict:
    # Validate credentials (e.g., API key, JWT token)
    api_key = headers.get(b"x-api-key")
    if not api_key or not is_valid_key(api_key):
        raise Auth.exceptions.HTTPException(
            status_code=401,
            detail="Invalid API key"
        )

    # Return user info - only identity and is_authenticated are required
    # Add any additional fields you need for authorization
    return {
        "identity": "user-123",        # Required: unique user identifier
        "is_authenticated": True,      # Optional: assumed True by default
        "permissions": ["read", "write"], # Optional: for permission-based auth
        # You can add more custom fields if you want to implement other auth patterns
        "role": "admin",
        "org_id": "org-456"

    }
```

The returned user information is available:

* To your authorization handlers via [`ctx.user`](https://reference.langchain.com/python/langgraph-sdk/auth/types/AuthContext)
* In your application via `config["configuration"]["langgraph_auth_user"]`

<Accordion title="Supported Parameters">
  The [`@auth.authenticate`](https://reference.langchain.com/python/langgraph-sdk/auth/Auth/authenticate) handler can accept any of the following parameters by name:

  * request (Request): The raw ASGI request object
  * path (str): The request path, e.g., `"/threads/abcd-1234-abcd-1234/runs/abcd-1234-abcd-1234/stream"`
  * method (str): The HTTP method, e.g., `"GET"`
  * path\_params (dict\[str, str]): URL path parameters, e.g., `{"thread_id": "abcd-1234-abcd-1234", "run_id": "abcd-1234-abcd-1234"}`
  * query\_params (dict\[str, str]): URL query parameters, e.g., `{"stream": "true"}`
  * headers (dict\[bytes, bytes]): Request headers
  * authorization (str | None): The Authorization header value (e.g., `"Bearer <token>"`)

  In many of our tutorials, we will just show the "authorization" parameter to be concise, but you can opt to accept more information as needed
  to implement your custom authentication scheme.
</Accordion>

### Agent authentication

Custom authentication permits delegated access. The values you return in  `@auth.authenticate` are added to the run context, giving agents user-scoped credentials lets them access resources on the user’s behalf.

```mermaid actions={false} theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sequenceDiagram
  %% Actors
  participant ClientApp as Client
  participant AuthProv  as Auth Provider
  participant LangGraph as Agent Server
  participant SecretStore as Secret Store
  participant ExternalService as External Service

  %% Platform login / AuthN
  ClientApp  ->> AuthProv: 1. Login (username / password)
  AuthProv   -->> ClientApp: 2. Return token
  ClientApp  ->> LangGraph: 3. Request with token

  Note over LangGraph: 4. Validate token (@auth.authenticate)
  LangGraph  -->> AuthProv: 5. Fetch user info
  AuthProv   -->> LangGraph: 6. Confirm validity

  %% Fetch user tokens from secret store
  LangGraph  ->> SecretStore: 6a. Fetch user tokens
  SecretStore -->> LangGraph: 6b. Return tokens

  Note over LangGraph: 7. Apply access control (@auth.on.*)

  %% External Service round-trip
  LangGraph  ->> ExternalService: 8. Call external service (with header)
  Note over ExternalService: 9. External service validates header and executes action
  ExternalService  -->> LangGraph: 10. Service response

  %% Return to caller
  LangGraph  -->> ClientApp: 11. Return resources
```

After authentication, the platform creates a special configuration object that is passed to your graph and all nodes via the configurable context.
This object contains information about the current user, including any custom fields you return from your [`@auth.authenticate`](https://reference.langchain.com/python/langgraph-sdk/auth/Auth/authenticate) handler.

To enable an agent to act on behalf of the user, use [custom authentication middleware](/langsmith/custom-auth). This will allow the agent to interact with external systems like MCP servers, external databases, and even other agents on behalf of the user.

For more information, see the [Use custom auth](/langsmith/custom-auth#enable-agent-authentication) guide.

### Agent authentication with MCP

For information on how to authenticate an agent to an MCP server, see the [MCP conceptual guide](/oss/python/langchain/mcp).

## Authorization

After authentication, LangGraph calls your [`@auth.on`](https://reference.langchain.com/python/langgraph-sdk/auth/Auth) handlers to control access to specific resources (e.g., threads, assistants, crons). These handlers can:

1. Add metadata to be saved during resource creation by mutating the `value["metadata"]` dictionary directly. See the [supported actions table](#supported-actions) for the list of types the value can take for each action.
2. Filter resources by metadata during search/list or read operations by returning a [filter dictionary](#filter-operations).
3. Raise an HTTP exception if access is denied.

If you want to just implement simple user-scoped access control, you can use a single [`@auth.on`](https://reference.langchain.com/python/langgraph-sdk/auth/Auth) handler for all resources and actions. If you want to have different control depending on the resource and action, you can use [resource-specific handlers](#resource-specific-handlers). See the [Supported Resources](#supported-resources) section for a full list of the resources that support access control.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
@auth.on
async def add_owner(
    ctx: Auth.types.AuthContext,
    value: dict  # The payload being sent to this access method
) -> dict:  # Returns a filter dict that restricts access to resources
    """Authorize all access to threads, runs, crons, and assistants.

    This handler does two things:
        - Adds a value to resource metadata (to persist with the resource so it can be filtered later)
        - Returns a filter (to restrict access to existing resources)

    Args:
        ctx: Authentication context containing user info, permissions, the path, and
        value: The request payload sent to the endpoint. For creation
              operations, this contains the resource parameters. For read
              operations, this contains the resource being accessed.

    Returns:
        A filter dictionary that LangGraph uses to restrict access to resources.
        See [Filter Operations](#filter-operations) for supported operators.
    """
    # Create filter to restrict access to just this user's resources
    filters = {"owner": ctx.user.identity}

    # Get or create the metadata dictionary in the payload
    # This is where we store persistent info about the resource
    metadata = value.setdefault("metadata", {})

    # Add owner to metadata - if this is a create or update operation,
    # this information will be saved with the resource
    # So we can filter by it later in read operations
    metadata.update(filters)

    # Return filters to restrict access
    # These filters are applied to ALL operations (create, read, update, search, etc.)
    # to ensure users can only access their own resources
    return filters
```

<a />

### Resource-specific handlers

You can register handlers for specific resources and actions by chaining the resource and action names together with the [`@auth.on`](https://reference.langchain.com/python/langgraph-sdk/auth/Auth) decorator.
When a request is made, the most specific handler that matches that resource and action is called. Below is an example of how to register handlers for specific resources and actions. For the following setup:

1. Authenticated users are able to create threads, read threads, and create runs on threads
2. Only users with the "assistants:create" permission are allowed to create new assistants
3. All other endpoints (e.g., e.g., delete assistant, crons, store) are disabled for all users.

<Tip>
  **Supported Handlers**
  For a full list of supported resources and actions, see the [Supported Resources](#supported-resources) section below.
</Tip>

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Generic / global handler catches calls that aren't handled by more specific handlers
@auth.on
async def reject_unhandled_requests(ctx: Auth.types.AuthContext, value: Any) -> False:
    print(f"Request to {ctx.path} by {ctx.user.identity}")
    raise Auth.exceptions.HTTPException(
        status_code=403,
        detail="Forbidden"
    )

# Matches the "thread" resource and all actions - create, read, update, delete, search

# Since this is **more specific** than the generic @auth.on handler, it will take precedence

# over the generic handler for all actions on the "threads" resource
@auth.on.threads
async def on_thread(
    ctx: Auth.types.AuthContext,
    value: Auth.types.threads.create.value
):
    # Setting metadata on the thread being created
    # will ensure that the resource contains an "owner" field
    # Then any time a user tries to access this thread or runs within the thread,
    # we can filter by owner
    metadata = value.setdefault("metadata", {})
    metadata["owner"] = ctx.user.identity
    return {"owner": ctx.user.identity}

# Thread creation. This will match only on thread create actions

# Since this is **more specific** than both the generic @auth.on handler and the @auth.on.threads handler,

# it will take precedence for any "create" actions on the "threads" resources
@auth.on.threads.create
async def on_thread_create(
    ctx: Auth.types.AuthContext,
    value: Auth.types.threads.create.value
):
    # Reject if the user does not have write access
    if "write" not in ctx.permissions:
        raise Auth.exceptions.HTTPException(
            status_code=403,
            detail="User lacks the required permissions."
        )
    # Setting metadata on the thread being created
    # will ensure that the resource contains an "owner" field
    # Then any time a user tries to access this thread or runs within the thread,
    # we can filter by owner
    metadata = value.setdefault("metadata", {})
    metadata["owner"] = ctx.user.identity
    return {"owner": ctx.user.identity}

# Reading a thread. Since this is also more specific than the generic @auth.on handler, and the @auth.on.threads handler,

# it will take precedence for any "read" actions on the "threads" resource
@auth.on.threads.read
async def on_thread_read(
    ctx: Auth.types.AuthContext,
    value: Auth.types.threads.read.value
):
    # Since we are reading (and not creating) a thread,
    # we don't need to set metadata. We just need to
    # return a filter to ensure users can only see their own threads
    return {"owner": ctx.user.identity}

# Run creation, streaming, updates, etc.

# This takes precedenceover the generic @auth.on handler and the @auth.on.threads handler
@auth.on.threads.create_run
async def on_run_create(
    ctx: Auth.types.AuthContext,
    value: Auth.types.threads.create_run.value
):
    metadata = value.setdefault("metadata", {})
    metadata["owner"] = ctx.user.identity
    # Inherit thread's access control
    return {"owner": ctx.user.identity}

# Assistant creation
@auth.on.assistants.create
async def on_assistant_create(
    ctx: Auth.types.AuthContext,
    value: Auth.types.assistants.create.value
):
    if "assistants:create" not in ctx.permissions:
        raise Auth.exceptions.HTTPException(
            status_code=403,
            detail="User lacks the required permissions."
        )
```

Notice that we are mixing global and resource-specific handlers in the above example. Since each request is handled by the most specific handler, a request to create a `thread` would match the `on_thread_create` handler but NOT the `reject_unhandled_requests` handler. A request to `update` a thread, however would be handled by the global handler, since we don't have a more specific handler for that resource and action.

<a />

### Filter operations

Authorization handlers can return `None`, a boolean, or a filter dictionary.

* `None` and `True` mean "authorize access to all underling resources"
* `False` means "deny access to all underling resources (raises a 403 exception)"
* A metadata filter dictionary will restrict access to resources

A filter dictionary is a dictionary with keys that match the resource metadata. It supports three operators:

* The default value is a shorthand for exact match, or "\$eq", below. For example, `{"owner": user_id}` will include only resources with metadata containing `{"owner": user_id}`
* `$eq`: Exact match (e.g., `{"owner": {"$eq": user_id}}`) - this is equivalent to the shorthand above, `{"owner": user_id}`
* `$contains`: List membership (e.g., `{"allowed_users": {"$contains": user_id}}`) or list containment (e.g., `{"allowed_users": {"$contains": [user_id_1, user_id_2]}}`). The value here must be an element of the list or a subset of the elements of the list, respectively. The metadata in the stored resource must be a list/container type.

A dictionary with multiple keys is treated using a logical `AND` filter. For example, `{"owner": org_id, "allowed_users": {"$contains": user_id}}` will only match resources with metadata whose "owner" is `org_id` and whose "allowed\_users" list contains `user_id`.
See the reference [`Auth`](https://reference.langchain.com/python/langgraph-sdk/auth/Auth)(Auth) for more information.

## Common access patterns

Here are some typical authorization patterns:

### Single-owner resources

This common pattern lets you scope all threads, assistants, crons, and runs to a single user. It's useful for common single-user use cases like regular chatbot-style apps.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
@auth.on
async def owner_only(ctx: Auth.types.AuthContext, value: dict):
    metadata = value.setdefault("metadata", {})
    metadata["owner"] = ctx.user.identity
    return {"owner": ctx.user.identity}
```

### Permission-based access

This pattern lets you control access based on **permissions**. It's useful if you want certain roles to have broader or more restricted access to resources.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# In your auth handler:
@auth.authenticate
async def authenticate(headers: dict) -> Auth.types.MinimalUserDict:
    ...
    return {
        "identity": "user-123",
        "is_authenticated": True,
        "permissions": ["threads:write", "threads:read"]  # Define permissions in auth
    }

def _default(ctx: Auth.types.AuthContext, value: dict):
    metadata = value.setdefault("metadata", {})
    metadata["owner"] = ctx.user.identity
    return {"owner": ctx.user.identity}

@auth.on.threads.create
async def create_thread(ctx: Auth.types.AuthContext, value: dict):
    if "threads:write" not in ctx.permissions:
        raise Auth.exceptions.HTTPException(
            status_code=403,
            detail="Unauthorized"
        )
    return _default(ctx, value)

@auth.on.threads.read
async def rbac_create(ctx: Auth.types.AuthContext, value: dict):
    if "threads:read" not in ctx.permissions and "threads:write" not in ctx.permissions:
        raise Auth.exceptions.HTTPException(
            status_code=403,
            detail="Unauthorized"
        )
    return _default(ctx, value)
```

## Supported resources

LangGraph provides three levels of authorization handlers, from most general to most specific:

1. **Global Handler** (`@auth.on`): Matches all resources and actions
2. **Resource Handler** (e.g., `@auth.on.threads`, `@auth.on.assistants`, `@auth.on.crons`): Matches all actions for a specific resource
3. **Action Handler** (e.g., `@auth.on.threads.create`, `@auth.on.threads.read`): Matches a specific action on a specific resource

The most specific matching handler will be used. For example, `@auth.on.threads.create` takes precedence over `@auth.on.threads` for thread creation.
If a more specific handler is registered, the more general handler will not be called for that resource and action.

<Tip>
  "Type Safety"
  Each handler has type hints available for its `value` parameter at `Auth.types.on.<resource>.<action>.value`. For example:

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  @auth.on.threads.create
  async def on_thread_create(
  ctx: Auth.types.AuthContext,
  value: Auth.types.on.threads.create.value  # Specific type for thread creation
  ):
  ...

  @auth.on.threads
  async def on_threads(
  ctx: Auth.types.AuthContext,
  value: Auth.types.on.threads.value  # Union type of all thread actions
  ):
  ...

  @auth.on
  async def on_all(
  ctx: Auth.types.AuthContext,
  value: dict  # Union type of all possible actions
  ):
  ...
  ```

  More specific handlers provide better type hints since they handle fewer action types.
</Tip>

<a />

#### Supported actions and types

Here are all the supported action handlers:

| Resource       | Handler                       | Description                | Value Type                                                                                             |
| -------------- | ----------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Threads**    | `@auth.on.threads.create`     | Thread creation            | [`ThreadsCreate`](https://reference.langchain.com/python/langgraph-sdk/auth/types/ThreadsCreate)       |
|                | `@auth.on.threads.read`       | Thread retrieval           | [`ThreadsRead`](https://reference.langchain.com/python/langgraph-sdk/auth/types/ThreadsRead)           |
|                | `@auth.on.threads.update`     | Thread updates             | [`ThreadsUpdate`](https://reference.langchain.com/python/langgraph-sdk/auth/types/ThreadsUpdate)       |
|                | `@auth.on.threads.delete`     | Thread deletion            | [`ThreadsDelete`](https://reference.langchain.com/python/langgraph-sdk/auth/types/ThreadsDelete)       |
|                | `@auth.on.threads.search`     | Listing threads            | [`ThreadsSearch`](https://reference.langchain.com/python/langgraph-sdk/auth/types/ThreadsSearch)       |
|                | `@auth.on.threads.create_run` | Creating or updating a run | [`RunsCreate`](https://reference.langchain.com/python/langgraph-sdk/auth/types/RunsCreate)             |
| **Assistants** | `@auth.on.assistants.create`  | Assistant creation         | [`AssistantsCreate`](https://reference.langchain.com/python/langgraph-sdk/auth/types/AssistantsCreate) |
|                | `@auth.on.assistants.read`    | Assistant retrieval        | [`AssistantsRead`](https://reference.langchain.com/python/langgraph-sdk/auth/types/AssistantsRead)     |
|                | `@auth.on.assistants.update`  | Assistant updates          | [`AssistantsUpdate`](https://reference.langchain.com/python/langgraph-sdk/auth/types/AssistantsUpdate) |
|                | `@auth.on.assistants.delete`  | Assistant deletion         | [`AssistantsDelete`](https://reference.langchain.com/python/langgraph-sdk/auth/types/AssistantsDelete) |
|                | `@auth.on.assistants.search`  | Listing assistants         | [`AssistantsSearch`](https://reference.langchain.com/python/langgraph-sdk/auth/types/AssistantsSearch) |
| **Crons**      | `@auth.on.crons.create`       | Cron job creation          | [`CronsCreate`](https://reference.langchain.com/python/langgraph-sdk/auth/types/CronsCreate)           |
|                | `@auth.on.crons.read`         | Cron job retrieval         | [`CronsRead`](https://reference.langchain.com/python/langgraph-sdk/auth/types/CronsRead)               |
|                | `@auth.on.crons.update`       | Cron job updates           | [`CronsUpdate`](https://reference.langchain.com/python/langgraph-sdk/auth/types/CronsUpdate)           |
|                | `@auth.on.crons.delete`       | Cron job deletion          | [`CronsDelete`](https://reference.langchain.com/python/langgraph-sdk/auth/types/CronsDelete)           |
|                | `@auth.on.crons.search`       | Listing cron jobs          | [`CronsSearch`](https://reference.langchain.com/python/langgraph-sdk/auth/types/CronsSearch)           |

<Note>
  "About Runs"

  Runs are scoped to their parent thread for access control. This means permissions are typically inherited from the thread, reflecting the conversational nature of the data model. All run operations (reading, listing) except creation are controlled by the thread's handlers.
  There is a specific `create_run` handler for creating new runs because it had more arguments that you can view in the handler.
</Note>

## Next steps

For implementation details:

* Check out the introductory tutorial on [setting up authentication](/langsmith/set-up-custom-auth)
* See the how-to guide on implementing a [custom auth handlers](/langsmith/custom-auth)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/auth.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Authentication methods
Source: https://docs.langchain.com/langsmith/authentication-methods

LangSmith supports multiple authentication methods for easy sign-up and login.

## Cloud

### Email/Password

Users can use an email address and password to sign up and login to LangSmith.

### Social providers

Users can alternatively use their credentials from GitHub or Google.

### SAML SSO

Enterprise customers can configure [SAML SSO](/langsmith/user-management) and [SCIM](/langsmith/user-management). [Get a demo](https://www.langchain.com/contact-sales) to learn more.

## Self-Hosted

Self-hosted customers have more control over how their users can login to LangSmith. For more in-depth coverage of configuration options, see [the self-hosting docs](/langsmith/self-hosted) and [Helm chart](https://github.com/langchain-ai/helm/tree/main/charts/langsmith).

### SSO with OAuth 2.0 and OIDC

Production installations should configure SSO in order to use an external identity provider. This enables users to login through an identity platform like Auth0/Okta. LangSmith supports almost any OIDC-compliant provider. Learn more about configuring SSO in the [SSO configuration guide](/langsmith/self-host-sso)

### Email/Password a.k.a. basic auth

This auth method requires very little configuration as it does not require an external identity provider. It is most appropriate to use for self-hosted trials. Learn more in the [basic auth configuration guide](/langsmith/self-host-basic-auth)

### None

<Warning>
  This authentication mode will be removed after the launch of Basic Auth.
</Warning>

If zero authentication methods are enabled, a self-hosted installation does not require any login/sign-up. This configuration should only be used for verifying installation at the infrastructure level, as the feature set supported in this mode is restricted with only a single organization and workspace.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/authentication-methods.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Self-hosted LangSmith on AWS
Source: https://docs.langchain.com/langsmith/aws-self-hosted

When running LangSmith on [Amazon Web Services (AWS)](https://aws.amazon.com/), [self-hosted](/langsmith/self-hosted) mode deploys a complete LangSmith platform with observability functionality.

This page provides:

* [Initial setup steps](#initial-setup) for deploying to EKS, configuring managed services, and setting up authentication.
* [AWS-specific architecture patterns](#reference-architecture) and reference diagrams.
* [Service recommendations](#compute-options) and best practices.
* [AWS Well-Architected best practices](#aws-well-architected-best-practices) for operational excellence, security, and reliability.

<Note>
  LangChain provides Terraform modules specifically for AWS to help provision infrastructure for LangSmith. These modules can quickly set up EKS clusters, RDS, ElastiCache, S3, and networking resources.

  View the [AWS Terraform modules](https://github.com/langchain-ai/terraform/tree/main/modules/aws) for documentation and examples.
</Note>

## Initial setup

<Steps>
  <Step title="Deploy to Kubernetes">
    Follow the [Kubernetes installation guide](/langsmith/kubernetes). LangSmith is tested on Amazon Elastic Kubernetes Service (EKS).

    **EKS-specific notes:**

    * Ensure the EBS CSI Driver is installed for persistent storage
    * Use the `ebs.csi.aws.com` storage class provisioner
  </Step>

  <Step title="Configure external services">
    For production deployments, connect to AWS managed services:

    <CardGroup>
      <Card title="Amazon S3" icon="database" href="/langsmith/self-host-blob-storage#amazon-s3">
        Store trace data in S3
      </Card>

      <Card title="Amazon RDS" icon="database" href="/langsmith/self-host-external-postgres#amazon-rds">
        PostgreSQL database
      </Card>

      <Card title="Amazon ElastiCache" icon="cpu" href="/langsmith/self-host-external-redis#amazon-elasticache">
        Redis or Valkey for caching
      </Card>

      <Card title="ClickHouse Cloud" icon="chart-line" href="/langsmith/self-host-external-clickhouse">
        Analytics database
      </Card>
    </CardGroup>
  </Step>

  <Step title="Set up authentication">
    Use [IAM Roles for Service Accounts (IRSA)](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) to authenticate LangSmith pods to AWS services without static credentials.

    **Key pages:**

    * [S3 IRSA configuration](/langsmith/self-host-blob-storage#amazon-s3)
    * [RDS IAM authentication](/langsmith/self-host-external-postgres#iam-authentication)
    * [ElastiCache IAM authentication](/langsmith/self-host-external-redis#iam-authentication)
  </Step>
</Steps>

After completing these initial setup steps, you can review the complete AWS architecture and best practices below.

## Reference architecture

We recommend leveraging AWS's managed services to provide a scalable, secure, and resilient platform. The following architecture applies to both self-hosted and hybrid and aligns with the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/):

<img alt="Architecture diagram showing AWS relations to LangSmith services" />

* <Icon icon="globe" /> **Ingress & networking**: Requests enter via [Amazon Application Load Balancer (ALB)](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/) within your [VPC](https://aws.amazon.com/vpc/), secured using [AWS WAF](https://aws.amazon.com/waf/) and [IAM](https://aws.amazon.com/iam/)-based authentication.

* <Icon icon="cube" /> **Frontend & backend services:** Containers run on [Amazon EKS](https://aws.amazon.com/eks/), orchestrated behind the ALB. routes requests to other services within the cluster as necessary.

* <Icon icon="database" /> **Storage & databases:**
  * [Amazon RDS for PostgreSQL](https://aws.amazon.com/rds/postgresql/) or [Aurora](https://aws.amazon.com/rds/aurora/): metadata, projects, users, and short-term and long-term memory for deployed agents. LangSmith supports PostgreSQL version 14 or higher.
  * [Amazon ElastiCache](https://aws.amazon.com/elasticache/) (Redis or Valkey): caching and job queues. ElastiCache can be in single-instance or cluster mode. LangSmith requires Redis OSS version 5 or higher, or Valkey 8.
  * ClickHouse + [Amazon EBS](https://aws.amazon.com/ebs/): analytics and trace storage.
    * We recommend using an [externally managed ClickHouse solution](/langsmith/self-host-external-clickhouse) unless security or compliance reasons
      prevent you from doing so.
    * ClickHouse is not required for hybrid deployments.
  * [Amazon S3](https://aws.amazon.com/s3/): object storage for trace artifacts and telemetry.

* <Icon icon="sparkles" /> **LLM integration:** Optionally proxy requests to [Amazon Bedrock](https://aws.amazon.com/bedrock/) or [Amazon SageMaker](https://aws.amazon.com/sagemaker/) for LLM inference.

* <Icon icon="chart-line" /> **Monitoring & observability:** Integrate with [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

## Compute options

LangSmith supports multiple compute options depending on your requirements:

| Compute option                             | Description                               | Suitable for                         |
| ------------------------------------------ | ----------------------------------------- | ------------------------------------ |
| **Elastic Kubernetes Service (preferred)** | Advanced scaling and multi-tenant support | Large enterprises                    |
| **EC2-based**                              | Full control, BYO-infra                   | Regulated or air-gapped environments |

## AWS Well-Architected best practices

This reference is designed to align with the six pillars of the AWS Well-Architected Framework:

### Operational excellence

* Automate deployments with IaC ([CloudFormation](https://aws.amazon.com/cloudformation/) / [Terraform](https://www.terraform.io/)).
* Use [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) for configuration.
* Configure your LangSmith instance to [export telemetry data](/langsmith/export-backend) and continuously monitor via [CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html).
* The preferred method to manage [LangSmith deployments](/langsmith/deployment) is to create a CI process that builds [Agent Server](/langsmith/agent-server) images and pushes them to [ECR](https://aws.amazon.com/ecr/). Create a test deployment for pull requests before deploying a new revision to staging or production upon PR merge.

### Security

* Use [IAM](https://aws.amazon.com/iam/) roles with least-privilege policies.
* Enable encryption at rest ([RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html), [S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html), ClickHouse volumes) and in transit (TLS 1.2+).
* Integrate with [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) for credentials.
* Use [Amazon Cognito](https://aws.amazon.com/cognito/) as an IDP in conjunction with LangSmith's built-in authentication and authorization features to secure access to agents and their tools.

### Reliability

* Replicate the LangSmith [data plane](/langsmith/data-plane) across regions: Deploy identical data planes to Kubernetes clusters in different regions for LangSmith Deployment. Deploy [RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html) and [ECS](https://aws.amazon.com/ecs/) services across [Multi-AZ](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/).
* Implement [auto-scaling](https://aws.amazon.com/autoscaling/) for backend workers.
* Use [Amazon Route 53](https://aws.amazon.com/route53/) health checks and failover policies.

### Performance efficiency

* Leverage [EC2](https://aws.amazon.com/ec2/) instances for optimized compute.
* Use [S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) for infrequently accessed trace data.

### Cost optimization

* Right-size [EKS](https://aws.amazon.com/eks/) clusters using [Compute Savings Plans](https://aws.amazon.com/savingsplans/compute-pricing/).
* Monitor cost KPIs using [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) dashboards.

### Sustainability

* Minimize idle workloads with on-demand compute.
* Store telemetry in low-latency, low-cost tiers.
* Enable auto-shutdown for non-prod environments.

## Security and compliance

LangSmith can be configured for:

* [PrivateLink](https://aws.amazon.com/privatelink/)-only access (no public internet exposure, besides egress necessary for billing).
* [KMS](https://aws.amazon.com/kms/)-based encryption keys for S3, RDS, and EBS.
* Audit logging to [CloudWatch](https://aws.amazon.com/cloudwatch/) and [AWS CloudTrail](https://aws.amazon.com/cloudtrail/).

Customers can deploy in [GovCloud](https://aws.amazon.com/govcloud-us/), ISO, or HIPAA regions as needed.

## Monitoring and evals

Use LangSmith to:

* Capture traces from LLM apps running on [Bedrock](https://aws.amazon.com/bedrock/) or [SageMaker](https://aws.amazon.com/sagemaker/).
* Evaluate model outputs via [LangSmith datasets](/langsmith/manage-datasets).
* Track latency, token usage, and success rates.

Integrate with:

* [AWS CloudWatch](https://aws.amazon.com/cloudwatch/) dashboards.
* [OpenTelemetry](https://opentelemetry.io/) and [Prometheus](https://prometheus.io/) exporters.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/aws-self-hosted.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
