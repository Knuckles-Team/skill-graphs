##  [Errors](https://vercel.com/docs/rest-api/projects/find-a-project-by-id-or-name#errors)[](https://vercel.com/docs/rest-api/projects/find-a-project-by-id-or-name#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
TypeScriptNext.jscURL
https://api.vercel.com/v9/projects/{idOrName}
```


1

const response = await fetch('https://api.vercel.com/v9/projects/idOrName?teamId=string&slug=string', {






2

  method: 'GET',






3

  headers: {






4

    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',






5

    'Content-Type': 'application/json',






6

  },






7

});






8







9

const data = await response.json();






10

console.log(data);




```

Response
```


1

{






2

  "integrations": [






3

    {






4

      "installationId": "icfg_3bwCLgxL8qt5kjRLcv2Dit7F",






5

      "resources": [






6

        {






7

          "externalResourceId": "example_id"






8

        }






9

      ]






10

    }






11

  ],






12

  "accountId": "example_id",






13

  "analytics": {






14

    "id": "icfg_1234567890",






15

    "canceledAt": "123",






16

    "disabledAt": "123",






17

    "enabledAt": "123",






18

    "paidAt": "123",






19

    "sampleRatePercent": "123",






20

    "spendLimitInDollars": "123"






21

  },






22

  "appliedCve55182Migration": "false",






23

  "speedInsights": {






24

    "id": "icfg_1234567890",






25

    "enabledAt": "123",






26

    "disabledAt": "123",






27

    "canceledAt": "123",






28

    "hasData": "false",






29

    "paidAt": "123"






30

  },






31

  "autoExposeSystemEnvs": "false",






32

  "autoAssignCustomDomains": "false",






33

  "autoAssignCustomDomainsUpdatedBy": "string",






34

  "buildCommand": "string",






35

  "commandForIgnoringBuildStep": "string",






36

  "connectConfigurations": [






37

    {






38

      "envId": "example_id",






39

      "connectConfigurationId": "example_id",






40

      "dc": "string",






41

      "passive": "false",






42

      "buildsEnabled": "false",






43

      "aws": {






44

        "subnetIds": [],






45

        "securityGroupId": "https://example.com"






46

      },






47

      "createdAt": "123",






48

      "updatedAt": "123"






49

    }






50

  ],






51

  "connectConfigurationId": "example_id",






52

  "connectBuildsEnabled": "false",






53

  "passiveConnectConfigurationId": "example_id",






54

  "createdAt": "123",






55

  "customerSupportCodeVisibility": "false",






56

  "crons": {






57

    "enabledAt": "123",






58

    "disabledAt": "123",






59

    "updatedAt": "123",






60

    "deploymentId": "example_id",






61

    "definitions": [






62

      {






63

        "host": "vercel.com",






64

        "path": "/api/crons/sync-something?hello=world",






65

        "schedule": "0 0 * * *"






66

      }






67

    ]






68

  },






69

  "dataCache": {






70

    "userDisabled": "false",






71

    "storageSizeBytes": "123",






72

    "unlimited": "false"






73

  },






74

  "deploymentExpiration": {






75

    "expirationDays": "123",






76

    "expirationDaysProduction": "123",






77

    "expirationDaysCanceled": "123",






78

    "expirationDaysErrored": "123",






79

    "deploymentsToKeep": "123"






80

  },






81

  "devCommand": "string",






82

  "directoryListing": "false",






83

  "installCommand": "string",






84

  "env": [






85

    {






86

      "target": [],






87

      "type": "secret",






88

      "sunsetSecretId": "example_id",






89

      "legacyValue": "string",






90

      "decrypted": "false",






91

      "value": "string",






92

      "vsmValue": "string",






93

      "id": "icfg_1234567890",






94

      "key": "string",






95

      "configurationId": "example_id",






96

      "createdAt": "123",






97

      "updatedAt": "123",






98

      "createdBy": "string",






99

      "updatedBy": "string",






100

      "gitBranch": "string",






101

      "edgeConfigId": "example_id",






102

      "edgeConfigTokenId": "example_id",






103

      "contentHint": {






104

        "type": "redis-url",






105

        "storeId": "example_id"






106

      },






107

      "internalContentHint": {






108

        "type": "flags-secret",






109

        "encryptedValue": "string"






110

      },






111

      "comment": "string",






112

      "customEnvironmentIds": []






113

    }






114

  ],






115

  "customEnvironments": [






116

    {






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

          "redirectStatusCode": "301",






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

    }






151

  ],






152

  "framework": "services",






153

  "gitForkProtection": "false",






154

  "gitLFS": "false",






155

  "id": "icfg_1234567890",






156

  "ipBuckets": [






157

    {






158

      "bucket": "string",






159

      "supportUntil": "123"






160

    }






161

  ],






162

  "latestDeployments": [






163

    {






164

      "alias": [],






165

      "aliasAssigned": "123",






166

      "builds": [






167

        {






168

          "use": "string",






169

          "src": "string",






170

          "dest": "string"






171

        }






172

      ],






173

      "createdAt": "123",






174

      "createdIn": "string",






175

      "creator": {






176

        "email": "user@example.com",






177

        "githubLogin": "string",






178

        "gitlabLogin": "string",






179

        "uid": "example_id",






180

        "username": "string"






181

      },






182

      "deploymentHostname": "Example Name",






183

      "name": "Example Name",






184

      "forced": "false",






185

      "id": "icfg_1234567890",






186

      "meta": "value",






187

      "plan": "string",






188

      "private": "false",






189

      "readyState": "string",






190

      "requestedAt": "123",






191

      "target": "string",






192

      "teamId": "example_id",






193

      "type": "string",






194

      "url": "https://example.com",






195

      "userId": "example_id",






196

      "withCache": "false"






197

    }






198

  ],






199

  "link": {






200

    "org": "string",






201

    "repoOwnerId": "123",






202

    "repo": "string",






203

    "repoId": "123",






204

    "type": "github",






205

    "createdAt": "123",






206

    "deployHooks": [






207

      {






208

        "createdAt": "123",






209

        "id": "icfg_1234567890",






210

        "name": "Example Name",






211

        "ref": "string",






212

        "url": "https://example.com"






213

      }






214

    ],






215

    "gitCredentialId": "example_id",






216

    "updatedAt": "123",






217

    "sourceless": "false",






218

    "productionBranch": "string"






219

  },






220

  "microfrontends": {






221

    "isDefaultApp": "true",






222

    "updatedAt": "123",






223

    "groupIds": [],






224

    "enabled": "true",






225

    "defaultRoute": "string",






226

    "freeProjectForLegacyLimits": "false"






227

  },






228

  "name": "Example Name",






229

  "nodeVersion": "24.x",






230

  "optionsAllowlist": {






231

    "paths": [






232

      {






233

        "value": "string"






234

      }






235

    ]






236

  },






237

  "outputDirectory": "string",






238

  "passwordProtection": "value",






239

  "productionDeploymentsFastLane": "false",






240

  "publicSource": "false",






241

  "resourceConfig": {






242

    "elasticConcurrencyEnabled": "false",






243

    "fluid": "false",






244

    "functionDefaultRegions": [],






245

    "functionDefaultTimeout": "123",






246

    "functionDefaultMemoryType": "standard_legacy",






247

    "functionZeroConfigFailover": "false",






248

    "buildMachineType": "standard",






249

    "buildMachineSelection": "fixed",






250

    "buildMachineElasticLastUpdated": "123",






251

    "isNSNBDisabled": "false",






252

    "buildQueue": {






253

      "configuration": "SKIP_NAMESPACE_QUEUE"






254

    }






255

  },






256

  "rollbackDescription": {






257

    "userId": "example_id",






258

    "username": "string",






259

    "description": "string",






260

    "createdAt": "123"






261

  },






262

  "rollingRelease": {






263

    "target": "production",






264

    "stages": [






265

      {






266

        "targetPercentage": "25",






267

        "requireApproval": "false",






268

        "duration": "600",






269

        "linearShift": "false"






270

      }






271

    ],






272

    "canaryResponseHeader": "false"






273

  },






274

  "defaultResourceConfig": {






275

    "elasticConcurrencyEnabled": "false",






276

    "fluid": "false",






277

    "functionDefaultRegions": [],






278

    "functionDefaultTimeout": "123",






279

    "functionDefaultMemoryType": "standard_legacy",






280

    "functionZeroConfigFailover": "false",






281

    "buildMachineType": "standard",






282

    "buildMachineSelection": "fixed",






283

    "buildMachineElasticLastUpdated": "123",






284

    "isNSNBDisabled": "false",






285

    "buildQueue": {






286

      "configuration": "SKIP_NAMESPACE_QUEUE"






287

    }






288

  },






289

  "rootDirectory": "string",






290

  "serverlessFunctionZeroConfigFailover": "false",






291

  "skewProtectionBoundaryAt": "123",






292

  "skewProtectionMaxAge": "123",






293

  "skewProtectionAllowedDomains": [],






294

  "skipGitConnectDuringLink": "false",






295

  "staticIps": {






296

    "builds": "false",






297

    "enabled": "false",






298

    "regions": []






299

  },






300

  "sourceFilesOutsideRootDirectory": "false",






301

  "enableAffectedProjectsDeployments": "false",






302

  "ssoProtection": {






303

    "deploymentType": "preview",






304

    "cve55182MigrationAppliedFrom": "preview"






305

  },






306

  "targets": "value",






307

  "transferCompletedAt": "123",






308

  "transferStartedAt": "123",






309

  "transferToAccountId": "example_id",






310

  "transferredFromAccountId": "example_id",






311

  "updatedAt": "123",






312

  "live": "false",






313

  "enablePreviewFeedback": "false",






314

  "enableProductionFeedback": "false",






315

  "permissions": {






316

    "oauth2Connection": [],






317

    "user": [],






318

    "userConnection": [],






319

    "userSudo": [],






320

    "webAuthn": [],






321

    "accessGroup": [],






322

    "agent": [],






323

    "aiGatewayUsage": [],






324

    "alerts": [],






325

    "alertRules": [],






326

    "aliasGlobal": [],






327

    "analyticsSampling": [],






328

    "analyticsUsage": [],






329

    "apiKey": [],






330

    "apiKeyAiGateway": [],






331

    "apiKeyOwnedBySelf": [],






332

    "oauth2Application": [],






333

    "vercelAppInstallation": [],






334

    "vercelAppInstallationRequest": [],






335

    "auditLog": [],






336

    "billingAddress": [],






337

    "billingInformation": [],






338

    "billingInvoice": [],






339

    "billingInvoiceEmailRecipient": [],






340

    "billingInvoiceLanguage": [],






341

    "billingPlan": [],






342

    "billingPurchaseOrder": [],






343

    "billingRefund": [],






344

    "billingTaxId": [],






345

    "blob": [],






346

    "blobStoreTokenSet": [],






347

    "budget": [],






348

    "cacheArtifact": [],






349

    "cacheArtifactUsageEvent": [],






350

    "codeChecks": [],






351

    "concurrentBuilds": [],






352

    "connect": [],






353

    "connectConfiguration": [],






354

    "buildMachineDefault": [],






355

    "dataCacheBillingSettings": [],






356

    "defaultDeploymentProtection": [],






357

    "domain": [],






358

    "domainAcceptDelegation": [],






359

    "domainAuthCodes": [],






360

    "domainCertificate": [],






361

    "domainCheckConfig": [],






362

    "domainMove": [],






363

    "domainPurchase": [],






364

    "domainRecord": [],






365

    "domainTransferIn": [],






366

    "drain": [],






367

    "edgeConfig": [],






368

    "edgeConfigItem": [],






369

    "edgeConfigSchema": [],






370

    "edgeConfigToken": [],






371

    "endpointVerification": [],






372

    "event": [],






373

    "fileUpload": [],






374

    "flagsExplorerSubscription": [],






375

    "gitRepository": [],






376

    "imageOptimizationNewPrice": [],






377

    "integration": [],






378

    "integrationAccount": [],






379

    "integrationConfiguration": [],






380

    "integrationConfigurationProjects": [],






381

    "integrationConfigurationRole": [],






382

    "integrationConfigurationTransfer": [],






383

    "integrationDeploymentAction": [],






384

    "integrationEvent": [],






385

    "integrationLog": [],






386

    "integrationResource": [],






387

    "integrationResourceData": [],






388

    "integrationResourceReplCommand": [],






389

    "integrationResourceSecrets": [],






390

    "integrationSSOSession": [],






391

    "integrationStrict": [],






392

    "integrationStoreTokenSet": [],






393

    "integrationVercelConfigurationOverride": [],






394

    "integrationPullRequest": [],






395

    "ipBlocking": [],






396

    "jobGlobal": [],






397

    "logDrain": [],






398

    "marketplaceBillingData": [],






399

    "marketplaceExperimentationEdgeConfigData": [],






400

    "marketplaceExperimentationItem": [],






401

    "marketplaceInstallationMember": [],






402

    "marketplaceInvoice": [],






403

    "marketplaceSettings": [],






404

    "Monitoring": [],






405

    "monitoringAlert": [],






406

    "monitoringChart": [],






407

    "monitoringQuery": [],






408

    "monitoringSettings": [],






409

    "notificationCustomerBudget": [],






410

    "notificationDeploymentFailed": [],






411

    "notificationDomainConfiguration": [],






412

    "notificationDomainExpire": [],






413

    "notificationDomainMoved": [],






414

    "notificationDomainPurchase": [],






415

    "notificationDomainRenewal": [],






416

    "notificationDomainTransfer": [],






417

    "notificationDomainUnverified": [],






418

    "NotificationMonitoringAlert": [],






419

    "notificationPaymentFailed": [],






420

    "notificationPreferences": [],






421

    "notificationStatementOfReasons": [],






422

    "notificationUsageAlert": [],






423

    "observabilityConfiguration": [],






424

    "observabilityFunnel": [],






425

    "observabilityNotebook": [],






426

    "openTelemetryEndpoint": [],






427

    "ownEvent": [],






428

    "organizationDomain": [],






429

    "passwordProtectionInvoiceItem": [],






430

    "paymentMethod": [],






431

    "permissions": [],






432

    "postgres": [],






433

    "postgresStoreTokenSet": [],






434

    "previewDeploymentSuffix": [],






435

    "privateCloudAccount": [],






436

    "projectTransferIn": [],






437

    "proTrialOnboarding": [],






438

    "rateLimit": [],






439

    "redis": [],






440

    "redisStoreTokenSet": [],






441

    "remoteCaching": [],






442

    "repository": [],






443

    "samlConfig": [],






444

    "secret": [],






445

    "securityPlusConfiguration": [],






446

    "sensitiveEnvironmentVariablePolicy": [],






447

    "sharedEnvVars": [],






448

    "sharedEnvVarsProduction": [],






449

    "space": [],






450

    "spaceRun": [],






451

    "storeTransfer": [],






452

    "supportCase": [],






453

    "supportCaseComment": [],






454

    "team": [],






455

    "teamAccessRequest": [],






456

    "teamFellowMembership": [],






457

    "teamGitExclusivity": [],






458

    "teamInvite": [],






459

    "teamInviteCode": [],






460

    "teamJoin": [],






461

    "teamMemberMfaStatus": [],






462

    "teamMicrofrontends": [],






463

    "teamOwnMembership": [],






464

    "teamOwnMembershipDisconnectSAML": [],






465

    "token": [],






466

    "toolbarComment": [],






467

    "usage": [],






468

    "usageCycle": [],






469

    "vercelRun": [],






470

    "vercelRunExec": [],






471

    "vpcPeeringConnection": [],






472

    "webAnalyticsPlan": [],






473

    "webhook": [],






474

    "webhook-event": [],






475

    "aliasProject": [],






476

    "aliasProtectionBypass": [],






477

    "bulkRedirects": [],






478

    "buildMachine": [],






479

    "connectConfigurationLink": [],






480

    "dataCacheNamespace": [],






481

    "deployment": [],






482

    "deploymentBuildLogs": [],






483

    "deploymentCheck": [],






484

    "deploymentCheckPreview": [],






485

    "deploymentCheckReRunFromProductionBranch": [],






486

    "deploymentProductionGit": [],






487

    "deploymentV0": [],






488

    "deploymentPreview": [],






489

    "deploymentPrivate": [],






490

    "deploymentPromote": [],






491

    "deploymentRollback": [],






492

    "edgeCacheNamespace": [],






493

    "environments": [],






494

    "job": [],






495

    "logs": [],






496

    "logsPreset": [],






497

    "observabilityData": [],






498

    "onDemandBuild": [],






499

    "onDemandConcurrency": [],






500

    "optionsAllowlist": [],






501

    "passwordProtection": [],






502

    "productionAliasProtectionBypass": [],






503

    "project": [],






504

    "projectAccessGroup": [],






505

    "projectAnalyticsSampling": [],






506

    "projectAnalyticsUsage": [],






507

    "projectCheck": [],






508

    "projectCheckRun": [],






509

    "projectDeploymentExpiration": [],






510

    "projectDeploymentHook": [],






511

    "projectDeploymentProtectionStrict": [],






512

    "projectDomain": [],






513

    "projectDomainCheckConfig": [],






514

    "projectDomainMove": [],






515

    "projectEvent": [],






516

    "projectEnvVars": [],






517

    "projectEnvVarsProduction": [],






518

    "projectEnvVarsUnownedByIntegration": [],






519

    "projectFlags": [],






520

    "projectFlagsProduction": [],






521

    "projectFromV0": [],






522

    "projectId": [],






523

    "projectIntegrationConfiguration": [],






524

    "projectLink": [],






525

    "projectMember": [],






526

    "projectMonitoring": [],






527

    "projectOIDCToken": [],






528

    "projectPermissions": [],






529

    "projectProductionBranch": [],






530

    "projectProtectionBypass": [],






531

    "projectRollingRelease": [],






532

    "projectRoutes": [],






533

    "projectSupportCase": [],






534

    "projectSupportCaseComment": [],






535

    "projectTier": [],






536

    "projectTransfer": [],






537

    "projectTransferOut": [],






538

    "projectUsage": [],






539

    "seawallConfig": [],






540

    "sharedEnvVarConnection": [],






541

    "skewProtection": [],






542

    "analytics": [],






543

    "trustedIps": [],






544

    "v0Chat": [],






545

    "webAnalytics": []






546

  },






547

  "lastRollbackTarget": "value",






548

  "lastAliasRequest": {






549

    "fromDeploymentId": "example_id",






550

    "toDeploymentId": "example_id",






551

    "fromRollingReleaseId": "example_id",






552

    "jobStatus": "succeeded",






553

    "requestedAt": "123",






554

    "type": "promote"






555

  },






556

  "protectionBypass": "value",






557

  "hasActiveBranches": "false",






558

  "trustedIps": {






559

    "deploymentType": "production",






560

    "addresses": [






561

      {






562

        "value": "string",






563

        "note": "string"






564

      }






565

    ],






566

    "protectionMode": "additional"






567

  },






568

  "gitComments": {






569

    "onPullRequest": "false",






570

    "onCommit": "false"






571

  },






572

  "gitProviderOptions": {






573

    "createDeployments": "enabled",






574

    "disableRepositoryDispatchEvents": "false",






575

    "requireVerifiedCommits": "false"






576

  },






577

  "paused": "false",






578

  "concurrencyBucketName": "Example Name",






579

  "webAnalytics": {






580

    "id": "icfg_1234567890",






581

    "disabledAt": "123",






582

    "canceledAt": "123",






583

    "enabledAt": "123",






584

    "hasData": "true"






585

  },






586

  "security": {






587

    "attackModeEnabled": "false",






588

    "attackModeUpdatedAt": "123",






589

    "firewallEnabled": "false",






590

    "firewallUpdatedAt": "123",






591

    "attackModeActiveUntil": "123",






592

    "firewallConfigVersion": "123",






593

    "firewallSeawallEnabled": "false",






594

    "ja3Enabled": "false",






595

    "ja4Enabled": "false",






596

    "firewallBypassIps": [],






597

    "managedRules": {






598

      "vercel_ruleset": {






599

        "active": "false",






600

        "action": "log"






601

      },






602

      "bot_filter": {






603

        "active": "false",






604

        "action": "log"






605

      },






606

      "ai_bots": {






607

        "active": "false",






608

        "action": "log"






609

      },






610

      "owasp": {






611

        "active": "false",






612

        "action": "log"






613

      }






614

    },






615

    "botIdEnabled": "false"






616

  },






617

  "oidcTokenConfig": {






618

    "enabled": "false",






619

    "issuerMode": "team"






620

  },






621

  "tier": "standard",






622

  "scheduledTierChange": {






623

    "tier": "standard",






624

    "effectiveAt": "123"






625

  },






626

  "usageStatus": {






627

    "kind": "flat",






628

    "exceededAllowanceUntil": "123",






629

    "bypassThrottleUntil": "123"






630

  },






631

  "features": {






632

    "webAnalytics": "false"






633

  },






634

  "v0": "false",






635

  "abuse": {






636

    "scanner": "string",






637

    "history": [






638

      {






639

        "scanner": "string",






640

        "reason": "Customer requested refund",






641

        "by": "string",






642

        "byId": "example_id",






643

        "at": "123"






644

      }






645

    ],






646

    "updatedAt": "123",






647

    "block": {






648

      "action": "blocked",






649

      "reason": "Customer requested refund",






650

      "statusCode": "123",






651

      "createdAt": "123",






652

      "caseId": "example_id",






653

      "actor": "string",






654

      "comment": "string",






655

      "ineligibleForAppeal": "false",






656

      "isCascading": "false"






657

    },






658

    "blockHistory": [






659

      {






660

        "action": "blocked",






661

        "reason": "Customer requested refund",






662

        "statusCode": "123",






663

        "createdAt": "123",






664

        "caseId": "example_id",






665

        "actor": "string",






666

        "comment": "string",






667

        "ineligibleForAppeal": "false",






668

        "isCascading": "false"






669

      }






670

    ],






671

    "interstitial": "false"






672

  },






673

  "internalRoutes": [






674

    {






675

      "src": "string",






676

      "status": "123"






677

    }






678

  ],






679

  "hasDeployments": "false",






680

  "dismissedToasts": [






681

    {






682

      "key": "string",






683

      "dismissedAt": "123",






684

      "action": "delete",






685

      "value": "string"






686

    }






687

  ],






688

  "protectedSourcemaps": "false"






689

}




```

Copy as MarkdownGive feedbackAsk AI about this page
