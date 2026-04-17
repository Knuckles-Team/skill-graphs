`response_model_exclude_unset` |  Configuration passed to Pydantic to define if the response data should have all the fields, including the ones that were not set and have their default values. This is different from `response_model_exclude_defaults` in that if the fields are set, they will be included in the response, even if the value is the same as the default. When `True`, default values are omitted from the response. Read more about it in the [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#use-the-response_model_exclude_unset-parameter). **TYPE:** `bool` **DEFAULT:** `False`
`response_model_exclude_defaults` |  Configuration passed to Pydantic to define if the response data should have all the fields, including the ones that have the same value as the default. This is different from `response_model_exclude_unset` in that if the fields are set but contain the same default values, they will be excluded from the response. When `True`, default values are omitted from the response. Read more about it in the [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#use-the-response_model_exclude_unset-parameter). **TYPE:** `bool` **DEFAULT:** `False`
`response_model_exclude_none` |  Configuration passed to Pydantic to define if the response data should exclude fields set to `None`. This is much simpler (less smart) than `response_model_exclude_unset` and `response_model_exclude_defaults`. You probably want to use one of those two instead of this one, as those allow returning `None` values when it makes sense. Read more about it in the [FastAPI docs for Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/#response_model_exclude_none). **TYPE:** `bool` **DEFAULT:** `False`
`include_in_schema` |  Include this _path operation_ in the generated OpenAPI schema. This affects the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for Query Parameters and String Validations](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#exclude-parameters-from-openapi). **TYPE:** `bool` **DEFAULT:** `True`
`response_class` |  Response class to be used for this _path operation_. This will not be used if you return a response directly. Read more about it in the [FastAPI docs for Custom Response - HTML, Stream, File, others](https://fastapi.tiangolo.com/advanced/custom-response/#redirectresponse). **TYPE:** `type[Response[](https://fastapi.tiangolo.com/reference/response/#fastapi.Response "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.Response</span> \(<code>starlette.responses.Response</code>\)")]` **DEFAULT:** `Default(JSONResponse[](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.responses.JSONResponse</span> \(<code>starlette.responses.JSONResponse</code>\)"))`
`name` |  Name for this _path operation_. Only used internally. **TYPE:** `str | None` **DEFAULT:** `None`
`callbacks` |  List of _path operations_ that will be used as OpenAPI callbacks. This is only for OpenAPI documentation, the callbacks won't be used directly. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for OpenAPI Callbacks](https://fastapi.tiangolo.com/advanced/openapi-callbacks/). **TYPE:** `list[BaseRoute] | None` **DEFAULT:** `None`
`openapi_extra` |  Extra metadata to be included in the OpenAPI schema for this _path operation_. Read more about it in the [FastAPI docs for Path Operation Advanced Configuration](https://fastapi.tiangolo.com/advanced/path-operation-advanced-configuration/#custom-openapi-path-operation-schema). **TYPE:** `dict[str, Any] | None` **DEFAULT:** `None`
`generate_unique_id_function` |  Customize the function used to generate unique IDs for the _path operations_ shown in the generated OpenAPI. This is particularly useful when automatically generating clients or SDKs for your API. Read more about it in the [FastAPI docs about how to Generate Clients](https://fastapi.tiangolo.com/advanced/generate-clients/#custom-generate-unique-id-function). **TYPE:** `Callable[[APIRoute], str]` **DEFAULT:** `Default(generate_unique_id)`
Source code in `fastapi/routing.py`
```
3345
3346
3347
3348
3349
3350
3351
3352
3353
3354
3355
3356
3357
3358
3359
3360
3361
3362
3363
3364
3365
3366
3367
3368
3369
3370
3371
3372
3373
3374
3375
3376
3377
3378
3379
3380
3381
3382
3383
3384
3385
3386
3387
3388
3389
3390
3391
3392
3393
3394
3395
3396
3397
3398
3399
3400
3401
3402
3403
3404
3405
3406
3407
3408
3409
3410
3411
3412
3413
3414
3415
3416
3417
3418
3419
3420
3421
3422
3423
3424
3425
3426
3427
3428
3429
3430
3431
3432
3433
3434
3435
3436
3437
3438
3439
3440
3441
3442
3443
3444
3445
3446
3447
3448
3449
3450
3451
3452
3453
3454
3455
3456
3457
3458
3459
3460
3461
3462
3463
3464
3465
3466
3467
3468
3469
3470
3471
3472
3473
3474
3475
3476
3477
3478
3479
3480
3481
3482
3483
3484
3485
3486
3487
3488
3489
3490
3491
3492
3493
3494
3495
3496
3497
3498
3499
3500
3501
3502
3503
3504
3505
3506
3507
3508
3509
3510
3511
3512
3513
3514
3515
3516
3517
3518
3519
3520
3521
3522
3523
3524
3525
3526
3527
3528
3529
3530
3531
3532
3533
3534
3535
3536
3537
3538
3539
3540
3541
3542
3543
3544
3545
3546
3547
3548
3549
3550
3551
3552
3553
3554
3555
3556
3557
3558
3559
3560
3561
3562
3563
3564
3565
3566
3567
3568
3569
3570
3571
3572
3573
3574
3575
3576
3577
3578
3579
3580
3581
3582
3583
3584
3585
3586
3587
3588
3589
3590
3591
3592
3593
3594
3595
3596
3597
3598
3599
3600
3601
3602
3603
3604
3605
3606
3607
3608
3609
3610
3611
3612
3613
3614
3615
3616
3617
3618
3619
3620
3621
3622
3623
3624
3625
3626
3627
3628
3629
3630
3631
3632
3633
3634
3635
3636
3637
3638
3639
3640
3641
3642
3643
3644
3645
3646
3647
3648
3649
3650
3651
3652
3653
3654
3655
3656
3657
3658
3659
3660
3661
3662
3663
3664
3665
3666
3667
3668
3669
3670
3671
3672
3673
3674
3675
3676
3677
3678
3679
3680
3681
3682
3683
3684
3685
3686
3687
3688
3689
3690
3691
3692
3693
3694
3695
3696
3697
3698
3699
3700
3701
3702
3703
3704
3705
3706
3707
3708
3709
3710
3711
3712
3713
3714
3715
3716
3717
3718
3719
3720
```
| ```
def options(
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
    Add a *path operation* using an HTTP OPTIONS operation.

    ## Example

```python
    from fastapi import APIRouter, FastAPI

    app = FastAPI()
    router = APIRouter()

    @router.options("/items/")
    def get_item_options():
        return {"additions": ["Aji", "Guacamole"]}

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
        methods=["OPTIONS"],
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
###  head [¶](https://fastapi.tiangolo.com/reference/apirouter/#fastapi.APIRouter.head "Permanent link")
```
head(
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

Add a _path operation_ using an HTTP HEAD operation.
##### Example[¶](https://fastapi.tiangolo.com/reference/apirouter/#fastapi.APIRouter.head--example)
```
from fastapi import APIRouter, FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None

app = FastAPI()
router = APIRouter()

@router.head("/items/", status_code=204)
def get_items_headers(response: Response):
    response.headers["X-Cat-Dog"] = "Alone in the world"

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
