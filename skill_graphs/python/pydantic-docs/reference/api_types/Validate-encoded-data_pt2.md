    belongs to, while still seeing all the performance benefits of a discriminated union.

    Consider this example, which is much more performant with the use of `Discriminator` and thus a `TaggedUnion`
    than it would be as a normal `Union`.

```python
    from typing import Annotated, Any, Literal, Union

    from pydantic import BaseModel, Discriminator, Tag

    class Pie(BaseModel):
        time_to_cook: int
        num_ingredients: int

    class ApplePie(Pie):
        fruit: Literal['apple'] = 'apple'

    class PumpkinPie(Pie):
        filling: Literal['pumpkin'] = 'pumpkin'

    def get_discriminator_value(v: Any) -> str:
        if isinstance(v, dict):
            return v.get('fruit', v.get('filling'))
        return getattr(v, 'fruit', getattr(v, 'filling', None))

    class ThanksgivingDinner(BaseModel):
        dessert: Annotated[
            Union[
                Annotated[ApplePie, Tag('apple')],
                Annotated[PumpkinPie, Tag('pumpkin')],
            ],
            Discriminator(get_discriminator_value),
        ]

    apple_variation = ThanksgivingDinner.model_validate(
        {'dessert': {'fruit': 'apple', 'time_to_cook': 60, 'num_ingredients': 8}}
    )
    print(repr(apple_variation))
    '''
    ThanksgivingDinner(dessert=ApplePie(time_to_cook=60, num_ingredients=8, fruit='apple'))
    '''

    pumpkin_variation = ThanksgivingDinner.model_validate(
        {
            'dessert': {
                'filling': 'pumpkin',
                'time_to_cook': 40,
                'num_ingredients': 6,
            }
        }
    )
    print(repr(pumpkin_variation))
    '''
    ThanksgivingDinner(dessert=PumpkinPie(time_to_cook=40, num_ingredients=6, filling='pumpkin'))
    '''
```

    See the [Discriminated Unions] concepts docs for more details on how to use `Discriminator`s.

    [Discriminated Unions]: ../concepts/unions.md#discriminated-unions
    """

    discriminator: str | Callable[[Any], Hashable]
    """The callable or field name for discriminating the type in a tagged union.

    A `Callable` discriminator must extract the value of the discriminator from the input.
    A `str` discriminator must be the name of a field to discriminate against.
    """
    custom_error_type: str | None = None
    """Type to use in [custom errors](../errors/errors.md) replacing the standard discriminated union
    validation errors.
    """
    custom_error_message: str | None = None
    """Message to use in custom errors."""
    custom_error_context: dict[str, int | str | float] | None = None
    """Context to use in custom errors."""

    def __get_pydantic_core_schema__(self, source_type: Any, handler: GetCoreSchemaHandler) -> CoreSchema:
        if not is_union_origin(get_origin(source_type)):
            raise TypeError(f'{type(self).__name__} must be used with a Union type, not {source_type}')

        if isinstance(self.discriminator, str):
            from pydantic import Field

            return handler(Annotated[source_type, Field(discriminator=self.discriminator)])
        else:
            original_schema = handler(source_type)
            return self._convert_schema(original_schema, handler)

    def _convert_schema(
        self, original_schema: core_schema.CoreSchema, handler: GetCoreSchemaHandler | None = None
    ) -> core_schema.TaggedUnionSchema:
        if original_schema['type'] != 'union':
            # This likely indicates that the schema was a single-item union that was simplified.
            # In this case, we do the same thing we do in
            # `pydantic._internal._discriminated_union._ApplyInferredDiscriminator._apply_to_root`, namely,
            # package the generated schema back into a single-item union.
            original_schema = core_schema.union_schema([original_schema])

        tagged_union_choices = {}
        for choice in original_schema['choices']:
            tag = None
            if isinstance(choice, tuple):
                choice, tag = choice
            metadata = cast('CoreMetadata | None', choice.get('metadata'))
            if metadata is not None:
                tag = metadata.get('pydantic_internal_union_tag_key') or tag
            if tag is None:
                # `handler` is None when this method is called from `apply_discriminator()` (deferred discriminators)
                if handler is not None and choice['type'] == 'definition-ref':
                    # If choice was built from a PEP 695 type alias, try to resolve the def:
                    try:
                        choice = handler.resolve_ref_schema(choice)
                    except LookupError:
                        pass
                    else:
                        metadata = cast('CoreMetadata | None', choice.get('metadata'))
                        if metadata is not None:
                            tag = metadata.get('pydantic_internal_union_tag_key')

                if tag is None:
                    raise PydanticUserError(
                        f'`Tag` not provided for choice {choice} used with `Discriminator`',
                        code='callable-discriminator-no-tag',
                    )
            tagged_union_choices[tag] = choice

        # Have to do these verbose checks to ensure falsy values ('' and {}) don't get ignored
        custom_error_type = self.custom_error_type
        if custom_error_type is None:
            custom_error_type = original_schema.get('custom_error_type')

        custom_error_message = self.custom_error_message
        if custom_error_message is None:
            custom_error_message = original_schema.get('custom_error_message')

        custom_error_context = self.custom_error_context
        if custom_error_context is None:
            custom_error_context = original_schema.get('custom_error_context')

        custom_error_type = original_schema.get('custom_error_type') if custom_error_type is None else custom_error_type
        return core_schema.tagged_union_schema(
            tagged_union_choices,
            self.discriminator,
            custom_error_type=custom_error_type,
            custom_error_message=custom_error_message,
            custom_error_context=custom_error_context,
            strict=original_schema.get('strict'),
            ref=original_schema.get('ref'),
            metadata=original_schema.get('metadata'),
            serialization=original_schema.get('serialization'),
        )

```

---|---
####  discriminator `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator.discriminator)
```
discriminator:  | [[], ]

```

The callable or field name for discriminating the type in a tagged union.
A `Callable` discriminator must extract the value of the discriminator from the input. A `str` discriminator must be the name of a field to discriminate against.
####  custom_error_type `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator.custom_error_type)
```
custom_error_type:  | None = None

```

Type to use in [custom errors](https://docs.pydantic.dev/latest/errors/errors/) replacing the standard discriminated union validation errors.
####  custom_error_message `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator.custom_error_message)
```
custom_error_message:  | None = None

```

Message to use in custom errors.
####  custom_error_context `class-attribute` `instance-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator.custom_error_context)
```
custom_error_context: (
    [,  |  | ] | None
) = None

```

Context to use in custom errors.
###  FailFast `dataclass` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.FailFast)
Bases: `PydanticMetadata`, `BaseMetadata`
A `FailFast` annotation can be used to specify that validation should stop at the first error.
This can be useful when you want to validate a large amount of data and you only need to know if it's valid or not.
You might want to enable this setting if you want to validate your data faster (basically, if you use this, validation will be more performant with the caveat that you get less information).
```
from typing import Annotated

from pydantic import BaseModel, FailFast, ValidationError

class Model(BaseModel):
    x: Annotated[list[int], FailFast()]

# This will raise a single error for the first invalid value and stop validation
try:
    obj = Model(x=[1, 2, 'a', 4, 5, 'b', 7, 8, 9, 'c'])
except ValidationError as e:
    print(e)
    '''
    1 validation error for Model
    x.2
      Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='a', input_type=str]
    '''

```

Source code in `pydantic/types.py`
```
3265
3266
3267
3268
3269
3270
3271
3272
3273
3274
3275
3276
3277
3278
3279
3280
3281
3282
3283
3284
3285
3286
3287
3288
3289
3290
3291
3292
3293
3294
3295
```
| ```
@_dataclasses.dataclass
class FailFast(_fields.PydanticMetadata, BaseMetadata):
    """A `FailFast` annotation can be used to specify that validation should stop at the first error.

    This can be useful when you want to validate a large amount of data and you only need to know if it's valid or not.

    You might want to enable this setting if you want to validate your data faster (basically, if you use this,
    validation will be more performant with the caveat that you get less information).

