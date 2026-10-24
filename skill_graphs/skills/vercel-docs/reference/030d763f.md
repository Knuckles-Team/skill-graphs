# Request access to a team
POST`https://api.vercel.com/v1/teams/{teamId}/request`
Request access to a team as a member. An owner has to approve the request. Only 10 users can request access to a team at the same time.
TypeScriptNext.jscURL
https://api.vercel.com/v1/teams/{teamId}/request
```


1

const response = await fetch('https://api.vercel.com/v1/teams/teamId/request', {






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

    "joinedFrom": {






9

      "origin": "github",






10

      "commitId": "f498d25d8bd654b578716203be73084b31130cd7",






11

      "repoId": "67753070",






12

      "repoPath": "jane-doe/example",






13

      "gitUserId": "example_id",






14

      "gitUserLogin": "jane-doe"






15

    }






16

  }),






17

});






18







19

const data = await response.json();






20

console.log(data);




```

Response
```


1

{






2

  "teamSlug": "string",






3

  "teamName": "Example Name",






4

  "confirmed": "false",






5

  "joinedFrom": {






6

    "origin": "teams",






7

    "commitId": "example_id",






8

    "repoId": "example_id",






9

    "repoPath": "string",






10

    "gitUserId": "example_id",






11

    "gitUserLogin": "string",






12

    "ssoUserId": "example_id",






13

    "ssoConnectedAt": "123",






14

    "idpUserId": "example_id",






15

    "dsyncUserId": "example_id",






16

    "dsyncConnectedAt": "123"






17

  },






18

  "accessRequestedAt": "123",






19

  "github": {






20

    "login": "string"






21

  },






22

  "gitlab": {






23

    "login": "string"






24

  },






25

  "bitbucket": {






26

    "login": "string"






27

  }






28

}




```

##  [Authentication](https://vercel.com/docs/rest-api/teams/request-access-to-a-team#authentication)[](https://vercel.com/docs/rest-api/teams/request-access-to-a-team#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/teams/request-access-to-a-team#path-parameters)[](https://vercel.com/docs/rest-api/teams/request-access-to-a-team#path-parameters)
teamIdstringRequired
##  [Body](https://vercel.com/docs/rest-api/teams/request-access-to-a-team#body)[](https://vercel.com/docs/rest-api/teams/request-access-to-a-team#body)
application/json
joinedFromobjectRequired
+Show 6 properties
##  [Response](https://vercel.com/docs/rest-api/teams/request-access-to-a-team#response)[](https://vercel.com/docs/rest-api/teams/request-access-to-a-team#response)
200Successfuly requested access to the team.
teamSlugstringRequired
teamNamestringRequired
confirmedbooleanOptional
+Show 2 enum values
joinedFromobjectOptional
+Show 11 properties
accessRequestedAtnumberOptional
githubobjectRequired
+Show 1 properties
gitlabobjectRequired
+Show 1 properties
bitbucketobjectRequired
+Show 1 properties
##  [Errors](https://vercel.com/docs/rest-api/teams/request-access-to-a-team#errors)[](https://vercel.com/docs/rest-api/teams/request-access-to-a-team#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401Error
403You do not have permission to access this resource.
404The team was not found.
429Error
503Error
TypeScriptNext.jscURL
https://api.vercel.com/v1/teams/{teamId}/request
```


1

const response = await fetch('https://api.vercel.com/v1/teams/teamId/request', {






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

    "joinedFrom": {






9

      "origin": "github",






10

      "commitId": "f498d25d8bd654b578716203be73084b31130cd7",






11

      "repoId": "67753070",






12

      "repoPath": "jane-doe/example",






13

      "gitUserId": "example_id",






14

      "gitUserLogin": "jane-doe"






15

    }






16

  }),






17

});






18







19

const data = await response.json();






20

console.log(data);




```

Response
```


1

{






2

  "teamSlug": "string",






3

  "teamName": "Example Name",






4

  "confirmed": "false",






5

  "joinedFrom": {






6

    "origin": "teams",






7

    "commitId": "example_id",






8

    "repoId": "example_id",






9

    "repoPath": "string",






10

    "gitUserId": "example_id",






11

    "gitUserLogin": "string",






12

    "ssoUserId": "example_id",






13

    "ssoConnectedAt": "123",






14

    "idpUserId": "example_id",






15

    "dsyncUserId": "example_id",






16

    "dsyncConnectedAt": "123"






17

  },






18

  "accessRequestedAt": "123",






19

  "github": {






20

    "login": "string"






21

  },






22

  "gitlab": {






23

    "login": "string"






24

  },






25

  "bitbucket": {






26

    "login": "string"






27

  }






28

}




```

Copy as MarkdownGive feedbackAsk AI about this page
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Get a Team
