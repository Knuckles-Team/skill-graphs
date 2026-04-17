##  `union_tag_invalid`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#union_tag_invalid)
This error is raised when the input's discriminator is not one of the expected values:
[Python 3.9 and above](https://docs.pydantic.dev/latest/errors/validation_errors/#__tabbed_2_1)[Python 3.10 and above](https://docs.pydantic.dev/latest/errors/validation_errors/#__tabbed_2_2)
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
    Model(cat={'pet_type': 'dog'})
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'union_tag_invalid'

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
    Model(cat={'pet_type': 'dog'})
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'union_tag_invalid'

```
