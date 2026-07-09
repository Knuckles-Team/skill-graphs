# List git repositories linked to namespace by provider
GET`https://api.vercel.com/v1/integrations/search-repo`
Lists git repositories linked to a namespace `id` for a supported provider. A specific namespace `id` can be obtained via the `git-namespaces` endpoint. Supported providers are `github`, `gitlab` and `bitbucket`. If the provider or namespace is not provided, it will try to obtain it from the user that authenticated the request.
TypeScriptNext.jscURL
https://api.vercel.com/v1/integrations/search-repo
```


1

const response = await fetch('https://api.vercel.com/v1/integrations/search-repo?query=string&namespaceId=value&provider=value&installationId=string&host=string&teamId=string&slug=string', {






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
"value"



```

##  [Authentication](https://vercel.com/docs/rest-api/integrations/list-git-repositories-linked-to-namespace-by-provider#authentication)[](https://vercel.com/docs/rest-api/integrations/list-git-repositories-linked-to-namespace-by-provider#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/integrations/list-git-repositories-linked-to-namespace-by-provider#query-parameters)[](https://vercel.com/docs/rest-api/integrations/list-git-repositories-linked-to-namespace-by-provider#query-parameters)
querystringOptional
namespaceIdanyOptional
provideranyOptional
+Show 5 enum values
installationIdstringOptional
hoststringOptional
The custom Git host if using a custom Git provider, like GitHub Enterprise Server
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/integrations/list-git-repositories-linked-to-namespace-by-provider#response)[](https://vercel.com/docs/rest-api/integrations/list-git-repositories-linked-to-namespace-by-provider#response)
200Success
##  [Errors](https://vercel.com/docs/rest-api/integrations/list-git-repositories-linked-to-namespace-by-provider#errors)[](https://vercel.com/docs/rest-api/integrations/list-git-repositories-linked-to-namespace-by-provider#errors)
400One of the provided values in the request query is invalid.
401Error
403You do not have permission to access this resource.
404Error
429Error
500Error
TypeScriptNext.jscURL
https://api.vercel.com/v1/integrations/search-repo
```


1

const response = await fetch('https://api.vercel.com/v1/integrations/search-repo?query=string&namespaceId=value&provider=value&installationId=string&host=string&teamId=string&slug=string', {






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
"value"



```

Copy as MarkdownGive feedbackAsk AI about this page
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Retrieve an integration configuration
