 741
 742
 743
 744
 745
 746
 747
 748
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
 829
 830
 831
 832
 833
 834
 835
 836
 837
 838
 839
 840
 841
 842
 843
 844
 845
 846
 847
 848
 849
 850
 851
 852
 853
 854
 855
 856
 857
 858
 859
 860
 861
 862
 863
 864
 865
 866
 867
 868
 869
 870
 871
 872
 873
 874
 875
 876
 877
 878
 879
 880
 881
 882
 883
 884
 885
 886
 887
 888
 889
 890
 891
 892
 893
 894
 895
 896
 897
 898
 899
 900
 901
 902
 903
 904
 905
 906
 907
 908
 909
 910
 911
 912
 913
 914
 915
 916
 917
 918
 919
 920
 921
 922
 923
 924
 925
 926
 927
 928
 929
 930
 931
 932
 933
 934
 935
 936
 937
 938
 939
 940
 941
 942
 943
 944
 945
 946
 947
 948
 949
 950
 951
 952
 953
 954
 955
 956
 957
 958
 959
 960
 961
 962
 963
 964
 965
 966
 967
 968
 969
 970
 971
 972
 973
 974
 975
 976
 977
 978
 979
 980
 981
 982
 983
 984
 985
 986
 987
 988
 989
 990
 991
 992
 993
 994
 995
 996
 997
 998
 999
