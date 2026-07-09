# Deployment Retention
Last updated December 17, 2025
Deployment Retention is available on [all plans](https://vercel.com/docs/plans)
Deployment retention refers to the configured policies that determine how long different types of deployments are kept before they are automatically deleted.
These configured retention policies allow you to control how long your deployment data is stored, providing:
  * Enhanced protection: Remove outdated deployments with potential vulnerabilities or sensitive data
  * Compliance support: Configure retention policies to align with your compliance requirements.
  * Efficient storage management: Automatically clear out unnecessary deployments


Vercel provides unlimited deployment retention for all deployments, regardless of the plan that you are on.
You can configure retention durations for the following deployment states:
  * Canceled deployments
  * Errored deployments
  * Preview deployments
  * Production deployments


For example, imagine you created a production deployment with a 60-day retention period on 01/01/2024 and later replaced it with a newer deployment. The origin deployment would expire on 03/01/2024, entering the recovery period, and users accessing it would see a 410 status code. If required, you could still restore it until 03/31/2024, when all associated resources are permanently removed and restoring the deployment is no longer possible.
Once a policy is enabled on a project, deployments within the retention period will start to be automatically marked for deletion, within a few days of enabling the policy.
