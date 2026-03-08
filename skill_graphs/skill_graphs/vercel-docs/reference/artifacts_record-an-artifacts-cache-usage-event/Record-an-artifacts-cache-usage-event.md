# Record an artifacts cache usage event
POST`https://api.vercel.com/v8/artifacts/events`
Records an artifacts cache usage event. The body of this request is an array of cache usage events. The supported event types are `HIT` and `MISS`. The source is either `LOCAL` the cache event was on the users filesystem cache or `REMOTE` if the cache event is for a remote cache. When the event is a `HIT` the request also accepts a number `duration` which is the time taken to generate the artifact in the cache.
TypeScriptNext.jscURL
https://api.vercel.com/v8/artifacts/events
```


1

const response = await fetch('https://api.vercel.com/v8/artifacts/events?teamId=string&slug=string', {






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

  body: JSON.stringify([






8

    {






9

      "sessionId": "example_id",






10

      "source": "LOCAL",






11

      "event": "HIT",






12

      "hash": "12HKQaOmR5t5Uy6vdcQsNIiZgHGB",






13

      "duration": "400"






14

    }






15

  ]),






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

{}




```