```python
    from typing import Annotated

    from pydantic import BaseModel, FailFast, ValidationError

    class Model(BaseModel):
        x: Annotated[list[int], FailFast()]

    # This will raise a single error for the first invalid value and stop validation
    try:
        obj = Model(x=[1, 2, 'a', 4, 5, 'b', 7, 8, 9, 'c'])
    except ValidationError as e:
        print(e)
        '''
        1 validation error for Model
        x.2
          Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='a', input_type=str]
        '''
```
    """

    fail_fast: bool = True

```

---|---
###  conint [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.conint)
```
conint(
    *,
    strict:  | None = None,
    gt:  | None = None,
    ge:  | None = None,
    lt:  | None = None,
    le:  | None = None,
    multiple_of:  | None = None
) -> []

```

Discouraged
This function is **discouraged** in favor of using [`Field`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) instead.
This function will be **deprecated** in Pydantic 3.0.
The reason is that `conint` returns a type, which doesn't play well with static analysis tools.
[![❌](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/274c.svg) Don't do this](https://docs.pydantic.dev/latest/api/types/#pydantic.types.conint--__tabbed_1_1)[![✅](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/2705.svg) Do this](https://docs.pydantic.dev/latest/api/types/#pydantic.types.conint--__tabbed_1_2)
```
from pydantic import BaseModel, conint

class Foo(BaseModel):
    bar: conint(strict=True, gt=0)

```

```
from typing import Annotated

from pydantic import BaseModel, Field

class Foo(BaseModel):
    bar: Annotated[int, Field(strict=True, gt=0)]

```

A wrapper around `int` that allows for additional constraints.
Parameters:
Name | Type | Description | Default
---|---|---|---
`strict` |  |  Whether to validate the integer in strict mode. Defaults to `None`. |  `None`
`gt` |  |  The value must be greater than this. |  `None`
`ge` |  |  The value must be greater than or equal to this. |  `None`
`lt` |  |  The value must be less than this. |  `None`
`le` |  |  The value must be less than or equal to this. |  `None`
`multiple_of` |  |  The value must be a multiple of this. |  `None`
Returns:
Type | Description
---|---
|  The wrapped integer type.
```
from pydantic import BaseModel, ValidationError, conint

class ConstrainedExample(BaseModel):
    constrained_int: conint(gt=1)

m = ConstrainedExample(constrained_int=2)
print(repr(m))
#> ConstrainedExample(constrained_int=2)

try:
    ConstrainedExample(constrained_int=0)
except ValidationError as e:
    print(e.errors())
    '''
    [
        {
            'type': 'greater_than',
            'loc': ('constrained_int',),
            'msg': 'Input should be greater than 1',
            'input': 0,
            'ctx': {'gt': 1},
            'url': 'https://errors.pydantic.dev/2/v/greater_than',
        }
    ]
    '''

```

Source code in `pydantic/types.py`
```
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
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
```
| ```
def conint(
    *,
    strict: bool | None = None,
    gt: int | None = None,
    ge: int | None = None,
    lt: int | None = None,
    le: int | None = None,
    multiple_of: int | None = None,
) -> type[int]:
    """
    !!! warning "Discouraged"
        This function is **discouraged** in favor of using
        [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated) with
        [`Field`][pydantic.fields.Field] instead.

        This function will be **deprecated** in Pydantic 3.0.

        The reason is that `conint` returns a type, which doesn't play well with static analysis tools.

        === ":x: Don't do this"
        ```python
            from pydantic import BaseModel, conint

            class Foo(BaseModel):
                bar: conint(strict=True, gt=0)
        ```

        === ":white_check_mark: Do this"
        ```python
            from typing import Annotated

            from pydantic import BaseModel, Field

            class Foo(BaseModel):
                bar: Annotated[int, Field(strict=True, gt=0)]
        ```

    A wrapper around `int` that allows for additional constraints.

    Args:
        strict: Whether to validate the integer in strict mode. Defaults to `None`.
        gt: The value must be greater than this.
        ge: The value must be greater than or equal to this.
        lt: The value must be less than this.
        le: The value must be less than or equal to this.
        multiple_of: The value must be a multiple of this.

    Returns:
        The wrapped integer type.

