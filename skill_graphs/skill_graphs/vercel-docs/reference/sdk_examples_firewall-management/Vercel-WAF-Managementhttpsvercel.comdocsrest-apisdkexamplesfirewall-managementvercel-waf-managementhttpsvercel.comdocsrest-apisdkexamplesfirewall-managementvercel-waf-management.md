#  [Vercel WAF Management](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#vercel-waf-management)[](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#vercel-waf-management)
##  [Add custom rules](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#add-custom-rules)[](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#add-custom-rules)
In this example, you create a new custom rule to protect your application against SQL injection threats.
run.ts
```


1

import { Vercel } from '@vercel/sdk';






2







3

const vercel = new Vercel({






4

  bearerToken: process.env.VERCEL_TOKEN,






5

});






6







7

async function insertCustomRule() {






8

  await vercel.security.updateFirewallConfig({






9

    projectId: "your-project-id",






10

    teamId: "your-team-id",






11

    requestBody: {






12

      action: "rules.insert",






13

      id: null,






14

      value: {






15

        active: true,






16

        name: "Block SQL Injection Attempts",






17

        description: "Block requests with SQL injection patterns in query parameters",






18

        conditionGroup: [






19

          {






20

            conditions: [






21

              {






22

                op: "inc",






23

                type: "query",






24

                value: "SELECT",






25

              },






26

            ],






27

          },






28

        ],






29

        action: {






30

          mitigate: {






31

            action: "deny",






32

            rateLimit: null,






33

            redirect: null,






34

            actionDuration: null,






35

          },






36

        },






37

      },






38

    },






39

  });






40

}






41







42

insertCustomRule();




```

##  [Modify existing rules](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#modify-existing-rules)[](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#modify-existing-rules)
In this example, you update an existing custom rule's configuration. This is useful when you need to programmatically adjust conditions, actions, or status of an existing rule.
run.ts
```


1

import { Vercel } from "@vercel/sdk";






2







3

const vercel = new Vercel({






4

  bearerToken: process.env.VERCEL_TOKEN,






5

});






6







7

async function updateExistingRule() {






8

  await vercel.security.updateFirewallConfig({






9

    projectId: "your-project-id",






10

    teamId: "your-team-id",






11

    requestBody: {






12

      action: "rules.update",






13

      id: "existing-rule-id",






14

      value: {






15

        active: true,






16

        name: "Updated Rule Name",






17

        description: "Updated rule description",






18

        conditionGroup: [






19

          {






20

            conditions: [






21

              {






22

                op: "pre",






23

                type: "path",






24

                value: "/admin",






25

              },






26

            ],






27

          },






28

        ],






29

        action: {






30

          mitigate: {






31

            action: "challenge",






32

            rateLimit: null,






33

            redirect: null,






34

            actionDuration: null,






35

          },






36

        },






37

      },






38

    },






39

  });






40

}






41







42

updateExistingRule();




```

##  [Delete custom rules](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#delete-custom-rules)[](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#delete-custom-rules)
In this example, you delete an existing custom rule.
run.ts
```


1

import { Vercel } from "@vercel/sdk";






2







3

const vercel = new Vercel({






4

  bearerToken: process.env.VERCEL_TOKEN,






5

});






6







7

async function deleteRule() {






8

  await vercel.security.updateFirewallConfig({






9

    projectId: "your-project-id",






10

    teamId: "your-team-id",






11

    requestBody: {






12

      action: "rules.remove",






13

      id: "rule-to-delete-id",






14

      value: null,






15

    },






16

  });






17

}






18







19

deleteRule();




```

##  [Change rule priority](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#change-rule-priority)[](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#change-rule-priority)
This applies when you have more than one custom rule. By default, priority is determined by the order rules are added. You can change this in the dashboard or with the SDK.
run.ts
```


1

import { Vercel } from "@vercel/sdk";






2







3

const vercel = new Vercel({






4

  bearerToken: process.env.VERCEL_TOKEN,






5

});






6







7

async function reorderRules() {






8

  await vercel.security.updateFirewallConfig({






9

    projectId: "your-project-id",






10

    teamId: "your-team-id",






11

    requestBody: {






12

      action: "rules.priority",






13

      id: "rule-to-update-priority-id",






14

      value: 1,






15

    },






16

  });






17

}






18







19

reorderRules();




```

