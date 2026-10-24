            return schema

    def __repr__(self) -> str:
        return 'AwareDatetime'

```

---|---
###  NaiveDatetime [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.NaiveDatetime)
A datetime that doesn't require timezone info.
Source code in `pydantic/types.py`
```
2293
2294
2295
2296
2297
2298
2299
2300
2301
2302
2303
2304
2305
2306
2307
2308
2309
2310
```
| ```
class NaiveDatetime:
    """A datetime that doesn't require timezone info."""

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        if cls is source:
            # used directly as a type
            return core_schema.datetime_schema(tz_constraint='naive')
        else:
            schema = handler(source)
            _check_annotated_type(schema['type'], 'datetime', cls.__name__)
            schema['tz_constraint'] = 'naive'
            return schema

    def __repr__(self) -> str:
        return 'NaiveDatetime'

```

---|---
###  PastDatetime [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PastDatetime)
A datetime that must be in the past.
Source code in `pydantic/types.py`
```
2312
2313
2314
2315
2316
2317
2318
2319
2320
2321
2322
2323
2324
2325
2326
2327
2328
2329
```
| ```
class PastDatetime:
    """A datetime that must be in the past."""

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        if cls is source:
            # used directly as a type
            return core_schema.datetime_schema(now_op='past')
        else:
            schema = handler(source)
            _check_annotated_type(schema['type'], 'datetime', cls.__name__)
            schema['now_op'] = 'past'
            return schema

    def __repr__(self) -> str:
        return 'PastDatetime'

```

---|---
###  FutureDatetime [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.FutureDatetime)
A datetime that must be in the future.
Source code in `pydantic/types.py`
```
2331
2332
2333
2334
2335
2336
2337
2338
2339
2340
2341
2342
2343
2344
2345
2346
2347
2348
```
| ```
class FutureDatetime:
    """A datetime that must be in the future."""

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        if cls is source:
            # used directly as a type
            return core_schema.datetime_schema(now_op='future')
        else:
            schema = handler(source)
            _check_annotated_type(schema['type'], 'datetime', cls.__name__)
            schema['now_op'] = 'future'
            return schema

    def __repr__(self) -> str:
        return 'FutureDatetime'

```

---|---
###  EncoderProtocol [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncoderProtocol)
Bases:
Protocol for encoding and decoding data to and from bytes.
Source code in `pydantic/types.py`
```
2354
2355
2356
2357
2358
2359
2360
2361
2362
2363
2364
2365
2366
2367
2368
2369
2370
2371
2372
2373
2374
2375
2376
2377
2378
2379
2380
2381
2382
2383
2384
2385
2386
2387
2388
```
| ```
class EncoderProtocol(Protocol):
    """Protocol for encoding and decoding data to and from bytes."""

    @classmethod
    def decode(cls, data: bytes) -> bytes:
        """Decode the data using the encoder.

        Args:
            data: The data to decode.

        Returns:
            The decoded data.
        """
        ...

    @classmethod
    def encode(cls, value: bytes) -> bytes:
        """Encode the data using the encoder.

        Args:
            value: The data to encode.

        Returns:
            The encoded data.
        """
        ...

    @classmethod
    def get_json_format(cls) -> str:
        """Get the JSON format for the encoded data.

        Returns:
            The JSON format for the encoded data.
        """
        ...

```

---|---
####  decode `classmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncoderProtocol.decode)
```
decode(data: ) ->

```

Decode the data using the encoder.
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
2357
2358
2359
2360
2361
2362
2363
2364
2365
2366
2367
```
| ```
@classmethod
def decode(cls, data: bytes) -> bytes:
    """Decode the data using the encoder.

    Args:
        data: The data to decode.

    Returns:
        The decoded data.
    """
    ...

```

---|---
####  encode `classmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncoderProtocol.encode)
```
encode(value: ) ->

```

Encode the data using the encoder.
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
2369
2370
2371
2372
2373
2374
2375
2376
2377
2378
2379
```
| ```
@classmethod
def encode(cls, value: bytes) -> bytes:
    """Encode the data using the encoder.

    Args:
        value: The data to encode.

    Returns:
        The encoded data.
    """
    ...

```

---|---
####  get_json_format `classmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncoderProtocol.get_json_format)
```
get_json_format() ->

```

Get the JSON format for the encoded data.
Returns:
Type | Description
---|---
|  The JSON format for the encoded data.
Source code in `pydantic/types.py`
```
2381
2382
2383
2384
2385
2386
2387
2388
```
| ```
@classmethod
def get_json_format(cls) -> str:
    """Get the JSON format for the encoded data.

    Returns:
        The JSON format for the encoded data.
    """
    ...

```

---|---
###  Base64Encoder [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64Encoder)
Bases: `EncoderProtocol[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncoderProtocol)`
Standard (non-URL-safe) Base64 encoder.
Source code in `pydantic/types.py`
```
2391
2392
2393
2394
2395
2396
2397
2398
2399
2400
2401
2402
2403
2404
2405
2406
2407
2408
2409
2410
2411
2412
2413
2414
2415
2416
2417
2418
2419
2420
2421
2422
2423
2424
2425
2426
2427
2428
```
| ```
class Base64Encoder(EncoderProtocol):
    """Standard (non-URL-safe) Base64 encoder."""

    @classmethod
    def decode(cls, data: bytes) -> bytes:
        """Decode the data from base64 encoded bytes to original bytes data.

        Args:
            data: The data to decode.

        Returns:
            The decoded data.
        """
        try:
            return base64.b64decode(data)
        except ValueError as e:
            raise PydanticCustomError('base64_decode', "Base64 decoding error: '{error}'", {'error': str(e)})

    @classmethod
    def encode(cls, value: bytes) -> bytes:
        """Encode the data from bytes to a base64 encoded bytes.

        Args:
            value: The data to encode.

        Returns:
            The encoded data.
        """
        return base64.b64encode(value)

    @classmethod
    def get_json_format(cls) -> Literal['base64']:
        """Get the JSON format for the encoded data.

        Returns:
            The JSON format for the encoded data.
        """
        return 'base64'

```

