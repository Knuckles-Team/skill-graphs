##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid. The provided token is not from an OAuth2 Client
401The request is not authorized.
403You do not have permission to access this resource.
404Check was not found The deployment was not found
413The output provided is too large
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

    res, err := s.Checks.UpdateCheck(ctx, operations.UpdateCheckRequest{






18

        DeploymentID: "dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6",






19

        CheckID: "check_2qn7PZrx89yxY34vEZPD31Y9XVj6",






20

        RequestBody: &operations.UpdateCheckRequestBody{






21

            Name: vercel.String("Performance Check"),






22

            Path: vercel.String("/"),






23

            DetailsURL: vercel.String("https://example.com/check/run/1234abc"),






24

            Output: &operations.Output{






25

                Metrics: &operations.Metrics{






26

                    Fcp: operations.Fcp{






27

                        Value: vercel.Float64(1200),






28

                        PreviousValue: vercel.Float64(900),






29

                        Source: operations.UpdateCheckSourceWebVitals,






30

                    },






31

                    Lcp: operations.Lcp{






32

                        Value: vercel.Float64(1200),






33

                        PreviousValue: vercel.Float64(1000),






34

                        Source: operations.UpdateCheckChecksSourceWebVitals,






35

                    },






36

                    Cls: operations.Cls{






37

                        Value: vercel.Float64(4),






38

                        PreviousValue: vercel.Float64(2),






39

                        Source: operations.UpdateCheckChecksRequestSourceWebVitals,






40

                    },






41

                    Tbt: operations.Tbt{






42

                        Value: vercel.Float64(3000),






43

                        PreviousValue: vercel.Float64(3500),






44

                        Source: operations.UpdateCheckChecksRequestRequestBodySourceWebVitals,






45

                    },






46

                    VirtualExperienceScore: &operations.VirtualExperienceScore{






47

                        Value: vercel.Int64(30),






48

                        PreviousValue: vercel.Int64(35),






49

                        Source: operations.UpdateCheckChecksRequestRequestBodyOutputSourceWebVitals,






50

                    },






51

                },






52

            },






53

            ExternalID: vercel.String("1234abc"),






54

        },






55

    })






56

    if err != nil {






57

        log.Fatal(err)






58

    }






59

    if res.Object != nil {






60

        // handle response






61

    }






62

}




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

Copy as MarkdownGive feedbackAsk AI about this page
