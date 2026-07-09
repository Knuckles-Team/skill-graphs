```
servers = None

```

####  parameters `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.PathItem.parameters "Permanent link")
```
parameters = None

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.PathItem.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

###  SecuritySchemeType [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.SecuritySchemeType "Permanent link")
Bases: `Enum`
####  apiKey `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.SecuritySchemeType.apiKey "Permanent link")
```
apiKey = 'apiKey'

```

####  http `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.SecuritySchemeType.http "Permanent link")
```
http = 'http'

```

####  oauth2 `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.SecuritySchemeType.oauth2 "Permanent link")
```
oauth2 = 'oauth2'

```

####  openIdConnect `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.SecuritySchemeType.openIdConnect "Permanent link")
```
openIdConnect = 'openIdConnect'

```

###  SecurityBase [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.SecurityBase "Permanent link")
Bases: `BaseModelWithConfig[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.BaseModelWithConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseModelWithConfig</span> \(<code>fastapi.openapi.models.BaseModelWithConfig</code>\)")`
####  type_ `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.SecurityBase.type_ "Permanent link")
```
type_ = Field(alias='type')

```

####  description `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.SecurityBase.description "Permanent link")
```
description = None

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.SecurityBase.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

###  APIKeyIn [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.APIKeyIn "Permanent link")
Bases: `Enum`
####  query `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.APIKeyIn.query "Permanent link")
```
query = 'query'

```

####  header `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.APIKeyIn.header "Permanent link")
```
header = 'header'

```

####  cookie `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.APIKeyIn.cookie "Permanent link")
```
cookie = 'cookie'

```

###  APIKey [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.APIKey "Permanent link")
Bases: `SecurityBase[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.SecurityBase "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">SecurityBase</span> \(<code>fastapi.openapi.models.SecurityBase</code>\)")`
####  type_ `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.APIKey.type_ "Permanent link")
```
type_ = Field(default=apiKey[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.SecuritySchemeType.apiKey "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">apiKey</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span> \(<code>fastapi.openapi.models.SecuritySchemeType.apiKey</code>\)"), alias='type')

```

####  in_ `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.APIKey.in_ "Permanent link")
```
in_ = Field(alias='in')

```

####  name `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.APIKey.name "Permanent link")
```
name

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.APIKey.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

####  description `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.APIKey.description "Permanent link")
```
description = None

```

###  HTTPBase [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.HTTPBase "Permanent link")
Bases: `SecurityBase[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.SecurityBase "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">SecurityBase</span> \(<code>fastapi.openapi.models.SecurityBase</code>\)")`
####  type_ `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.HTTPBase.type_ "Permanent link")
```
type_ = Field(default=http[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.SecuritySchemeType.http "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">http</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span> \(<code>fastapi.openapi.models.SecuritySchemeType.http</code>\)"), alias='type')

```

####  scheme `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.HTTPBase.scheme "Permanent link")
```
scheme

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.HTTPBase.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

####  description `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.HTTPBase.description "Permanent link")
```
description = None

```

###  HTTPBearer [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.HTTPBearer "Permanent link")
Bases: `HTTPBase[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.HTTPBase "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">HTTPBase</span> \(<code>fastapi.openapi.models.HTTPBase</code>\)")`
####  scheme `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.HTTPBearer.scheme "Permanent link")
```
scheme = 'bearer'

```

####  bearerFormat `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.HTTPBearer.bearerFormat "Permanent link")
```
bearerFormat = None

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.HTTPBearer.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

####  type_ `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.HTTPBearer.type_ "Permanent link")
```
type_ = Field(default=http[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.SecuritySchemeType.http "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">http</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span> \(<code>fastapi.openapi.models.SecuritySchemeType.http</code>\)"), alias='type')

```

####  description `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.HTTPBearer.description "Permanent link")
```
description = None

```

###  OAuthFlow [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlow "Permanent link")
Bases: `BaseModelWithConfig[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.BaseModelWithConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseModelWithConfig</span> \(<code>fastapi.openapi.models.BaseModelWithConfig</code>\)")`
####  refreshUrl `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlow.refreshUrl "Permanent link")
```
refreshUrl = None

```

####  scopes `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlow.scopes "Permanent link")
```
scopes = {}

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlow.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

###  OAuthFlowImplicit [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlowImplicit "Permanent link")
Bases: `OAuthFlow[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlow "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">OAuthFlow</span> \(<code>fastapi.openapi.models.OAuthFlow</code>\)")`
####  authorizationUrl `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlowImplicit.authorizationUrl "Permanent link")
```
authorizationUrl

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlowImplicit.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

####  refreshUrl `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlowImplicit.refreshUrl "Permanent link")
```
refreshUrl = None

```

####  scopes `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlowImplicit.scopes "Permanent link")
```
scopes = {}

```

###  OAuthFlowPassword [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlowPassword "Permanent link")
Bases: `OAuthFlow[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlow "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">OAuthFlow</span> \(<code>fastapi.openapi.models.OAuthFlow</code>\)")`
####  tokenUrl `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlowPassword.tokenUrl "Permanent link")
```
tokenUrl

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlowPassword.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

####  refreshUrl `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlowPassword.refreshUrl "Permanent link")
```
refreshUrl = None

```

