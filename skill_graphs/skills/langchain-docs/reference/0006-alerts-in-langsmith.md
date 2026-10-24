# Alerts in LangSmith
Source: https://docs.langchain.com/langsmith/alerts

<Note>
  **Self-hosted version requirement**: Access to alerts requires Helm chart version **0.10.3** or later.
</Note>

Effective observability in LLM applications requires proactive detection of failures, performance degradations, and regressions. LangSmith's alerts feature helps identify critical issues such as:

* API rate limit violations from model providers.
* Latency increases for your application.
* Application changes that affect feedback scores reflecting end-user experience.
* Unexpected cost spikes from LLM usage.

Alerts in LangSmith are project-scoped, requiring separate configuration for each monitored project.

<Tip>
  Alerts can [route](#step-4-configure-notification-channel) to PagerDuty, Dynatrace, or any HTTP endpoint via webhook. The **Webhook** tab includes [example recipes](#example-recipes) for sending alerts to Slack, Microsoft Teams, and email.
</Tip>

Follow these steps to configure an alert.

## Step 1: Navigate to create alert

In the [UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-alerts), navigate to the Tracing project that you would like to configure alerts for. Click the **Alerts** icon on the top right-hand corner of the page to view existing alerts for that project and set up a new alert.

## Step 2: Select metric type

LangSmith provides threshold-based alerting on the following metrics:

| Metric Type        | Description                                                                                                           | Use Case                                                                                                                                                             |
| ------------------ | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Run Count**      | Tracks the total number of [runs](/langsmith/observability-concepts#runs) over a time window.                         | Monitor whether a pipeline is producing runs at the expected volume and alert when it drops unexpectedly.                                                            |
| **Cost**           | Tracks the total cost of runs over a time window.                                                                     | Monitor LLM spending to alert when costs exceed expected thresholds. Requires [cost tracking](/langsmith/cost-tracking) to be configured.                            |
| **Errors**         | Tracks runs with an error status. Alert on total error count or error percent (rate of errored runs out of all runs). | Monitor for failures in an application, or alert when the error rate exceeds an acceptable threshold.                                                                |
| **Feedback Score** | Measures the average feedback score.                                                                                  | Track [feedback from end users](/langsmith/attach-user-feedback) or [online evaluation results](/langsmith/online-evaluations-llm-as-judge) to alert on regressions. |
| **Latency**        | Measures average run execution time.                                                                                  | Tracks the latency of your application to alert on spikes and performance bottlenecks.                                                                               |

Additionally, for **Errors** and **Latency**, you can use the filter builder to stack conditions on fields such as **Status**, **Run Type**, **Tag**, and **Error**. For example, you can scope an error alert to runs where **Status** is `error`, **Run Type** is `llm`, **Tag** is `support_agent`, and **Error** matches `RateLimitExceeded`.

## Step 3: Define alert conditions

Alert conditions consist of several components:

* **Aggregation Method**: Average, Percentage, or Count.
* **Comparison Operator**: `>=`, `<=`, or exceeds threshold.
* **Threshold Value**: Numerical value triggering the alert.
* **Aggregation Window**: Time period for metric calculation (choose between 5 or 15 minutes).
* **Feedback Key** (Feedback Score alerts only): Specific feedback metric to monitor.

<div>
  <img alt="Alert Condition Configuration" />
</div>

**Example:** The configuration in the screenshot would generate an alert when more than 5% of runs within the past 5 minutes result in errors.

You can preview alert behavior over a historical time window to understand how many datapoints, and which ones, would have triggered an alert at a chosen threshold (indicated in red). For example, setting an average latency threshold of 60 seconds for a project lets you visualize potential alerts, as shown in the following screenshot.

<div>
  <img alt="Alert Metrics" />
</div>

## Step 4: Configure notification channel

<Tip>
  The **Webhook** tab includes [example recipes](#example-recipes) for sending alerts to Slack, Microsoft Teams, and email.
</Tip>

<Tabs>
  <Tab title="PagerDuty">
    Configure PagerDuty as a notification channel using PagerDuty's [Events API v2](https://developer.pagerduty.com/docs/events-api-v2-overview). This integration allows critical LLM application issues to trigger PagerDuty incidents, enabling rapid response through your established incident management workflow.

    **Prerequisites**

    * An active PagerDuty account with administrator access
    * Appropriate service-level permissions in PagerDuty

    If on a custom deployment of LangSmith, make sure there are no firewall settings blocking egress traffic from LangSmith services.

    ### 1. Create a Service in PagerDuty

    1. Log in to your PagerDuty account
    2. Navigate to **Services → Service Directory**
    3. Click **+ New Service**
    4. Complete the following fields:
       * **Name**: Provide a descriptive name (e.g., "LangSmith Monitoring")
       * **Description**: Add details about the monitored application
       * **Escalation Policy**: Select the appropriate team escalation policy
       * **Integration Type**: Select "Events API V2"
    5. Click **Add Service** to create the service

    ### 2. Obtain integration key

    After creating the service, retrieve the Integration Key:

    1. From the **Service Directory**, locate and click on your newly created service
    2. Select the **Integrations** tab
    3. Find the "Events API V2" integration
    4. Copy the **Integration Key** (a 32-character alphanumeric string)

       <img alt="PagerDuty Integration Key Location" />

    ### 3. Configure LangSmith alert with PagerDuty

    <Info>
      To receive the same alert again within an hour of it being triggered, you must resolve the active incident created by the alert in PagerDuty.
    </Info>

    <img alt="PagerDuty Setup" />

    1. In the notification section of your alert set-up in LangSmith, select **PagerDuty**
    2. Click the key icon to save the Integration Key as a Workspace secret or select an existing Workspace secret. As a best practice, we recommend saving the Integration Key as a Workspace Secret rather than adding it directly. This will allow you to reuse the same key across alerts for a workspace.
    3. Configure additional notification options:
       * **Severity**: Maps to PagerDuty incident priority
    4. Send a test alert by clicking **Send Test Alert**
    5. Verify the incident is triggered by PagerDuty and contains relevant LangSmith alert information

    ### Troubleshooting

    If incidents aren't being created in PagerDuty:

    * Verify the Integration Key is entered correctly in LangSmith
    * Ensure the PagerDuty service is active and not in maintenance mode
    * Check that your PagerDuty account has Events API v2 enabled
    * If an alert trigger appears to be missing in PagerDuty, check whether the expected trigger occurred within one hour of a previous trigger from the same alert rule, and whether the incident created by the previous alert is still open.
    * Review network connectivity if your LangSmith instance is behind a firewall

    ### Additional resources

    * [PagerDuty Events API v2 Documentation](https://developer.pagerduty.com/docs/events-api-v2/overview/)
    * [PagerDuty Integration Guide](https://support.pagerduty.com/docs/services-and-integrations)
  </Tab>

  <Tab title="Dynatrace">
    Configure Dynatrace as a notification channel using Dynatrace's [Events API v2](https://docs.dynatrace.com/docs/dynatrace-api/environment-api/events-v2/post-event). This integration sends LangSmith alert events to your Dynatrace environment, enabling correlation with your broader infrastructure monitoring.

    **Prerequisites**

    * An active Dynatrace environment (SaaS or Managed).
    * A Dynatrace API access token with the `events.ingest` scope.

    If you're working from a custom [deployment](/langsmith/self-hosted) of LangSmith, make sure there are no firewall settings blocking egress traffic from LangSmith services.

    ### 1. Create an API token in Dynatrace

    1. Log in to your Dynatrace environment.
    2. Navigate to **Access Tokens**.
    3. Click **Generate new token**.
    4. Provide a descriptive name (e.g., "LangSmith Alerts").
    5. Under **Scopes**, search for and enable `events.ingest` (Ingest events).
    6. Click **Generate token**.
    7. Copy the generated token and store it securely. The token is only displayed once.

    ### 2. Obtain your Dynatrace environment URL

    Your Dynatrace environment URL follows this format:

    ```
    https://{your-environment-id}.live.dynatrace.com
    ```

    You can find your environment ID in the browser URL bar when logged in to Dynatrace.

    ### 3. Configure LangSmith alert with Dynatrace

    1. In the **Notifications Settings** for your alert setup in LangSmith, select **Dynatrace**.
    2. Enter your Dynatrace environment URL.
    3. Click the key icon to save the API token as a workspace secret or select an existing workspace secret. As a best practice, save the API token as a workspace secret rather than adding it directly. This allows you to reuse the same token across alerts for a workspace.
    4. Configure additional notification options:
       * **Event Type**: Select the Dynatrace event type (e.g., `CUSTOM_ALERT`, `ERROR_EVENT`)
    5. Send a test alert by clicking **Send Test Notification**.
    6. Verify the event appears in your Dynatrace environment.

    ### Troubleshooting

    If events aren't appearing in Dynatrace:

    * Verify the API token has the `events.ingest` scope and is not expired.
    * Ensure the environment URL is correct and includes your environment ID.
    * Confirm the `Authorization` header format uses `Api-Token` (not `Bearer`).
    * Check that your Dynatrace environment is active and accessible.
    * Review network connectivity if your LangSmith instance is behind a firewall.

    ### Additional resources

    * [Dynatrace Events API v2 Documentation](https://docs.dynatrace.com/docs/dynatrace-api/environment-api/events-v2/post-event)
    * [Dynatrace Access Tokens](https://docs.dynatrace.com/docs/manage/access-control/access-tokens)
  </Tab>

  <Tab title="Webhook">
    Webhooks enable integration with custom services and third-party platforms by sending HTTP POST requests when alert conditions are triggered. Use webhooks to forward alert data to ticketing systems, chat applications, or custom monitoring solutions.

    **Prerequisites**

    * An endpoint that can receive HTTP POST requests
    * Appropriate authentication credentials for your receiving service (if required)

    ### 1. Prepare your receiving endpoint

    Before configuring the webhook in LangSmith, ensure your receiving endpoint:

    * Accepts HTTP POST requests
    * Can process JSON payloads
    * Is accessible from external services
    * Has appropriate authentication mechanisms (if required)

    If on a custom deployment of LangSmith, make sure there are no firewall settings blocking egress traffic from LangSmith services.

    ### 2. Configure webhook parameters

    In the **Monitoring** section of the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-alerts) under the **Alerts** tab, click **+ Alert** to create a. new alert.

    In the **Notification Settings** section, complete the webhook configuration with the following parameters:

    **Required fields**

    * **URL**: The complete URL of your receiving endpoint
      * Example: `https://api.example.com/incident-webhook`

    **Optional fields**

    * **Headers**: JSON key-value pairs sent with the webhook request
      * Common headers include:
        * `Authorization`: For authentication tokens
        * `Content-Type`: Usually set to `application/json` (default)
        * `X-Source`: To identify the source as LangSmith
      * If no headers, use `{}`

    * **Request Body Template**: Customize the JSON payload sent to your endpoint
      * Default: LangSmith sends the payload defined and the following additional key-value pairs appended to the payload:
        * `project_name`: Name of the triggered alert
        * `alert_rule_id`: A UUID to identify the LangSmith alert. This can be used as a de-duplication key in the webhook service.
        * `alert_rule_name`: The name of the alert rule.
        * `alert_rule_type`: The type of alert (as of 04/01/2025 all alerts are of type `threshold`).
        * `alert_rule_attribute`: The attribute associated with the alert rule - `error_count`, `feedback_score`, `latency`, or `cost`.
        * `triggered_metric_value`: The value of the metric at the time the threshold was triggered.
        * `triggered_threshold`: The threshold that triggered the alert.
        * `timestamp`: The timestamp that triggered the alert.

    <Info>
      LangSmith does not perform template substitution on the request body. The auto-populated fields above are merged into the outgoing JSON as top-level keys, alongside the body you configure. Placeholder syntax like `{alert_rule_name}` is sent verbatim to the receiving service. It only resolves to a real value if the receiver itself can extract fields from the incoming JSON (for example, a Power Automate Workflow, an AWS Lambda, or a custom HTTP handler).
    </Info>

    ### 3. Test the webhook

    Click **Send Test Alert** to send the webhook notification to ensure the notification works as intended.

    ### Troubleshooting

    If webhook notifications aren't being delivered:

    * Verify the webhook URL is correct and accessible
    * Ensure any authentication headers are properly formatted
    * Check that your receiving endpoint accepts POST requests
    * Examine your endpoint's logs for received but rejected requests
    * Verify your custom payload template is valid JSON format

    ### Security considerations

    * Use HTTPS for your webhook endpoints
    * Implement authentication for your webhook endpoint
    * Consider adding a shared secret in your headers to verify webhook sources
    * Validate incoming webhook requests before processing them

    ### Example recipes

    <Accordion title="Configure Slack notifications via webhook">
      Here is an example for configuring LangSmith alerts to send notifications to Slack channels using the [`chat.postMessage`](https://api.slack.com/methods/chat.postMessage) API.

      **Prerequisites**

      * Access to a Slack workspace.
      * A LangSmith project to set up alerts.
      * Permissions to create Slack applications.

      **Step 1: Create a Slack app**

      1. Visit the [Slack API Applications page](https://api.slack.com/apps).
      2. Click **Create New App**.
      3. Select **From scratch**.
      4. Provide an **App Name** (e.g., "LangSmith Alerts").
      5. Select the workspace where you want to install the app.
      6. Click **Create App**.

      **Step 2: Configure bot permissions**

      1. In the left sidebar of your Slack app configuration, click **OAuth & Permissions**.
      2. Scroll down to **Bot Token Scopes** under **Scopes** and click **Add an OAuth Scope**.
      3. Add the following scopes:
         * `chat:write` (Send messages as the app).
         * `chat:write.public` (Send messages to channels the app isn't in).
         * `channels:read` (View basic channel information).

      **Step 3: Install the app to your workspace**

      1. Scroll up to the top of the **OAuth & Permissions** page.
      2. Click **Install to Workspace**.
      3. Review the permissions and click **Allow**.
      4. Copy the **Bot User OAuth Token** that appears (begins with `xoxb-`).

      **Step 4: Add the bot to a Slack channel**

      Add the bot to the specific channel you want to receive alerts in. You can add a bot to a Slack channel by mentioning it in the message field (e.g., `@botname`).

      You also need the channel ID to configure the webhook alert in LangSmith. You can find the channel ID by opening channel details > About.

      **Step 5: Configure the webhook alert in LangSmith**

      1. In LangSmith, navigate to your project.
      2. Select **Alerts → Create Alert**.
      3. Define your alert metrics and conditions.
      4. In the notification section, select **Webhook**.
      5. Configure the webhook with the following settings:

      **Webhook URL**

      ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      https://slack.com/api/chat.postMessage
      ```

      **Headers**
      <Note>Replace `xoxb-your-token-here` with your Bot's User OAuth Token</Note>

      ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      {
        "Content-Type": "application/json",
        "Authorization": "Bearer xoxb-your-token-here"
      }
      ```

      **Request Body Template**
      <Note>It is required to fill in the `{channel_id}` from the value found in Step 4. <br /><br />The remaining fields: `alert_name`, `project_name` and `project_url` optionally add additional context to the alert message. You can find your `project_url` in the browser's URL bar. Copy the portion up to but not including any query parameters.</Note>

      ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      {
        "channel": "{channel_id}",
        "text": "{alert_name} triggered for {project_name}",
        "blocks": [
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "🚨{alert_name} has been triggered"
            }
          },
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "Please check the following link for more information:"
            }
          },
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "<{project-url}|View in LangSmith>"
            }
          }
        ]
      }
      ```

      6. Click **Save** to activate the webhook configuration.

      **Step 6: Test the integration**

      1. In the LangSmith alert configuration, click **Test Alert**.
      2. Check your specified Slack channel for the test notification.
      3. Verify that the message contains the expected alert information.

      **(Optional) Step 7: Link to the alert preview in the request body**

      After creating an alert, you can optionally link to its preview in the webhook's request body.

      <img alt="Alert Preview Pane" />

      To configure this:

      1. Save your alert.
      2. Find your saved alert in the alerts table and click it.
      3. Copy the displayed URL.
      4. Click "Edit Alert".
      5. Replace the existing project URL with the copied alert preview URL.
    </Accordion>

    <Accordion title="Configure Microsoft Teams notifications via webhook">
      Here is an example for configuring LangSmith alerts to send notifications to a Microsoft Teams channel using the [Workflows app](https://support.microsoft.com/en-us/office/create-incoming-webhooks-with-workflows-for-microsoft-teams-8ae491c7-0394-4861-ba59-055e33f75498) (Power Automate). This approach is recommended because it extracts fields from the incoming JSON within the flow, so the auto-populated LangSmith alert fields render correctly in the Teams message.

      <Note>
        Microsoft's legacy Office 365 Incoming Webhook connectors are being retired. Use the Workflows app for new integrations.
      </Note>

      **Prerequisites**

      * Access to a Microsoft Teams workspace with permissions to add Workflows.
      * A LangSmith project to set up alerts.

      **Step 1: Create a Workflow in Teams**

      1. In Microsoft Teams, navigate to the channel where you want to receive alerts.
      2. Click the **...** (More options) menu next to the channel name.
      3. Select **Workflows**.
      4. Search for and select the **Post to a channel when a webhook request is received** template.
      5. Sign in to confirm the connections, then click **Next**.
      6. Confirm the team and channel where alerts should be posted, then click **Add workflow**.
      7. Copy the generated **HTTP POST URL**—use this in LangSmith.

      **Step 2: Customize the message in Power Automate (optional)**

      The default workflow posts the raw JSON body as a card. To format alert details, edit the flow in Power Automate:

      1. Open the [Power Automate portal](https://make.powerautomate.com) and edit the workflow you created.
      2. Click the **Post card in a chat or channel** action.
      3. In the **Adaptive Card** field, reference incoming fields using `triggerOutputs()?['body/alert_rule_name']`, `triggerOutputs()?['body/project_name']`, `triggerOutputs()?['body/triggered_metric_value']`, `triggerOutputs()?['body/triggered_threshold']`, `triggerOutputs()?['body/timestamp']`, and `triggerOutputs()?['body/alert_rule_url']`.
      4. Save the flow.

      **Step 3: Configure the webhook alert in LangSmith**

      1. In LangSmith, navigate to your project.
      2. Select **Alerts → Create Alert**.
      3. Define your alert metrics and conditions.
      4. In the notification section, select **Webhook**.
      5. Configure the webhook with the following settings:

      **Webhook URL**

      Paste the HTTP POST URL from your Teams Workflow:

      ```
      https://prod-XX.westus.logic.azure.com:443/workflows/.../triggers/manual/paths/invoke?...
      ```

      **Headers**

      ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      {
        "Content-Type": "application/json"
      }
      ```

      **Request Body Template**

      LangSmith automatically merges the auto-populated alert fields (`alert_rule_name`, `project_name`, `triggered_metric_value`, `triggered_threshold`, `timestamp`, `alert_rule_url`, and others) into the request body as top-level JSON keys. Power Automate reads these fields directly from the incoming payload, so an empty body is sufficient:

      ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      {}
      ```

      6. Click **Save** to activate the webhook configuration.

      **Step 4: Test the integration**

      1. In the LangSmith alert configuration, click **Send Test Alert**.
      2. Check your specified Teams channel for the test notification.
      3. Verify that the card contains the expected alert information.

      **Reference implementation**

      For a working example that translates LangSmith webhook payloads (threshold alerts, run rules, and generic events) into formatted Teams Adaptive Cards, see the [langsmith-teams-webhook](https://github.com/langchain-samples/langsmith-teams-webhook) sample repo. The sample runs as a small Python service in front of a Teams Workflow URL, which avoids customizing the Power Automate flow itself.
    </Accordion>

    <Accordion title="Configure email notifications via webhook">
      Here is an example for configuring LangSmith alerts to send email notifications using [SendGrid's Mail Send API](https://docs.sendgrid.com/api-reference/mail-send/mail-send). You can use any transactional email provider that exposes an HTTP API (e.g., Mailgun, Amazon SES, Postmark).

      **Prerequisites**

      * A SendGrid account with a verified sender identity.
      * A SendGrid API key with **Mail Send** permissions.
      * A LangSmith project to set up alerts.

      **Step 1: Create a SendGrid API key**

      1. Log in to your [SendGrid dashboard](https://app.sendgrid.com).
      2. Navigate to **Settings → API Keys**.
      3. Click **Create API Key**.
      4. Choose **Restricted Access** and enable **Mail Send → Full Access**.
      5. Click **Create & View**, copy the key, and store it securely.

      **Step 2: Verify your sender email**

      1. In SendGrid, navigate to **Settings → Sender Authentication**.
      2. Complete either **Domain Authentication** (recommended) or **Single Sender Verification** for the address you want to send from.

      **Step 3: Configure the webhook alert in LangSmith**

      1. In LangSmith, navigate to your project.
      2. Select **Alerts → Create Alert**.
      3. Define your alert metrics and conditions.
      4. In the notification section, select **Webhook**.
      5. Configure the webhook with the following settings:

      **Webhook URL**

      ```
      https://api.sendgrid.com/v3/mail/send
      ```

      **Headers**

      <Note>Replace `SG.your-api-key-here` with your SendGrid API key.</Note>

      ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      {
        "Content-Type": "application/json",
        "Authorization": "Bearer SG.your-api-key-here"
      }
      ```

      **Request Body Template**

      <Note>
        Replace `alerts@your-company.com` with your verified sender address and `oncall@your-company.com` with the recipient address. SendGrid does not extract fields from arbitrary top-level JSON keys, so this example uses a fixed subject and body. To include alert-specific values in the email, route the LangSmith webhook through a middleware (such as a Power Automate flow, AWS Lambda, or Zapier webhook) that reads the incoming payload and renders the SendGrid request.
      </Note>

      ```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      {
        "personalizations": [
          {
            "to": [
              {
                "email": "oncall@your-company.com"
              }
            ],
            "subject": "LangSmith alert triggered"
          }
        ],
        "from": {
          "email": "alerts@your-company.com",
          "name": "LangSmith Alerts"
        },
        "content": [
          {
            "type": "text/plain",
            "value": "A LangSmith alert was triggered. Open your LangSmith workspace to view the alert details, including the project, metric value, threshold, and timestamp."
          }
        ]
      }
      ```

      6. Click **Save** to activate the webhook configuration.

      **Step 4: Test the integration**

      1. In the LangSmith alert configuration, click **Send Test Alert**.
      2. Check the recipient inbox for the test notification.
      3. Verify the email contains the expected alert information.

      **Using other email providers**

      The same pattern works with other transactional email APIs that accept static authentication headers. Change the **Webhook URL** and **Headers** to match your provider:

      | Provider | Webhook URL                                         | Auth header format                         |
      | -------- | --------------------------------------------------- | ------------------------------------------ |
      | Mailgun  | `https://api.mailgun.net/v3/{your-domain}/messages` | `Authorization: Basic <base64(api:<key>)>` |
      | Postmark | `https://api.postmarkapp.com/email`                 | `X-Postmark-Server-Token: <token>`         |

      Adjust the **Request Body Template** to match each provider's expected payload format. Amazon SES is not directly compatible because the SES API requires per-request AWS SigV4 signing, which cannot be expressed as a static header. To use SES, route through a middleware (for example, a Lambda function with an HTTP trigger).
    </Accordion>

    ### Additional resources

    * [Slack chat.postMessage API Documentation](https://api.slack.com/methods/chat.postMessage)
    * [Slack Block Kit Builder](https://app.slack.com/block-kit-builder/)
    * [Create incoming webhooks with Workflows for Microsoft Teams](https://support.microsoft.com/en-us/office/create-incoming-webhooks-with-workflows-for-microsoft-teams-8ae491c7-0394-4861-ba59-055e33f75498)
    * [Power Automate documentation](https://learn.microsoft.com/en-us/power-automate/)
    * [langsmith-teams-webhook sample repo](https://github.com/langchain-samples/langsmith-teams-webhook)
    * [SendGrid Mail Send API Documentation](https://docs.sendgrid.com/api-reference/mail-send/mail-send)
  </Tab>
</Tabs>

## Best practices

* Adjust sensitivity based on application criticality
* Start with broader thresholds and refine based on observed patterns
* Ensure alert routing reaches appropriate on-call personnel

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/alerts.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Analyze an experiment
Source: https://docs.langchain.com/langsmith/analyze-an-experiment

This page describes some of the essential tasks for working with [*experiments*](/langsmith/evaluation-concepts#experiment) in LangSmith:

* **[Analyze a single experiment](#analyze-a-single-experiment)**: View and interpret experiment results, customize columns, filter data, and compare runs.
* **[Set a baseline in the Experiments tab view](#set-a-baseline-in-the-experiments-tab-view)**: Set a baseline for a dataset that you want to outperform.
* **[Filter and group by models, prompts, and tools in the Experiments tab view](#filter-and-group-by-models-prompts-and-tools-in-the-experiments-tab-view)**: Use **Models**, **Prompts**, and **Tools** columns to filter and group experiments in the **Experiments** tab view.
* **[Download experiment results as a CSV](#download-experiment-results-as-a-csv)**: Export your experiment data for external analysis and sharing.
* **[Rename an experiment](#rename-an-experiment)**: Update experiment names in both the Playground and experiment view.

## Analyze a single experiment

After running an experiment, you can use LangSmith's experiment view to analyze the results and draw insights about your experiment's performance.

### Open the experiment view

To open the experiment view,

1. Select the relevant [*dataset*](/langsmith/evaluation-concepts#datasets) from the **Dataset & Experiments** page which opens the **Experiments** tab view.
2. Click the row of the experiment you want to view.

<img alt="Open experiment view" />

### View experiment results

#### Customize columns

By default, the experiment view shows the input, output, and reference output for each [example](/langsmith/evaluation-concepts#examples) in the dataset, feedback scores from evaluations and experiment metrics like cost, token counts, latency and status.

You can customize the columns clicking the **Columns** icon at the top right of the view to make it easier to interpret experiment results:

* **Break out fields from inputs, outputs, and reference outputs** into their own columns. This is especially helpful if you have long inputs/outputs/reference outputs and want to surface important fields.
* **Hide and reorder columns** to create focused views for analysis.
* **Control decimal precision on feedback scores**. By default, LangSmith surfaces numerical feedback scores with a decimal precision of 2, but you can customize this setting to be up to 6 decimals.
* **Set the Heat Map threshold** to high, middle, and low for numeric feedback scores in your experiment, which affects the threshold at which score chips render as red or green:

<img alt="Column heatmap configuration" />

<Tip>
  You can set default configurations for an entire dataset or temporarily save settings just for yourself.
</Tip>

#### Sort and filter

To sort rows by a feedback score, click the **Sort by** icon in the column header.

<img alt="Sort column" />

To filter rows, click the <Icon icon="dots-vertical" /> icon in the column header and configure your filter settings.

<img alt="Filter column" />

#### Table views

Select one of three table view icons at the top right of the experiment view:

* **Compact**: Shows each run as a single row for quick score comparisons.
* **Full**: Shows the full output for each run.
* **Diff**: Shows the text difference between the reference output and the output for each run.

<img alt="Diff view" />

#### View the traces

Click any row in the experiment view to open the details panel, which shows the trace alongside feedback, input, output, and attributes for that run.

<img alt="View trace" />

To view the entire tracing project, click on the **View Project** icon at the top right of the experiment view.

#### View evaluator runs

By hovering over the evaluator score, you can view additional details about that evaluator run. For [LLM-as-a-judge evaluators](/langsmith/llm-as-judge), click the **Source** link to view the prompt used, or **Evaluator trace** to open the trace in a new browser tab. For experiments with [repetitions](/langsmith/repetition), click the aggregate average score to view links to all individual runs.

<img alt="View evaluator runs" />

### Group results by metadata

You can add metadata to examples to categorize and organize them. For example, if you're evaluating factual accuracy on a question answering dataset, the metadata might include which subject area each question belongs to. Metadata can be added either [via the UI](/langsmith/manage-datasets-in-application#edit-example-metadata) or [via the SDK](/langsmith/manage-datasets-programmatically#update-single-example).

To analyze results by metadata, use the **Group by** icon at the top right of the experiment view and select your desired metadata key. This displays average feedback scores, latency, total tokens, and cost for each metadata group.

<Info>
  You will only be able to group by example metadata on experiments created after February 20th, 2025. Any experiments before that date can still be grouped by metadata, but only if the metadata is on the experiment traces themselves.
</Info>

### Repetitions

If you've run your experiment with [*repetitions*](/langsmith/repetition), click any row to open the details panel. The **Repetition Summary** shows a metrics table, all feedback scores, and lets you toggle through outputs or view individual repetitions with their traces.

<img alt="Repetitions" />

### Compare to another experiment

In the top right of the experiment view, you can select another experiment to compare to. This will open up a comparison view, where you can see how the two experiments compare. To learn more about the comparison view, see [how to compare experiment results](/langsmith/compare-experiment-results).

## Set a baseline in the Experiments tab view

While you may run dozens of tests, you typically have a specific benchmark you are trying to outperform. Setting a *baseline* anchors your results against this reference point, which allows you to identify improvements or regressions in a crowded experiment list.

By designating a baseline, you can:

* Highlight a reference: Explicitly mark your best-performing run so it remains visible at the top of the **Experiments** tab view as you iterate.
* See instant diffs: View performance deltas across all experiments automatically, which means you don't necessarily need to perform manual side-by-side selection.
* Accelerate assessment: Quickly determine if new iterations meet or exceed your current performance standards.

<img alt="The Experiments tab view with an experiment marked as the baseline at the top of the table. Scores show against the baseline on the rows of other experiments." />

<img alt="The Experiments tab view with an experiment marked as the baseline at the top of the table. Scores show against the baseline on the rows of other experiments." />

To set a baseline for a dataset:

1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-analyze-an-experiment), navigate to the **Datasets & Experiments** option in the left menu.
2. Select the dataset that you want to work with from the table.
3. In the **Experiments** tab view, hover over an experiment row to display the **Set baseline** button on the right end of the row. Click to select your baseline experiment.

Your baseline experiment will pin to the top of the table and have the **Baseline** tag next to its name. Once an experiment is set as a baseline, the table will display scores against the baseline on each experiment for each column. When you are selecting multiple experiments for comparison, the baseline experiment will be the default source experiment to be compared to.

## Filter and group by models, prompts, and tools in the Experiments tab view

The experiments table includes **Models**, **Prompts**, and **Tools** columns that show which models, prompts, and tools were used for each experiment, making it easier to understand what changed between runs at a glance.

These columns are populated automatically when you run experiments from the Playground. When running experiments via the SDK, pass a `metadata` object with `models`, `prompts`, and `tools` keys to `evaluate()`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
results = client.evaluate(
    target,
    data="my-dataset",
    evaluators=[...],
    metadata={
        "models": "openai:gpt-5.4-mini",
        "prompts": ["my-org/my-prompt:abc12345"],
        "tools": [{"name": "web_search", "description": "Search the web for information"}],
    },
)
```

See [how to evaluate an LLM application](/langsmith/evaluate-llm-application#run-the-evaluation) for an example using metadata.

The columns only appear when at least one experiment in the dataset has the field set. Once populated, click on a value in these columns to filter or group experiments.

<img alt="The Experiments tab view with metadata columns for models, prompts, and tools." />

<img alt="The Experiments tab view with metadata columns for models, prompts, and tools." />

You can also filter and group by models, model providers, prompts, prompt commits, tools, and other experiment metadata at the top left of the **Experiments** tab view:

<img alt="The Experiments tab view with metadata columns for models, prompts, and tools." />

<img alt="The Experiments tab view with metadata columns for models, prompts, and tools." />

## Download experiment results as a CSV

LangSmith lets you download experiment results as a CSV file for external analysis and sharing. Click the **Download as CSV** icon at the top right of the experiment view.

<Note>
  There is a 5,000 row download limit for experiment results.
</Note>

## Rename an experiment

<Note>
  Experiment names must be unique per workspace.
</Note>

You can rename an experiment in the LangSmith UI in the following places:

* **Experiment view**: Rename an experiment by using the pencil icon beside the experiment name.

  <img alt="Edit name in experiment view" />

* **Playground**: A default name with the format `pg::prompt-name::model::uuid` (eg. `pg::gpt-5.4-mini::897ee630`) is automatically assigned. You can rename an experiment immediately after running it by editing its name in the Playground table header.

  <img alt="Edit name in playground" />

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/analyze-an-experiment.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
