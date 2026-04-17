# Create a new project
POST`https://api.vercel.com/v11/projects`
Allows to create a new project with the provided configuration. It only requires the project `name` but more configuration can be provided to override the defaults.
TypeScriptNext.jscURL
https://api.vercel.com/v11/projects
```


1

const response = await fetch('https://api.vercel.com/v11/projects?teamId=string&slug=string', {






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

    "enablePreviewFeedback": "true",






9

    "enableProductionFeedback": "true",






10

    "previewDeploymentsDisabled": "true",






11

    "previewDeploymentSuffix": "string",






12

    "buildCommand": "string",






13

    "commandForIgnoringBuildStep": "string",






14

    "devCommand": "string",






15

    "environmentVariables": [






16

      {






17

        "key": "string",






18

        "target": "production",






19

        "gitBranch": "string",






20

        "type": "system",






21

        "value": "string"






22

      }






23

    ],






24

    "framework": "null",






25

    "gitRepository": {






26

      "repo": "string",






27

      "type": "github"






28

    },






29

    "installCommand": "string",






30

    "name": "a-project-name",






31

    "skipGitConnectDuringLink": "true",






32

    "ssoProtection": {






33

      "deploymentType": "all"






34

    },






35

    "outputDirectory": "string",






36

    "publicSource": "true",






37

    "rootDirectory": "string",






38

    "serverlessFunctionRegion": "string",






39

    "serverlessFunctionZeroConfigFailover": "true",






40

    "oidcTokenConfig": {






41

      "enabled": "true",






42

      "issuerMode": "team"






43

    },






44

    "enableAffectedProjectsDeployments": "true",






45

    "resourceConfig": {






46

      "fluid": "true",






47

      "functionDefaultRegions": [],






48

      "functionDefaultTimeout": "123",






49

      "functionDefaultMemoryType": "standard_legacy",






50

      "functionZeroConfigFailover": "true",






51

      "elasticConcurrencyEnabled": "true",






52

      "buildMachineType": "enhanced",






53

      "buildMachineSelection": "elastic",






54

      "buildMachineElasticLastUpdated": "123",






55

      "isNSNBDisabled": "true",






56

      "buildQueue": {






57

        "configuration": "SKIP_NAMESPACE_QUEUE"






58

      }






59

    }






60

  }),






61

});






62







63

const data = await response.json();






64

console.log(data);




```

