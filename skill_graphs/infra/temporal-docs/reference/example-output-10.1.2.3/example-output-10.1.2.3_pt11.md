grants access to call the API, but the scope of what the caller can interact with depends on their role.

### API key authorization behavior

All roles can create and manage their **own** API keys. An API key inherits the permissions of its owner — it cannot
grant access beyond what the owning user or service account already has.

| Behavior                                            | Read-only | Developer | Finance Admin | Global Admin | Account Owner |
| --------------------------------------------------- | :-------: | :-------: | :-----------: | :----------: | :-----------: |
| Create, view, update, and delete own API keys       |     ✔     |     ✔     |       ✔       |      ✔       |       ✔       |
| View, update, and delete any API key in the account |           |           |               |      ✔       |       ✔       |

**Affected APIs:** CreateApiKey, GetApiKey, GetApiKeys, UpdateApiKey, DeleteApiKey

### Service account authorization behavior

All roles can list service accounts within their account. However, the ability to create, update, and delete service
accounts depends on the scope of the service account and the caller's role.

| Behavior                                         | Read-only | Developer | Finance Admin | Global Admin | Account Owner |
| ------------------------------------------------ | :-------: | :-------: | :-----------: | :----------: | :-----------: |
| List all service accounts in the account         |     ✔     |     ✔     |       ✔       |      ✔       |       ✔       |
| Manage unscoped (account-level) service accounts |           |           |               |      ✔       |       ✔       |
| Manage Namespace-scoped service accounts         |     §     |     §     |       §       |      ✔       |       ✔       |

§ Requires Namespace Admin permission on the target Namespace. Any role can manage Namespace-scoped service accounts if
they hold Namespace Admin on that Namespace.

**Affected APIs:** CreateServiceAccount, GetServiceAccount, GetServiceAccounts, UpdateServiceAccount,
DeleteServiceAccount

---

## Roles and permissions

Temporal Cloud uses role-based access control (RBAC) to manage access to resources. Access is governed both on the
account-level and within a Namespace. On the account-level, each access principal is assigned one account-level role. On
the Namespace-level, each access principal can be assigned one Namespace-level permission. Some account-level roles,
such as Account Owner and Global Admin, automatically have Namespace Admin permissions on all Namespaces in the account.

## Account-level roles

Account-level roles are assigned to access principals at the account level. They control access to account resources,
such as:

