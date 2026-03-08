##  `union_tag_not_found`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#union_tag_not_found)
This error is raised when it is not possible to extract a discriminator value from the input:
[Python 3.9 and above](https://docs.pydantic.dev/latest/errors/validation_errors/#__tabbed_3_1)[Python 3.10 and above](https://docs.pydantic.dev/latest/errors/validation_errors/#__tabbed_3_2)
```
from typing import Literal, Union

from pydantic import BaseModel, Field, ValidationError


class BlackCat(BaseModel):
    pet_type: Literal['blackcat']


class WhiteCat(BaseModel):
    pet_type: Literal['whitecat']


class Model(BaseModel):
    cat: Union[BlackCat, WhiteCat] = Field(discriminator='pet_type')


try:
    Model(cat={'name': 'blackcat'})
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'union_tag_not_found'

```

```
from typing import Literal

from pydantic import BaseModel, Field, ValidationError


class BlackCat(BaseModel):
    pet_type: Literal['blackcat']


class WhiteCat(BaseModel):
    pet_type: Literal['whitecat']


class Model(BaseModel):
    cat: BlackCat | WhiteCat = Field(discriminator='pet_type')


try:
    Model(cat={'name': 'blackcat'})
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'union_tag_not_found'

```
