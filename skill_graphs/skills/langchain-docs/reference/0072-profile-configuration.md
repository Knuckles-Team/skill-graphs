# Profile configuration
Source: https://docs.langchain.com/langsmith/profile-configuration

Configure LangSmith SDK credentials and endpoints with a local profile file.

LangSmith SDK profiles let you keep [API keys](/langsmith/create-account-api-key), endpoints, and workspace IDs in a reusable JSON file instead of setting the same environment variables in every shell session.

Use profiles when you switch between [LangSmith Cloud regions](/langsmith/cloud#regional-storage), self-hosted instances, or [workspaces](/langsmith/administration-overview#workspaces) often, or when you want a remote runtime to load the same SDK configuration from a mounted file.

<Warning>
  Profile files can contain API keys and OAuth refresh tokens. Do not commit them to source control, bake them into container images, or print them in logs. Store and mount them with the same care as other credentials.
</Warning>

## Minimum versions

Profile support is available in the following releases:

| Tool or SDK                    | Minimum version |
| ------------------------------ | --------------- |
| LangSmith CLI profile commands | `v0.2.26`       |
| `langsmith auth login`         | `v0.2.30`       |
| Go SDK                         | `v0.7.0`        |
| Python SDK                     | `v0.8.1`        |
| TypeScript SDK                 | `v0.6.1`        |
| Java SDK                       | `v0.1.0-beta.3` |

## Profile file location

By default, [SDKs](/langsmith/reference) look for a profile file at:

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
~/.langsmith/config.json
```

To use a different path, set `LANGSMITH_CONFIG_FILE`:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_CONFIG_FILE=/path/to/langsmith-config.json
```

The TypeScript SDK only loads profiles in Node.js-like runtimes. Browser and web worker runtimes do not have filesystem access, so pass configuration explicitly in those environments.

## Create a profile file

Create `~/.langsmith/config.json` with a `profiles` object. Each profile can define:

| Field          | Description                                                                                |
| -------------- | ------------------------------------------------------------------------------------------ |
| `api_url`      | LangSmith API endpoint. Use the same value you would use for `LANGSMITH_ENDPOINT`.         |
| `api_key`      | LangSmith API key. See [Create an account and API key](/langsmith/create-account-api-key). |
| `workspace_id` | Workspace ID. Required when the API key can access multiple workspaces.                    |
| `oauth`        | OAuth token metadata created by LangSmith tooling.                                         |

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "current_profile": "dev",
  "profiles": {
    "dev": {
      "api_url": "https://api.smith.langchain.com",
      "api_key": "<LANGSMITH_API_KEY>",
      "workspace_id": "<WORKSPACE_ID>"
    },
    "eu": {
      "api_url": "https://eu.api.smith.langchain.com",
      "api_key": "<EU_LANGSMITH_API_KEY>",
      "workspace_id": "<EU_WORKSPACE_ID>"
    },
    "apac": {
      "api_url": "https://apac.api.smith.langchain.com",
      "api_key": "<APAC_LANGSMITH_API_KEY>",
      "workspace_id": "<APAC_WORKSPACE_ID>"
    }
  }
}
```

Restrict the file so only your user can read it:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
chmod 600 ~/.langsmith/config.json
```

## Select a profile

SDKs select profiles in this order:

1. `LANGSMITH_PROFILE`, if set.
2. `current_profile` in the profile file, if set.
3. A profile named `default`, if present.

For example:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_PROFILE=eu
```

The [LangSmith CLI](/langsmith/langsmith-cli) also accepts a global `--profile` flag, which takes precedence over `LANGSMITH_PROFILE` for that command:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith --profile eu project list
```

## Manage profiles with the CLI

Use the [LangSmith CLI](/langsmith/langsmith-cli) to create, inspect, switch, and delete profiles without editing the JSON file by hand.

To create an API-key profile from an existing API key:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_API_KEY=<LANGSMITH_API_KEY>
langsmith profile create dev \
  --workspace-id <WORKSPACE_ID> \
  --set-current
```

You can also pass the key and endpoint as flags. Prefer environment variables on shared machines, because shell history may record command flags.

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith profile create eu \
  --api-key <EU_LANGSMITH_API_KEY> \
  --api-url https://eu.api.smith.langchain.com \
  --workspace-id <EU_WORKSPACE_ID>
```

Common profile commands:

