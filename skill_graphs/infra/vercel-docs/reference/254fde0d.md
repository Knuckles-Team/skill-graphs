# Create a new deployment
POST`https://api.vercel.com/v13/deployments`
Create a new deployment with all the required and intended data. If the deployment is not a git deployment, all files must be provided with the request, either referenced or inlined. Additionally, a deployment id can be specified to redeploy a previous deployment.
TypeScriptNext.jscURL
https://api.vercel.com/v13/deployments
```


1

const response = await fetch('https://api.vercel.com/v13/deployments?forceNew=value&skipAutoDetectionConfirmation=value&teamId=string&slug=string', {






2

  method: 'POST',






3

  headers: {






4

    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',






5

    'Content-Type': 'application/json',






6

  },






7

  body: JSON.stringify({






8

    "customEnvironmentSlugOrId": "example_id",






9

    "deploymentId": "dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6",






10

    "files": [






11

      {






12

        "data": "string",






13

        "encoding": "base64",






14

        "file": "folder/file.js"






15

      }






16

    ],






17

    "gitMetadata": {






18

      "remoteUrl": "https://github.com/vercel/next.js",






19

      "commitAuthorName": "kyliau",






20

      "commitAuthorEmail": "kyliau@example.com",






21

      "commitMessage": "add method to measure Interaction to Next Paint (INP) (#36490)",






22

      "commitRef": "main",






23

      "commitSha": "dc36199b2234c6586ebe05ec94078a895c707e29",






24

      "dirty": "true",






25

      "ci": "true",






26

      "ciType": "github-actions",






27

      "ciGitProviderUsername": "rauchg",






28

      "ciGitRepoVisibility": "private"






29

    },






30

    "gitSource": {






31

      "ref": "main",






32

      "repoId": "123",






33

      "sha": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0",






34

      "type": "github"






35

    },






36

    "meta": "[object Object]",






37

    "monorepoManager": "string",






38

    "name": "my-instant-deployment",






39

    "project": "my-deployment-project",






40

    "projectSettings": {






41

      "buildCommand": "next build",






42

      "commandForIgnoringBuildStep": "string",






43

      "devCommand": "string",






44

      "framework": "null",






45

      "installCommand": "pnpm install",






46

      "nodeVersion": "24.x",






47

      "outputDirectory": "string",






48

      "rootDirectory": "string",






49

      "serverlessFunctionRegion": "string",






50

      "skipGitConnectDuringLink": "true",






51

      "sourceFilesOutsideRootDirectory": "true"






52

    },






53

    "target": "production",






54

    "withLatestCommit": "true"






55

  }),






56

});






57







58

const data = await response.json();






59

console.log(data);




```

