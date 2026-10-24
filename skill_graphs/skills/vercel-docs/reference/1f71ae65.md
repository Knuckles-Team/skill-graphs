# Read Firewall Configuration
GET`https://api.vercel.com/v1/security/firewall/config/{configVersion}`
Retrieve the specified firewall configuration for a project. The deployed configVersion will be `active`
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

  const result = await vercel.security.getFirewallConfig({






9

    projectId: "<id>",






10

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






11

    slug: "my-team-url-slug",






12

    configVersion: "<value>",






13

  });






14







15

  console.log(result);






16

}






17







18

run();




```

Response
```


1

{






2

  "ownerId": "example_id",






3

  "projectKey": "string",






4

  "id": "icfg_1234567890",






5

  "version": "123",






6

  "updatedAt": "string",






7

  "firewallEnabled": "false",






8

  "crs": {






9

    "sd": {






10

      "active": "false",






11

      "action": "deny"






12

    },






13

    "ma": {






14

      "active": "false",






15

      "action": "deny"






16

    },






17

    "lfi": {






18

      "active": "false",






19

      "action": "deny"






20

    },






21

    "rfi": {






22

      "active": "false",






23

      "action": "deny"






24

    },






25

    "rce": {






26

      "active": "false",






27

      "action": "deny"






28

    },






29

    "php": {






30

      "active": "false",






31

      "action": "deny"






32

    },






33

    "gen": {






34

      "active": "false",






35

      "action": "deny"






36

    },






37

    "xss": {






38

      "active": "false",






39

      "action": "deny"






40

    },






41

    "sqli": {






42

      "active": "false",






43

      "action": "deny"






44

    },






45

    "sf": {






46

      "active": "false",






47

      "action": "deny"






48

    },






49

    "java": {






50

      "active": "false",






51

      "action": "deny"






52

    }






53

  },






54

  "rules": [






55

    {






56

      "id": "icfg_1234567890",






57

      "name": "Example Name",






58

      "description": "string",






59

      "active": "false",






60

      "conditionGroup": [






61

        {






62

          "conditions": [






63

            {






64

              "type": "host",






65

              "op": "sub",






66

              "neg": "false",






67

              "key": "string",






68

              "value": "string"






69

            }






70

          ]






71

        }






72

      ],






73

      "action": {






74

        "mitigate": {






75

          "action": "deny",






76

          "rateLimit": {






77

            "algo": "fixed_window",






78

            "window": "123",






79

            "limit": "123",






80

            "keys": [],






81

            "action": "deny"






82

          },






83

          "redirect": {






84

            "location": "string",






85

            "permanent": "false"






86

          },






87

          "actionDuration": "string",






88

          "bypassSystem": "false",






89

          "logHeaders": []






90

        }






91

      },






92

      "valid": "true",






93

      "validationErrors": "value"






94

    }






95

  ],






96

  "ips": [






97

    {






98

      "id": "icfg_1234567890",






99

      "hostname": "Example Name",






100

      "ip": "string",






101

      "notes": "string",






102

      "action": "deny"






103

    }






104

  ],






105

  "changes": [






106

    "value"






107

  ],






108

  "managedRules": {






109

    "bot_protection": {






110

      "active": "false",






111

      "action": "deny",






112

      "updatedAt": "string",






113

      "userId": "example_id",






114

      "username": "string"






115

    },






116

    "ai_bots": {






117

      "active": "false",






118

      "action": "deny",






119

      "updatedAt": "string",






120

      "userId": "example_id",






121

      "username": "string"






122

    },






123

    "owasp": {






124

      "active": "false",






125

      "action": "deny",






126

      "updatedAt": "string",






127

      "userId": "example_id",






128

      "username": "string"






129

    },






130

    "vercel_ruleset": {






131

      "active": "false",






132

      "action": "deny",






133

      "updatedAt": "string",






134

      "userId": "example_id",






135

      "username": "string"






136

    }






137

  },






138

  "botIdEnabled": "false"






139

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/security/read-firewall-configuration#authentication)[](https://vercel.com/docs/rest-api/sdk/security/read-firewall-configuration#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/security/read-firewall-configuration#path-parameters)[](https://vercel.com/docs/rest-api/sdk/security/read-firewall-configuration#path-parameters)
configVersionstringRequired
The deployed configVersion for the firewall configuration
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/security/read-firewall-configuration#query-parameters)[](https://vercel.com/docs/rest-api/sdk/security/read-firewall-configuration#query-parameters)
projectIdstringRequired
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/security/read-firewall-configuration#response)[](https://vercel.com/docs/rest-api/sdk/security/read-firewall-configuration#response)
200If the firewall configuration includes a [custom managed ruleset](https://vercel.com/docs/security/vercel-waf/managed-rulesets), it will include a `crs` item that has the following values: sd: Scanner Detection ma: Multipart Attack lfi: Local File Inclusion Attack rfi: Remote File Inclusion Attack rce: Remote Execution Attack php: PHP Attack gen: Generic Attack xss: XSS Attack sqli: SQL Injection Attack sf: Session Fixation Attack java: Java Attack
ownerIdstringRequired
projectKeystringRequired
idstringRequired
versionnumberRequired
updatedAtstringRequired
firewallEnabledbooleanRequired
+Show 2 enum values
crsobjectRequired
Custom Ruleset
+Show 11 properties
rulesarrayRequired
+Show 8 properties
ipsarrayRequired
+Show 5 properties
changesarrayRequired
managedRulesobjectOptional
+Show 4 properties
botIdEnabledbooleanOptional
+Show 2 enum values
##  [Errors](https://vercel.com/docs/rest-api/sdk/security/read-firewall-configuration#errors)[](https://vercel.com/docs/rest-api/sdk/security/read-firewall-configuration#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
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

  const result = await vercel.security.getFirewallConfig({






9

    projectId: "<id>",






10

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






11

    slug: "my-team-url-slug",






12

    configVersion: "<value>",






13

  });






14







15

  console.log(result);






16

}






17







18

run();




```

Response
```


1

{






2

  "ownerId": "example_id",






3

  "projectKey": "string",






4

  "id": "icfg_1234567890",






5

  "version": "123",






6

  "updatedAt": "string",






7

  "firewallEnabled": "false",






8

  "crs": {






9

    "sd": {






10

      "active": "false",






11

      "action": "deny"






12

    },






13

    "ma": {






14

      "active": "false",






15

      "action": "deny"






16

    },






17

    "lfi": {






18

      "active": "false",






19

      "action": "deny"






20

    },






21

    "rfi": {






22

      "active": "false",






23

      "action": "deny"






24

    },






25

    "rce": {






26

      "active": "false",






27

      "action": "deny"






28

    },






29

    "php": {






30

      "active": "false",






31

      "action": "deny"






32

    },






33

    "gen": {






34

      "active": "false",






35

      "action": "deny"






36

    },






37

    "xss": {






38

      "active": "false",






39

      "action": "deny"






40

    },






41

    "sqli": {






42

      "active": "false",






43

      "action": "deny"






44

    },






45

    "sf": {






46

      "active": "false",






47

      "action": "deny"






48

    },






49

    "java": {






50

      "active": "false",






51

      "action": "deny"






52

    }






53

  },






54

  "rules": [






55

    {






56

      "id": "icfg_1234567890",






57

      "name": "Example Name",






58

      "description": "string",






59

      "active": "false",






60

      "conditionGroup": [






61

        {






62

          "conditions": [






63

            {






64

              "type": "host",






65

              "op": "sub",






66

              "neg": "false",






67

              "key": "string",






68

              "value": "string"






69

            }






70

          ]






71

        }






72

      ],






73

      "action": {






74

        "mitigate": {






75

          "action": "deny",






76

          "rateLimit": {






77

            "algo": "fixed_window",






78

            "window": "123",






79

            "limit": "123",






80

            "keys": [],






81

            "action": "deny"






82

          },






83

          "redirect": {






84

            "location": "string",






85

            "permanent": "false"






86

          },






87

          "actionDuration": "string",






88

          "bypassSystem": "false",






89

          "logHeaders": []






90

        }






91

      },






92

      "valid": "true",






93

      "validationErrors": "value"






94

    }






95

  ],






96

  "ips": [






97

    {






98

      "id": "icfg_1234567890",






99

      "hostname": "Example Name",






100

      "ip": "string",






101

      "notes": "string",






102

      "action": "deny"






103

    }






104

  ],






105

  "changes": [






106

    "value"






107

  ],






108

  "managedRules": {






109

    "bot_protection": {






110

      "active": "false",






111

      "action": "deny",






112

      "updatedAt": "string",






113

      "userId": "example_id",






114

      "username": "string"






115

    },






116

    "ai_bots": {






117

      "active": "false",






118

      "action": "deny",






119

      "updatedAt": "string",






120

      "userId": "example_id",






121

      "username": "string"






122

    },






123

    "owasp": {






124

      "active": "false",






125

      "action": "deny",






126

      "updatedAt": "string",






127

      "userId": "example_id",






128

      "username": "string"






129

    },






130

    "vercel_ruleset": {






131

      "active": "false",






132

      "action": "deny",






133

      "updatedAt": "string",






134

      "userId": "example_id",






135

      "username": "string"






136

    }






137

  },






138

  "botIdEnabled": "false"






139

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
