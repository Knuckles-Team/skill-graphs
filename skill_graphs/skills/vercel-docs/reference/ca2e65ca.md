##  [Authentication](https://vercel.com/docs#authentication)[](https://vercel.com/docs#authentication)
Vercel authenticates requests to your Partner API endpoints using the methods below. You must validate authentication on every request to ensure requests come from Vercel.
###  [User Authentication](https://vercel.com/docs#user-authentication)[](https://vercel.com/docs#user-authentication)
This authentication uses the [here](https://marketplace.vercel.com/.well-known/jwks).
User Auth OIDC token claims schema:
```









```


1

{






2

  "type": "object",






3

  "properties": {






4

    "iss": {






5

      "type": "string",






6

      "enum": [






7

        "https://marketplace.vercel.com"






8

      ]






9

    },






10

    "aud": {






11

      "type": "string",






12

      "description": "The integration ID. Example: \"oac_9f4YG9JFjgKkRlxoaaGG0y05\""






13

    },






14

    "type": {






15

      "type": "string",






16

      "enum": [






17

        "access_token",






18

        "id_token"






19

      ],






20

      "description": "The type of the token: id_token or access_token."






21

    },






22

    "account_id": {






23

      "type": "string"






24

    },






25

    "sub": {






26

      "type": "string",






27

      "description": "Denotes the User who is making the change (matches `/^account:[0-9a-fA-F]+:user:[0-9a-fA-F]+$/`)"






28

    },






29

    "installation_id": {






30

      "type": "string",






31

      "description": "The ID of the installation. Example: \"icfg_9bceb8ccT32d3U417ezb5c8p\""






32

    },






33

    "user_id": {






34

      "type": "string"






35

    },






36

    "user_role": {






37

      "type": "string",






38

      "enum": [






39

        "ADMIN",






40

        "USER"






41

      ],






42

      "description": "The `ADMIN` role, by default, is provided to users capable of installing integrations, while the `USER` role can be granted to Vercel users with the Vercel `Billing` or Vercel `Viewer` role, which are considered to be Read-Only roles."






43

    },






44

    "user_email": {






45

      "type": "string",






46

      "description": "The user's verified email address. For this property to have a value, your Marketplace integration must be opted in. Please reach out to Vercel Support to request access. Without access, this property will be undefined."






47

    },






48

    "user_name": {






49

      "type": "string",






50

      "description": "The user's real name"






51

    },






52

    "user_avatar_url": {






53

      "type": "string",






54

      "description": "The user's public avatar URL"






55

    }






56

  },






57

  "required": [






58

    "iss",






59

    "aud",






60

    "account_id",






61

    "sub",






62

    "installation_id",






63

    "user_id",






64

    "user_role"






65

  ],






66

  "additionalProperties": false






67

}




```


```

###  [System Authentication](https://vercel.com/docs#system-authentication)[](https://vercel.com/docs#system-authentication)
This authentication uses the [here](https://marketplace.vercel.com/.well-known/jwks).
System Auth OIDC token claims schema:
```









```


1

{






2

  "type": "object",






3

  "properties": {






4

    "iss": {






5

      "type": "string",






6

      "enum": [






7

        "https://marketplace.vercel.com"






8

      ]






9

    },






10

    "sub": {






11

      "type": "string",






12

      "description": "Denotes the Account (or Team) who is making the change (matches `/^account:[0-9a-fA-F]+$/`), possibly null"






13

    },






14

    "aud": {






15

      "type": "string",






16

      "description": "The integration ID. Example: \"oac_9f4YG9JFjgKkRlxoaaGG0y05\""






17

    },






18

    "type": {






19

      "type": "string",






20

      "enum": [






21

        "access_token",






22

        "id_token"






23

      ],






24

      "description": "The type of the token: id_token or access_token."






25

    },






26

    "installation_id": {






27

      "type": "string",






28

      "nullable": true,






29

      "description": "The ID of the installation. Example: \"icfg_9bceb8ccT32d3U417ezb5c8p\""






30

    },






31

    "account_id": {






32

      "type": "string"






33

    }






34

  },






35

  "required": [






36

    "iss",






37

    "sub",






38

    "aud",






39

    "installation_id",






40

    "account_id"






41

  ],






42

  "additionalProperties": false






43

}




```


```

###  [Security best practices](https://vercel.com/docs#security-best-practices)[](https://vercel.com/docs#security-best-practices)
  * **Verify token signatures** — Always validate OIDC token signatures using Vercel's [OIDC configuration](https://marketplace.vercel.com/.well-known/openid-configuration)
  * **Check claims** — Verify the `aud` claim matches your integration ID and the `sub` claim identifies the authenticated user or account
  * **Validate user roles** — For user authentication, always validate the user's role before performing actions
