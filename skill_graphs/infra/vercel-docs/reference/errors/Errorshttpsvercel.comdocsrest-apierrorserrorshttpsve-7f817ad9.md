#  [Errors](https://vercel.com/docs/rest-api/errors#errors)[](https://vercel.com/docs/rest-api/errors#errors)
List of general and specific errors you may encounter when using the REST API.
##  [Generic errors](https://vercel.com/docs/rest-api/errors#generic-errors)[](https://vercel.com/docs/rest-api/errors#generic-errors)
These error codes are consistent for all endpoints.
###  [Forbidden](https://vercel.com/docs/rest-api/errors#forbidden)[](https://vercel.com/docs/rest-api/errors#forbidden)
You're not authorized to use the endpoint. This usually happens due to missing a user token.
Similar to the HTTP 403 Forbidden error.
```


1

{






2

  "error": {






3

    "code": "forbidden",






4

    "message": "Not authorized"






5

  }






6

}




```

###  [Rate limited](https://vercel.com/docs/rest-api/errors#rate-limited)[](https://vercel.com/docs/rest-api/errors#rate-limited)
You exceeded the maximum allotted requests.
The limit of requests is per endpoint basis so you can continue using other endpoints even if some of them give you this error.
```


1

{






2

  "error": {






3

    "code": "rate_limited",






4

    "message": "The rate limit of 6 exceeded for 'api-www-user-update-username'. Try again in 7 days",






5

    "limit": {






6

      "remaining": 0,






7

      "reset": 1571432075,






8

      "resetMs": 1571432075563,






9

      "total": 6






10

    }






11

  }






12

}




```

###  [Bad request](https://vercel.com/docs/rest-api/errors#bad-request)[](https://vercel.com/docs/rest-api/errors#bad-request)
There was an error with the request, the `error.message` would contain information about the issue.
```


1

{






2

  "error": {






3

    "code": "bad_request",






4

    "message": "An english description of the error that just occurred"






5

  }






6

}




```

###  [Internal server error](https://vercel.com/docs/rest-api/errors#internal-server-error)[](https://vercel.com/docs/rest-api/errors#internal-server-error)
This error is similar to the HTTP 500 Internal Server Error error code.
```


1

{






2

  "error": {






3

    "code": "internal_server_error",






4

    "message": "An unexpected internal error occurred"






5

  }






6

}




```

###  [Resource not found](https://vercel.com/docs/rest-api/errors#resource-not-found)[](https://vercel.com/docs/rest-api/errors#resource-not-found)
The requested resource could not be found.
```


1

{






2

  "error": {






3

    "code": "not_found",






4

    "message": "Could not find the RESOURCE: ID"






5

  }






6

}




```

###  [Method unknown](https://vercel.com/docs/rest-api/errors#method-unknown)[](https://vercel.com/docs/rest-api/errors#method-unknown)
The endpoint you're requesting does not handle the method you defined. The error message will contain the methods the endpoint responds to.
```


1

{






2

  "error": {






3

    "code": "method_unknown",






4

    "message": "This endpoint only responds to METHOD"






5

  }






6

}




```

##  [Deployment errors](https://vercel.com/docs/rest-api/errors#deployment-errors)[](https://vercel.com/docs/rest-api/errors#deployment-errors)
These error codes can happen when using any deployment related endpoint.
###  [Missing files](https://vercel.com/docs/rest-api/errors#missing-files)[](https://vercel.com/docs/rest-api/errors#missing-files)
Some of the files you defined when creating the deployment are missing.
```


1

{






2

  "error": {






3

    "code": "missing_files",






4

    "message": "Missing files",






5

    "missing": []






6

  }






7

}




```

###  [No files in the deployment](https://vercel.com/docs/rest-api/errors#no-files-in-the-deployment)[](https://vercel.com/docs/rest-api/errors#no-files-in-the-deployment)
You tried to create an empty deployment.
```


1

{






2

  "error": {






3

    "code": "no_files",






4

    "message": "No files in the deployment"






5

  }






6

}




```

