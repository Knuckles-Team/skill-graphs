# List team members
GET`https://api.vercel.com/v3/teams/{teamId}/members`
Get a paginated list of team members for the provided team.
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

  const result = await vercel.teams.getTeamMembers({






9

    limit: 20,






10

    since: 1540095775951,






11

    until: 1540095775951,






12

    role: "OWNER",






13

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






14

    slug: "my-team-url-slug",






15

  });






16







17

  console.log(result);






18

}






19







20

run();




```

Response
```


1

{






2

  "members": [






3

    {






4

      "avatar": "123a6c5209bc3778245d011443644c8d27dc2c50",






5

      "confirmed": "true",






6

      "email": "jane.doe@example.com",






7

      "github": {






8

        "login": "string"






9

      },






10

      "gitlab": {






11

        "login": "string"






12

      },






13

      "bitbucket": {






14

        "login": "string"






15

      },






16

      "role": "OWNER",






17

      "uid": "zTuNVUXEAvvnNN3IaqinkyMw",






18

      "username": "jane-doe",






19

      "name": "Jane Doe",






20

      "createdAt": "1588720733602",






21

      "accessRequestedAt": "1588820733602",






22

      "joinedFrom": {






23

        "origin": "teams",






24

        "commitId": "example_id",






25

        "repoId": "example_id",






26

        "repoPath": "string",






27

        "gitUserId": "example_id",






28

        "gitUserLogin": "string",






29

        "ssoUserId": "example_id",






30

        "ssoConnectedAt": "123",






31

        "idpUserId": "example_id",






32

        "dsyncUserId": "example_id",






33

        "dsyncConnectedAt": "123"






34

      },






35

      "projects": [






36

        {






37

          "name": "Example Name",






38

          "id": "icfg_1234567890",






39

          "role": "ADMIN"






40

        }






41

      ],






42

      "isEnterpriseManaged": "false"






43

    }






44

  ],






45

  "emailInviteCodes": [






46

    {






47

      "accessGroups": [],






48

      "id": "icfg_1234567890",






49

      "email": "user@example.com",






50

      "role": "OWNER",






51

      "teamRoles": [],






52

      "teamPermissions": [],






53

      "isDSyncUser": "false",






54

      "createdAt": "123",






55

      "expired": "true",






56

      "projects": "value",






57

      "entitlements": []






58

    }






59

  ],






60

  "pagination": {






61

    "hasNext": "false",






62

    "count": "20",






63

    "next": "1540095775951",






64

    "prev": "1540095775951"






65

  }






66

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/teams/list-team-members#authentication)[](https://vercel.com/docs/rest-api/sdk/teams/list-team-members#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/teams/list-team-members#path-parameters)[](https://vercel.com/docs/rest-api/sdk/teams/list-team-members#path-parameters)
teamIdstringRequired
The Team identifier to perform the request on behalf of.
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/teams/list-team-members#query-parameters)[](https://vercel.com/docs/rest-api/sdk/teams/list-team-members#query-parameters)
limitnumberOptional
Limit how many teams should be returned
sincenumberOptional
Timestamp in milliseconds to only include members added since then.
untilnumberOptional
Timestamp in milliseconds to only include members added until then.
searchstringOptional
Search team members by their name, username, and email.
rolestringOptional
Only return members with the specified team role.
+Show 8 enum values
excludeProjectstringOptional
Exclude members who belong to the specified project.
eligibleMembersForProjectIdstringOptional
Include team members who are eligible to be members of the specified project.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/teams/list-team-members#response)[](https://vercel.com/docs/rest-api/sdk/teams/list-team-members#response)
200Success
membersarrayRequired
+Show 15 properties
emailInviteCodesarrayOptional
+Show 11 properties
paginationobjectRequired
+Show 4 properties
##  [Errors](https://vercel.com/docs/rest-api/sdk/teams/list-team-members#errors)[](https://vercel.com/docs/rest-api/sdk/teams/list-team-members#errors)
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

  const result = await vercel.teams.getTeamMembers({






9

    limit: 20,






10

    since: 1540095775951,






11

    until: 1540095775951,






12

    role: "OWNER",






13

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






14

    slug: "my-team-url-slug",






15

  });






16







17

  console.log(result);






18

}






19







20

run();




```

Response
```


1

{






2

  "members": [






3

    {






4

      "avatar": "123a6c5209bc3778245d011443644c8d27dc2c50",






5

      "confirmed": "true",






6

      "email": "jane.doe@example.com",






7

      "github": {






8

        "login": "string"






9

      },






10

      "gitlab": {






11

        "login": "string"






12

      },






13

      "bitbucket": {






14

        "login": "string"






15

      },






16

      "role": "OWNER",






17

      "uid": "zTuNVUXEAvvnNN3IaqinkyMw",






18

      "username": "jane-doe",






19

      "name": "Jane Doe",






20

      "createdAt": "1588720733602",






21

      "accessRequestedAt": "1588820733602",






22

      "joinedFrom": {






23

        "origin": "teams",






24

        "commitId": "example_id",






25

        "repoId": "example_id",






26

        "repoPath": "string",






27

        "gitUserId": "example_id",






28

        "gitUserLogin": "string",






29

        "ssoUserId": "example_id",






30

        "ssoConnectedAt": "123",






31

        "idpUserId": "example_id",






32

        "dsyncUserId": "example_id",






33

        "dsyncConnectedAt": "123"






34

      },






35

      "projects": [






36

        {






37

          "name": "Example Name",






38

          "id": "icfg_1234567890",






39

          "role": "ADMIN"






40

        }






41

      ],






42

      "isEnterpriseManaged": "false"






43

    }






44

  ],






45

  "emailInviteCodes": [






46

    {






47

      "accessGroups": [],






48

      "id": "icfg_1234567890",






49

      "email": "user@example.com",






50

      "role": "OWNER",






51

      "teamRoles": [],






52

      "teamPermissions": [],






53

      "isDSyncUser": "false",






54

      "createdAt": "123",






55

      "expired": "true",






56

      "projects": "value",






57

      "entitlements": []






58

    }






59

  ],






60

  "pagination": {






61

    "hasNext": "false",






62

    "count": "20",






63

    "next": "1540095775951",






64

    "prev": "1540095775951"






65

  }






66

}




```

Copy as MarkdownGive feedbackAsk AI about this page
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Update a Team Member
