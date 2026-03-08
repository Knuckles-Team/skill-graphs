Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Get a Domain's configuration
# Get a Domain's configuration
GET`https://api.vercel.com/v6/domains/{domain}/config`
Get a Domain's configuration.
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

  const result = await vercel.domains.getDomainConfig({






9

    domain: "example.com",






10

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






11

    slug: "my-team-url-slug",






12

  });






13







14

  console.log(result);






15

}






16







17

run();




```

Response
```


1

{






2

  "configuredBy": "A",






3

  "acceptedChallenges": [],






4

  "recommendedIPv4": [






5

    {






6

      "rank": "123",






7

      "value": []






8

    }






9

  ],






10

  "recommendedCNAME": [






11

    {






12

      "rank": "123",






13

      "value": "string"






14

    }






15

  ],






16

  "misconfigured": "false"






17

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/domains/get-a-domain-s-configuration#authentication)[](https://vercel.com/docs/rest-api/sdk/domains/get-a-domain-s-configuration#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/domains/get-a-domain-s-configuration#path-parameters)[](https://vercel.com/docs/rest-api/sdk/domains/get-a-domain-s-configuration#path-parameters)
domainstringRequired
The name of the domain.
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/domains/get-a-domain-s-configuration#query-parameters)[](https://vercel.com/docs/rest-api/sdk/domains/get-a-domain-s-configuration#query-parameters)
projectIdOrNamestringOptional
The project id or name that will be associated with the domain. Use this when the domain is not yet associated with a project.
strictanyOptional
When true, the response will only include the nameservers assigned directly to the specified domain. When false and there are no nameservers assigned directly to the specified domain, the response will include the nameservers of the domain's parent zone.
+Show 2 enum values
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/domains/get-a-domain-s-configuration#response)[](https://vercel.com/docs/rest-api/sdk/domains/get-a-domain-s-configuration#response)
200Success
configuredBystringRequired
How we see the domain's configuration. - `CNAME`: Domain has a CNAME pointing to Vercel. - `A`: Domain's A record is resolving to Vercel. - `http`: Domain is resolving to Vercel but may be behind a Proxy. - `dns-01`: Domain is not resolving to Vercel but dns-01 challenge is enabled. - `null`: Domain is not resolving to Vercel.
+Show 4 enum values
acceptedChallengesarrayRequired
Which challenge types the domain can use for issuing certs.
recommendedIPv4arrayRequired
Recommended IPv4s for the domain. rank=1 is the preferred value(s) to use. Only using 1 ip value is acceptable.
+Show 2 properties
recommendedCNAMEarrayRequired
Recommended CNAMEs for the domain. rank=1 is the preferred value to use.
+Show 2 properties
misconfiguredbooleanRequired
Whether or not the domain is configured AND we can automatically generate a TLS certificate.
+Show 2 enum values
##  [Errors](https://vercel.com/docs/rest-api/sdk/domains/get-a-domain-s-configuration#errors)[](https://vercel.com/docs/rest-api/sdk/domains/get-a-domain-s-configuration#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
