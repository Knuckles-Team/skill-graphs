4. You will be taken to the CloudFormation Console to create the stack with pre-populated information.
   - Review the information and then select **Create stack**.

#### Manual setup

You can manually configure a CloudFormation stack using the provided template.

1. Open the Temporal Cloud UI and navigate to the Namespace you want to configure.
2. Select **Configure** from the **Export** card.
3. Select **Manual** from **Access method**.
   - Enter the Template URL into your web browser to download your copy of the CloudFormation template.
   - Configure the CloudFormation template for your export sink.
   - Follow the steps in the [AWS documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-using-console-create-stack-template.html) by uploading the template to the CloudFormation console.

### Using `tcld`

Run the `tcld namespace export s3 create` command and provide the following information:

- `--namespace`: The Namespace to configure export for.
- `--sink-name`: The name of the export sink.
- `--role-arn`: The ARN of the AWS IAM role to use for the CloudFormation stack that has write permission to the S3 bucket.
- `--s3-bucket-name`: The name of the AWS S3 bucket.

For example:

```command
tcld namespace export s3 create --namespace "your-namespace.your-account" --sink-name "your-sink-name" --role-arn "arn:aws:iam::123456789012:role/test-sink" --s3-bucket-name "your-aws-s3-bucket-name"
```

Retrieve the status of this command by running the `tcld namespace export s3 get` command.

For example:

```command
tcld namespace export s3 get --namespace "your-namespace.your-account" --sink-name "your-sink-name"
```

The following is an example of the output:

```json
{
  "name": "your-sink-name",
  "resourceVersion": "a6442895-1c07-4da4-aaca-58d57d338345",
  "state": "Active",
  "spec": {
    "name": "your-sink-name",
    "enabled": true,
    "destinationType": "S3",
    "s3Sink": {
      "roleName": "your-export-test",
      "bucketName": "your-export-test",
      "region": "us-east-1",
      "kmsArn": "",
      "awsAccountId": "123456789012"
    }
  },
  "health": "Ok",
  "errorMessage": "",
  "latestDataExportTime": "0001-01-01T00:00:00Z",
  "lastHealthCheckTime": "2023-08-14T21:30:02Z"
}
```

### Using `terraform`

