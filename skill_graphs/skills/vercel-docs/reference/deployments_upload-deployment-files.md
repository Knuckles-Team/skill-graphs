Menu
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Upload Deployment Files
# Upload Deployment Files
POST`https://api.vercel.com/v2/files`
Before you create a deployment you need to upload the required files for that deployment. To do it, you need to first upload each file to this endpoint. Once that's completed, you can create a new deployment with the uploaded files. The file content must be placed inside the body of the request. In the case of a successful response you'll receive a status code 200 with an empty body.
TypeScriptNext.jscURL
https://api.vercel.com/v2/files
```


1

const response = await fetch('https://api.vercel.com/v2/files?teamId=string&slug=string', {






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

  "urls": []






3

}




```

##  [Authentication](https://vercel.com/docs/rest-api/deployments/upload-deployment-files#authentication)[](https://vercel.com/docs/rest-api/deployments/upload-deployment-files#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/deployments/upload-deployment-files#query-parameters)[](https://vercel.com/docs/rest-api/deployments/upload-deployment-files#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Header parameters](https://vercel.com/docs/rest-api/deployments/upload-deployment-files#header-parameters)[](https://vercel.com/docs/rest-api/deployments/upload-deployment-files#header-parameters)
Content-LengthnumberOptional
The file size in bytes
x-vercel-digeststringOptional
The file SHA1 used to check the integrity
x-now-digeststringOptionalDeprecated
The file SHA1 used to check the integrity
x-now-sizenumberOptionalDeprecated
The file size as an alternative to `Content-Length`
##  [Response](https://vercel.com/docs/rest-api/deployments/upload-deployment-files#response)[](https://vercel.com/docs/rest-api/deployments/upload-deployment-files#response)
200File already uploaded File successfully uploaded
urlsarrayRequired
Array of URLs where the file was updated
##  [Errors](https://vercel.com/docs/rest-api/deployments/upload-deployment-files#errors)[](https://vercel.com/docs/rest-api/deployments/upload-deployment-files#errors)
400One of the provided values in the headers is invalid Digest is not valid File size is not valid
401The request is not authorized.
403You do not have permission to access this resource.
