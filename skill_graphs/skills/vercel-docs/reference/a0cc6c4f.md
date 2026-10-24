# Retrieve a list of projects
GET`https://api.vercel.com/v10/projects`
Allows to retrieve the list of projects of the authenticated user or team. The list will be paginated and the provided query parameters allow filtering the returned projects.
Request
```


1

import { Vercel } from "@vercel/sdk";






2







3

const vercel = new Vercel({






4

  bearerToken: "<YOUR_BEARER_TOKEN_HERE>",






5

});






6







7

async function run() {






8

  const result = await vercel.projects.getProjects({






9

    gitForkProtection: "1",






10

    repoUrl: "https://github.com/vercel/next.js",






11

    elasticConcurrencyEnabled: "1",






12

    staticIpsEnabled: "1",






13

    buildMachineTypes: "default,enhanced",






14

    buildQueueConfiguration: "SKIP_NAMESPACE_QUEUE",






15

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






16

    slug: "my-team-url-slug",






17

  });






18







19

  console.log(result);






20

}






21







22

run();




```

Response
```


1

[






2

  {






3

    "accountId": "example_id",






4

    "alias": [






5

      {






6

        "configuredBy": "A",






7

        "configuredChangedAt": "123",






8

        "createdAt": "123",






9

        "deployment": {






10

          "alias": [],






11

          "aliasAssigned": "123",






12

          "builds": [






13

            {






14

              "use": "string",






15

              "src": "string",






16

              "dest": "string"






17

            }






18

          ],






19

          "createdAt": "123",






20

          "createdIn": "string",






21

          "creator": {






22

            "email": "user@example.com",






23

            "githubLogin": "string",






24

            "gitlabLogin": "string",






25

            "uid": "example_id",






26

            "username": "string"






27

          },






28

          "deploymentHostname": "Example Name",






29

          "name": "Example Name",






30

          "forced": "false",






31

          "id": "icfg_1234567890",






32

          "meta": "value",






33

          "plan": "string",






34

          "private": "false",






35

          "readyState": "string",






36

          "requestedAt": "123",






37

          "target": "string",






38

          "teamId": "example_id",






39

          "type": "string",






40

          "url": "https://example.com",






41

          "userId": "example_id",






42

          "withCache": "false"






43

        },






44

        "domain": "string",






45

        "environment": "production",






46

        "gitBranch": "string",






47

        "redirect": "string",






48

        "redirectStatusCode": "301",






49

        "target": "PRODUCTION"






50

      }






51

    ],






52

    "analytics": {






53

      "id": "icfg_1234567890",






54

      "canceledAt": "123",






55

      "disabledAt": "123",






56

      "enabledAt": "123",






57

      "paidAt": "123",






58

      "sampleRatePercent": "123",






59

      "spendLimitInDollars": "123"






60

    },






61

    "appliedCve55182Migration": "false",






62

    "autoExposeSystemEnvs": "false",






63

    "autoAssignCustomDomains": "false",






64

    "autoAssignCustomDomainsUpdatedBy": "string",






65

    "buildCommand": "string",






66

    "commandForIgnoringBuildStep": "string",






67

    "customerSupportCodeVisibility": "false",






68

    "createdAt": "123",






69

    "devCommand": "string",






70

    "directoryListing": "false",






71

    "deploymentExpiration": {






72

      "expirationDays": "123",






73

      "expirationDaysProduction": "123",






74

      "expirationDaysCanceled": "123",






75

      "expirationDaysErrored": "123",






76

      "deploymentsToKeep": "123"






77

    },






78

    "installCommand": "string",






79

    "ipBuckets": [






80

      {






81

        "bucket": "string",






82

        "supportUntil": "123"






83

      }






84

    ],






85

    "env": [






86

      {






87

        "target": [],






88

        "type": "secret",






89

        "sunsetSecretId": "example_id",






90

        "legacyValue": "string",






91

        "decrypted": "false",






92

        "value": "string",






93

        "vsmValue": "string",






94

        "id": "icfg_1234567890",






95

        "key": "string",






96

        "configurationId": "example_id",






97

        "createdAt": "123",






98

        "updatedAt": "123",






99

        "createdBy": "string",






100

        "updatedBy": "string",






101

        "gitBranch": "string",






102

        "edgeConfigId": "example_id",






103

        "edgeConfigTokenId": "example_id",






104

        "contentHint": {






105

          "type": "redis-url",






106

          "storeId": "example_id"






107

        },






108

        "internalContentHint": {






109

          "type": "flags-secret",






110

          "encryptedValue": "string"






111

        },






112

        "comment": "string",






113

        "customEnvironmentIds": []






114

      }






115

    ],






116

    "framework": "services",






117

    "gitForkProtection": "false",






118

    "id": "icfg_1234567890",






119

    "latestDeployments": [






120

      {






121

        "alias": [],






122

        "aliasAssigned": "123",






123

        "builds": [






124

          {






125

            "use": "string",






126

            "src": "string",






127

            "dest": "string"






128

          }






129

        ],






130

        "createdAt": "123",






131

        "createdIn": "string",






132

        "creator": {






133

          "email": "user@example.com",






134

          "githubLogin": "string",






135

          "gitlabLogin": "string",






136

          "uid": "example_id",






137

          "username": "string"






138

        },






139

        "deploymentHostname": "Example Name",






140

        "name": "Example Name",






141

        "forced": "false",






142

        "id": "icfg_1234567890",






143

        "meta": "value",






144

        "plan": "string",






145

        "private": "false",






146

        "readyState": "string",






147

        "requestedAt": "123",






148

        "target": "string",






149

        "teamId": "example_id",






150

        "type": "string",






151

        "url": "https://example.com",






152

        "userId": "example_id",






153

        "withCache": "false"






154

      }






155

    ],






156

    "link": {






157

      "org": "string",






158

      "repoOwnerId": "123",






159

      "repo": "string",






160

      "repoId": "123",






161

      "type": "github",






162

      "createdAt": "123",






163

      "deployHooks": [






164

        {






165

          "createdAt": "123",






166

          "id": "icfg_1234567890",






167

          "name": "Example Name",






168

          "ref": "string",






169

          "url": "https://example.com"






170

        }






171

      ],






172

      "gitCredentialId": "example_id",






173

      "updatedAt": "123",






174

      "sourceless": "false",






175

      "productionBranch": "string"






176

    },






177

    "name": "Example Name",






178

    "nodeVersion": "24.x",






179

    "outputDirectory": "string",






180

    "passwordProtection": "value",






181

    "publicSource": "false",






182

    "resourceConfig": {






183

      "elasticConcurrencyEnabled": "false",






184

      "fluid": "false",






185

      "functionDefaultRegions": [],






186

      "functionDefaultTimeout": "123",






187

      "functionDefaultMemoryType": "standard_legacy",






188

      "functionZeroConfigFailover": "false",






189

      "buildMachineType": "standard",






190

      "buildMachineSelection": "fixed",






191

      "buildMachineElasticLastUpdated": "123",






192

      "isNSNBDisabled": "false",






193

      "buildQueue": {






194

        "configuration": "SKIP_NAMESPACE_QUEUE"






195

      }






196

    },






197

    "rollingRelease": {






198

      "target": "production",






199

      "stages": [






200

        {






201

          "targetPercentage": "25",






202

          "requireApproval": "false",






203

          "duration": "600",






204

          "linearShift": "false"






205

        }






206

      ],






207

      "canaryResponseHeader": "false"






208

    },






209

    "rootDirectory": "string",






210

    "serverlessFunctionRegion": "string",






211

    "serverlessFunctionZeroConfigFailover": "false",






212

    "speedInsights": {






213

      "id": "icfg_1234567890",






214

      "enabledAt": "123",






215

      "disabledAt": "123",






216

      "canceledAt": "123",






217

      "hasData": "false",






218

      "paidAt": "123"






219

    },






220

    "skipGitConnectDuringLink": "false",






221

    "sourceFilesOutsideRootDirectory": "false",






222

    "ssoProtection": {






223

      "deploymentType": "preview",






224

      "cve55182MigrationAppliedFrom": "preview"






225

    },






226

    "targets": "value",






227

    "transferCompletedAt": "123",






228

    "transferStartedAt": "123",






229

    "transferToAccountId": "example_id",






230

    "transferredFromAccountId": "example_id",






231

    "updatedAt": "123",






232

    "live": "false",






233

    "hasActiveBranches": "false",






234

    "gitComments": {






235

      "onPullRequest": "false",






236

      "onCommit": "false"






237

    },






238

    "gitProviderOptions": {






239

      "createDeployments": "enabled",






240

      "disableRepositoryDispatchEvents": "false",






241

      "requireVerifiedCommits": "false"






242

    },






243

    "paused": "false",






244

    "webAnalytics": {






245

      "id": "icfg_1234567890",






246

      "disabledAt": "123",






247

      "canceledAt": "123",






248

      "enabledAt": "123",






249

      "hasData": "true"






250

    },






251

    "security": {






252

      "attackModeEnabled": "false",






253

      "attackModeUpdatedAt": "123",






254

      "firewallEnabled": "false",






255

      "firewallUpdatedAt": "123",






256

      "attackModeActiveUntil": "123",






257

      "firewallConfigVersion": "123",






258

      "firewallRoutes": [






259

        {






260

          "src": "string",






261

          "has": [






262

            {






263

              "type": "path",






264

              "key": "string",






265

              "value": "string"






266

            }






267

          ],






268

          "missing": [






269

            {






270

              "type": "path",






271

              "key": "string",






272

              "value": "string"






273

            }






274

          ],






275

          "dest": "string",






276

          "status": "123",






277

          "handle": "init",






278

          "mitigate": {






279

            "action": "log",






280

            "rule_id": "example_id",






281

            "ttl": "123",






282

            "erl": {






283

              "algo": "fixed_window",






284

              "window": "123",






285

              "limit": "123",






286

              "keys": []






287

            },






288

            "log_headers": []






289

          }






290

        }






291

      ],






292

      "firewallSeawallEnabled": "false",






293

      "ja3Enabled": "false",






294

      "ja4Enabled": "false",






295

      "firewallBypassIps": [],






296

      "managedRules": {






297

        "vercel_ruleset": {






298

          "active": "false",






299

          "action": "log"






300

        },






301

        "bot_filter": {






302

          "active": "false",






303

          "action": "log"






304

        },






305

        "ai_bots": {






306

          "active": "false",






307

          "action": "log"






308

        },






309

        "owasp": {






310

          "active": "false",






311

          "action": "log"






312

        }






313

      },






314

      "botIdEnabled": "false",






315

      "requestLogsKey": []






316

    },






317

    "oidcTokenConfig": {






318

      "enabled": "false",






319

      "issuerMode": "team"






320

    },






321

    "tier": "standard",






322

    "abuse": {






323

      "scanner": "string",






324

      "history": [






325

        {






326

          "scanner": "string",






327

          "reason": "Customer requested refund",






328

          "by": "string",






329

          "byId": "example_id",






330

          "at": "123"






331

        }






332

      ],






333

      "updatedAt": "123",






334

      "block": {






335

        "action": "blocked",






336

        "reason": "Customer requested refund",






337

        "statusCode": "123",






338

        "createdAt": "123",






339

        "caseId": "example_id",






340

        "actor": "string",






341

        "comment": "string",






342

        "ineligibleForAppeal": "false",






343

        "isCascading": "false"






344

      },






345

      "blockHistory": [






346

        {






347

          "action": "blocked",






348

          "reason": "Customer requested refund",






349

          "statusCode": "123",






350

          "createdAt": "123",






351

          "caseId": "example_id",






352

          "actor": "string",






353

          "comment": "string",






354

          "ineligibleForAppeal": "false",






355

          "isCascading": "false"






356

        }






357

      ],






358

      "interstitial": "false"






359

    },






360

    "internalRoutes": [






361

      {






362

        "src": "string",






363

        "status": "123"






364

      }






365

    ]






366

  }






367

]




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/projects/retrieve-a-list-of-projects#authentication)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-a-list-of-projects#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/projects/retrieve-a-list-of-projects#query-parameters)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-a-list-of-projects#query-parameters)
fromstringOptional
Query only projects updated after the given timestamp or continuation token.
gitForkProtectionstringOptional
Specifies whether PRs from Git forks should require a team member's authorization before it can be deployed
+Show 2 enum values
limitstringOptional
Limit the number of projects returned
searchstringOptional
Search projects by the name field
repostringOptional
Filter results by repo. Also used for project count
repoIdstringOptional
Filter results by Repository ID.
repoUrlstringOptional
Filter results by Repository URL.
excludeReposstringOptional
Filter results by excluding those projects that belong to a repo
edgeConfigIdstringOptional
Filter results by connected Edge Config ID
edgeConfigTokenIdstringOptional
Filter results by connected Edge Config Token ID
deprecatedbooleanOptional
elasticConcurrencyEnabledstringOptional
Filter results by projects with elastic concurrency enabled
+Show 2 enum values
staticIpsEnabledstringOptional
Filter results by projects with Static IPs enabled
+Show 2 enum values
buildMachineTypesstringOptional
Filter results by build machine types. Accepts comma-separated values. Use "default" for projects without a build machine type set.
buildQueueConfigurationstringOptional
Filter results by build queue configuration. SKIP_NAMESPACE_QUEUE includes projects without a configuration set.
+Show 2 enum values
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/projects/retrieve-a-list-of-projects#response)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-a-list-of-projects#response)
200Success
##  [Errors](https://vercel.com/docs/rest-api/sdk/projects/retrieve-a-list-of-projects#errors)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-a-list-of-projects#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
Request
```


