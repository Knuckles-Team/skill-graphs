##  [Body](https://vercel.com/docs/rest-api/projects/update-an-existing-project#body)[](https://vercel.com/docs/rest-api/projects/update-an-existing-project#body)
application/json
autoExposeSystemEnvsbooleanOptional
autoAssignCustomDomainsbooleanOptional
autoAssignCustomDomainsUpdatedBystringOptional
buildCommandstringOptional
The build command for this project. When `null` is used this value will be automatically detected
commandForIgnoringBuildStepstringOptional
customerSupportCodeVisibilitybooleanOptional
Specifies whether customer support can see git source for a deployment
devCommandstringOptional
The dev command for this project. When `null` is used this value will be automatically detected
directoryListingbooleanOptional
frameworkstringOptional
The framework that is being used for this project. When `null` is used no framework is selected
+Show 66 enum values
gitForkProtectionbooleanOptional
Specifies whether PRs from Git forks should require a team member's authorization before it can be deployed
gitLFSbooleanOptional
Specifies whether Git LFS is enabled for this project.
protectedSourcemapsbooleanOptional
Specifies whether sourcemaps are protected and require authentication to access.
installCommandstringOptional
The install command for this project. When `null` is used this value will be automatically detected
namestringOptional
The desired name for the project
nodeVersionstringOptional
+Show 8 enum values
outputDirectorystringOptional
The output directory of the project. When `null` is used this value will be automatically detected
previewDeploymentsDisabledbooleanOptional
Specifies whether preview deployments are disabled for this project.
previewDeploymentSuffixstringOptional
Custom domain suffix for preview deployments. Takes precedence over team-level suffix. Must be a domain owned by the team.
publicSourcebooleanOptional
Specifies whether the source code and logs of the deployments for this project should be public or not
resourceConfigobjectOptional
Specifies resource override configuration for the project
+Show 11 properties
rootDirectorystringOptional
The name of a directory or relative path to the source code of your project. When `null` is used it will default to the project root
serverlessFunctionRegionstringOptional
The region to deploy Serverless Functions in this project
serverlessFunctionZeroConfigFailoverbooleanOptional
skewProtectionBoundaryAtintegerOptional
Deployments created before this absolute datetime have Skew Protection disabled. Value is in milliseconds since epoch to match "createdAt" fields.
skewProtectionMaxAgeintegerOptional
Deployments created before this rolling window have Skew Protection disabled. Value is in seconds to match "revalidate" fields.
skewProtectionAllowedDomainsarrayOptional
Cross-site domains allowed to fetch skew-protected assets (hostnames, optionally with leading wildcard like *.example.com).
skipGitConnectDuringLinkbooleanOptionalDeprecated
Opts-out of the message prompting a CLI user to connect a Git repository in `vercel link`.
sourceFilesOutsideRootDirectorybooleanOptional
Indicates if there are source files outside of the root directory
enablePreviewFeedbackbooleanOptional
Opt-in to preview toolbar on the project level
enableProductionFeedbackbooleanOptional
Opt-in to production toolbar on the project level
enableAffectedProjectsDeploymentsbooleanOptional
Opt-in to skip deployments when there are no changes to the root directory and its dependencies
staticIpsobjectOptional
Manage Static IPs for this project
+Show 1 properties
oidcTokenConfigobjectOptional
OpenID Connect JSON Web Token generation configuration.
+Show 2 properties
passwordProtectionobjectOptional
Allows to protect project deployments with a password
+Show 2 properties
ssoProtectionobjectOptional
Ensures visitors to your Preview Deployments are logged into Vercel and have a minimum of Viewer access on your team
+Show 1 properties
trustedIpsobjectOptional
Restricts access to deployments based on the incoming request IP address
+Show 3 properties
optionsAllowlistobjectOptional
Specify a list of paths that should not be protected by Deployment Protection to enable Cors preflight requests
+Show 1 properties
connectConfigurationsarrayOptional
The list of connections from project environment to Secure Compute network
+Show 4 properties
dismissedToastsarrayOptional
An array of objects representing a Dismissed Toast in regards to a Project. Objects are either merged with existing toasts (on key match), or added to the `dimissedToasts` array.`
+Show 4 properties
