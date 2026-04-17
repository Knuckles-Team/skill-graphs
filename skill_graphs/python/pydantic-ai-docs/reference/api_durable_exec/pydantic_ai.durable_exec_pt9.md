        activities = list(config.get('activities', []))  # type: ignore[reportUnknownMemberType]

        for workflow_class in workflows:  # type: ignore[reportUnknownMemberType]
            agents = getattr(workflow_class, '__pydantic_ai_agents__', None)  # type: ignore[reportUnknownMemberType]
            if agents is None:
                continue
            if not isinstance(agents, Sequence):
                raise TypeError(  # pragma: no cover
                    f'__pydantic_ai_agents__ must be a Sequence of TemporalAgent instances, got {type(agents)}'
                )
            for agent in agents:  # type: ignore[reportUnknownVariableType]
                if not isinstance(agent, TemporalAgent):
                    raise TypeError(  # pragma: no cover
                        f'__pydantic_ai_agents__ must be a Sequence of TemporalAgent, got {type(agent)}'  # type: ignore[reportUnknownVariableType]
                    )
                activities.extend(agent.temporal_activities)  # type: ignore[reportUnknownMemberType]

        config['activities'] = activities

        return config

```

---|---
###  AgentPlugin
Bases: `SimplePlugin`
Temporal worker plugin for a specific Pydantic AI agent.
Source code in `pydantic_ai_slim/pydantic_ai/durable_exec/temporal/__init__.py`
```
131
132
133
134
135
136
137
138
```
| ```
class AgentPlugin(SimplePlugin):
    """Temporal worker plugin for a specific Pydantic AI agent."""

    def __init__(self, agent: TemporalAgent[Any, Any]):
        super().__init__(  # type: ignore[reportUnknownMemberType]
            name='AgentPlugin',
            activities=agent.temporal_activities,
        )

