## Continue using Pydantic V1 features[¶](https://docs.pydantic.dev/latest/migration/#continue-using-pydantic-v1-features)
Pydantic V1 is still available when you need it, though we recommend migrating to Pydantic V2 for its improvements and new features.
If you need to use latest Pydantic V1, you can install it with:
```
pip install "pydantic==1.*"

```

The Pydantic V2 package also continues to provide access to the Pydantic V1 API by importing through `pydantic.v1`.
For example, you can use the `BaseModel` class from Pydantic V1 instead of the Pydantic V2 `pydantic.BaseModel` class:
```
from pydantic.v1 import BaseModel

```

You can also import functions that have been removed from Pydantic V2, such as `lenient_isinstance`:
```
from pydantic.v1.utils import lenient_isinstance

```

Pydantic V1 documentation is available at <https://docs.pydantic.dev/1.10/>.
### Using Pydantic v1 features in a v1/v2 environment[¶](https://docs.pydantic.dev/latest/migration/#using-pydantic-v1-features-in-a-v1v2-environment)
As of `pydantic>=1.10.17`, the `pydantic.v1` namespace can be used within V1. This makes it easier to migrate to V2, which also supports the `pydantic.v1` namespace. In order to unpin a `pydantic<2` dependency and continue using V1 features, take the following steps:
  1. Replace `pydantic<2` with `pydantic>=1.10.17`
  2. Find and replace all occurrences of:


```
from pydantic.<module> import <object>

```

with:
```
from pydantic.v1.<module> import <object>

```

Here's how you can import `pydantic`'s v1 features based on your version of `pydantic`:
[`pydantic>=1.10.17,<3`](https://docs.pydantic.dev/latest/migration/#__tabbed_1_1)[`pydantic<3`](https://docs.pydantic.dev/latest/migration/#__tabbed_1_2)
As of `v1.10.17` the `.v1` namespace is available in V1, allowing imports as below:
```
from pydantic.v1.fields import ModelField

```

All versions of Pydantic V1 and V2 support the following import pattern, in case you don't know which version of Pydantic you are using:
```
try:
    from pydantic.v1.fields import ModelField
except ImportError:
    from pydantic.fields import ModelField

```

Note
When importing modules using `pydantic>=1.10.17,<2` with the `.v1` namespace these modules will _not_ be the **same** module as the same import without the `.v1` namespace, but the symbols imported _will_ be. For example `pydantic.v1.fields is not pydantic.fields` but `pydantic.v1.fields.ModelField is pydantic.fields.ModelField`. Luckily, this is not likely to be relevant in the vast majority of cases. It's just an unfortunate consequence of providing a smoother migration experience.
