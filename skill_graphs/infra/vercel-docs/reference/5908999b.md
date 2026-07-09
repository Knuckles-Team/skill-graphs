##  [Response](https://vercel.com/docs/rest-api/sdk/projects/find-a-project-by-id-or-name#response)[](https://vercel.com/docs/rest-api/sdk/projects/find-a-project-by-id-or-name#response)
200The project information
integrationsarrayOptional
+Show 2 properties
accountIdstringRequired
analyticsobjectOptional
+Show 7 properties
appliedCve55182MigrationbooleanOptional
+Show 2 enum values
speedInsightsobjectOptional
+Show 6 properties
autoExposeSystemEnvsbooleanOptional
+Show 2 enum values
autoAssignCustomDomainsbooleanOptional
+Show 2 enum values
autoAssignCustomDomainsUpdatedBystringOptional
buildCommandstringOptional
commandForIgnoringBuildStepstringOptional
connectConfigurationsarrayOptional
+Show 8 properties
connectConfigurationIdstringOptional
connectBuildsEnabledbooleanOptional
+Show 2 enum values
passiveConnectConfigurationIdstringOptional
createdAtnumberOptional
customerSupportCodeVisibilitybooleanOptional
+Show 2 enum values
cronsobjectOptional
+Show 5 properties
dataCacheobjectOptional
+Show 3 properties
deploymentExpirationobjectRequired
Retention policies for deployments. These are enforced at the project level, but we also maintain an instance of this at the team level as a default policy that gets applied to new projects.
+Show 5 properties
devCommandstringOptional
directoryListingbooleanRequired
+Show 2 enum values
installCommandstringOptional
envarrayOptional
+Show 21 properties
customEnvironmentsarrayOptional
+Show 9 properties
frameworkstringOptional
+Show 65 enum values
gitForkProtectionbooleanOptional
+Show 2 enum values
gitLFSbooleanOptional
+Show 2 enum values
idstringRequired
ipBucketsarrayOptional
+Show 2 properties
latestDeploymentsarrayOptional
+Show 21 properties
linkobjectOptional5 variants
+Show 5 variants
microfrontendsobjectOptional3 variants
+Show 3 variants
namestringRequired
nodeVersionstringRequired
+Show 9 enum values
optionsAllowlistobjectOptional
+Show 1 properties
outputDirectorystringOptional
passwordProtectionobjectOptional
productionDeploymentsFastLanebooleanOptional
+Show 2 enum values
publicSourcebooleanOptional
+Show 2 enum values
resourceConfigobjectRequired
+Show 11 properties
rollbackDescriptionobjectOptional
Description of why a project was rolled back, and by whom. Note that lastAliasRequest contains the from/to details of the rollback.
+Show 4 properties
rollingReleaseobjectOptional
Project-level rolling release configuration that defines how deployments should be gradually rolled out
+Show 3 properties
defaultResourceConfigobjectRequired
+Show 11 properties
rootDirectorystringOptional
serverlessFunctionZeroConfigFailoverbooleanOptional
+Show 2 enum values
skewProtectionBoundaryAtnumberOptional
skewProtectionMaxAgenumberOptional
skewProtectionAllowedDomainsarrayOptional
skipGitConnectDuringLinkbooleanOptional
+Show 2 enum values
staticIpsobjectOptional
+Show 3 properties
sourceFilesOutsideRootDirectorybooleanOptional
+Show 2 enum values
enableAffectedProjectsDeploymentsbooleanOptional
+Show 2 enum values
ssoProtectionobjectOptional
+Show 2 properties
targetsobjectOptional
transferCompletedAtnumberOptional
transferStartedAtnumberOptional
transferToAccountIdstringOptional
transferredFromAccountIdstringOptional
updatedAtnumberOptional
livebooleanOptional
+Show 2 enum values
enablePreviewFeedbackbooleanOptional
+Show 2 enum values
enableProductionFeedbackbooleanOptional
+Show 2 enum values
permissionsobjectOptional
+Show 229 properties
lastRollbackTargetobjectOptional
lastAliasRequestobjectOptional
+Show 6 properties
protectionBypassobjectOptional
hasActiveBranchesbooleanOptional
+Show 2 enum values
trustedIpsobjectOptional2 variants
+Show 2 variants
gitCommentsobjectOptional
+Show 2 properties
gitProviderOptionsobjectOptional
+Show 3 properties
pausedbooleanOptional
+Show 2 enum values
concurrencyBucketNamestringOptional
webAnalyticsobjectOptional
+Show 5 properties
securityobjectOptional
+Show 12 properties
oidcTokenConfigobjectOptional
+Show 2 properties
tierstringOptional
+Show 4 enum values
scheduledTierChangeobjectOptional
+Show 2 properties
usageStatusobjectOptional
+Show 3 properties
featuresobjectOptional
+Show 1 properties
v0booleanOptional
+Show 2 enum values
abuseobjectOptional
+Show 6 properties
internalRoutesarrayOptional
+Show 2 properties
hasDeploymentsbooleanOptional
+Show 2 enum values
dismissedToastsarrayOptional
+Show 4 properties
protectedSourcemapsbooleanOptional
+Show 2 enum values
