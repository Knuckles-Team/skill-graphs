2300
2301
2302
2303
2304
2305
2306
2307
2308
2309
2310
2311
2312
2313
2314
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
```
| ```
@dataclass
class OpenAIStreamedResponse(StreamedResponse):
    """Implementation of `StreamedResponse` for OpenAI models."""

    _model_name: OpenAIModelName
    _model_profile: ModelProfile
    _response: AsyncIterable[ChatCompletionChunk]
    _provider_name: str
    _provider_url: str
    _provider_timestamp: datetime | None = None
    _timestamp: datetime = field(default_factory=_now_utc)
    _model_settings: OpenAIChatModelSettings | None = None
    _has_refusal: bool = field(default=False, init=False)
    _refusal_text: str = field(default='', init=False)

    async def _get_event_iterator(self) -> AsyncIterator[ModelResponseStreamEvent]:
        if self._provider_timestamp is not None:  # pragma: no branch
            self.provider_details = {'timestamp': self._provider_timestamp}
        async for chunk in self._validate_response():
            chunk_usage = self._map_usage(chunk)
            if self._model_settings and self._model_settings.get('openai_continuous_usage_stats'):
                # When continuous_usage_stats is enabled, each chunk contains cumulative usage,
                # so we replace rather than increment to avoid double-counting.
                self._usage = chunk_usage
            else:
                self._usage += chunk_usage

            if chunk.id:  # pragma: no branch
                self.provider_response_id = chunk.id

            if chunk.model:
                self._model_name = chunk.model

            try:
                choice = chunk.choices[0]
            except IndexError:
                continue

            # When using Azure OpenAI and an async content filter is enabled, the openai SDK can return None deltas.
            if choice.delta is None:  # pyright: ignore[reportUnnecessaryComparison]
                continue

            # Handle refusal responses (structured output safety filter).
            # Note: OpenAI sends refusal instead of content (not alongside it), so in practice
            # text parts won't have been yielded before _has_refusal is set.
            if choice.delta.refusal:
                self._has_refusal = True
                self.finish_reason = 'content_filter'
                self._refusal_text += choice.delta.refusal
                continue

            if raw_finish_reason := choice.finish_reason:
                if not self._has_refusal:
                    self.finish_reason = self._map_finish_reason(raw_finish_reason)

            if provider_details := self._map_provider_details(chunk):  # pragma: no branch
                if self._has_refusal:
                    provider_details.pop('finish_reason', None)
                self.provider_details = {**(self.provider_details or {}), **provider_details}

            for event in self._map_part_delta(choice):
                yield event

        if self._refusal_text:
            self.provider_details = {**(self.provider_details or {}), 'refusal': self._refusal_text}

    def _validate_response(self) -> AsyncIterable[ChatCompletionChunk]:
        """Hook that validates incoming chunks.

        This method may be overridden by subclasses of `OpenAIStreamedResponse` to apply custom chunk validations.

        By default, this is a no-op since `ChatCompletionChunk` is already validated.
        """
        return self._response

    def _map_part_delta(self, choice: chat_completion_chunk.Choice) -> Iterable[ModelResponseStreamEvent]:
        """Hook that determines the sequence of mappings that will be called to produce events.

        This method may be overridden by subclasses of `OpenAIStreamResponse` to customize the mapping.
        """
        return itertools.chain(
            self._map_thinking_delta(choice), self._map_text_delta(choice), self._map_tool_call_delta(choice)
        )

    def _map_thinking_delta(self, choice: chat_completion_chunk.Choice) -> Iterable[ModelResponseStreamEvent]:
        """Hook that maps thinking delta content to events.

        This method may be overridden by subclasses of `OpenAIStreamResponse` to customize the mapping.
        """
        profile = OpenAIModelProfile.from_profile(self._model_profile)
        custom_field = profile.openai_chat_thinking_field

        # Prefer the configured custom reasoning field, if present in profile.
        # Fall back to built-in fields if no custom field result was found.

        # The `reasoning_content` field is typically present in DeepSeek and Moonshot models.
        # https://api-docs.deepseek.com/guides/reasoning_model

        # The `reasoning` field is typically present in gpt-oss via Ollama and OpenRouter.
        # - https://cookbook.openai.com/articles/gpt-oss/handle-raw-cot#chat-completions-api
        # - https://openrouter.ai/docs/use-cases/reasoning-tokens#basic-usage-with-reasoning-tokens
        for field_name in (custom_field, 'reasoning', 'reasoning_content'):
            if not field_name:
                continue
            reasoning: str | None = getattr(choice.delta, field_name, None)
            if reasoning:  # pragma: no branch
                yield from self._parts_manager.handle_thinking_delta(
                    vendor_part_id=field_name,
                    id=field_name,
                    content=reasoning,
                    provider_name=self.provider_name,
                )
                break

    def _map_text_delta(self, choice: chat_completion_chunk.Choice) -> Iterable[ModelResponseStreamEvent]:
        """Hook that maps text delta content to events.

        This method may be overridden by subclasses of `OpenAIStreamResponse` to customize the mapping.
        """
        # Handle the text part of the response
        content = choice.delta.content
        if content:
            for event in self._parts_manager.handle_text_delta(
                vendor_part_id='content',
                content=content,
                thinking_tags=self._model_profile.thinking_tags,
                ignore_leading_whitespace=self._model_profile.ignore_streamed_leading_whitespace,
            ):
                if isinstance(event, PartStartEvent) and isinstance(event.part, ThinkingPart):
                    event.part.id = 'content'
                    event.part.provider_name = self.provider_name
                yield event

    def _map_tool_call_delta(self, choice: chat_completion_chunk.Choice) -> Iterable[ModelResponseStreamEvent]:
        """Hook that maps tool call delta content to events.

        This method may be overridden by subclasses of `OpenAIStreamResponse` to customize the mapping.
        """
        for dtc in choice.delta.tool_calls or []:
            maybe_event = self._parts_manager.handle_tool_call_delta(
                vendor_part_id=dtc.index,
                tool_name=dtc.function and dtc.function.name,
                args=dtc.function and dtc.function.arguments,
                tool_call_id=dtc.id,
            )
            if maybe_event is not None:
                yield maybe_event

    def _map_provider_details(self, chunk: ChatCompletionChunk) -> dict[str, Any] | None:
        """Hook that generates the provider details from chunk content.

        This method may be overridden by subclasses of `OpenAIStreamResponse` to customize the provider details.
        """
        return _map_provider_details(chunk.choices[0])

    def _map_usage(self, response: ChatCompletionChunk) -> usage.RequestUsage:
        return _map_usage(response, self._provider_name, self._provider_url, self.model_name)

    def _map_finish_reason(
        self, key: Literal['stop', 'length', 'tool_calls', 'content_filter', 'function_call']
    ) -> FinishReason | None:
        """Hooks that maps a finish reason key to a [FinishReason](pydantic_ai.messages.FinishReason).

        This method may be overridden by subclasses of `OpenAIChatModel` to accommodate custom keys.
        """
        return _CHAT_FINISH_REASON_MAP.get(key)

    @property
    def model_name(self) -> OpenAIModelName:
        """Get the model name of the response."""
        return self._model_name

    @property
    def provider_name(self) -> str:
        """Get the provider name."""
        return self._provider_name

    @property
    def provider_url(self) -> str:
        """Get the provider base URL."""
        return self._provider_url

    @property
    def timestamp(self) -> datetime:
        """Get the timestamp of the response."""
        return self._timestamp