| Command                                          | Description                                                 |
| ------------------------------------------------ | ----------------------------------------------------------- |
| `langsmith profile list`                         | List saved profiles. Alias: `langsmith profile ls`.         |
| `langsmith profile show <name>`                  | Show a saved profile. Secret values are redacted in output. |
| `langsmith profile use <name>`                   | Set `current_profile` in the profile file.                  |
| `langsmith profile set-workspace <workspace-id>` | Set the default workspace for the selected profile.         |
| `langsmith profile delete <name>`                | Delete a saved profile.                                     |

Use `--format pretty` for human-readable tables:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith --format pretty profile list
```

## Authenticate with `langsmith auth login`

Run `langsmith auth login` to authenticate with OAuth instead of manually creating an API-key profile. The command starts a browser-based device authorization flow, stores OAuth tokens in the selected profile, and sets that profile as current.

<Note>
  `langsmith auth login` currently supports LangSmith Cloud (SaaS) only. For self-hosted or other non-SaaS LangSmith endpoints, create an API-key profile instead.
</Note>

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith auth login
```

Choose the profile with `--profile` or `LANGSMITH_PROFILE`:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith auth login --profile dev
```

For a headless environment, suppress automatic browser opening and pass a workspace ID:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langsmith auth login \
  --profile prod \
  --no-browser \
  --workspace-id <WORKSPACE_ID>
```

`langsmith auth login` chooses the profile name in this order:

1. `--profile`, if passed.
2. `LANGSMITH_PROFILE`, if set.
3. `current_profile` in the profile file, if set.
4. `default`.

It chooses the API URL in this order:

1. `--api-url`, if passed.
2. `LANGSMITH_ENDPOINT`, if set.
3. The selected profile's `api_url`, if present.
4. The default LangSmith Cloud endpoint.

After login, the CLI and SDKs can use the saved profile. The CLI refreshes OAuth tokens when needed and writes refreshed token fields back to the profile file. SDKs also use the OAuth access token from the profile when environment or constructor API-key auth is not set.

## Override profile values

Explicit client constructor arguments and environment variables take precedence over profile values.

| Setting        | Precedence                                                                                                                       |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Endpoint       | Constructor `api_url` or `apiUrl`, then `LANGSMITH_ENDPOINT`, then profile `api_url`, then the default LangSmith Cloud endpoint. |
| Authentication | Constructor API key, then `LANGSMITH_API_KEY`, then profile OAuth access token, then profile `api_key`.                          |
| Workspace      | Constructor `workspace_id` or `workspaceId`, then `LANGSMITH_WORKSPACE_ID`, then profile `workspace_id`.                         |

The older `LANGCHAIN_API_KEY`, `LANGCHAIN_ENDPOINT`, and `LANGCHAIN_WORKSPACE_ID` aliases still work, but prefer the `LANGSMITH_*` names for new configuration.

If a profile contains both `oauth.access_token` and `api_key`, SDKs use the OAuth access token first. If an OAuth refresh token is present and the access token is expired or close to expiring, SDKs can refresh the token and write the updated token fields back to the profile file.

<Note>
  If you mount a profile file as read-only, OAuth token refresh cannot persist updated tokens. Read-only mounts are appropriate for API-key profiles. Use a writable mount only when you intentionally rely on OAuth token refresh.
</Note>

## Use profiles in code

When the profile file is present, create the client normally:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client

  client = Client()
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  const client = new Client();
  ```
</CodeGroup>

To override a profile in code, pass the value explicitly:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import Client

  client = Client(api_key="<LANGSMITH_API_KEY>")
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Client } from "langsmith";

  const client = new Client({ apiKey: "<LANGSMITH_API_KEY>" });
  ```
</CodeGroup>

## Mount profiles in remote runtimes

For remote runtimes, mount the profile file as a secret file and set `LANGSMITH_CONFIG_FILE` to the mounted path. Do not copy the file into the image or repository.

### Docker

Mount your local profile directory into the container:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
docker run --rm \
  -e LANGSMITH_CONFIG_FILE=/home/app/.langsmith/config.json \
  -e LANGSMITH_PROFILE=prod \
  -v "$HOME/.langsmith:/home/app/.langsmith:ro" \
  my-image
```

Use a read-write mount only when the profile uses OAuth refresh tokens:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
docker run --rm \
  -e LANGSMITH_CONFIG_FILE=/home/app/.langsmith/config.json \
  -e LANGSMITH_PROFILE=prod \
  -v "$HOME/.langsmith:/home/app/.langsmith" \
  my-image
```

### Kubernetes

Create a Kubernetes secret from the profile file:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
kubectl create secret generic langsmith-profile \
  --from-file=config.json="$HOME/.langsmith/config.json"
