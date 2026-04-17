# Reads an access group
GET`https://api.vercel.com/v1/access-groups/{idOrName}`
Allows to read an access group
TypeScriptNext.jscURL
https://api.vercel.com/v1/access-groups/{idOrName}
```


1

const response = await fetch('https://api.vercel.com/v1/access-groups/idOrName?teamId=string&slug=string', {






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

  "teamPermissions": [],






3

  "entitlements": [],






4

  "isDsyncManaged": "false",






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

  "membersCount": "5",






11

  "projectsCount": "2",






12

  "teamRoles": []






13

}




```
