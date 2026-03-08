# Create a new project
POST`https://api.vercel.com/v11/projects`
Allows to create a new project with the provided configuration. It only requires the project `name` but more configuration can be provided to override the defaults.
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

  const result = await vercel.projects.createProject({






9

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






10

    slug: "my-team-url-slug",






11

    requestBody: {






12

      name: "a-project-name",






13

    },






14

  });






15







16

  console.log(result);






17

}






18







19

run();




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

    "integrationResourceReplCommand": [],






378

    "integrationResourceSecrets": [],






379

    "integrationSSOSession": [],






380

    "integrationStrict": [],






381

    "integrationStoreTokenSet": [],






382

    "integrationVercelConfigurationOverride": [],






383

    "integrationPullRequest": [],






384

    "ipBlocking": [],






385

    "jobGlobal": [],






386

    "logDrain": [],






387

    "marketplaceBillingData": [],






388

    "marketplaceExperimentationEdgeConfigData": [],






389

    "marketplaceExperimentationItem": [],






390

    "marketplaceInstallationMember": [],






391

    "marketplaceInvoice": [],






392

    "marketplaceSettings": [],






393

    "Monitoring": [],






394

    "monitoringAlert": [],






395

    "monitoringChart": [],






396

    "monitoringQuery": [],






397

    "monitoringSettings": [],






398

    "notificationCustomerBudget": [],






399

    "notificationDeploymentFailed": [],






400

    "notificationDomainConfiguration": [],






401

    "notificationDomainExpire": [],






402

    "notificationDomainMoved": [],






403

    "notificationDomainPurchase": [],






404

    "notificationDomainRenewal": [],






405

    "notificationDomainTransfer": [],






406

    "notificationDomainUnverified": [],






407

    "NotificationMonitoringAlert": [],






408

    "notificationPaymentFailed": [],






409

    "notificationPreferences": [],






410

    "notificationStatementOfReasons": [],






411

    "notificationUsageAlert": [],






412

    "observabilityConfiguration": [],






413

    "observabilityFunnel": [],






414

    "observabilityNotebook": [],






415

    "openTelemetryEndpoint": [],






416

    "ownEvent": [],






417

    "organizationDomain": [],






418

    "passwordProtectionInvoiceItem": [],






419

    "paymentMethod": [],






420

    "permissions": [],






421

    "postgres": [],






422

    "postgresStoreTokenSet": [],






423

    "previewDeploymentSuffix": [],






424

    "privateCloudAccount": [],






425

    "projectTransferIn": [],






426

    "proTrialOnboarding": [],






427

    "rateLimit": [],






428

    "redis": [],






429

    "redisStoreTokenSet": [],






430

    "remoteCaching": [],






431

    "repository": [],






432

    "samlConfig": [],






433

    "secret": [],






434

    "securityPlusConfiguration": [],






435

    "sensitiveEnvironmentVariablePolicy": [],






436

    "sharedEnvVars": [],






437

    "sharedEnvVarsProduction": [],






438

    "space": [],






439

    "spaceRun": [],






440

    "storeTransfer": [],






441

    "supportCase": [],






442

    "supportCaseComment": [],






443

    "team": [],






444

    "teamAccessRequest": [],






445

    "teamFellowMembership": [],






446

    "teamGitExclusivity": [],






447

    "teamInvite": [],






448

    "teamInviteCode": [],






449

    "teamJoin": [],






450

    "teamMemberMfaStatus": [],






451

    "teamMicrofrontends": [],






452

    "teamOwnMembership": [],






453

    "teamOwnMembershipDisconnectSAML": [],






454

    "token": [],






455

    "toolbarComment": [],






456

    "usage": [],






457

    "usageCycle": [],






458

    "vercelRun": [],






459

    "vercelRunExec": [],






460

    "vpcPeeringConnection": [],






461

    "webAnalyticsPlan": [],






462

    "webhook": [],






463

    "webhook-event": [],






464

    "aliasProject": [],






465

    "aliasProtectionBypass": [],






466

    "bulkRedirects": [],






467

    "buildMachine": [],






468

    "connectConfigurationLink": [],






469

    "dataCacheNamespace": [],






470

    "deployment": [],






471

    "deploymentBuildLogs": [],






472

    "deploymentCheck": [],






473

    "deploymentCheckPreview": [],






474

    "deploymentCheckReRunFromProductionBranch": [],






475

    "deploymentProductionGit": [],






476

    "deploymentV0": [],






477

    "deploymentPreview": [],






478

    "deploymentPrivate": [],






479

    "deploymentPromote": [],






480

    "deploymentRollback": [],






481

    "edgeCacheNamespace": [],






482

    "environments": [],






483

    "job": [],






484

    "logs": [],






485

    "logsPreset": [],






486

    "observabilityData": [],






487

    "onDemandBuild": [],






488

    "onDemandConcurrency": [],






489

    "optionsAllowlist": [],






490

    "passwordProtection": [],






491

    "productionAliasProtectionBypass": [],






492

    "project": [],






493

    "projectAccessGroup": [],






494

    "projectAnalyticsSampling": [],






495

    "projectAnalyticsUsage": [],






496

    "projectCheck": [],






497

    "projectCheckRun": [],






498

    "projectDeploymentExpiration": [],






499

    "projectDeploymentHook": [],






500

    "projectDeploymentProtectionStrict": [],






501

    "projectDomain": [],






502

    "projectDomainCheckConfig": [],