```

---|---
###  DBOSAgent
Bases: `WrapperAgent[](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.WrapperAgent "WrapperAgent \(pydantic_ai.agent.WrapperAgent\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai.tools.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]`, `DBOSConfiguredInstance`
Source code in `pydantic_ai_slim/pydantic_ai/durable_exec/dbos/_agent.py`
```
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
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
```
| ```
@DBOS.dbos_class()
class DBOSAgent(WrapperAgent[AgentDepsT, OutputDataT], DBOSConfiguredInstance):
    _parallel_execution_mode: ParallelExecutionMode

    def __init__(
        self,
        wrapped: AbstractAgent[AgentDepsT, OutputDataT],
        *,
        name: str | None = None,
        event_stream_handler: EventStreamHandler[AgentDepsT] | None = None,
        mcp_step_config: StepConfig | None = None,
        model_step_config: StepConfig | None = None,
        parallel_execution_mode: DBOSParallelExecutionMode = 'parallel_ordered_events',
    ):
        """Wrap an agent to enable it with DBOS durable workflows, by automatically offloading model requests, tool calls, and MCP server communication to DBOS steps.

        After wrapping, the original agent can still be used as normal outside of the DBOS workflow.

        Args:
            wrapped: The agent to wrap.
            name: Optional unique agent name to use as the DBOS configured instance name. If not provided, the agent's `name` will be used.
            event_stream_handler: Optional event stream handler to use instead of the one set on the wrapped agent.
            mcp_step_config: The base DBOS step config to use for MCP server steps. If no config is provided, use the default settings of DBOS.
            model_step_config: The DBOS step config to use for model request steps. If no config is provided, use the default settings of DBOS.
            parallel_execution_mode: The mode for executing tool calls:
                - 'parallel_ordered_events' (default): Run tool calls in parallel, but events are emitted in order, after all calls complete.
                - 'sequential': Run tool calls one at a time in order.
        """
        super().__init__(wrapped)

        self._name = name or wrapped.name
        self._event_stream_handler = event_stream_handler
        self._parallel_execution_mode = cast(ParallelExecutionMode, parallel_execution_mode)
        if self._name is None:
            raise UserError(
                "An agent needs to have a unique `name` in order to be used with DBOS. The name will be used to identify the agent's workflows and steps."
            )

        # Merge the config with the default DBOS config
        self._mcp_step_config = mcp_step_config or {}
        self._model_step_config = model_step_config or {}

        if not isinstance(wrapped.model, Model):
            raise UserError(
                'An agent needs to have a `model` in order to be used with DBOS, it cannot be set at agent run time.'
            )

        dbos_model = DBOSModel(
            wrapped.model,
            step_name_prefix=self._name,
            step_config=self._model_step_config,
            event_stream_handler=self.event_stream_handler,
        )
        self._model = dbos_model

        dbosagent_name = self._name

        def dbosify_toolset(toolset: AbstractToolset[AgentDepsT]) -> AbstractToolset[AgentDepsT]:
            # Replace MCPServer with DBOSMCPServer
            try:
                from pydantic_ai.mcp import MCPServer

                from ._mcp_server import DBOSMCPServer
            except ImportError:
                pass
            else:
                if isinstance(toolset, MCPServer):
                    return DBOSMCPServer(
                        wrapped=toolset,
                        step_name_prefix=dbosagent_name,
                        step_config=self._mcp_step_config,
                    )

            # Replace FastMCPToolset with DBOSFastMCPToolset
            try:
                from pydantic_ai.toolsets.fastmcp import FastMCPToolset

                from ._fastmcp_toolset import DBOSFastMCPToolset
            except ImportError:
                pass
            else:
                if isinstance(toolset, FastMCPToolset):
                    return DBOSFastMCPToolset(
                        wrapped=toolset,
                        step_name_prefix=dbosagent_name,
                        step_config=self._mcp_step_config,
                    )

            return toolset

        dbos_toolsets = [toolset.visit_and_replace(dbosify_toolset) for toolset in wrapped.toolsets]
        self._toolsets = dbos_toolsets
        DBOSConfiguredInstance.__init__(self, self._name)

        # Wrap the `run` method in a DBOS workflow
        @DBOS.workflow(name=f'{self._name}.run')
        async def wrapped_run_workflow(
            user_prompt: str | Sequence[_messages.UserContent] | None = None,
            *,
            output_type: OutputSpec[RunOutputDataT] | None = None,
            message_history: Sequence[_messages.ModelMessage] | None = None,
            deferred_tool_results: DeferredToolResults | None = None,
            model: models.Model | models.KnownModelName | str | None = None,
            instructions: Instructions[AgentDepsT] = None,
            deps: AgentDepsT,
            model_settings: ModelSettings | None = None,
            usage_limits: _usage.UsageLimits | None = None,
            usage: _usage.RunUsage | None = None,
            metadata: AgentMetadata[AgentDepsT] | None = None,
            infer_name: bool = True,
            toolsets: Sequence[AbstractToolset[AgentDepsT]] | None = None,
            builtin_tools: Sequence[AbstractBuiltinTool | BuiltinToolFunc[AgentDepsT]] | None = None,
            event_stream_handler: EventStreamHandler[AgentDepsT] | None = None,
            **_deprecated_kwargs: Never,
        ) -> AgentRunResult[Any]:
            with self._dbos_overrides():
                return await super(WrapperAgent, self).run(
                    user_prompt,
                    output_type=output_type,
                    message_history=message_history,
                    deferred_tool_results=deferred_tool_results,
                    model=model,
                    instructions=instructions,
                    deps=deps,
                    model_settings=model_settings,
                    usage_limits=usage_limits,
                    usage=usage,
                    metadata=metadata,
                    infer_name=infer_name,
                    toolsets=toolsets,
                    builtin_tools=builtin_tools,
                    event_stream_handler=event_stream_handler,
                    **_deprecated_kwargs,
                )

        self.dbos_wrapped_run_workflow = wrapped_run_workflow

        # Wrap the `run_sync` method in a DBOS workflow
        @DBOS.workflow(name=f'{self._name}.run_sync')
        def wrapped_run_sync_workflow(
            user_prompt: str | Sequence[_messages.UserContent] | None = None,
            *,
            output_type: OutputSpec[RunOutputDataT] | None = None,
            message_history: Sequence[_messages.ModelMessage] | None = None,
            deferred_tool_results: DeferredToolResults | None = None,
            model: models.Model | models.KnownModelName | str | None = None,
            deps: AgentDepsT,
            model_settings: ModelSettings | None = None,
            instructions: Instructions[AgentDepsT] = None,
            usage_limits: _usage.UsageLimits | None = None,
            usage: _usage.RunUsage | None = None,
            metadata: AgentMetadata[AgentDepsT] | None = None,
            infer_name: bool = True,
            toolsets: Sequence[AbstractToolset[AgentDepsT]] | None = None,
            builtin_tools: Sequence[AbstractBuiltinTool | BuiltinToolFunc[AgentDepsT]] | None = None,
            event_stream_handler: EventStreamHandler[AgentDepsT] | None = None,
            **_deprecated_kwargs: Never,
        ) -> AgentRunResult[Any]:
            with self._dbos_overrides():
                return super(DBOSAgent, self).run_sync(
                    user_prompt,
                    output_type=output_type,
                    message_history=message_history,
                    deferred_tool_results=deferred_tool_results,
                    model=model,
                    instructions=instructions,
                    deps=deps,
                    model_settings=model_settings,
                    usage_limits=usage_limits,
                    usage=usage,
                    metadata=metadata,
                    infer_name=infer_name,
                    toolsets=toolsets,
                    builtin_tools=builtin_tools,
                    event_stream_handler=event_stream_handler,
                    **_deprecated_kwargs,
                )

        self.dbos_wrapped_run_sync_workflow = wrapped_run_sync_workflow

    @property
    def name(self) -> str | None:
        return self._name

    @name.setter
    def name(self, value: str | None) -> None:  # pragma: no cover
        raise UserError(
            'The agent name cannot be changed after creation. If you need to change the name, create a new agent.'
        )

    @property
    def model(self) -> Model:
        return self._model

    @property
    def event_stream_handler(self) -> EventStreamHandler[AgentDepsT] | None:
        handler = self._event_stream_handler or super().event_stream_handler
        if handler is None:
            return None
        elif DBOS.workflow_id is not None and DBOS.step_id is None:
            # Special case if it's in a DBOS workflow but not a step, we need to iterate through all events and call the handler.
            return self._call_event_stream_handler_in_workflow
        else:
            return handler

    async def _call_event_stream_handler_in_workflow(
        self, ctx: RunContext[AgentDepsT], stream: AsyncIterable[_messages.AgentStreamEvent]
    ) -> None:
        handler = self._event_stream_handler or super().event_stream_handler
        assert handler is not None

        async def streamed_response(event: _messages.AgentStreamEvent):
            yield event

        async for event in stream:
            await handler(ctx, streamed_response(event))

    @property
    def toolsets(self) -> Sequence[AbstractToolset[AgentDepsT]]:
        with self._dbos_overrides():
            return super().toolsets

    @contextmanager
    def _dbos_overrides(self) -> Iterator[None]:
        # Override with DBOSModel and DBOSMCPServer in the toolsets.
        # Use the configured parallel execution mode for deterministic event ordering during DBOS replay.
        with (
            super().override(model=self._model, toolsets=self._toolsets, tools=[]),
            self.parallel_tool_call_execution_mode(self._parallel_execution_mode),
        ):
            yield

    @overload
    async def run(
        self,
        user_prompt: str | Sequence[_messages.UserContent] | None = None,
        *,
        output_type: None = None,
        message_history: Sequence[_messages.ModelMessage] | None = None,
        deferred_tool_results: DeferredToolResults | None = None,
        model: models.Model | models.KnownModelName | str | None = None,
        instructions: Instructions[AgentDepsT] = None,
        deps: AgentDepsT = None,
        model_settings: ModelSettings | None = None,
        usage_limits: _usage.UsageLimits | None = None,
        usage: _usage.RunUsage | None = None,
        metadata: AgentMetadata[AgentDepsT] | None = None,
        infer_name: bool = True,
        toolsets: Sequence[AbstractToolset[AgentDepsT]] | None = None,
        builtin_tools: Sequence[AbstractBuiltinTool | BuiltinToolFunc[AgentDepsT]] | None = None,
        event_stream_handler: EventStreamHandler[AgentDepsT] | None = None,
    ) -> AgentRunResult[OutputDataT]: ...

    @overload
    async def run(
        self,
        user_prompt: str | Sequence[_messages.UserContent] | None = None,
        *,
        output_type: OutputSpec[RunOutputDataT],
        message_history: Sequence[_messages.ModelMessage] | None = None,
        deferred_tool_results: DeferredToolResults | None = None,
        model: models.Model | models.KnownModelName | str | None = None,
        instructions: Instructions[AgentDepsT] = None,
        deps: AgentDepsT = None,
        model_settings: ModelSettings | None = None,
        usage_limits: _usage.UsageLimits | None = None,
        usage: _usage.RunUsage | None = None,
        metadata: AgentMetadata[AgentDepsT] | None = None,
        infer_name: bool = True,
        toolsets: Sequence[AbstractToolset[AgentDepsT]] | None = None,
        builtin_tools: Sequence[AbstractBuiltinTool | BuiltinToolFunc[AgentDepsT]] | None = None,
        event_stream_handler: EventStreamHandler[AgentDepsT] | None = None,
    ) -> AgentRunResult[RunOutputDataT]: ...

    async def run(
        self,
        user_prompt: str | Sequence[_messages.UserContent] | None = None,
        *,
        output_type: OutputSpec[RunOutputDataT] | None = None,
        message_history: Sequence[_messages.ModelMessage] | None = None,
        deferred_tool_results: DeferredToolResults | None = None,
        model: models.Model | models.KnownModelName | str | None = None,
        instructions: Instructions[AgentDepsT] = None,
        deps: AgentDepsT = None,
        model_settings: ModelSettings | None = None,
        usage_limits: _usage.UsageLimits | None = None,
        usage: _usage.RunUsage | None = None,
        metadata: AgentMetadata[AgentDepsT] | None = None,
        infer_name: bool = True,
        toolsets: Sequence[AbstractToolset[AgentDepsT]] | None = None,
        builtin_tools: Sequence[AbstractBuiltinTool | BuiltinToolFunc[AgentDepsT]] | None = None,
        event_stream_handler: EventStreamHandler[AgentDepsT] | None = None,
        **_deprecated_kwargs: Never,
    ) -> AgentRunResult[Any]:
        """Run the agent with a user prompt in async mode.

        This method builds an internal agent graph (using system prompts, tools and result schemas) and then
        runs the graph to completion. The result of the run is returned.

        Example:
    ```python
        from pydantic_ai import Agent

        agent = Agent('openai:gpt-5.2')

        async def main():
            agent_run = await agent.run('What is the capital of France?')
            print(agent_run.output)
            #> The capital of France is Paris.
    ```

        Args:
            user_prompt: User input to start/continue the conversation.
            output_type: Custom output type to use for this run, `output_type` may only be used if the agent has no
                output validators since output validators would expect an argument that matches the agent's output type.
            message_history: History of the conversation so far.
            deferred_tool_results: Optional results for deferred tool calls in the message history.
            model: Optional model to use for this run, required if `model` was not set when creating the agent.
            instructions: Optional additional instructions to use for this run.
            deps: Optional dependencies to use for this run.
            model_settings: Optional settings to use for this model's request.
            usage_limits: Optional limits on model request count or token usage.
            usage: Optional usage to start with, useful for resuming a conversation or agents used in tools.
            metadata: Optional metadata to attach to this run. Accepts a dictionary or a callable taking
                [`RunContext`][pydantic_ai.tools.RunContext]; merged with the agent's configured metadata.
            infer_name: Whether to try to infer the agent name from the call frame if it's not set.
            toolsets: Optional additional toolsets for this run.
            builtin_tools: Optional additional builtin tools for this run.
            event_stream_handler: Optional event stream handler to use for this run.

        Returns:
            The result of the run.
        """
        if model is not None and not isinstance(model, DBOSModel):
            raise UserError(
                'Non-DBOS model cannot be set at agent run time inside a DBOS workflow, it must be set at agent creation time.'
            )
        return await self.dbos_wrapped_run_workflow(
            user_prompt,
            output_type=output_type,
            message_history=message_history,
            deferred_tool_results=deferred_tool_results,
            model=model,
            instructions=instructions,
            deps=deps,
            model_settings=model_settings,
            usage_limits=usage_limits,
            usage=usage,
            metadata=metadata,
            infer_name=infer_name,
            toolsets=toolsets,
            builtin_tools=builtin_tools,
            event_stream_handler=event_stream_handler,
            **_deprecated_kwargs,
        )

    @overload
    def run_sync(
        self,
        user_prompt: str | Sequence[_messages.UserContent] | None = None,
        *,
        output_type: None = None,
        message_history: Sequence[_messages.ModelMessage] | None = None,
        deferred_tool_results: DeferredToolResults | None = None,
        model: models.Model | models.KnownModelName | str | None = None,
        instructions: Instructions[AgentDepsT] = None,
        deps: AgentDepsT = None,
        model_settings: ModelSettings | None = None,
        usage_limits: _usage.UsageLimits | None = None,
        usage: _usage.RunUsage | None = None,
        metadata: AgentMetadata[AgentDepsT] | None = None,
        infer_name: bool = True,
        toolsets: Sequence[AbstractToolset[AgentDepsT]] | None = None,
        builtin_tools: Sequence[AbstractBuiltinTool | BuiltinToolFunc[AgentDepsT]] | None = None,
        event_stream_handler: EventStreamHandler[AgentDepsT] | None = None,
    ) -> AgentRunResult[OutputDataT]: ...

    @overload
    def run_sync(
        self,
        user_prompt: str | Sequence[_messages.UserContent] | None = None,
        *,
        output_type: OutputSpec[RunOutputDataT],
        message_history: Sequence[_messages.ModelMessage] | None = None,
        deferred_tool_results: DeferredToolResults | None = None,
        model: models.Model | models.KnownModelName | str | None = None,
        instructions: Instructions[AgentDepsT] = None,
        deps: AgentDepsT = None,
        model_settings: ModelSettings | None = None,
        usage_limits: _usage.UsageLimits | None = None,
        usage: _usage.RunUsage | None = None,
        metadata: AgentMetadata[AgentDepsT] | None = None,
        infer_name: bool = True,
        toolsets: Sequence[AbstractToolset[AgentDepsT]] | None = None,
        builtin_tools: Sequence[AbstractBuiltinTool | BuiltinToolFunc[AgentDepsT]] | None = None,
        event_stream_handler: EventStreamHandler[AgentDepsT] | None = None,
    ) -> AgentRunResult[RunOutputDataT]: ...

    def run_sync(
        self,
        user_prompt: str | Sequence[_messages.UserContent] | None = None,
        *,
        output_type: OutputSpec[RunOutputDataT] | None = None,
        message_history: Sequence[_messages.ModelMessage] | None = None,
        deferred_tool_results: DeferredToolResults | None = None,
        model: models.Model | models.KnownModelName | str | None = None,
        instructions: Instructions[AgentDepsT] = None,
        deps: AgentDepsT = None,
        model_settings: ModelSettings | None = None,
        usage_limits: _usage.UsageLimits | None = None,
        usage: _usage.RunUsage | None = None,
        metadata: AgentMetadata[AgentDepsT] | None = None,
        infer_name: bool = True,
        toolsets: Sequence[AbstractToolset[AgentDepsT]] | None = None,
        builtin_tools: Sequence[AbstractBuiltinTool | BuiltinToolFunc[AgentDepsT]] | None = None,
        event_stream_handler: EventStreamHandler[AgentDepsT] | None = None,
        **_deprecated_kwargs: Never,