1000
1001
1002
1003
1004
1005
1006
1007
1008
1009
1010
1011
1012
1013
1014
1015
1016
1017
1018
1019
```
| ```
def __init__(
    self: AppType,
    *,
    debug: Annotated[
        bool,
        Doc(
            """
            Boolean indicating if debug tracebacks should be returned on server
            errors.

            Read more in the
            [Starlette docs for Applications](https://www.starlette.dev/applications/#instantiating-the-application).
            """
        ),
    ] = False,
    routes: Annotated[
        list[BaseRoute] | None,
        Doc(
            """
            **Note**: you probably shouldn't use this parameter, it is inherited
            from Starlette and supported for compatibility.

            ---

            A list of routes to serve incoming HTTP and WebSocket requests.
            """
        ),
        deprecated(
            """
            You normally wouldn't use this parameter with FastAPI, it is inherited
            from Starlette and supported for compatibility.

            In FastAPI, you normally would use the *path operation methods*,
            like `app.get()`, `app.post()`, etc.
            """
        ),
    ] = None,
    title: Annotated[
        str,
        Doc(
            """
            The title of the API.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Read more in the
            [FastAPI docs for Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-api).

            **Example**

        ```python
            from fastapi import FastAPI

            app = FastAPI(title="ChimichangApp")
        ```
            """
        ),
    ] = "FastAPI",
    summary: Annotated[
        str | None,
        Doc(
            """
            A short summary of the API.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Read more in the
            [FastAPI docs for Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-api).

            **Example**

        ```python
            from fastapi import FastAPI

            app = FastAPI(summary="Deadpond's favorite app. Nuff said.")
        ```
            """
        ),
    ] = None,
    description: Annotated[
        str,
        Doc(
            '''
            A description of the API. Supports Markdown (using
            [CommonMark syntax](https://commonmark.org/)).

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Read more in the
            [FastAPI docs for Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-api).

            **Example**

        ```python
            from fastapi import FastAPI

            app = FastAPI(
                description="""
                            ChimichangApp API helps you do awesome stuff. 🚀

                            ## Items

                            You can **read items**.

                            ## Users

                            You will be able to:

                            * **Create users** (_not implemented_).
                            * **Read users** (_not implemented_).

                            """
            )
        ```
            '''
        ),
    ] = "",
    version: Annotated[
        str,
        Doc(
            """
            The version of the API.

            **Note** This is the version of your application, not the version of
            the OpenAPI specification nor the version of FastAPI being used.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Read more in the
            [FastAPI docs for Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-api).

            **Example**

        ```python
            from fastapi import FastAPI

            app = FastAPI(version="0.0.1")
        ```
            """
        ),
    ] = "0.1.0",
    openapi_url: Annotated[
        str | None,
        Doc(
            """
            The URL where the OpenAPI schema will be served from.

            If you set it to `None`, no OpenAPI schema will be served publicly, and
            the default automatic endpoints `/docs` and `/redoc` will also be
            disabled.

            Read more in the
            [FastAPI docs for Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/#openapi-url).

            **Example**

        ```python
            from fastapi import FastAPI

            app = FastAPI(openapi_url="/api/v1/openapi.json")
        ```
            """
        ),
    ] = "/openapi.json",
    openapi_tags: Annotated[
        list[dict[str, Any]] | None,
        Doc(
            """
            A list of tags used by OpenAPI, these are the same `tags` you can set
            in the *path operations*, like:

            * `@app.get("/users/", tags=["users"])`
            * `@app.get("/items/", tags=["items"])`

            The order of the tags can be used to specify the order shown in
            tools like Swagger UI, used in the automatic path `/docs`.

            It's not required to specify all the tags used.

            The tags that are not declared MAY be organized randomly or based
            on the tools' logic. Each tag name in the list MUST be unique.

            The value of each item is a `dict` containing:

            * `name`: The name of the tag.
            * `description`: A short description of the tag.
                [CommonMark syntax](https://commonmark.org/) MAY be used for rich
                text representation.
            * `externalDocs`: Additional external documentation for this tag. If
                provided, it would contain a `dict` with:
                * `description`: A short description of the target documentation.
                    [CommonMark syntax](https://commonmark.org/) MAY be used for
                    rich text representation.
                * `url`: The URL for the target documentation. Value MUST be in
                    the form of a URL.

            Read more in the
            [FastAPI docs for Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-tags).

            **Example**

        ```python
            from fastapi import FastAPI

            tags_metadata = [
                {
                    "name": "users",
                    "description": "Operations with users. The **login** logic is also here.",
                },
                {
                    "name": "items",
                    "description": "Manage items. So _fancy_ they have their own docs.",
                    "externalDocs": {
                        "description": "Items external docs",
                        "url": "https://fastapi.tiangolo.com/",
                    },
                },
            ]

            app = FastAPI(openapi_tags=tags_metadata)
        ```
            """
        ),
    ] = None,
    servers: Annotated[
        list[dict[str, str | Any]] | None,
        Doc(
            """
            A `list` of `dict`s with connectivity information to a target server.

            You would use it, for example, if your application is served from
            different domains and you want to use the same Swagger UI in the
            browser to interact with each of them (instead of having multiple
            browser tabs open). Or if you want to leave fixed the possible URLs.

            If the servers `list` is not provided, or is an empty `list`, the
            `servers` property in the generated OpenAPI will be:

            * a `dict` with a `url` value of the application's mounting point
            (`root_path`) if it's different from `/`.
            * otherwise, the `servers` property will be omitted from the OpenAPI
            schema.

            Each item in the `list` is a `dict` containing:

            * `url`: A URL to the target host. This URL supports Server Variables
            and MAY be relative, to indicate that the host location is relative
            to the location where the OpenAPI document is being served. Variable
            substitutions will be made when a variable is named in `{`brackets`}`.
            * `description`: An optional string describing the host designated by
            the URL. [CommonMark syntax](https://commonmark.org/) MAY be used for
            rich text representation.
            * `variables`: A `dict` between a variable name and its value. The value
                is used for substitution in the server's URL template.

            Read more in the
            [FastAPI docs for Behind a Proxy](https://fastapi.tiangolo.com/advanced/behind-a-proxy/#additional-servers).

            **Example**

        ```python
            from fastapi import FastAPI

            app = FastAPI(
                servers=[
                    {"url": "https://stag.example.com", "description": "Staging environment"},
                    {"url": "https://prod.example.com", "description": "Production environment"},
                ]
            )
        ```
            """
        ),
    ] = None,
    dependencies: Annotated[
        Sequence[Depends] | None,
        Doc(
            """
            A list of global dependencies, they will be applied to each
            *path operation*, including in sub-routers.

            Read more about it in the
            [FastAPI docs for Global Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/global-dependencies/).

            **Example**

        ```python
            from fastapi import Depends, FastAPI

            from .dependencies import func_dep_1, func_dep_2

            app = FastAPI(dependencies=[Depends(func_dep_1), Depends(func_dep_2)])
        ```
            """
        ),
    ] = None,
    default_response_class: Annotated[
        type[Response],
        Doc(
            """
            The default response class to be used.

            Read more in the
            [FastAPI docs for Custom Response - HTML, Stream, File, others](https://fastapi.tiangolo.com/advanced/custom-response/#default-response-class).

            **Example**

        ```python
            from fastapi import FastAPI
            from fastapi.responses import ORJSONResponse

            app = FastAPI(default_response_class=ORJSONResponse)
        ```
            """
        ),
    ] = Default(JSONResponse),
    redirect_slashes: Annotated[
        bool,
        Doc(
            """
            Whether to detect and redirect slashes in URLs when the client doesn't
            use the same format.

            **Example**

        ```python
            from fastapi import FastAPI

            app = FastAPI(redirect_slashes=True)  # the default

            @app.get("/items/")
            async def read_items():
                return [{"item_id": "Foo"}]
        ```

            With this app, if a client goes to `/items` (without a trailing slash),
            they will be automatically redirected with an HTTP status code of 307
            to `/items/`.
            """
        ),
    ] = True,
    docs_url: Annotated[
        str | None,
        Doc(
            """
            The path to the automatic interactive API documentation.
            It is handled in the browser by Swagger UI.

            The default URL is `/docs`. You can disable it by setting it to `None`.

            If `openapi_url` is set to `None`, this will be automatically disabled.

            Read more in the
            [FastAPI docs for Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/#docs-urls).

            **Example**

        ```python
            from fastapi import FastAPI

            app = FastAPI(docs_url="/documentation", redoc_url=None)
        ```
            """
        ),
    ] = "/docs",
    redoc_url: Annotated[
        str | None,
        Doc(
            """
            The path to the alternative automatic interactive API documentation
            provided by ReDoc.

            The default URL is `/redoc`. You can disable it by setting it to `None`.

            If `openapi_url` is set to `None`, this will be automatically disabled.

            Read more in the
            [FastAPI docs for Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/#docs-urls).

            **Example**

        ```python
            from fastapi import FastAPI

            app = FastAPI(docs_url="/documentation", redoc_url="redocumentation")
        ```
            """
        ),
    ] = "/redoc",
    swagger_ui_oauth2_redirect_url: Annotated[
        str | None,
        Doc(
            """
            The OAuth2 redirect endpoint for the Swagger UI.

            By default it is `/docs/oauth2-redirect`.

            This is only used if you use OAuth2 (with the "Authorize" button)
            with Swagger UI.
            """
        ),
    ] = "/docs/oauth2-redirect",
    swagger_ui_init_oauth: Annotated[
        dict[str, Any] | None,
        Doc(
            """
            OAuth2 configuration for the Swagger UI, by default shown at `/docs`.

            Read more about the available configuration options in the
            [Swagger UI docs](https://swagger.io/docs/open-source-tools/swagger-ui/usage/oauth2/).
            """
        ),
    ] = None,
    middleware: Annotated[
        Sequence[Middleware] | None,
        Doc(
            """
            List of middleware to be added when creating the application.

            In FastAPI you would normally do this with `app.add_middleware()`
            instead.

            Read more in the
            [FastAPI docs for Middleware](https://fastapi.tiangolo.com/tutorial/middleware/).
            """
        ),
    ] = None,
    exception_handlers: Annotated[
        dict[
            int | type[Exception],
            Callable[[Request, Any], Coroutine[Any, Any, Response]],
        ]
        | None,
        Doc(
            """
            A dictionary with handlers for exceptions.

            In FastAPI, you would normally use the decorator
            `@app.exception_handler()`.

            Read more in the
            [FastAPI docs for Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/).
            """
        ),
    ] = None,
    on_startup: Annotated[
        Sequence[Callable[[], Any]] | None,
        Doc(
            """
            A list of startup event handler functions.

            You should instead use the `lifespan` handlers.

            Read more in the [FastAPI docs for `lifespan`](https://fastapi.tiangolo.com/advanced/events/).
            """
        ),
    ] = None,
    on_shutdown: Annotated[
        Sequence[Callable[[], Any]] | None,
        Doc(
            """
            A list of shutdown event handler functions.

            You should instead use the `lifespan` handlers.

            Read more in the
            [FastAPI docs for `lifespan`](https://fastapi.tiangolo.com/advanced/events/).
            """
        ),
    ] = None,
    lifespan: Annotated[
        Lifespan[AppType] | None,
        Doc(
            """
            A `Lifespan` context manager handler. This replaces `startup` and
            `shutdown` functions with a single context manager.

            Read more in the
            [FastAPI docs for `lifespan`](https://fastapi.tiangolo.com/advanced/events/).
            """
        ),
    ] = None,
    terms_of_service: Annotated[
        str | None,
        Doc(
            """
            A URL to the Terms of Service for your API.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Read more at the
            [FastAPI docs for Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-api).

            **Example**

        ```python
            app = FastAPI(terms_of_service="http://example.com/terms/")
        ```
            """
        ),
    ] = None,
    contact: Annotated[
        dict[str, str | Any] | None,
        Doc(
            """
            A dictionary with the contact information for the exposed API.

            It can contain several fields.

            * `name`: (`str`) The name of the contact person/organization.
            * `url`: (`str`) A URL pointing to the contact information. MUST be in
                the format of a URL.
            * `email`: (`str`) The email address of the contact person/organization.
                MUST be in the format of an email address.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Read more at the
            [FastAPI docs for Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-api).

            **Example**

        ```python
            app = FastAPI(
                contact={
                    "name": "Deadpoolio the Amazing",
                    "url": "http://x-force.example.com/contact/",
                    "email": "dp@x-force.example.com",
                }
            )
        ```
            """
        ),
    ] = None,
    license_info: Annotated[
        dict[str, str | Any] | None,
        Doc(
            """
            A dictionary with the license information for the exposed API.

            It can contain several fields.

            * `name`: (`str`) **REQUIRED** (if a `license_info` is set). The
                license name used for the API.
            * `identifier`: (`str`) An [SPDX](https://spdx.dev/) license expression
                for the API. The `identifier` field is mutually exclusive of the `url`
                field. Available since OpenAPI 3.1.0, FastAPI 0.99.0.
            * `url`: (`str`) A URL to the license used for the API. This MUST be
                the format of a URL.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Read more at the
            [FastAPI docs for Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-api).

            **Example**

        ```python
            app = FastAPI(
                license_info={
                    "name": "Apache 2.0",
                    "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
                }
            )
        ```
            """
        ),
    ] = None,
    openapi_prefix: Annotated[
        str,
        Doc(
            """
            A URL prefix for the OpenAPI URL.
            """
        ),
        deprecated(
            """
            "openapi_prefix" has been deprecated in favor of "root_path", which
            follows more closely the ASGI standard, is simpler, and more
            automatic.
            """
        ),
    ] = "",
    root_path: Annotated[
        str,
        Doc(
            """
            A path prefix handled by a proxy that is not seen by the application
            but is seen by external clients, which affects things like Swagger UI.

            Read more about it at the
            [FastAPI docs for Behind a Proxy](https://fastapi.tiangolo.com/advanced/behind-a-proxy/).

            **Example**

        ```python
            from fastapi import FastAPI

            app = FastAPI(root_path="/api/v1")
        ```
            """
        ),
    ] = "",
    root_path_in_servers: Annotated[
        bool,
        Doc(
            """
            To disable automatically generating the URLs in the `servers` field
            in the autogenerated OpenAPI using the `root_path`.

            Read more about it in the
            [FastAPI docs for Behind a Proxy](https://fastapi.tiangolo.com/advanced/behind-a-proxy/#disable-automatic-server-from-root-path).

            **Example**

        ```python
            from fastapi import FastAPI

            app = FastAPI(root_path_in_servers=False)
        ```
            """
        ),
    ] = True,
    responses: Annotated[
        dict[int | str, dict[str, Any]] | None,
        Doc(
            """
            Additional responses to be shown in OpenAPI.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Read more about it in the
            [FastAPI docs for Additional Responses in OpenAPI](https://fastapi.tiangolo.com/advanced/additional-responses/).

            And in the
            [FastAPI docs for Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-an-apirouter-with-a-custom-prefix-tags-responses-and-dependencies).
            """
        ),
    ] = None,
    callbacks: Annotated[
        list[BaseRoute] | None,
        Doc(
            """
            OpenAPI callbacks that should apply to all *path operations*.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Read more about it in the
            [FastAPI docs for OpenAPI Callbacks](https://fastapi.tiangolo.com/advanced/openapi-callbacks/).
            """
        ),
    ] = None,
    webhooks: Annotated[
        routing.APIRouter | None,
        Doc(
            """
            Add OpenAPI webhooks. This is similar to `callbacks` but it doesn't
            depend on specific *path operations*.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            **Note**: This is available since OpenAPI 3.1.0, FastAPI 0.99.0.

            Read more about it in the
            [FastAPI docs for OpenAPI Webhooks](https://fastapi.tiangolo.com/advanced/openapi-webhooks/).
            """
        ),
    ] = None,
    deprecated: Annotated[
        bool | None,
        Doc(
            """
            Mark all *path operations* as deprecated. You probably don't need it,
            but it's available.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Read more about it in the
            [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/#deprecate-a-path-operation).
            """
        ),
    ] = None,
    include_in_schema: Annotated[
        bool,
        Doc(
            """
            To include (or not) all the *path operations* in the generated OpenAPI.
            You probably don't need it, but it's available.

            This affects the generated OpenAPI (e.g. visible at `/docs`).

            Read more about it in the
            [FastAPI docs for Query Parameters and String Validations](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#exclude-parameters-from-openapi).
            """
        ),
    ] = True,
    swagger_ui_parameters: Annotated[
        dict[str, Any] | None,
        Doc(
            """
            Parameters to configure Swagger UI, the autogenerated interactive API
            documentation (by default at `/docs`).

            Read more about it in the
            [FastAPI docs about how to Configure Swagger UI](https://fastapi.tiangolo.com/how-to/configure-swagger-ui/).
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
    separate_input_output_schemas: Annotated[
        bool,
        Doc(
            """
            Whether to generate separate OpenAPI schemas for request body and
            response body when the results would be more precise.

            This is particularly useful when automatically generating clients.

            For example, if you have a model like:

        ```python
            from pydantic import BaseModel

            class Item(BaseModel):
                name: str
                tags: list[str] = []
        ```
