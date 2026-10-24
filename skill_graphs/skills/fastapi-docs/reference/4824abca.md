##  fastapi.APIRouter [¶](https://fastapi.tiangolo.com/reference/apirouter/#fastapi.APIRouter "Permanent link")
```
APIRouter(
    *,
    prefix="",
    tags=None,
    dependencies=None,
    default_response_class=Default(JSONResponse[](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.responses.JSONResponse</span> \(<code>starlette.responses.JSONResponse</code>\)")),
    responses=None,
    callbacks=None,
    routes=None,
    redirect_slashes=True,
    default=None,
    dependency_overrides_provider=None,
    route_class=APIRoute,
    on_startup=None,
    on_shutdown=None,
    lifespan=None,
    deprecated=None,
    include_in_schema=True,
    generate_unique_id_function=Default(generate_unique_id),
    strict_content_type=Default(True)
)

```

Bases: `Router`
`APIRouter` class, used to group _path operations_ , for example to structure an app in multiple files. It would then be included in the `FastAPI` app, or in another `APIRouter` (ultimately included in the app).
Read more about it in the [FastAPI docs for Bigger Applications - Multiple Files](https://fastapi.tiangolo.com/tutorial/bigger-applications/).
#### Example[¶](https://fastapi.tiangolo.com/reference/apirouter/#fastapi.APIRouter--example)
```
from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


app.include_router(router)

```

PARAMETER | DESCRIPTION
---|---
`prefix` |  An optional path prefix for the router. **TYPE:** `str` **DEFAULT:** `''`
`tags` |  A list of tags to be applied to all the _path operations_ in this router. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/). **TYPE:** `list[str | Enum] | None` **DEFAULT:** `None`
`dependencies` |  A list of dependencies (using `Depends()`) to be applied to all the _path operations_ in this router. Read more about it in the [FastAPI docs for Bigger Applications - Multiple Files](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-an-apirouter-with-a-custom-prefix-tags-responses-and-dependencies). **TYPE:** `Sequence[Depends] | None` **DEFAULT:** `None`
`default_response_class` |  The default response class to be used. Read more in the [FastAPI docs for Custom Response - HTML, Stream, File, others](https://fastapi.tiangolo.com/advanced/custom-response/#default-response-class). **TYPE:** `type[Response[](https://fastapi.tiangolo.com/reference/response/#fastapi.Response "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.Response</span> \(<code>starlette.responses.Response</code>\)")]` **DEFAULT:** `Default(JSONResponse[](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.responses.JSONResponse</span> \(<code>starlette.responses.JSONResponse</code>\)"))`
`responses` |  Additional responses to be shown in OpenAPI. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for Additional Responses in OpenAPI](https://fastapi.tiangolo.com/advanced/additional-responses/). And in the [FastAPI docs for Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-an-apirouter-with-a-custom-prefix-tags-responses-and-dependencies). **TYPE:** `dict[int | str, dict[str, Any]] | None` **DEFAULT:** `None`
`callbacks` |  OpenAPI callbacks that should apply to all _path operations_ in this router. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for OpenAPI Callbacks](https://fastapi.tiangolo.com/advanced/openapi-callbacks/). **TYPE:** `list[BaseRoute] | None` **DEFAULT:** `None`
`routes` |  **Note** : you probably shouldn't use this parameter, it is inherited from Starlette and supported for compatibility.
* * *
A list of routes to serve incoming HTTP and WebSocket requests. **TYPE:** `list[BaseRoute] | None` **DEFAULT:** `None`
`redirect_slashes` |  Whether to detect and redirect slashes in URLs when the client doesn't use the same format. **TYPE:** `bool` **DEFAULT:** `True`
`default` |  Default function handler for this router. Used to handle 404 Not Found errors. **TYPE:** `ASGIApp | None` **DEFAULT:** `None`
`dependency_overrides_provider` |  Only used internally by FastAPI to handle dependency overrides. You shouldn't need to use it. It normally points to the `FastAPI` app object. **TYPE:** `Any | None` **DEFAULT:** `None`
`route_class` |  Custom route (_path operation_) class to be used by this router. Read more about it in the [FastAPI docs for Custom Request and APIRoute class](https://fastapi.tiangolo.com/how-to/custom-request-and-route/#custom-apiroute-class-in-a-router). **TYPE:** `type[APIRoute]` **DEFAULT:** `APIRoute`
`on_startup` |  A list of startup event handler functions. You should instead use the `lifespan` handlers. Read more in the [FastAPI docs for `lifespan`](https://fastapi.tiangolo.com/advanced/events/). **TYPE:** `Sequence[Callable[[], Any]] | None` **DEFAULT:** `None`
`on_shutdown` |  A list of shutdown event handler functions. You should instead use the `lifespan` handlers. Read more in the [FastAPI docs for `lifespan`](https://fastapi.tiangolo.com/advanced/events/). **TYPE:** `Sequence[Callable[[], Any]] | None` **DEFAULT:** `None`
`lifespan` |  A `Lifespan` context manager handler. This replaces `startup` and `shutdown` functions with a single context manager. Read more in the [FastAPI docs for `lifespan`](https://fastapi.tiangolo.com/advanced/events/). **TYPE:** `Lifespan[Any] | None` **DEFAULT:** `None`
`deprecated` |  Mark all _path operations_ in this router as deprecated. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/). **TYPE:** `bool | None` **DEFAULT:** `None`
`include_in_schema` |  To include (or not) all the _path operations_ in this router in the generated OpenAPI. This affects the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for Query Parameters and String Validations](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#exclude-parameters-from-openapi). **TYPE:** `bool` **DEFAULT:** `True`
`generate_unique_id_function` |  Customize the function used to generate unique IDs for the _path operations_ shown in the generated OpenAPI. This is particularly useful when automatically generating clients or SDKs for your API. Read more about it in the [FastAPI docs about how to Generate Clients](https://fastapi.tiangolo.com/advanced/generate-clients/#custom-generate-unique-id-function). **TYPE:** `Callable[[APIRoute], str]` **DEFAULT:** `Default(generate_unique_id)`
`strict_content_type` |  Enable strict checking for request Content-Type headers. When `True` (the default), requests with a body that do not include a `Content-Type` header will **not** be parsed as JSON. This prevents potential cross-site request forgery (CSRF) attacks that exploit the browser's ability to send requests without a Content-Type header, bypassing CORS preflight checks. In particular applicable for apps that need to be run locally (in localhost). When `False`, requests without a `Content-Type` header will have their body parsed as JSON, which maintains compatibility with certain clients that don't send `Content-Type` headers. Read more about it in the [FastAPI docs for Strict Content-Type](https://fastapi.tiangolo.com/advanced/strict-content-type/). **TYPE:** `bool` **DEFAULT:** `Default(True)`
Source code in `fastapi/routing.py`
```
1028
1029
1030
1031
1032
1033
1034
1035
1036
1037
1038
1039
1040
1041
1042
1043
1044
1045
1046
1047
1048
1049
1050
1051
1052
1053
1054
1055
1056
1057
1058
1059
1060
1061
1062
1063
1064
1065
1066
1067
1068
1069
1070
1071
1072
1073
1074
1075
1076
1077
1078
1079
1080
1081
1082
1083
1084
1085
1086
1087
1088
1089
1090
1091
1092
1093
1094
1095
1096
1097
1098
1099
1100
1101
1102
1103
1104
1105
1106
1107
1108
1109
1110
1111
1112
1113
1114
1115
1116
1117
1118
1119
1120
1121
1122
1123
1124
1125
1126
1127
1128
1129
1130
1131
1132
1133
1134
1135
1136
1137
1138
1139
1140
1141
1142
1143
1144
1145
1146
1147
1148
1149
1150
1151
1152
1153
1154
1155
1156
1157
1158
1159
1160
1161
1162
1163
1164
1165
1166
1167
1168
1169
1170
1171
1172
1173
1174
1175
1176
1177
1178
1179
1180
1181
1182
1183
1184
1185
1186
1187
1188
1189
1190
1191
1192
1193
1194
1195
1196
1197
1198
1199
1200
1201
1202
1203
1204
1205
1206
1207
1208
1209
1210
1211
1212
1213
1214
1215
1216
1217
1218
1219
1220
1221
1222
1223
1224
1225
1226
1227
1228
1229
1230
1231
1232
1233
1234
1235
1236
1237
1238
1239
1240
1241
1242
1243
1244
1245
1246
1247
1248
1249
1250
1251
1252
1253
1254
1255
1256
1257
1258
1259
1260
1261
1262
1263
1264
1265
1266
1267
1268
1269
1270
1271
1272
1273
1274
1275
1276
1277
1278
1279
1280
1281
1282
1283
1284
1285
1286
1287
1288
1289
1290
1291
1292
1293
1294
1295
1296
1297
1298
1299
1300
1301
1302
1303
1304
1305
1306
1307
1308
1309
1310
1311
```
| ```
def __init__(
    self,
    *,
    prefix: Annotated[str, Doc("An optional path prefix for the router.")] = "",
    tags: Annotated[
        list[str | Enum] | None,
        Doc(
            """
            A list of tags to be applied to all the *path operations* in this
            router.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Read more about it in the
            [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/).
            """
        ),
    ] = None,
    dependencies: Annotated[
        Sequence[params.Depends] | None,
        Doc(
            """
            A list of dependencies (using `Depends()`) to be applied to all the
            *path operations* in this router.

            Read more about it in the
            [FastAPI docs for Bigger Applications - Multiple Files](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-an-apirouter-with-a-custom-prefix-tags-responses-and-dependencies).
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
            """
        ),
    ] = Default(JSONResponse),
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
            OpenAPI callbacks that should apply to all *path operations* in this
            router.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Read more about it in the
            [FastAPI docs for OpenAPI Callbacks](https://fastapi.tiangolo.com/advanced/openapi-callbacks/).
            """
        ),
    ] = None,
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
            like `router.get()`, `router.post()`, etc.
            """
        ),
    ] = None,
    redirect_slashes: Annotated[
        bool,
        Doc(
            """
            Whether to detect and redirect slashes in URLs when the client doesn't
            use the same format.
            """
        ),
    ] = True,
    default: Annotated[
        ASGIApp | None,
        Doc(
            """
            Default function handler for this router. Used to handle
            404 Not Found errors.
            """
        ),
    ] = None,
    dependency_overrides_provider: Annotated[
        Any | None,
        Doc(
            """
            Only used internally by FastAPI to handle dependency overrides.

            You shouldn't need to use it. It normally points to the `FastAPI` app
            object.
            """
        ),
    ] = None,
    route_class: Annotated[
        type[APIRoute],
        Doc(
            """
            Custom route (*path operation*) class to be used by this router.

            Read more about it in the
            [FastAPI docs for Custom Request and APIRoute class](https://fastapi.tiangolo.com/how-to/custom-request-and-route/#custom-apiroute-class-in-a-router).
            """
        ),
    ] = APIRoute,
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
    # the generic to Lifespan[AppType] is the type of the top level application
    # which the router cannot know statically, so we use typing.Any
    lifespan: Annotated[
        Lifespan[Any] | None,
        Doc(
            """
            A `Lifespan` context manager handler. This replaces `startup` and
            `shutdown` functions with a single context manager.

            Read more in the
            [FastAPI docs for `lifespan`](https://fastapi.tiangolo.com/advanced/events/).
            """
        ),
    ] = None,
    deprecated: Annotated[
        bool | None,
        Doc(
            """
            Mark all *path operations* in this router as deprecated.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Read more about it in the
            [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/).
            """
        ),
    ] = None,
    include_in_schema: Annotated[
        bool,
        Doc(
            """
            To include (or not) all the *path operations* in this router in the
            generated OpenAPI.

            This affects the generated OpenAPI (e.g. visible at `/docs`).

            Read more about it in the
            [FastAPI docs for Query Parameters and String Validations](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#exclude-parameters-from-openapi).
            """
        ),
    ] = True,
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
    strict_content_type: Annotated[
        bool,
        Doc(
            """
            Enable strict checking for request Content-Type headers.

            When `True` (the default), requests with a body that do not include
            a `Content-Type` header will **not** be parsed as JSON.

            This prevents potential cross-site request forgery (CSRF) attacks
            that exploit the browser's ability to send requests without a
            Content-Type header, bypassing CORS preflight checks. In particular
            applicable for apps that need to be run locally (in localhost).

            When `False`, requests without a `Content-Type` header will have
            their body parsed as JSON, which maintains compatibility with
            certain clients that don't send `Content-Type` headers.

            Read more about it in the
            [FastAPI docs for Strict Content-Type](https://fastapi.tiangolo.com/advanced/strict-content-type/).
            """
        ),
    ] = Default(True),
) -> None:
    # Determine the lifespan context to use
    if lifespan is None:
        # Use the default lifespan that runs on_startup/on_shutdown handlers
        lifespan_context: Lifespan[Any] = _DefaultLifespan(self)
    elif inspect.isasyncgenfunction(lifespan):
        lifespan_context = asynccontextmanager(lifespan)
    elif inspect.isgeneratorfunction(lifespan):
        lifespan_context = _wrap_gen_lifespan_context(lifespan)
    else:
        lifespan_context = lifespan
    self.lifespan_context = lifespan_context

    super().__init__(
        routes=routes,
        redirect_slashes=redirect_slashes,
        default=default,
        lifespan=lifespan_context,
    )
    if prefix:
        assert prefix.startswith("/"), "A path prefix must start with '/'"
        assert not prefix.endswith("/"), (
            "A path prefix must not end with '/', as the routes will start with '/'"
        )

    # Handle on_startup/on_shutdown locally since Starlette removed support
    # Ref: https://github.com/Kludex/starlette/pull/3117
    # TODO: deprecate this once the lifespan (or alternative) interface is improved
    self.on_startup: list[Callable[[], Any]] = (
        [] if on_startup is None else list(on_startup)
    )
    self.on_shutdown: list[Callable[[], Any]] = (
        [] if on_shutdown is None else list(on_shutdown)
    )

    self.prefix = prefix
    self.tags: list[str | Enum] = tags or []
    self.dependencies = list(dependencies or [])
    self.deprecated = deprecated
    self.include_in_schema = include_in_schema
    self.responses = responses or {}
    self.callbacks = callbacks or []
    self.dependency_overrides_provider = dependency_overrides_provider
    self.route_class = route_class
    self.default_response_class = default_response_class
    self.generate_unique_id_function = generate_unique_id_function
    self.strict_content_type = strict_content_type

```

---|---
###  websocket [¶](https://fastapi.tiangolo.com/reference/apirouter/#fastapi.APIRouter.websocket "Permanent link")
```
websocket(path, name=None, *, dependencies=None)

```

Decorate a WebSocket function.
Read more about it in the [FastAPI docs for WebSockets](https://fastapi.tiangolo.com/advanced/websockets/).
**Example**
##### Example[¶](https://fastapi.tiangolo.com/reference/apirouter/#fastapi.APIRouter.websocket--example)
```
from fastapi import APIRouter, FastAPI, WebSocket

app = FastAPI()
router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

app.include_router(router)

```

PARAMETER | DESCRIPTION
---|---
`path` |  WebSocket path. **TYPE:** `str`
`name` |  A name for the WebSocket. Only used internally. **TYPE:** `str | None` **DEFAULT:** `None`
`dependencies` |  A list of dependencies (using `Depends()`) to be used for this WebSocket. Read more about it in the [FastAPI docs for WebSockets](https://fastapi.tiangolo.com/advanced/websockets/). **TYPE:** `Sequence[Depends] | None` **DEFAULT:** `None`
Source code in `fastapi/routing.py`
```
1498
1499
1500
1501
1502
1503
1504
1505
1506
1507
1508
1509
1510
1511
1512
1513
1514
1515
1516
1517
1518
1519
1520
1521
1522
1523
1524
1525
1526
1527
1528
1529
1530
1531
1532
1533
1534
1535
1536
1537
1538
1539
1540
1541
1542
1543
1544
1545
1546
1547
1548
1549
1550
1551
1552
1553
1554
1555
1556
1557
1558
1559
1560
1561
1562
1563
```
| ```
def websocket(
    self,
    path: Annotated[
        str,
        Doc(
            """
            WebSocket path.
            """
        ),
    ],
    name: Annotated[
        str | None,
        Doc(
            """
            A name for the WebSocket. Only used internally.
            """
        ),
    ] = None,
    *,
    dependencies: Annotated[
        Sequence[params.Depends] | None,
        Doc(
            """
            A list of dependencies (using `Depends()`) to be used for this
            WebSocket.

            Read more about it in the
            [FastAPI docs for WebSockets](https://fastapi.tiangolo.com/advanced/websockets/).
            """
        ),
    ] = None,
) -> Callable[[DecoratedCallable], DecoratedCallable]:
    """
    Decorate a WebSocket function.

    Read more about it in the
    [FastAPI docs for WebSockets](https://fastapi.tiangolo.com/advanced/websockets/).

    **Example**

    ## Example

```python
    from fastapi import APIRouter, FastAPI, WebSocket

    app = FastAPI()
    router = APIRouter()

    @router.websocket("/ws")
    async def websocket_endpoint(websocket: WebSocket):
        await websocket.accept()
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")

    app.include_router(router)
```
    """

    def decorator(func: DecoratedCallable) -> DecoratedCallable:
        self.add_api_websocket_route(
            path, func, name=name, dependencies=dependencies
        )
        return func

    return decorator

```

---|---
###  include_router [¶](https://fastapi.tiangolo.com/reference/apirouter/#fastapi.APIRouter.include_router "Permanent link")
```
include_router(
    router,
    *,
    prefix="",
    tags=None,
    dependencies=None,
    default_response_class=Default(JSONResponse[](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.responses.JSONResponse</span> \(<code>starlette.responses.JSONResponse</code>\)")),
    responses=None,
    callbacks=None,
    deprecated=None,
    include_in_schema=True,
    generate_unique_id_function=Default(generate_unique_id)
)

```

Include another `APIRouter` in the same current `APIRouter`.
Read more about it in the [FastAPI docs for Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/).
##### Example[¶](https://fastapi.tiangolo.com/reference/apirouter/#fastapi.APIRouter.include_router--example)
```
from fastapi import APIRouter, FastAPI

app = FastAPI()
internal_router = APIRouter()
users_router = APIRouter()

@users_router.get("/users/")
def read_users():
    return [{"name": "Rick"}, {"name": "Morty"}]

internal_router.include_router(users_router)
app.include_router(internal_router)

```

PARAMETER | DESCRIPTION
---|---
`router` |  The `APIRouter` to include. **TYPE:** `APIRouter[](https://fastapi.tiangolo.com/reference/apirouter/#fastapi.APIRouter "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.APIRouter</span> \(<code>fastapi.routing.APIRouter</code>\)")`
`prefix` |  An optional path prefix for the router. **TYPE:** `str` **DEFAULT:** `''`
`tags` |  A list of tags to be applied to all the _path operations_ in this router. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/). **TYPE:** `list[str | Enum] | None` **DEFAULT:** `None`
`dependencies` |  A list of dependencies (using `Depends()`) to be applied to all the _path operations_ in this router. Read more about it in the [FastAPI docs for Bigger Applications - Multiple Files](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-an-apirouter-with-a-custom-prefix-tags-responses-and-dependencies). **TYPE:** `Sequence[Depends] | None` **DEFAULT:** `None`