###  [Too many environment variables](https://vercel.com/docs/rest-api/errors#too-many-environment-variables)[](https://vercel.com/docs/rest-api/errors#too-many-environment-variables)
The limit of environment variables per deployment is 100 and you defined more. The error message indicates the amount you defined.
`#` is your number of variables.
```


1

{






2

  "error": {






3

    "code": "env_too_many_keys",






4

    "message": "Too many env vars have been supplied (100 max allowed, but got #)"






5

  }






6

}




```

###  [Environment variable key with invalid characters](https://vercel.com/docs/rest-api/errors#environment-variable-key-with-invalid-characters)[](https://vercel.com/docs/rest-api/errors#environment-variable-key-with-invalid-characters)
Some environment variable name contains an invalid character. The only valid characters are letters, digits and `_`.
The error message will contain the `KEY` with the problem.
```


1

{






2

  "error": {






3

    "code": "env_key_invalid_characters",






4

    "message": "The env key \"KEY\" contains invalid characters. Only letters, digits and `_` are allowed",






5

    "key": "KEY"






6

  }






7

}




```

###  [Environment variable key with a long name](https://vercel.com/docs/rest-api/errors#environment-variable-key-with-a-long-name)[](https://vercel.com/docs/rest-api/errors#environment-variable-key-with-a-long-name)
An environment variable name is too long, the maximum permitted name is 256 characters.
The error message contains the environment `KEY`.
```


1

{






2

  "error": {






3

    "code": "env_key_invalid_length",






4

    "message": "The env key \"KEY\" exceeds the 256 length limit",






5

    "key": "KEY"






6

  }






7

}




```

###  [Environment variable value with a long name](https://vercel.com/docs/rest-api/errors#environment-variable-value-with-a-long-name)[](https://vercel.com/docs/rest-api/errors#environment-variable-value-with-a-long-name)
An environment variable value contains a value too long, the maximum permitted value is 65536 characters.
The error message contains the environment `KEY`.
```


1

{






2

  "error": {






3

    "code": "env_value_invalid_length",






4

    "message": "The env value for \"KEY\" exceeds the 65536 length limit",






5

    "key": "KEY",






6

    "value": "VALUE"






7

  }






8

}




```

###  [Environment variable value is an object without UID](https://vercel.com/docs/rest-api/errors#environment-variable-value-is-an-object-without-uid)[](https://vercel.com/docs/rest-api/errors#environment-variable-value-is-an-object-without-uid)
The value of an environment variable is an object but it doesn't have a `uid`.
The error message contains the environment `KEY` which has the error.
```


1

{






2

  "error": {






3

    "code": "env_value_invalid_type_missing_uid",






4

    "message": "The env key \"KEY\" passed an object as a value with no `uid` key"






5

  }






6

}




```

###  [Environment variable value is an object with unknown props](https://vercel.com/docs/rest-api/errors#environment-variable-value-is-an-object-with-unknown-props)[](https://vercel.com/docs/rest-api/errors#environment-variable-value-is-an-object-with-unknown-props)
The value of an environment variable is an object with unknown attributes, it can only have a `uid` key inside the object.
```


1

{






2

  "error": {






3

    "code": "env_value_invalid_type_unknown_props",






4

    "message": "The env key \"KEY\" passed an object with unknown properties. Only `uid` is allowed when passing an object"






5

  }






6

}




```

###  [Environment variable value with an invalid type](https://vercel.com/docs/rest-api/errors#environment-variable-value-with-an-invalid-type)[](https://vercel.com/docs/rest-api/errors#environment-variable-value-with-an-invalid-type)
An environment variable value passed is of an unsupported type.
The error message contains the environment `KEY`.
```


1

{






2

  "error": {






3

    "code": "env_value_invalid_type",






4

    "message": "The env key \"KEY\" passed an unsupported type for its value",






5

    "key": "KEY"






6

  }






7

}




```

###  [Not allowed to access a secret](https://vercel.com/docs/rest-api/errors#not-allowed-to-access-a-secret)[](https://vercel.com/docs/rest-api/errors#not-allowed-to-access-a-secret)
You're trying to use a secret but you don't have access to it.
```


1

{






2

  "error": {






3

    "code": "env_secret_forbidden",






4

    "message": "Not allowed to access secret \"NAME\"",






5

    "uid": "UID"






6

  }






7

}




```

