# `pydantic_ai.ui.vercel_ai`
Vercel AI protocol adapter for Pydantic AI agents.
This module provides classes for integrating Pydantic AI agents with the Vercel AI protocol, enabling streaming event-based communication for interactive AI applications.
Converted to Python from: https://github.com/vercel/ai/blob/ai%405.0.34/packages/ai/src/ui/ui-messages.ts
###  VercelAIAdapter `dataclass`
Bases: `UIAdapter[](https://ai.pydantic.dev/api/ui/base/#pydantic_ai.ui.UIAdapter "UIAdapter



      dataclass
   \(pydantic_ai.ui.UIAdapter\)")[RequestData[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.RequestData "RequestData



      module-attribute
   \(pydantic_ai.ui.vercel_ai.request_types.RequestData\)"), UIMessage[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.request_types.UIMessage "UIMessage \(pydantic_ai.ui.vercel_ai.request_types.UIMessage\)"), BaseChunk[](https://ai.pydantic.dev/api/ui/vercel_ai/#pydantic_ai.ui.vercel_ai.response_types.BaseChunk "BaseChunk \(pydantic_ai.ui.vercel_ai.response_types.BaseChunk\)"), AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]`
UI adapter for the Vercel AI protocol.
Source code in `pydantic_ai_slim/pydantic_ai/ui/vercel_ai/_adapter.py`
```
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
741
742
743
744
745
746
```
| ```
@dataclass
class VercelAIAdapter(UIAdapter[RequestData, UIMessage, BaseChunk, AgentDepsT, OutputDataT]):
    """UI adapter for the Vercel AI protocol."""

    _: KW_ONLY
    sdk_version: Literal[5, 6] = 5
    """Vercel AI SDK version to target. Default is 5 for backwards compatibility.

    Setting `sdk_version=6` enables tool approval streaming for human-in-the-loop workflows.
    """

    @classmethod
    def build_run_input(cls, body: bytes) -> RequestData:
        """Build a Vercel AI run input object from the request body."""
        return request_data_ta.validate_json(body)

    @classmethod
    async def from_request(
        cls,
        request: Request,
        *,
        agent: AbstractAgent[AgentDepsT, OutputDataT],
        sdk_version: Literal[5, 6] = 5,
        **kwargs: Any,
    ) -> VercelAIAdapter[AgentDepsT, OutputDataT]:
        """Extends [`from_request`][pydantic_ai.ui.UIAdapter.from_request] with the `sdk_version` parameter."""
        return await super().from_request(request, agent=agent, sdk_version=sdk_version, **kwargs)

    @classmethod
    async def dispatch_request(
        cls,
        request: Request,
        *,
        agent: AbstractAgent[DispatchDepsT, DispatchOutputDataT],
        sdk_version: Literal[5, 6] = 5,
        message_history: Sequence[ModelMessage] | None = None,
        deferred_tool_results: DeferredToolResults | None = None,
        model: Model | KnownModelName | str | None = None,
        instructions: Instructions[DispatchDepsT] = None,
        deps: DispatchDepsT = None,
        output_type: OutputSpec[Any] | None = None,
        model_settings: ModelSettings | None = None,
        usage_limits: UsageLimits | None = None,
        usage: RunUsage | None = None,
        metadata: AgentMetadata[DispatchDepsT] | None = None,
        infer_name: bool = True,
        toolsets: Sequence[AbstractToolset[DispatchDepsT]] | None = None,
        builtin_tools: Sequence[AbstractBuiltinTool] | None = None,
        on_complete: OnCompleteFunc[BaseChunk] | None = None,
        **kwargs: Any,
    ) -> Response:
        """Extends [`dispatch_request`][pydantic_ai.ui.UIAdapter.dispatch_request] with the `sdk_version` parameter."""
        return await super().dispatch_request(
            request,
            agent=agent,
            sdk_version=sdk_version,
            message_history=message_history,
            deferred_tool_results=deferred_tool_results,
            model=model,
            instructions=instructions,
            deps=deps,
            output_type=output_type,
            model_settings=model_settings,
            usage_limits=usage_limits,
            usage=usage,
            metadata=metadata,
            infer_name=infer_name,
            toolsets=toolsets,
            builtin_tools=builtin_tools,
            on_complete=on_complete,
            **kwargs,
        )

    def build_event_stream(self) -> UIEventStream[RequestData, BaseChunk, AgentDepsT, OutputDataT]:
        """Build a Vercel AI event stream transformer."""
        return VercelAIEventStream(self.run_input, accept=self.accept, sdk_version=self.sdk_version)

    @cached_property
    def deferred_tool_results(self) -> DeferredToolResults | None:
        """Extract deferred tool results from Vercel AI messages with approval responses."""
        if self.sdk_version < 6:
            return None
        approvals: dict[str, bool | DeferredToolApprovalResult] = {}
        for tool_call_id, approval in iter_tool_approval_responses(self.run_input.messages):
            if approval.approved:
                approvals[tool_call_id] = True
            elif approval.reason:
                approvals[tool_call_id] = ToolDenied(message=approval.reason)
            else:
                approvals[tool_call_id] = False
        return DeferredToolResults(approvals=approvals) if approvals else None

    @cached_property
    def messages(self) -> list[ModelMessage]:
        """Pydantic AI messages from the Vercel AI run input."""
        return self.load_messages(self.run_input.messages)

    @classmethod
    def load_messages(cls, messages: Sequence[UIMessage]) -> list[ModelMessage]:  # noqa: C901
        """Transform Vercel AI messages into Pydantic AI messages."""
        builder = MessagesBuilder()

        for msg in messages:
            if msg.role == 'system':
                for part in msg.parts:
                    if isinstance(part, TextUIPart):
                        builder.add(SystemPromptPart(content=part.text))
                    else:  # pragma: no cover
                        raise ValueError(f'Unsupported system message part type: {type(part)}')
            elif msg.role == 'user':
                user_prompt_content: str | list[UserContent] = []
                for part in msg.parts:
                    if isinstance(part, TextUIPart):
                        user_prompt_content.append(part.text)
                    elif isinstance(part, FileUIPart):
                        try:
                            file = BinaryContent.from_data_uri(part.url)
                        except ValueError:
                            # Check provider_metadata for UploadedFile data
                            provider_meta = load_provider_metadata(part.provider_metadata)
                            uploaded_file_id = provider_meta.get('file_id')
                            uploaded_file_provider = provider_meta.get('provider_name')
                            if uploaded_file_id and uploaded_file_provider:
                                file = UploadedFile(
                                    file_id=uploaded_file_id,
                                    provider_name=cast(UploadedFileProviderName, uploaded_file_provider),
                                    media_type=part.media_type,
                                    vendor_metadata=provider_meta.get('vendor_metadata'),
                                    identifier=provider_meta.get('identifier'),
                                )
                            else:
                                media_type_prefix = part.media_type.split('/', 1)[0]
                                match media_type_prefix:
                                    case 'image':
                                        file = ImageUrl(url=part.url, media_type=part.media_type)
                                    case 'video':
                                        file = VideoUrl(url=part.url, media_type=part.media_type)
                                    case 'audio':
                                        file = AudioUrl(url=part.url, media_type=part.media_type)
                                    case _:
                                        file = DocumentUrl(url=part.url, media_type=part.media_type)
                        user_prompt_content.append(file)
                    else:  # pragma: no cover
                        raise ValueError(f'Unsupported user message part type: {type(part)}')

                if user_prompt_content:  # pragma: no branch
                    if len(user_prompt_content) == 1 and isinstance(user_prompt_content[0], str):
                        user_prompt_content = user_prompt_content[0]
                    builder.add(UserPromptPart(content=user_prompt_content))

            elif msg.role == 'assistant':
                for part in msg.parts:
                    if isinstance(part, TextUIPart):
                        provider_meta = load_provider_metadata(part.provider_metadata)
                        builder.add(
                            TextPart(
                                content=part.text,
                                id=provider_meta.get('id'),
                                provider_name=provider_meta.get('provider_name'),
                                provider_details=provider_meta.get('provider_details'),
                            )
                        )
                    elif isinstance(part, ReasoningUIPart):
                        provider_meta = load_provider_metadata(part.provider_metadata)
                        builder.add(
                            ThinkingPart(
                                content=part.text,
                                id=provider_meta.get('id'),
                                signature=provider_meta.get('signature'),
                                provider_name=provider_meta.get('provider_name'),
                                provider_details=provider_meta.get('provider_details'),
                            )
                        )
                    elif isinstance(part, FileUIPart):
                        try:
                            file = BinaryContent.from_data_uri(part.url)
                        except ValueError as e:  # pragma: no cover
                            # We don't yet handle non-data-URI file URLs returned by assistants, as no Pydantic AI models do this.
                            raise ValueError(
                                'Vercel AI integration can currently only handle assistant file parts with data URIs.'
                            ) from e
                        provider_meta = load_provider_metadata(part.provider_metadata)
                        builder.add(
                            FilePart(
                                content=file,
                                id=provider_meta.get('id'),
                                provider_name=provider_meta.get('provider_name'),
                                provider_details=provider_meta.get('provider_details'),
                            )
                        )
                    elif isinstance(part, ToolUIPart | DynamicToolUIPart):
                        if isinstance(part, DynamicToolUIPart):
                            tool_name = part.tool_name
                            builtin_tool = False
                        else:
                            tool_name = part.type.removeprefix('tool-')
                            builtin_tool = part.provider_executed

                        tool_call_id = part.tool_call_id

                        args: str | dict[str, Any] | None = part.input

                        if isinstance(args, str):
                            try:
                                parsed = json.loads(args)
                                if isinstance(parsed, dict):
                                    args = cast(dict[str, Any], parsed)
                            except json.JSONDecodeError:
                                pass
                        elif isinstance(args, dict) or args is None:
                            pass
                        else:
                            assert_never(args)

                        provider_meta = load_provider_metadata(part.call_provider_metadata)
                        part_id = provider_meta.get('id')
                        provider_name = provider_meta.get('provider_name')
                        provider_details = provider_meta.get('provider_details')

                        if builtin_tool:
                            # For builtin tools, we need to create 2 parts (BuiltinToolCall & BuiltinToolReturn) for a single Vercel ToolOutput
                            # The call and return metadata are combined in the output part.
                            # So we extract and return them to the respective parts
                            call_meta = return_meta = {}
                            has_tool_output = isinstance(
                                part, (ToolOutputAvailablePart, ToolOutputErrorPart, ToolOutputDeniedPart)
                            )

                            if has_tool_output:
                                call_meta, return_meta = cls._load_builtin_tool_meta(provider_meta)

                            builder.add(
                                BuiltinToolCallPart(
                                    tool_name=tool_name,
                                    tool_call_id=tool_call_id,
                                    args=args,
                                    id=call_meta.get('id') or part_id,
                                    provider_name=call_meta.get('provider_name') or provider_name,
                                    provider_details=call_meta.get('provider_details') or provider_details,
                                )
                            )

                            if has_tool_output:
                                if isinstance(part, ToolOutputErrorPart):
                                    output: Any = part.error_text
                                    outcome: Literal['success', 'failed', 'denied'] = 'failed'
                                elif isinstance(part, ToolOutputDeniedPart):
                                    output = _denial_reason(part)
                                    outcome = 'denied'
                                else:
                                    output = part.output if isinstance(part, ToolOutputAvailablePart) else None
                                    outcome = 'success'
                                builder.add(
                                    BuiltinToolReturnPart(
                                        tool_name=tool_name,
                                        tool_call_id=tool_call_id,
                                        content=output,
                                        provider_name=return_meta.get('provider_name') or provider_name,
                                        provider_details=return_meta.get('provider_details') or provider_details,
                                        outcome=outcome,
                                    )
                                )
                        else:
                            builder.add(
                                ToolCallPart(
                                    tool_name=tool_name,
                                    tool_call_id=tool_call_id,
                                    args=args,
                                    id=part_id,
                                    provider_name=provider_name,
                                    provider_details=provider_details,
                                )
                            )

                            if part.state == 'output-available':
                                builder.add(
                                    ToolReturnPart(tool_name=tool_name, tool_call_id=tool_call_id, content=part.output)
                                )
                            elif part.state == 'output-error':
                                builder.add(
                                    ToolReturnPart(
                                        tool_name=tool_name,
                                        tool_call_id=tool_call_id,
                                        content=part.error_text,
                                        outcome='failed',
                                    )
                                )
                            elif part.state == 'output-denied':
                                builder.add(
                                    ToolReturnPart(
                                        tool_name=tool_name,
                                        tool_call_id=tool_call_id,
                                        content=_denial_reason(part),
                                        outcome='denied',
                                    )
                                )
                    elif isinstance(part, DataUIPart):  # pragma: no cover
                        # Contains custom data that shouldn't be sent to the model
                        pass
                    elif isinstance(part, SourceUrlUIPart):  # pragma: no cover
                        # TODO: Once we support citations: https://github.com/pydantic/pydantic-ai/issues/3126
                        pass
                    elif isinstance(part, SourceDocumentUIPart):  # pragma: no cover
                        # TODO: Once we support citations: https://github.com/pydantic/pydantic-ai/issues/3126
                        pass
                    elif isinstance(part, StepStartUIPart):  # pragma: no cover
                        # Nothing to do here
                        pass
                    else:
                        assert_never(part)
            else:
                assert_never(msg.role)

        return builder.messages

    @staticmethod
    def _dump_builtin_tool_meta(
        call_provider_metadata: ProviderMetadata | None, return_provider_metadata: ProviderMetadata | None
    ) -> ProviderMetadata | None:
        """Use special keys (call_meta and return_meta) to dump combined provider metadata."""
        return dump_provider_metadata(call_meta=call_provider_metadata, return_meta=return_provider_metadata)

    @staticmethod
    def _load_builtin_tool_meta(
        provider_metadata: ProviderMetadata,
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        """Use special keys (call_meta and return_meta) to load combined provider metadata."""
        return provider_metadata.get('call_meta') or {}, provider_metadata.get('return_meta') or {}

    @staticmethod
    def _dump_request_message(msg: ModelRequest) -> tuple[list[UIMessagePart], list[UIMessagePart]]:
        """Convert a ModelRequest into a UIMessage."""
        system_ui_parts: list[UIMessagePart] = []
        user_ui_parts: list[UIMessagePart] = []

        for part in msg.parts:
            if isinstance(part, SystemPromptPart):
                system_ui_parts.append(TextUIPart(text=part.content, state='done'))
            elif isinstance(part, UserPromptPart):
                user_ui_parts.extend(_convert_user_prompt_part(part))
            elif isinstance(part, ToolReturnPart):
                # Tool returns are merged into the tool call in the assistant message
                pass
            elif isinstance(part, RetryPromptPart):
                if part.tool_name:
                    # Tool-related retries are handled when processing ToolCallPart in ModelResponse
                    pass
                else:
                    # Non-tool retries (e.g., output validation errors) become user text
                    user_ui_parts.append(TextUIPart(text=part.model_response(), state='done'))
            else:
                assert_never(part)

        return system_ui_parts, user_ui_parts

    @classmethod
    def _dump_response_message(
        cls, msg: ModelResponse, tool_results: dict[str, ToolReturnPart | RetryPromptPart]
    ) -> list[UIMessagePart]:
        """Convert a ModelResponse into a UIMessage."""
        ui_parts: list[UIMessagePart] = []

        # For builtin tools, returns can be in the same ModelResponse as calls
        local_builtin_returns: dict[str, BuiltinToolReturnPart] = {
            part.tool_call_id: part for part in msg.parts if isinstance(part, BuiltinToolReturnPart)
        }

        for part in msg.parts:
            if isinstance(part, BuiltinToolReturnPart):
                continue
            elif isinstance(part, TextPart):
                # Combine consecutive text parts
                if ui_parts and isinstance(ui_parts[-1], TextUIPart):
                    ui_parts[-1].text += part.content
                else:
                    provider_metadata = dump_provider_metadata(
                        id=part.id, provider_name=part.provider_name, provider_details=part.provider_details
                    )
                    ui_parts.append(TextUIPart(text=part.content, state='done', provider_metadata=provider_metadata))
            elif isinstance(part, ThinkingPart):
                provider_metadata = dump_provider_metadata(
                    id=part.id,
                    signature=part.signature,
                    provider_name=part.provider_name,
                    provider_details=part.provider_details,
                )
                ui_parts.append(ReasoningUIPart(text=part.content, state='done', provider_metadata=provider_metadata))
            elif isinstance(part, FilePart):
                ui_parts.append(
                    FileUIPart(
                        url=part.content.data_uri,
                        media_type=part.content.media_type,
                        provider_metadata=dump_provider_metadata(
                            id=part.id, provider_name=part.provider_name, provider_details=part.provider_details
                        ),
                    )
                )
            elif isinstance(part, BuiltinToolCallPart):
                tool_name = f'tool-{part.tool_name}'
                if builtin_return := local_builtin_returns.get(part.tool_call_id):
                    # Builtin tool calls are represented by two parts in pydantic_ai:
                    #   1. BuiltinToolCallPart (the tool request) -> part
                    #   2. BuiltinToolReturnPart (the tool's output) -> builtin_return
                    # The Vercel AI SDK only has a single ToolOutputPart (ToolOutputAvailablePart or ToolOutputErrorPart).
                    # So, we need to combine the metadata so that when we later convert back from Vercel AI to pydantic_ai,
                    # we can properly reconstruct both the call and return parts with their respective metadata.
                    # Note: This extra metadata handling is only needed for built-in tools, since normal tool returns
                    # (ToolReturnPart) do not include provider metadata.

                    call_meta = dump_provider_metadata(
                        wrapper_key=None,
                        id=part.id,