####  scopes `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlowPassword.scopes "Permanent link")
```
scopes = {}

```

###  OAuthFlowClientCredentials [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlowClientCredentials "Permanent link")
Bases: `OAuthFlow[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlow "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">OAuthFlow</span> \(<code>fastapi.openapi.models.OAuthFlow</code>\)")`
####  tokenUrl `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlowClientCredentials.tokenUrl "Permanent link")
```
tokenUrl

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlowClientCredentials.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

####  refreshUrl `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlowClientCredentials.refreshUrl "Permanent link")
```
refreshUrl = None

```

####  scopes `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlowClientCredentials.scopes "Permanent link")
```
scopes = {}

```

###  OAuthFlowAuthorizationCode [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlowAuthorizationCode "Permanent link")
Bases: `OAuthFlow[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlow "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">OAuthFlow</span> \(<code>fastapi.openapi.models.OAuthFlow</code>\)")`
####  authorizationUrl `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlowAuthorizationCode.authorizationUrl "Permanent link")
```
authorizationUrl

```

####  tokenUrl `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlowAuthorizationCode.tokenUrl "Permanent link")
```
tokenUrl

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlowAuthorizationCode.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

####  refreshUrl `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlowAuthorizationCode.refreshUrl "Permanent link")
```
refreshUrl = None

```

####  scopes `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlowAuthorizationCode.scopes "Permanent link")
```
scopes = {}

```

###  OAuthFlows [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlows "Permanent link")
Bases: `BaseModelWithConfig[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.BaseModelWithConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseModelWithConfig</span> \(<code>fastapi.openapi.models.BaseModelWithConfig</code>\)")`
####  implicit `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlows.implicit "Permanent link")
```
implicit = None

```

####  password `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlows.password "Permanent link")
```
password = None

```

####  clientCredentials `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlows.clientCredentials "Permanent link")
```
clientCredentials = None

```

####  authorizationCode `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlows.authorizationCode "Permanent link")
```
authorizationCode = None

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlows.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

###  OAuth2 [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuth2 "Permanent link")
Bases: `SecurityBase[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.SecurityBase "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">SecurityBase</span> \(<code>fastapi.openapi.models.SecurityBase</code>\)")`
####  type_ `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuth2.type_ "Permanent link")
```
type_ = Field(default=oauth2[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.SecuritySchemeType.oauth2 "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">oauth2</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span> \(<code>fastapi.openapi.models.SecuritySchemeType.oauth2</code>\)"), alias='type')

```

####  flows `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuth2.flows "Permanent link")
```
flows

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuth2.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

####  description `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuth2.description "Permanent link")
```
description = None

```

###  OpenIdConnect [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OpenIdConnect "Permanent link")
Bases: `SecurityBase[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.SecurityBase "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">SecurityBase</span> \(<code>fastapi.openapi.models.SecurityBase</code>\)")`
####  type_ `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OpenIdConnect.type_ "Permanent link")
```
type_ = Field(default=openIdConnect[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.SecuritySchemeType.openIdConnect "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">openIdConnect</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span> \(<code>fastapi.openapi.models.SecuritySchemeType.openIdConnect</code>\)"), alias='type')

```

####  openIdConnectUrl `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OpenIdConnect.openIdConnectUrl "Permanent link")
```
openIdConnectUrl

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OpenIdConnect.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

####  description `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OpenIdConnect.description "Permanent link")
```
description = None

```

###  Components [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Components "Permanent link")
Bases: `BaseModelWithConfig[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.BaseModelWithConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseModelWithConfig</span> \(<code>fastapi.openapi.models.BaseModelWithConfig</code>\)")`
####  schemas `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Components.schemas "Permanent link")
```
schemas = None

```

####  responses `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Components.responses "Permanent link")
```
responses = None

```

####  parameters `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Components.parameters "Permanent link")
```
parameters = None

```

####  examples `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Components.examples "Permanent link")
```
examples = None

```

####  requestBodies `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Components.requestBodies "Permanent link")
```
requestBodies = None

```

####  headers `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Components.headers "Permanent link")
```
headers = None

```

####  securitySchemes `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Components.securitySchemes "Permanent link")
```
securitySchemes = None

```

####  links `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Components.links "Permanent link")
```
links = None

```

####  callbacks `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Components.callbacks "Permanent link")
```
callbacks = None

```

####  pathItems `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Components.pathItems "Permanent link")
```
pathItems = None

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Components.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

###  Tag [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Tag "Permanent link")
Bases: `BaseModelWithConfig[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.BaseModelWithConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseModelWithConfig</span> \(<code>fastapi.openapi.models.BaseModelWithConfig</code>\)")`
####  name `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Tag.name "Permanent link")
```
name

```

####  description `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Tag.description "Permanent link")
```
description = None

```

####  externalDocs `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Tag.externalDocs "Permanent link")
```
externalDocs = None

```

####  model_config `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Tag.model_config "Permanent link")
```
model_config = {'extra': 'allow'}

```

###  OpenAPI [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OpenAPI "Permanent link")
Bases: `BaseModelWithConfig[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.BaseModelWithConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseModelWithConfig</span> \(<code>fastapi.openapi.models.BaseModelWithConfig</code>\)")`
####  openapi `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OpenAPI.openapi "Permanent link")