###  [Missing secret](https://vercel.com/docs/rest-api/errors#missing-secret)[](https://vercel.com/docs/rest-api/errors#missing-secret)
You're trying to use a secret as an environment value and it doesn't exist.
```


1

{






2

  "error": {






3

    "code": "env_secret_missing",






4

    "message": "Could not find a secret by uid \"UID\"",






5

    "uid": "UID"






6

  }






7

}




```

##  [Domain errors](https://vercel.com/docs/rest-api/errors#domain-errors)[](https://vercel.com/docs/rest-api/errors#domain-errors)
These error codes can happen when using any domain related endpoint.
###  [Domain forbidden](https://vercel.com/docs/rest-api/errors#domain-forbidden)[](https://vercel.com/docs/rest-api/errors#domain-forbidden)
You don't have access to the domain, this usually means the domain is owned by another account or team.
The domain is specified in the message and the `DOMAIN` key.
```


1

{






2

  "error": {






3

    "code": "forbidden",






4

    "message": "You don't have access to \"DOMAIN\"",






5

    "domain": "DOMAIN"






6

  }






7

}




```

###  [Domain not found](https://vercel.com/docs/rest-api/errors#domain-not-found)[](https://vercel.com/docs/rest-api/errors#domain-not-found)
The domain name could not be found in the system.
```


1

{






2

  "error": {






3

    "code": "not_found",






4

    "message": "Domain name not found"






5

  }






6

}




```

###  [Missing domain name](https://vercel.com/docs/rest-api/errors#missing-domain-name)[](https://vercel.com/docs/rest-api/errors#missing-domain-name)
The domain name wasn't specified in the URL. This means you tried to use an endpoint which requires you to define the domain name in the URL but didn't define it.
```


1

{






2

  "error": {






3

    "code": "missing_name",






4

    "message": "The URL was expected to include the domain name. Example: /domains/google.com"






5

  }






6

}




```

###  [Conflicting aliases](https://vercel.com/docs/rest-api/errors#conflicting-aliases)[](https://vercel.com/docs/rest-api/errors#conflicting-aliases)
You must remove the aliases described in the error before removing the domain.
The aliases are specified in the `ALIASES` key.
```


1

{






2

  "error": {






3

    "code": "conflict_aliases",






4

    "message": "The following aliases must be removed before removing the domain: ALIASES",






5

    "aliases": ["ALIASES"]






6

  }






7

}




```

###  [Not modified](https://vercel.com/docs/rest-api/errors#not-modified)[](https://vercel.com/docs/rest-api/errors#not-modified)
When trying to modify a domain nothing was required to change.
```


1

{






2

  "error": {






3

    "code": "not_modified",






4

    "message": "Nothing to do"






5

  }






6

}




```

###  [Missing name for domain](https://vercel.com/docs/rest-api/errors#missing-name-for-domain)[](https://vercel.com/docs/rest-api/errors#missing-name-for-domain)
When trying to add a domain the name wasn't present in the request body.
```


1

{






2

  "error": {






3

    "code": "missing_name",






4

    "message": "The `name` field in the body was expected but is not present in the body payload. Example value: `example.com`"






5

  }






6

}




```

###  [Invalid name for domain](https://vercel.com/docs/rest-api/errors#invalid-name-for-domain)[](https://vercel.com/docs/rest-api/errors#invalid-name-for-domain)
The domain name defined in the request body is invalid.
The name is specified in the error as the `NAME` key.
```


1

{






2

  "error": {






3

    "code": "invalid_name",






4

    "message": "The `name` field contains an invalid domain name (\"NAME\")",






5

    "name": "NAME"






6

  }






7

}




```

###  [Custom domain needs a plan upgrade](https://vercel.com/docs/rest-api/errors#custom-domain-needs-a-plan-upgrade)[](https://vercel.com/docs/rest-api/errors#custom-domain-needs-a-plan-upgrade)
To add a custom domain to your account or team you need to upgrade to a paid plan.
```


1

{






2

  "error": {






3

    "code": "custom_domain_needs_upgrade",






4

    "message": "Domain name creation requires a premium account."






5

  }






6

}




```

