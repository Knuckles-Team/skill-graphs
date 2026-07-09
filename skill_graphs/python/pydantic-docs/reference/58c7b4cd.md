# note: this will not work!
class ImportThingsMissingValidateDefault(BaseModel):
    obj: ImportString = 'math.cos'

my_cos_default3 = ImportThingsMissingValidateDefault()
assert my_cos_default3.obj == 'math.cos'  # just string, not evaluated

```

Serializing an `ImportString` type to json is also possible.
```
from pydantic import BaseModel, ImportString

class ImportThings(BaseModel):
    obj: ImportString
