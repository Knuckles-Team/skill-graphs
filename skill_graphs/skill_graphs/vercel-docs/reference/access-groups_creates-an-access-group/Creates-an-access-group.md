# Creates an access group
POST`https://api.vercel.com/v1/access-groups`
Allows to create an access group
TypeScriptNext.jscURL
https://api.vercel.com/v1/access-groups
```


1

const response = await fetch('https://api.vercel.com/v1/access-groups?teamId=string&slug=string', {






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

    "name": "My access group",






9

    "projects": [






10

      {






11

        "projectId": "prj_ndlgr43fadlPyCtREAqxxdyFK",






12

        "role": "ADMIN"






13

      }






14

    ],






15

    "membersToAdd": []






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