##  [Custom system bypass rule](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#custom-system-bypass-rule)[](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#custom-system-bypass-rule)
WAF system bypass rules allow specific IP addresses or CIDRs to bypass system-level mitigations such as DDoS Mitigation. For more complex filters, you can use the REST API directly. This example creates a custom rule to allow mobile applications to bypass system-level mitigations.
Bypassing system-level mitigations with the API is currently in beta. Contact support if you would like to use it.
run.ts
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

  const result = await vercel.security.updateFirewallConfig({






9

    projectId: "<your_project_id>",






10

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






11

    requestBody: {






12

      action: "rules.insert",






13

      id: null,






14

      value: {






15

        name: "Mobile App Bypass Security Rule",






16

        description: "Custom system bypass rule targeting mobile applications",






17

        active: true,






18

        conditionGroup: [






19

          {






20

            conditions: [






21

              {






22

                type: "user_agent",






23

                op: "re",






24

                neg: false,






25

                value: "Mobile|Android|iPhone|iPad"






26

              }






27

            ]






28

          }






29

        ],






30

        action: {






31

          mitigate: {






32

            action: "bypass",






33

            bypassSystem: true






34

          }






35

        }






36

      }






37

    },






38

  });






39







40

  console.log(result);






41

}






42







43

run();




```

##  [Update an OWASP rule](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#update-an-owasp-rule)[](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#update-an-owasp-rule)
In this example, you update a specific rule from the OWASP ruleset in your project using crs.update. You specify the rule to update by using its name in the id field.
run.ts
```


1

import { Vercel } from "@vercel/sdk";






2







3

const vercel = new Vercel({






4

  bearerToken: process.env.VERCEL_TOKEN,






5

});






6







7

async function updateOwaspRule() {






8

  await vercel.security.updateFirewallConfig({






9

    projectId: "your-project-id",






10

    teamId: "your-team-id",






11

    requestBody: {






12

      action: "crs.update",






13

      id: "xss", // eg. "sd", "max", "lfi", "rfi", "rce", "php", "gen", "xss", "sqli", "sf", "java"






14

      value: {






15

        active: true,






16

        action: "log", // e.g. "deny" | "log"






17

      },






18

    },






19

  });






20

}






21







22

updateOwaspRule();




```

##  [Disable all OWASP rules](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#disable-all-owasp-rules)[](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#disable-all-owasp-rules)
This example disables all OWASP rules for the project. It is a shortcut equivalent to setting every OWASP rule to active = false.
run.ts
```


1

import { Vercel } from "@vercel/sdk";






2







3

const vercel = new Vercel({






4

  bearerToken: process.env.VERCEL_TOKEN,






5

});






6







7

async function disableOWASPRules() {






8

  await vercel.security.updateFirewallConfig({






9

    projectId: "your-project-id",






10

    teamId: "your-team-id",






11

    requestBody: {






12

      action: "crs.disable",






13

      id: null,






14

      value: null,






15

    },






16

  });






17

}






18







19

disableOWASPRules();




```

##  [Update a managed ruleset](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#update-a-managed-ruleset)[](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#update-a-managed-ruleset)
Use managedRules.update with the ruleset name as id to enable/disable the ruleset and update the firewall action for that managed ruleset for the project.
run.ts
```


1

import { Vercel } from "@vercel/sdk";






2







3

const vercel = new Vercel({






4

  bearerToken: process.env.VERCEL_TOKEN,






5

});






6







7

async function updateManagedRuleset() {






8

  await vercel.security.updateFirewallConfig({






9

    projectId: "your-project-id",






10

    teamId: "your-team-id",






11

    requestBody: {






12

      action: "managedRules.update",






13

      id: "bot_protection", // eg. "owasp", "bot_protection", "ai_bots", "bot_filter"






14

      value: {






15

        active: true,






16

        action: "log", // e.g. "deny" | "log" | "challenge"






17

      },






18

    },






19

  });






20

}






21







22

updateManagedRuleset();




```

On this page
  * [Add custom rules](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#add-custom-rules)
  * [Modify existing rules](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#modify-existing-rules)
  * [Delete custom rules](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#delete-custom-rules)
  * [Change rule priority](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#change-rule-priority)
  * [Custom system bypass rule](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#custom-system-bypass-rule)
  * [Update an OWASP rule](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#update-an-owasp-rule)
  * [Disable all OWASP rules](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#disable-all-owasp-rules)
  * [Update a managed ruleset](https://vercel.com/docs/rest-api/sdk/examples/firewall-management#update-a-managed-ruleset)


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