```python
    from pydantic import BaseModel, ValidationError, conint

    class ConstrainedExample(BaseModel):
        constrained_int: conint(gt=1)

    m = ConstrainedExample(constrained_int=2)
    print(repr(m))
    #> ConstrainedExample(constrained_int=2)

    try:
        ConstrainedExample(constrained_int=0)
    except ValidationError as e:
        print(e.errors())
        '''
        [
            {
                'type': 'greater_than',
                'loc': ('constrained_int',),
                'msg': 'Input should be greater than 1',
                'input': 0,
                'ctx': {'gt': 1},
                'url': 'https://errors.pydantic.dev/2/v/greater_than',
            }
        ]
        '''
```

    """  # noqa: D212
    return Annotated[  # pyright: ignore[reportReturnType]
        int,
        Strict(strict) if strict is not None else None,
        annotated_types.Interval(gt=gt, ge=ge, lt=lt, le=le),
        annotated_types.MultipleOf(multiple_of) if multiple_of is not None else None,
    ]

```

---|---
###  confloat [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.confloat)
```
confloat(
    *,
    strict:  | None = None,
    gt:  | None = None,
    ge:  | None = None,
    lt:  | None = None,
    le:  | None = None,
    multiple_of:  | None = None,
    allow_inf_nan:  | None = None
) -> []

```

Discouraged
This function is **discouraged** in favor of using [`Field`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) instead.
This function will be **deprecated** in Pydantic 3.0.
The reason is that `confloat` returns a type, which doesn't play well with static analysis tools.
[![❌](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/274c.svg) Don't do this](https://docs.pydantic.dev/latest/api/types/#pydantic.types.confloat--__tabbed_1_1)[![✅](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/2705.svg) Do this](https://docs.pydantic.dev/latest/api/types/#pydantic.types.confloat--__tabbed_1_2)
```
from pydantic import BaseModel, confloat

class Foo(BaseModel):
    bar: confloat(strict=True, gt=0)

```

```
from typing import Annotated

from pydantic import BaseModel, Field

class Foo(BaseModel):
    bar: Annotated[float, Field(strict=True, gt=0)]

```

A wrapper around `float` that allows for additional constraints.
Parameters:
Name | Type | Description | Default
---|---|---|---
`strict` |  |  Whether to validate the float in strict mode. |  `None`
`gt` |  |  The value must be greater than this. |  `None`
`ge` |  |  The value must be greater than or equal to this. |  `None`
`lt` |  |  The value must be less than this. |  `None`
`le` |  |  The value must be less than or equal to this. |  `None`
`multiple_of` |  |  The value must be a multiple of this. |  `None`
`allow_inf_nan` |  |  Whether to allow `-inf`, `inf`, and `nan`. |  `None`
Returns:
Type | Description
---|---
|  The wrapped float type.
```
from pydantic import BaseModel, ValidationError, confloat

class ConstrainedExample(BaseModel):
    constrained_float: confloat(gt=1.0)

m = ConstrainedExample(constrained_float=1.1)
print(repr(m))
#> ConstrainedExample(constrained_float=1.1)

try:
    ConstrainedExample(constrained_float=0.9)
except ValidationError as e:
    print(e.errors())
    '''
    [
        {
            'type': 'greater_than',
            'loc': ('constrained_float',),
            'msg': 'Input should be greater than 1',
            'input': 0.9,
            'ctx': {'gt': 1.0},
            'url': 'https://errors.pydantic.dev/2/v/greater_than',
        }
    ]
    '''

```

Source code in `pydantic/types.py`
```
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
```
| ```
def confloat(
    *,
    strict: bool | None = None,
    gt: float | None = None,
    ge: float | None = None,
    lt: float | None = None,
    le: float | None = None,
    multiple_of: float | None = None,
    allow_inf_nan: bool | None = None,
) -> type[float]:
    """
    !!! warning "Discouraged"
        This function is **discouraged** in favor of using
        [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated) with
        [`Field`][pydantic.fields.Field] instead.

        This function will be **deprecated** in Pydantic 3.0.

        The reason is that `confloat` returns a type, which doesn't play well with static analysis tools.

        === ":x: Don't do this"
        ```python
            from pydantic import BaseModel, confloat

            class Foo(BaseModel):
                bar: confloat(strict=True, gt=0)
        ```

        === ":white_check_mark: Do this"
        ```python
            from typing import Annotated

            from pydantic import BaseModel, Field

            class Foo(BaseModel):
                bar: Annotated[float, Field(strict=True, gt=0)]
        ```

    A wrapper around `float` that allows for additional constraints.

    Args:
        strict: Whether to validate the float in strict mode.
        gt: The value must be greater than this.
        ge: The value must be greater than or equal to this.
        lt: The value must be less than this.
        le: The value must be less than or equal to this.
        multiple_of: The value must be a multiple of this.
        allow_inf_nan: Whether to allow `-inf`, `inf`, and `nan`.

    Returns:
        The wrapped float type.

