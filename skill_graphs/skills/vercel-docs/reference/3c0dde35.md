# Retrieve project domains by project by id or name
GET`https://api.vercel.com/v9/projects/{idOrName}/domains`
Retrieve the domains associated with a given project by passing either the project `id` or `name` in the URL.
TypeScriptNext.jscURL
https://api.vercel.com/v9/projects/{idOrName}/domains
```


1

const response = await fetch('https://api.vercel.com/v9/projects/idOrName/domains?production=value&target=string&customEnvironmentId=string&gitBranch=string&redirects=value&redirect=string&verified=value&limit=123&since=123&until=123&order=value&teamId=string&slug=string', {






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

  "domains": [






3

    {






4

      "name": "Example Name",






5

      "apexName": "Example Name",






6

      "projectId": "example_id",






7

      "redirect": "string",






8

      "redirectStatusCode": "301",






9

      "gitBranch": "string",






10

      "customEnvironmentId": "example_id",






11

      "updatedAt": "123",






12

      "createdAt": "123",






13

      "verified": "false",






14

      "verification": [






15

        {






16

          "type": "string",






17

          "domain": "string",






18

          "value": "string",






19

          "reason": "Customer requested refund"






20

        }






21

      ]






22

    }






23

  ],






24

  "pagination": {






25

    "count": "123",






26

    "next": "123",






27

    "prev": "123"






28

  }






29

}




```

##  [Authentication](https://vercel.com/docs/rest-api/projects/retrieve-project-domains-by-project-by-id-or-name#authentication)[](https://vercel.com/docs/rest-api/projects/retrieve-project-domains-by-project-by-id-or-name#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/projects/retrieve-project-domains-by-project-by-id-or-name#path-parameters)[](https://vercel.com/docs/rest-api/projects/retrieve-project-domains-by-project-by-id-or-name#path-parameters)
idOrNameanyRequired
The unique project identifier or the project name
##  [Query parameters](https://vercel.com/docs/rest-api/projects/retrieve-project-domains-by-project-by-id-or-name#query-parameters)[](https://vercel.com/docs/rest-api/projects/retrieve-project-domains-by-project-by-id-or-name#query-parameters)
productionanyOptional
Filters only production domains when set to `true`.
+Show 2 enum values
targetstringOptional
Filters on the target of the domain. Can be either "production", "preview"
+Show 2 enum values
customEnvironmentIdstringOptional
The unique custom environment identifier within the project
gitBranchstringOptional
Filters domains based on specific branch.
redirectsanyOptional
Excludes redirect project domains when "false". Includes redirect project domains when "true" (default).
+Show 2 enum values
redirectstringOptional
Filters domains based on their redirect target.
verifiedanyOptional
Filters domains based on their verification status.
+Show 2 enum values
limitnumberOptional
Maximum number of domains to list from a request (max 100).
sincenumberOptional
Get domains created after this JavaScript timestamp.
untilnumberOptional
Get domains created before this JavaScript timestamp.
orderanyOptional
Domains sort order by createdAt
+Show 2 enum values
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/projects/retrieve-project-domains-by-project-by-id-or-name#response)[](https://vercel.com/docs/rest-api/projects/retrieve-project-domains-by-project-by-id-or-name#response)
200Successful response retrieving a list of domains
domainsarrayRequired
+Show 11 properties
paginationobjectRequired
+Show 3 properties
##  [Errors](https://vercel.com/docs/rest-api/projects/retrieve-project-domains-by-project-by-id-or-name#errors)[](https://vercel.com/docs/rest-api/projects/retrieve-project-domains-by-project-by-id-or-name#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
TypeScriptNext.jscURL
https://api.vercel.com/v9/projects/{idOrName}/domains
```


1

const response = await fetch('https://api.vercel.com/v9/projects/idOrName/domains?production=value&target=string&customEnvironmentId=string&gitBranch=string&redirects=value&redirect=string&verified=value&limit=123&since=123&until=123&order=value&teamId=string&slug=string', {






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

  "domains": [






3

    {






4

      "name": "Example Name",






5

      "apexName": "Example Name",






6

      "projectId": "example_id",






7

      "redirect": "string",






8

      "redirectStatusCode": "301",






9

      "gitBranch": "string",






10

      "customEnvironmentId": "example_id",






11

      "updatedAt": "123",






12

      "createdAt": "123",






13

      "verified": "false",






14

      "verification": [






15

        {






16

          "type": "string",






17

          "domain": "string",






18

          "value": "string",






19

          "reason": "Customer requested refund"






20

        }






21

      ]






22

    }






23

  ],






24

  "pagination": {






25

    "count": "123",






26

    "next": "123",






27

    "prev": "123"






28

  }






29

}




```

Copy as MarkdownGive feedbackAsk AI about this page
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Add a domain to a project
