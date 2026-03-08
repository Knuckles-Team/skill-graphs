# Delete an authentication token
DEL`https://api.vercel.com/v3/user/tokens/{tokenId}`
Invalidate an authentication token, such that it will no longer be valid for future HTTP requests.
TypeScriptNext.jscURL
https://api.vercel.com/v3/user/tokens/{tokenId}
```


1

const response = await fetch('https://api.vercel.com/v3/user/tokens/tokenId', {






2

  method: 'DELETE',






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

  "tokenId": "5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391"






3

}




```