503

    "projectDomainMove": [],






504

    "projectEvent": [],






505

    "projectEnvVars": [],






506

    "projectEnvVarsProduction": [],






507

    "projectEnvVarsUnownedByIntegration": [],






508

    "projectFlags": [],






509

    "projectFlagsProduction": [],






510

    "projectFromV0": [],






511

    "projectId": [],






512

    "projectIntegrationConfiguration": [],






513

    "projectLink": [],






514

    "projectMember": [],






515

    "projectMonitoring": [],






516

    "projectOIDCToken": [],






517

    "projectPermissions": [],






518

    "projectProductionBranch": [],






519

    "projectProtectionBypass": [],






520

    "projectRollingRelease": [],






521

    "projectRoutes": [],






522

    "projectSupportCase": [],






523

    "projectSupportCaseComment": [],






524

    "projectTier": [],






525

    "projectTransfer": [],






526

    "projectTransferOut": [],






527

    "projectUsage": [],






528

    "seawallConfig": [],






529

    "sharedEnvVarConnection": [],






530

    "skewProtection": [],






531

    "analytics": [],






532

    "trustedIps": [],






533

    "v0Chat": [],






534

    "webAnalytics": []






535

  },






536

  "lastRollbackTarget": "value",






537

  "lastAliasRequest": {






538

    "fromDeploymentId": "example_id",






539

    "toDeploymentId": "example_id",






540

    "fromRollingReleaseId": "example_id",






541

    "jobStatus": "succeeded",






542

    "requestedAt": "123",






543

    "type": "promote"






544

  },






545

  "protectionBypass": "value",






546

  "hasActiveBranches": "false",






547

  "trustedIps": {






548

    "deploymentType": "production",






549

    "addresses": [






550

      {






551

        "value": "string",






552

        "note": "string"






553

      }






554

    ],






555

    "protectionMode": "additional"






556

  },






557

  "gitComments": {






558

    "onPullRequest": "false",






559

    "onCommit": "false"






560

  },






561

  "gitProviderOptions": {






562

    "createDeployments": "enabled",






563

    "disableRepositoryDispatchEvents": "false",






564

    "requireVerifiedCommits": "false"






565

  },






566

  "paused": "false",






567

  "concurrencyBucketName": "Example Name",






568

  "webAnalytics": {






569

    "id": "icfg_1234567890",






570

    "disabledAt": "123",






571

    "canceledAt": "123",






572

    "enabledAt": "123",






573

    "hasData": "true"






574

  },






575

  "security": {






576

    "attackModeEnabled": "false",






577

    "attackModeUpdatedAt": "123",






578

    "firewallEnabled": "false",






579

    "firewallUpdatedAt": "123",






580

    "attackModeActiveUntil": "123",






581

    "firewallConfigVersion": "123",






582

    "firewallSeawallEnabled": "false",






583

    "ja3Enabled": "false",






584

    "ja4Enabled": "false",






585

    "firewallBypassIps": [],






586

    "managedRules": {






587

      "vercel_ruleset": {






588

        "active": "false",






589

        "action": "log"






590

      },






591

      "bot_filter": {






592

        "active": "false",






593

        "action": "log"






594

      },






595

      "ai_bots": {






596

        "active": "false",






597

        "action": "log"






598

      },






599

      "owasp": {






600

        "active": "false",






601

        "action": "log"






602

      }






603

    },






604

    "botIdEnabled": "false"






605

  },






606

  "oidcTokenConfig": {






607

    "enabled": "false",






608

    "issuerMode": "team"






609

  },






610

  "tier": "standard",






611

  "scheduledTierChange": {






612

    "tier": "standard",






613

    "effectiveAt": "123"






614

  },






615

  "usageStatus": {






616

    "kind": "flat",






617

    "exceededAllowanceUntil": "123",






618

    "bypassThrottleUntil": "123"






619

  },






620

  "features": {






621

    "webAnalytics": "false"






622

  },






623

  "v0": "false",






624

  "abuse": {






625

    "scanner": "string",






626

    "history": [






627

      {






628

        "scanner": "string",






629

        "reason": "Customer requested refund",






630

        "by": "string",






631

        "byId": "example_id",






632

        "at": "123"






633

      }






634

    ],






635

    "updatedAt": "123",






636

    "block": {






637

      "action": "blocked",






638

      "reason": "Customer requested refund",






639

      "statusCode": "123",






640

      "createdAt": "123",






641

      "caseId": "example_id",






642

      "actor": "string",






643

      "comment": "string",






644

      "ineligibleForAppeal": "false",






645

      "isCascading": "false"






646

    },






647

    "blockHistory": [






648

      {






649

        "action": "blocked",






650

        "reason": "Customer requested refund",






651

        "statusCode": "123",






652

        "createdAt": "123",






653

        "caseId": "example_id",






654

        "actor": "string",






655

        "comment": "string",






656

        "ineligibleForAppeal": "false",






657

        "isCascading": "false"






658

      }






659

    ],






660

    "interstitial": "false"






661

  },






662

  "internalRoutes": [






663

    {






664

      "src": "string",






665

      "status": "123"






666

    }






667

  ],






668

  "hasDeployments": "false",






669

  "dismissedToasts": [






670

    {






671

      "key": "string",






672

      "dismissedAt": "123",






673

      "action": "delete",






674

      "value": "string"






675

    }






676

  ],






677

  "protectedSourcemaps": "false"






678

}




```
