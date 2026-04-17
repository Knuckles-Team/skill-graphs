##  fastapi.FastAPI [¶](https://fastapi.tiangolo.com/reference/fastapi/#fastapi.FastAPI "Permanent link")
```
FastAPI(
    *,
    debug=False,
    routes=None,
    title="FastAPI",
    summary=None,
    description="",
    version="0.1.0",
    openapi_url="/openapi.json",
    openapi_tags=None,
    servers=None,
    dependencies=None,
    default_response_class=Default(JSONResponse[](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.responses.JSONResponse</span> \(<code>starlette.responses.JSONResponse</code>\)")),
    redirect_slashes=True,
    docs_url="/docs",
    redoc_url="/redoc",
    swagger_ui_oauth2_redirect_url="/docs/oauth2-redirect",
    swagger_ui_init_oauth=None,
    middleware=None,
    exception_handlers=None,
    on_startup=None,
    on_shutdown=None,
    lifespan=None,
    terms_of_service=None,
    contact=None,
    license_info=None,
    openapi_prefix="",
    root_path="",
    root_path_in_servers=True,
    responses=None,
    callbacks=None,
    webhooks=None,
    deprecated=None,
    include_in_schema=True,
    swagger_ui_parameters=None,
    generate_unique_id_function=Default(generate_unique_id),
    separate_input_output_schemas=True,
    openapi_external_docs=None,
    strict_content_type=True,
    **extra
)

```

Bases: `Starlette`
`FastAPI` app class, the main entrypoint to use FastAPI.
Read more in the [FastAPI docs for First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/).
#### Example[¶](https://fastapi.tiangolo.com/reference/fastapi/#fastapi.FastAPI--example)
```
from fastapi import FastAPI

app = FastAPI()

```