```python
    from pydantic import BaseModel, ValidationError, confloat

    class ConstrainedExample(BaseModel):
        constrained_float: confloat(gt=1.0)

    m = ConstrainedExample(constrained_float=1.1)
    print(repr(m))
    #> ConstrainedExample(constrained_float=1.1)

    try:
        ConstrainedExample(constrained_float=0.9)
    except ValidationError as e:
        print(e.errors())
        '''
        [
            {
                'type': 'greater_than',
                'loc': ('constrained_float',),
                'msg': 'Input should be greater than 1',
                'input': 0.9,
                'ctx': {'gt': 1.0},
                'url': 'https://errors.pydantic.dev/2/v/greater_than',
            }
        ]
        '''
```
    """  # noqa: D212
    return Annotated[  # pyright: ignore[reportReturnType]
        float,
        Strict(strict) if strict is not None else None,
        annotated_types.Interval(gt=gt, ge=ge, lt=lt, le=le),
        annotated_types.MultipleOf(multiple_of) if multiple_of is not None else None,
        AllowInfNan(allow_inf_nan) if allow_inf_nan is not None else None,
    ]

```

---|---
###  conbytes [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.conbytes)
```
conbytes(
    *,
    min_length:  | None = None,
    max_length:  | None = None,
    strict:  | None = None
) -> []

```

A wrapper around `bytes` that allows for additional constraints.
Parameters:
Name | Type | Description | Default
---|---|---|---
`min_length` |  |  The minimum length of the bytes. |  `None`
`max_length` |  |  The maximum length of the bytes. |  `None`
`strict` |  |  Whether to validate the bytes in strict mode. |  `None`
Returns:
Type | Description
---|---
|  The wrapped bytes type.
Source code in `pydantic/types.py`
```
663
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
```
| ```
def conbytes(
    *,
    min_length: int | None = None,
    max_length: int | None = None,
    strict: bool | None = None,
) -> type[bytes]:
    """A wrapper around `bytes` that allows for additional constraints.

    Args:
        min_length: The minimum length of the bytes.
        max_length: The maximum length of the bytes.
        strict: Whether to validate the bytes in strict mode.

    Returns:
        The wrapped bytes type.
    """
    return Annotated[  # pyright: ignore[reportReturnType]
        bytes,
        Strict(strict) if strict is not None else None,
        annotated_types.Len(min_length or 0, max_length),
    ]

```

---|---
###  constr [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.constr)
```
constr(
    *,
    strip_whitespace:  | None = None,
    to_upper:  | None = None,
    to_lower:  | None = None,
    strict:  | None = None,
    min_length:  | None = None,
    max_length:  | None = None,
    pattern:  | [] | None = None
) -> []

```

Discouraged
This function is **discouraged** in favor of using [`StringConstraints`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StringConstraints) instead.
This function will be **deprecated** in Pydantic 3.0.
The reason is that `constr` returns a type, which doesn't play well with static analysis tools.
[![❌](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/274c.svg) Don't do this](https://docs.pydantic.dev/latest/api/types/#pydantic.types.constr--__tabbed_1_1)[![✅](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/2705.svg) Do this](https://docs.pydantic.dev/latest/api/types/#pydantic.types.constr--__tabbed_1_2)
```
from pydantic import BaseModel, constr

class Foo(BaseModel):
    bar: constr(strip_whitespace=True, to_upper=True, pattern=r'^[A-Z]+$')

```

```
from typing import Annotated

from pydantic import BaseModel, StringConstraints

class Foo(BaseModel):
    bar: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True, to_upper=True, pattern=r'^[A-Z]+$'
        ),
    ]

```

A wrapper around `str` that allows for additional constraints.
```
from pydantic import BaseModel, constr

class Foo(BaseModel):
    bar: constr(strip_whitespace=True, to_upper=True)

foo = Foo(bar='  hello  ')
print(foo)
#> bar='HELLO'

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`strip_whitespace` |  |  Whether to remove leading and trailing whitespace. |  `None`
`to_upper` |  |  Whether to turn all characters to uppercase. |  `None`
`to_lower` |  |  Whether to turn all characters to lowercase. |  `None`
`strict` |  |  Whether to validate the string in strict mode. |  `None`
`min_length` |  |  The minimum length of the string. |  `None`
`max_length` |  |  The maximum length of the string. |  `None`
`pattern` |  |  A regex pattern to validate the string against. |  `None`
Returns:
Type | Description
---|---
|  The wrapped string type.
Source code in `pydantic/types.py`
```
749
750
751
752
753
754
755
756
757
758
759
760
761
762
763
764
765
766
767
768
769
770
771
772
773
774
775
776
777
778
779
780
781
782
783
784
785
786
787
788
789
790
791
792
793
794
795
796
797
798
799
800
801
802
803
804
805
806
807
808
809
810
811
812
813
814
815
816
817
818
819
820
821
822
823
824
825
826
827
828
```
| ```
def constr(
    *,
    strip_whitespace: bool | None = None,
    to_upper: bool | None = None,
    to_lower: bool | None = None,
    strict: bool | None = None,
