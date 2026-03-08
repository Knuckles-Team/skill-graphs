Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Creates an access group
# Creates an access group
POST`https://api.vercel.com/v1/access-groups`
Allows to create an access group
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

  const result = await vercel.accessGroups.createAccessGroup({






9

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






10

    slug: "my-team-url-slug",






11

    requestBody: {






12

      name: "My access group",






13

      projects: [






14

        {






15

          projectId: "prj_ndlgr43fadlPyCtREAqxxdyFK",






16

          role: "ADMIN",






17

        },






18

        {






19

          projectId: "prj_ndlgr43fadlPyCtREAqxxdyFK",






20

          role: "ADMIN",






21

        },






22

        {






23

          projectId: "prj_ndlgr43fadlPyCtREAqxxdyFK",






24

          role: "ADMIN",






25

        },






26

      ],






27

      membersToAdd: [






28

        "usr_1a2b3c4d5e6f7g8h9i0j",






29

        "usr_2b3c4d5e6f7g8h9i0j1k",






30

      ],






31

    },






32

  });






33







34

  console.log(result);






35

}






36







37

run();




```

Response
```


1

{






2

  "entitlements": [],






3

  "membersCount": "123",






4

  "projectsCount": "123",






5

  "name": "my-access-group",






6

  "createdAt": "1588720733602",






7

  "teamId": "team_123a6c5209bc3778245d011443644c8d27dc2c50",






8

  "updatedAt": "1588720733602",






9

  "accessGroupId": "ag_123a6c5209bc3778245d011443644c8d27dc2c50",






10

  "teamRoles": [],






11

  "teamPermissions": []






12

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/access-groups/creates-an-access-group#authentication)[](https://vercel.com/docs/rest-api/sdk/access-groups/creates-an-access-group#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/access-groups/creates-an-access-group#query-parameters)[](https://vercel.com/docs/rest-api/sdk/access-groups/creates-an-access-group#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/sdk/access-groups/creates-an-access-group#body)[](https://vercel.com/docs/rest-api/sdk/access-groups/creates-an-access-group#body)
application/json
namestringRequired
The name of the access group
projectsarrayOptional
+Show 2 properties
membersToAddarrayOptional
List of members to add to the access group.
##  [Response](https://vercel.com/docs/rest-api/sdk/access-groups/creates-an-access-group#response)[](https://vercel.com/docs/rest-api/sdk/access-groups/creates-an-access-group#response)
200Success
entitlementsarrayRequired
membersCountnumberRequired
projectsCountnumberRequired
namestringRequired
The name of this access group.
createdAtstringRequired
Timestamp in milliseconds when the access group was created.
teamIdstringRequired
ID of the team that this access group belongs to.
updatedAtstringRequired
Timestamp in milliseconds when the access group was last updated.
accessGroupIdstringRequired
ID of the access group.
teamRolesarrayOptional
Roles that the team has in the access group.
teamPermissionsarrayOptional
Permissions that the team has in the access group.
##  [Errors](https://vercel.com/docs/rest-api/sdk/access-groups/creates-an-access-group#errors)[](https://vercel.com/docs/rest-api/sdk/access-groups/creates-an-access-group#errors)
400One of the provided values in the request body is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
