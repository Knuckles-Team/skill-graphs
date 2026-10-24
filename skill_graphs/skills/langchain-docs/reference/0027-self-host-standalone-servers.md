# Self-host standalone servers
Source: https://docs.langchain.com/langsmith/deploy-standalone-server

Deploy standalone Agent Servers using Docker, Docker Compose, or Kubernetes without the LangSmith control plane.

This guide shows you how to deploy **standalone <Tooltip>Agent Servers</Tooltip>** directly, without a [control plane](/langsmith/control-plane). You can deploy the server independently and still send traces to LangSmith (self-hosted or SaaS) for observability and evaluation. Standalone servers are production-ready and provide the most lightweight option for running agents.

## Overview

You manage a simplified <Tooltip>data plane</Tooltip> made up of Agent Servers and their required backing services (PostgreSQL, Redis, etc.):

| Component         | Responsibilities                                              | Where it runs       | Who manages it |
| ----------------- | ------------------------------------------------------------- | ------------------- | -------------- |
| **Control plane** | n/a                                                           | n/a                 | n/a            |
| **Data plane**    | <ul><li>Agent Servers</li><li>Postgres, Redis, etc.</li></ul> | Your infrastructure | You            |

This option gives you full control over scaling, deployment, and CI/CD pipelines, while still allowing optional integration with LangSmith for tracing and evaluation.

<Warning>
  Do not run standalone servers in serverless environments. Scale-to-zero may cause task loss and scaling up will not work reliably.
</Warning>

<img alt="Standalone server architecture" />

<img alt="Standalone server architecture" />

### Workflow

1. Define and test your graph locally using the `langgraph-cli` or [Studio](/langsmith/studio).
2. Package your agent as a Docker image.
3. Deploy the Agent Server to your compute platform of choice (Kubernetes, Docker, VM).
4. Optionally, configure LangSmith API keys and endpoints so the server reports traces and evaluations back to LangSmith (self-hosted or SaaS).

### Supported compute platforms

* **Kubernetes**: Use the LangSmith Helm chart to run Agent Servers in a Kubernetes cluster. This is the recommended option for production-grade deployments.
* **Docker**: Run in any Docker-supported compute platform (local dev machine, VM, ECS, etc.). This is best suited for development or small-scale workloads.

## Prerequisites

