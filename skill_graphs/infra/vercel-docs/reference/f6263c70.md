# Update a Team Member
PATCH`https://api.vercel.com/v1/teams/{teamId}/members/{uid}`
Update the membership of a Team Member on the Team specified by `teamId`, such as changing the _role_ of the member, or confirming a request to join the Team for an unconfirmed member. The authenticated user must be an `OWNER` of the Team.
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

  const result = await vercel.teams.updateTeamMember({






9

    uid: "ndfasllgPyCtREAqxxdyFKb",






10

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






11

    requestBody: {






12

      confirmed: true,






13

      role: "VIEWER",






14

      projects: [






15

        {






16

          projectId: "prj_ndlgr43fadlPyCtREAqxxdyFK",






17

          role: "ADMIN",






18

        },






19

        {






20

          projectId: "prj_ndlgr43fadlPyCtREAqxxdyFK",






21

          role: "ADMIN",






22

        },






23

        {






24

          projectId: "prj_ndlgr43fadlPyCtREAqxxdyFK",






25

          role: "ADMIN",






26

        },






27

      ],






28

    },






29

  });






30







31

  console.log(result);






32

}






33







34

run();




```

Response
```


1

{






2

  "id": "icfg_1234567890"






3

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/teams/list-team-members#authentication)[](https://vercel.com/docs/rest-api/sdk/teams/list-team-members#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/teams/list-team-members#path-parameters)[](https://vercel.com/docs/rest-api/sdk/teams/list-team-members#path-parameters)
uidstringRequired
The ID of the member.
teamIdstringRequired
##  [Body](https://vercel.com/docs/rest-api/sdk/teams/list-team-members#body)[](https://vercel.com/docs/rest-api/sdk/teams/list-team-members#body)
application/json
confirmedbooleanOptional
Accept a user who requested access to the team.
+Show 1 enum values
rolestringOptional
The role in the team of the member.
projectsarrayOptional
+Show 2 properties
joinedFromobjectOptional
+Show 1 properties
##  [Response](https://vercel.com/docs/rest-api/sdk/teams/list-team-members#response)[](https://vercel.com/docs/rest-api/sdk/teams/list-team-members#response)
200Successfully updated the membership.
idstringRequired
ID of the team.
##  [Errors](https://vercel.com/docs/rest-api/sdk/teams/list-team-members#errors)[](https://vercel.com/docs/rest-api/sdk/teams/list-team-members#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid. Cannot disconnect SSO from a Team member that does not have a SSO connection. Cannot confirm a member that is already confirmed. Cannot confirm a member that did not request access.
401The request is not authorized. Team members can only be updated by an owner, or by the authenticated user if they are only disconnecting their SAML connection to the Team.
402Error
403You do not have permission to access this resource.
404The provided user is not part of this team. A user with the specified ID does not exist.
409Error
500Error
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

  const result = await vercel.teams.updateTeamMember({






9

    uid: "ndfasllgPyCtREAqxxdyFKb",






10

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






11

    requestBody: {






12

      confirmed: true,






13

      role: "VIEWER",






14

      projects: [






15

        {






16

          projectId: "prj_ndlgr43fadlPyCtREAqxxdyFK",






17

          role: "ADMIN",






18

        },






19

        {






20

          projectId: "prj_ndlgr43fadlPyCtREAqxxdyFK",






21

          role: "ADMIN",






22

        },






23

        {






24

          projectId: "prj_ndlgr43fadlPyCtREAqxxdyFK",






25

          role: "ADMIN",






26

        },






27

      ],






28

    },






29

  });






30







31

  console.log(result);






32

}






33







34

run();




```

Response
```


1

{






2

  "id": "icfg_1234567890"






3

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
