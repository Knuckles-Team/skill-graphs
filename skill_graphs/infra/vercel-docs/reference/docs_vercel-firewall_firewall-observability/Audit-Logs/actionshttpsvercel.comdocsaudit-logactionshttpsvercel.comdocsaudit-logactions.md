##  [`actions`](https://vercel.com/docs/audit-log#actions)[](https://vercel.com/docs/audit-log#actions)
Vercel logs the following list of `actions` performed by team members.
###  [`alias`](https://vercel.com/docs/audit-log#alias)[](https://vercel.com/docs/audit-log#alias)
Maps a custom domain or subdomain to a specific deployment or URL of a project. To learn more, see the `vercel alias` [docs](https://vercel.com/docs/cli/alias).
Action Name | Description
---|---
`alias.created` | Indicates that a new alias was created
`alias.deleted` | Indicates that an alias was deleted
`alias.protection-user-access-request-requested` | An external user requested access to a protected deployment alias URL
###  [`auditlog`](https://vercel.com/docs/audit-log#auditlog)[](https://vercel.com/docs/audit-log#auditlog)
Refers to the audit logs of your Vercel team account.
Action Name | Description
---|---
`auditlog.export.downloaded` | Indicates that an export of the audit logs was downloaded
`auditlog.export.requested` | Indicates that an export of the audit logs was requested
###  [`cert`](https://vercel.com/docs/audit-log#cert)[](https://vercel.com/docs/audit-log#cert)
A digital certificate to manage SSL/TLS certificates for your custom domains through the [vercel certs](https://vercel.com/docs/cli/certs) command. It is used to authenticate the identity of a server and establish a secure connection.
Action Name | Description
---|---
`cert.created` | Indicates that a new certificate was created
`cert.deleted` | Indicates that a new certificate was deleted
`cert.renewed` | Indicates that a new certificate was renewed
###  [`deploy_hook`](https://vercel.com/docs/audit-log#deploy_hook)[](https://vercel.com/docs/audit-log#deploy_hook)
Create URLs that accept HTTP POST requests to trigger deployments and rerun the build step. To learn more, see the [Deploy Hooks](https://vercel.com/docs/deploy-hooks) docs.
Action Name | Description
---|---
`deploy_hook.deduped` | A deploy hook is de-duplicated which means that multiple instances of the same hook have been combined into one
###  [`deployment`](https://vercel.com/docs/audit-log#deployment)[](https://vercel.com/docs/audit-log#deployment)
Refers to a successful build of your application. To learn more, see the [deployment](https://vercel.com/docs/deployments) docs.
Action Name | Description
---|---
`deployment.deleted` | Indicates that a deployment was deleted
`deployment.job.errored` | Indicates that a job in a deployment has failed with an error
###  [`domain`](https://vercel.com/docs/audit-log#domain)[](https://vercel.com/docs/audit-log#domain)
A unique name that identifies your website. To learn more, see the [domains](https://vercel.com/docs/domains) docs.
Action Name | Description
---|---
`domain.auto_renew.changed` | Indicates that the auto-renew setting for a domain was changed
`domain.buy` | Indicates that a domain was purchased
`domain.created` | Indicates that a new domain was created
`domain.delegated` | Indicates that a domain was delegated to another account
`domain.deleted` | Indicates that a domain was deleted
`domain.move_out.requested` | Indicates that a request was made to move a domain out of the current account
`domain.moved_in` | Indicates that a domain was moved into the current account
`domain.moved_out` | Indicates that a domain was moved out of the current account
`domain.record.created` | Indicates that a new domain record was created
`domain.record.deleted` | Indicates that a new domain record was deleted
`domain.record.updated` | Indicates that a new domain record was updated
`domain.transfer_in` | Indicates that a request was made to transfer a domain into the current account
`domain.transfer_in.canceled` | Indicates that a request to transfer a domain into the current account was canceled
`domain.transfer_in.completed` | Indicates that a domain was transferred into the current account
###  [`edge_config`](https://vercel.com/docs/audit-log#edge_config)[](https://vercel.com/docs/audit-log#edge_config)
A key-value data store associated with your Vercel account that enables you to read data in the region closest to the user without querying an external database. To learn more, see the [Edge Config docs](https://vercel.com/docs/edge-config).
Action Name | Description
---|---
`edge_config.created` | Indicates that a new edge configuration was created
`edge_config.deleted` | Indicates that a new edge configuration was deleted
`edge_config.updated` | Indicates that a new edge configuration was updated
###  [`integration`](https://vercel.com/docs/audit-log#integration)[](https://vercel.com/docs/audit-log#integration)
Helps you pair Vercel's functionality with a third-party service to streamline installation, reduce configuration, and increase productivity. To learn more, see the [integrations docs](https://vercel.com/docs/integrations).
Action Name | Description
---|---
`integration.deleted` | Indicates that an integration was deleted
`integration.installed` | Indicates that an integration was installed
`integration.updated` | Indicates that an integration was updated
###  [`password_protection`](https://vercel.com/docs/audit-log#password_protection)[](https://vercel.com/docs/audit-log#password_protection)
[Password Protection](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/password-protection) allows visitors to access preview deployments with a password to manage team-wide access.
Action Name | Description
---|---
`password_protection.disabled` | Indicates that password protection was disabled
`password_protection.enabled` | Indicates that password protection was enabled
###  [`preview_deployment_suffix`](https://vercel.com/docs/audit-log#preview_deployment_suffix)[](https://vercel.com/docs/audit-log#preview_deployment_suffix)
Customize the appearance of your preview deployment URLs by adding a valid suffix. To learn more, see the [preview deployment suffix](https://vercel.com/docs/deployments/generated-urls#preview-deployment-suffix) docs.
Action Name | Description
---|---
`preview_deployment_suffix.disabled` | Indicates that the preview deployment suffix was disabled
`preview_deployment_suffix.enabled` | Indicates that the preview deployment suffix was enabled
`preview_deployment_suffix.updated` | Indicates that the preview deployment suffix was updated
###  [`project`](https://vercel.com/docs/audit-log#project)[](https://vercel.com/docs/audit-log#project)
Refers to actions performed on your Vercel [projects](https://vercel.com/docs/projects/overview).
Action Name | Description
---|---
`project.analytics.disabled` | Indicates that analytics were disabled for the project
`project.analytics.enabled` | Indicates that analytics were enabled for the project
`project.deleted` | Indicates that a project was deleted
`project.env_variable` | This field refers to an environment variable within a project
`project.env_variable.created` | Indicates that a new environment variable was created for the project
`project.env_variable.deleted` | Indicates that a new environment variable was deleted for the project
`project.env_variable.updated` | Indicates that a new environment variable was updated for the project
###  [`project.password_protection`](https://vercel.com/docs/audit-log#project.password_protection)[](https://vercel.com/docs/audit-log#project.password_protection)
Refers to the password protection settings for a project.
Action Name | Description
---|---
`project.password_protection.disabled` | Indicates that password protection was disabled for the project
`project.password_protection.enabled` | Indicates that password protection was enabled for the project
`project.password_protection.updated` | Indicates that password protection was updated for the project
###  [`project.sso_protection`](https://vercel.com/docs/audit-log#project.sso_protection)[](https://vercel.com/docs/audit-log#project.sso_protection)
Refers to the [Single Sign-On (SSO)](https://vercel.com/docs/saml) protection settings for a project.
Action Name | Description
---|---
`project.sso_protection.disabled` | Indicates that SSO protection was disabled for the project
`project.sso_protection.enabled` | Indicates that SSO protection was enabled for the project
`project.sso_protection.updated` | Indicates that SSO protection was updated for the project
###  [`project.rolling_release`](https://vercel.com/docs/audit-log#project.rolling_release)[](https://vercel.com/docs/audit-log#project.rolling_release)
Refers to [Rolling Releases](https://vercel.com/docs/rolling-releases) for a project, which allow you to gradually roll out deployments to production.
Action Name | Description
---|---
`project.rolling_release.aborted` | Indicates that a rolling release was aborted
`project.rolling_release.approved` | Indicates that a rolling release was approved to advance to the next stage
`project.rolling_release.completed` | Indicates that a rolling release was completed successfully
`project.rolling_release.configured` | Indicates that the rolling release configuration was updated for the project
`project.rolling_release.deleted` | Indicates that a rolling release was deleted
`project.rolling_release.started` | Indicates that a rolling release was started
###  [`project.transfer`](https://vercel.com/docs/audit-log#project.transfer)[](https://vercel.com/docs/audit-log#project.transfer)
Refers to the transfer of a project between Vercel accounts.
Action Name | Description
---|---
`project.transfer_in.completed` | Indicates that a project transfer into the current account was completed successfully
`project.transfer_in.failed` | Indicates that a project transfer into the current account was failed
`project.transfer_out.completed` | Indicates that a project transfer out of the current account was completed successfully
`project.transfer_out.failed` | Indicates that a project transfer out of the current account was
`project.transfer.started` | Indicates that a project transfer was initiated
###  [`project.web-analytics`](https://vercel.com/docs/audit-log#project.web-analytics)[](https://vercel.com/docs/audit-log#project.web-analytics)
Refers to the generation of web [analytics](https://vercel.com/docs/analytics) for a Vercel project.
Action Name | Description
---|---
`project.web-analytics.disabled` | Indicates that web analytics were disabled for the project
`project.web-analytics.enabled` | Indicates that web analytics were enabled for the project
###  [`shared_env_variable`](https://vercel.com/docs/audit-log#shared_env_variable)[](https://vercel.com/docs/audit-log#shared_env_variable)
Refers to environment variables defined at the team level. To learn more, see the [shared environment variables](https://vercel.com/docs/environment-variables/shared-environment-variables) docs.
Action Name | Description
---|---
`shared_env_variable.created` | Indicates that a new shared environment variable was created
`shared_env_variable.decrypted` | Indicates that a new shared environment variable was decrypted
`shared_env_variable.deleted` | Indicates that a new shared environment variable was deleted
`shared_env_variable.updated` | Indicates that a new shared environment variable was updated
###  [`team`](https://vercel.com/docs/audit-log#team)[](https://vercel.com/docs/audit-log#team)
Refers to actions performed by members of a Vercel [team](https://vercel.com/docs/accounts/create-a-team).
Action Name | Description
---|---
`team.avatar.updated` | Indicates that the avatar (profile picture) associated with the team was updated
`team.created` | Indicates that a new team was created
`team.deleted` | Indicates that a new team was deleted
`team.name.updated` | Indicates that the name of the team was updated
`team.slug.updated` | Indicates that the team's unique identifier, or "slug," was updated
###  [`team.member`](https://vercel.com/docs/audit-log#team.member)[](https://vercel.com/docs/audit-log#team.member)
Refers to actions performed by any [team member](https://vercel.com/docs/accounts/team-members-and-roles).
Action Name | Description
---|---
`team.member.access_request.confirmed` | Indicates that an access request by a team member was confirmed
`team.member.access_request.declined` | Indicates that an access request by a team member was declined
`team.member.access_request.requested` | Indicates that a team member has requested access to the team
`team.member.added` | Indicates that a new member was added to the team
`team.member.deleted` | Indicates that a member was removed from the team
`team.member.joined` | Indicates that a member has joined the team
`team.member.left` | Indicates that a new member has left the team
`team.member.role.updated` | Indicates that the role of a team member was updated
* * *
[ Previous Overview ](https://vercel.com/docs/security)[ Next Firewall ](https://vercel.com/docs/vercel-firewall)
Was this helpful?
Send
On this page
  * [Export audit logs](https://vercel.com/docs/audit-log#export-audit-logs)
  * [Custom SIEM Log Streaming](https://vercel.com/docs/audit-log#custom-siem-log-streaming)
  * [Allowlisting IP addresses](https://vercel.com/docs/audit-log#allowlisting-ip-addresses)
  * [Setup process](https://vercel.com/docs/audit-log#setup-process)
  * [Audit Logs CSV file structure](https://vercel.com/docs/audit-log#audit-logs-csv-file-structure)
  * [actions](https://vercel.com/docs/audit-log#actions)
  * [alias](https://vercel.com/docs/audit-log#alias)
  * [auditlog](https://vercel.com/docs/audit-log#auditlog)
  * [cert](https://vercel.com/docs/audit-log#cert)
  * [deploy_hook](https://vercel.com/docs/audit-log#deploy_hook)
  * [deployment](https://vercel.com/docs/audit-log#deployment)
  * [domain](https://vercel.com/docs/audit-log#domain)
  * [edge_config](https://vercel.com/docs/audit-log#edge_config)
  * [integration](https://vercel.com/docs/audit-log#integration)
  * [password_protection](https://vercel.com/docs/audit-log#password_protection)
  * [preview_deployment_suffix](https://vercel.com/docs/audit-log#preview_deployment_suffix)
  * [project](https://vercel.com/docs/audit-log#project)
  * [project.password_protection](https://vercel.com/docs/audit-log#project.password_protection)
  * [project.sso_protection](https://vercel.com/docs/audit-log#project.sso_protection)
  * [project.rolling_release](https://vercel.com/docs/audit-log#project.rolling_release)
  * [project.transfer](https://vercel.com/docs/audit-log#project.transfer)
  * [project.web-analytics](https://vercel.com/docs/audit-log#project.web-analytics)
  * [shared_env_variable](https://vercel.com/docs/audit-log#shared_env_variable)
  * [team](https://vercel.com/docs/audit-log#team)
  * [team.member](https://vercel.com/docs/audit-log#team.member)


Copy as MarkdownGive feedbackAsk AI about this page
Audit Logs