```

Mount the secret and point the SDK to it:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app
spec:
  template:
    spec:
      containers:
        - name: app
          image: my-image
          env:
            - name: LANGSMITH_CONFIG_FILE
              value: /var/run/langsmith/config.json
            - name: LANGSMITH_PROFILE
              value: prod
          volumeMounts:
            - name: langsmith-profile
              mountPath: /var/run/langsmith
              readOnly: true
      volumes:
        - name: langsmith-profile
          secret:
            secretName: langsmith-profile
```

Kubernetes secret volumes are read-only. Use API-key profiles for this pattern, or use a writable secret-sync mechanism if your OAuth profile must refresh and persist tokens.

### Remote development and CI

In remote development environments or CI jobs, store the profile JSON in the platform's secret store, write it to a temporary file at runtime, and set `LANGSMITH_CONFIG_FILE` to that file path.

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
mkdir -p "$RUNNER_TEMP/langsmith"
printf '%s' "$LANGSMITH_PROFILE_JSON" > "$RUNNER_TEMP/langsmith/config.json"
chmod 600 "$RUNNER_TEMP/langsmith/config.json"
export LANGSMITH_CONFIG_FILE="$RUNNER_TEMP/langsmith/config.json"
export LANGSMITH_PROFILE=prod
```

For hosted LangSmith Cloud deployments, configure these values as deployment environment variables or workspace secrets unless the platform explicitly supports mounting secret files.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/profile-configuration.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# How to sync prompts with GitHub
Source: https://docs.langchain.com/langsmith/prompt-commit

LangSmith provides a collaborative interface to create, test, and iterate on prompts.

While you can [dynamically fetch prompts](/langsmith/manage-prompts-programmatically#pull-a-prompt) from LangSmith into your application at runtime, you may prefer to sync prompts with your own database or version control system. To support this workflow, LangSmith allows you to receive notifications of prompt updates via webhooks.

**Why sync prompts with GitHub?**

* **Version Control:** Keep your prompts versioned alongside your application code in a familiar system.
* **CI/CD Integration:** Trigger automated staging or production deployments when critical prompts change.

<img alt="Prompt Webhook Diagram" />

## Prerequisites

Before we begin, ensure you have the following set up:

1. **GitHub Account:** A standard GitHub account.

2. **GitHub Repository:** Create a new (or choose an existing) repository where your LangSmith prompt manifests will be stored. This could be the same repository as your application code or a dedicated one for prompts.

3. **GitHub Personal Access Token (PAT):**

   * LangSmith webhooks don't directly interact with GitHub—they call an intermediary server that *you* create.
   * This server requires a GitHub PAT to authenticate and make commits to your repository.
   * Must include the `repo` scope (`public_repo` is sufficient for public repositories).
   * Go to **GitHub > Settings > Developer settings > Personal access tokens > Tokens (classic)**.
   * Click **Generate new token (classic)**.
   * Name it (e.g., "LangSmith Prompt Sync"), set an expiration, and select the required scopes.
   * Click **Generate token** and **copy it immediately** — it won't be shown again.
   * Store the token securely and provide it as an environment variable to your server.

## Understanding LangSmith "Prompt commits" and webhooks

In LangSmith, when you save changes to a prompt, you're essentially creating a new version or a "Prompt Commit." These commits are what can trigger webhooks.

The webhook will send a JSON payload containing the new **prompt manifest**.

<Accordion title="Sample Webhook Payload">
  ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  {
    "prompt_id": "f33dcb51-eb17-47a5-83ca-64ac8a027a29",
    "prompt_name": "My Prompt",
    "commit_hash": "commit_hash_1234567890",
    "created_at": "2021-01-01T00:00:00Z",
    "created_by": "Jane Doe",
    "manifest": {
      "lc": 1,
      "type": "constructor",
      "id": ["langchain", "schema", "runnable", "RunnableSequence"],
      "kwargs": {
        "first": {
          "lc": 1,
          "type": "constructor",
          "id": ["langchain", "prompts", "chat", "ChatPromptTemplate"],
          "kwargs": {
            "messages": [
              {
                "lc": 1,
                "type": "constructor",
                "id": [
                  "langchain_core",
                  "prompts",
                  "chat",
                  "SystemMessagePromptTemplate"
                ],
                "kwargs": {
                  "prompt": {
                    "lc": 1,
                    "type": "constructor",
                    "id": [
                      "langchain_core",
                      "prompts",
                      "prompt",
                      "PromptTemplate"
                    ],
                    "kwargs": {
                      "input_variables": [],
                      "template_format": "mustache",
                      "template": "You are a chatbot."
                    }
                  }
                }
              },
              {
                "lc": 1,
                "type": "constructor",
                "id": [
                  "langchain_core",
                  "prompts",
                  "chat",
                  "HumanMessagePromptTemplate"
                ],
                "kwargs": {
                  "prompt": {
                    "lc": 1,
                    "type": "constructor",
                    "id": [
                      "langchain_core",
                      "prompts",
                      "prompt",
                      "PromptTemplate"
                    ],
                    "kwargs": {
                      "input_variables": ["question"],
                      "template_format": "mustache",
                      "template": "{{question}}"
                    }
                  }
                }
              }
            ],
            "input_variables": ["question"]
          }
        },
        "last": {
          "lc": 1,
          "type": "constructor",
          "id": ["langchain", "schema", "runnable", "RunnableBinding"],
          "kwargs": {
            "bound": {
              "lc": 1,
              "type": "constructor",
              "id": ["langchain", "chat_models", "openai", "ChatOpenAI"],
              "kwargs": {
                "temperature": 1,
                "top_p": 1,
                "presence_penalty": 0,
                "frequency_penalty": 0,
                "model": "gpt-5.4-mini",
                "extra_headers": {},
                "openai_api_key": {
                  "id": ["OPENAI_API_KEY"],
                  "lc": 1,
                  "type": "secret"
                }
              }
            },
            "kwargs": {}
          }
        }
      }
    }
  }
  ```