```

---|---
####  model_name `property`
```
model_name: OpenAIModelName[](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIModelName "OpenAIModelName



      module-attribute
   \(pydantic_ai.models.openai.OpenAIModelName\)")

```

Get the model name of the response.
####  provider_name `property`
```
provider_name:

```

Get the provider name.
####  provider_url `property`
```
provider_url:

```

Get the provider base URL.
####  timestamp `property`
```
timestamp:

```

Get the timestamp of the response.
###  OpenAIResponsesStreamedResponse `dataclass`
Bases: `StreamedResponse[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.StreamedResponse "StreamedResponse



      dataclass
   \(pydantic_ai.models.StreamedResponse\)")`
Implementation of `StreamedResponse` for OpenAI Responses API.
Source code in `pydantic_ai_slim/pydantic_ai/models/openai.py`
```
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
2692
2693
2694
2695
2696
2697
2698
2699
2700
2701
2702
2703
2704
2705
2706
2707
2708
2709
2710
2711
2712
2713
2714
2715
2716
2717
2718
2719
2720
2721
2722
2723
2724
2725
2726
2727
2728
2729
2730
2731
2732
2733
2734
2735
2736
2737
2738
2739
2740
2741
2742
2743
2744
2745
2746
2747
2748
2749
2750
2751
2752
2753
2754
2755
2756
2757
2758
2759
2760
2761
2762
2763
2764
2765
2766
2767
2768
2769
2770
2771
2772
2773
2774
2775
2776
2777
2778
2779
2780
2781
2782
2783
2784
2785
2786
2787
2788
2789
2790
2791
2792
2793
2794
2795
2796
2797
2798
2799
2800
2801
2802
2803
2804
2805
2806
2807
2808
2809
2810
2811
2812
2813
2814
2815
2816
2817
2818
2819
2820
2821
2822
2823
2824
2825
2826
2827
2828
2829
2830
2831
2832
2833
2834
2835
2836
2837
2838
2839
2840
2841
2842
2843
2844
2845
2846
2847
2848
2849
2850
2851
```
| ```
@dataclass
class OpenAIResponsesStreamedResponse(StreamedResponse):
    """Implementation of `StreamedResponse` for OpenAI Responses API."""

    _model_name: OpenAIModelName
    _model_settings: OpenAIResponsesModelSettings
    _response: AsyncIterable[responses.ResponseStreamEvent]
    _provider_name: str
    _provider_url: str
    _provider_timestamp: datetime | None = None
    _timestamp: datetime = field(default_factory=_now_utc)
    _has_refusal: bool = field(default=False, init=False)
    _refusal_text: str = field(default='', init=False)

    async def _get_event_iterator(self) -> AsyncIterator[ModelResponseStreamEvent]:  # noqa: C901
        # Track annotations by item_id and content_index
        _annotations_by_item: dict[str, list[Any]] = {}

        if self._provider_timestamp is not None:  # pragma: no branch
            self.provider_details = {'timestamp': self._provider_timestamp}

        async for chunk in self._response:
            # NOTE: You can inspect the builtin tools used checking the `ResponseCompletedEvent`.
            if isinstance(chunk, responses.ResponseCompletedEvent):
                self._usage += self._map_usage(chunk.response)

                raw_finish_reason = (
                    details.reason if (details := chunk.response.incomplete_details) else chunk.response.status
                )

                if raw_finish_reason:  # pragma: no branch
                    if not self._has_refusal:
                        self.provider_details = {**(self.provider_details or {}), 'finish_reason': raw_finish_reason}
                        self.finish_reason = _RESPONSES_FINISH_REASON_MAP.get(raw_finish_reason)

            elif isinstance(chunk, responses.ResponseContentPartAddedEvent):
                pass  # there's nothing we need to do here

            elif isinstance(chunk, responses.ResponseContentPartDoneEvent):
                pass  # there's nothing we need to do here

            elif isinstance(chunk, responses.ResponseCreatedEvent):
                if chunk.response.id:  # pragma: no branch
                    self.provider_response_id = chunk.response.id

            elif isinstance(chunk, responses.ResponseFailedEvent):  # pragma: no cover
                self._usage += self._map_usage(chunk.response)

            elif isinstance(chunk, responses.ResponseFunctionCallArgumentsDeltaEvent):
                maybe_event = self._parts_manager.handle_tool_call_delta(
                    vendor_part_id=chunk.item_id,
                    args=chunk.delta,
                )
                if maybe_event is not None:  # pragma: no branch
                    yield maybe_event

            elif isinstance(chunk, responses.ResponseFunctionCallArgumentsDoneEvent):
                pass  # there's nothing we need to do here

            elif isinstance(chunk, responses.ResponseIncompleteEvent):  # pragma: no cover
                self._usage += self._map_usage(chunk.response)

            elif isinstance(chunk, responses.ResponseInProgressEvent):
                self._usage += self._map_usage(chunk.response)

            elif isinstance(chunk, responses.ResponseOutputItemAddedEvent):
                if isinstance(chunk.item, responses.ResponseFunctionToolCall):
                    yield self._parts_manager.handle_tool_call_part(
                        vendor_part_id=chunk.item.id,
                        tool_name=chunk.item.name,
                        args=chunk.item.arguments,
                        tool_call_id=chunk.item.call_id,
                        id=chunk.item.id,
                        provider_name=self.provider_name,
                    )
                elif isinstance(chunk.item, responses.ResponseReasoningItem):
                    pass
                elif isinstance(chunk.item, responses.ResponseOutputMessage):
                    pass
                elif isinstance(chunk.item, responses.ResponseFunctionWebSearch):
                    call_part, _ = _map_web_search_tool_call(chunk.item, self.provider_name)
                    yield self._parts_manager.handle_part(
                        vendor_part_id=f'{chunk.item.id}-call', part=replace(call_part, args=None)
                    )
                elif isinstance(chunk.item, responses.ResponseFileSearchToolCall):
                    call_part, _ = _map_file_search_tool_call(chunk.item, self.provider_name)
                    yield self._parts_manager.handle_part(
                        vendor_part_id=f'{chunk.item.id}-call', part=replace(call_part, args=None)
                    )
                elif isinstance(chunk.item, responses.ResponseCodeInterpreterToolCall):
                    call_part, _, _ = _map_code_interpreter_tool_call(chunk.item, self.provider_name)

                    args_json = call_part.args_as_json_str()
                    # Drop the final `"}` so that we can add code deltas
                    args_json_delta = args_json[:-2]
                    assert args_json_delta.endswith('"code":"'), f'Expected {args_json_delta!r} to end in `"code":"`'

                    yield self._parts_manager.handle_part(
                        vendor_part_id=f'{chunk.item.id}-call', part=replace(call_part, args=None)
                    )
                    maybe_event = self._parts_manager.handle_tool_call_delta(
                        vendor_part_id=f'{chunk.item.id}-call',
                        args=args_json_delta,
                    )
                    if maybe_event is not None:  # pragma: no branch
                        yield maybe_event
                elif isinstance(chunk.item, responses.response_output_item.ImageGenerationCall):
                    call_part, _, _ = _map_image_generation_tool_call(chunk.item, self.provider_name)
                    yield self._parts_manager.handle_part(vendor_part_id=f'{chunk.item.id}-call', part=call_part)
                elif isinstance(chunk.item, responses.response_output_item.McpCall):
                    call_part, _ = _map_mcp_call(chunk.item, self.provider_name)

                    args_json = call_part.args_as_json_str()
                    # Drop the final `{}}` so that we can add tool args deltas
                    args_json_delta = args_json[:-3]
                    assert args_json_delta.endswith('"tool_args":'), (
                        f'Expected {args_json_delta!r} to end in `"tool_args":"`'
                    )

                    yield self._parts_manager.handle_part(
                        vendor_part_id=f'{chunk.item.id}-call', part=replace(call_part, args=None)
                    )
                    maybe_event = self._parts_manager.handle_tool_call_delta(
                        vendor_part_id=f'{chunk.item.id}-call',
                        args=args_json_delta,
                    )
                    if maybe_event is not None:  # pragma: no branch
                        yield maybe_event
                elif isinstance(chunk.item, responses.response_output_item.McpListTools):
                    call_part, _ = _map_mcp_list_tools(chunk.item, self.provider_name)
                    yield self._parts_manager.handle_part(vendor_part_id=f'{chunk.item.id}-call', part=call_part)
                else:
                    warnings.warn(  # pragma: no cover
                        f'Handling of this item type is not yet implemented. Please report on our GitHub: {chunk}',
                        UserWarning,
                    )

            elif isinstance(chunk, responses.ResponseOutputItemDoneEvent):
                if isinstance(chunk.item, responses.ResponseReasoningItem):
                    if signature := chunk.item.encrypted_content:  # pragma: no branch
                        # Add the signature to the part corresponding to the first summary/raw CoT
                        for event in self._parts_manager.handle_thinking_delta(
                            vendor_part_id=chunk.item.id,
                            id=chunk.item.id,
                            signature=signature,
                            provider_name=self.provider_name,
                        ):
                            yield event
                elif isinstance(chunk.item, responses.ResponseCodeInterpreterToolCall):
                    _, return_part, file_parts = _map_code_interpreter_tool_call(chunk.item, self.provider_name)
                    for i, file_part in enumerate(file_parts):
                        yield self._parts_manager.handle_part(
                            vendor_part_id=f'{chunk.item.id}-file-{i}', part=file_part
                        )
                    yield self._parts_manager.handle_part(vendor_part_id=f'{chunk.item.id}-return', part=return_part)
                elif isinstance(chunk.item, responses.ResponseFunctionWebSearch):
                    call_part, return_part = _map_web_search_tool_call(chunk.item, self.provider_name)

                    maybe_event = self._parts_manager.handle_tool_call_delta(
                        vendor_part_id=f'{chunk.item.id}-call',
                        args=call_part.args,
                    )
                    if maybe_event is not None:  # pragma: no branch
                        yield maybe_event

                    yield self._parts_manager.handle_part(vendor_part_id=f'{chunk.item.id}-return', part=return_part)
                elif isinstance(chunk.item, responses.ResponseFileSearchToolCall):
                    call_part, return_part = _map_file_search_tool_call(chunk.item, self.provider_name)

                    maybe_event = self._parts_manager.handle_tool_call_delta(
                        vendor_part_id=f'{chunk.item.id}-call',
                        args=call_part.args,
                    )
                    if maybe_event is not None:  # pragma: no branch
                        yield maybe_event

                    yield self._parts_manager.handle_part(vendor_part_id=f'{chunk.item.id}-return', part=return_part)
                elif isinstance(chunk.item, responses.response_output_item.ImageGenerationCall):
                    _, return_part, file_part = _map_image_generation_tool_call(chunk.item, self.provider_name)
                    if file_part:  # pragma: no branch
                        yield self._parts_manager.handle_part(vendor_part_id=f'{chunk.item.id}-file', part=file_part)
                    yield self._parts_manager.handle_part(vendor_part_id=f'{chunk.item.id}-return', part=return_part)

                elif isinstance(chunk.item, responses.response_output_item.McpCall):
                    _, return_part = _map_mcp_call(chunk.item, self.provider_name)
                    yield self._parts_manager.handle_part(vendor_part_id=f'{chunk.item.id}-return', part=return_part)
                elif isinstance(chunk.item, responses.response_output_item.McpListTools):
                    _, return_part = _map_mcp_list_tools(chunk.item, self.provider_name)
                    yield self._parts_manager.handle_part(vendor_part_id=f'{chunk.item.id}-return', part=return_part)

            elif isinstance(chunk, responses.ResponseReasoningSummaryPartAddedEvent):
                # Use same vendor_part_id as raw CoT for first summary (index 0) so they merge into one ThinkingPart
                vendor_id = chunk.item_id if chunk.summary_index == 0 else f'{chunk.item_id}-{chunk.summary_index}'
                for event in self._parts_manager.handle_thinking_delta(
                    vendor_part_id=vendor_id,
                    content=chunk.part.text,
                    id=chunk.item_id,
                    provider_name=self.provider_name,
                ):
                    yield event

            elif isinstance(chunk, responses.ResponseReasoningSummaryPartDoneEvent):
                pass  # there's nothing we need to do here

            elif isinstance(chunk, responses.ResponseReasoningSummaryTextDoneEvent):
                pass  # there's nothing we need to do here

            elif isinstance(chunk, responses.ResponseReasoningSummaryTextDeltaEvent):
                # Use same vendor_part_id as raw CoT for first summary (index 0) so they merge into one ThinkingPart
                vendor_id = chunk.item_id if chunk.summary_index == 0 else f'{chunk.item_id}-{chunk.summary_index}'
                for event in self._parts_manager.handle_thinking_delta(
                    vendor_part_id=vendor_id,
                    content=chunk.delta,
                    id=chunk.item_id,
                    provider_name=self.provider_name,
                ):
                    yield event

            elif isinstance(chunk, responses.ResponseReasoningTextDeltaEvent):
                # Handle raw CoT from gpt-oss models using callback pattern
                for event in self._parts_manager.handle_thinking_delta(
                    vendor_part_id=chunk.item_id,
                    id=chunk.item_id,
                    provider_name=self.provider_name,
                    provider_details=_make_raw_content_updater(chunk.delta, chunk.content_index),
                ):
                    yield event

            elif isinstance(chunk, responses.ResponseReasoningTextDoneEvent):
                pass  # content already accumulated via delta events

            elif isinstance(chunk, responses.ResponseOutputTextAnnotationAddedEvent):
                # Collect annotations if the setting is enabled
                if self._model_settings.get('openai_include_raw_annotations'):
