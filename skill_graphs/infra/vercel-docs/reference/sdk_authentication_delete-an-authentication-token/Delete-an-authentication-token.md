# Delete an authentication token
DEL`https://api.vercel.com/v3/user/tokens/{tokenId}`
Invalidate an authentication token, such that it will no longer be valid for future HTTP requests.
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

  const result = await vercel.authentication.deleteAuthToken({






9

    tokenId: "5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391",






10

  });






11







12

  console.log(result);






13

}






14







15

run();




```

Response
```


1

{






2

  "tokenId": "5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391"






3

}




```
