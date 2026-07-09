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
Source code in `fastapi/routing.py`
```
3722
3723
3724
3725
3726
3727
3728
3729
3730
3731
3732
3733
3734
3735
3736
3737
3738
3739
3740
3741
3742
3743
3744
3745
3746
3747
3748
3749
3750
3751
3752
3753
3754
3755
3756
3757
3758
3759
3760
3761
3762
3763
3764
3765
3766
3767
3768
3769
3770
3771
3772
3773
3774
3775
3776
3777
3778
3779
3780
3781
3782
3783
3784
3785
3786
3787
3788
3789
3790
3791
3792
3793
3794
3795
3796
3797
3798
3799
3800
3801
3802
3803
3804
3805
3806
3807
3808
3809
3810
3811
3812
3813
3814
3815
3816
3817
3818
3819
3820
3821
3822
3823
3824
3825
3826
3827
3828
3829
3830
3831
3832
3833
3834
3835
3836
3837
3838
3839
3840
3841
3842
3843
3844
3845
3846
3847
3848
3849
3850
3851
3852
3853
3854
3855
3856
3857
3858
3859
3860
3861
3862
3863
3864
3865
3866
3867
3868
3869
3870
3871
3872
3873
3874
3875
3876
3877
3878
3879
3880
3881
3882
3883
3884
3885
3886
3887
3888
3889
3890
3891
3892
3893
3894
3895
3896
3897
3898
3899
3900
3901
3902
3903
3904
3905
3906
3907
3908
3909
3910
3911
3912
3913
3914
3915
3916
3917
3918
3919
3920
3921
3922
3923
3924
3925
3926
3927
3928
3929
3930
3931
3932
3933
3934
3935
3936
3937
3938
3939
3940
3941
3942
3943
3944
3945
3946
3947
3948
3949
3950
3951
3952
3953
3954
3955
3956
3957
3958
3959
3960
3961
3962
3963
3964
3965
3966
3967
3968
3969
3970
3971
3972
3973
3974
3975
3976
3977
3978
3979
3980
3981
3982
3983
3984
3985
3986
3987
3988
3989
3990
3991
3992
3993
3994
3995
3996
3997
3998
3999
4000
4001
4002
4003
4004
4005
4006
4007
4008
4009
4010
4011
4012
4013
4014
4015
4016
4017
4018
4019
4020
4021
4022
4023
4024
4025
4026
4027
4028
4029
4030
4031
4032
4033
4034
4035
4036
4037
4038
4039
4040
4041
4042
4043
4044
4045
4046
4047
4048
4049
4050
4051
4052
4053
4054
4055
4056
4057
4058
4059
4060
4061
4062
4063
4064
4065
4066
4067
4068
4069
4070
4071
4072
4073
4074
4075
4076
4077
4078
4079
4080
4081
4082
4083
4084
4085
4086
4087
4088
4089
4090
4091
4092
4093
4094
4095
4096
4097
4098
4099
4100
4101
4102
```
| ```
def head(
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
    Add a *path operation* using an HTTP HEAD operation.

    ## Example

```python
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
        methods=["HEAD"],
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
###  patch [¶](https://fastapi.tiangolo.com/reference/apirouter/#fastapi.APIRouter.patch "Permanent link")
```
patch(
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

Add a _path operation_ using an HTTP PATCH operation.
##### Example[¶](https://fastapi.tiangolo.com/reference/apirouter/#fastapi.APIRouter.patch--example)
```
from fastapi import APIRouter, FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None

app = FastAPI()
router = APIRouter()

@router.patch("/items/")
def update_item(item: Item):
    return {"message": "Item updated in place"}

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
