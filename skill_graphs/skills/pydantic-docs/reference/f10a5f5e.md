## Validators and initialization hooks[¶](https://docs.pydantic.dev/latest/concepts/dataclasses/#validators-and-initialization-hooks)
Validators also work with Pydantic dataclasses:
```
from pydantic import field_validator
from pydantic.dataclasses import dataclass


@dataclass
class DemoDataclass:
    product_id: str  # should be a five-digit string, may have leading zeros

    @field_validator('product_id', mode='before')
    @classmethod
    def convert_int_serial(cls, v):
        if isinstance(v, int):
            v = str(v).zfill(5)
        return v


print(DemoDataclass(product_id='01234'))
#> DemoDataclass(product_id='01234')
print(DemoDataclass(product_id=2468))
#> DemoDataclass(product_id='02468')

```

The dataclass _before_ and _after_ model validators.
Example
```
from pydantic_core import ArgsKwargs
from typing_extensions import Self

from pydantic import model_validator
from pydantic.dataclasses import dataclass


@dataclass
class Birth:
    year: int
    month: int
    day: int


@dataclass
class User:
    birth: Birth

    @model_validator(mode='before')
    @classmethod
    def before(cls, values: ArgsKwargs) -> ArgsKwargs:
        print(f'First: {values}')  [](https://docs.pydantic.dev/latest/concepts/dataclasses/#__code_12_annotation_1)
        """
        First: ArgsKwargs((), {'birth': {'year': 1995, 'month': 3, 'day': 2}})
        """
        return values

    @model_validator(mode='after')
    def after(self) -> Self:
        print(f'Third: {self}')
        #> Third: User(birth=Birth(year=1995, month=3, day=2))
        return self

    def __post_init__(self):
        print(f'Second: {self.birth}')
        #> Second: Birth(year=1995, month=3, day=2)


user = User(**{'birth': {'year': 1995, 'month': 3, 'day': 2}})

```

