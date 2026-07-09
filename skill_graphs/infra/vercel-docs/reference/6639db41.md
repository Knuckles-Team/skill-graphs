# Add a routing rule
POST`https://api.vercel.com/v1/projects/{projectId}/routes`
Add a single routing rule to a project at a specified position. Defaults to the end of the list if no position is provided. The route is enabled by default. Stages a new version with the added route.
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

  const result = await vercel.projectRoutes.addRoute({






9

    projectId: "<id>",






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

  "route": {






3

    "routeType": "rewrite",






4

    "id": "icfg_1234567890",






5

    "name": "Example Name",






6

    "description": "string",






7

    "enabled": "false",






8

    "staged": "false",






9

    "route": {






10

      "src": "string",






11

      "dest": "string",






12

      "headers": "value",






13

      "methods": [],






14

      "continue": "false",






15

      "override": "false",






16

      "caseSensitive": "false",






17

      "check": "false",






18

      "important": "false",






19

      "status": "123",






20

      "has": [






21

        {






22

          "type": "host",






23

          "value": "string"






24

        }






25

      ],






26

      "missing": [






27

        {






28

          "type": "host",






29

          "value": "string"






30

        }






31

      ],






32

      "mitigate": {






33

        "action": "challenge"






34

      },






35

      "transforms": [






36

        {






37

          "type": "request.headers",






38

          "op": "append",






39

          "target": {






40

            "key": "string"






41

          },






42

          "args": "string",






43

          "env": []






44

        }






45

      ],






46

      "env": [],






47

      "locale": {






48

        "redirect": "value",






49

        "cookie": "string"






50

      },






51

      "source": "string",






52

      "destination": "string",






53

      "statusCode": "123",






54

      "middlewarePath": "example_id",






55

      "middlewareRawSrc": [],






56

      "middleware": "123",






57

      "respectOriginCacheControl": "false"






58

    },






59

    "rawSrc": "string",






60

    "rawDest": "string",






61

    "srcSyntax": "equals"






62

  },






63

  "version": {






64

    "id": "icfg_1234567890",






65

    "s3Key": "string",






66

    "lastModified": "123",






67

    "createdBy": "string",






68

    "isStaging": "false",






69

    "isLive": "false",






70

    "ruleCount": "123",






71

    "alias": "string"






72

  }






73

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/project-routes/add-a-routing-rule#authentication)[](https://vercel.com/docs/rest-api/sdk/project-routes/add-a-routing-rule#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/project-routes/add-a-routing-rule#path-parameters)[](https://vercel.com/docs/rest-api/sdk/project-routes/add-a-routing-rule#path-parameters)
projectIdstringRequired
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/project-routes/add-a-routing-rule#query-parameters)[](https://vercel.com/docs/rest-api/sdk/project-routes/add-a-routing-rule#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/sdk/project-routes/add-a-routing-rule#body)[](https://vercel.com/docs/rest-api/sdk/project-routes/add-a-routing-rule#body)
application/json
routeobjectRequired
+Show 5 properties
positionobjectOptional
Controls where the route is inserted. Defaults to "end" if omitted.
+Show 2 properties
##  [Response](https://vercel.com/docs/rest-api/sdk/project-routes/add-a-routing-rule#response)[](https://vercel.com/docs/rest-api/sdk/project-routes/add-a-routing-rule#response)
200Success
routeobjectRequired
+Show 10 properties
versionobjectRequired
A version of routing rules stored in S3.
+Show 8 properties
##  [Errors](https://vercel.com/docs/rest-api/sdk/project-routes/add-a-routing-rule#errors)[](https://vercel.com/docs/rest-api/sdk/project-routes/add-a-routing-rule#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
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

  const result = await vercel.projectRoutes.addRoute({






9

    projectId: "<id>",






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

  "route": {






3

    "routeType": "rewrite",






4

    "id": "icfg_1234567890",






5

    "name": "Example Name",






6

    "description": "string",






7

    "enabled": "false",






8

    "staged": "false",






9

    "route": {






10

      "src": "string",






11

      "dest": "string",






12

      "headers": "value",






13

      "methods": [],






14

      "continue": "false",






15

      "override": "false",






16

      "caseSensitive": "false",






17

      "check": "false",






18

      "important": "false",






19

      "status": "123",






20

      "has": [






21

        {






22

          "type": "host",






23

          "value": "string"






24

        }






25

      ],






26

      "missing": [






27

        {






28

          "type": "host",






29

          "value": "string"






30

        }






31

      ],






32

      "mitigate": {






33

        "action": "challenge"






34

      },






35

      "transforms": [






36

        {






37

          "type": "request.headers",






38

          "op": "append",






39

          "target": {






40

            "key": "string"






41

          },






42

          "args": "string",






43

          "env": []






44

        }






45

      ],






46

      "env": [],






47

      "locale": {






48

        "redirect": "value",






49

        "cookie": "string"






50

      },






51

      "source": "string",






52

      "destination": "string",






53

      "statusCode": "123",






54

      "middlewarePath": "example_id",






55

      "middlewareRawSrc": [],






56

      "middleware": "123",






57

      "respectOriginCacheControl": "false"






58

    },






59

    "rawSrc": "string",






60

    "rawDest": "string",






61

    "srcSyntax": "equals"






62

  },






63

  "version": {






64

    "id": "icfg_1234567890",






65

    "s3Key": "string",






66

    "lastModified": "123",






67

    "createdBy": "string",






68

    "isStaging": "false",






69

    "isLive": "false",






70

    "ruleCount": "123",






71

    "alias": "string"






72

  }






73

}




```

Copy as MarkdownGive feedbackAsk AI about this page
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Get routing rule version history
