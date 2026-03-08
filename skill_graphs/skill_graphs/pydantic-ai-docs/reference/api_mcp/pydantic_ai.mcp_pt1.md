# `pydantic_ai.mcp`
###  MCPError
Bases:
Raised when an MCP server returns an error response.
This exception wraps error responses from MCP servers, following the ErrorData schema from the MCP specification.
Source code in `pydantic_ai_slim/pydantic_ai/mcp.py`
```
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
```
| ```
class MCPError(RuntimeError):
    """Raised when an MCP server returns an error response.

    This exception wraps error responses from MCP servers, following the ErrorData schema
    from the MCP specification.
    """

    message: str
    """The error message."""

    code: int
    """The error code returned by the server."""

    data: dict[str, Any] | None
    """Additional information about the error, if provided by the server."""

    def __init__(self, message: str, code: int, data: dict[str, Any] | None = None):
        self.message = message
        self.code = code
        self.data = data
        super().__init__(message)

    @classmethod
    def from_mcp_sdk(cls, error: mcp_exceptions.McpError) -> MCPError:
        """Create an MCPError from an MCP SDK McpError.

        Args:
            error: An McpError from the MCP SDK.
        """
        # Extract error data from the McpError.error attribute
        error_data = error.error
        return cls(message=error_data.message, code=error_data.code, data=error_data.data)

    def __str__(self) -> str:
        if self.data:
            return f'{self.message} (code: {self.code}, data: {self.data})'
        return f'{self.message} (code: {self.code})'

```

---|---
####  message `instance-attribute`
```
message:  = message

```

The error message.
####  code `instance-attribute`
```
code:  = code

```

The error code returned by the server.
####  data `instance-attribute`
```
data: [, ] | None = data

```

Additional information about the error, if provided by the server.
####  from_mcp_sdk `classmethod`
```
from_mcp_sdk(error: ) -> MCPError[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.MCPError "MCPError \(pydantic_ai.mcp.MCPError\)")

```

Create an MCPError from an MCP SDK McpError.
Parameters:
Name | Type | Description | Default
---|---|---|---
`error` |  |  An McpError from the MCP SDK. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/mcp.py`
```
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
```
| ```
@classmethod
def from_mcp_sdk(cls, error: mcp_exceptions.McpError) -> MCPError:
    """Create an MCPError from an MCP SDK McpError.

    Args:
        error: An McpError from the MCP SDK.
    """
    # Extract error data from the McpError.error attribute
    error_data = error.error
    return cls(message=error_data.message, code=error_data.code, data=error_data.data)

```

---|---
###  ResourceAnnotations `dataclass`
Additional properties describing MCP entities.
See the
Source code in `pydantic_ai_slim/pydantic_ai/mcp.py`
```
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
```
| ```
@dataclass(repr=False, kw_only=True)
class ResourceAnnotations:
    """Additional properties describing MCP entities.

    See the [resource annotations in the MCP specification](https://modelcontextprotocol.io/specification/2025-06-18/server/resources#annotations).
    """

    audience: list[mcp_types.Role] | None = None
    """Intended audience for this entity."""

    priority: Annotated[float, Field(ge=0.0, le=1.0)] | None = None
    """Priority level for this entity, ranging from 0.0 to 1.0."""

    __repr__ = _utils.dataclasses_no_defaults_repr

    @classmethod
    def from_mcp_sdk(cls, mcp_annotations: mcp_types.Annotations) -> ResourceAnnotations:
        """Convert from MCP SDK Annotations to ResourceAnnotations.

        Args:
            mcp_annotations: The MCP SDK annotations object.
        """
        return cls(audience=mcp_annotations.audience, priority=mcp_annotations.priority)

```

---|---
####  audience `class-attribute` `instance-attribute`
```
audience: [Role] | None = None

```

Intended audience for this entity.
####  priority `class-attribute` `instance-attribute`
```
priority: [, Field[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "pydantic.Field")(ge=0.0, le=1.0)] | None = (
    None
)