###  [Domain already exists](https://vercel.com/docs/rest-api/errors#domain-already-exists)[](https://vercel.com/docs/rest-api/errors#domain-already-exists)
The domain name you're trying to add already exists.
The domain name and its current ID are received in the `NAME` and `DOMAIN_ID` keys.
```


1

{






2

  "error": {






3

    "code": "not_modified",






4

    "message": "The domain \"NAME\" already exists",






5

    "name": "NAME",






6

    "uid": "DOMAIN_ID"






7

  }






8

}




```

###  [Can't create the domain](https://vercel.com/docs/rest-api/errors#can't-create-the-domain)[](https://vercel.com/docs/rest-api/errors#can't-create-the-domain)
The domain name can't be created. Most likely it couldn't be verified.
```


1

{






2

  "error": {






3

    "code": "forbidden",






4

    "message": "You don't have permission to create a domain"






5

  }






6

}




```

###  [Failed to add domain after purchase](https://vercel.com/docs/rest-api/errors#failed-to-add-domain-after-purchase)[](https://vercel.com/docs/rest-api/errors#failed-to-add-domain-after-purchase)
The domain was purchased but there was an error adding it to your account. Please [contact support](https://vercel.com/help).
```


1

{






2

  "error": {






3

    "code": "failed_to_add_domain",






4

    "message": "The domain was bought but couldn't be added."






5

  }






6

}




```

###  [Unable to determine the domain price](https://vercel.com/docs/rest-api/errors#unable-to-determine-the-domain-price)[](https://vercel.com/docs/rest-api/errors#unable-to-determine-the-domain-price)
The price of a domain could not be determined.
```


1

{






2

  "error": {






3

    "code": "service_unavailable",






4

    "message": "Failed to determine the domain price"






5

  }






6

}




```

###  [Domain price mismatch](https://vercel.com/docs/rest-api/errors#domain-price-mismatch)[](https://vercel.com/docs/rest-api/errors#domain-price-mismatch)
The `expectedPrice` supplied in the request body does not match the actual domain price, which is specified in the `actualPrice` key.
```


1

{






2

  "error": {






3

    "code": "price_mismatch",






4

    "message": "The expected price does not match the actual price",






5

    "price": "ACTUAL_PRICE"






6

  }






7

}




```

###  [Domain is not available](https://vercel.com/docs/rest-api/errors#domain-is-not-available)[](https://vercel.com/docs/rest-api/errors#domain-is-not-available)
The domain name is not available to be purchased.
```


1

{






2

  "error": {






3

    "code": "not_available",






4

    "message": "Domain is not available"






5

  }






6

}




```

###  [Invalid domain name](https://vercel.com/docs/rest-api/errors#invalid-domain-name)[](https://vercel.com/docs/rest-api/errors#invalid-domain-name)
The domain name or TLD is invalid or not supported.
```


1

{






2

  "error": {






3

    "code": "invalid_domain",






4

    "message": "Invalid domain or TLD"






5

  }






6

}




```

###  [Missing DNS record name](https://vercel.com/docs/rest-api/errors#missing-dns-record-name)[](https://vercel.com/docs/rest-api/errors#missing-dns-record-name)
The DNS record key `name` is required and was not provided. It could be
```


1

{






2

  "error": {






3

    "code": "missing_type",






4

    "message": "Missing `type` parameter"






5

  }






6

}




```

##  [DNS errors](https://vercel.com/docs/rest-api/errors#dns-errors)[](https://vercel.com/docs/rest-api/errors#dns-errors)
These error codes can happen when using any DNS related endpoint.
###  [Missing DNS record name](https://vercel.com/docs/rest-api/errors#missing-dns-record-name)[](https://vercel.com/docs/rest-api/errors#missing-dns-record-name)
The DNS record key `name` is required and was not provided. It should be either a subdomain or `@` for the domain itself.
```


1

{






2

  "error": {






3

    "code": "missing_name",






4

    "message": "Missing `name` parameter"






5

  }






6

}




```

###  [Missing DNS record type](https://vercel.com/docs/rest-api/errors#missing-dns-record-type)[](https://vercel.com/docs/rest-api/errors#missing-dns-record-type)
The DNS record key `type` is required and was not provided. It could be
```


1

{






2

  "error": {






3

    "code": "missing_type",






4

    "message": "Missing `type` parameter"






5

  }






6

}




```

##  [OAuth2 errors](https://vercel.com/docs/rest-api/errors#oauth2-errors)[](https://vercel.com/docs/rest-api/errors#oauth2-errors)
These errors can occur when using any [OAuth2 related endpoint](https://vercel.com/docs/integrations/vercel-api-integrations#create-an-access-token).
###  [Client not found](https://vercel.com/docs/rest-api/errors#client-not-found)[](https://vercel.com/docs/rest-api/errors#client-not-found)
The OAuth2 client ID could not be found or doesn't exist.
```


1

{






2

  "error": {






3

    "code": "not_found",






4

    "message": "OAuth client doesn't not found: CLIENT_ID"






5

  }






6

}




```

On this page
  * [Generic errors](https://vercel.com/docs/rest-api/errors#generic-errors)
  * [Forbidden](https://vercel.com/docs/rest-api/errors#forbidden)
  * [Rate limited](https://vercel.com/docs/rest-api/errors#rate-limited)
  * [Bad request](https://vercel.com/docs/rest-api/errors#bad-request)
  * [Internal server error](https://vercel.com/docs/rest-api/errors#internal-server-error)
  * [Resource not found](https://vercel.com/docs/rest-api/errors#resource-not-found)
  * [Method unknown](https://vercel.com/docs/rest-api/errors#method-unknown)
  * [Deployment errors](https://vercel.com/docs/rest-api/errors#deployment-errors)
  * [Missing files](https://vercel.com/docs/rest-api/errors#missing-files)
  * [No files in the deployment](https://vercel.com/docs/rest-api/errors#no-files-in-the-deployment)
  * [Too many environment variables](https://vercel.com/docs/rest-api/errors#too-many-environment-variables)
  * [Environment variable key with invalid characters](https://vercel.com/docs/rest-api/errors#environment-variable-key-with-invalid-characters)
  * [Environment variable key with a long name](https://vercel.com/docs/rest-api/errors#environment-variable-key-with-a-long-name)
  * [Environment variable value with a long name](https://vercel.com/docs/rest-api/errors#environment-variable-value-with-a-long-name)
  * [Environment variable value is an object without UID](https://vercel.com/docs/rest-api/errors#environment-variable-value-is-an-object-without-uid)
  * [Environment variable value is an object with unknown props](https://vercel.com/docs/rest-api/errors#environment-variable-value-is-an-object-with-unknown-props)
  * [Environment variable value with an invalid type](https://vercel.com/docs/rest-api/errors#environment-variable-value-with-an-invalid-type)
  * [Not allowed to access a secret](https://vercel.com/docs/rest-api/errors#not-allowed-to-access-a-secret)
  * [Missing secret](https://vercel.com/docs/rest-api/errors#missing-secret)
  * [Domain errors](https://vercel.com/docs/rest-api/errors#domain-errors)
  * [Domain forbidden](https://vercel.com/docs/rest-api/errors#domain-forbidden)
  * [Domain not found](https://vercel.com/docs/rest-api/errors#domain-not-found)
  * [Missing domain name](https://vercel.com/docs/rest-api/errors#missing-domain-name)
  * [Conflicting aliases](https://vercel.com/docs/rest-api/errors#conflicting-aliases)
  * [Not modified](https://vercel.com/docs/rest-api/errors#not-modified)
  * [Missing name for domain](https://vercel.com/docs/rest-api/errors#missing-name-for-domain)
  * [Invalid name for domain](https://vercel.com/docs/rest-api/errors#invalid-name-for-domain)
  * [Custom domain needs a plan upgrade](https://vercel.com/docs/rest-api/errors#custom-domain-needs-a-plan-upgrade)
  * [Domain already exists](https://vercel.com/docs/rest-api/errors#domain-already-exists)
  * [Can't create the domain](https://vercel.com/docs/rest-api/errors#can't-create-the-domain)
  * [Failed to add domain after purchase](https://vercel.com/docs/rest-api/errors#failed-to-add-domain-after-purchase)
  * [Unable to determine the domain price](https://vercel.com/docs/rest-api/errors#unable-to-determine-the-domain-price)
  * [Domain price mismatch](https://vercel.com/docs/rest-api/errors#domain-price-mismatch)
  * [Domain is not available](https://vercel.com/docs/rest-api/errors#domain-is-not-available)
  * [Invalid domain name](https://vercel.com/docs/rest-api/errors#invalid-domain-name)
  * [Missing DNS record name](https://vercel.com/docs/rest-api/errors#missing-dns-record-name)
  * [DNS errors](https://vercel.com/docs/rest-api/errors#dns-errors)
  * [Missing DNS record name](https://vercel.com/docs/rest-api/errors#missing-dns-record-name)
  * [Missing DNS record type](https://vercel.com/docs/rest-api/errors#missing-dns-record-type)
  * [OAuth2 errors](https://vercel.com/docs/rest-api/errors#oauth2-errors)
  * [Client not found](https://vercel.com/docs/rest-api/errors#client-not-found)


Copy as MarkdownGive feedbackAsk AI about this page
## Get Started
  * [Templates](https://vercel.com/templates)
  * [Supported frameworks](https://vercel.com/docs/frameworks)
  * [Marketplace](https://vercel.com/marketplace)
  * [Domains](https://vercel.com/domains)


## Build
  * [Next.js on Vercel](https://vercel.com/frameworks/nextjs)
  * [Turborepo](https://vercel.com/solutions/turborepo)


## Scale
  * [Content delivery network](https://vercel.com/cdn)
  * [Fluid compute](https://vercel.com/fluid)
  * [CI/CD](https://vercel.com/products/previews)
  * [Observability](https://vercel.com/products/observability)
  * [AI GatewayNew](https://vercel.com/ai-gateway)
  * [Vercel AgentNew](https://vercel.com/agent)


## Secure
  * [Platform security](https://vercel.com/security)
  * [Web Application Firewall](https://vercel.com/security/web-application-firewall)
  * [Bot management](https://vercel.com/security/bot-management)
  * [BotID](https://vercel.com/botid)
  * [SandboxNew](https://vercel.com/sandbox)


## Resources
  * [Pricing](https://vercel.com/pricing)
  * [Customers](https://vercel.com/customers)
  * [Enterprise](https://vercel.com/enterprise)
  * [Articles](https://vercel.com/i)
  * [Startups](https://vercel.com/startups)
  * [Solution partners](https://vercel.com/partners/solution-partners)


## Learn
  * [Docs](https://vercel.com/docs)
  * [Blog](https://vercel.com/blog)
  * [Changelog](https://vercel.com/changelog)
  * [Knowledge Base](https://vercel.com/kb)
  * [Academy](https://vercel.com/academy)
  * [Community](https://community.vercel.com)


## Frameworks
  * [Next.js](https://vercel.com/frameworks/nextjs)
  * [Nuxt](https://vercel.com/docs/frameworks/full-stack/nuxt)
  * [Svelte](https://vercel.com/docs/frameworks/full-stack/sveltekit)
  * [Nitro](https://vercel.com/docs/frameworks/backend/nitro)
  * [Turbo](https://vercel.com/solutions/turborepo)


## SDKs
## Use Cases
  * [Composable commerce](https://vercel.com/solutions/composable-commerce)
  * [Multi-tenant platforms](https://vercel.com/solutions/multi-tenant-saas)
  * [Web apps](https://vercel.com/solutions/web-apps)
  * [Marketing sites](https://vercel.com/solutions/marketing-sites)
  * [Platform engineers](https://vercel.com/solutions/platform-engineering)
  * [Design engineers](https://vercel.com/solutions/design-engineering)


## Company
  * [About](https://vercel.com/about)
  * [Careers](https://vercel.com/careers)
  * [Help](https://vercel.com/help)
  * [Press](https://vercel.com/press)
  * [Legal](https://vercel.com/legal)
  * [Privacy Policy](https://vercel.com/legal/privacy-policy)


## Community
  * [Open source program](https://vercel.com/open-source-program)
  * [Events](https://vercel.com/events)
  * [Shipped on Vercel](https://vercel.com/shipped)


[](https://vercel.com/home)

Select a display theme: systemlightdark
