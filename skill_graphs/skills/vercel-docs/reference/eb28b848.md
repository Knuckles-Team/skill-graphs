##  [Body](https://vercel.com/docs/rest-api/sdk/projects/create-a-new-project#body)[](https://vercel.com/docs/rest-api/sdk/projects/create-a-new-project#body)
application/json
enablePreviewFeedbackbooleanOptional
Opt-in to preview toolbar on the project level
enableProductionFeedbackbooleanOptional
Opt-in to production toolbar on the project level
previewDeploymentsDisabledbooleanOptional
Specifies whether preview deployments are disabled for this project.
previewDeploymentSuffixstringOptional
Custom domain suffix for preview deployments. Takes precedence over team-level suffix. Must be a domain owned by the team.
buildCommandstringOptional
The build command for this project. When `null` is used this value will be automatically detected
commandForIgnoringBuildStepstringOptional
devCommandstringOptional
The dev command for this project. When `null` is used this value will be automatically detected
environmentVariablesarrayOptional
Collection of ENV Variables the Project will use
+Show 5 properties
frameworkobjectOptional
The framework that is being used for this project. When `null` is used no framework is selected
+Show 66 enum values
gitRepositoryobjectOptional
The Git Repository that will be connected to the project. When this is defined, any pushes to the specified connected Git Repository will be automatically deployed
+Show 2 properties
installCommandstringOptional
The install command for this project. When `null` is used this value will be automatically detected
namestringRequired
The desired name for the project
skipGitConnectDuringLinkbooleanOptionalDeprecated
Opts-out of the message prompting a CLI user to connect a Git repository in `vercel link`.
ssoProtectionobjectOptional
The Vercel Auth setting for the project (historically named "SSO Protection")
+Show 1 properties
outputDirectorystringOptional
The output directory of the project. When `null` is used this value will be automatically detected
publicSourcebooleanOptional
Specifies whether the source code and logs of the deployments for this project should be public or not
rootDirectorystringOptional
The name of a directory or relative path to the source code of your project. When `null` is used it will default to the project root
serverlessFunctionRegionstringOptional
The region to deploy Serverless Functions in this project
serverlessFunctionZeroConfigFailoverbooleanOptional
oidcTokenConfigobjectOptional
OpenID Connect JSON Web Token generation configuration.
+Show 2 properties
enableAffectedProjectsDeploymentsbooleanOptional
Opt-in to skip deployments when there are no changes to the root directory and its dependencies
resourceConfigobjectOptional
Specifies resource override configuration for the project
+Show 11 properties