---|---
####  decode `classmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64Encoder.decode)
```
decode(data: ) ->

```

Decode the data from base64 encoded bytes to original bytes data.
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
2394
2395
2396
2397
2398
2399
2400
2401
2402
2403
2404
2405
2406
2407
```
| ```
@classmethod
def decode(cls, data: bytes) -> bytes:
    """Decode the data from base64 encoded bytes to original bytes data.

    Args:
        data: The data to decode.

    Returns:
        The decoded data.
    """
    try:
        return base64.b64decode(data)
    except ValueError as e:
        raise PydanticCustomError('base64_decode', "Base64 decoding error: '{error}'", {'error': str(e)})

```

---|---
####  encode `classmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64Encoder.encode)
```
encode(value: ) ->

```

Encode the data from bytes to a base64 encoded bytes.
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
2409
2410
2411
2412
2413
2414
2415
2416
2417
2418
2419
```
| ```
@classmethod
def encode(cls, value: bytes) -> bytes:
    """Encode the data from bytes to a base64 encoded bytes.

    Args:
        value: The data to encode.

    Returns:
        The encoded data.
    """
    return base64.b64encode(value)

```

---|---
####  get_json_format `classmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64Encoder.get_json_format)
```
get_json_format() -> ['base64']

```

Get the JSON format for the encoded data.
Returns:
Type | Description
---|---
|  The JSON format for the encoded data.
Source code in `pydantic/types.py`
```
2421
2422
2423
2424
2425
2426
2427
2428
```
| ```
@classmethod
def get_json_format(cls) -> Literal['base64']:
    """Get the JSON format for the encoded data.

    Returns:
        The JSON format for the encoded data.
    """
    return 'base64'

```

---|---
###  Base64UrlEncoder [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64UrlEncoder)
Bases: `EncoderProtocol[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncoderProtocol)`
URL-safe Base64 encoder.
Source code in `pydantic/types.py`
```
2431
2432
2433
2434
2435
2436
2437
2438
2439
2440
2441
2442
2443
2444
2445
2446
2447
2448
2449
2450
2451
2452
2453
2454
2455
2456
2457
2458
2459
2460
2461
2462
2463
2464
2465
2466
2467
2468
```
| ```
class Base64UrlEncoder(EncoderProtocol):
    """URL-safe Base64 encoder."""

    @classmethod
    def decode(cls, data: bytes) -> bytes:
        """Decode the data from base64 encoded bytes to original bytes data.

        Args:
            data: The data to decode.

        Returns:
            The decoded data.
        """
        try:
            return base64.urlsafe_b64decode(data)
        except ValueError as e:
            raise PydanticCustomError('base64_decode', "Base64 decoding error: '{error}'", {'error': str(e)})

    @classmethod
    def encode(cls, value: bytes) -> bytes:
        """Encode the data from bytes to a base64 encoded bytes.

        Args:
            value: The data to encode.

        Returns:
            The encoded data.
        """
        return base64.urlsafe_b64encode(value)

    @classmethod
    def get_json_format(cls) -> Literal['base64url']:
        """Get the JSON format for the encoded data.

        Returns:
            The JSON format for the encoded data.
        """
        return 'base64url'

```

---|---
####  decode `classmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64UrlEncoder.decode)
```
decode(data: ) ->

```

Decode the data from base64 encoded bytes to original bytes data.
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
2434
2435
2436
2437
2438
2439
2440
2441
2442
2443
2444
2445
2446
2447
```
| ```
@classmethod
def decode(cls, data: bytes) -> bytes:
    """Decode the data from base64 encoded bytes to original bytes data.

    Args:
        data: The data to decode.

    Returns:
        The decoded data.
    """
    try:
        return base64.urlsafe_b64decode(data)
    except ValueError as e:
        raise PydanticCustomError('base64_decode', "Base64 decoding error: '{error}'", {'error': str(e)})

```

---|---
####  encode `classmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64UrlEncoder.encode)
```
encode(value: ) ->

```

Encode the data from bytes to a base64 encoded bytes.
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
2449
2450
2451
2452
2453
2454
2455
2456
2457
2458
2459
```
| ```
@classmethod
def encode(cls, value: bytes) -> bytes:
    """Encode the data from bytes to a base64 encoded bytes.

    Args:
        value: The data to encode.

    Returns:
        The encoded data.
    """
    return base64.urlsafe_b64encode(value)

```

---|---
####  get_json_format `classmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64UrlEncoder.get_json_format)
```
get_json_format() -> ['base64url']

```

Get the JSON format for the encoded data.
Returns:
Type | Description
---|---
|  The JSON format for the encoded data.
Source code in `pydantic/types.py`
```
2461
2462
2463
2464
2465
2466
2467
2468
```
| ```
@classmethod
def get_json_format(cls) -> Literal['base64url']:
    """Get the JSON format for the encoded data.

    Returns:
        The JSON format for the encoded data.
    """
    return 'base64url'

```

---|---
###  EncodedBytes `dataclass` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncodedBytes)
A bytes type that is encoded and decoded using the specified encoder.
`EncodedBytes` needs an encoder that implements `EncoderProtocol` to operate.
```
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
