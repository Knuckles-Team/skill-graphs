# Find a project by id or name
GET`https://api.vercel.com/v9/projects/{idOrName}`
Get the information for a specific project by passing either the project `id` or `name` in the URL.
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

    "integrationResourceReplCommand": [],






388

    "integrationResourceSecrets": [],






389

    "integrationSSOSession": [],






390

    "integrationStrict": [],






391

    "integrationStoreTokenSet": [],






392

    "integrationVercelConfigurationOverride": [],






393

    "integrationPullRequest": [],






394

    "ipBlocking": [],






395

    "jobGlobal": [],






396

    "logDrain": [],






397

    "marketplaceBillingData": [],






398

    "marketplaceExperimentationEdgeConfigData": [],






399

    "marketplaceExperimentationItem": [],






400

    "marketplaceInstallationMember": [],






401

    "marketplaceInvoice": [],






402

    "marketplaceSettings": [],






403

    "Monitoring": [],






404

    "monitoringAlert": [],






405

    "monitoringChart": [],






406

    "monitoringQuery": [],






407

    "monitoringSettings": [],






408

    "notificationCustomerBudget": [],






409

    "notificationDeploymentFailed": [],






410

    "notificationDomainConfiguration": [],






411

    "notificationDomainExpire": [],






412

    "notificationDomainMoved": [],






413

    "notificationDomainPurchase": [],






414

    "notificationDomainRenewal": [],






415

    "notificationDomainTransfer": [],






416

    "notificationDomainUnverified": [],






417

    "NotificationMonitoringAlert": [],






418

    "notificationPaymentFailed": [],






419

    "notificationPreferences": [],






420

    "notificationStatementOfReasons": [],






421

    "notificationUsageAlert": [],






422

    "observabilityConfiguration": [],






423

    "observabilityFunnel": [],






424

    "observabilityNotebook": [],






425

    "openTelemetryEndpoint": [],






426

    "ownEvent": [],






427

    "organizationDomain": [],






428

    "passwordProtectionInvoiceItem": [],






429

    "paymentMethod": [],






430

    "permissions": [],






431

    "postgres": [],






432

    "postgresStoreTokenSet": [],






433

    "previewDeploymentSuffix": [],






434

    "privateCloudAccount": [],






435

    "projectTransferIn": [],






436

    "proTrialOnboarding": [],






437

    "rateLimit": [],






438

    "redis": [],






439

    "redisStoreTokenSet": [],






440

    "remoteCaching": [],






441

    "repository": [],






442

    "samlConfig": [],






443

    "secret": [],






444

    "securityPlusConfiguration": [],






445

    "sensitiveEnvironmentVariablePolicy": [],






446

    "sharedEnvVars": [],






447

    "sharedEnvVarsProduction": [],






448

    "space": [],






449

    "spaceRun": [],






450

    "storeTransfer": [],






451

    "supportCase": [],






452

    "supportCaseComment": [],






453

    "team": [],






454

    "teamAccessRequest": [],






455

    "teamFellowMembership": [],






456

    "teamGitExclusivity": [],






457

    "teamInvite": [],






458

    "teamInviteCode": [],






459

    "teamJoin": [],






460

    "teamMemberMfaStatus": [],






461

    "teamMicrofrontends": [],






462

    "teamOwnMembership": [],






463

    "teamOwnMembershipDisconnectSAML": [],






464

    "token": [],






465

    "toolbarComment": [],






466

    "usage": [],






467

    "usageCycle": [],






468

    "vercelRun": [],






469

    "vercelRunExec": [],






470

    "vpcPeeringConnection": [],






471

    "webAnalyticsPlan": [],






472

    "webhook": [],






473

    "webhook-event": [],






474

    "aliasProject": [],






475

    "aliasProtectionBypass": [],






476

    "bulkRedirects": [],






477

    "buildMachine": [],






478

    "connectConfigurationLink": [],






479

    "dataCacheNamespace": [],






480

    "deployment": [],






481

    "deploymentBuildLogs": [],






482

    "deploymentCheck": [],






483

    "deploymentCheckPreview": [],






484

    "deploymentCheckReRunFromProductionBranch": [],






485

    "deploymentProductionGit": [],






486

    "deploymentV0": [],






487

    "deploymentPreview": [],






488

    "deploymentPrivate": [],






489

    "deploymentPromote": [],






490

    "deploymentRollback": [],






491

    "edgeCacheNamespace": [],






492

    "environments": [],






493

    "job": [],






494

    "logs": [],






495

    "logsPreset": [],






496

    "observabilityData": [],






497

    "onDemandBuild": [],






498

    "onDemandConcurrency": [],






499

    "optionsAllowlist": [],






500

    "passwordProtection": [],






501

    "productionAliasProtectionBypass": [],






502

    "project": [],






503

    "projectAccessGroup": [],






504

    "projectAnalyticsSampling": [],






505

    "projectAnalyticsUsage": [],






506

    "projectCheck": [],






507

    "projectCheckRun": [],






508

    "projectDeploymentExpiration": [],






509

    "projectDeploymentHook": [],






510

    "projectDeploymentProtectionStrict": [],






511

    "projectDomain": [],






512

    "projectDomainCheckConfig": [],






513

    "projectDomainMove": [],






514

    "projectEvent": [],






515

    "projectEnvVars": [],






