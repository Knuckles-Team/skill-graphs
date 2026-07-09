# Validate encoded data
try:
    Model(my_encoded_bytes=b'**undecodable**')
except ValidationError as e:
    print(e)
    '''
    1 validation error for Model
    my_encoded_bytes
      Value error, Cannot decode data [type=value_error, input_value=b'**undecodable**', input_type=bytes]
    '''

```

Source code in `pydantic/types.py`
```
2471
2472
2473
2474
2475
2476
2477
2478
2479
2480
2481
2482
2483
2484
2485
2486
2487
2488
2489
2490
2491
2492
2493
2494
2495
2496
2497
2498
2499
2500
2501
2502
2503
2504
2505
2506
2507
2508
2509
2510
2511
2512
2513
2514
2515
2516
2517
2518
2519
2520
2521
2522
2523
2524
2525
2526
2527
2528
2529
2530
2531
2532
2533
2534
2535
2536
2537
2538
2539
2540
2541
2542
2543
2544
2545
2546
2547
2548
2549
2550
2551
2552
2553
2554
2555
2556
2557
2558
2559
2560
2561
2562
2563
2564
2565
2566
2567
```
| ```
@_dataclasses.dataclass(**_internal_dataclass.slots_true)
class EncodedBytes:
    """A bytes type that is encoded and decoded using the specified encoder.

    `EncodedBytes` needs an encoder that implements `EncoderProtocol` to operate.

```python
    from typing import Annotated

    from pydantic import BaseModel, EncodedBytes, EncoderProtocol, ValidationError

    class MyEncoder(EncoderProtocol):
        @classmethod
        def decode(cls, data: bytes) -> bytes:
            if data == b'**undecodable**':
                raise ValueError('Cannot decode data')
            return data[13:]

        @classmethod
        def encode(cls, value: bytes) -> bytes:
            return b'**encoded**: ' + value

        @classmethod
        def get_json_format(cls) -> str:
            return 'my-encoder'

    MyEncodedBytes = Annotated[bytes, EncodedBytes(encoder=MyEncoder)]

    class Model(BaseModel):
        my_encoded_bytes: MyEncodedBytes

    # Initialize the model with encoded data
    m = Model(my_encoded_bytes=b'**encoded**: some bytes')

    # Access decoded value
    print(m.my_encoded_bytes)
    #> b'some bytes'

    # Serialize into the encoded form
    print(m.model_dump())
    #> {'my_encoded_bytes': b'**encoded**: some bytes'}

    # Validate encoded data
    try:
        Model(my_encoded_bytes=b'**undecodable**')
    except ValidationError as e:
        print(e)
        '''
        1 validation error for Model
        my_encoded_bytes
          Value error, Cannot decode data [type=value_error, input_value=b'**undecodable**', input_type=bytes]
        '''
```
    """

    encoder: type[EncoderProtocol]

    def __get_pydantic_json_schema__(
        self, core_schema: core_schema.CoreSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        field_schema = handler(core_schema)
        field_schema.update(type='string', format=self.encoder.get_json_format())
        return field_schema

    def __get_pydantic_core_schema__(self, source: type[Any], handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        schema = handler(source)
        _check_annotated_type(schema['type'], 'bytes', self.__class__.__name__)
        return core_schema.with_info_after_validator_function(
            function=self.decode,
            schema=schema,
            serialization=core_schema.plain_serializer_function_ser_schema(function=self.encode),
        )

    def decode(self, data: bytes, _: core_schema.ValidationInfo) -> bytes:
        """Decode the data using the specified encoder.

        Args:
            data: The data to decode.

        Returns:
            The decoded data.
        """
        return self.encoder.decode(data)

    def encode(self, value: bytes) -> bytes:
        """Encode the data using the specified encoder.

        Args:
            value: The data to encode.

        Returns:
            The encoded data.
        """
        return self.encoder.encode(value)

    def __hash__(self) -> int:
        return hash(self.encoder)

```

---|---
####  decode [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncodedBytes.decode)
```
decode(data: , _: ValidationInfo[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo)) ->

```

Decode the data using the specified encoder.
Parameters:
Name | Type | Description | Default
---|---|---|---
`data` |  |  The data to decode. |  _required_
Returns:
Type | Description
---|---
|  The decoded data.
Source code in `pydantic/types.py`
```
2544
2545
2546
2547
2548
2549
2550
2551
2552
2553
```
| ```
def decode(self, data: bytes, _: core_schema.ValidationInfo) -> bytes:
    """Decode the data using the specified encoder.

    Args:
        data: The data to decode.

    Returns:
        The decoded data.
    """
    return self.encoder.decode(data)

```

---|---
####  encode [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncodedBytes.encode)
```
encode(value: ) ->

```

Encode the data using the specified encoder.
Parameters:
Name | Type | Description | Default
---|---|---|---
`value` |  |  The data to encode. |  _required_
Returns:
Type | Description
---|---
|  The encoded data.
Source code in `pydantic/types.py`
```
2555
2556
2557
2558
2559
2560
2561
2562
2563
2564
```
| ```
def encode(self, value: bytes) -> bytes:
    """Encode the data using the specified encoder.

    Args:
        value: The data to encode.

    Returns:
        The encoded data.
    """
    return self.encoder.encode(value)

```

---|---
###  EncodedStr `dataclass` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncodedStr)
A str type that is encoded and decoded using the specified encoder.
`EncodedStr` needs an encoder that implements `EncoderProtocol` to operate.
```
from typing import Annotated

from pydantic import BaseModel, EncodedStr, EncoderProtocol, ValidationError

class MyEncoder(EncoderProtocol):
    @classmethod
    def decode(cls, data: bytes) -> bytes:
        if data == b'**undecodable**':
            raise ValueError('Cannot decode data')
        return data[13:]

    @classmethod
    def encode(cls, value: bytes) -> bytes:
        return b'**encoded**: ' + value

    @classmethod
    def get_json_format(cls) -> str:
        return 'my-encoder'

MyEncodedStr = Annotated[str, EncodedStr(encoder=MyEncoder)]

class Model(BaseModel):
    my_encoded_str: MyEncodedStr

# Initialize the model with encoded data
m = Model(my_encoded_str='**encoded**: some str')

# Access decoded value
print(m.my_encoded_str)
#> some str

# Serialize into the encoded form
print(m.model_dump())
#> {'my_encoded_str': '**encoded**: some str'}

# Validate encoded data
try:
    Model(my_encoded_str='**undecodable**')
except ValidationError as e:
    print(e)
    '''
    1 validation error for Model
    my_encoded_str
      Value error, Cannot decode data [type=value_error, input_value='**undecodable**', input_type=str]
    '''

```

Source code in `pydantic/types.py`
```
2570
2571
2572
2573
2574
2575
2576
2577
2578
2579
2580
2581
2582
2583
2584
2585
2586
2587
2588
2589
2590
2591
2592
2593
2594
2595
2596
2597
2598
2599
2600
2601
2602
2603
2604
2605
2606
2607
2608
2609
2610
2611
2612
2613
2614
2615
2616
2617
2618
2619
2620
2621
2622
2623
2624
2625
2626
2627
2628
2629
2630
2631
2632
2633
2634
2635
2636
2637
2638
2639
2640
2641
2642
2643
2644
2645
2646
2647
2648
2649
2650
2651
2652
2653
2654
2655
2656
2657
2658
2659
2660
2661
2662
2663
2664
2665
2666
```
| ```
@_dataclasses.dataclass(**_internal_dataclass.slots_true)
class EncodedStr:
    """A str type that is encoded and decoded using the specified encoder.

    `EncodedStr` needs an encoder that implements `EncoderProtocol` to operate.

```python
    from typing import Annotated

    from pydantic import BaseModel, EncodedStr, EncoderProtocol, ValidationError

    class MyEncoder(EncoderProtocol):
        @classmethod
        def decode(cls, data: bytes) -> bytes:
            if data == b'**undecodable**':
                raise ValueError('Cannot decode data')
            return data[13:]

        @classmethod
        def encode(cls, value: bytes) -> bytes:
            return b'**encoded**: ' + value

        @classmethod
        def get_json_format(cls) -> str:
            return 'my-encoder'

    MyEncodedStr = Annotated[str, EncodedStr(encoder=MyEncoder)]

    class Model(BaseModel):
        my_encoded_str: MyEncodedStr

    # Initialize the model with encoded data
    m = Model(my_encoded_str='**encoded**: some str')

    # Access decoded value
    print(m.my_encoded_str)
    #> some str

    # Serialize into the encoded form
    print(m.model_dump())
    #> {'my_encoded_str': '**encoded**: some str'}

    # Validate encoded data
    try:
        Model(my_encoded_str='**undecodable**')
    except ValidationError as e:
        print(e)
        '''
        1 validation error for Model
        my_encoded_str
          Value error, Cannot decode data [type=value_error, input_value='**undecodable**', input_type=str]
        '''
```
    """

    encoder: type[EncoderProtocol]

    def __get_pydantic_json_schema__(
        self, core_schema: core_schema.CoreSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        field_schema = handler(core_schema)
        field_schema.update(type='string', format=self.encoder.get_json_format())
        return field_schema

    def __get_pydantic_core_schema__(self, source: type[Any], handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        schema = handler(source)
        _check_annotated_type(schema['type'], 'str', self.__class__.__name__)
        return core_schema.with_info_after_validator_function(
            function=self.decode_str,
            schema=schema,
            serialization=core_schema.plain_serializer_function_ser_schema(function=self.encode_str),
        )

    def decode_str(self, data: str, _: core_schema.ValidationInfo) -> str:
        """Decode the data using the specified encoder.

        Args:
            data: The data to decode.

        Returns:
            The decoded data.
        """
        return self.encoder.decode(data.encode()).decode()

    def encode_str(self, value: str) -> str:
        """Encode the data using the specified encoder.

        Args:
            value: The data to encode.

        Returns:
            The encoded data.
        """
        return self.encoder.encode(value.encode()).decode()  # noqa: UP008

    def __hash__(self) -> int:
        return hash(self.encoder)

```

---|---
####  decode_str [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncodedStr.decode_str)
```
decode_str(data: , _: ValidationInfo[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo)) ->

```

Decode the data using the specified encoder.
Parameters:
Name | Type | Description | Default
---|---|---|---
`data` |  |  The data to decode. |  _required_
Returns:
Type | Description
---|---
|  The decoded data.
Source code in `pydantic/types.py`
```
2643
2644
2645
2646
2647
2648
2649
2650
2651
2652
```
| ```
def decode_str(self, data: str, _: core_schema.ValidationInfo) -> str:
    """Decode the data using the specified encoder.

    Args:
        data: The data to decode.

    Returns:
        The decoded data.
    """
    return self.encoder.decode(data.encode()).decode()

```

---|---
####  encode_str [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncodedStr.encode_str)
```
encode_str(value: ) ->

```

Encode the data using the specified encoder.
Parameters:
Name | Type | Description | Default
---|---|---|---
`value` |  |  The data to encode. |  _required_
Returns:
Type | Description
---|---
|  The encoded data.
Source code in `pydantic/types.py`
```
2654
2655
2656
2657
2658
2659
2660
2661
2662
2663
```
| ```
def encode_str(self, value: str) -> str:
    """Encode the data using the specified encoder.

    Args:
        value: The data to encode.

    Returns:
        The encoded data.
    """
    return self.encoder.encode(value.encode()).decode()  # noqa: UP008

```

---|---
###  GetPydanticSchema `dataclass` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.GetPydanticSchema)
Usage Documentation
[Using `GetPydanticSchema` to Reduce Boilerplate](https://docs.pydantic.dev/latest/concepts/types/#using-getpydanticschema-to-reduce-boilerplate)
A convenience class for creating an annotation that provides pydantic custom type hooks.
This class is intended to eliminate the need to create a custom "marker" which defines the `__get_pydantic_core_schema__` and `__get_pydantic_json_schema__` custom hook methods.
For example, to have a field treated by type checkers as `int`, but by pydantic as `Any`, you can do:
```
from typing import Annotated, Any

from pydantic import BaseModel, GetPydanticSchema

HandleAsAny = GetPydanticSchema(lambda _s, h: h(Any))

class Model(BaseModel):
    x: Annotated[int, HandleAsAny]  # pydantic sees `x: Any`

print(repr(Model(x='abc').x))
#> 'abc'

```

Source code in `pydantic/types.py`
```
2842
2843
2844
2845
2846
2847
2848
2849
2850
2851
2852
2853
2854
2855
2856
2857
2858
2859
2860
2861
2862
2863
2864
2865
2866
2867
2868
2869
2870
2871
2872
2873
2874
2875
2876
2877
2878
2879
2880
2881
2882
2883
2884
2885
2886
```
| ```
@_dataclasses.dataclass(**_internal_dataclass.slots_true)
class GetPydanticSchema:
    """!!! abstract "Usage Documentation"
        [Using `GetPydanticSchema` to Reduce Boilerplate](../concepts/types.md#using-getpydanticschema-to-reduce-boilerplate)

    A convenience class for creating an annotation that provides pydantic custom type hooks.

    This class is intended to eliminate the need to create a custom "marker" which defines the
     `__get_pydantic_core_schema__` and `__get_pydantic_json_schema__` custom hook methods.

    For example, to have a field treated by type checkers as `int`, but by pydantic as `Any`, you can do:
```python
    from typing import Annotated, Any

    from pydantic import BaseModel, GetPydanticSchema

    HandleAsAny = GetPydanticSchema(lambda _s, h: h(Any))

    class Model(BaseModel):
        x: Annotated[int, HandleAsAny]  # pydantic sees `x: Any`

    print(repr(Model(x='abc').x))
    #> 'abc'
```
    """

    get_pydantic_core_schema: Callable[[Any, GetCoreSchemaHandler], CoreSchema] | None = None
    get_pydantic_json_schema: Callable[[Any, GetJsonSchemaHandler], JsonSchemaValue] | None = None

    # Note: we may want to consider adding a convenience staticmethod `def for_type(type_: Any) -> GetPydanticSchema:`
    #   which returns `GetPydanticSchema(lambda _s, h: h(type_))`

    if not TYPE_CHECKING:
        # We put `__getattr__` in a non-TYPE_CHECKING block because otherwise, mypy allows arbitrary attribute access

        def __getattr__(self, item: str) -> Any:
            """Use this rather than defining `__get_pydantic_core_schema__` etc. to reduce the number of nested calls."""
            if item == '__get_pydantic_core_schema__' and self.get_pydantic_core_schema:
                return self.get_pydantic_core_schema
            elif item == '__get_pydantic_json_schema__' and self.get_pydantic_json_schema:
                return self.get_pydantic_json_schema
            else:
                return object.__getattribute__(self, item)

    __hash__ = object.__hash__

```

---|---
###  Tag `dataclass` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Tag)
Provides a way to specify the expected tag to use for a case of a (callable) discriminated union.
Also provides a way to label a union case in error messages.
When using a callable `Discriminator`, attach a `Tag` to each case in the `Union` to specify the tag that should be used to identify that case. For example, in the below example, the `Tag` is used to specify that if `get_discriminator_value` returns `'apple'`, the input should be validated as an `ApplePie`, and if it returns `'pumpkin'`, the input should be validated as a `PumpkinPie`.
The primary role of the `Tag` here is to map the return value from the callable `Discriminator` function to the appropriate member of the `Union` in question.
```
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

Note
You must specify a `Tag` for every case in a `Tag` that is associated with a callable `Discriminator`. Failing to do so will result in a `PydanticUserError` with code [`callable-discriminator-no-tag`](https://docs.pydantic.dev/latest/errors/usage_errors/#callable-discriminator-no-tag).
See the [Discriminated Unions](https://docs.pydantic.dev/latest/concepts/unions/#discriminated-unions) concepts docs for more details on how to use `Tag`s.
Source code in `pydantic/types.py`
```
2889
2890
2891
2892
2893
2894
2895
2896
2897
2898
2899
2900
2901
2902
2903
2904
2905
2906
2907
2908
2909
2910
2911
2912
2913
2914
2915
2916
2917
2918
2919
2920
2921
2922
2923
2924
2925
2926
2927
2928
2929
2930
2931
2932
2933
2934
2935
2936
2937
2938
2939
2940
2941
2942
2943
2944
2945
2946
2947
2948
2949
2950
2951
2952
2953
2954
2955
2956
2957
2958
2959
2960
2961
2962
2963
2964
2965
2966
2967
2968
2969
2970
2971
```
| ```
@_dataclasses.dataclass(**_internal_dataclass.slots_true, frozen=True)
class Tag:
    """Provides a way to specify the expected tag to use for a case of a (callable) discriminated union.

    Also provides a way to label a union case in error messages.

    When using a callable `Discriminator`, attach a `Tag` to each case in the `Union` to specify the tag that
    should be used to identify that case. For example, in the below example, the `Tag` is used to specify that
    if `get_discriminator_value` returns `'apple'`, the input should be validated as an `ApplePie`, and if it
    returns `'pumpkin'`, the input should be validated as a `PumpkinPie`.

    The primary role of the `Tag` here is to map the return value from the callable `Discriminator` function to
    the appropriate member of the `Union` in question.

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

    !!! note
        You must specify a `Tag` for every case in a `Tag` that is associated with a
        callable `Discriminator`. Failing to do so will result in a `PydanticUserError` with code
        [`callable-discriminator-no-tag`](../errors/usage_errors.md#callable-discriminator-no-tag).

    See the [Discriminated Unions] concepts docs for more details on how to use `Tag`s.

    [Discriminated Unions]: ../concepts/unions.md#discriminated-unions
    """

    tag: str

    def __get_pydantic_core_schema__(self, source_type: Any, handler: GetCoreSchemaHandler) -> CoreSchema:
        schema = handler(source_type)
        metadata = cast('CoreMetadata', schema.setdefault('metadata', {}))
        metadata['pydantic_internal_union_tag_key'] = self.tag
        return schema

```

---|---
###  Discriminator `dataclass` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator)
Usage Documentation
[Discriminated Unions with `Callable` `Discriminator`](https://docs.pydantic.dev/latest/concepts/unions/#discriminated-unions-with-callable-discriminator)
Provides a way to use a custom callable as the way to extract the value of a union discriminator.
This allows you to get validation behavior like you'd get from `Field(discriminator=<field_name>)`, but without needing to have a single shared field across all the union choices. This also makes it possible to handle unions of models and primitive types with discriminated-union-style validation errors. Finally, this allows you to use a custom callable as the way to identify which member of a union a value belongs to, while still seeing all the performance benefits of a discriminated union.
Consider this example, which is much more performant with the use of `Discriminator` and thus a `TaggedUnion` than it would be as a normal `Union`.
```
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

See the [Discriminated Unions](https://docs.pydantic.dev/latest/concepts/unions/#discriminated-unions) concepts docs for more details on how to use `Discriminator`s.
Source code in `pydantic/types.py`
```
2974
2975
2976
2977
2978
2979
2980
2981
2982
2983
2984
2985
2986
2987
2988
2989
2990
2991
2992
2993
2994
2995
2996
2997
2998
2999
3000
3001
3002
3003
3004
3005
3006
3007
3008
3009
3010
3011
3012
3013
3014
3015
3016
3017
3018
3019
3020
3021
3022
3023
3024
3025
3026
3027
3028
3029
3030
3031
3032
3033
3034
3035
3036
3037
3038
3039
3040
3041
3042
3043
3044
3045
3046
3047
3048
3049
3050
3051
3052
3053
3054
3055
3056
3057
3058
3059
3060
3061
3062
3063
3064
3065
3066
3067
3068
3069
3070
3071
3072
3073
3074
3075
3076
3077
3078
3079
3080
3081
3082
3083
3084
3085
3086
3087
3088
3089
3090
3091
3092
3093
3094
3095
3096
3097
3098
3099
3100
3101
3102
3103
3104
3105
3106
3107
3108
3109
3110
3111
3112
3113
3114
3115
3116
3117
3118
3119
3120
3121
3122
3123
3124
3125
3126
3127
3128
3129
3130
3131
3132
3133
3134
3135
3136
```
| ```
@_dataclasses.dataclass(**_internal_dataclass.slots_true, frozen=True)
class Discriminator:
    """!!! abstract "Usage Documentation"
        [Discriminated Unions with `Callable` `Discriminator`](../concepts/unions.md#discriminated-unions-with-callable-discriminator)

    Provides a way to use a custom callable as the way to extract the value of a union discriminator.

    This allows you to get validation behavior like you'd get from `Field(discriminator=<field_name>)`,
    but without needing to have a single shared field across all the union choices. This also makes it
    possible to handle unions of models and primitive types with discriminated-union-style validation errors.
    Finally, this allows you to use a custom callable as the way to identify which member of a union a value
