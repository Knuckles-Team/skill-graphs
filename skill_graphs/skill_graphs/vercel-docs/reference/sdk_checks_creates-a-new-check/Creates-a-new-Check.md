# Creates a new Check
POST`https://api.vercel.com/v1/deployments/{deploymentId}/checks`
Creates a new check. This endpoint must be called with an OAuth2 or it will produce a 400 error.
This endpoint is deprecated
Request
```


1

package main






2







3

import(






4

	"os"






5

	"github.com/vercel/vercel"






6

	"context"






7

	"github.com/vercel/vercel/models/operations"






8

	"log"






9

)






10







11

func main() {






12

    s := vercel.New(






13

        vercel.WithSecurity(os.Getenv("VERCEL_BEARER_TOKEN")),






14

    )






15







16

    ctx := context.Background()






17

    res, err := s.Checks.CreateCheck(ctx, "dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6", nil, nil, &operations.CreateCheckRequestBody{






18

        Name: "Performance Check",






19

        Path: vercel.String("/"),






20

        Blocking: true,






21

        DetailsURL: vercel.String("http://example.com"),






22

        ExternalID: vercel.String("1234abc"),






23

        Rerequestable: vercel.Bool(true),






24

    })






25

    if err != nil {






26

        log.Fatal(err)






27

    }






28

    if res.Object != nil {






29

        // handle response






30

    }






31

}




```

Response
```


1

{






2

  "id": "chk_1a2b3c4d5e6f7g8h9i0j",






3

  "name": "Performance Check",






4

  "createdAt": "123",






5

  "updatedAt": "123",






6

  "deploymentId": "example_id",






7

  "status": "completed",






8

  "conclusion": "succeeded",






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

  "path": "/api/users",






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