516

    "projectEnvVarsProduction": [],






517

    "projectEnvVarsUnownedByIntegration": [],






518

    "projectFlags": [],






519

    "projectFlagsProduction": [],






520

    "projectFromV0": [],






521

    "projectId": [],






522

    "projectIntegrationConfiguration": [],






523

    "projectLink": [],






524

    "projectMember": [],






525

    "projectMonitoring": [],






526

    "projectOIDCToken": [],






527

    "projectPermissions": [],






528

    "projectProductionBranch": [],






529

    "projectProtectionBypass": [],






530

    "projectRollingRelease": [],






531

    "projectRoutes": [],






532

    "projectSupportCase": [],






533

    "projectSupportCaseComment": [],






534

    "projectTier": [],






535

    "projectTransfer": [],






536

    "projectTransferOut": [],






537

    "projectUsage": [],






538

    "seawallConfig": [],






539

    "sharedEnvVarConnection": [],






540

    "skewProtection": [],






541

    "analytics": [],






542

    "trustedIps": [],






543

    "v0Chat": [],






544

    "webAnalytics": []






545

  },






546

  "lastRollbackTarget": "value",






547

  "lastAliasRequest": {






548

    "fromDeploymentId": "example_id",






549

    "toDeploymentId": "example_id",






550

    "fromRollingReleaseId": "example_id",






551

    "jobStatus": "succeeded",






552

    "requestedAt": "123",






553

    "type": "promote"






554

  },






555

  "protectionBypass": "value",






556

  "hasActiveBranches": "false",






557

  "trustedIps": {






558

    "deploymentType": "production",






559

    "addresses": [






560

      {






561

        "value": "string",






562

        "note": "string"






563

      }






564

    ],






565

    "protectionMode": "additional"






566

  },






567

  "gitComments": {






568

    "onPullRequest": "false",






569

    "onCommit": "false"






570

  },






571

  "gitProviderOptions": {






572

    "createDeployments": "enabled",






573

    "disableRepositoryDispatchEvents": "false",






574

    "requireVerifiedCommits": "false"






575

  },






576

  "paused": "false",






577

  "concurrencyBucketName": "Example Name",






578

  "webAnalytics": {






579

    "id": "icfg_1234567890",






580

    "disabledAt": "123",






581

    "canceledAt": "123",






582

    "enabledAt": "123",






583

    "hasData": "true"






584

  },






585

  "security": {






586

    "attackModeEnabled": "false",






587

    "attackModeUpdatedAt": "123",






588

    "firewallEnabled": "false",






589

    "firewallUpdatedAt": "123",






590

    "attackModeActiveUntil": "123",






591

    "firewallConfigVersion": "123",






592

    "firewallSeawallEnabled": "false",






593

    "ja3Enabled": "false",






594

    "ja4Enabled": "false",






595

    "firewallBypassIps": [],






596

    "managedRules": {






597

      "vercel_ruleset": {






598

        "active": "false",






599

        "action": "log"






600

      },






601

      "bot_filter": {






602

        "active": "false",






603

        "action": "log"






604

      },






605

      "ai_bots": {






606

        "active": "false",






607

        "action": "log"






608

      },






609

      "owasp": {






610

        "active": "false",






611

        "action": "log"






612

      }






613

    },






614

    "botIdEnabled": "false"






615

  },






616

  "oidcTokenConfig": {






617

    "enabled": "false",






618

    "issuerMode": "team"






619

  },






620

  "tier": "standard",






621

  "scheduledTierChange": {






622

    "tier": "standard",






623

    "effectiveAt": "123"






624

  },






625

  "usageStatus": {






626

    "kind": "flat",






627

    "exceededAllowanceUntil": "123",






628

    "bypassThrottleUntil": "123"






629

  },






630

  "features": {






631

    "webAnalytics": "false"






632

  },






633

  "v0": "false",






634

  "abuse": {






635

    "scanner": "string",






636

    "history": [






637

      {






638

        "scanner": "string",






639

        "reason": "Customer requested refund",






640

        "by": "string",






641

        "byId": "example_id",






642

        "at": "123"






643

      }






644

    ],






645

    "updatedAt": "123",






646

    "block": {






647

      "action": "blocked",






648

      "reason": "Customer requested refund",






649

      "statusCode": "123",






650

      "createdAt": "123",






651

      "caseId": "example_id",






652

      "actor": "string",






653

      "comment": "string",






654

      "ineligibleForAppeal": "false",






655

      "isCascading": "false"






656

    },






657

    "blockHistory": [






658

      {






659

        "action": "blocked",






660

        "reason": "Customer requested refund",






661

        "statusCode": "123",






662

        "createdAt": "123",






663

        "caseId": "example_id",






664

        "actor": "string",






665

        "comment": "string",






666

        "ineligibleForAppeal": "false",






667

        "isCascading": "false"






668

      }






669

    ],






670

    "interstitial": "false"






671

  },






672

  "internalRoutes": [






673

    {






674

      "src": "string",






675

      "status": "123"






676

    }






677

  ],






678

  "hasDeployments": "false",






679

  "dismissedToasts": [






680

    {






681

      "key": "string",






682

      "dismissedAt": "123",






683

      "action": "delete",






684

      "value": "string"






685

    }






686

  ],






687

  "protectedSourcemaps": "false"






688

}




```
