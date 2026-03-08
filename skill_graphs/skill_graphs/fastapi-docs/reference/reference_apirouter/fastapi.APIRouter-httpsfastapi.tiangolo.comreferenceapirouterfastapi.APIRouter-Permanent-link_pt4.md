`openapi_extra` |  Extra metadata to be included in the OpenAPI schema for this _path operation_. Read more about it in the [FastAPI docs for Path Operation Advanced Configuration](https://fastapi.tiangolo.com/advanced/path-operation-advanced-configuration/#custom-openapi-path-operation-schema). **TYPE:** `dict[str, Any] | None` **DEFAULT:** `None`
`generate_unique_id_function` |  Customize the function used to generate unique IDs for the _path operations_ shown in the generated OpenAPI. This is particularly useful when automatically generating clients or SDKs for your API. Read more about it in the [FastAPI docs about how to Generate Clients](https://fastapi.tiangolo.com/advanced/generate-clients/#custom-generate-unique-id-function). **TYPE:** `Callable[[APIRoute], str]` **DEFAULT:** `Default(generate_unique_id)`
Source code in `fastapi/routing.py`
```
2204
2205
2206
2207
2208
2209
2210
2211
2212
2213
2214
2215
2216
2217
2218
2219
2220
2221
2222
2223
2224
2225
2226
2227
2228
2229
2230
2231
2232
2233
2234
2235
2236
2237
2238
2239
2240
2241
2242
2243
2244
2245
2246
2247
2248
2249
2250
2251
2252
2253
2254
2255
2256
2257
2258
2259
2260
2261
2262
2263
2264
2265
2266
2267
2268
2269
2270
2271
2272
2273
2274
2275
2276
2277
2278
2279
2280
2281
2282
2283
2284
2285
2286
2287
2288
2289
2290
2291
2292
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
2311
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
2330
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
2349
2350
2351
2352
2353
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
2389
2390
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
2429
2430
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
2469
2470
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
2568
2569
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
```
| ```
def put(
    self,
    path: Annotated[
        str,
        Doc(
            """
            The URL path to be used for this *path operation*.

            For example, in `http://example.com/items`, the path is `/items`.
            """
        ),
    ],
    *,
    response_model: Annotated[
        Any,
        Doc(
            """
            The type to use for the response.

            It could be any valid Pydantic *field* type. So, it doesn't have to
            be a Pydantic model, it could be other things, like a `list`, `dict`,
            etc.

            It will be used for:

            * Documentation: the generated OpenAPI (and the UI at `/docs`) will
                show it as the response (JSON Schema).
            * Serialization: you could return an arbitrary object and the
                `response_model` would be used to serialize that object into the
                corresponding JSON.
            * Filtering: the JSON sent to the client will only contain the data
                (fields) defined in the `response_model`. If you returned an object
                that contains an attribute `password` but the `response_model` does
                not include that field, the JSON sent to the client would not have
                that `password`.
            * Validation: whatever you return will be serialized with the
                `response_model`, converting any data as necessary to generate the
                corresponding JSON. But if the data in the object returned is not
                valid, that would mean a violation of the contract with the client,
                so it's an error from the API developer. So, FastAPI will raise an
                error and return a 500 error code (Internal Server Error).

            Read more about it in the
            [FastAPI docs for Response Model](https://fastapi.tiangolo.com/tutorial/response-model/).
            """
        ),
    ] = Default(None),
    status_code: Annotated[
        int | None,
        Doc(
            """
            The default status code to be used for the response.

            You could override the status code by returning a response directly.

            Read more about it in the
            [FastAPI docs for Response Status Code](https://fastapi.tiangolo.com/tutorial/response-status-code/).
            """
        ),
    ] = None,
    tags: Annotated[
        list[str | Enum] | None,
        Doc(
            """
            A list of tags to be applied to the *path operation*.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Read more about it in the
            [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/#tags).
            """
        ),
    ] = None,
    dependencies: Annotated[
        Sequence[params.Depends] | None,
        Doc(
            """
            A list of dependencies (using `Depends()`) to be applied to the
            *path operation*.

            Read more about it in the
            [FastAPI docs for Dependencies in path operation decorators](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/).
            """
        ),
    ] = None,
    summary: Annotated[
        str | None,
        Doc(
            """
            A summary for the *path operation*.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Read more about it in the
            [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/).
            """
        ),
    ] = None,
    description: Annotated[
        str | None,
        Doc(
            """
            A description for the *path operation*.

            If not provided, it will be extracted automatically from the docstring
            of the *path operation function*.

            It can contain Markdown.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Read more about it in the
            [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/).
            """
        ),
    ] = None,
    response_description: Annotated[
        str,
        Doc(
            """
            The description for the default response.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).
            """
        ),
    ] = "Successful Response",
    responses: Annotated[
        dict[int | str, dict[str, Any]] | None,
        Doc(
            """
            Additional responses that could be returned by this *path operation*.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).
            """
        ),
    ] = None,
    deprecated: Annotated[
        bool | None,
        Doc(
            """
            Mark this *path operation* as deprecated.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).
            """
        ),
    ] = None,
    operation_id: Annotated[
        str | None,
        Doc(
            """
            Custom operation ID to be used by this *path operation*.

            By default, it is generated automatically.

            If you provide a custom operation ID, you need to make sure it is
            unique for the whole API.

            You can customize the
            operation ID generation with the parameter
            `generate_unique_id_function` in the `FastAPI` class.

            Read more about it in the
            [FastAPI docs about how to Generate Clients](https://fastapi.tiangolo.com/advanced/generate-clients/#custom-generate-unique-id-function).
            """
        ),
    ] = None,
    response_model_include: Annotated[
        IncEx | None,
        Doc(
            """
            Configuration passed to Pydantic to include only certain fields in the
            response data.

            Read more about it in the
            [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#response_model_include-and-response_model_exclude).
            """
        ),
    ] = None,
    response_model_exclude: Annotated[
        IncEx | None,
        Doc(
            """
            Configuration passed to Pydantic to exclude certain fields in the
            response data.

            Read more about it in the
            [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#response_model_include-and-response_model_exclude).
            """
        ),
    ] = None,
    response_model_by_alias: Annotated[
        bool,
        Doc(
            """
            Configuration passed to Pydantic to define if the response model
            should be serialized by alias when an alias is used.

            Read more about it in the
            [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#response_model_include-and-response_model_exclude).
            """
        ),
    ] = True,
    response_model_exclude_unset: Annotated[
        bool,
        Doc(
            """
            Configuration passed to Pydantic to define if the response data
            should have all the fields, including the ones that were not set and
            have their default values. This is different from
            `response_model_exclude_defaults` in that if the fields are set,
            they will be included in the response, even if the value is the same
            as the default.

            When `True`, default values are omitted from the response.

            Read more about it in the
            [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#use-the-response_model_exclude_unset-parameter).
            """
        ),
    ] = False,
    response_model_exclude_defaults: Annotated[
        bool,
        Doc(
            """
            Configuration passed to Pydantic to define if the response data
            should have all the fields, including the ones that have the same value
            as the default. This is different from `response_model_exclude_unset`
            in that if the fields are set but contain the same default values,
            they will be excluded from the response.

            When `True`, default values are omitted from the response.

            Read more about it in the
            [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#use-the-response_model_exclude_unset-parameter).
            """
        ),
    ] = False,
    response_model_exclude_none: Annotated[
        bool,
        Doc(
            """
            Configuration passed to Pydantic to define if the response data should
            exclude fields set to `None`.

            This is much simpler (less smart) than `response_model_exclude_unset`
            and `response_model_exclude_defaults`. You probably want to use one of
            those two instead of this one, as those allow returning `None` values
            when it makes sense.

            Read more about it in the
            [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#response_model_exclude_none).
            """
        ),
    ] = False,
    include_in_schema: Annotated[
        bool,
        Doc(
            """
            Include this *path operation* in the generated OpenAPI schema.

            This affects the generated OpenAPI (e.g. visible at `/docs`).

            Read more about it in the
            [FastAPI docs for Query Parameters and String Validations](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#exclude-parameters-from-openapi).
            """
        ),
    ] = True,
    response_class: Annotated[
        type[Response],
        Doc(
            """
            Response class to be used for this *path operation*.

            This will not be used if you return a response directly.

            Read more about it in the
            [FastAPI docs for Custom Response - HTML, Stream, File, others](https://fastapi.tiangolo.com/advanced/custom-response/#redirectresponse).
            """
        ),
    ] = Default(JSONResponse),
    name: Annotated[
        str | None,
        Doc(
            """
            Name for this *path operation*. Only used internally.
            """
        ),
    ] = None,
    callbacks: Annotated[
        list[BaseRoute] | None,
        Doc(
            """
            List of *path operations* that will be used as OpenAPI callbacks.

            This is only for OpenAPI documentation, the callbacks won't be used
            directly.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Read more about it in the
            [FastAPI docs for OpenAPI Callbacks](https://fastapi.tiangolo.com/advanced/openapi-callbacks/).
            """
        ),
    ] = None,
    openapi_extra: Annotated[
        dict[str, Any] | None,
        Doc(
            """
            Extra metadata to be included in the OpenAPI schema for this *path
            operation*.

            Read more about it in the
            [FastAPI docs for Path Operation Advanced Configuration](https://fastapi.tiangolo.com/advanced/path-operation-advanced-configuration/#custom-openapi-path-operation-schema).
            """
        ),
    ] = None,
    generate_unique_id_function: Annotated[
        Callable[[APIRoute], str],
        Doc(
            """
            Customize the function used to generate unique IDs for the *path
            operations* shown in the generated OpenAPI.

            This is particularly useful when automatically generating clients or
            SDKs for your API.

            Read more about it in the
            [FastAPI docs about how to Generate Clients](https://fastapi.tiangolo.com/advanced/generate-clients/#custom-generate-unique-id-function).
            """
        ),
    ] = Default(generate_unique_id),
) -> Callable[[DecoratedCallable], DecoratedCallable]:
    """
    Add a *path operation* using an HTTP PUT operation.

    ## Example

```python
    from fastapi import APIRouter, FastAPI
    from pydantic import BaseModel

    class Item(BaseModel):
        name: str
        description: str | None = None

    app = FastAPI()
    router = APIRouter()

    @router.put("/items/{item_id}")
    def replace_item(item_id: str, item: Item):
        return {"message": "Item replaced", "id": item_id}

    app.include_router(router)
```
    """
    return self.api_route(
        path=path,
        response_model=response_model,
        status_code=status_code,
        tags=tags,
        dependencies=dependencies,
        summary=summary,
        description=description,
        response_description=response_description,
        responses=responses,
        deprecated=deprecated,
        methods=["PUT"],
        operation_id=operation_id,
        response_model_include=response_model_include,
        response_model_exclude=response_model_exclude,
        response_model_by_alias=response_model_by_alias,
        response_model_exclude_unset=response_model_exclude_unset,
        response_model_exclude_defaults=response_model_exclude_defaults,
        response_model_exclude_none=response_model_exclude_none,
        include_in_schema=include_in_schema,
        response_class=response_class,
        name=name,
        callbacks=callbacks,
        openapi_extra=openapi_extra,
        generate_unique_id_function=generate_unique_id_function,
    )

```

---|---
###  post [¶](https://fastapi.tiangolo.com/reference/apirouter/#fastapi.APIRouter.post "Permanent link")
```
post(
    path,
    *,
    response_model=Default(None),
    status_code=None,
    tags=None,
    dependencies=None,
    summary=None,
    description=None,
    response_description="Successful Response",
    responses=None,
    deprecated=None,
    operation_id=None,
    response_model_include=None,
    response_model_exclude=None,
    response_model_by_alias=True,
    response_model_exclude_unset=False,
    response_model_exclude_defaults=False,
    response_model_exclude_none=False,
    include_in_schema=True,
    response_class=Default(JSONResponse[](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.responses.JSONResponse</span> \(<code>starlette.responses.JSONResponse</code>\)")),
    name=None,
    callbacks=None,
    openapi_extra=None,
    generate_unique_id_function=Default(generate_unique_id)
)

```

Add a _path operation_ using an HTTP POST operation.
##### Example[¶](https://fastapi.tiangolo.com/reference/apirouter/#fastapi.APIRouter.post--example)
```
from fastapi import APIRouter, FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None

app = FastAPI()
router = APIRouter()

@router.post("/items/")
def create_item(item: Item):
    return {"message": "Item created"}

app.include_router(router)

```

PARAMETER | DESCRIPTION
---|---
`path` |  The URL path to be used for this _path operation_. For example, in `http://example.com/items`, the path is `/items`. **TYPE:** `str`
`response_model` |  The type to use for the response. It could be any valid Pydantic _field_ type. So, it doesn't have to be a Pydantic model, it could be other things, like a `list`, `dict`, etc. It will be used for:
  * Documentation: the generated OpenAPI (and the UI at `/docs`) will show it as the response (JSON Schema).
  * Serialization: you could return an arbitrary object and the `response_model` would be used to serialize that object into the corresponding JSON.
  * Filtering: the JSON sent to the client will only contain the data (fields) defined in the `response_model`. If you returned an object that contains an attribute `password` but the `response_model` does not include that field, the JSON sent to the client would not have that `password`.
  * Validation: whatever you return will be serialized with the `response_model`, converting any data as necessary to generate the corresponding JSON. But if the data in the object returned is not valid, that would mean a violation of the contract with the client, so it's an error from the API developer. So, FastAPI will raise an error and return a 500 error code (Internal Server Error).

Read more about it in the [FastAPI docs for Response Model](https://fastapi.tiangolo.com/tutorial/response-model/). **TYPE:** `Any` **DEFAULT:** `Default(None)`
`status_code` |  The default status code to be used for the response. You could override the status code by returning a response directly. Read more about it in the [FastAPI docs for Response Status Code](https://fastapi.tiangolo.com/tutorial/response-status-code/). **TYPE:** `int | None` **DEFAULT:** `None`
`tags` |  A list of tags to be applied to the _path operation_. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/#tags). **TYPE:** `list[str | Enum] | None` **DEFAULT:** `None`
`dependencies` |  A list of dependencies (using `Depends()`) to be applied to the _path operation_. Read more about it in the [FastAPI docs for Dependencies in path operation decorators](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/). **TYPE:** `Sequence[Depends] | None` **DEFAULT:** `None`
`summary` |  A summary for the _path operation_. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/). **TYPE:** `str | None` **DEFAULT:** `None`
`description` |  A description for the _path operation_. If not provided, it will be extracted automatically from the docstring of the _path operation function_. It can contain Markdown. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/). **TYPE:** `str | None` **DEFAULT:** `None`
`response_description` |  The description for the default response. It will be added to the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `str` **DEFAULT:** `'Successful Response'`
`responses` |  Additional responses that could be returned by this _path operation_. It will be added to the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `dict[int | str, dict[str, Any]] | None` **DEFAULT:** `None`
`deprecated` |  Mark this _path operation_ as deprecated. It will be added to the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `bool | None` **DEFAULT:** `None`
`operation_id` |  Custom operation ID to be used by this _path operation_. By default, it is generated automatically. If you provide a custom operation ID, you need to make sure it is unique for the whole API. You can customize the operation ID generation with the parameter `generate_unique_id_function` in the `FastAPI` class. Read more about it in the [FastAPI docs about how to Generate Clients](https://fastapi.tiangolo.com/advanced/generate-clients/#custom-generate-unique-id-function). **TYPE:** `str | None` **DEFAULT:** `None`
`response_model_include` |  Configuration passed to Pydantic to include only certain fields in the response data. Read more about it in the [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#response_model_include-and-response_model_exclude). **TYPE:** `IncEx | None` **DEFAULT:** `None`
`response_model_exclude` |  Configuration passed to Pydantic to exclude certain fields in the response data. Read more about it in the [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#response_model_include-and-response_model_exclude). **TYPE:** `IncEx | None` **DEFAULT:** `None`
`response_model_by_alias` |  Configuration passed to Pydantic to define if the response model should be serialized by alias when an alias is used. Read more about it in the [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#response_model_include-and-response_model_exclude). **TYPE:** `bool` **DEFAULT:** `True`
`response_model_exclude_unset` |  Configuration passed to Pydantic to define if the response data should have all the fields, including the ones that were not set and have their default values. This is different from `response_model_exclude_defaults` in that if the fields are set, they will be included in the response, even if the value is the same as the default. When `True`, default values are omitted from the response. Read more about it in the [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#use-the-response_model_exclude_unset-parameter). **TYPE:** `bool` **DEFAULT:** `False`
`response_model_exclude_defaults` |  Configuration passed to Pydantic to define if the response data should have all the fields, including the ones that have the same value as the default. This is different from `response_model_exclude_unset` in that if the fields are set but contain the same default values, they will be excluded from the response. When `True`, default values are omitted from the response. Read more about it in the [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#use-the-response_model_exclude_unset-parameter). **TYPE:** `bool` **DEFAULT:** `False`
`response_model_exclude_none` |  Configuration passed to Pydantic to define if the response data should exclude fields set to `None`. This is much simpler (less smart) than `response_model_exclude_unset` and `response_model_exclude_defaults`. You probably want to use one of those two instead of this one, as those allow returning `None` values when it makes sense. Read more about it in the [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#response_model_exclude_none). **TYPE:** `bool` **DEFAULT:** `False`
`include_in_schema` |  Include this _path operation_ in the generated OpenAPI schema. This affects the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for Query Parameters and String Validations](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#exclude-parameters-from-openapi). **TYPE:** `bool` **DEFAULT:** `True`