PARAMETER | DESCRIPTION
---|---
`debug` |  Boolean indicating if debug tracebacks should be returned on server errors. Read more in the  **TYPE:** `bool` **DEFAULT:** `False`
`routes` |  **Note** : you probably shouldn't use this parameter, it is inherited from Starlette and supported for compatibility.
* * *
A list of routes to serve incoming HTTP and WebSocket requests. **TYPE:** `list[BaseRoute] | None` **DEFAULT:** `None`
`title` |  The title of the API. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more in the [FastAPI docs for Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-api). **Example** ```
from fastapi import FastAPI

app = FastAPI(title="ChimichangApp")

```
**TYPE:** `str` **DEFAULT:** `'FastAPI'`
`summary` |  A short summary of the API. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more in the [FastAPI docs for Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-api). **Example** ```
from fastapi import FastAPI

app = FastAPI(summary="Deadpond's favorite app. Nuff said.")

```
**TYPE:** `str | None` **DEFAULT:** `None`
`description` |  A description of the API. Supports Markdown (using  It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more in the [FastAPI docs for Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-api). **Example** ```
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
**TYPE:** `str` **DEFAULT:** `''`
`version` |  The version of the API. **Note** This is the version of your application, not the version of the OpenAPI specification nor the version of FastAPI being used. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more in the [FastAPI docs for Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-api). **Example** ```
from fastapi import FastAPI

app = FastAPI(version="0.0.1")

```
**TYPE:** `str` **DEFAULT:** `'0.1.0'`
`openapi_url` |  The URL where the OpenAPI schema will be served from. If you set it to `None`, no OpenAPI schema will be served publicly, and the default automatic endpoints `/docs` and `/redoc` will also be disabled. Read more in the [FastAPI docs for Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/#openapi-url). **Example** ```
from fastapi import FastAPI

app = FastAPI(openapi_url="/api/v1/openapi.json")

```
**TYPE:** `str | None` **DEFAULT:** `'/openapi.json'`
`openapi_tags` |  A list of tags used by OpenAPI, these are the same `tags` you can set in the _path operations_ , like:
  * `@app.get("/users/", tags=["users"])`
  * `@app.get("/items/", tags=["items"])`

The order of the tags can be used to specify the order shown in tools like Swagger UI, used in the automatic path `/docs`. It's not required to specify all the tags used. The tags that are not declared MAY be organized randomly or based on the tools' logic. Each tag name in the list MUST be unique. The value of each item is a `dict` containing:
  * `name`: The name of the tag.
  * `description`: A short description of the tag.
  * `externalDocs`: Additional external documentation for this tag. If provided, it would contain a `dict` with:
    * `description`: A short description of the target documentation.
    * `url`: The URL for the target documentation. Value MUST be in the form of a URL.

Read more in the [FastAPI docs for Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-tags). **Example** ```
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
**TYPE:** `list[dict[str, Any]] | None` **DEFAULT:** `None`
`servers` |  A `list` of `dict`s with connectivity information to a target server. You would use it, for example, if your application is served from different domains and you want to use the same Swagger UI in the browser to interact with each of them (instead of having multiple browser tabs open). Or if you want to leave fixed the possible URLs. If the servers `list` is not provided, or is an empty `list`, the `servers` property in the generated OpenAPI will be:
  * a `dict` with a `url` value of the application's mounting point (`root_path`) if it's different from `/`.
  * otherwise, the `servers` property will be omitted from the OpenAPI schema.

Each item in the `list` is a `dict` containing:
  * `url`: A URL to the target host. This URL supports Server Variables and MAY be relative, to indicate that the host location is relative to the location where the OpenAPI document is being served. Variable substitutions will be made when a variable is named in `{`brackets`}`.
  * `description`: An optional string describing the host designated by the URL.
  * `variables`: A `dict` between a variable name and its value. The value is used for substitution in the server's URL template.

Read more in the [FastAPI docs for Behind a Proxy](https://fastapi.tiangolo.com/advanced/behind-a-proxy/#additional-servers). **Example** ```
from fastapi import FastAPI

app = FastAPI(
    servers=[
        {"url": "https://stag.example.com", "description": "Staging environment"},
        {"url": "https://prod.example.com", "description": "Production environment"},
    ]
)

```
**TYPE:** `list[dict[str, str | Any]] | None` **DEFAULT:** `None`
`dependencies` |  A list of global dependencies, they will be applied to each _path operation_ , including in sub-routers. Read more about it in the [FastAPI docs for Global Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/global-dependencies/). **Example** ```
from fastapi import Depends, FastAPI

from .dependencies import func_dep_1, func_dep_2

app = FastAPI(dependencies=[Depends(func_dep_1), Depends(func_dep_2)])

```
**TYPE:** `Sequence[Depends] | None` **DEFAULT:** `None`
`default_response_class` |  The default response class to be used. Read more in the [FastAPI docs for Custom Response - HTML, Stream, File, others](https://fastapi.tiangolo.com/advanced/custom-response/#default-response-class). **Example** ```
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

app = FastAPI(default_response_class=ORJSONResponse)

```
**TYPE:** `type[Response[](https://fastapi.tiangolo.com/reference/response/#fastapi.Response "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.Response</span> \(<code>starlette.responses.Response</code>\)")]` **DEFAULT:** `Default(JSONResponse[](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.responses.JSONResponse</span> \(<code>starlette.responses.JSONResponse</code>\)"))`
`redirect_slashes` |  Whether to detect and redirect slashes in URLs when the client doesn't use the same format. **Example** ```
from fastapi import FastAPI

app = FastAPI(redirect_slashes=True)  # the default

@app.get("/items/")
async def read_items():
    return [{"item_id": "Foo"}]

```
With this app, if a client goes to `/items` (without a trailing slash), they will be automatically redirected with an HTTP status code of 307 to `/items/`. **TYPE:** `bool` **DEFAULT:** `True`
`docs_url` |  The path to the automatic interactive API documentation. It is handled in the browser by Swagger UI. The default URL is `/docs`. You can disable it by setting it to `None`. If `openapi_url` is set to `None`, this will be automatically disabled. Read more in the [FastAPI docs for Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/#docs-urls). **Example** ```
from fastapi import FastAPI

app = FastAPI(docs_url="/documentation", redoc_url=None)

```
**TYPE:** `str | None` **DEFAULT:** `'/docs'`
`redoc_url` |  The path to the alternative automatic interactive API documentation provided by ReDoc. The default URL is `/redoc`. You can disable it by setting it to `None`. If `openapi_url` is set to `None`, this will be automatically disabled. Read more in the [FastAPI docs for Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/#docs-urls). **Example** ```
from fastapi import FastAPI

app = FastAPI(docs_url="/documentation", redoc_url="redocumentation")

```
**TYPE:** `str | None` **DEFAULT:** `'/redoc'`
`swagger_ui_oauth2_redirect_url` |  The OAuth2 redirect endpoint for the Swagger UI. By default it is `/docs/oauth2-redirect`. This is only used if you use OAuth2 (with the "Authorize" button) with Swagger UI. **TYPE:** `str | None` **DEFAULT:** `'/docs/oauth2-redirect'`
`swagger_ui_init_oauth` |  OAuth2 configuration for the Swagger UI, by default shown at `/docs`. Read more about the available configuration options in the  **TYPE:** `dict[str, Any] | None` **DEFAULT:** `None`
`middleware` |  List of middleware to be added when creating the application. In FastAPI you would normally do this with `app.add_middleware()` instead. Read more in the [FastAPI docs for Middleware](https://fastapi.tiangolo.com/tutorial/middleware/). **TYPE:** `Sequence[Middleware] | None` **DEFAULT:** `None`
`exception_handlers` |  A dictionary with handlers for exceptions. In FastAPI, you would normally use the decorator `@app.exception_handler()`. Read more in the [FastAPI docs for Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/). **TYPE:** `dict[int | type[Exception], Callable[[Request[](https://fastapi.tiangolo.com/reference/request/#fastapi.Request "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.Request</span> \(<code>starlette.requests.Request</code>\)"), Any], Coroutine[Any, Any, Response[](https://fastapi.tiangolo.com/reference/response/#fastapi.Response "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.Response</span> \(<code>starlette.responses.Response</code>\)")]]] | None` **DEFAULT:** `None`
`on_startup` |  A list of startup event handler functions. You should instead use the `lifespan` handlers. Read more in the [FastAPI docs for `lifespan`](https://fastapi.tiangolo.com/advanced/events/). **TYPE:** `Sequence[Callable[[], Any]] | None` **DEFAULT:** `None`
`on_shutdown` |  A list of shutdown event handler functions. You should instead use the `lifespan` handlers. Read more in the [FastAPI docs for `lifespan`](https://fastapi.tiangolo.com/advanced/events/). **TYPE:** `Sequence[Callable[[], Any]] | None` **DEFAULT:** `None`
`lifespan` |  A `Lifespan` context manager handler. This replaces `startup` and `shutdown` functions with a single context manager. Read more in the [FastAPI docs for `lifespan`](https://fastapi.tiangolo.com/advanced/events/). **TYPE:** `Lifespan[AppType] | None` **DEFAULT:** `None`
`terms_of_service` |  A URL to the Terms of Service for your API. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more at the [FastAPI docs for Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-api). **Example** ```
app = FastAPI(terms_of_service="http://example.com/terms/")

```
**TYPE:** `str | None` **DEFAULT:** `None`
`contact` |  A dictionary with the contact information for the exposed API. It can contain several fields.
  * `name`: (`str`) The name of the contact person/organization.
  * `url`: (`str`) A URL pointing to the contact information. MUST be in the format of a URL.
  * `email`: (`str`) The email address of the contact person/organization. MUST be in the format of an email address.

It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more at the [FastAPI docs for Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-api). **Example** ```
app = FastAPI(
    contact={
        "name": "Deadpoolio the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    }
)

```
**TYPE:** `dict[str, str | Any] | None` **DEFAULT:** `None`
`license_info` |  A dictionary with the license information for the exposed API. It can contain several fields.
  * `name`: (`str`) **REQUIRED** (if a `license_info` is set). The license name used for the API.
  * `identifier`: (`str`) An `identifier` field is mutually exclusive of the `url` field. Available since OpenAPI 3.1.0, FastAPI 0.99.0.
  * `url`: (`str`) A URL to the license used for the API. This MUST be the format of a URL.

It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more at the [FastAPI docs for Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-api). **Example** ```
app = FastAPI(
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }
)

```
**TYPE:** `dict[str, str | Any] | None` **DEFAULT:** `None`
`openapi_prefix` |  A URL prefix for the OpenAPI URL. **TYPE:** `str` **DEFAULT:** `''`
`root_path` |  A path prefix handled by a proxy that is not seen by the application but is seen by external clients, which affects things like Swagger UI. Read more about it at the [FastAPI docs for Behind a Proxy](https://fastapi.tiangolo.com/advanced/behind-a-proxy/). **Example** ```
from fastapi import FastAPI

app = FastAPI(root_path="/api/v1")

```
**TYPE:** `str` **DEFAULT:** `''`
`root_path_in_servers` |  To disable automatically generating the URLs in the `servers` field in the autogenerated OpenAPI using the `root_path`. Read more about it in the [FastAPI docs for Behind a Proxy](https://fastapi.tiangolo.com/advanced/behind-a-proxy/#disable-automatic-server-from-root-path). **Example** ```
from fastapi import FastAPI

app = FastAPI(root_path_in_servers=False)

```
**TYPE:** `bool` **DEFAULT:** `True`
`responses` |  Additional responses to be shown in OpenAPI. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for Additional Responses in OpenAPI](https://fastapi.tiangolo.com/advanced/additional-responses/). And in the [FastAPI docs for Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-an-apirouter-with-a-custom-prefix-tags-responses-and-dependencies). **TYPE:** `dict[int | str, dict[str, Any]] | None` **DEFAULT:** `None`
`callbacks` |  OpenAPI callbacks that should apply to all _path operations_. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for OpenAPI Callbacks](https://fastapi.tiangolo.com/advanced/openapi-callbacks/). **TYPE:** `list[BaseRoute] | None` **DEFAULT:** `None`
`webhooks` |  Add OpenAPI webhooks. This is similar to `callbacks` but it doesn't depend on specific _path operations_. It will be added to the generated OpenAPI (e.g. visible at `/docs`). **Note** : This is available since OpenAPI 3.1.0, FastAPI 0.99.0. Read more about it in the [FastAPI docs for OpenAPI Webhooks](https://fastapi.tiangolo.com/advanced/openapi-webhooks/). **TYPE:** `APIRouter[](https://fastapi.tiangolo.com/reference/apirouter/#fastapi.APIRouter "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.APIRouter</span> \(<code>fastapi.routing.APIRouter</code>\)") | None` **DEFAULT:** `None`
`deprecated` |  Mark all _path operations_ as deprecated. You probably don't need it, but it's available. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/#deprecate-a-path-operation). **TYPE:** `bool | None` **DEFAULT:** `None`
`include_in_schema` |  To include (or not) all the _path operations_ in the generated OpenAPI. You probably don't need it, but it's available. This affects the generated OpenAPI (e.g. visible at `/docs`). Read more about it in the [FastAPI docs for Query Parameters and String Validations](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#exclude-parameters-from-openapi). **TYPE:** `bool` **DEFAULT:** `True`
`swagger_ui_parameters` |  Parameters to configure Swagger UI, the autogenerated interactive API documentation (by default at `/docs`). Read more about it in the [FastAPI docs about how to Configure Swagger UI](https://fastapi.tiangolo.com/how-to/configure-swagger-ui/). **TYPE:** `dict[str, Any] | None` **DEFAULT:** `None`
`generate_unique_id_function` |  Customize the function used to generate unique IDs for the _path operations_ shown in the generated OpenAPI. This is particularly useful when automatically generating clients or SDKs for your API. Read more about it in the [FastAPI docs about how to Generate Clients](https://fastapi.tiangolo.com/advanced/generate-clients/#custom-generate-unique-id-function). **TYPE:** `Callable[[APIRoute], str]` **DEFAULT:** `Default(generate_unique_id)`
`separate_input_output_schemas` |  Whether to generate separate OpenAPI schemas for request body and response body when the results would be more precise. This is particularly useful when automatically generating clients. For example, if you have a model like: ```
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    tags: list[str] = []

```
When `Item` is used for input, a request body, `tags` is not required, the client doesn't have to provide it. But when using `Item` for output, for a response body, `tags` is always available because it has a default value, even if it's just an empty list. So, the client should be able to always expect it. In this case, there would be two different schemas, one for input and another one for output. Read more about it in the [FastAPI docs about how to separate schemas for input and output](https://fastapi.tiangolo.com/how-to/separate-openapi-schemas) **TYPE:** `bool` **DEFAULT:** `True`
`openapi_external_docs` |  This field allows you to provide additional external documentation links. If provided, it must be a dictionary containing:
  * `description`: A brief description of the external documentation.
  * `url`: The URL pointing to the external documentation. The value **MUST** be a valid URL format.

**Example** : ```
from fastapi import FastAPI

external_docs = {
    "description": "Detailed API Reference",
    "url": "https://example.com/api-docs",
}

app = FastAPI(openapi_external_docs=external_docs)

```
**TYPE:** `dict[str, Any] | None` **DEFAULT:** `None`
`strict_content_type` |  Enable strict checking for request Content-Type headers. When `True` (the default), requests with a body that do not include a `Content-Type` header will **not** be parsed as JSON. This prevents potential cross-site request forgery (CSRF) attacks that exploit the browser's ability to send requests without a Content-Type header, bypassing CORS preflight checks. In particular applicable for apps that need to be run locally (in localhost). When `False`, requests without a `Content-Type` header will have their body parsed as JSON, which maintains compatibility with certain clients that don't send `Content-Type` headers. Read more about it in the [FastAPI docs for Strict Content-Type](https://fastapi.tiangolo.com/advanced/strict-content-type/). **TYPE:** `bool` **DEFAULT:** `True`
`**extra` |  Extra keyword arguments to be stored in the app, not used by FastAPI anywhere. **TYPE:** `Any` **DEFAULT:** `{}`
Source code in `fastapi/applications.py`
```
  61
  62
  63
  64
  65
  66
  67
  68
  69
  70
  71
  72
  73
  74
  75
  76
  77
  78
  79
  80
  81
  82
  83
  84
  85
  86
  87
  88
  89
  90
  91
  92
  93
  94
  95
  96
  97
  98
  99
 100
 101
 102
 103
 104
 105
 106
 107
 108
 109
 110
 111
 112
 113
 114
 115
 116
 117
 118
 119
 120
 121
 122
 123
 124
 125
 126
 127
 128
 129
 130
 131
 132
 133
 134
 135
 136
 137
 138
 139
 140
 141
 142
 143
 144
 145
 146
 147
 148
 149
 150
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
 236
 237
 238
 239
 240
 241
 242
 243
 244
 245
 246
 247
 248
 249
 250
 251
 252
 253
 254
 255
 256
 257
 258
 259
 260
 261
 262
 263
 264
 265
 266
 267
 268
 269
 270
 271
 272
 273
 274
 275
 276
 277
 278
 279
 280
 281
 282
 283
 284
 285
 286
 287
 288
 289
 290
 291
 292
 293
 294
 295
 296
 297
 298
 299
 300
 301
 302
 303
 304
 305
 306
 307
 308
 309
 310
 311
 312
 313
 314
 315
 316
 317
 318
 319
 320
 321
 322
 323
 324
 325
 326
 327
 328
 329
 330
 331
 332
 333
 334
 335
 336
 337
 338
 339
 340
 341
 342
 343
 344
 345
 346
 347
 348
 349
 350
 351
 352
 353
 354
 355
 356
 357
 358
 359
 360
 361
 362
 363
 364
 365
 366
 367
 368
 369
 370
 371
 372
 373
 374
 375
 376
 377
 378
 379
 380
 381
 382
 383
 384
 385
 386
 387
 388
 389
 390
 391
 392
 393
 394
 395
 396
 397
 398
 399
 400
 401
 402
 403
 404
 405
 406
 407
 408
 409
 410
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
 498
 499
 500
 501
 502
 503
 504
 505
 506
 507
 508
 509
 510
 511
 512
 513
 514
 515
 516
 517
 518
 519
 520
 521
 522
 523
 524
 525
 526
 527
 528
 529
 530
 531
 532
 533
 534
 535
 536
 537
 538
 539
 540
 541
 542
 543
 544
 545
 546
 547
 548
 549
 550
 551
 552
 553
 554
 555
 556
 557
 558
 559
 560
 561
 562
 563
 564
 565
 566
 567
 568
 569
 570
 571
 572
 573
 574
 575
 576
 577
 578
 579
 580
 581
 582
 583
 584
 585
 586
 587
 588
 589
 590
 591
 592
 593
 594
 595
 596
 597
 598
 599
 600
 601
 602
 603
 604
 605
 606
 607
 608
 609
 610
 611
 612
 613
 614
 615
 616
 617
 618
 619
 620
 621
 622
 623
 624
 625
 626
 627
 628
 629
 630
 631
 632
 633
 634
 635
 636
 637
 638
 639
 640
 641
 642
 643
 644
 645
 646
 647
 648
 649
 650
 651
 652
 653
 654
 655
 656
 657
 658
 659
 660
 661
 662
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
 684
 685
 686
 687
 688
 689
 690
 691
 692
 693
 694
 695
 696
 697
 698
 699
 700
 701
 702
 703
 704
 705
 706
 707
 708
 709
 710
 711
 712
 713
 714
 715
 716
 717
 718
 719
 720
 721
 722
 723
 724
 725
 726
 727
 728
 729
 730
 731
 732
 733
 734
 735
 736
 737
 738
 739
 740
