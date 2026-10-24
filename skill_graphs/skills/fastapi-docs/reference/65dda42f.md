
            When `Item` is used for input, a request body, `tags` is not required,
            the client doesn't have to provide it.

            But when using `Item` for output, for a response body, `tags` is always
            available because it has a default value, even if it's just an empty
            list. So, the client should be able to always expect it.

            In this case, there would be two different schemas, one for input and
            another one for output.

            Read more about it in the
            [FastAPI docs about how to separate schemas for input and output](https://fastapi.tiangolo.com/how-to/separate-openapi-schemas)
            """
        ),
    ] = True,
    openapi_external_docs: Annotated[
        dict[str, Any] | None,
        Doc(
            """
            This field allows you to provide additional external documentation links.
            If provided, it must be a dictionary containing:

            * `description`: A brief description of the external documentation.
            * `url`: The URL pointing to the external documentation. The value **MUST**
            be a valid URL format.

            **Example**:

        ```python
            from fastapi import FastAPI

            external_docs = {
                "description": "Detailed API Reference",
                "url": "https://example.com/api-docs",
            }

            app = FastAPI(openapi_external_docs=external_docs)
        ```
            """
        ),
    ] = None,
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
    ] = True,
    **extra: Annotated[
        Any,
        Doc(
            """
            Extra keyword arguments to be stored in the app, not used by FastAPI
            anywhere.
            """
        ),
    ],
) -> None:
    self.debug = debug
    self.title = title
    self.summary = summary
    self.description = description
    self.version = version
    self.terms_of_service = terms_of_service
    self.contact = contact
    self.license_info = license_info
    self.openapi_url = openapi_url
    self.openapi_tags = openapi_tags
    self.root_path_in_servers = root_path_in_servers
    self.docs_url = docs_url
    self.redoc_url = redoc_url
    self.swagger_ui_oauth2_redirect_url = swagger_ui_oauth2_redirect_url
    self.swagger_ui_init_oauth = swagger_ui_init_oauth
    self.swagger_ui_parameters = swagger_ui_parameters
    self.servers = servers or []
    self.separate_input_output_schemas = separate_input_output_schemas
    self.openapi_external_docs = openapi_external_docs
    self.extra = extra
    self.openapi_version: Annotated[
        str,
        Doc(
            """
            The version string of OpenAPI.

            FastAPI will generate OpenAPI version 3.1.0, and will output that as
            the OpenAPI version. But some tools, even though they might be
            compatible with OpenAPI 3.1.0, might not recognize it as a valid.

            So you could override this value to trick those tools into using
            the generated OpenAPI. Have in mind that this is a hack. But if you
            avoid using features added in OpenAPI 3.1.0, it might work for your
            use case.

            This is not passed as a parameter to the `FastAPI` class to avoid
            giving the false idea that FastAPI would generate a different OpenAPI
            schema. It is only available as an attribute.

            **Example**

        ```python
            from fastapi import FastAPI

            app = FastAPI()

            app.openapi_version = "3.0.2"
        ```
            """
        ),
    ] = "3.1.0"
    self.openapi_schema: dict[str, Any] | None = None
    if self.openapi_url:
        assert self.title, "A title must be provided for OpenAPI, e.g.: 'My API'"
        assert self.version, "A version must be provided for OpenAPI, e.g.: '2.1.0'"
    # TODO: remove when discarding the openapi_prefix parameter
    if openapi_prefix:
        logger.warning(
            '"openapi_prefix" has been deprecated in favor of "root_path", which '
            "follows more closely the ASGI standard, is simpler, and more "
            "automatic. Check the docs at "
            "https://fastapi.tiangolo.com/advanced/sub-applications/"
        )
    self.webhooks: Annotated[
        routing.APIRouter,
        Doc(
            """
            The `app.webhooks` attribute is an `APIRouter` with the *path
            operations* that will be used just for documentation of webhooks.

            Read more about it in the
            [FastAPI docs for OpenAPI Webhooks](https://fastapi.tiangolo.com/advanced/openapi-webhooks/).
            """
        ),
    ] = webhooks or routing.APIRouter()
    self.root_path = root_path or openapi_prefix
    self.state: Annotated[
        State,
        Doc(
            """
            A state object for the application. This is the same object for the
            entire application, it doesn't change from request to request.

            You normally wouldn't use this in FastAPI, for most of the cases you
            would instead use FastAPI dependencies.

            This is simply inherited from Starlette.

            Read more about it in the
            [Starlette docs for Applications](https://www.starlette.dev/applications/#storing-state-on-the-app-instance).
            """
        ),
    ] = State()
    self.dependency_overrides: Annotated[
        dict[Callable[..., Any], Callable[..., Any]],
        Doc(
            """
            A dictionary with overrides for the dependencies.

            Each key is the original dependency callable, and the value is the
            actual dependency that should be called.

            This is for testing, to replace expensive dependencies with testing
            versions.

            Read more about it in the
            [FastAPI docs for Testing Dependencies with Overrides](https://fastapi.tiangolo.com/advanced/testing-dependencies/).
            """
        ),
    ] = {}
    self.router: routing.APIRouter = routing.APIRouter(
        routes=routes,
        redirect_slashes=redirect_slashes,
        dependency_overrides_provider=self,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        lifespan=lifespan,
        default_response_class=default_response_class,
        dependencies=dependencies,
        callbacks=callbacks,
        deprecated=deprecated,
        include_in_schema=include_in_schema,
        responses=responses,
        generate_unique_id_function=generate_unique_id_function,
        strict_content_type=strict_content_type,
    )
    self.exception_handlers: dict[
        Any, Callable[[Request, Any], Response | Awaitable[Response]]
    ] = {} if exception_handlers is None else dict(exception_handlers)
    self.exception_handlers.setdefault(HTTPException, http_exception_handler)
    self.exception_handlers.setdefault(
        RequestValidationError, request_validation_exception_handler
    )
    self.exception_handlers.setdefault(
        WebSocketRequestValidationError,
        # Starlette still has incorrect type specification for the handlers
        websocket_request_validation_exception_handler,  # type: ignore
    )

    self.user_middleware: list[Middleware] = (
        [] if middleware is None else list(middleware)
    )
    self.middleware_stack: ASGIApp | None = None
    self.setup()

```

---|---
###  openapi_version `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/fastapi/#fastapi.FastAPI.openapi_version "Permanent link")
```
openapi_version = '3.1.0'

```

The version string of OpenAPI.
FastAPI will generate OpenAPI version 3.1.0, and will output that as the OpenAPI version. But some tools, even though they might be compatible with OpenAPI 3.1.0, might not recognize it as a valid.
So you could override this value to trick those tools into using the generated OpenAPI. Have in mind that this is a hack. But if you avoid using features added in OpenAPI 3.1.0, it might work for your use case.
This is not passed as a parameter to the `FastAPI` class to avoid giving the false idea that FastAPI would generate a different OpenAPI schema. It is only available as an attribute.
**Example**
```
from fastapi import FastAPI

app = FastAPI()

app.openapi_version = "3.0.2"

```

###  webhooks `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/fastapi/#fastapi.FastAPI.webhooks "Permanent link")
```
webhooks = webhooks or APIRouter[](https://fastapi.tiangolo.com/reference/apirouter/#fastapi.APIRouter "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.APIRouter</span> \(<code>fastapi.routing.APIRouter</code>\)")()

```

The `app.webhooks` attribute is an `APIRouter` with the _path operations_ that will be used just for documentation of webhooks.
Read more about it in the [FastAPI docs for OpenAPI Webhooks](https://fastapi.tiangolo.com/advanced/openapi-webhooks/).
###  state `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/fastapi/#fastapi.FastAPI.state "Permanent link")
```
state = State()

```

A state object for the application. This is the same object for the entire application, it doesn't change from request to request.
You normally wouldn't use this in FastAPI, for most of the cases you would instead use FastAPI dependencies.
This is simply inherited from Starlette.
Read more about it in the
###  dependency_overrides `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/fastapi/#fastapi.FastAPI.dependency_overrides "Permanent link")
```
dependency_overrides = {}

```

A dictionary with overrides for the dependencies.
Each key is the original dependency callable, and the value is the actual dependency that should be called.
This is for testing, to replace expensive dependencies with testing versions.
Read more about it in the [FastAPI docs for Testing Dependencies with Overrides](https://fastapi.tiangolo.com/advanced/testing-dependencies/).
###  openapi [¶](https://fastapi.tiangolo.com/reference/fastapi/#fastapi.FastAPI.openapi "Permanent link")
```
openapi()

```

Generate the OpenAPI schema of the application. This is called by FastAPI internally.
The first time it is called it stores the result in the attribute `app.openapi_schema`, and next times it is called, it just returns that same result. To avoid the cost of generating the schema every time.
If you need to modify the generated OpenAPI schema, you could modify it.
Read more in the [FastAPI docs for OpenAPI](https://fastapi.tiangolo.com/how-to/extending-openapi/).
Source code in `fastapi/applications.py`
```
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
```
| ```
def openapi(self) -> dict[str, Any]:
    """
    Generate the OpenAPI schema of the application. This is called by FastAPI
    internally.

    The first time it is called it stores the result in the attribute
    `app.openapi_schema`, and next times it is called, it just returns that same
    result. To avoid the cost of generating the schema every time.

    If you need to modify the generated OpenAPI schema, you could modify it.

    Read more in the
    [FastAPI docs for OpenAPI](https://fastapi.tiangolo.com/how-to/extending-openapi/).
    """
    if not self.openapi_schema:
        self.openapi_schema = get_openapi(
            title=self.title,
            version=self.version,
            openapi_version=self.openapi_version,
            summary=self.summary,
            description=self.description,
            terms_of_service=self.terms_of_service,
            contact=self.contact,
            license_info=self.license_info,
            routes=self.routes,
            webhooks=self.webhooks.routes,
            tags=self.openapi_tags,
            servers=self.servers,
            separate_input_output_schemas=self.separate_input_output_schemas,
            external_docs=self.openapi_external_docs,
        )
    return self.openapi_schema

```

---|---
###  websocket [¶](https://fastapi.tiangolo.com/reference/fastapi/#fastapi.FastAPI.websocket "Permanent link")
```
websocket(path, name=None, *, dependencies=None)

```

Decorate a WebSocket function.
Read more about it in the [FastAPI docs for WebSockets](https://fastapi.tiangolo.com/advanced/websockets/).
**Example**
```
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

```

PARAMETER | DESCRIPTION
---|---
`path` |  WebSocket path. **TYPE:** `str`
`name` |  A name for the WebSocket. Only used internally. **TYPE:** `str | None` **DEFAULT:** `None`
`dependencies` |  A list of dependencies (using `Depends()`) to be used for this WebSocket. Read more about it in the [FastAPI docs for WebSockets](https://fastapi.tiangolo.com/advanced/websockets/). **TYPE:** `Sequence[Depends] | None` **DEFAULT:** `None`
Source code in `fastapi/applications.py`
```
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
1312
1313
1314
1315
1316
1317
1318
1319
1320
1321
1322
1323
1324
1325
1326
1327
1328
1329
1330
1331
1332
1333
1334
1335
1336
1337
1338
1339
1340
1341
1342
1343
1344
1345
1346
1347
1348
1349
1350
1351
1352
1353
1354
1355
1356
1357
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
        Sequence[Depends] | None,
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

```python
    from fastapi import FastAPI, WebSocket

    app = FastAPI()

    @app.websocket("/ws")
    async def websocket_endpoint(websocket: WebSocket):
        await websocket.accept()
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
```
    """

    def decorator(func: DecoratedCallable) -> DecoratedCallable:
        self.add_api_websocket_route(
            path,
            func,
            name=name,
            dependencies=dependencies,
        )
        return func

    return decorator

```

---|---
###  include_router [¶](https://fastapi.tiangolo.com/reference/fastapi/#fastapi.FastAPI.include_router "Permanent link")
```
include_router(
    router,
    *,
    prefix="",
    tags=None,
    dependencies=None,
    responses=None,
    deprecated=None,
    include_in_schema=True,
    default_response_class=Default(JSONResponse[](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.responses.JSONResponse</span> \(<code>starlette.responses.JSONResponse</code>\)")),
    callbacks=None,
    generate_unique_id_function=Default(generate_unique_id)
)

```

Include an `APIRouter` in the same app.
Read more about it in the [FastAPI docs for Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/).
##### Example[¶](https://fastapi.tiangolo.com/reference/fastapi/#fastapi.FastAPI.include_router--example)
```
from fastapi import FastAPI

from .users import users_router

app = FastAPI()

app.include_router(users_router)

```

PARAMETER | DESCRIPTION
---|---
`router` |  The `APIRouter` to include. **TYPE:** `APIRouter[](https://fastapi.tiangolo.com/reference/apirouter/#fastapi.APIRouter "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.APIRouter</span> \(<code>fastapi.routing.APIRouter</code>\)")`
`prefix` |  An optional path prefix for the router. **TYPE:** `str` **DEFAULT:** `''`
`tags` |  A list of tags to be applied to all the _path operations_ in this router. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/). **TYPE:** `list[str | Enum] | None` **DEFAULT:** `None`
`dependencies` |  A list of dependencies (using `Depends()`) to be applied to all the _path operations_ in this router. Read more about it in the [FastAPI docs for Bigger Applications - Multiple Files](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-an-apirouter-with-a-custom-prefix-tags-responses-and-dependencies). **Example** ```
from fastapi import Depends, FastAPI

from .dependencies import get_token_header
from .internal import admin

app = FastAPI()

app.include_router(
    admin.router,
    dependencies=[Depends(get_token_header)],
)

```
**TYPE:** `Sequence[Depends] | None` **DEFAULT:** `None`
`responses` |  Additional responses to be shown in OpenAPI. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for Additional Responses in OpenAPI](https://fastapi.tiangolo.com/advanced/additional-responses/). And in the [FastAPI docs for Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-an-apirouter-with-a-custom-prefix-tags-responses-and-dependencies). **TYPE:** `dict[int | str, dict[str, Any]] | None` **DEFAULT:** `None`
`deprecated` |  Mark all the _path operations_ in this router as deprecated. It will be added to the generated OpenAPI (e.g. visible at `/docs`). **Example** ```
from fastapi import FastAPI

from .internal import old_api

app = FastAPI()

app.include_router(
    old_api.router,
    deprecated=True,
)

```
**TYPE:** `bool | None` **DEFAULT:** `None`
`include_in_schema` |  Include (or not) all the _path operations_ in this router in the generated OpenAPI schema. This affects the generated OpenAPI (e.g. visible at `/docs`). **Example** ```
from fastapi import FastAPI

from .internal import old_api

app = FastAPI()

app.include_router(
    old_api.router,
    include_in_schema=False,
)

```
**TYPE:** `bool` **DEFAULT:** `True`
`default_response_class` |  Default response class to be used for the _path operations_ in this router. Read more in the [FastAPI docs for Custom Response - HTML, Stream, File, others](https://fastapi.tiangolo.com/advanced/custom-response/#default-response-class). **Example** ```
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from .internal import old_api

app = FastAPI()

app.include_router(
    old_api.router,
    default_response_class=ORJSONResponse,
)

```
**TYPE:** `type[Response[](https://fastapi.tiangolo.com/reference/response/#fastapi.Response "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.Response</span> \(<code>starlette.responses.Response</code>\)")]` **DEFAULT:** `Default(JSONResponse[](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.responses.JSONResponse</span> \(<code>starlette.responses.JSONResponse</code>\)"))`
`callbacks` |  List of _path operations_ that will be used as OpenAPI callbacks. This is only for OpenAPI documentation, the callbacks won't be used directly. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for OpenAPI Callbacks](https://fastapi.tiangolo.com/advanced/openapi-callbacks/). **TYPE:** `list[BaseRoute] | None` **DEFAULT:** `None`
`generate_unique_id_function` |  Customize the function used to generate unique IDs for the _path operations_ shown in the generated OpenAPI. This is particularly useful when automatically generating clients or SDKs for your API. Read more about it in the [FastAPI docs about how to Generate Clients](https://fastapi.tiangolo.com/advanced/generate-clients/#custom-generate-unique-id-function). **TYPE:** `Callable[[APIRoute], str]` **DEFAULT:** `Default(generate_unique_id)`
Source code in `fastapi/applications.py`
```
1359
1360
1361
1362
1363
1364
1365
1366
1367
1368
1369
1370
1371
1372
1373
1374
1375
1376
1377
1378
1379
1380
1381
1382
1383
1384
1385
1386
1387
1388
1389
1390
1391
1392
1393
1394
1395
1396
1397
1398
1399
1400
1401
1402
1403
1404
1405
1406
1407
1408
1409
1410
1411
1412
1413
1414
1415
1416
1417
1418
1419
1420
1421
1422
1423
1424
1425
1426
1427
1428
1429
1430
1431
1432
1433
1434
1435
1436
1437
1438
1439
1440
1441
1442
1443
1444
1445
1446
1447
1448
1449
1450
1451
1452
1453
1454
1455
1456
1457
1458
1459
1460
1461
1462
1463
1464
1465
1466
1467
1468
1469
1470
1471
1472
1473
1474
1475
1476
1477
1478
1479
1480
1481
1482
1483
1484
1485
1486
1487
1488
1489
1490
1491
1492
1493
1494
1495
1496
1497
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
```
| ```
def include_router(
    self,
    router: Annotated[routing.APIRouter, Doc("The `APIRouter` to include.")],
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
        Sequence[Depends] | None,
        Doc(
            """
            A list of dependencies (using `Depends()`) to be applied to all the
            *path operations* in this router.

            Read more about it in the
            [FastAPI docs for Bigger Applications - Multiple Files](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-an-apirouter-with-a-custom-prefix-tags-responses-and-dependencies).

            **Example**

        ```python
            from fastapi import Depends, FastAPI

            from .dependencies import get_token_header
            from .internal import admin

            app = FastAPI()

            app.include_router(
                admin.router,
                dependencies=[Depends(get_token_header)],
            )
        ```
            """
        ),
    ] = None,
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
    deprecated: Annotated[
        bool | None,
        Doc(
            """
            Mark all the *path operations* in this router as deprecated.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            **Example**

        ```python
            from fastapi import FastAPI

            from .internal import old_api

            app = FastAPI()

            app.include_router(
                old_api.router,