1. Use the [LangGraph CLI](/langsmith/cli) to [test your application locally](/langsmith/local-dev-testing).
2. Use the [LangGraph CLI](/langsmith/cli) to build a Docker image (i.e. `langgraph build`).
3. The following environment variables are needed for a data plane deployment.
4. `REDIS_URI`: Connection details to a Redis instance. Redis will be used as a pub-sub broker to enable streaming real time output from background runs. The value of `REDIS_URI` must be a valid [Redis connection URI](https://redis-py.readthedocs.io/en/stable/connections.html#redis.Redis.from_url).

   <Note>
     **Shared Redis Instance**
     Multiple self-hosted deployments can share the same Redis instance. For example, for `Deployment A`, `REDIS_URI` can be set to `redis://<hostname_1>:<port>/1` and for `Deployment B`, `REDIS_URI` can be set to `redis://<hostname_1>:<port>/2`.

     `1` and `2` are different database numbers within the same instance, but `<hostname_1>` is shared. **The same database number cannot be used for separate deployments**.
   </Note>
5. `DATABASE_URI`: Postgres connection details. Postgres will be used to store assistants, threads, runs, persist thread state and long term memory, and to manage the state of the background task queue with 'exactly once' semantics. The value of `DATABASE_URI` must be a valid [Postgres connection URI](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING-URIS).

   <Note>
     **Shared Postgres Instance**
     Multiple self-hosted deployments can share the same Postgres instance. For example, for `Deployment A`, `DATABASE_URI` can be set to `postgres://<user>:<password>@/<database_name_1>?host=<hostname_1>` and for `Deployment B`, `DATABASE_URI` can be set to `postgres://<user>:<password>@/<database_name_2>?host=<hostname_1>`.

     `<database_name_1>` and `database_name_2` are different databases within the same instance, but `<hostname_1>` is shared. **The same database cannot be used for separate deployments**.
   </Note>

   <Tip>
     You can optionally store checkpoint data in MongoDB instead of PostgreSQL. PostgreSQL is still required for all other server data. See [Configure checkpointer backend](/langsmith/configure-checkpointer) for details.
   </Tip>
6. `LANGSMITH_API_KEY`: LangSmith API key.
7. `LANGGRAPH_CLOUD_LICENSE_KEY`: LangSmith license key. This will be used to authenticate ONCE at server start up.
8. `LANGSMITH_ENDPOINT`: To send traces to a [self-hosted LangSmith](/langsmith/self-hosted) instance, set `LANGSMITH_ENDPOINT` to the hostname of the self-hosted LangSmith instance.
9. Egress to `https://beacon.langchain.com` from your network. This is required for license verification and usage reporting if not running in air-gapped mode. See the [Egress documentation](/langsmith/self-host-egress) for more details.

<a />

## Kubernetes

Use this [Helm chart](https://github.com/langchain-ai/helm/blob/main/charts/langgraph-cloud/README.md) to deploy an Agent Server to a Kubernetes cluster. This is the recommended setup for production standalone server deployments.

The Helm chart (v0.2.6+) supports MongoDB checkpointing with a bundled instance (dev/testing) or an external deployment (production). Set `mongo.enabled: true` in your values file. See [Configure checkpointer backend](/langsmith/configure-checkpointer#deploy-by-environment) for full configuration details.

## Docker

This `docker` example is intended for local development and testing.

Run the following `docker` command:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
docker run \
    --env-file .env \
    -p 8123:8000 \
    -e REDIS_URI="foo" \
    -e DATABASE_URI="bar" \
    -e LANGSMITH_API_KEY="baz" \
    my-image
```

<Note>
  * You need to replace `my-image` with the name of the image you built in the prerequisite steps (from `langgraph build`)

  and you should provide appropriate values for `REDIS_URI`, `DATABASE_URI`, and `LANGSMITH_API_KEY`.

  * If your application requires additional environment variables, you can pass them in a similar way.
</Note>

## Docker Compose

This Docker Compose example is intended for local development and testing.

Use the following Docker Compose file:

```yml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
volumes:
    langgraph-data:
        driver: local
services:
    langgraph-redis:
        image: redis:6
        healthcheck:
            test: redis-cli ping
            interval: 5s
            timeout: 1s
            retries: 5
    langgraph-postgres:
        image: postgres:16
        ports:
            - "5432:5432"
        environment:
            POSTGRES_DB: postgres
            POSTGRES_USER: postgres
            POSTGRES_PASSWORD: postgres
        volumes:
            - langgraph-data:/var/lib/postgresql/data
        healthcheck:
            test: pg_isready -U postgres
            start_period: 10s
            timeout: 1s
            retries: 5
            interval: 5s
    langgraph-api:
        image: ${IMAGE_NAME}
        ports:
            - "8123:8000"
        depends_on:
            langgraph-redis:
                condition: service_healthy
            langgraph-postgres:
                condition: service_healthy
        env_file:
            - .env
        environment:
            REDIS_URI: redis://langgraph-redis:6379
            LANGSMITH_API_KEY: ${LANGSMITH_API_KEY}
            DATABASE_URI: postgres://postgres:postgres@langgraph-postgres:5432/postgres?sslmode=disable
```

Run `docker compose up` with this file in the same folder.

<Accordion title="With MongoDB checkpointing">
  To store checkpoints in MongoDB instead of PostgreSQL, add a MongoDB service and configure the checkpointer backend. Set the backend to `"mongo"` in your `langgraph.json` or use the `LS_DEFAULT_CHECKPOINTER_BACKEND` environment variable. PostgreSQL is still required for all other server data.

  ```yml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  volumes:
      langgraph-data:
          driver: local
      langgraph-mongo-data:
          driver: local
  services:
      langgraph-redis:
          image: redis:6
          healthcheck:
              test: redis-cli ping
              interval: 5s
              timeout: 1s
              retries: 5
      langgraph-postgres:
          image: postgres:16
          ports:
              - "5432:5432"
          environment:
              POSTGRES_DB: postgres
              POSTGRES_USER: postgres
              POSTGRES_PASSWORD: postgres
          volumes:
              - langgraph-data:/var/lib/postgresql/data
          healthcheck:
              test: pg_isready -U postgres
              start_period: 10s
              timeout: 1s
              retries: 5
              interval: 5s
      langgraph-mongo:
          image: mongo:7
          command: ["mongod", "--replSet", "rs0"]
          ports:
              - "27017:27017"
          volumes:
              - langgraph-mongo-data:/data/db
          healthcheck:
              test: mongosh --eval "try { rs.status().ok } catch(e) { rs.initiate({_id:'rs0',members:[{_id:0,host:'langgraph-mongo:27017'}]}).ok }" --quiet
              interval: 5s
              timeout: 10s
              retries: 10
              start_period: 10s
      langgraph-api:
          image: ${IMAGE_NAME}
          ports:
              - "8123:8000"
          depends_on:
              langgraph-redis:
                  condition: service_healthy
              langgraph-postgres:
                  condition: service_healthy
              langgraph-mongo:
                  condition: service_healthy
          env_file:
              - .env
          environment:
              REDIS_URI: redis://langgraph-redis:6379
              LANGSMITH_API_KEY: ${LANGSMITH_API_KEY}
              DATABASE_URI: postgres://postgres:postgres@langgraph-postgres:5432/postgres?sslmode=disable
              LS_DEFAULT_CHECKPOINTER_BACKEND: mongo
              LS_MONGODB_URI: mongodb://langgraph-mongo:27017/langgraph?replicaSet=rs0
  ```

  See [Configure checkpointer backend](/langsmith/configure-checkpointer) for more details on MongoDB configuration options.
</Accordion>

This will launch an Agent Server on port `8123` (change the port mapping in `langgraph-api` if needed). Test if the application is healthy:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl --request GET --url 0.0.0.0:8123/ok
```

Assuming everything is running correctly, you should see a response like:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{"ok":true}
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/deploy-standalone-server.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Deploy on Cloud
Source: https://docs.langchain.com/langsmith/deploy-to-cloud

Create and manage LangSmith Cloud deployments including revisions, logs, metrics, and settings.

This is the comprehensive setup and management guide for deploying applications to LangSmith Cloud. LangSmith Cloud runs on AWS and GCP (see the [Cloud overview page](/langsmith/cloud) for region details). This guide covers two deployment methods: the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-deploy-to-cloud), which deploys from a connected GitHub repository, and the [`langgraph deploy` CLI command](/langsmith/cli#deploy), which builds and pushes directly from your local machine.

<Callout icon="bolt">
  **If you're looking for a quick setup**, try the [quickstart guide](/langsmith/deployment-quickstart) first.
</Callout>

Before setting up, review the [Cloud overview page](/langsmith/cloud) to understand the Cloud hosting model.

## Prerequisites

* A LangSmith account on the [Plus plan or above](https://www.langchain.com/pricing).
* [Verify that the LangGraph API runs locally](/langsmith/local-dev-testing). If the API does not run successfully (i.e., `langgraph dev`), deploying to LangSmith will fail as well.

## Create new deployment

Choose the deployment method that fits your workflow—the LangSmith UI connects to a GitHub repository and supports automatic deploys on push, while the `langgraph deploy` CLI command builds and deploys directly from your local project directory.

<Tabs>
  <Tab title="LangSmith UI">
    <Note>
      **One-Time Setup Required**: A GitHub organization owner or admin must complete the OAuth flow in the LangSmith UI to authorize the `hosted-langserve` GitHub app. This only needs to be done once per workspace. After the initial OAuth authorization, all developers with deployment permissions can create and manage deployments without requiring GitHub admin access.
    </Note>

    Starting from the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-deploy-to-cloud), select **Deployments** in the left-hand navigation panel, **Deployments**. In the top-right corner, select **+ New Deployment** to create a new deployment:

    1. In the **Create New Deployment** panel, fill out the required fields. For **Deployment details**:
       1. Select **Import from GitHub** and follow the GitHub OAuth workflow to install and authorize LangChain's `hosted-langserve` GitHub app to access the selected repositories. After installation is complete, return to the **Create New Deployment** panel and select the GitHub repository to deploy from the dropdown menu.
          <Note> The GitHub user installing LangChain's `hosted-langserve` GitHub app must be an [owner](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#organization-owners) of the organization or account. This authorization only needs to be completed once per LangSmith workspace—subsequent deployments can be created by any user with deployment permissions.</Note>
       2. Specify a name for the deployment.
       3. Specify the desired **Git Branch**. A deployment is linked to a branch. When a new revision is created, code for the linked branch will be deployed. The branch can be updated later in the [Deployment Settings](#deployment-settings).
       4. Specify the full path to the [LangGraph API config file](/langsmith/cli#configuration-file) including the file name. For example, if the file `langgraph.json` is in the root of the repository, specify `langgraph.json`.
       5. Use the checkbox to **Automatically update deployment on push to branch**. If checked, the deployment will automatically be updated when changes are pushed to the specified **Git Branch**. You can enable or disable this setting on the [Deployment Settings](#deployment-settings) in [the UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-deploy-to-cloud).
          For **Deployment Type**:
          * Development deployments are meant for non-production use cases and are provisioned with minimal resources.
          * Production deployments can serve up to 500 requests/second and are provisioned with highly available storage with automatic backups.
       6. Determine if the deployment should be **Shareable through Studio**.
          1. If unchecked, the deployment will only be accessible with a valid LangSmith API key for the [workspace](/langsmith/administration-overview#workspaces).
          2. If checked, the deployment will be accessible through [Studio](/langsmith/studio) to any LangSmith user. A direct URL to Studio for the deployment will be provided to share with other LangSmith users.
       7. Specify **Environment Variables** and secrets. To configure additional variables for the deployment, refer to the [Environment Variables reference](/langsmith/env-var).
          1. Sensitive values such as API keys (e.g., `OPENAI_API_KEY`) should be specified as secrets.
          2. Additional non-secret environment variables can be specified as well.
       8. A new LangSmith [tracing project](/langsmith/observability) is automatically created with the same name as the deployment.
    2. In the top-right corner, select **Submit**. After a few seconds, the **Deployment** view appears and the new deployment will be queued for provisioning.
  </Tab>

  <Tab title="LangGraph CLI">
    <Note>
      The `langgraph deploy` command is in **beta**. It requires [Docker](https://docs.docker.com/get-docker/) to be installed and running. On Apple Silicon (M1/M2/M3), [Docker Buildx](https://docs.docker.com/build/install-buildx/) is also required for cross-compiling to `linux/amd64`.
    </Note>

    1. Install the [LangGraph CLI](/langsmith/cli):
       ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
       uv tool install langgraph-cli
       ```
    2. Add your LangSmith API key to a `.env` file in your project root:
       ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
       LANGSMITH_API_KEY=lsv2_...
       ```
    3. Run the deploy command from your project directory:
       ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
       langgraph deploy
       ```
       This creates a `dev` deployment named after your project directory. Use `--name` to specify a different name or `--deployment-type prod` for a production deployment:
       ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
       langgraph deploy --name my-agent --deployment-type prod
       ```
       After the command completes, the deployment is queued for provisioning. Environment variables can be managed through the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-deploy-to-cloud) after the deployment is created, or configured in the [`env` field of your `langgraph.json`](/langsmith/cli#configuration-file).
  </Tab>
</Tabs>

## Create new revision

When [creating a new deployment](#create-new-deployment), a new revision is created by default. You can create subsequent revisions to deploy new code changes.

<Tabs>
  <Tab title="LangSmith UI">
    Starting from the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-deploy-to-cloud), select **Deployments** in the left-hand navigation panel. Select an existing deployment to create a new revision for.

    1. In the **Deployment** view, in the top-right corner, select **+ New Revision**.
    2. In the **New Revision** modal, fill out the required fields.
       1. Specify the full path to the [API config file](/langsmith/cli#configuration-file) including the file name. For example, if the file `langgraph.json` is in the root of the repository, specify `langgraph.json`.
       2. Determine if the deployment should be **Shareable through Studio**.
          * If unchecked, the deployment will only be accessible with a valid LangSmith API key for the [workspace](/langsmith/administration-overview#workspaces).
          * If checked, the deployment will be accessible through [Studio](/langsmith/studio) to any LangSmith user. A direct URL to Studio for the deployment will be provided to share with other LangSmith users.
       3. Specify **Environment Variables** and secrets. Existing secrets and environment variables are prepopulated. To configure additional variables for the revision, refer to the [Environment Variables reference](/langsmith/env-var).
          1. Add new secrets or environment variables.
          2. Remove existing secrets or environment variables.
          3. Update the value of existing secrets or environment variables.
    3. Select **Submit**. After a few seconds, the **New Revision** modal will close and the new revision will be queued for deployment.
  </Tab>

  <Tab title="LangGraph CLI">
    Re-run `langgraph deploy` from your project directory. The command finds the existing deployment by name and creates a new revision with your latest code changes:

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    langgraph deploy
    ```

    To target a specific deployment by ID rather than by name, use `--deployment-id`:

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    langgraph deploy --deployment-id <DEPLOYMENT_ID>
    ```

    Use `langgraph deploy list` to view all deployments and find their IDs:

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    langgraph deploy list
    ```

    <Note>
      `langgraph deploy` can only update deployments that were originally created by `langgraph deploy`. Deployments created through the LangSmith UI or GitHub integration cannot be updated with this command.
    </Note>
  </Tab>
</Tabs>

## View build and server logs

Build and server logs are available for each revision.

<Tabs>
  <Tab title="LangSmith UI">
    Starting from the **Deployments** view:

    1. Select the desired revision from the **Revisions** table. A panel slides open from the right-hand side and the **Build** tab is selected by default, which displays build logs for the revision.
    2. In the panel, select the **Server** tab to view server logs for the revision. Server logs are only available after a revision has been deployed.
    3. Within the **Server** tab, adjust the date/time range picker as needed. By default, the date/time range picker is set to the **Last 7 days**.
  </Tab>

  <Tab title="LangGraph CLI">
    Use `langgraph deploy logs` to fetch logs for a deployment.

    To view server (runtime) logs:

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    langgraph deploy logs
    ```

    To view build logs:

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    langgraph deploy logs --type build
    ```

    To tail logs continuously as they arrive:

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    langgraph deploy logs --follow
    ```

    Filter logs by time range, log level, or search string:

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    langgraph deploy logs --start-time 2026-03-01T00:00:00Z --level ERROR
    ```

    If you have multiple deployments, specify the target by name or ID:

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    langgraph deploy logs --name my-agent
    langgraph deploy logs --deployment-id <DEPLOYMENT_ID>
    ```

    For all available options, refer to the [`deploy logs` CLI reference](/langsmith/cli#deploy-logs).
  </Tab>
</Tabs>

## View deployment metrics

Once your deployment is live, you can monitor its performance from the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-deploy-to-cloud).

Starting from the LangSmith UI:

1. In the left-hand navigation panel, select **Deployments**.
2. Select an existing deployment to monitor.
3. Select the **Monitoring** tab to view the deployment metrics. Refer to a list of [all available metrics](/langsmith/control-plane#monitoring).
4. Within the **Monitoring** tab, use the date/time range picker as needed. By default, the date/time range picker is set to the **Last 15 minutes**.

## Interrupt revision

Interrupting a revision will stop deployment of the revision.

<Warning>
  **Undefined Behavior**
  Interrupted revisions have undefined behavior. This is only useful if you need to deploy a new revision and you already have a revision "stuck" in progress. In the future, this feature may be removed.
</Warning>

Starting from the **Deployments** view:

1. Select the menu icon (three dots) on the right-hand side of the row for the desired revision from the **Revisions** table.
2. Select **Interrupt** from the menu.
3. A modal will appear. Review the confirmation message. Select **Interrupt revision**.

## Delete deployment

<Tabs>
  <Tab title="LangSmith UI">
    Starting from the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-deploy-to-cloud):

    1. In the left-hand navigation panel, select **Deployments**, which contains a list of existing deployments.
    2. Select the menu icon (three dots) on the right-hand side of the row for the desired deployment and select **Delete**.
    3. A **Confirmation** modal will appear. Select **Delete**.
  </Tab>

  <Tab title="LangGraph CLI">
    Use `langgraph deploy list` to find the ID of the deployment you want to delete:

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    langgraph deploy list
    ```

    Then delete it by ID:

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    langgraph deploy delete <DEPLOYMENT_ID>
    ```

    To skip the confirmation prompt, use `--force`:

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    langgraph deploy delete --force <DEPLOYMENT_ID>
    ```
  </Tab>
</Tabs>

## Deployment settings

Starting from the **Deployments** view:

1. In the top-right corner, select the gear icon (**Deployment Settings**).
2. Update the `Git Branch` to the desired branch.
3. Check/uncheck checkbox to **Automatically update deployment on push to branch**.
   1. Branch creation/deletion and tag creation/deletion events will not trigger an update. Only pushes to an existing branch will trigger an update.
   2. Pushes in quick succession to a branch will queue subsequent updates. Once a build completes, the most recent commit will begin building and the other queued builds will be skipped.

## Add or remove GitHub repositories

After installing and authorizing LangChain's `hosted-langserve` GitHub app, repository access for the app can be modified to add new repositories or remove existing repositories. If a new repository is created, it may need to be added explicitly.

1. From the GitHub profile, navigate to **Settings** > **Applications** > `hosted-langserve` > click **Configure**.
2. Under **Repository access**, select **All repositories** or **Only select repositories**. If **Only select repositories** is selected, new repositories must be explicitly added.
3. Click **Save**.
4. When creating a new deployment, the list of GitHub repositories in the dropdown menu will be updated to reflect the repository access changes.

## Allowlist IP addresses

All traffic from LangSmith deployments created after January 6th 2025 will come through a NAT gateway.
This NAT gateway will have several static IP addresses depending on the region you are deploying in. Refer to the table below for the list of IP addresses to allowlist:

| GCP US         | GCP EU         | GCP APAC       | AWS US        |
| -------------- | -------------- | -------------- | ------------- |
| 35.197.29.146  | 34.90.213.236  | 34.40.236.16   | 3.13.80.97    |
| 34.145.102.123 | 34.13.244.114  | 34.40.140.88   | 3.146.216.198 |
| 34.169.45.153  | 34.32.180.189  | 34.151.88.209  | 16.59.72.244  |
| 34.82.222.17   | 34.34.69.108   | 35.189.51.120  |               |
| 35.227.171.135 | 34.32.145.240  | 34.40.172.39   |               |
| 34.169.88.30   | 34.90.157.44   | 35.189.56.87   |               |
| 34.19.93.202   | 34.141.242.180 | 35.189.17.201  |               |
| 34.19.34.50    | 34.32.141.108  | 35.244.99.196  |               |
| 34.59.244.194  | 34.12.178.175  | 34.40.149.177  |               |
| 34.9.99.224    | 34.91.192.230  | 34.40.144.104  |               |
| 34.68.27.146   | 34.32.209.237  | 34.151.130.182 |               |
| 34.41.178.137  | 34.178.128.69  | 34.116.82.199  |               |
| 34.123.151.210 |                |                |               |
| 34.135.61.140  |                |                |               |
| 34.121.166.52  |                |                |               |
| 34.31.121.70   |                |                |               |

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/deploy-to-cloud.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Deploy with control plane
Source: https://docs.langchain.com/langsmith/deploy-with-control-plane

Build Docker images and deploy applications to a self-hosted LangSmith instance using the control plane UI.

<Info>
  **This guide is for self-hosted LangSmith customers** who have [enabled LangSmith Deployment](/langsmith/deploy-self-hosted-full-platform#enable-langsmith-deployment) on their instance. For Cloud customers, see [Deploy on Cloud](/langsmith/deploy-to-cloud). For standalone Agent Servers without a control plane, see [Self-host standalone servers](/langsmith/deploy-standalone-server).
</Info>

This guide shows you how to deploy your applications to a [self-hosted](/langsmith/self-hosted) LangSmith instance using a [control plane](/langsmith/control-plane). With a control plane, you build Docker images locally, push them to a registry that your Kubernetes cluster has access to, and deploy them with the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-deploy-with-control-plane).

## Overview

Applications deployed to a self-hosted LangSmith instance with a control plane use Docker images. In this guide, the application deployment workflow is:

1. Test your application locally using `langgraph dev` or [Studio](/langsmith/studio).
2. Build a Docker image using the `langgraph build` command.
3. Push the image to a container registry accessible by your infrastructure.
4. Deploy from the [control plane UI](/langsmith/control-plane#control-plane-ui) by specifying the image URL.

## Prerequisites

Before completing this guide, you'll need the following:

* [LangSmith Deployment enabled](/langsmith/deploy-self-hosted-full-platform#enable-langsmith-deployment) on your self-hosted LangSmith instance.
* Access to the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-deploy-with-control-plane) with LangSmith Deployment enabled.
* A container registry accessible by your Kubernetes cluster. If using a private registry that requires authentication, you must configure image pull secrets as part of your infrastructure setup. Refer to [Private registry authentication](#private-registry-authentication).

## Step 1. Test locally

Before deploying, test your application locally. You can use the [LangGraph CLI](/langsmith/cli#dev) to run an Agent server in development mode:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langgraph dev
```

For a full guide local testing, refer to the [Local server quickstart](/langsmith/local-dev-testing).

## Step 2. Build Docker image

Build a Docker image of your application using the [`langgraph build`](/langsmith/cli#build) command:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langgraph build -t my-image
```

Build command options include:

| Option               | Default          | Description                                                       |
| -------------------- | ---------------- | ----------------------------------------------------------------- |
| `-t, --tag TEXT`     | Required         | Tag for the Docker image                                          |
| `--platform TEXT`    |                  | Target platform(s) to build for (e.g., `linux/amd64,linux/arm64`) |
| `--pull / --no-pull` | `--pull`         | Build with latest remote Docker image                             |
| `-c, --config FILE`  | `langgraph.json` | Path to configuration file                                        |

Example with platform specification:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langgraph build --platform linux/amd64 -t my-image:v1.0.0
```

For full details, see the [CLI reference](/langsmith/cli#build).

## Step 3. Push to container registry

Push your image to a container registry accessible by your Kubernetes cluster. The specific commands depend on your registry provider.

<Tip>
  Tag your images with version information (e.g., `my-registry.com/my-app:v1.0.0`) to make rollbacks easier.
</Tip>

## Step 4. Deploy with the control plane UI

The [control plane UI](/langsmith/control-plane#control-plane-ui) allows you to create and manage deployments, view logs and metrics, and update configurations. To create a new deployment in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-deploy-with-control-plane):

1. In the left-hand navigation panel, select **Deployments**.
2. In the top-right corner, select **+ New Deployment**.
3. In the deployment configuration panel, provide:
   * **Image URL**: The full image URL you pushed in [Step 3](#step-3-push-to-container-registry).
   * **Listener/Compute ID**: Select the listener configured for your infrastructure.
   * **Namespace**: The Kubernetes namespace to deploy to.
   * **Environment variables**: Any required configuration (API keys, etc.).
   * Other deployment settings as needed.
4. Select **Submit**.

The control plane will coordinate with your [data plane](/langsmith/data-plane) listener to deploy your application.

After creating a deployment, the infrastructure is [provisioned asynchronously](/langsmith/control-plane#asynchronous-deployment). Deployment can take up to several minutes, with initial deployments taking longer due to database creation.

From the control plane UI, you can view build logs, server logs, and deployment metrics including CPU/memory usage, replicas, and API performance. For more details, refer to the [control plane monitoring documentation](/langsmith/control-plane#monitoring).

<Note>
  A [LangSmith Observability tracing project](/langsmith/observability) is automatically created for each deployment with the same name as the deployment. Tracing environment variables are set automatically by the control plane.
</Note>

## Update deployment

To deploy a new version of your application, create a [new revision](/langsmith/control-plane#revisions):

Starting from the LangSmith UI:

1. In the left-hand navigation panel, select **Deployments**.
2. Select an existing deployment.
3. In the Deployment view, select **+ New Revision** in the top-right corner.
4. Update the configuration:
   * Update the **Image URL** to your new image version.
   * Update environment variables if needed.
   * Adjust other settings as needed.
5. Select **Submit**.

## Private registry authentication

If your container registry requires authentication (e.g., AWS ECR, Azure ACR, GCP Artifact Registry, private Docker registry), you must configure Kubernetes image pull secrets before deploying applications. This is a one-time infrastructure configuration.

<Note>
  **This configuration is done at the infrastructure level, not per-deployment.** Once configured, all deployments automatically inherit the registry credentials.
</Note>

Configure `imagePullSecrets` in your LangSmith Helm chart's `values.yaml` file. See the detailed steps in the [Enable LangSmith Deployment guide](/langsmith/deploy-self-hosted-full-platform#enable-langsmith-deployment).

For detailed steps on creating image pull secrets for different registry providers, refer to the [Kubernetes documentation on pulling images from private registries](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/).

## Next steps

* **[Control plane](/langsmith/control-plane)**: Learn more about control plane features.
* **[Data plane](/langsmith/data-plane)**: Understand data plane architecture.
* **[Observability](/langsmith/observability)**: Monitor your deployments with automatic tracing.
* **[Studio](/langsmith/studio)**: Test and debug deployed applications.
* **[LangGraph CLI](/langsmith/cli)**: Full CLI reference documentation.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/deploy-with-control-plane.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith Deployment
Source: https://docs.langchain.com/langsmith/deployment

Deploy and manage agents with durable execution, real-time streaming, and horizontal scaling.

<div>
  <div>
    # LangSmith Deployment

    LangSmith Deployment is a workflow orchestration runtime purpose-built for agent workloads. It provides the managed infrastructure agents need to run reliably in production at scale, supporting the full lifecycle from local development to deployment.

    ## Get started

    <Steps>
      <Step title="Create an account" icon="user-plus">
        Sign up at [smith.langchain.com](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=snippets-langsmith-account-api-key-quickstart) (no credit card required).
        You can log in with **Google**, **GitHub**, or **email**.
      </Step>

      <Step title="Create an API key" icon="key">
        Go to your [Settings page](https://smith.langchain.com/settings) → **API Keys** → **Create API Key**.
        Copy the key and save it securely.
      </Step>
    </Steps>

    Once your account and API key are ready, [deploy your first agent](/langsmith/deployment-quickstart).

    ## Deployable products

    LangSmith Deployment is framework-agnostic which means you can deploy agents built with:

    <CardGroup>
      <Card title="Deep Agents" href="/langsmith/managed-deep-agents-overview" icon="robot">
        Create, run, and operate Managed Deep Agents through the private preview API.
      </Card>

      <Card title="LangGraph (and LangChain)" href="/langsmith/deployment-quickstart" icon="chart-dots-3">
        Use the LangGraph CLI and app templates to deploy a LangGraph application to LangSmith.
      </Card>

      <Card title="Google ADK" href="/langsmith/deploy-google-adk" icon="google">
        Deploy Google Agent Development Kit (ADK) agent as a LangGraph with the `deployments-wrap-sdk` package.
      </Card>

      <Card title="Other frameworks" href="/langsmith/deploy-other-frameworks" icon="packages">
        Use the LangGraph Functional API to deploy Strands, CrewAI, and other agent frameworks.
      </Card>
    </CardGroup>

    ## Deployment environments

    You can run the same [Agent Server](/langsmith/agent-server) runtime in several hosting models. A **standalone server** is the lightest option: you run containers yourself without the LangSmith [control plane](/langsmith/control-plane). For managed deployments through the UI and APIs, use **Cloud** or **Self-hosted** (full platform in your infrastructure).

    <CardGroup>
      <Card title="Cloud" href="/langsmith/deploy-to-cloud" icon="cloud">
        Fully managed by LangChain, running on AWS and GCP. Create deployments from GitHub in the LangSmith UI or with [`langgraph deploy`](/langsmith/cli#deploy). Requires a [Plus plan or above](https://www.langchain.com/pricing).
      </Card>

      <Card title="Standalone server" href="/langsmith/deploy-standalone-server" icon="server">
        Deploy Agent Server with Docker, Compose, or Kubernetes. Bring your own PostgreSQL, Redis, and LangSmith license; no control plane. Optional [LangSmith tracing](/langsmith/observability) to Cloud or a self-hosted instance.
      </Card>

      <Card title="Self-hosted" href="/langsmith/self-hosted" icon="buildings">
        Run the full LangSmith platform, including the control plane and data plane, in your cloud (for example on Kubernetes). Requires [Enterprise plan](https://www.langchain.com/pricing). Integrates observability, evaluation, and agent deployment in one private stack.
      </Card>
    </CardGroup>

    Same runtime, same APIs. What changes is who manages the infrastructure.
    For a feature-level comparison and infrastructure setup, see [Platform setup](/langsmith/platform-setup).

    ## Deployment capabilities

    Once an agent is deployed, you work with [Agent Server](/langsmith/assistants)’s execution model: **assistants** for configuration, **threads** for state, and **runs** for workloads.

    <CardGroup>
      <Card title="Core capabilities" href="/langsmith/streaming" icon="bolt">
        Stream to users, pause for human review, handle concurrent input, and connect via MCP and A2A.
      </Card>

      <Card title="Studio" href="/langsmith/studio" icon="window">
        Use an interactive environment for developing and debugging agents.
      </Card>

      <Card title="Advanced configuration" href="/langsmith/auth" icon="lock">
        Authentication, encryption, custom routes, and short- and long-term memory stores.
      </Card>

      <Card title="Agent composition" href="/langsmith/use-remote-graph" icon="book">
        RemoteGraph lets any agent call other deployed agents with MCP and A2A.
      </Card>
    </CardGroup>

    <Card title="Find and fix failures with Engine" icon="https://mintcdn.com/langchain-5e9cc07a/auWE6_dMRp183OCf/images/brand/engine-icon-no-bg-dark.svg?fit=max&auto=format&n=auWE6_dMRp183OCf&q=85&s=dd41aef3ce789c1a04ea3c37b5903eac" href="/langsmith/engine-overview">
      Once agents are in production, use LangSmith Engine to detect recurring failures in their traces, diagnose root causes, and resolve them.
    </Card>

    ### Reference & operations

    #### Tutorials

    * [Collect user feedback for Agent Server runs](/langsmith/agent-server-feedback): Attach end-user feedback to runs and traces
    * [Deploy other frameworks (e.g., Strands, CrewAI)](/langsmith/deploy-other-frameworks): Wrap existing agents with Functional API and deploy
    * [Implement generative user interfaces with LangGraph](/langsmith/generative-ui-react): Stream UI elements to a React client
    * [Implement a CI/CD pipeline](/langsmith/cicd-pipeline-example): Automate tests, evaluations, and deployments with GitHub Actions

    #### Securing and customizing your server

    * [Custom auth](/langsmith/auth): Authentication and multi-tenant access control
    * [Server customization](/langsmith/custom-routes): Custom routes, [middleware](/langsmith/custom-middleware), [lifespan hooks](/langsmith/custom-lifespan), [encryption](/langsmith/encryption)

    #### Operations

    * [CI/CD pipelines](/langsmith/cicd-pipeline-example)
    * [TTL configuration](/langsmith/configure-ttl) for state and thread management
    * [Semantic search](/langsmith/semantic-search)
  </div>
</div>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/deployment.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
