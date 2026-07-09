# Update a check
PATCH`https://api.vercel.com/v1/deployments/{deploymentId}/checks/{checkId}`
Update an existing check. This endpoint must be called with an OAuth2 or it will produce a 400 error.
This endpoint is deprecated
TypeScriptNext.jscURL
https://api.vercel.com/v1/deployments/{deploymentId}/checks/{checkId}
```


1

const response = await fetch('https://api.vercel.com/v1/deployments/deploymentId/checks/checkId?teamId=string&slug=string', {






2

  method: 'PATCH',






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

    "name": "Performance Check",






9

    "path": "/",






10

    "status": "running",






11

    "conclusion": "canceled",






12

    "detailsUrl": "https://example.com/check/run/1234abc",






13

    "output": {






14

      "metrics": {






15

        "FCP": {






16

          "value": "1200",






17

          "previousValue": "900",






18

          "source": "web-vitals"






19

        },






20

        "LCP": {






21

          "value": "1200",






22

          "previousValue": "1000",






23

          "source": "web-vitals"






24

        },






25

        "CLS": {






26

          "value": "4",






27

          "previousValue": "2",






28

          "source": "web-vitals"






29

        },






30

        "TBT": {






31

          "value": "3000",






32

          "previousValue": "3500",






33

          "source": "web-vitals"






34

        },






35

        "virtualExperienceScore": {






36

          "value": "30",






37

          "previousValue": "35",






38

          "source": "web-vitals"






39

        }






40

      }






41

    },






42

    "externalId": "1234abc"






43

  }),






44

});






45







46

const data = await response.json();






47

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

  "createdAt": "123",






5

  "updatedAt": "123",






6

  "deploymentId": "example_id",






7

  "status": "running",






8

  "conclusion": "canceled",






9

  "externalId": "example_id",






10

  "output": {






11

    "metrics": {






12

      "FCP": {






13

        "value": "123",






14

        "previousValue": "123",






15

        "source": "web-vitals"






16

      },






17

      "LCP": {






18

        "value": "123",






19

        "previousValue": "123",






20

        "source": "web-vitals"






21

      },






22

      "CLS": {






23

        "value": "123",






24

        "previousValue": "123",






25

        "source": "web-vitals"






26

      },






27

      "TBT": {






28

        "value": "123",






29

        "previousValue": "123",






30

        "source": "web-vitals"






31

      },






32

      "virtualExperienceScore": {






33

        "value": "123",






34

        "previousValue": "123",






35

        "source": "web-vitals"






36

      }






37

    }






38

  },






39

  "completedAt": "123",






40

  "path": "string",






41

  "blocking": "false",






42

  "detailsUrl": "https://example.com",






43

  "integrationId": "example_id",






44

  "startedAt": "123",






45

  "rerequestable": "false"






46

}




```