Response
```


1

{






2

  "accountId": "example_id",






3

  "analytics": {






4

    "id": "icfg_1234567890",






5

    "canceledAt": "123",






6

    "disabledAt": "123",






7

    "enabledAt": "123",






8

    "paidAt": "123",






9

    "sampleRatePercent": "123",






10

    "spendLimitInDollars": "123"






11

  },






12

  "appliedCve55182Migration": "false",






13

  "speedInsights": {






14

    "id": "icfg_1234567890",






15

    "enabledAt": "123",






16

    "disabledAt": "123",






17

    "canceledAt": "123",






18

    "hasData": "false",






19

    "paidAt": "123"






20

  },






21

  "autoExposeSystemEnvs": "false",






22

  "autoAssignCustomDomains": "false",






23

  "autoAssignCustomDomainsUpdatedBy": "string",






24

  "buildCommand": "string",






25

  "commandForIgnoringBuildStep": "string",






26

  "connectConfigurations": [






27

    {






28

      "envId": "example_id",






29

      "connectConfigurationId": "example_id",






30

      "dc": "string",






31

      "passive": "false",






32

      "buildsEnabled": "false",






33

      "aws": {






34

        "subnetIds": [],






35

        "securityGroupId": "https://example.com"






36

      },






37

      "createdAt": "123",






38

      "updatedAt": "123"






39

    }






40

  ],






41

  "connectConfigurationId": "example_id",






42

  "connectBuildsEnabled": "false",






43

  "passiveConnectConfigurationId": "example_id",






44

  "createdAt": "123",






45

  "customerSupportCodeVisibility": "false",






46

  "crons": {






47

    "enabledAt": "123",






48

    "disabledAt": "123",






49

    "updatedAt": "123",






50

    "deploymentId": "example_id",






51

    "definitions": [






52

      {






53

        "host": "vercel.com",






54

        "path": "/api/crons/sync-something?hello=world",






55

        "schedule": "0 0 * * *"






56

      }






57

    ]






58

  },






59

  "dataCache": {






60

    "userDisabled": "false",






61

    "storageSizeBytes": "123",






62

    "unlimited": "false"






63

  },






64

  "deploymentExpiration": {






65

    "expirationDays": "123",






66

    "expirationDaysProduction": "123",






67

    "expirationDaysCanceled": "123",






68

    "expirationDaysErrored": "123",






69

    "deploymentsToKeep": "123"






70

  },






71

  "devCommand": "string",






72

  "directoryListing": "false",






73

  "installCommand": "string",






74

  "env": [






75

    {






76

      "target": [],






77

      "type": "secret",






78

      "sunsetSecretId": "example_id",






79

      "legacyValue": "string",






80

      "decrypted": "false",






81

      "value": "string",






82

      "vsmValue": "string",






83

      "id": "icfg_1234567890",






84

      "key": "string",






85

      "configurationId": "example_id",






86

      "createdAt": "123",






87

      "updatedAt": "123",






88

      "createdBy": "string",






89

      "updatedBy": "string",






90

      "gitBranch": "string",






91

      "edgeConfigId": "example_id",






92

      "edgeConfigTokenId": "example_id",






93

      "contentHint": {






94

        "type": "redis-url",






95

        "storeId": "example_id"






96

      },






97

      "internalContentHint": {






98

        "type": "flags-secret",






99

        "encryptedValue": "string"






100

      },






101

      "comment": "string",






102

      "customEnvironmentIds": []






103

    }






104

  ],






105

  "customEnvironments": [






106

    {






107

      "id": "icfg_1234567890",






108

      "slug": "string",






109

      "type": "production",






110

      "description": "string",






111

      "branchMatcher": {






112

        "type": "endsWith",






113

        "pattern": "string"






114

      },






115

      "domains": [






116

        {






117

          "name": "Example Name",






118

          "apexName": "Example Name",






119

          "projectId": "example_id",






120

          "redirect": "string",






121

          "redirectStatusCode": "301",






122

          "gitBranch": "string",






123

          "customEnvironmentId": "example_id",






124

          "updatedAt": "123",






125

          "createdAt": "123",






126

          "verified": "false",






127

          "verification": [






128

            {






129

              "type": "string",






130

              "domain": "string",






131

              "value": "string",






132

              "reason": "Customer requested refund"






133

            }






134

          ]






135

        }






136

      ],






137

      "currentDeploymentAliases": [],






138

      "createdAt": "123",






139

      "updatedAt": "123"






140

    }






141

  ],






142

  "framework": "services",






143

  "gitForkProtection": "false",






144

  "gitLFS": "false",






145

  "id": "icfg_1234567890",






146

  "ipBuckets": [






147

    {






148

      "bucket": "string",






149

      "supportUntil": "123"






150

    }






151

  ],






152

  "latestDeployments": [






153

    {






154

      "alias": [],






155

      "aliasAssigned": "123",






156

      "builds": [






157

        {






158

          "use": "string",






159

          "src": "string",






160

          "dest": "string"






161

        }






162

      ],






163

      "createdAt": "123",






164

      "createdIn": "string",






165

      "creator": {






166

        "email": "user@example.com",






167

        "githubLogin": "string",






168

        "gitlabLogin": "string",






169

        "uid": "example_id",






170

        "username": "string"






171

      },






172

      "deploymentHostname": "Example Name",






173

      "name": "Example Name",






174

      "forced": "false",






175

      "id": "icfg_1234567890",






176

      "meta": "value",






177

      "plan": "string",






178

      "private": "false",






179

      "readyState": "string",






180

      "requestedAt": "123",






181

      "target": "string",






182

      "teamId": "example_id",






183

      "type": "string",






184

      "url": "https://example.com",






185

      "userId": "example_id",






186

      "withCache": "false"






187

    }






188

  ],






189

  "link": {






190

    "org": "string",






191

    "repoOwnerId": "123",






192

    "repo": "string",






193

    "repoId": "123",






194

    "type": "github",






195

    "createdAt": "123",






196

    "deployHooks": [






197

      {






198

        "createdAt": "123",






199

        "id": "icfg_1234567890",






200

        "name": "Example Name",






201

        "ref": "string",






202

        "url": "https://example.com"






203

      }






204

    ],






205

    "gitCredentialId": "example_id",






206

    "updatedAt": "123",






207

    "sourceless": "false",






208

    "productionBranch": "string"






209

  },






210

  "microfrontends": {






211

    "isDefaultApp": "true",






212

    "updatedAt": "123",






213

    "groupIds": [],






214

    "enabled": "true",






215

    "defaultRoute": "string",






216

    "freeProjectForLegacyLimits": "false"






217

  },






218

  "name": "Example Name",






219

  "nodeVersion": "24.x",






220

  "optionsAllowlist": {






221

    "paths": [






222

      {






223

        "value": "string"






224

      }






225

    ]






226

  },






227

  "outputDirectory": "string",






228

  "passwordProtection": "value",






229

  "productionDeploymentsFastLane": "false",






230

  "publicSource": "false",






231

  "resourceConfig": {






232

    "elasticConcurrencyEnabled": "false",






233

    "fluid": "false",






234

    "functionDefaultRegions": [],






235

    "functionDefaultTimeout": "123",






236

    "functionDefaultMemoryType": "standard_legacy",






237

    "functionZeroConfigFailover": "false",






238

    "buildMachineType": "standard",






239

    "buildMachineSelection": "fixed",






240

    "buildMachineElasticLastUpdated": "123",






241

    "isNSNBDisabled": "false",






242

    "buildQueue": {






243

      "configuration": "SKIP_NAMESPACE_QUEUE"






244

    }






245

  },






246

  "rollbackDescription": {






247

    "userId": "example_id",






248

    "username": "string",






249

    "description": "string",






250

    "createdAt": "123"






251

  },






252

  "rollingRelease": {






253

    "target": "production",






254

    "stages": [






255

      {






256

        "targetPercentage": "25",






257

        "requireApproval": "false",






258

        "duration": "600",






259

        "linearShift": "false"






260

      }






261

    ],






262

    "canaryResponseHeader": "false"






263

  },






264

  "defaultResourceConfig": {






265

    "elasticConcurrencyEnabled": "false",






266

    "fluid": "false",






267

    "functionDefaultRegions": [],






268

    "functionDefaultTimeout": "123",






269

    "functionDefaultMemoryType": "standard_legacy",






270

    "functionZeroConfigFailover": "false",






271

    "buildMachineType": "standard",






272

    "buildMachineSelection": "fixed",






273

    "buildMachineElasticLastUpdated": "123",






274

    "isNSNBDisabled": "false",






275

    "buildQueue": {






276

      "configuration": "SKIP_NAMESPACE_QUEUE"






277

    }






278

  },






279

  "rootDirectory": "string",






280

  "serverlessFunctionZeroConfigFailover": "false",






281

  "skewProtectionBoundaryAt": "123",






282

  "skewProtectionMaxAge": "123",






283

  "skewProtectionAllowedDomains": [],






284

  "skipGitConnectDuringLink": "false",






285

  "staticIps": {






286

    "builds": "false",






287

    "enabled": "false",






288

    "regions": []






289

  },






290

  "sourceFilesOutsideRootDirectory": "false",






291

  "enableAffectedProjectsDeployments": "false",






292

  "ssoProtection": {






293

    "deploymentType": "preview",






294

    "cve55182MigrationAppliedFrom": "preview"






295

  },






296

  "targets": "value",






297

  "transferCompletedAt": "123",






298

  "transferStartedAt": "123",






299

  "transferToAccountId": "example_id",






300

  "transferredFromAccountId": "example_id",






301

  "updatedAt": "123",






302

  "live": "false",






303

  "enablePreviewFeedback": "false",






304

  "enableProductionFeedback": "false",






305

  "permissions": {






306

    "oauth2Connection": [],






307

    "user": [],






308

    "userConnection": [],






309

    "userSudo": [],






310

    "webAuthn": [],






311

    "accessGroup": [],






312

    "agent": [],






313

    "aiGatewayUsage": [],






314

    "alerts": [],






315

    "alertRules": [],






316

    "aliasGlobal": [],






317

    "analyticsSampling": [],






318

    "analyticsUsage": [],






319

    "apiKey": [],






320

    "apiKeyAiGateway": [],






321

    "apiKeyOwnedBySelf": [],






322

    "oauth2Application": [],






323

    "vercelAppInstallation": [],






324

    "vercelAppInstallationRequest": [],






325

    "auditLog": [],






326

    "billingAddress": [],






327

    "billingInformation": [],






328

    "billingInvoice": [],






329

    "billingInvoiceEmailRecipient": [],






330

    "billingInvoiceLanguage": [],






331

    "billingPlan": [],






332

    "billingPurchaseOrder": [],






333

    "billingRefund": [],






334

    "billingTaxId": [],






335

    "blob": [],






336

    "blobStoreTokenSet": [],






337

    "budget": [],






338

    "cacheArtifact": [],






339

    "cacheArtifactUsageEvent": [],






340

    "codeChecks": [],






341

    "concurrentBuilds": [],






342

    "connect": [],






343

    "connectConfiguration": [],






344

    "buildMachineDefault": [],






345

    "dataCacheBillingSettings": [],






346

    "defaultDeploymentProtection": [],






347

    "domain": [],






348

    "domainAcceptDelegation": [],






349

    "domainAuthCodes": [],






350

    "domainCertificate": [],






351

    "domainCheckConfig": [],






352

    "domainMove": [],






353

    "domainPurchase": [],






354

    "domainRecord": [],






355

    "domainTransferIn": [],






356

    "drain": [],






357

    "edgeConfig": [],






358

    "edgeConfigItem": [],






359

    "edgeConfigSchema": [],






360

    "edgeConfigToken": [],






361

    "endpointVerification": [],






362

    "event": [],






363

    "fileUpload": [],






364

    "flagsExplorerSubscription": [],






365

    "gitRepository": [],






366

    "imageOptimizationNewPrice": [],






367

    "integration": [],






368

    "integrationAccount": [],






369

    "integrationConfiguration": [],






370

    "integrationConfigurationProjects": [],






371

    "integrationConfigurationRole": [],






372

    "integrationConfigurationTransfer": [],






373

    "integrationDeploymentAction": [],






374

    "integrationEvent": [],






375

    "integrationLog": [],






376

    "integrationResource": [],






377

    "integrationResourceData": [],






378

    "integrationResourceReplCommand": [],






379

    "integrationResourceSecrets": [],






380

    "integrationSSOSession": [],






381

    "integrationStrict": [],






382

    "integrationStoreTokenSet": [],






383

    "integrationVercelConfigurationOverride": [],






384

    "integrationPullRequest": [],






385

    "ipBlocking": [],






386

    "jobGlobal": [],






387

    "logDrain": [],






388

    "marketplaceBillingData": [],






389

    "marketplaceExperimentationEdgeConfigData": [],






390

    "marketplaceExperimentationItem": [],






391

    "marketplaceInstallationMember": [],






392

    "marketplaceInvoice": [],






393

    "marketplaceSettings": [],






394

    "Monitoring": [],






395

    "monitoringAlert": [],






396

    "monitoringChart": [],






397

    "monitoringQuery": [],






398

    "monitoringSettings": [],






399

    "notificationCustomerBudget": [],






400

    "notificationDeploymentFailed": [],






401

    "notificationDomainConfiguration": [],






402

    "notificationDomainExpire": [],






403

    "notificationDomainMoved": [],






404

    "notificationDomainPurchase": [],






405

    "notificationDomainRenewal": [],






406

    "notificationDomainTransfer": [],






407

    "notificationDomainUnverified": [],






408

    "NotificationMonitoringAlert": [],






409

    "notificationPaymentFailed": [],






410

    "notificationPreferences": [],






411

    "notificationStatementOfReasons": [],






412

    "notificationUsageAlert": [],






413

    "observabilityConfiguration": [],






414

    "observabilityFunnel": [],






415

    "observabilityNotebook": [],






416

    "openTelemetryEndpoint": [],






417

    "ownEvent": [],






418

    "organizationDomain": [],






419

    "passwordProtectionInvoiceItem": [],






420

    "paymentMethod": [],






421

    "permissions": [],






422

    "postgres": [],






423

    "postgresStoreTokenSet": [],






424

    "previewDeploymentSuffix": [],






425

    "privateCloudAccount": [],






426

    "projectTransferIn": [],






427

    "proTrialOnboarding": [],






428

    "rateLimit": [],






429

    "redis": [],






430

    "redisStoreTokenSet": [],






431

    "remoteCaching": [],






432

    "repository": [],






433

    "samlConfig": [],






434

    "secret": [],






435

    "securityPlusConfiguration": [],






436

    "sensitiveEnvironmentVariablePolicy": [],






437

    "sharedEnvVars": [],






438

    "sharedEnvVarsProduction": [],






439

    "space": [],






440

    "spaceRun": [],






441

    "storeTransfer": [],






442

    "supportCase": [],






443

    "supportCaseComment": [],






444

    "team": [],






445

    "teamAccessRequest": [],






446

    "teamFellowMembership": [],






447

    "teamGitExclusivity": [],






448

    "teamInvite": [],






449

    "teamInviteCode": [],






450

    "teamJoin": [],






451

    "teamMemberMfaStatus": [],






452

    "teamMicrofrontends": [],






453

    "teamOwnMembership": [],






454

    "teamOwnMembershipDisconnectSAML": [],






455

    "token": [],






456

    "toolbarComment": [],






457

    "usage": [],






458

    "usageCycle": [],






459

    "vercelRun": [],






460

    "vercelRunExec": [],






461

    "vpcPeeringConnection": [],






462

    "webAnalyticsPlan": [],






463

    "webhook": [],






464

    "webhook-event": [],






465

    "aliasProject": [],






466

    "aliasProtectionBypass": [],






467

    "bulkRedirects": [],






468

    "buildMachine": [],






469

    "connectConfigurationLink": [],






470

    "dataCacheNamespace": [],






471

    "deployment": [],






472

    "deploymentBuildLogs": [],






473

    "deploymentCheck": [],






474

    "deploymentCheckPreview": [],






475

    "deploymentCheckReRunFromProductionBranch": [],






476

    "deploymentProductionGit": [],






477

    "deploymentV0": [],






478

    "deploymentPreview": [],






479

    "deploymentPrivate": [],






480

    "deploymentPromote": [],






481

    "deploymentRollback": [],






482

    "edgeCacheNamespace": [],






483

    "environments": [],






484

    "job": [],






485

    "logs": [],






486

    "logsPreset": [],






487

    "observabilityData": [],






488

    "onDemandBuild": [],






489

    "onDemandConcurrency": [],






490

    "optionsAllowlist": [],






491

    "passwordProtection": [],






492

    "productionAliasProtectionBypass": [],






493

    "project": [],






494

    "projectAccessGroup": [],






495

    "projectAnalyticsSampling": [],






496

    "projectAnalyticsUsage": [],






497

    "projectCheck": [],






498

    "projectCheckRun": [],






499

    "projectDeploymentExpiration": [],






500

    "projectDeploymentHook": [],






501

    "projectDeploymentProtectionStrict": [],






502

    "projectDomain": [],






503

    "projectDomainCheckConfig": [],






504

    "projectDomainMove": [],






505

    "projectEvent": [],






506

    "projectEnvVars": [],






507

    "projectEnvVarsProduction": [],






508

    "projectEnvVarsUnownedByIntegration": [],






509

    "projectFlags": [],






510

    "projectFlagsProduction": [],






511

    "projectFromV0": [],






512

    "projectId": [],






513

    "projectIntegrationConfiguration": [],






514

    "projectLink": [],






515

    "projectMember": [],






516

    "projectMonitoring": [],






517

    "projectOIDCToken": [],






518

    "projectPermissions": [],






519

    "projectProductionBranch": [],






520

    "projectProtectionBypass": [],






521

    "projectRollingRelease": [],






522

    "projectRoutes": [],






523

    "projectSupportCase": [],






524

    "projectSupportCaseComment": [],






525

    "projectTier": [],






526

    "projectTransfer": [],






527

    "projectTransferOut": [],






528

    "projectUsage": [],






529

    "seawallConfig": [],






530

    "sharedEnvVarConnection": [],






531

    "skewProtection": [],






532

    "analytics": [],






533

    "trustedIps": [],






534

    "v0Chat": [],






535

    "webAnalytics": []






536

  },






537

  "lastRollbackTarget": "value",






538

  "lastAliasRequest": {






539

    "fromDeploymentId": "example_id",






540

    "toDeploymentId": "example_id",






541

    "fromRollingReleaseId": "example_id",






542

    "jobStatus": "succeeded",






543

    "requestedAt": "123",






544

    "type": "promote"






545

  },






546

  "protectionBypass": "value",






547

  "hasActiveBranches": "false",






548

  "trustedIps": {






549

    "deploymentType": "production",






550

    "addresses": [






551

      {






552

        "value": "string",






553

        "note": "string"






554

      }






555

    ],






556

    "protectionMode": "additional"






557

  },






558

  "gitComments": {






559

    "onPullRequest": "false",






560

    "onCommit": "false"






561

  },






562

  "gitProviderOptions": {






563

    "createDeployments": "enabled",






564

    "disableRepositoryDispatchEvents": "false",






565

    "requireVerifiedCommits": "false"






566

  },






567

  "paused": "false",






568

  "concurrencyBucketName": "Example Name",






569

  "webAnalytics": {






570

    "id": "icfg_1234567890",






571

    "disabledAt": "123",






572

    "canceledAt": "123",






573

    "enabledAt": "123",






574

    "hasData": "true"






575

  },






576

  "security": {






577

    "attackModeEnabled": "false",






578

    "attackModeUpdatedAt": "123",






579

    "firewallEnabled": "false",






580

    "firewallUpdatedAt": "123",






581

    "attackModeActiveUntil": "123",






582

    "firewallConfigVersion": "123",






583

    "firewallSeawallEnabled": "false",






584

    "ja3Enabled": "false",






585

    "ja4Enabled": "false",






586

    "firewallBypassIps": [],






587

    "managedRules": {






588

      "vercel_ruleset": {






589

        "active": "false",






590

        "action": "log"






591

      },






592

      "bot_filter": {






593

        "active": "false",






594

        "action": "log"






595

      },






596

      "ai_bots": {






597

        "active": "false",






598

        "action": "log"






599

      },






600

      "owasp": {






601

        "active": "false",






602

        "action": "log"






603

      }






604

    },






605

    "botIdEnabled": "false"






606

  },






607

  "oidcTokenConfig": {






608

    "enabled": "false",






609

    "issuerMode": "team"






610

  },






611

  "tier": "standard",






612

  "scheduledTierChange": {






613

    "tier": "standard",






614

    "effectiveAt": "123"






615

  },






616

  "usageStatus": {






617

    "kind": "flat",






618

    "exceededAllowanceUntil": "123",






619

    "bypassThrottleUntil": "123"






620

  },






621

  "features": {






622

    "webAnalytics": "false"






623

  },






624

  "v0": "false",






625

  "abuse": {






626

    "scanner": "string",






627

    "history": [






628

      {






629

        "scanner": "string",






630

        "reason": "Customer requested refund",






631

        "by": "string",






632

        "byId": "example_id",






633

        "at": "123"






634

      }






635

    ],






636

    "updatedAt": "123",






637

    "block": {






638

      "action": "blocked",






639

      "reason": "Customer requested refund",






640

      "statusCode": "123",






641

      "createdAt": "123",






642

      "caseId": "example_id",






643

      "actor": "string",






644

      "comment": "string",






645

      "ineligibleForAppeal": "false",






646

      "isCascading": "false"






647

    },






648

    "blockHistory": [






649

      {






650

        "action": "blocked",






651

        "reason": "Customer requested refund",






652

        "statusCode": "123",






653

        "createdAt": "123",






654

        "caseId": "example_id",






655

        "actor": "string",






656

        "comment": "string",






657

        "ineligibleForAppeal": "false",






658

        "isCascading": "false"






659

      }






660

    ],






661

    "interstitial": "false"






662

  },






663

  "internalRoutes": [






664

    {






665

      "src": "string",






666

      "status": "123"






667

    }






668

  ],






669

  "hasDeployments": "false",






670

  "dismissedToasts": [






671

    {






672

      "key": "string",






673

      "dismissedAt": "123",






674

      "action": "delete",






675

      "value": "string"






676

    }






677

  ],






678

  "protectedSourcemaps": "false"






679

}




```