Response
```


1

{






2

  "aliasAssignedAt": "123",






3

  "alwaysRefuseToBuild": "false",






4

  "build": {






5

    "env": []






6

  },






7

  "buildArtifactUrls": [],






8

  "builds": [






9

    {






10

      "use": "string",






11

      "src": "string",






12

      "config": "value"






13

    }






14

  ],






15

  "env": [],






16

  "inspectorUrl": "https://example.com",






17

  "isInConcurrentBuildsQueue": "false",






18

  "isInSystemBuildsQueue": "false",






19

  "projectSettings": {






20

    "nodeVersion": "24.x",






21

    "buildCommand": "string",






22

    "devCommand": "string",






23

    "framework": "blitzjs",






24

    "commandForIgnoringBuildStep": "string",






25

    "installCommand": "string",






26

    "outputDirectory": "string",






27

    "speedInsights": {






28

      "id": "icfg_1234567890",






29

      "enabledAt": "123",






30

      "disabledAt": "123",






31

      "canceledAt": "123",






32

      "hasData": "false",






33

      "paidAt": "123"






34

    },






35

    "webAnalytics": {






36

      "id": "icfg_1234567890",






37

      "disabledAt": "123",






38

      "canceledAt": "123",






39

      "enabledAt": "123",






40

      "hasData": "true"






41

    }






42

  },






43

  "readyStateReason": "Customer requested refund",






44

  "integrations": {






45

    "status": "skipped",






46

    "startedAt": "123",






47

    "completedAt": "123",






48

    "skippedAt": "123",






49

    "skippedBy": "string"






50

  },






51

  "images": {






52

    "sizes": [],






53

    "qualities": [],






54

    "domains": [],






55

    "remotePatterns": [






56

      {






57

        "protocol": "http",






58

        "hostname": "Example Name",






59

        "port": "string",






60

        "pathname": "Example Name",






61

        "search": "string"






62

      }






63

    ],






64

    "localPatterns": [






65

      {






66

        "pathname": "Example Name",






67

        "search": "string"






68

      }






69

    ],






70

    "minimumCacheTTL": "123",






71

    "formats": [],






72

    "dangerouslyAllowSVG": "false",






73

    "contentSecurityPolicy": "https://example.com",






74

    "contentDispositionType": "inline"






75

  },






76

  "alias": [],






77

  "aliasAssigned": "true",






78

  "bootedAt": "123",






79

  "buildingAt": "123",






80

  "buildContainerFinishedAt": "123",






81

  "buildSkipped": "false",






82

  "creator": {






83

    "uid": "96SnxkFiMyVKsK3pnoHfx3Hz",






84

    "username": "john-doe",






85

    "avatar": "string"






86

  },






87

  "initReadyAt": "123",






88

  "isFirstBranchDeployment": "false",






89

  "lambdas": [






90

    {






91

      "id": "icfg_1234567890",






92

      "createdAt": "123",






93

      "readyState": "BUILDING",






94

      "entrypoint": "string",






95

      "readyStateAt": "123",






96

      "output": [






97

        {






98

          "path": "string",






99

          "functionName": "Example Name"






100

        }






101

      ]






102

    }






103

  ],






104

  "public": "false",






105

  "ready": "123",






106

  "status": "QUEUED",






107

  "team": {






108

    "id": "icfg_1234567890",






109

    "name": "Example Name",






110

    "slug": "string",






111

    "avatar": "string"






112

  },






113

  "userAliases": [],






114

  "previewCommentsEnabled": "false",






115

  "ttyBuildLogs": "false",






116

  "customEnvironment": {






117

    "id": "icfg_1234567890",






118

    "slug": "string",






119

    "type": "production",






120

    "description": "string",






121

    "branchMatcher": {






122

      "type": "endsWith",






123

      "pattern": "string"






124

    },






125

    "domains": [






126

      {






127

        "name": "Example Name",






128

        "apexName": "Example Name",






129

        "projectId": "example_id",






130

        "redirect": "string",






131

        "redirectStatusCode": "307",






132

        "gitBranch": "string",






133

        "customEnvironmentId": "example_id",






134

        "updatedAt": "123",






135

        "createdAt": "123",






136

        "verified": "false",






137

        "verification": [






138

          {






139

            "type": "string",






140

            "domain": "string",






141

            "value": "string",






142

            "reason": "Customer requested refund"






143

          }






144

        ]






145

      }






146

    ],






147

    "currentDeploymentAliases": [],






148

    "createdAt": "123",






149

    "updatedAt": "123"






150

  },






151

  "oomReport": "out-of-memory",






152

  "aliasWarning": {






153

    "code": "string",






154

    "message": "string",






155

    "link": "string",






156

    "action": "string"






157

  },






158

  "id": "dpl_89qyp1cskzkLrVicDaZoDbjyHuDJ",






159

  "createdAt": "1540257589405",






160

  "readyState": "READY",






161

  "name": "my-project",






162

  "type": "LAMBDAS",






163

  "aliasError": {






164

    "code": "string",






165

    "message": "string"






166

  },






167

  "aliasFinal": "string",






168

  "autoAssignCustomDomains": "false",






169

  "automaticAliases": [],






170

  "buildErrorAt": "123",






171

  "checksState": "registered",






172

  "checksConclusion": "succeeded",






173

  "deletedAt": "1540257589405",






174

  "defaultRoute": "string",






175

  "canceledAt": "123",






176

  "errorCode": "string",






177

  "errorLink": "string",






178

  "errorMessage": "string",






179

  "errorStep": "string",






180

  "passiveRegions": [],






181

  "gitSource": {






182

    "type": "github",






183

    "repoId": "example_id",






184

    "ref": "string",






185

    "sha": "string",






186

    "prId": "123"






187

  },






188

  "manualProvisioning": {






189

    "state": "PENDING",






190

    "completedAt": "123"






191

  },






192

  "meta": "value",






193

  "originCacheRegion": "string",






194

  "nodeVersion": "24.x",






195

  "project": {






196

    "id": "icfg_1234567890",






197

    "name": "Example Name",






198

    "framework": "string"






199

  },






200

  "prebuilt": "false",






201

  "readySubstate": "STAGED",






202

  "regions": [],






203

  "softDeletedByRetention": "true",






204

  "source": "cli",






205

  "target": "null",






206

  "undeletedAt": "1540257589405",






207

  "url": "my-instant-deployment-3ij3cxz9qr.now.sh",






208

  "userConfiguredDeploymentId": "abc123",






209

  "version": "2",






210

  "oidcTokenClaims": {






211

    "iss": "string",






212

    "sub": "string",






213

    "scope": "string",






214

    "aud": "string",






215

    "owner": "string",






216

    "owner_id": "example_id",






217

    "project": "string",






218

    "project_id": "example_id",






219

    "environment": "string",






220

    "plan": "string"






221

  },






222

  "projectId": "example_id",






223

  "plan": "pro",






224

  "platform": {






225

    "source": {






226

      "name": "Example Name"






227

    },






228

    "origin": {






229

      "type": "id",






230

      "value": "string"






231

    },






232

    "creator": {






233

      "name": "Example Name",






234

      "avatar": "string"






235

    },






236

    "meta": "value"






237

  },






238

  "connectBuildsEnabled": "false",






239

  "connectConfigurationId": "example_id",






240

  "createdIn": "string",






241

  "crons": [






242

    {






243

      "schedule": "string",






244

      "path": "string"






245

    }






246

  ],






247

  "functions": "value",






248

  "monorepoManager": "string",






249

  "ownerId": "example_id",






250

  "passiveConnectConfigurationId": "example_id",






251

  "routes": [






252

    {






253

      "src": "string",






254

      "dest": "string",






255

      "headers": "value",






256

      "methods": [],






257

      "continue": "false",






258

      "override": "false",






259

      "caseSensitive": "false",






260

      "check": "false",






261

      "important": "false",






262

      "status": "123",






263

      "has": [






264

        {






265

          "type": "host",






266

          "value": "string"






267

        }






268

      ],






269

      "missing": [






270

        {






271

          "type": "host",






272

          "value": "string"






273

        }






274

      ],






275

      "mitigate": {






276

        "action": "challenge"






277

      },






278

      "transforms": [






279

        {






280

          "type": "request.headers",






281

          "op": "append",






282

          "target": {






283

            "key": "string"






284

          },






285

          "args": "string",






286

          "env": []






287

        }






288

      ],






289

      "env": [],






290

      "locale": {






291

        "redirect": "value",






292

        "cookie": "string"






293

      },






294

      "source": "string",






295

      "destination": "string",






296

      "statusCode": "123",






297

      "middlewarePath": "example_id",






298

      "middlewareRawSrc": [],






299

      "middleware": "123",






300

      "respectOriginCacheControl": "false"






301

    }






302

  ],






303

  "gitRepo": {






304

    "namespace": "Example Name",






305

    "projectId": "123",






306

    "type": "gitlab",






307

    "url": "https://example.com",






308

    "path": "string",






309

    "defaultBranch": "string",






310

    "name": "Example Name",






311

    "private": "false",






312

    "ownerType": "team"






313

  },






314

  "flags": {






315

    "definitions": "value"






316

  },






317

  "microfrontends": {






318

    "isDefaultApp": "false",






319

    "defaultAppProjectName": "Example Name",






320

    "defaultRoute": "string",






321

    "groupIds": []






322

  },






323

  "config": {






324

    "version": "123",






325

    "functionType": "standard",






326

    "functionMemoryType": "standard",






327

    "functionTimeout": "123",






328

    "secureComputePrimaryRegion": "string",






329

    "secureComputeFallbackRegion": "string",






330

    "isUsingActiveCPU": "false",






331

    "resourceConfig": {






332

      "buildQueue": {






333

        "configuration": "SKIP_NAMESPACE_QUEUE"






334

      },






335

      "elasticConcurrency": "TEAM_SETTING",






336

      "buildMachine": {






337

        "purchaseType": "enhanced"






338

      }






339

    }






340

  },






341

  "checks": {






342

    "deployment-alias": {






343

      "state": "succeeded",






344

      "startedAt": "123",






345

      "completedAt": "123"






346

    }






347

  },






348

  "seatBlock": {






349

    "blockCode": "TEAM_ACCESS_REQUIRED",






350

    "userId": "example_id",






351

    "isVerified": "false"






352

  }






353

}




```

