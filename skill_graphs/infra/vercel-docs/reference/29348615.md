# Create a check
POST`https://api.vercel.com/v2/projects/{projectIdOrName}/checks`
Creates a new check for a project.
TypeScriptNext.jscURL
https://api.vercel.com/v2/projects/{projectIdOrName}/checks
```


1

const response = await fetch('https://api.vercel.com/v2/projects/projectIdOrName/checks?teamId=string&slug=string', {






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

    "name": "Example Name",






9

    "isRerequestable": "true",






10

    "requires": "build-ready",






11

    "targets": [],






12

    "blocks": "build-start",






13

    "source": "value",






14

    "timeout": "123"






15

  }),






16

});






17







18

const data = await response.json();






19

console.log(data);




```

Response
```


1

{






2

  "id": "icfg_1234567890",






3

  "name": "Example Name",






4

  "ownerId": "example_id",






5

  "projectId": "example_id",






6

  "isRerequestable": "false",






7

  "requires": "build-ready",






8

  "source": {






9

    "kind": "integration",






10

    "integrationId": "example_id",






11

    "integrationConfigurationId": "example_id",






12

    "resourceId": "example_id",






13

    "externalResourceId": "example_id"






14

  },






15

  "blocks": "none",






16

  "targets": [],






17

  "sourceKind": "integration",






18

  "sourceIntegrationConfigurationId": "example_id",






19

  "timeout": "123",






20

  "createdAt": "123",






21

  "updatedAt": "123",






22

  "deletedAt": "123"






23

}




```
