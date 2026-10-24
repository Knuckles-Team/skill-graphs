# Get access request status
GET`https://api.vercel.com/v1/teams/{teamId}/request/{userId}`
Check the status of a join request. It'll respond with a 404 if the request has been declined. If no `userId` path segment was provided, this endpoint will instead return the status of the authenticated user.
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

  const result = await vercel.teams.getTeamAccessRequest({






9

    userId: "<id>",






10

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






11

  });






12







13

  console.log(result);






14

}






15







16

run();




```

Response
```


1

{






2

  "teamSlug": "my-team",






3

  "teamName": "My Team",






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

  "accessRequestedAt": "1588720733602",






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

##  [Authentication](https://vercel.com/docs/rest-api/sdk/teams/get-access-request-status#authentication)[](https://vercel.com/docs/rest-api/sdk/teams/get-access-request-status#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/teams/get-access-request-status#path-parameters)[](https://vercel.com/docs/rest-api/sdk/teams/get-access-request-status#path-parameters)
userIdstringRequired
teamIdstringRequired
##  [Response](https://vercel.com/docs/rest-api/sdk/teams/get-access-request-status#response)[](https://vercel.com/docs/rest-api/sdk/teams/get-access-request-status#response)
200Successfully
teamSlugstringRequired
The slug of the team.
teamNamestringRequired
The name of the team.
confirmedbooleanRequired
Current status of the membership. Will be `true` if confirmed, if pending it'll be `false`.
+Show 2 enum values
joinedFromobjectRequired
A map that describes the origin from where the user joined.
+Show 11 properties
accessRequestedAtnumberRequired
Timestamp in milliseconds when the user requested access to the team.
githubobjectRequired
Map of the connected GitHub account.
+Show 1 properties
gitlabobjectRequired
Map of the connected GitLab account.
+Show 1 properties
bitbucketobjectRequired
Map of the connected Bitbucket account.
+Show 1 properties
##  [Errors](https://vercel.com/docs/rest-api/sdk/teams/get-access-request-status#errors)[](https://vercel.com/docs/rest-api/sdk/teams/get-access-request-status#errors)
400One of the provided values in the request query is invalid. User is already a confirmed member of the team and did not request access. Only visible when the authenticated user does have access to the team.
401Error
403You do not have permission to access this resource.
404The provided user doesn't have a membership. Team was not found.
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

  const result = await vercel.teams.getTeamAccessRequest({






9

    userId: "<id>",






10

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






11

  });






12







13

  console.log(result);






14

}






15







16

run();




```

Response
```


1

{






2

  "teamSlug": "my-team",






3

  "teamName": "My Team",






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

  "accessRequestedAt": "1588720733602",






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
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Update a Team