##  [Authentication](https://vercel.com/docs/rest-api/deployments/create-a-new-deployment#authentication)[](https://vercel.com/docs/rest-api/deployments/create-a-new-deployment#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/deployments/create-a-new-deployment#query-parameters)[](https://vercel.com/docs/rest-api/deployments/create-a-new-deployment#query-parameters)
forceNewanyOptional
Forces a new deployment even if there is a previous similar deployment
+Show 2 enum values
skipAutoDetectionConfirmationanyOptional
Allows to skip framework detection so the API would not fail to ask for confirmation
+Show 2 enum values
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/deployments/create-a-new-deployment#body)[](https://vercel.com/docs/rest-api/deployments/create-a-new-deployment#body)
application/json
customEnvironmentSlugOrIdstringOptional
Deploy to a custom environment, which will override the default environment
deploymentIdstringOptional
An deployment id for an existing deployment to redeploy
filesarrayOptional
A list of objects with the files to be deployed
+Show 3 properties
gitMetadataobjectOptional
Populates initial git metadata for different git providers.
+Show 11 properties
gitSourceobjectOptional7 variants
+Show 7 variants
metaobjectOptional
An object containing the deployment's metadata. Multiple key-value pairs can be attached to a deployment
monorepoManagerstringOptional
The monorepo manager that is being used for this deployment. When `null` is used no monorepo manager is selected
namestringRequired
A string with the project name used in the deployment URL
projectstringOptional
The target project identifier in which the deployment will be created. When defined, this parameter overrides name
projectSettingsobjectOptional
Project settings that will be applied to the deployment. It is required for the first deployment of a project and will be saved for any following deployments
+Show 11 properties
targetstringOptional
Either not defined, `staging`, `production`, or a custom environment identifier. If `staging`, a staging alias in the format `<project>-<team>.vercel.app` will be assigned. If `production`, any aliases defined in `alias` will be assigned. If omitted, the target will be `preview`.
withLatestCommitbooleanOptional
When `true` and `deploymentId` is passed in, the sha from the previous deployment's `gitSource` is removed forcing the latest commit to be used.
##  [Response](https://vercel.com/docs/rest-api/deployments/create-a-new-deployment#response)[](https://vercel.com/docs/rest-api/deployments/create-a-new-deployment#response)
200The successfully created deployment
aliasAssignedAtobjectOptional2 variants
+Show 2 variants
alwaysRefuseToBuildbooleanOptional
+Show 2 enum values
buildobjectRequired
+Show 1 properties
buildArtifactUrlsarrayOptional
buildsarrayOptional
+Show 3 properties
envarrayRequired
inspectorUrlstringRequired
isInConcurrentBuildsQueuebooleanRequired
+Show 2 enum values
isInSystemBuildsQueuebooleanRequired
+Show 2 enum values
projectSettingsobjectRequired
+Show 9 properties
readyStateReasonstringOptional
integrationsobjectOptional
+Show 5 properties
imagesobjectOptional
+Show 10 properties
aliasarrayOptional
A list of all the aliases (default aliases, staging aliases and production aliases) that were assigned upon deployment creation
aliasAssignedbooleanRequired
A boolean that will be true when the aliases from the alias property were assigned successfully
+Show 2 enum values
bootedAtnumberRequired
buildingAtnumberRequired
buildContainerFinishedAtnumberOptional
Since April 2025 it necessary for On-Demand Concurrency Minutes calculation
buildSkippedbooleanRequired
+Show 2 enum values
creatorobjectRequired
Information about the deployment creator
+Show 3 properties
initReadyAtnumberOptional
isFirstBranchDeploymentbooleanOptional
+Show 2 enum values
lambdasarrayOptional
+Show 6 properties
publicbooleanRequired
A boolean representing if the deployment is public or not. By default this is `false`
+Show 2 enum values
readynumberOptional
statusstringRequired
+Show 6 enum values
teamobjectOptional
The team that owns the deployment if any
+Show 4 properties
userAliasesarrayOptional
An array of domains that were provided by the user when creating the Deployment.
previewCommentsEnabledbooleanOptional
Whether or not preview comments are enabled for the deployment
+Show 2 enum values
ttyBuildLogsbooleanOptional
+Show 2 enum values
customEnvironmentobjectOptional2 variants
+Show 2 variants
oomReportstringOptional
+Show 1 enum values
aliasWarningobjectOptional
+Show 4 properties
idstringRequired
A string holding the unique ID of the deployment
createdAtnumberRequired
A number containing the date when the deployment was created in milliseconds
readyStatestringRequired
The state of the deployment depending on the process of deploying, or if it is ready or in an error state
+Show 6 enum values
namestringRequired
The name of the project associated with the deployment at the time that the deployment was created
typestringRequired
+Show 1 enum values
aliasErrorobjectOptional
An object that will contain a `code` and a `message` when the aliasing fails, otherwise the value will be `null`
+Show 2 properties
aliasFinalstringOptional
autoAssignCustomDomainsbooleanOptional
applies to custom domains only, defaults to `true`
+Show 2 enum values
automaticAliasesarrayOptional
buildErrorAtnumberOptional
checksStatestringOptional
+Show 3 enum values
checksConclusionstringOptional
+Show 4 enum values
deletedAtnumberOptional
A number containing the date when the deployment was deleted at milliseconds
defaultRoutestringOptional
Computed field that is only available for deployments with a microfrontend configuration.
canceledAtnumberOptional
errorCodestringOptional
errorLinkstringOptional
errorMessagestringOptional
errorStepstringOptional
passiveRegionsarrayOptional
Since November 2023 this field defines a set of regions that we will deploy the lambda to passively Lambdas will be deployed to these regions but only invoked if all of the primary `regions` are marked as out of service
gitSourceobjectOptional15 variants
+Show 15 variants
manualProvisioningobjectOptional
Present when deployment was created with VERCEL_MANUAL_PROVISIONING=true. The deployment stays in INITIALIZING until /continue is called.
+Show 2 properties
metaobjectRequired
originCacheRegionstringOptional
nodeVersionstringOptional
If set it overrides the `projectSettings.nodeVersion` for this deployment.
+Show 9 enum values
projectobjectOptional
The public project information associated with the deployment.
+Show 3 properties
prebuiltbooleanOptional
+Show 2 enum values
readySubstatestringOptional
Substate of deployment when readyState is 'READY' Tracks whether or not deployment has seen production traffic: - STAGED: never seen production traffic - ROLLING: in the process of having production traffic gradually transitioned. - PROMOTED: has seen production traffic
+Show 3 enum values
regionsarrayRequired
The regions the deployment exists in
softDeletedByRetentionbooleanOptional
flag to indicate if the deployment was deleted by retention policy
+Show 2 enum values
sourcestringOptional
Where was the deployment created from
+Show 8 enum values
targetstringOptional
If defined, either `staging` if a staging alias in the format `<project>.<team>.now.sh` was assigned upon creation, or `production` if the aliases from `alias` were assigned. `null` value indicates the "preview" deployment.
+Show 2 enum values
undeletedAtnumberOptional
A number containing the date when the deployment was undeleted at milliseconds
urlstringRequired
A string with the unique URL of the deployment
userConfiguredDeploymentIdstringOptional
Since January 2025 User-configured deployment ID for skew protection with pre-built deployments. This is set when users configure a custom deploymentId in their next.config.js file. This allows Next.js to use skew protection even when deployments are pre-built outside of Vercel's build system.
versionnumberRequired
The platform version that was used to create the deployment.
+Show 1 enum values
oidcTokenClaimsobjectOptional
+Show 10 properties
projectIdstringRequired
planstringRequired
+Show 3 enum values
platformobjectOptional
Metadata about the source platform that triggered the deployment. Allows us to map a deployment back to a platform (e.g. the chat that created it)
+Show 4 properties
connectBuildsEnabledbooleanOptional
+Show 2 enum values
connectConfigurationIdstringOptional
createdInstringRequired
cronsarrayOptional
+Show 2 properties
functionsobjectOptional
monorepoManagerstringOptional
ownerIdstringRequired
passiveConnectConfigurationIdstringOptional
Since November 2023 this field defines a Secure Compute network that will only be used to deploy passive lambdas to (as in passiveRegions)
routesarrayRequired
+Show 23 properties
gitRepoobjectOptional3 variants
+Show 3 variants
flagsobjectOptional
Flags defined in the Build Output API, used by this deployment. Primarily used by the Toolbar to know about the used flags.
+Show 1 properties
microfrontendsobjectOptional2 variants
+Show 2 variants
configobjectOptional
Since February 2025 the configuration must include snapshot data at the time of deployment creation to capture properties for the /deployments/:id/config endpoint utilized for displaying Deployment Configuration on the frontend This is optional because older deployments may not have this data captured
+Show 8 properties
checksobjectOptional
+Show 1 properties
seatBlockobjectOptional
NSNB Blocked metadata
+Show 3 properties
##  [Errors](https://vercel.com/docs/rest-api/deployments/create-a-new-deployment#errors)[](https://vercel.com/docs/rest-api/deployments/create-a-new-deployment#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
402The account was soft-blocked for an unhandled reason. The account is missing a payment so payment method must be updated Pro customers are allowed to deploy Serverless Functions to up to `proMaxRegions` regions, or if the project was created before the limit was introduced. Deploying to Serverless Functions to multiple regions requires a plan update
403You do not have permission to access this resource.
404Error
409The deployment project is being transferred
426Error
429Error
500Error
503Error
TypeScriptNext.jscURL
https://api.vercel.com/v13/deployments
```


1

const response = await fetch('https://api.vercel.com/v13/deployments?forceNew=value&skipAutoDetectionConfirmation=value&teamId=string&slug=string', {






2

  method: 'POST',






3

  headers: {






4

    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',






5

    'Content-Type': 'application/json',






6

  },






7

  body: JSON.stringify({






8

    "customEnvironmentSlugOrId": "example_id",






9

    "deploymentId": "dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6",






10

    "files": [






11

      {






12

        "data": "string",






13

        "encoding": "base64",






14

        "file": "folder/file.js"






15

      }






16

    ],






17

    "gitMetadata": {






18

      "remoteUrl": "https://github.com/vercel/next.js",






19

      "commitAuthorName": "kyliau",






20

      "commitAuthorEmail": "kyliau@example.com",






21

      "commitMessage": "add method to measure Interaction to Next Paint (INP) (#36490)",






22

      "commitRef": "main",






23

      "commitSha": "dc36199b2234c6586ebe05ec94078a895c707e29",






24

      "dirty": "true",






25

      "ci": "true",






26

      "ciType": "github-actions",






27

      "ciGitProviderUsername": "rauchg",






28

      "ciGitRepoVisibility": "private"






29

    },






30

    "gitSource": {






31

      "ref": "main",






32

      "repoId": "123",






33

      "sha": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0",






34

      "type": "github"






35

    },






36

    "meta": "[object Object]",






37

    "monorepoManager": "string",






38

    "name": "my-instant-deployment",






39

    "project": "my-deployment-project",






40

    "projectSettings": {






41

      "buildCommand": "next build",






42

      "commandForIgnoringBuildStep": "string",






43

      "devCommand": "string",






44

      "framework": "null",






45

      "installCommand": "pnpm install",






46

      "nodeVersion": "24.x",






47

      "outputDirectory": "string",






48

      "rootDirectory": "string",






49

      "serverlessFunctionRegion": "string",






50

      "skipGitConnectDuringLink": "true",






51

      "sourceFilesOutsideRootDirectory": "true"






52

    },






53

    "target": "production",






54

    "withLatestCommit": "true"






55

  }),






56

});






57







58

const data = await response.json();






59

console.log(data);




```