See the [terraform export support](https://registry.terraform.io/providers/temporalio/temporalcloud/latest/docs/resources/namespace_export_sink) for setup instructions.

### Next Steps

- [Verify export setup](/cloud/export#verify)
- [Monitor export progress](/cloud/export#monitor)
- [Work with exported files](/cloud/export#working-with-exported-files)

---

## Usage dashboards

## Usage {/* #usage */}

Actions usage is tracked across an account in the [usage dashboard](https://cloud.temporal.io/usage) and is visible to
Account Owners, Finance Admin and Global Admin. For individual Namespaces, usage can be seen in the
[Namespace summary](https://cloud.temporal.io/namespaces/) for a specific Namespace.

![Temporal Cloud Usage dashboard](/img/cloud/billing/usage-dashboard.png)

## Actions in Workflows {/* #actions-in-workflows */}

When viewing a Event history, events that represent a Billable Action are annotated with the number consumed by the
event in the **Billable Actions** Column. These Actions are summarized at the top of the workflow.

<CaptionedImage
    src="/img/cloud/billing/aggregate-billable-actions.png"
    title="Temporal Cloud Usage dashboard showing aggregated Billable Actions"
/>

<CaptionedImage
    src="/img/cloud/billing/individual-billable-actions.png"
    title="Temporal Cloud Usage dashboard showing individual Billable Actions associated with events"
/>

This Billable Action estimate is useful for projecting the cost of Workflows. For example, if you ran a test Workflow
that generated 20 Billable Actions and projected that it would be run 100 times a day for a month, you could anticipate
that Workflow to generate 20 Actions x 100 runs/day x 30 days = 60,000 Billable Actions per month. You can also use the
Billable Action estimate to help optimize Workflows by better understanding your cost drivers.

:::tip Excluded Billable Actions

The Billable Action estimate is an experimental feature and only measures Billable Actions that exist within Workflow
event histories. Some billable concepts are not included in these calculations such as:

- Query
- Activity Heartbeats
- Rejected Update Workflow Executions
- Export
- Schedule
- Replicated Actions that occur in a
  [Namespace replication](../../cloud/high-availability/index.mdx#high-availability-features)

Additionally, Workflows with the `TemporalNamespaceDivision` Search Attribute set may not have accurate Billable Action
Estimates. The estimated Billable Actions should only be treated as an estimate. If billable events exist outside of
event history, the Actions count could be higher.

:::

[Reach out](https://pages.temporal.io/contact-us) to our team for more information or to help size your number of
Actions.

---

## Cloud Billing API

<ReleaseNoteHeader
  type="publicPreview"
/>

The Temporal Cloud Billing API provides Namespace-level cost attribution through on-demand billing reports.
Reports are delivered in CSV format and can be accessed via API or downloaded directly for use in FinOps tooling and cost management platforms.

This API is part of the [Cloud Operations API](/ops).

The Billing API allows you to:

- Generate billing reports for specified invoice months
- Retrieve report status and metadata
- Download CSV reports that can be fed into internal analytics tooling or cloud cost management platforms

The Billing Report contains:

- Accurate Namespace-level cost attribution
- Hourly, daily, and monthly granularities
- A [FOCUS](https://focus.finops.org/)-friendly data format

For complete request and response schemas, refer to the Schema below.

Billing report generation is **asynchronous**. You initiate report creation, then poll for completion.

## Report data limitations

For public preview, reports can be generated with hourly, daily and monthly granularities, each of which have their own data ranges.
- Hourly: Current billing month and previous billing month
- Daily: Current billing month and previous two billing months
- Monthly: Current billing month and previous eleven billing months

## Allowed date ranges

Date ranges must use billing-month boundaries (MM/YYYY).
Requests may include the current billing month.
The data in finalized reports includes usage up to `current_time` \- 24 hours (rounded down to the granularity level).

## Rate limits and concurrency

Rate limits apply to API usage.

### Per-account concurrency

Within a single account:

- Only one billing report per account is generated at a time
- Additional requests are accepted but queued

### Report Generation Latency

Report generation time varies and is not guaranteed. Factors that affect it include the size of the requested date range and overall platform load.

## Best practices

Provide an idempotency key (`async_operation_id`) when retrying requests.

Poll `GetBillingReport` using exponential backoff.

Download reports immediately after generation (URLs expire).

Avoid frequent generation of large overlapping ranges in the current billing period.

## Billing report schema

Billing reports are delivered in CSV format.

Each row represents a charge record.

| Column Name | Description | Example |
| ----- | ----- | ----- |
| BillingAccountID | Temporal Cloud account ID | a2dd6 |
| BillingAccountName | Temporal Cloud account name | temporal |
| BillingCurrency | The currency an account is billed in | USD (cents) |
| BillingPeriodEnd | The exclusive end bound of a billing period | 2024-02-01T00:00:00Z |
| BillingPeriodStart | The inclusive start bound of a billing period | 2024-01-01T00:00:00Z |
| ChargeCategory | The highest level classification of a charge based on how it is billed | Usage |
| ChargeDescription | A self contained summary of the charge’s purpose | Actions \- Tier 1 |
| ChargeFrequency | Indicates how often a charge will occur | Usage-Based |
| ChargePeriodEnd | Time period end from when this charge took place, correlates to data granularity | 2025-10-01T01:00:00.000Z |
| ChargePeriodStart | Time period start from when this charge took place, correlates to data granularity | 2025-10-01T00:00:00.000Z |
| ContractedCost | Cost calculated by multiplying ContractedUnitPrice and PricingQuantity | 100.00 |
| ContractedUnitPrice | The agreed-upon unit price for a single pricing unit of the associated SKU. Inclusive of negotiated discounts | 10.00 |
| InvoiceID | The ID of the invoice for this billing period | in\_XXXXXXXXXXXXXXXXXXXX |
| InvoiceIssuer | The entity responsible for issuing payable invoices | stripe |
| PricingQuantity | The volume of a given SKU used or purchased | 10.00 |
| PricingUnit | The measurement unit used for PricingQuantity | 1 Million Actions |
| Provider | The provider of purchased resources or services | Temporal Technologies |
| Publisher | The publisher of purchased resources or services | Temporal Technologies |
| ResourceID | Namespace name \+ Temporal Cloud account ID | production.a2dd6 |
| ResourceName | Namespace name \+ Temporal Cloud account ID | production.a2dd6 |
| ResourceType | The type of resource the charge applies to | Namespace |
| ServiceCategory | The highest level classification of a service based on the core function of the service | Temporal Cloud |
| ServiceName | An offering that can be purchased from a provider | Temporal Cloud |
| ServiceSubcategory | A secondary classification of the service category for a service based on its core function | Actions |
| SKUID | A unique identifier that represents a specific SKU | essentials-actions |
| SKUMeter | The functionality being metered or measured by a particular SKU in a charge | Actions |
| Tags | Provider and customer defined tags associated with resources | `{"$tmprl_project":["project-id"],"namespace-tag-key":["namespace-tag-value"]}` |

## Generate a report

To generate a report, follow these steps:

1. Create a billing report using `CreateBillingReport`. The response includes a `billing_report_id` and `async_operation_id`.
1. Poll `GetBillingReport` using the `billing_report_id`
1. When the report state becomes `BILLING_REPORT_STATE_GENERATED`, retrieve the download URL
1. Download the report before the URL expires

### Key identifiers

| Identifier | Purpose |
| ----- | ----- |
| `billing_report_id` | Identifies the billing report and is used to retrieve metadata and download URLs |
| `async_operation_id` | Identifies the background operation responsible for generating the report |

The async operation follows the standard Cloud Operations async model (see [Async Operations](/ops#per-identity-rate-limits)).

---

## Billing Center

## Current balance {/* #current-balance */}

Your current balance card shows the balance for your current billing cycle and the date it was last updated.
This balance adjusts with use and appears on the first line of your Invoices table.

:::note Billing Cycles

Billing cycles normally begin on the first of the month (UTC).
The minimum plan fee for your first month is prorated based on your sign-up date.

:::

## Recent bill {/* #recent-bill */}

The "Recent Bill" card displays the previous bill amount.

![Recent bill card showing a balance of $0.00](/img/cloud/billing/billing-card.png)

- If you pay your invoices through Stripe, you'll see a **Pay Now** button.
  It takes you to the Stripe portal to complete your payment
- If your account is set up for auto-payment, you don’t need to manually pay bills.
  However, you can choose to make manual payments whenever you wish

## Invoices {/* #invoice */}

To review your invoices, follow these steps:

1. Click **Billing** on your left-side vertical navigation.
2. Under the **Invoices** section, select and download the invoice(s) you want to review.

The Invoices table shows the following information:

- Date (UTC): The date range covered by the invoice
- Type: The type of invoice, such as credit purchase or cloud usage
- Status: The current status of the invoice, such as paid or pending
- Credit Granted: The total credits added to your account
- Credit Purchase Amount: The amount paid for purchasing credits
- Credit Usage: The credits used during the billing cycle
- Subtotal: The total amount of the invoice before any adjustments
- Balance Due: The amount to pay after applying credits

![Billing page showing Invoices tab](/img/cloud/billing/billing-invoices.png)

You may download your Invoices prior to this calendar month by clicking the download icon by the date.

:::note Current Month Invoice

During the current billing period, your invoice will not be finalized and the download option will not be available.

:::

## Credits {/* #credit-table */}

The following information appears under the credits table:

- Effective At (UTC): The date when the credit grant became effective
- Type: Indicates whether the transaction was a deduction, expiry, or grant
- Amount: The credit amount that was granted, deducted, or expired
- Credits Remaining: The remaining credit available in the account

![Billing page showing Credits tab](/img/cloud/billing/billing-credits.png)

## Cost by Namespace {/* #cost-by-namespace */}

:::tip Temporal Cloud Billing API in Public Preview

The [Temporal Cloud Billing API](/cloud/billing-api) allows you to access billing information on a Namespace basis to an hourly granularity, enriched with Tags and Projects. The Billing API will replace the Cost by Namespace UI.

:::

Account Owners and Finance Admins can access a cost column on the Usage page.
This allows you to monitor your cost on a per Namespace basis.
If your organization separates work by Namespace—for development, production, or different products—you can view costs for each.

![Billing page showing Usage](/img/cloud/billing/billing-usage.png)

:::note Cost Breakdown Limitations

Namespace cost details are not available for "last 90 days" or "last 120 days".

Cost breakdowns distribute the total usage cost to namespaces proportionally based on their metered usage. The proration
reflects your effective price, factoring in included Actions/Storage and tiered pricing rates in your Temporal plan.

:::

## Plans {/* #plans */}

Account Owners and Finance Admins can access their Temporal Plan information on the plans page.
For customers on a standard agreement you will be able to:

- View current plan information, pricing details and entitlements
- View other available plans, pricing details and entitlements
- View Pay-as-You-Go pricing rates applicable to your plan
- Upgrade and Downgrade between plans available on a standard agreement

![Billing page showing Plans tab](/img/cloud/billing/billing-plans.png)

Requests to upgrade your plan are processed immediately and you will be billed on a pro-rated basis for that billing period.
Your monthly entitlements will reflect the full volume of included Actions and Storage of the upgrade plan for that billing month.
After an upgrade, a downgrade cannot be processed until the following billing period.

Requests to downgrade will be processed immediately. Billing and entitlements will be backdated to the beginning of the billing period.

## Account Cancellation

The way you created your Temporal account determines how you can cancel your subscription and remove the account.

- **For accounts managed by our sales team**.
  Please submit a support ticket so we can help you.

- **For accounts created through our self-signup portal**.
  Account owners can delete their accounts on the Temporal Cloud Billing page, under the **Plan** tab.
  If you're no longer using Temporal Cloud, use the Delete Account button to begin the process.

  - Permanently deleted accounts will immediately cease billing and be scheduled for full deletion within 72 hours.

  - Account Data and Active Storage will be permanently deleted. Retained Storage will be deleted in accordance with its configured retention period.

![Billing page showing the Plan tab. The contents on the tab include "Manage Payment Method" and "Delete Account" buttons. The "Delete Account" button is placed below text asking "No longer using Temporal Cloud?"](/img/cloud/billing/billing-cancel.png)

---

## Billing and usage management

Temporal Cloud provides billing and costs information for your account.
Use this information to assess your spending patterns, inspect your credit ledger,
check your invoice histories, update payment details, and manage your current plan as needed.

For more information on current Temporal Cloud pricing for Actions, storage, and services/support,
please visit our [Pricing page](/cloud/pricing).

Usage on Temporal is measured in Actions and Storage.
This can help understand your bills, forecast usage, optimize Workflows, and troubleshoot errors.
You can view your Action usage in multiple ways.
The following tools are available for measuring Usage and Billing:

- **[Billing Center](/cloud/billing):** Allows you to see summary invoices and credits, manage plans, and delete your accounts.
    - Viewable by Account Owners and Finance Admin

- **[Billing API](/cloud/billing-api):** Allows you to access billing information on a Namespace basis down to an hourly granularity, enriched with Tags and Projects. The Billing API provides a FOCUS-guided data format that can be ingested into your cloud cost management platform or analytics tooling.
  - Viewable by Account Owners and Finance Admin

  <ReleaseNoteHeader
    type="publicPreview"
  />

- **[Usage Dashboards](/cloud/actions-usage):** Aggregate Actions on a Namespace level and includes Action categories that groups similar types of Actions as seen in [Actions](/cloud/actions). Available in the Cloud UI in the usage dashboard and Namespace overview pages.
    - Viewable by Account Owners, Finance Admin, Global Admin on an account level. Namespace level usage is visible on the Namespace pages to those with access.

- **[Actions in Event History](/cloud/actions-usage#actions-in-workflows):** Highlights Actions in a given Event History via the Temporal Cloud UI. Note that some Actions are not measured in Workflow histories.
    - Viewable by Account Owners, Global Admin and Namespace Admin, Developers and Read-only

- **[Actions Metrics](/cloud/metrics/openmetrics/metrics-reference#temporal_cloud_v1_billable_action_count):** A high cardinality billable action metric that include labels for Category, Action Type, Workflow Type and Namespace down to minute granularity.
    - Viewable by creating a service account with the "Metrics Read-Only" role. See the [OpenMetrics](/cloud/metrics/openmetrics#api-key-authentication) page for more information.

  <ReleaseNoteHeader
    type="publicPreview"
  />

---

## Capacity modes

Each Namespace in Temporal has a rate limit, which is measured in [Actions](/cloud/pricing#action) per second.
Temporal offers two different modes for adjusting capacity: On-Demand Capacity or Provisioned Capacity.
With On-Demand Capacity, Namespace capacity is increased automatically along with usage.
With Provisioned Capacity, you can control your capacity limits by requesting Temporal Resource Units (TRUs).

## Namespace Capacity

Namespaces in Temporal can be set to either an **On-Demand** or **Provisioned Capacity** Mode.
These modes govern how limits are assigned to a Namespace.

Actions Per Second (APS) is the primary limit for Namespaces and is based on the operating billable Actions that occur each second.
Some Actions can result in multiple back-end operations, so limits are also set on Requests Per Second (RPS) and Operations Per Second (OPS) to maintain reliability.

See [Service-level RPS limits](/references/dynamic-configuration#service-level-rps-limits) for more about RPS.
See the [operations list](/references/operation-list) for the list of operations.
See the [Actions page](/cloud/actions) for the list of actions.

:::tip Measuring throughput with APS, RPS, and OPS

APS, RPS, and OPS are all measures of throughput that apply to different aspects of Temporal.

APS, or Actions Per Second, is specific to Temporal Cloud.
It measures the rate at which Actions, like starting or signaling a Workflow, can be performed in a specific Namespace.
Temporal Cloud uses APS to protect the system from sudden major spikes in load.

RPS, or Requests Per Second, is used in the Temporal Service, both in self-hosted Temporal and Temporal Cloud.
It measures and controls the rate of gRPC requests to the Service.
This is a lower-level measure that manages rates at the service level.

OPS, or Operations per Second, is used by Temporal Cloud.
An operation is anything a user does directly, or that Temporal does on behalf of the user in the background, that results in load on Temporal Server.
This is a lower-level measure that manages rates across Temporal cloud services.

In summary, APS is a higher-level measure to limit and mitigate Action spikes in Temporal Cloud.
RPS and OPS  are lower-level measures to control and balance request rates at the service level.

:::

### What happens when my Actions Rate exceeds my Limit?

When your Action rate exceeds your quota, Temporal Cloud throttles Actions.
Throttling limits the rate at which Actions are performed to prevent the Namespace from exceeding its APS limit.

**How throttling works:**
- Low-priority operations are throttled first; higher-priority operations (like starting or signaling Workflows) continue when possible.
- Rate limiting is not instantaneous, so usage may briefly exceed your limit before throttling takes effect.
- When throttled, the server returns `ResourceExhausted` errors that SDK clients automatically retry.
- If throttling persists beyond the SDK's retry limit, client calls can fail.

**To avoid data loss during throttling:**
- Log any failed client calls (with payloads) so you can retry or backfill later.
- Set up [limit metrics](/cloud/metrics/openmetrics/metrics-reference#limit-metrics) to alert when approaching your limits.

See [Throttling behavior](/cloud/limits#throttling-behavior) for more details.

Your rate limits can be adjusted automatically over time or provisioned manually with Capacity Modes.

We recommend tracking your Actions Rate and Limits using Temporal metrics to assess your use cases specific needs.
See [Monitoring Trends Against Limits](/cloud/service-health#rps-aps-rate-limits) to track usage trends.

For Namespaces using Provisioned Capacity, on-demand envelope metrics show what your limits would be if operating in on-demand mode.
Use these to evaluate whether on-demand capacity would meet your needs before switching modes.
See [On-demand envelope limits](/cloud/service-health#on-demand-envelope-limits) for details.

:::note Actions that don't count against APS
Actions that are external to the core Temporal service do not contribute to your APS. These Calls include:
* [Export](/cloud/export)
* Capacity Related Actions
:::

## On-Demand Capacity {/* #on-demand-capacity */}

Using On-Demand Capacity, your rate limit grows automatically along with your usage.

|               | Actions Per Second | Requests Per Second | Operations Per Second|
|---------------|--------------------|---------------------|----------------------|
| Default Limit | 500                | 2000                | 4000                 |

Scaling automatically adjusts based on the lesser of 4 * APS Average or 2 * APS P90 over the past 7 days.

If you experience usage spikes, you may hit a throughput limit.
In that case, consider switching to [Provisioned Capacity](#provisioned-capacity).
You can also optimize your workload to remain under the On-Demand limits. See [Best Practices for Managing APS Limits](/best-practices/managing-aps-limits) for more information.

### What kind of throughput can I get on Temporal Cloud with On-Demand Capacity?

Each Namespace has a rate limit, which is measured in Actions per second (APS).
A Namespace's default limit is set at 500 APS and automatically adjusts based on a formula that compares your average usage over the last 7 days and your usage at the 90th percentile, or P90.
Your throughput limit will never fall below the default value.
Under On-Demand capacity you are only charged for the Actions you use.

For example: If your average APS in the last 7 days was 200 APS, and your P90 was 500 APS, then your limit would be calculated as follows:
Greater of:
* Default limit of 500 APS
* The lesser of:
  * 4 * 200 APS Mean = 800 APS
  * 2 * 500 APS P90 = 1000 APS

This means that your default limit would be 800 APS.

![Usage graph showing increasing APS usage for one month, with occasional spikes, and a rising APS limit](/img/cloud/provisioned-capacity/usage_graph.png)

## Provisioned Capacity {/* #provisioned-capacity */}

Provisioned Capacity provides an alternative to On-Demand Capacity by allowing you to control the limits on your Namespace based on your specific need.

|               | Actions Per Second | Requests Per Second | Operations Per Second|
|---------------|--------------------|---------------------|----------------------|
| TRU           | 500                | 1500                | 4000                 |

Customers can set 2, 3, 4, 6, 8, 10, 12 TRUs, subject to availability. TRUs can be adjusted hourly.

See [Capacity Mode Pricing](/cloud/pricing#capacity-modes-pricing) for pricing implications.

### What kind of throughput can I get with Temporal Cloud with Provisioned Capacity?