```

Priority level for this entity, ranging from 0.0 to 1.0.
####  from_mcp_sdk `classmethod`
```
from_mcp_sdk(
    mcp_annotations: Annotations,
) -> ResourceAnnotations[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.ResourceAnnotations "ResourceAnnotations



      dataclass
   \(pydantic_ai.mcp.ResourceAnnotations\)")

```

Convert from MCP SDK Annotations to ResourceAnnotations.
Parameters:
Name | Type | Description | Default
---|---|---|---
`mcp_annotations` |  `Annotations` |  The MCP SDK annotations object. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/mcp.py`
```
117
118
119
120
121
122
123
124
```
| ```
@classmethod
def from_mcp_sdk(cls, mcp_annotations: mcp_types.Annotations) -> ResourceAnnotations:
    """Convert from MCP SDK Annotations to ResourceAnnotations.

    Args:
        mcp_annotations: The MCP SDK annotations object.
    """
    return cls(audience=mcp_annotations.audience, priority=mcp_annotations.priority)

```

---|---
###  BaseResource `dataclass`
Bases:
Base class for MCP resources.
Source code in `pydantic_ai_slim/pydantic_ai/mcp.py`
```
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
```
| ```
@dataclass(repr=False, kw_only=True)
class BaseResource(ABC):
    """Base class for MCP resources."""

    name: str
    """The programmatic name of the resource."""

    title: str | None = None
    """Human-readable title for UI contexts."""

    description: str | None = None
    """A description of what this resource represents."""

    mime_type: str | None = None
    """The MIME type of the resource, if known."""

    annotations: ResourceAnnotations | None = None
    """Optional annotations for the resource."""

    metadata: dict[str, Any] | None = None
    """Optional metadata for the resource."""

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  name `instance-attribute`
```
name:

```

The programmatic name of the resource.
####  title `class-attribute` `instance-attribute`
```
title:  | None = None

```

Human-readable title for UI contexts.
####  description `class-attribute` `instance-attribute`
```
description:  | None = None

```

A description of what this resource represents.
####  mime_type `class-attribute` `instance-attribute`
```
mime_type:  | None = None

```

The MIME type of the resource, if known.
####  annotations `class-attribute` `instance-attribute`
```
annotations: ResourceAnnotations[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.ResourceAnnotations "ResourceAnnotations



      dataclass
   \(pydantic_ai.mcp.ResourceAnnotations\)") | None = None

```

Optional annotations for the resource.
####  metadata `class-attribute` `instance-attribute`
```
metadata: [, ] | None = None

```

Optional metadata for the resource.
###  Resource `dataclass`
Bases: `BaseResource[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.BaseResource "BaseResource



      dataclass
   \(pydantic_ai.mcp.BaseResource\)")`
A resource that can be read from an MCP server.
See the
Source code in `pydantic_ai_slim/pydantic_ai/mcp.py`
```
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
```
| ```
@dataclass(repr=False, kw_only=True)
class Resource(BaseResource):
    """A resource that can be read from an MCP server.

    See the [resources in the MCP specification](https://modelcontextprotocol.io/specification/2025-06-18/server/resources).
    """

    uri: str
    """The URI of the resource."""

    size: int | None = None
    """The size of the raw resource content in bytes (before base64 encoding), if known."""

    @classmethod
    def from_mcp_sdk(cls, mcp_resource: mcp_types.Resource) -> Resource:
        """Convert from MCP SDK Resource to PydanticAI Resource.

        Args:
            mcp_resource: The MCP SDK Resource object.
        """
        return cls(
            uri=str(mcp_resource.uri),
            name=mcp_resource.name,
            title=mcp_resource.title,
            description=mcp_resource.description,
            mime_type=mcp_resource.mimeType,
            size=mcp_resource.size,
            annotations=ResourceAnnotations.from_mcp_sdk(mcp_resource.annotations)
            if mcp_resource.annotations
            else None,
            metadata=mcp_resource.meta,
        )

```

---|---
####  uri `instance-attribute`
```
uri:

```

The URI of the resource.
####  size `class-attribute` `instance-attribute`
```
size:  | None = None

```

The size of the raw resource content in bytes (before base64 encoding), if known.
####  from_mcp_sdk `classmethod`
```
from_mcp_sdk(mcp_resource: ) -> Resource[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.Resource "Resource



      dataclass
   \(pydantic_ai.mcp.Resource\)")

```

Convert from MCP SDK Resource to PydanticAI Resource.
Parameters:
Name | Type | Description | Default
---|---|---|---
`mcp_resource` |  |  The MCP SDK Resource object. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/mcp.py`
```
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
```
| ```
@classmethod
def from_mcp_sdk(cls, mcp_resource: mcp_types.Resource) -> Resource:
    """Convert from MCP SDK Resource to PydanticAI Resource.

    Args:
        mcp_resource: The MCP SDK Resource object.
    """
    return cls(
        uri=str(mcp_resource.uri),
        name=mcp_resource.name,
        title=mcp_resource.title,
        description=mcp_resource.description,
        mime_type=mcp_resource.mimeType,
        size=mcp_resource.size,
        annotations=ResourceAnnotations.from_mcp_sdk(mcp_resource.annotations)
        if mcp_resource.annotations
        else None,
        metadata=mcp_resource.meta,
    )

```

---|---
###  ResourceTemplate `dataclass`
Bases: `BaseResource[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.BaseResource "BaseResource



      dataclass
   \(pydantic_ai.mcp.BaseResource\)")`
A template for parameterized resources on an MCP server.
See the
Source code in `pydantic_ai_slim/pydantic_ai/mcp.py`
```
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
```
| ```
@dataclass(repr=False, kw_only=True)
class ResourceTemplate(BaseResource):
    """A template for parameterized resources on an MCP server.

    See the [resource templates in the MCP specification](https://modelcontextprotocol.io/specification/2025-06-18/server/resources#resource-templates).
    """

    uri_template: str
    """URI template (RFC 6570) for constructing resource URIs."""

    @classmethod
    def from_mcp_sdk(cls, mcp_template: mcp_types.ResourceTemplate) -> ResourceTemplate:
        """Convert from MCP SDK ResourceTemplate to PydanticAI ResourceTemplate.

        Args:
            mcp_template: The MCP SDK ResourceTemplate object.
        """
        return cls(
            uri_template=mcp_template.uriTemplate,
            name=mcp_template.name,
            title=mcp_template.title,
            description=mcp_template.description,
            mime_type=mcp_template.mimeType,
            annotations=ResourceAnnotations.from_mcp_sdk(mcp_template.annotations)
            if mcp_template.annotations
            else None,
            metadata=mcp_template.meta,
        )

```

---|---
####  uri_template `instance-attribute`
```
uri_template:

```

URI template (RFC 6570) for constructing resource URIs.
####  from_mcp_sdk `classmethod`
```
from_mcp_sdk(
    mcp_template: ResourceTemplate,
) -> ResourceTemplate[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.ResourceTemplate "ResourceTemplate



      dataclass
   \(pydantic_ai.mcp.ResourceTemplate\)")

```

Convert from MCP SDK ResourceTemplate to PydanticAI ResourceTemplate.
Parameters:
Name | Type | Description | Default
---|---|---|---
`mcp_template` |  `ResourceTemplate` |  The MCP SDK ResourceTemplate object. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/mcp.py`
```
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
```
| ```
@classmethod
def from_mcp_sdk(cls, mcp_template: mcp_types.ResourceTemplate) -> ResourceTemplate:
    """Convert from MCP SDK ResourceTemplate to PydanticAI ResourceTemplate.

    Args:
        mcp_template: The MCP SDK ResourceTemplate object.
    """
    return cls(
        uri_template=mcp_template.uriTemplate,
        name=mcp_template.name,
        title=mcp_template.title,
        description=mcp_template.description,
        mime_type=mcp_template.mimeType,
        annotations=ResourceAnnotations.from_mcp_sdk(mcp_template.annotations)
        if mcp_template.annotations
        else None,
        metadata=mcp_template.meta,
    )

```

---|---
###  ServerCapabilities `dataclass`
Capabilities that an MCP server supports.
Source code in `pydantic_ai_slim/pydantic_ai/mcp.py`
```
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
```
| ```
@dataclass(repr=False, kw_only=True)
class ServerCapabilities:
    """Capabilities that an MCP server supports."""

    experimental: list[str] | None = None
    """Experimental, non-standard capabilities that the server supports."""

    logging: bool = False
    """Whether the server supports sending log messages to the client."""

    prompts: bool = False
    """Whether the server offers any prompt templates."""

    prompts_list_changed: bool = False
    """Whether the server will emit notifications when the list of prompts changes."""

    resources: bool = False
    """Whether the server offers any resources to read."""

    resources_list_changed: bool = False
    """Whether the server will emit notifications when the list of resources changes."""

    tools: bool = False
    """Whether the server offers any tools to call."""

    tools_list_changed: bool = False
    """Whether the server will emit notifications when the list of tools changes."""

    completions: bool = False
    """Whether the server offers autocompletion suggestions for prompts and resources."""

    __repr__ = _utils.dataclasses_no_defaults_repr

    @classmethod
    def from_mcp_sdk(cls, mcp_capabilities: mcp_types.ServerCapabilities) -> ServerCapabilities:
        """Convert from MCP SDK ServerCapabilities to PydanticAI ServerCapabilities.

        Args:
            mcp_capabilities: The MCP SDK ServerCapabilities object.
        """
        prompts_cap = mcp_capabilities.prompts
        resources_cap = mcp_capabilities.resources
        tools_cap = mcp_capabilities.tools
        return cls(
            experimental=list(mcp_capabilities.experimental.keys()) if mcp_capabilities.experimental else None,
            logging=mcp_capabilities.logging is not None,
            prompts=prompts_cap is not None,
            prompts_list_changed=bool(prompts_cap.listChanged) if prompts_cap else False,
            resources=resources_cap is not None,
            resources_list_changed=bool(resources_cap.listChanged) if resources_cap else False,
            tools=tools_cap is not None,
            tools_list_changed=bool(tools_cap.listChanged) if tools_cap else False,
            completions=mcp_capabilities.completions is not None,
        )

```

---|---
####  experimental `class-attribute` `instance-attribute`
```
experimental: [] | None = None

```

Experimental, non-standard capabilities that the server supports.
####  logging `class-attribute` `instance-attribute`
```
logging:  = False

```

Whether the server supports sending log messages to the client.
####  prompts `class-attribute` `instance-attribute`
```
prompts:  = False

```

Whether the server offers any prompt templates.
####  prompts_list_changed `class-attribute` `instance-attribute`
```
prompts_list_changed:  = False

```

Whether the server will emit notifications when the list of prompts changes.
####  resources `class-attribute` `instance-attribute`
```
resources:  = False

```

Whether the server offers any resources to read.
####  resources_list_changed `class-attribute` `instance-attribute`
```
resources_list_changed:  = False

```

Whether the server will emit notifications when the list of resources changes.
####  tools `class-attribute` `instance-attribute`
```
tools:  = False

```

Whether the server offers any tools to call.
####  tools_list_changed `class-attribute` `instance-attribute`
```
tools_list_changed:  = False

```

Whether the server will emit notifications when the list of tools changes.
####  completions `class-attribute` `instance-attribute`
```
completions:  = False

```

Whether the server offers autocompletion suggestions for prompts and resources.
####  from_mcp_sdk `classmethod`
```
from_mcp_sdk(
    mcp_capabilities: ,
) -> ServerCapabilities[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.ServerCapabilities "ServerCapabilities



      dataclass
   \(pydantic_ai.mcp.ServerCapabilities\)")

```

Convert from MCP SDK ServerCapabilities to PydanticAI ServerCapabilities.
Parameters:
Name | Type | Description | Default
---|---|---|---
`mcp_capabilities` |  |  The MCP SDK ServerCapabilities object. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/mcp.py`
```
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
```
| ```
@classmethod
def from_mcp_sdk(cls, mcp_capabilities: mcp_types.ServerCapabilities) -> ServerCapabilities:
    """Convert from MCP SDK ServerCapabilities to PydanticAI ServerCapabilities.

    Args:
        mcp_capabilities: The MCP SDK ServerCapabilities object.
    """
    prompts_cap = mcp_capabilities.prompts
    resources_cap = mcp_capabilities.resources
    tools_cap = mcp_capabilities.tools
    return cls(
        experimental=list(mcp_capabilities.experimental.keys()) if mcp_capabilities.experimental else None,
        logging=mcp_capabilities.logging is not None,
        prompts=prompts_cap is not None,
        prompts_list_changed=bool(prompts_cap.listChanged) if prompts_cap else False,
        resources=resources_cap is not None,
        resources_list_changed=bool(resources_cap.listChanged) if resources_cap else False,
        tools=tools_cap is not None,
        tools_list_changed=bool(tools_cap.listChanged) if tools_cap else False,
        completions=mcp_capabilities.completions is not None,
    )

```

---|---
###  MCPServer
Bases: `AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.abstract.AbstractToolset\)")[`,
Base class for attaching agents to MCP servers.
See
Source code in `pydantic_ai_slim/pydantic_ai/mcp.py`
```
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
```
| ```
class MCPServer(AbstractToolset[Any], ABC):
    """Base class for attaching agents to MCP servers.

    See <https://modelcontextprotocol.io> for more information.
    """

    tool_prefix: str | None
    """A prefix to add to all tools that are registered with the server.

    If not empty, will include a trailing underscore(`_`).

    e.g. if `tool_prefix='foo'`, then a tool named `bar` will be registered as `foo_bar`
    """

    log_level: mcp_types.LoggingLevel | None
    """The log level to set when connecting to the server, if any.

    See <https://modelcontextprotocol.io/specification/2025-03-26/server/utilities/logging#logging> for more details.

    If `None`, no log level will be set.
    """

    log_handler: LoggingFnT | None
    """A handler for logging messages from the server."""

    timeout: float
    """The timeout in seconds to wait for the client to initialize."""

    read_timeout: float
    """Maximum time in seconds to wait for new messages before timing out.

    This timeout applies to the long-lived connection after it's established.
    If no new messages are received within this time, the connection will be considered stale
    and may be closed. Defaults to 5 minutes (300 seconds).
    """

    process_tool_call: ProcessToolCallback | None
    """Hook to customize tool calling and optionally pass extra metadata."""

    allow_sampling: bool
    """Whether to allow MCP sampling through this client."""

    sampling_model: models.Model | None
    """The model to use for sampling."""

    max_retries: int
    """The maximum number of times to retry a tool call."""

    elicitation_callback: ElicitationFnT | None = None
    """Callback function to handle elicitation requests from the server."""

    cache_tools: bool
    """Whether to cache the list of tools.

    When enabled (default), tools are fetched once and cached until either:
    - The server sends a `notifications/tools/list_changed` notification
    - [`MCPServer.__aexit__`][pydantic_ai.mcp.MCPServer.__aexit__] is called (when the last context exits)

    Set to `False` for servers that change tools dynamically without sending notifications.

    Note: When using durable execution (Temporal, DBOS), tool definitions are additionally cached
    at the wrapper level across activities/steps, to avoid redundant MCP connections. This
    wrapper-level cache is not invalidated by `tools/list_changed` notifications.
    Set to `False` to disable all caching if tools may change during a workflow.
    """

    cache_resources: bool
    """Whether to cache the list of resources.

    When enabled (default), resources are fetched once and cached until either:
    - The server sends a `notifications/resources/list_changed` notification
    - [`MCPServer.__aexit__`][pydantic_ai.mcp.MCPServer.__aexit__] is called (when the last context exits)

    Set to `False` for servers that change resources dynamically without sending notifications.
    """

    _id: str | None

    _enter_lock: Lock = field(compare=False)
    _running_count: int
    _exit_stack: AsyncExitStack | None

    _client: ClientSession
    _read_stream: MemoryObjectReceiveStream[SessionMessage | Exception]
    _write_stream: MemoryObjectSendStream[SessionMessage]
    _server_info: mcp_types.Implementation
    _server_capabilities: ServerCapabilities
    _instructions: str | None

    _cached_tools: list[mcp_types.Tool] | None
    _cached_resources: list[Resource] | None

    # TODO (v2): enforce the arguments to be passed as keyword arguments only
    def __init__(
        self,
        tool_prefix: str | None = None,
        log_level: mcp_types.LoggingLevel | None = None,
        log_handler: LoggingFnT | None = None,
        timeout: float = 5,
        read_timeout: float = 5 * 60,
        process_tool_call: ProcessToolCallback | None = None,
        allow_sampling: bool = True,
        sampling_model: models.Model | None = None,
        max_retries: int = 1,
        elicitation_callback: ElicitationFnT | None = None,
        cache_tools: bool = True,
        cache_resources: bool = True,
        *,
        id: str | None = None,
        client_info: mcp_types.Implementation | None = None,
    ):
        self.tool_prefix = tool_prefix
        self.log_level = log_level
        self.log_handler = log_handler
        self.timeout = timeout