Response
```


1

{






2

  "aliasAssignedAt": "123",






3

  "alwaysRefuseToBuild": "false",






4

  "build": {






5

    "env": []






6

  },






7

  "buildArtifactUrls": [],






8

  "builds": [






9

    {






10

      "use": "string",






11

      "src": "string",






12

      "config": "value"






13

    }






14

  ],






15

  "env": [],






16

  "inspectorUrl": "https://example.com",






17

  "isInConcurrentBuildsQueue": "false",






18

  "isInSystemBuildsQueue": "false",






19

  "projectSettings": {






20

    "nodeVersion": "24.x",






21

    "buildCommand": "string",






22

    "devCommand": "string",






23

    "framework": "blitzjs",






24

    "commandForIgnoringBuildStep": "string",






25

    "installCommand": "string",






26

    "outputDirectory": "string",






27

    "speedInsights": {






28

      "id": "icfg_1234567890",






29

      "enabledAt": "123",






30

      "disabledAt": "123",






31

      "canceledAt": "123",






32

      "hasData": "false",






33

      "paidAt": "123"






34

    },






35

    "webAnalytics": {






36

      "id": "icfg_1234567890",






37

      "disabledAt": "123",






38

      "canceledAt": "123",






39

      "enabledAt": "123",






40

      "hasData": "true"






41

    }






42

  },






43

  "readyStateReason": "Customer requested refund",






44

  "integrations": {






45

    "status": "skipped",






46

    "startedAt": "123",






47

    "completedAt": "123",






48

    "skippedAt": "123",






49

    "skippedBy": "string"






50

  },






51

  "images": {






52

    "sizes": [],






53

    "qualities": [],






54

    "domains": [],






55

    "remotePatterns": [






56

      {






57

        "protocol": "http",






58

        "hostname": "Example Name",






59

        "port": "string",






60

        "pathname": "Example Name",






61

        "search": "string"






62

      }






63

    ],






64

    "localPatterns": [






65

      {






66

        "pathname": "Example Name",






67

        "search": "string"






68

      }






69

    ],






70

    "minimumCacheTTL": "123",






71

    "formats": [],






72

    "dangerouslyAllowSVG": "false",






73

    "contentSecurityPolicy": "https://example.com",






74

    "contentDispositionType": "inline"






75

  },






76

  "alias": [],






77

  "aliasAssigned": "true",






78

  "bootedAt": "123",






79

  "buildingAt": "123",






80

  "buildContainerFinishedAt": "123",






81

  "buildSkipped": "false",






82

  "creator": {






83

    "uid": "96SnxkFiMyVKsK3pnoHfx3Hz",






84

    "username": "john-doe",






85

    "avatar": "string"






86

  },






87

  "initReadyAt": "123",






88

  "isFirstBranchDeployment": "false",






89

  "lambdas": [






90

    {






91

      "id": "icfg_1234567890",






92

      "createdAt": "123",






93

      "readyState": "BUILDING",






94

      "entrypoint": "string",






95

      "readyStateAt": "123",






96

      "output": [






97

        {






98

          "path": "string",






99

          "functionName": "Example Name"






100

        }






101

      ]






102

    }






103

  ],






104

  "public": "false",






105

  "ready": "123",






106

  "status": "QUEUED",






107

  "team": {






108

    "id": "icfg_1234567890",






109

    "name": "Example Name",






110

    "slug": "string",






111

    "avatar": "string"






112

  },






113

  "userAliases": [],






114

  "previewCommentsEnabled": "false",






115

  "ttyBuildLogs": "false",






116

  "customEnvironment": {






117

    "id": "icfg_1234567890",






118

    "slug": "string",






119

    "type": "production",






120

    "description": "string",






121

    "branchMatcher": {






122

      "type": "endsWith",






123

      "pattern": "string"






124

    },






125

    "domains": [






126

      {






127

        "name": "Example Name",






128

        "apexName": "Example Name",






129

        "projectId": "example_id",






130

        "redirect": "string",






131

        "redirectStatusCode": "307",






132

        "gitBranch": "string",






133

        "customEnvironmentId": "example_id",






134

        "updatedAt": "123",






135

        "createdAt": "123",






136

        "verified": "false",






137

        "verification": [






138

          {






139

            "type": "string",






140

            "domain": "string",






141

            "value": "string",






142

            "reason": "Customer requested refund"






143

          }






144

        ]






145

      }






146

    ],






147

    "currentDeploymentAliases": [],






148

    "createdAt": "123",






149

    "updatedAt": "123"






150

  },






151

  "oomReport": "out-of-memory",






152

  "aliasWarning": {






153

    "code": "string",






154

    "message": "string",






155

    "link": "string",






156

    "action": "string"






157

  },






158

  "id": "dpl_89qyp1cskzkLrVicDaZoDbjyHuDJ",






159

  "createdAt": "1540257589405",






160

  "readyState": "READY",






161

  "name": "my-project",






162

  "type": "LAMBDAS",






163

  "aliasError": {






164

    "code": "string",






165

    "message": "string"






166

  },






167

  "aliasFinal": "string",






168

  "autoAssignCustomDomains": "false",






169

  "automaticAliases": [],






170

  "buildErrorAt": "123",






171

  "checksState": "registered",






172

  "checksConclusion": "succeeded",






173

  "deletedAt": "1540257589405",






174

  "defaultRoute": "string",






175

  "canceledAt": "123",






176

  "errorCode": "string",






177

  "errorLink": "string",






178

  "errorMessage": "string",






179

  "errorStep": "string",






180

  "passiveRegions": [],






181

  "gitSource": {






182

    "type": "github",






183

    "repoId": "example_id",






184

    "ref": "string",






185

    "sha": "string",






186

    "prId": "123"






187

  },






188

  "manualProvisioning": {






189

    "state": "PENDING",






190

    "completedAt": "123"






191

  },






192

  "meta": "value",






193

  "originCacheRegion": "string",






194

  "nodeVersion": "24.x",






195

  "project": {






196

    "id": "icfg_1234567890",






197

    "name": "Example Name",






198

    "framework": "string"






199

  },






200

  "prebuilt": "false",






201

  "readySubstate": "STAGED",






202

  "regions": [],






203

  "softDeletedByRetention": "true",






204

  "source": "cli",






205

  "target": "null",






206

  "undeletedAt": "1540257589405",






207

  "url": "my-instant-deployment-3ij3cxz9qr.now.sh",






208

  "userConfiguredDeploymentId": "abc123",






209

  "version": "2",






210

  "oidcTokenClaims": {






211

    "iss": "string",






212

    "sub": "string",






213

    "scope": "string",






214

    "aud": "string",






215

    "owner": "string",






216

    "owner_id": "example_id",






217

    "project": "string",






218

    "project_id": "example_id",






219

    "environment": "string",






220

    "plan": "string"






221

  },






222

  "projectId": "example_id",






223

  "plan": "pro",






224

  "platform": {






225

    "source": {






226

      "name": "Example Name"






227

    },






228

    "origin": {






229

      "type": "id",






230

      "value": "string"






231

    },






232

    "creator": {






233

      "name": "Example Name",






234

      "avatar": "string"






235

    },






236

    "meta": "value"






237

  },






238

  "connectBuildsEnabled": "false",






239

  "connectConfigurationId": "example_id",






240

  "createdIn": "string",






241

  "crons": [






242

    {






243

      "schedule": "string",






244

      "path": "string"






245

    }






246

  ],






247

  "functions": "value",






248

  "monorepoManager": "string",






249

  "ownerId": "example_id",






250

  "passiveConnectConfigurationId": "example_id",






251

  "routes": [






252

    {






253

      "src": "string",






254

      "dest": "string",






255

      "headers": "value",






256

      "methods": [],






257

      "continue": "false",






258

      "override": "false",






259

      "caseSensitive": "false",






260

      "check": "false",






261

      "important": "false",






262

      "status": "123",






263

      "has": [






264

        {






265

          "type": "host",






266

          "value": "string"






267

        }






268

      ],






269

      "missing": [






270

        {






271

          "type": "host",






272

          "value": "string"






273

        }






274

      ],






275

      "mitigate": {






276

        "action": "challenge"






277

      },






278

      "transforms": [






279

        {






280

          "type": "request.headers",






281

          "op": "append",






282

          "target": {






283

            "key": "string"






284

          },






285

          "args": "string",






286

          "env": []






287

        }






288

      ],






289

      "env": [],






290

      "locale": {






291

        "redirect": "value",






292

        "cookie": "string"






293

      },






294

      "source": "string",






295

      "destination": "string",






296

      "statusCode": "123",






297

      "middlewarePath": "example_id",






298

      "middlewareRawSrc": [],






299

      "middleware": "123",






300

      "respectOriginCacheControl": "false"






301

    }






302

  ],






303

  "gitRepo": {






304

    "namespace": "Example Name",






305

    "projectId": "123",






306

    "type": "gitlab",






307

    "url": "https://example.com",






308

    "path": "string",






309

    "defaultBranch": "string",






310

    "name": "Example Name",






311

    "private": "false",






312

    "ownerType": "team"






313

  },






314

  "flags": {






315

    "definitions": "value"






316

  },






317

  "microfrontends": {






318

    "isDefaultApp": "false",






319

    "defaultAppProjectName": "Example Name",






320

    "defaultRoute": "string",






321

    "groupIds": []






322

  },






323

  "config": {






324

    "version": "123",






325

    "functionType": "standard",






326

    "functionMemoryType": "standard",






327

    "functionTimeout": "123",






328

    "secureComputePrimaryRegion": "string",






329

    "secureComputeFallbackRegion": "string",






330

    "isUsingActiveCPU": "false",






331

    "resourceConfig": {






332

      "buildQueue": {






333

        "configuration": "SKIP_NAMESPACE_QUEUE"






334

      },






335

      "elasticConcurrency": "TEAM_SETTING",






336

      "buildMachine": {






337

        "purchaseType": "enhanced"






338

      }






339

    }






340

  },






341

  "checks": {






342

    "deployment-alias": {






343

      "state": "succeeded",






344

      "startedAt": "123",






345

      "completedAt": "123"






346

    }






347

  },






348

  "seatBlock": {






349

    "blockCode": "TEAM_ACCESS_REQUIRED",






350

    "userId": "example_id",






351

    "isVerified": "false"






352

  }






353

}




```

