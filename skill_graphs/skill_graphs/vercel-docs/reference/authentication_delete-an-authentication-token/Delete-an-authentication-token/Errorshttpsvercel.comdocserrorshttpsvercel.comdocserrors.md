##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Token not found with the requested `tokenId`.
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

Copy as MarkdownGive feedbackAsk AI about this page
