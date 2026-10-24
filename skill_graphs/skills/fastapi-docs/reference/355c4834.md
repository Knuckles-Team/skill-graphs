
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
        Callable[[routing.APIRoute], str],
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
    from fastapi import FastAPI
    from pydantic import BaseModel

    class Item(BaseModel):
        name: str
        description: str | None = None

    app = FastAPI()

    @app.put("/items/{item_id}")
    def replace_item(item_id: str, item: Item):
        return {"message": "Item replaced", "id": item_id}
```
    """
    return self.router.put(
        path,
        response_model=response_model,
        status_code=status_code,
        tags=tags,
        dependencies=dependencies,
        summary=summary,
        description=description,
        response_description=response_description,
        responses=responses,
        deprecated=deprecated,
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
###  post [¶](https://fastapi.tiangolo.com/reference/fastapi/#fastapi.FastAPI.post "Permanent link")
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
##### Example[¶](https://fastapi.tiangolo.com/reference/fastapi/#fastapi.FastAPI.post--example)
```
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None

app = FastAPI()

@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item created"}

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
`response_class` |  Response class to be used for this _path operation_. This will not be used if you return a response directly. Read more about it in the [FastAPI docs for Custom Response - HTML, Stream, File, others](https://fastapi.tiangolo.com/advanced/custom-response/#redirectresponse). **TYPE:** `type[Response[](https://fastapi.tiangolo.com/reference/response/#fastapi.Response "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.Response</span> \(<code>starlette.responses.Response</code>\)")]` **DEFAULT:** `Default(JSONResponse[](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.responses.JSONResponse</span> \(<code>starlette.responses.JSONResponse</code>\)"))`
`name` |  Name for this _path operation_. Only used internally. **TYPE:** `str | None` **DEFAULT:** `None`
`callbacks` |  List of _path operations_ that will be used as OpenAPI callbacks. This is only for OpenAPI documentation, the callbacks won't be used directly. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for OpenAPI Callbacks](https://fastapi.tiangolo.com/advanced/openapi-callbacks/). **TYPE:** `list[BaseRoute] | None` **DEFAULT:** `None`
`openapi_extra` |  Extra metadata to be included in the OpenAPI schema for this _path operation_. Read more about it in the [FastAPI docs for Path Operation Advanced Configuration](https://fastapi.tiangolo.com/advanced/path-operation-advanced-configuration/#custom-openapi-path-operation-schema). **TYPE:** `dict[str, Any] | None` **DEFAULT:** `None`
`generate_unique_id_function` |  Customize the function used to generate unique IDs for the _path operations_ shown in the generated OpenAPI. This is particularly useful when automatically generating clients or SDKs for your API. Read more about it in the [FastAPI docs about how to Generate Clients](https://fastapi.tiangolo.com/advanced/generate-clients/#custom-generate-unique-id-function). **TYPE:** `Callable[[APIRoute], str]` **DEFAULT:** `Default(generate_unique_id)`
Source code in `fastapi/applications.py`
```
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
2667
2668
2669
2670
2671
2672
2673
2674
2675
2676
2677
2678
2679
2680
2681
2682
2683
2684
2685
2686
2687
2688
2689
2690
2691
```
| ```
def post(
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
        Sequence[Depends] | None,
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
