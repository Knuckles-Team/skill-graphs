# Record an artifacts cache usage event
POST`https://api.vercel.com/v8/artifacts/events`
Records an artifacts cache usage event. The body of this request is an array of cache usage events. The supported event types are `HIT` and `MISS`. The source is either `LOCAL` the cache event was on the users filesystem cache or `REMOTE` if the cache event is for a remote cache. When the event is a `HIT` the request also accepts a number `duration` which is the time taken to generate the artifact in the cache.
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

  await vercel.artifacts.recordEvents({






9

    xArtifactClientCi: "VERCEL",






10

    xArtifactClientInteractive: 0,






11

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






12

    slug: "my-team-url-slug",






13

    requestBody: [






14

      {






15

        sessionId: "<id>",






16

        source: "REMOTE",






17

        event: "MISS",






18

        hash: "12HKQaOmR5t5Uy6vdcQsNIiZgHGB",






19

        duration: 400,






20

      },






21

    ],






22

  });






23







24







25

}






26







27

run();




```

Response
```


1

{}




```