Copy as MarkdownGive feedbackAsk AI about this page
## Get Started
  * [Templates](https://vercel.com/templates)
  * [Supported frameworks](https://vercel.com/docs/frameworks)
  * [Marketplace](https://vercel.com/marketplace)
  * [Domains](https://vercel.com/domains)


## Build
  * [Next.js on Vercel](https://vercel.com/frameworks/nextjs)
  * [Turborepo](https://vercel.com/solutions/turborepo)


## Scale
  * [Content delivery network](https://vercel.com/cdn)
  * [Fluid compute](https://vercel.com/fluid)
  * [CI/CD](https://vercel.com/products/previews)
  * [Observability](https://vercel.com/products/observability)
  * [AI GatewayNew](https://vercel.com/ai-gateway)
  * [Vercel AgentNew](https://vercel.com/agent)


## Secure
  * [Platform security](https://vercel.com/security)
  * [Web Application Firewall](https://vercel.com/security/web-application-firewall)
  * [Bot management](https://vercel.com/security/bot-management)
  * [BotID](https://vercel.com/botid)
  * [SandboxNew](https://vercel.com/sandbox)


## Resources
  * [Pricing](https://vercel.com/pricing)
  * [Customers](https://vercel.com/customers)
  * [Enterprise](https://vercel.com/enterprise)
  * [Articles](https://vercel.com/i)
  * [Startups](https://vercel.com/startups)
  * [Solution partners](https://vercel.com/partners/solution-partners)


## Learn
  * [Docs](https://vercel.com/docs)
  * [Blog](https://vercel.com/blog)
  * [Changelog](https://vercel.com/changelog)
  * [Knowledge Base](https://vercel.com/kb)
  * [Academy](https://vercel.com/academy)
  * [Community](https://community.vercel.com)


## Frameworks
  * [Next.js](https://vercel.com/frameworks/nextjs)
  * [Nuxt](https://vercel.com/docs/frameworks/full-stack/nuxt)
  * [Svelte](https://vercel.com/docs/frameworks/full-stack/sveltekit)
  * [Nitro](https://vercel.com/docs/frameworks/backend/nitro)
  * [Turbo](https://vercel.com/solutions/turborepo)


## SDKs
## Use Cases
  * [Composable commerce](https://vercel.com/solutions/composable-commerce)
  * [Multi-tenant platforms](https://vercel.com/solutions/multi-tenant-saas)
  * [Web apps](https://vercel.com/solutions/web-apps)
  * [Marketing sites](https://vercel.com/solutions/marketing-sites)
  * [Platform engineers](https://vercel.com/solutions/platform-engineering)
  * [Design engineers](https://vercel.com/solutions/design-engineering)


## Company
  * [About](https://vercel.com/about)
  * [Careers](https://vercel.com/careers)
  * [Help](https://vercel.com/help)
  * [Press](https://vercel.com/press)
  * [Legal](https://vercel.com/legal)
  * [Privacy Policy](https://vercel.com/legal/privacy-policy)


## Community
  * [Open source program](https://vercel.com/open-source-program)
  * [Events](https://vercel.com/events)
  * [Shipped on Vercel](https://vercel.com/shipped)


[](https://vercel.com/home)

Select a display theme: systemlightdark