- Users and Service Accounts
- Billing and usage
- Namespaces. This includes creating and managing Namespaces only, not access to resources within a Namespace, which is
  controlled by [Namespace-level permissions](#namespace-level-permissions).
- Nexus Endpoints

The following table provides a summary of the account-level roles and their primary purpose. Refer to the
[Permissions reference](/cloud/manage-access/permissions-reference#account-level-access) for API-level details.

| Role          | Primary purpose                             | Can create Namespaces | Automatic Namespace Admin               | Billing and usage access          |
| ------------- | ------------------------------------------- | --------------------- | --------------------------------------- | --------------------------------- |
| Account Owner | Owns and governs the account                | Yes                   | All Namespaces (cannot be revoked)      | Full billing, payments, and usage |
| Global Admin  | Administers account configuration and users | Yes                   | All Namespaces (cannot be revoked)      | Usage only                        |
| Developer     | Creates and manages Namespaces they own     | Yes                   | Namespaces they create (can be revoked) | None                              |
| Finance Admin | Manages billing and payment information     | No                    | None                                    | Full billing, payments, and usage         |
| Read-Only     | Views account configuration and resources   | No                    | None                                    | None                              |

Account-level roles don't govern day-to-day operations within a Namespace. Access to resources inside a Namespace, such
as Workflows and Workflow Executions, is controlled by [Namespace-level permissions](#namespace-level-permissions).

Account Owner and Global Admin roles automatically have Namespace Admin permissions on all Namespaces in the account,
and these permissions cannot be revoked without removing the role. Developers can create Namespaces, and have Namespace
Admin permissions for each Namespace they create. This permission can be revoked. Developer roles also don't have
automatic access to Namespaces that they didn't create.

### Best practice for assigning the Account Owner role

The Account Owner role holds the highest level of access in the system. This role configures account-level parameters
and manages Temporal billing and payment information. It allows users to perform all actions within the Temporal Cloud
account.

We strongly recommend the following precautions when assigning the Account Owner role to users:

- Assign the role to at least two users in your organization. Otherwise, limit the number of users with this role.
- Associate a person’s direct email address to the Account Owner, rather than a shared or generic address, so Temporal
  Support can contact the right person in urgent situations.

This latter rule is useful for anyone on your team who may need to be contacted urgently, regardless of their Account
role.

## Namespace-level permissions {/* #namespace-level-permissions */}

Namespace-level permissions govern access to resources within a Namespace, such as the following:

- Workflows
- Workflow Executions
- Task Queues
- Activity Executions
- Search Attributes
- History
- Events

Namespace-level permissions are assigned to access principals within a Namespace. Each permission has a set of actions
that grant access to specific resources within the Namespace.

The following table provides a summary of the Namespace-level permissions and their primary purpose. Refer to the
[Permissions reference](/cloud/manage-access/permissions-reference#namespace-level-permissions) for API-level details.

| Permission level | Intended use                      | Human access                                                                                 | Worker runtime access                                     | Namespace administration                                                                                  |
| ---------------- | --------------------------------- | -------------------------------------------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Read             | Observe Namespace activity        | View Workflows, Workflow Executions, Schedules, Task Queues, and metadata                    | None                                                      | None                                                                                                      |
| Write            | Operate Workflows and run Workers | Start, signal, cancel, terminate, and reset Workflows; manage Schedules and batch operations | Poll Task Queues and complete Workflow and Activity Tasks | None                                                                                                      |
| Namespace Admin  | Administer the Namespace          | All Read and Write capabilities                                                              | All Read and Write capabilities                           | Update Namespace settings, manage Search Attributes, Export Sinks, replication, and Namespace user access |

You can grant Namespace Admin, Write, or Read-Only permissions to principals with the account-level roles of Developer,
Finance Admin, or Read-Only. Account Owners and Global Admins already have Namespace Admin permissions on all Namespaces
in the account and do not need to be manually assigned Namespace-level permissions.

---

## General observability setup with metrics

:::danger PromQL endpoint deprecated

The PromQL endpoint and its `temporal_cloud_v0_*` metrics were deprecated on April 2, 2026 and are no longer accepting new users.
The PromQL endpoint will be disabled for all users on **October 5, 2026**.

New users should set up the [OpenMetrics endpoint](/cloud/metrics/openmetrics) instead.
Existing users should follow the [migration guide](/cloud/metrics/openmetrics/migration-guide) to transition to the OpenMetrics endpoint.

:::

You will learn how to do the following:

- [Configure an endpoint using the UI](#configure-via-ui)
- [Configure an endpoint using tcld](#configure-via-cli-tcld)
- [Query for metrics with a PromQL endpoint](#query-promql)

## Configure using the UI {/* #configure-via-ui */}

**How to configure a metrics endpoint using Temporal Cloud UI**

:::note

To view and manage third-party integration settings, your user account must have the Account Owner or Global Admin [role](/cloud/manage-access/roles-and-permissions#account-level-roles).

:::

To assign a certificate and generate your metrics endpoint, follow these steps:

1. Log in to Temporal Cloud UI with an Account Owner or Global Admin [role](/cloud/manage-access/roles-and-permissions#account-level-roles).
2. Go to **Settings** and select **Observability**.
4. Add your root CA certificate (.pem) and save it.
   Note that if an observability endpoint is already set up, you can append your root CA certificate here to use the generated observability endpoint in your observability tool.
5. To test your endpoint, run the following command on your host:
   ```
   curl -v --cert <path to your client-cert.pem> --key <path to your client-cert.key> "<your generated Temporal Cloud prometheus_endpoint>/api/v1/query?query=temporal_cloud_v0_state_transition_count"
   ```
   If you have Workflows running on a Namespace in your Temporal Cloud instance, you should see some data as a result of running this command.

After the page refreshes, the new metrics endpoint appears below **Endpoint**, in the form `https://<account-id>.tmprl.cloud/prometheus`.
Use the endpoint to configure your observability tool.
For example, if you use Grafana, see [Grafana data source configuration](/cloud/metrics/prometheus-grafana#grafana-data-source-configuration).

You can also query via the [Prometheus HTTP API](https://prometheus.io/docs/prometheus/latest/querying/api/) at URLs like:

```
https://<account-id>.tmprl.cloud/prometheus/api/v1/query?query=temporal_cloud_v0_state_transition_count
```

For example:

```
$ curl --cert client.pem --key client-key.pem "https://<account-id>.tmprl.cloud/prometheus/api/v1/query?query=temporal_cloud_v0_state_transition_count" | jq .
{
  "status": "success",
  "data": {
    "resultType": "vector",
    "result": [
      {
        "metric": {
          "__name__": "temporal_cloud_v0_state_transition_count",
          "__rollup__": "true",
          "operation": "WorkflowContext",
          "temporal_account": "your-account",
          "temporal_namespace": "your-namespace.your-account-is",
          "temporal_service_type": "history"
        },
        "value": [
          1672347471.2,
          "0"
        ]
      },
      ...
}
```

## Configure endpoint using tcld {/* #configure-via-cli-tcld */}

**How to configure a metrics endpoint using the tcld CLI.**

To add a certificate to a metrics endpoint, use [`tcld account metrics accepted-client-ca add`](/cloud/tcld/account#add).

To enable a metrics endpoint, use [`tcld account metrics enable`](/cloud/tcld/account#enable).

To disable a metrics endpoint, use [`tcld account metrics disable`](/cloud/tcld/account#disable).

For more information, see [tcld account metrics command](/cloud/tcld/account#metrics).

## Query for metrics with a PromQL endpoint {/* #query-promql */}

Temporal Cloud emits metrics in a Prometheus-supported format.
Prometheus is an open-source toolkit for alerting and monitoring.
The Temporal Service exposes Cloud metrics with a [Prometheus HTTP API endpoint](https://prometheus.io/docs/prometheus/latest/querying/api/).
Temporal Cloud metrics provide a compatible data source for visualizing, monitoring, and observability platforms.

You can use functions like [rate](https://prometheus.io/docs/prometheus/latest/querying/functions/#rate) or [increase](https://prometheus.io/docs/prometheus/latest/querying/functions/#increase) to calculate the rate of increase for a Temporal Cloud metric:

```
rate(temporal_cloud_v0_frontend_service_request_count[$__rate_interval])
```

Or you might use Prometheus to calculate average latencies or histogram quartiles:

```