Was this page helpful?
Thanks for your feedback!
Thanks for your feedback!
Made with
Bases: `T]`
Usage Documentation
[`TypeAdapter`](https://docs.pydantic.dev/latest/concepts/type_adapter/)
Type adapters provide a flexible way to perform validation and serialization based on a Python type.
A `TypeAdapter` instance exposes some of the functionality from `BaseModel` instance methods for types that do not have such methods (such as dataclasses, primitive types, and more).
**Note:** `TypeAdapter` instances are not types, and cannot be used as type annotations for fields.
Parameters:
Name | Type | Description | Default
---|---|---|---
`type` |  |  The type associated with the `TypeAdapter`. |  _required_
`config` |  `ConfigDict[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict "pydantic.config.ConfigDict") | None` |  Configuration for the `TypeAdapter`, should be a dictionary conforming to [`ConfigDict`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict). Note You cannot provide a configuration when instantiating a `TypeAdapter` if the type you're using has its own config that cannot be overridden (ex: `BaseModel`, `TypedDict`, and `dataclass`). A [`type-adapter-config-unused`](https://docs.pydantic.dev/latest/errors/usage_errors/#type-adapter-config-unused) error will be raised in this case. |  `None`
`_parent_depth` |  |  Depth at which to search for the `TypeAdapter` was instantiated. Note This parameter is named with an underscore to suggest its private nature and discourage use. It may be deprecated in a minor version, so we only recommend using it if you're comfortable with potential change in behavior/support. It's default value is 2 because internally, the `TypeAdapter` class makes another call to fetch the frame. |  `2`
`module` |  |  The module that passes to plugin if provided. |  `None`
Attributes:
Name | Type | Description
---|---|---
`core_schema` |  `CoreSchema` |  The core schema for the type.
`validator` |  `SchemaValidator[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaValidator "pydantic_core.SchemaValidator") | PluggableSchemaValidator` |  The schema validator for the type.
`serializer` |  `SchemaSerializer[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaSerializer "pydantic_core.SchemaSerializer")` |  The schema serializer for the type.
`pydantic_complete` |  |  Whether the core schema for the type is successfully built.
Compatibility with `mypy`
Depending on the type used, `mypy` might raise an error when instantiating a `TypeAdapter`. As a workaround, you can explicitly annotate your variable:
```
from typing import Union

from pydantic import TypeAdapter

ta: TypeAdapter[Union[str, int]] = TypeAdapter(Union[str, int])  # type: ignore[arg-type]

```

Namespace management nuances and implementation details
Here, we collect some notes on namespace management, and subtle differences from `BaseModel`:
`BaseModel` uses its own `__module__` to find out where it was defined and then looks for symbols to resolve forward references in those globals. On the other hand, `TypeAdapter` can be initialized with arbitrary objects, which may not be types and thus do not have a `__module__` available. So instead we look at the globals in our parent stack frame.
It is expected that the `ns_resolver` passed to this function will have the correct namespace for the type we're adapting. See the source code for `TypeAdapter.__init__` and `TypeAdapter.rebuild` for various ways to construct this namespace.
This works for the case where this function is called in a module that has the target of forward references in its scope, but does not always work for more complex cases.
For example, take the following:
a.py```
IntList = list[int]
OuterDict = dict[str, 'IntList']

```

b.py```
from a import OuterDict

from pydantic import TypeAdapter

IntList = int  # replaces the symbol the forward reference is looking for
v = TypeAdapter(OuterDict)
v({'x': 1})  # should fail but doesn't

```

If `OuterDict` were a `BaseModel`, this would work because it would resolve the forward reference within the `a.py` namespace. But `TypeAdapter(OuterDict)` can't determine what module `OuterDict` came from.
In other words, the assumption that _all_ forward references exist in the module we are being called from is not technically always true. Although most of the time it is and it works fine for recursive models and such, `BaseModel`'s behavior isn't perfect either and _can_ break in similar ways, so there is no right or wrong between the two.
But at the very least this behavior is _subtly_ different from `BaseModel`'s.
Source code in `pydantic/type_adapter.py`
```
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
```
| ```
def __init__(
    self,
    type: Any,
    *,
    config: ConfigDict | None = None,
    _parent_depth: int = 2,
    module: str | None = None,
) -> None:
    if _type_has_config(type) and config is not None:
        raise PydanticUserError(
            'Cannot use `config` when the type is a BaseModel, dataclass or TypedDict.'
            ' These types can have their own config and setting the config via the `config`'
            ' parameter to TypeAdapter will not override it, thus the `config` you passed to'
            ' TypeAdapter becomes meaningless, which is probably not what you want.',
            code='type-adapter-config-unused',
        )

    self._type = type
    self._config = config
    self._parent_depth = _parent_depth
    self.pydantic_complete = False

    parent_frame = self._fetch_parent_frame()
    if isinstance(type, types.FunctionType):
        # Special case functions, which are *not* pushed to the `NsResolver` stack and without this special case
        # would only have access to the parent namespace where the `TypeAdapter` was instantiated (if the function is defined
        # in another module, we need to look at that module's globals).
        if parent_frame is not None:
            # `f_locals` is the namespace where the type adapter was instantiated (~ to `f_globals` if at the module level):
            parent_ns = parent_frame.f_locals
        else:  # pragma: no cover
            parent_ns = None
        globalns, localns = _namespace_utils.ns_for_function(
            type,
            parent_namespace=parent_ns,
        )
        parent_namespace = None
    else:
        if parent_frame is not None:
            globalns = parent_frame.f_globals
            # Do not provide a local ns if the type adapter happens to be instantiated at the module level:
            localns = parent_frame.f_locals if parent_frame.f_locals is not globalns else {}
        else:  # pragma: no cover
            globalns = {}
            localns = {}
        parent_namespace = localns

    self._module_name = module or cast(str, globalns.get('__name__', ''))
    self._init_core_attrs(
        ns_resolver=_namespace_utils.NsResolver(
            namespaces_tuple=_namespace_utils.NamespacesTuple(locals=localns, globals=globalns),
            parent_namespace=parent_namespace,
        ),
        force=False,
    )

```

---|---
##  rebuild [¶](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter.rebuild "Permanent link")
```
rebuild(
    *,
    force:  = False,
    raise_errors:  = True,
    _parent_namespace_depth:  = 2,
    _types_namespace: MappingNamespace | None = None
) ->  | None

```

Try to rebuild the pydantic-core schema for the adapter's type.
This may be necessary when one of the annotations is a ForwardRef which could not be resolved during the initial attempt to build the schema, and automatic rebuilding fails.
Parameters:
Name | Type | Description | Default
---|---|---|---
`force` |  |  Whether to force the rebuilding of the type adapter's schema, defaults to `False`. |  `False`
`raise_errors` |  |  Whether to raise errors, defaults to `True`. |  `True`
`_parent_namespace_depth` |  |  Depth at which to search for the  |  `2`
`_types_namespace` |  `MappingNamespace | None` |  An explicit types namespace to use, instead of using the local namespace from the parent frame. Defaults to `None`. |  `None`
Returns:
Type | Description
---|---
|  Returns `None` if the schema is already "complete" and rebuilding was not required.
|  If rebuilding _was_ required, returns `True` if rebuilding was successful, otherwise `False`.
Source code in `pydantic/type_adapter.py`
```
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
```
| ```
def rebuild(
    self,
    *,
    force: bool = False,
    raise_errors: bool = True,
    _parent_namespace_depth: int = 2,
    _types_namespace: _namespace_utils.MappingNamespace | None = None,
) -> bool | None:
    """Try to rebuild the pydantic-core schema for the adapter's type.

    This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
    the initial attempt to build the schema, and automatic rebuilding fails.

    Args:
        force: Whether to force the rebuilding of the type adapter's schema, defaults to `False`.
        raise_errors: Whether to raise errors, defaults to `True`.
        _parent_namespace_depth: Depth at which to search for the [parent frame][frame-objects]. This
            frame is used when resolving forward annotations during schema rebuilding, by looking for
            the locals of this frame. Defaults to 2, which will result in the frame where the method
            was called.
        _types_namespace: An explicit types namespace to use, instead of using the local namespace
            from the parent frame. Defaults to `None`.

    Returns:
        Returns `None` if the schema is already "complete" and rebuilding was not required.
        If rebuilding _was_ required, returns `True` if rebuilding was successful, otherwise `False`.
    """
    if not force and self.pydantic_complete:
        return None

    if _types_namespace is not None:
        rebuild_ns = _types_namespace
    elif _parent_namespace_depth > 0:
        rebuild_ns = _typing_extra.parent_frame_namespace(parent_depth=_parent_namespace_depth, force=True) or {}
    else:
        rebuild_ns = {}

    # we have to manually fetch globals here because there's no type on the stack of the NsResolver
    # and so we skip the globalns = get_module_ns_of(typ) call that would normally happen
    globalns = sys._getframe(max(_parent_namespace_depth - 1, 1)).f_globals
    ns_resolver = _namespace_utils.NsResolver(
        namespaces_tuple=_namespace_utils.NamespacesTuple(locals=rebuild_ns, globals=globalns),
        parent_namespace=rebuild_ns,
    )
    return self._init_core_attrs(ns_resolver=ns_resolver, force=True, raise_errors=raise_errors)

```

---|---