</Accordion>

<Note>
  It's important to understand that LangSmith webhooks for prompt commits are generally triggered at the **workspace level**. This means if *any* prompt within your LangSmith workspace is modified and a "prompt commit" is saved, the webhook will fire and send the updated manifest of the prompt. The payloads are identifiable by prompt id. Your receiving server should be designed with this in mind.
</Note>

## Implementing a FastAPI server for webhook reception

To effectively process webhook notifications from LangSmith when prompts are updated, an intermediary server application is necessary. This server will act as the receiver for HTTP POST requests sent by LangSmith. For demonstration purposes in this guide, we will outline the creation of a simple FastAPI application to fulfill this role.

This publicly accessible server will be responsible for:

1. **Receiving Webhook Requests:** Listening for incoming HTTP POST requests.
2. **Parsing Payloads:** Extracting and interpreting the JSON-formatted prompt manifest from the request body.
3. **Committing to GitHub:** Programmatically creating a new commit in your specified GitHub repository, containing the updated prompt manifest. This ensures your prompts remain version-controlled and synchronized with changes made in LangSmith.

For deployment, platforms like [Render.com](https://render.com/) (offering a suitable free tier), Vercel, Fly.io, or other cloud providers (AWS, GCP, Azure) can be utilized to host the FastAPI application and obtain a public URL.

The server's core functionality will include an endpoint for webhook reception, logic for parsing the manifest, and integration with the GitHub API (using a Personal Access Token for authentication) to manage commits.

<Accordion title="Minimal FastAPI Server Code ()">
  `main.py`

  This server will listen for incoming webhooks from LangSmith and commit the received prompt manifest to your GitHub repository.

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import base64
  import json
  import uuid
  from typing import Any, Dict
  import httpx
  from fastapi import FastAPI, HTTPException, Body
  from pydantic import BaseModel, Field
  from pydantic_settings import BaseSettings, SettingsConfigDict

  # --- Configuration ---
  class AppConfig(BaseSettings):
      """
      Application configuration model.
      Loads settings from environment variables.
      """
      GITHUB_TOKEN: str
      GITHUB_REPO_OWNER: str
      GITHUB_REPO_NAME: str
      GITHUB_FILE_PATH: str = "prompt_manifest.json"
      GITHUB_BRANCH: str = "main"
      model_config = SettingsConfigDict(
          env_file=".env",
          env_file_encoding='utf-8',
          extra='ignore'
      )

  settings = AppConfig()

  # --- Pydantic Models ---
  class WebhookPayload(BaseModel):
      """
      Defines the expected structure of the incoming webhook payload.
      """
      prompt_id: UUID = Field(
          ...,
          description="The unique identifier for the prompt."
      )
      prompt_name: str = Field(
          ...,
          description="The name/title of the prompt."
      )
      commit_hash: str = Field(
          ...,
          description="An identifier for the commit event that triggered the webhook."
      )
      created_at: str = Field(
          ...,
          description="Timestamp indicating when the event was created (ISO format preferred)."
      )
      created_by: str = Field(
          ...,
          description="The name of the user who created the event."
      )
      manifest: Dict[str, Any] = Field(
          ...,
          description="The main content or configuration data to be committed to GitHub."
      )

  # --- GitHub Helper Function ---
  async def commit_manifest_to_github(payload: WebhookPayload) -> Dict[str, Any]:
      """
      Helper function to commit the manifest directly to the configured branch.
      """
      github_api_base_url = "https://api.github.com"
      repo_file_url = (
          f"{github_api_base_url}/repos/{settings.GITHUB_REPO_OWNER}/"
          f"{settings.GITHUB_REPO_NAME}/contents/{settings.GITHUB_FILE_PATH}"
      )
      headers = {
          "Authorization": f"Bearer {settings.GITHUB_TOKEN}",
          "Accept": "application/vnd.github.v3+json",
          "X-GitHub-Api-Version": "2022-11-28",
      }
      manifest_json_string = json.dumps(payload.manifest, indent=2)
      content_base64 = base64.b64encode(manifest_json_string.encode('utf-8')).decode('utf-8')
      commit_message = f"feat: Update {settings.GITHUB_FILE_PATH} via webhook - commit {payload.commit_hash}"
      data_to_commit = {
          "message": commit_message,
          "content": content_base64,
          "branch": settings.GITHUB_BRANCH,
      }
      async with httpx.AsyncClient() as client:
          current_file_sha = None
          try:
              params_get = {"ref": settings.GITHUB_BRANCH}
              response_get = await client.get(repo_file_url, headers=headers, params=params_get)
              if response_get.status_code == 200:
                  current_file_sha = response_get.json().get("sha")
              elif response_get.status_code != 404: # If not 404 (not found), it's an unexpected error
                  response_get.raise_for_status()
          except httpx.HTTPStatusError as e:
              error_detail = f"GitHub API error (GET file SHA): {e.response.status_code} - {e.response.text}"
              print(f"[ERROR] {error_detail}")
              raise HTTPException(status_code=e.response.status_code, detail=error_detail)
          except httpx.RequestError as e:
              error_detail = f"Network error connecting to GitHub (GET file SHA): {str(e)}"
              print(f"[ERROR] {error_detail}")
              raise HTTPException(status_code=503, detail=error_detail)
          if current_file_sha:
              data_to_commit["sha"] = current_file_sha
          try:
              response_put = await client.put(repo_file_url, headers=headers, json=data_to_commit)
              response_put.raise_for_status()
              return response_put.json()
          except httpx.HTTPStatusError as e:
              error_detail = f"GitHub API error (PUT content): {e.response.status_code} - {e.response.text}"
              if e.response.status_code == 409: # Conflict
                  error_detail = (
                      f"GitHub API conflict (PUT content): {e.response.text}. "
                      "This might be due to an outdated SHA or branch protection rules."
                  )
              elif e.response.status_code == 422: # Unprocessable Entity
                  error_detail = (
                      f"GitHub API Unprocessable Entity (PUT content): {e.response.text}. "
                      f"Ensure the branch '{settings.GITHUB_BRANCH}' exists and the payload is correctly formatted."
                  )
              print(f"[ERROR] {error_detail}")
              raise HTTPException(status_code=e.response.status_code, detail=error_detail)
          except httpx.RequestError as e:
              error_detail = f"Network error connecting to GitHub (PUT content): {str(e)}"
              print(f"[ERROR] {error_detail}")
              raise HTTPException(status_code=503, detail=error_detail)

  # --- FastAPI Application ---
  app = FastAPI(
      title="Minimal Webhook to GitHub Commit Service",
      description="Receives a webhook and commits its 'manifest' part directly to a GitHub repository.",
      version="0.1.0",
  )

  @app.post("/webhook/commit", status_code=201, tags=["GitHub Webhooks"])
  async def handle_webhook_direct_commit(payload: WebhookPayload = Body(...)):
      """
      Webhook endpoint to receive events and commit DIRECTLY to the configured branch.
      """
      try:
          github_response = await commit_manifest_to_github(payload)
          return {
              "message": "Webhook received and manifest committed directly to GitHub successfully.",
              "github_commit_details": github_response.get("commit", {}),
              "github_content_details": github_response.get("content", {})
          }
      except HTTPException:
          raise # Re-raise if it's an HTTPException from the helper
      except Exception as e:
          error_message = f"An unexpected error occurred: {str(e)}"
          print(f"[ERROR] {error_message}")
          raise HTTPException(status_code=500, detail="An internal server error occurred.")

  @app.get("/health", status_code=200, tags=["Health"])
  async def health_check():
      """
      A simple health check endpoint.
      """
      return {"status": "ok", "message": "Service is running."}

  # To run this server (save as main.py):
  # 1. Install dependencies: pip install fastapi uvicorn pydantic pydantic-settings httpx python-dotenv
  # 2. Create a .env file with your GitHub token and repo details.
  # 3. Run with Uvicorn: uvicorn main:app --reload
  # 4. Deploy to a public platform like Render.com.
  ```

  **Key aspects of this server:**

  * **Configuration (`.env`):** It expects a `.env` file with your `GITHUB_TOKEN`, `GITHUB_REPO_OWNER`, and `GITHUB_REPO_NAME`. You can also customize `GITHUB_FILE_PATH` (default: `LangSmith_prompt_manifest.json`) and `GITHUB_BRANCH` (default: `main`).
  * **GitHub Interaction:** The `commit_manifest_to_github` function handles the logic of fetching the current file's SHA (to update it) and then committing the new manifest content.
  * **Webhook Endpoint (`/webhook/commit`):** This is the URL path your LangSmith webhook will target.
  * **Error Handling:** Basic error handling for GitHub API interactions is included.

  **Deploy this server to your chosen platform (e.g., Render) and note down its public URL (e.g., `https://prompt-commit-webhook.onrender.com`).**
</Accordion>

## Configuring the webhook in LangSmith

Once your FastAPI server is deployed and you have its public URL, you can configure the webhook in LangSmith:

1. Navigate to your LangSmith workspace.

2. Go to the **Prompts** section. Here you'll see a list of your prompts.

   <img alt="LangSmith Prompts section" />

3. On the top right of the Prompts page, click the **+ Webhook** button.

4. You'll be presented with a form to configure your webhook:

   <img alt="LangSmith Webhook configuration modal" />

   * **Webhook URL:** Enter the full public URL of your deployed FastAPI server's endpoint. For our example server, this would be `https://prompt-commit-webhook.onrender.com/webhook/commit`.
   * **Headers (Optional):**
     * You can add custom headers that LangSmith will send with each webhook request.

5. **Test the Webhook:** LangSmith provides a "Send Test Notification" button. Use this to send a sample payload to your server. Check your server logs (e.g., on Render) to ensure it receives the request and processes it successfully (or to debug any issues).

6. **Save** the webhook configuration.

## The workflow in action

<img alt="Workflow Diagram showing: User saves prompt in LangSmith, LangSmith sends webhook to FastAPI Server, which interacts with GitHub to update files" />

Now, with everything set up, here's what happens:

1. **Prompt Modification:** A user (developer or non-technical team member) modifies a prompt in the LangSmith UI and saves it, creating a new "prompt commit."

2. **Webhook Trigger:** LangSmith detects this new prompt commit and triggers the configured webhook.

3. **HTTP Request:** LangSmith sends an HTTP POST request to the public URL of your FastAPI server (e.g., `https://prompt-commit-webhook.onrender.com/webhook/commit`). The body of this request contains the JSON prompt manifest for the entire workspace.

4. **Server Receives Payload:** Your FastAPI server's endpoint receives the request.

5. **GitHub Commit:** The server parses the JSON manifest from the request body. It then uses the configured GitHub Personal Access Token, repository owner, repository name, file path, and branch to:

   * Check if the manifest file already exists in the repository on the specified branch to get its SHA (this is necessary for updating an existing file).
   * Create a new commit with the latest prompt manifest, either creating the file or updating it if it already exists. The commit message will indicate that it's an update from LangSmith.

6. **Confirmation:** You should see the new commit appear in your GitHub repository.

   <img alt="Manifest committed to GitHub" />

You've now successfully synced your LangSmith prompts with GitHub!

## Beyond a simple commit

Our example FastAPI server performs a direct commit of the entire prompt manifest. However, this is just the starting point. You can extend the server's functionality to perform more sophisticated actions:

* **Granular Commits:** Parse the manifest and commit changes to individual prompt files if you prefer a more granular structure in your repository.
* **Trigger CI/CD:** Instead of (or in addition to) committing, have the server trigger a CI/CD pipeline (e.g., Jenkins, GitHub Actions, GitLab CI) to deploy a staging environment, run tests, or build new application versions.
* **Update Databases/Caches:** If your application loads prompts from a database or cache, update these stores directly.
* **Notifications:** Send notifications to Slack, email, or other communication channels about prompt changes.
* **Selective Processing:** Based on metadata within the LangSmith payload (if available, e.g., which specific prompt changed or by whom), you could apply different logic.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/prompt-commit.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Prompt engineering
Source: https://docs.langchain.com/langsmith/prompt-engineering

The following sections help you create, manage, and optimize your prompts:

<Columns>
  <Card title="Create and update prompts" icon="edit" href="/langsmith/create-a-prompt">
    Build prompts via the UI or SDK, configure settings, use tools, add multimodal inputs, and connect model providers.
  </Card>

  <Card title="Manage prompts" icon="tags" href="/langsmith/manage-prompts">
    Organize with tags, commit changes, trigger webhooks, and share through the public prompt hub.
  </Card>

  <Card title="Build agent and skill contexts" icon="git-branch" href="/langsmith/use-the-context-hub">
    Create, version, and promote agent and skill contexts in the LangSmith Context Hub.
  </Card>

  <Card title="Explore the prompt hub" icon="folders" href="/langsmith/manage-prompts#public-prompt-hub">
    Browse and manage prompt tags and discover community prompts from the LangChain Hub.
  </Card>

  <Card title="Open the Playground" icon="test-pipe" href="/langsmith/prompt-engineering-concepts#playground">
    Test and experiment with prompts using custom endpoints and model configurations.
  </Card>

  <Card title="Follow tutorials" icon="notebook" href="/langsmith/optimize-classifier">
    Learn step-by-step techniques, like optimizing classifiers and advanced prompt engineering.
  </Card>
</Columns>

<Callout type="info" icon="feather">
  Use the **[Chat](/langsmith/chat)** in the Playground to optimize prompts, generate tools, and create output schemas with AI-powered assistance.
</Callout>

<Note>
  To set up a LangSmith instance, visit the [Platform setup section](/langsmith/platform-setup) to choose between cloud, hybrid, or self-hosted. All options include observability, evaluation, prompt engineering, and deployment.
</Note>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/prompt-engineering.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Prompt engineering concepts
Source: https://docs.langchain.com/langsmith/prompt-engineering-concepts

While traditional software applications are built by writing code, AI applications often derive their logic from prompts.

This guide will walk through the key concepts of prompt engineering in LangSmith.

## Why prompt engineering?

A prompt guides the model's behavior without changing its underlying capabilities. By providing instructions, examples, and context, prompts shape how the model responds to inputs.

Prompt engineering is important because it allows you to modify model behavior. While other approaches exist (such as fine-tuning), prompt engineering typically offers the lowest barrier to entry and often delivers the highest return on investment.

Prompt engineering is often a multi-disciplinary effort. The most effective prompt engineer may be a product manager, domain expert, or other non-technical team member rather than the software engineer building the application. Proper tooling and infrastructure are essential to support this cross-functional collaboration.

## Prompt types

There are two different types of prompt formats: `chat` style prompts and `completion` style prompts.

**Chat prompts** are a list of messages, each with a role (such as `system`, `user`, or `assistant`). This is the prompting style supported by most current model APIs and is the recommended format.

**Completion prompts** are a single string. This is an older prompting style maintained primarily for backward compatibility.

<Note>
  Unless you have a specific reason to use completion prompts, use chat prompts for new projects. Chat prompts provide better structure for multi-turn conversations and are better supported by modern LLMs.
</Note>

## Prompts vs. prompt templates

While *prompt* and *prompt template* are often used interchangeably, understanding the distinction helps clarify how LangSmith manages and evaluates your AI application.

* **Prompts** refer to the messages that are passed into the language model.
* **Prompt templates** allow you to create reusable prompts with dynamic placeholders that get filled in at runtime. Instead of hardcoding values, you define variables that LangSmith replaces with different inputs each time you run your prompt. This makes prompts flexible, testable, and easier to iterate on.

Here's how templates work in practice:

1. **Define the template**: Create a prompt with variables (marked with curly braces) that will be replaced at runtime:

   ```
   You are a customer support agent. This is the refund policy:

   {refund_policy}

   Please respond to the user's question:

   {question}
   ```

2. **Provide input values**: Supply the actual values for each variable:

   ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   {
   "refund_policy": "no refunds under any circumstances",
   "question": "can I get a refund for this hat?"
   }
   ```

3. **Get the final prompt**: LangSmith replaces the variables with your inputs to create the prompt sent to the model:

   ```
   You are a customer support agent. This is the refund policy:

   no refunds under any circumstances

   Please respond to the user's question:

   Can I get a refund for this hat?
   ```

<Tip>
  Learn more about template variable syntax and formatting options in the [Prompt template format](/langsmith/create-a-prompt#template-format) guide.
</Tip>

## Prompts in LangSmith

You can store and version prompt templates in LangSmith. These templates can be tested in the Playground, versioned with commits and tags, and pulled into your application code.

<Callout type="info" icon="player-play">
  Open the [Playground](https://smith.langchain.com/playground) to create and test your first prompt template. For a step-by-step, refer to [Create a prompt](/langsmith/create-a-prompt).
</Callout>

The following sections describe key aspects of prompt templates.

### F-string vs. mustache

You can format your prompt template with input variables using either [f-string](https://realpython.com/python-f-strings/) or [mustache](https://mustache.github.io/mustache.5.html) format.

For details on how to use these formats in the Playground, see [Template format](/langsmith/create-a-prompt#template-format).

<Check>
  The [Playground](https://smith.langchain.com/playground) uses `f-string` as the default template format, but you can switch to `mustache` format in the prompt settings/template format section. `mustache` gives you more flexibility around conditional variables, loops, and nested keys. For conditional variables, you'll need to manually add json variables in the 'inputs' section. Read [the documentation](https://mustache.github.io/mustache.5.html)
</Check>

### Tools

[Tools](/langsmith/use-tools) are interfaces the LLM can use to interact with the outside world. Tools consist of a name, description, and JSON schema of arguments used to call the tool.

### Structured output

Structured output is a feature of most state of the art LLMs, wherein instead of producing raw text as output they stick to a specified schema. This may or may not use [Tools](#tools) under the hood.

<Check>
  Structured output is similar to tools, but different in a few key ways. With tools, the LLM choose which tool to call (or may choose not to call any); with structured output, the LLM **always** responds in this format. With tools, the LLM may select **multiple** tools; with structured output, only one response is generate.
</Check>

### Model

Optionally, you can store a model configuration alongside a prompt template. This includes the name of the model and any other parameters (temperature, etc).

## Prompt versioning

Versioning is a key component of iterating on and collaborating with prompts.

### Commits

Every saved update to a prompt creates a new commit with a unique commit hash. This allows you to:

* View the full history of changes to a prompt.
* Review earlier versions.
* Revert to a previous state if needed.
* Reference specific versions in your code using the commit hash (e.g., `client.pull_prompt("prompt_name:commit_hash")`).

In the UI, you can compare a commit with its previous version by toggling **Diff** in the top-right corner of the [Prompt detail page](/langsmith/manage-prompts#prompt-detail-page).

### Tags

Commit tags are human-readable labels that point to specific commits in your prompt's history. Unlike commit hashes, tags can be moved to point to different commits, allowing you to update which version your code references without changing the code itself.

Use cases for commit tags can include:

* **Environments**: The `staging` and `production` tags are reserved for the [Environments](/langsmith/manage-prompts#environments) feature, which lets you promote commits between named deployment targets and switch versions without changing your code.
* **Version control**: Mark stable versions of your prompts, for example, `v1`, `v2`, which lets you reference specific versions in your code and track changes over time.
* **Collaboration**: Mark versions ready for review, which enables you to share specific versions with collaborators and get feedback.

<Note>
  **Not to be confused with resource tags**: Commit tags reference specific prompt versions. [Resource tags](/langsmith/set-up-resource-tags) are key-value pairs used to organize workspace resources.
</Note>

For detailed information on creating and managing commit tags, see [Manage prompts](/langsmith/manage-prompts#commit-tags).

## Playground

The Playground provides an interface for iterating on and testing prompts. You can access the Playground from the sidebar or directly from a saved prompt.

In the Playground you can:

* Change the model being used
* Change prompt template being used
* Change the output schema
* Change the tools available
* Enter the input variables to run through the prompt template
* Run the prompt through the model
* Observe the outputs

<Callout type="info" icon="feather">
  Use the **[Chat](/langsmith/chat)** in the Playground to optimize prompts, generate tools, and create output schemas with AI assistance.
</Callout>

## Testing multiple prompts

You can add multiple prompts to your Playground to compare outputs and evaluate performance:

<img alt="Add prompt to Playground" />

## Testing over a dataset

To test over a dataset, select the dataset from the top right and click Start. You can configure whether results are streamed and the number of repetitions for the test.

<img alt="Test over dataset in Playground" />

Click the "View Experiment" button to view detailed test results.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/prompt-engineering-concepts.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