1

import { Vercel } from "@vercel/sdk";






2







3

const vercel = new Vercel({






4

  bearerToken: "<YOUR_BEARER_TOKEN_HERE>",






5

});






6







7

async function run() {






8

  const result = await vercel.projects.getProjects({






9

    gitForkProtection: "1",






10

    repoUrl: "https://github.com/vercel/next.js",






11

    elasticConcurrencyEnabled: "1",






12

    staticIpsEnabled: "1",






13

    buildMachineTypes: "default,enhanced",






14

    buildQueueConfiguration: "SKIP_NAMESPACE_QUEUE",






15

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






16

    slug: "my-team-url-slug",






17

  });






18







19

  console.log(result);






20

}






21







22

run();




```

Response
```


1

[






2

  {






3

    "accountId": "example_id",






4

    "alias": [






5

      {






6

        "configuredBy": "A",






7

        "configuredChangedAt": "123",






8

        "createdAt": "123",






9

        "deployment": {






10

          "alias": [],






11

          "aliasAssigned": "123",






12

          "builds": [






13

            {






14

              "use": "string",






15

              "src": "string",






16

              "dest": "string"






17

            }






18

          ],






19

          "createdAt": "123",






20

          "createdIn": "string",






21

          "creator": {






22

            "email": "user@example.com",






23

            "githubLogin": "string",






24

            "gitlabLogin": "string",






25

            "uid": "example_id",






26

            "username": "string"






27

          },






28

          "deploymentHostname": "Example Name",






29

          "name": "Example Name",






30

          "forced": "false",






31

          "id": "icfg_1234567890",






32

          "meta": "value",






33

          "plan": "string",






34

          "private": "false",






35

          "readyState": "string",






36

          "requestedAt": "123",






37

          "target": "string",






38

          "teamId": "example_id",






39

          "type": "string",






40

          "url": "https://example.com",






41

          "userId": "example_id",






42

          "withCache": "false"






43

        },






44

        "domain": "string",






45

        "environment": "production",






46

        "gitBranch": "string",






47

        "redirect": "string",






48

        "redirectStatusCode": "301",






49

        "target": "PRODUCTION"






50

      }






51

    ],






52

    "analytics": {






53

      "id": "icfg_1234567890",






54

      "canceledAt": "123",






55

      "disabledAt": "123",






56

      "enabledAt": "123",






57

      "paidAt": "123",






58

      "sampleRatePercent": "123",






59

      "spendLimitInDollars": "123"






60

    },






61

    "appliedCve55182Migration": "false",






62

    "autoExposeSystemEnvs": "false",






63

    "autoAssignCustomDomains": "false",






64

    "autoAssignCustomDomainsUpdatedBy": "string",






65

    "buildCommand": "string",






66

    "commandForIgnoringBuildStep": "string",






67

    "customerSupportCodeVisibility": "false",






68

    "createdAt": "123",






69

    "devCommand": "string",






70

    "directoryListing": "false",






71

    "deploymentExpiration": {






72

      "expirationDays": "123",






73

      "expirationDaysProduction": "123",






74

      "expirationDaysCanceled": "123",






75

      "expirationDaysErrored": "123",






76

      "deploymentsToKeep": "123"






77

    },






78

    "installCommand": "string",






79

    "ipBuckets": [






80

      {






81

        "bucket": "string",






82

        "supportUntil": "123"






83

      }






84

    ],






85

    "env": [






86

      {






87

        "target": [],






88

        "type": "secret",






89

        "sunsetSecretId": "example_id",






90

        "legacyValue": "string",






91

        "decrypted": "false",






92

        "value": "string",






93

        "vsmValue": "string",






94

        "id": "icfg_1234567890",






95

        "key": "string",






96

        "configurationId": "example_id",






97

        "createdAt": "123",






98

        "updatedAt": "123",






99

        "createdBy": "string",






100

        "updatedBy": "string",






101

        "gitBranch": "string",






102

        "edgeConfigId": "example_id",






103

        "edgeConfigTokenId": "example_id",






104

        "contentHint": {






105

          "type": "redis-url",






106

          "storeId": "example_id"






107

        },






108

        "internalContentHint": {






109

          "type": "flags-secret",






110

          "encryptedValue": "string"






111

        },






112

        "comment": "string",






113

        "customEnvironmentIds": []






114

      }






115

    ],






116

    "framework": "services",






117

    "gitForkProtection": "false",






118

    "id": "icfg_1234567890",






119

    "latestDeployments": [






120

      {






121

        "alias": [],






122

        "aliasAssigned": "123",






123

        "builds": [






124

          {






125

            "use": "string",






126

            "src": "string",






127

            "dest": "string"






128

          }






129

        ],






130

        "createdAt": "123",






131

        "createdIn": "string",






132

        "creator": {






133

          "email": "user@example.com",






134

          "githubLogin": "string",






135

          "gitlabLogin": "string",






136

          "uid": "example_id",






137

          "username": "string"






138

        },






139

        "deploymentHostname": "Example Name",






140

        "name": "Example Name",






141

        "forced": "false",






142

        "id": "icfg_1234567890",






143

        "meta": "value",






144

        "plan": "string",






145

        "private": "false",






146

        "readyState": "string",






147

        "requestedAt": "123",






148

        "target": "string",






149

        "teamId": "example_id",






150

        "type": "string",






151

        "url": "https://example.com",






152

        "userId": "example_id",






153

        "withCache": "false"






154

      }






155

    ],






156

    "link": {






157

      "org": "string",






158

      "repoOwnerId": "123",






159

      "repo": "string",






160

      "repoId": "123",






161

      "type": "github",






162

      "createdAt": "123",






163

      "deployHooks": [






164

        {






165

          "createdAt": "123",






166

          "id": "icfg_1234567890",






167

          "name": "Example Name",






168

          "ref": "string",






169

          "url": "https://example.com"






170

        }






171

      ],






172

      "gitCredentialId": "example_id",






173

      "updatedAt": "123",






174

      "sourceless": "false",






175

      "productionBranch": "string"






176

    },






177

    "name": "Example Name",






178

    "nodeVersion": "24.x",






179

    "outputDirectory": "string",






180

    "passwordProtection": "value",






181

    "publicSource": "false",






182

    "resourceConfig": {






183

      "elasticConcurrencyEnabled": "false",






184

      "fluid": "false",






185

      "functionDefaultRegions": [],






186

      "functionDefaultTimeout": "123",






187

      "functionDefaultMemoryType": "standard_legacy",






188

      "functionZeroConfigFailover": "false",






189

      "buildMachineType": "standard",






190

      "buildMachineSelection": "fixed",






191

      "buildMachineElasticLastUpdated": "123",






192

      "isNSNBDisabled": "false",






193

      "buildQueue": {






194

        "configuration": "SKIP_NAMESPACE_QUEUE"






195

      }






196

    },






197

    "rollingRelease": {






198

      "target": "production",






199

      "stages": [






200

        {






201

          "targetPercentage": "25",






202

          "requireApproval": "false",






203

          "duration": "600",






204

          "linearShift": "false"






205

        }






206

      ],






207

      "canaryResponseHeader": "false"






208

    },






209

    "rootDirectory": "string",






210

    "serverlessFunctionRegion": "string",






211

    "serverlessFunctionZeroConfigFailover": "false",






212

    "speedInsights": {






213

      "id": "icfg_1234567890",






214

      "enabledAt": "123",






215

      "disabledAt": "123",






216

      "canceledAt": "123",






217

      "hasData": "false",






218

      "paidAt": "123"






219

    },






220

    "skipGitConnectDuringLink": "false",






221

    "sourceFilesOutsideRootDirectory": "false",






222

    "ssoProtection": {






223

      "deploymentType": "preview",






224

      "cve55182MigrationAppliedFrom": "preview"






225

    },






226

    "targets": "value",






227

    "transferCompletedAt": "123",






228

    "transferStartedAt": "123",






229

    "transferToAccountId": "example_id",






230

    "transferredFromAccountId": "example_id",






231

    "updatedAt": "123",






232

    "live": "false",






233

    "hasActiveBranches": "false",






234

    "gitComments": {






235

      "onPullRequest": "false",






236

      "onCommit": "false"






237

    },






238

    "gitProviderOptions": {






239

      "createDeployments": "enabled",






240

      "disableRepositoryDispatchEvents": "false",






241

      "requireVerifiedCommits": "false"






242

    },






243

    "paused": "false",






244

    "webAnalytics": {






245

      "id": "icfg_1234567890",






246

      "disabledAt": "123",






247

      "canceledAt": "123",






248

      "enabledAt": "123",






249

      "hasData": "true"






250

    },






251

    "security": {






252

      "attackModeEnabled": "false",






253

      "attackModeUpdatedAt": "123",






254

      "firewallEnabled": "false",






255

      "firewallUpdatedAt": "123",






256

      "attackModeActiveUntil": "123",






257

      "firewallConfigVersion": "123",






258

      "firewallRoutes": [






259

        {






260

          "src": "string",






261

          "has": [






262

            {






263

              "type": "path",






264

              "key": "string",






265

              "value": "string"






266

            }






267

          ],






268

          "missing": [






269

            {






270

              "type": "path",






271

              "key": "string",






272

              "value": "string"






273

            }






274

          ],






275

          "dest": "string",






276

          "status": "123",






277

          "handle": "init",






278

          "mitigate": {






279

            "action": "log",






280

            "rule_id": "example_id",






281

            "ttl": "123",






282

            "erl": {






283

              "algo": "fixed_window",






284

              "window": "123",






285

              "limit": "123",






286

              "keys": []






287

            },






288

            "log_headers": []






289

          }






290

        }






291

      ],






292

      "firewallSeawallEnabled": "false",






293

      "ja3Enabled": "false",






294

      "ja4Enabled": "false",






295

      "firewallBypassIps": [],






296

      "managedRules": {






297

        "vercel_ruleset": {






298

          "active": "false",






299

          "action": "log"






300

        },






301

        "bot_filter": {






302

          "active": "false",






303

          "action": "log"






304

        },






305

        "ai_bots": {






306

          "active": "false",






307

          "action": "log"






308

        },






309

        "owasp": {






310

          "active": "false",






311

          "action": "log"






312

        }






313

      },






314

      "botIdEnabled": "false",






315

      "requestLogsKey": []






316

    },






317

    "oidcTokenConfig": {






318

      "enabled": "false",






319

      "issuerMode": "team"






320

    },






321

    "tier": "standard",






322

    "abuse": {






323

      "scanner": "string",






324

      "history": [






325

        {






326

          "scanner": "string",






327

          "reason": "Customer requested refund",






328

          "by": "string",






329

          "byId": "example_id",






330

          "at": "123"






331

        }






332

      ],






333

      "updatedAt": "123",






334

      "block": {






335

        "action": "blocked",






336

        "reason": "Customer requested refund",






337

        "statusCode": "123",






338

        "createdAt": "123",






339

        "caseId": "example_id",






340

        "actor": "string",






341

        "comment": "string",






342

        "ineligibleForAppeal": "false",






343

        "isCascading": "false"






344

      },






345

      "blockHistory": [






346

        {






347

          "action": "blocked",






348

          "reason": "Customer requested refund",






349

          "statusCode": "123",






350

          "createdAt": "123",






351

          "caseId": "example_id",






352

          "actor": "string",






353

          "comment": "string",






354

          "ineligibleForAppeal": "false",






355

          "isCascading": "false"






356

        }






357

      ],






358

      "interstitial": "false"






359

    },






360

    "internalRoutes": [






361

      {






362

        "src": "string",






363

        "status": "123"






364

      }






365

    ]






366

  }






367

]




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
