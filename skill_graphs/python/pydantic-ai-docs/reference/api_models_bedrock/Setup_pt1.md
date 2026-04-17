## Setup
For details on how to set up authentication with this model, see [model configuration for Bedrock](https://ai.pydantic.dev/models/bedrock/).
###  LatestBedrockModelNames `module-attribute`
```
LatestBedrockModelNames = [
    "amazon.titan-tg1-large",
    "amazon.titan-text-lite-v1",
    "amazon.titan-text-express-v1",
    "us.amazon.nova-2-lite-v1:0",
    "us.amazon.nova-pro-v1:0",
    "us.amazon.nova-lite-v1:0",
    "us.amazon.nova-micro-v1:0",
    "anthropic.claude-3-5-sonnet-20241022-v2:0",
    "us.anthropic.claude-3-5-sonnet-20241022-v2:0",
    "anthropic.claude-3-5-haiku-20241022-v1:0",
    "us.anthropic.claude-3-5-haiku-20241022-v1:0",
    "anthropic.claude-instant-v1",
    "anthropic.claude-v2:1",
    "anthropic.claude-v2",
    "anthropic.claude-3-sonnet-20240229-v1:0",
    "us.anthropic.claude-3-sonnet-20240229-v1:0",
    "anthropic.claude-3-haiku-20240307-v1:0",
    "us.anthropic.claude-3-haiku-20240307-v1:0",
    "anthropic.claude-3-opus-20240229-v1:0",
    "us.anthropic.claude-3-opus-20240229-v1:0",
    "anthropic.claude-3-5-sonnet-20240620-v1:0",
    "us.anthropic.claude-3-5-sonnet-20240620-v1:0",
    "anthropic.claude-3-7-sonnet-20250219-v1:0",
    "us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    "anthropic.claude-opus-4-20250514-v1:0",
    "us.anthropic.claude-opus-4-20250514-v1:0",
    "global.anthropic.claude-opus-4-5-20251101-v1:0",
    "anthropic.claude-sonnet-4-20250514-v1:0",
    "us.anthropic.claude-sonnet-4-20250514-v1:0",
    "eu.anthropic.claude-sonnet-4-20250514-v1:0",
    "anthropic.claude-sonnet-4-5-20250929-v1:0",
    "us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    "eu.anthropic.claude-sonnet-4-5-20250929-v1:0",
    "anthropic.claude-sonnet-4-6",
    "us.anthropic.claude-sonnet-4-6",
    "eu.anthropic.claude-sonnet-4-6",
    "anthropic.claude-haiku-4-5-20251001-v1:0",
    "us.anthropic.claude-haiku-4-5-20251001-v1:0",
    "eu.anthropic.claude-haiku-4-5-20251001-v1:0",
    "cohere.command-text-v14",
    "cohere.command-r-v1:0",
    "cohere.command-r-plus-v1:0",
    "cohere.command-light-text-v14",
    "meta.llama3-8b-instruct-v1:0",
    "meta.llama3-70b-instruct-v1:0",
    "meta.llama3-1-8b-instruct-v1:0",
    "us.meta.llama3-1-8b-instruct-v1:0",
    "meta.llama3-1-70b-instruct-v1:0",
    "us.meta.llama3-1-70b-instruct-v1:0",
    "meta.llama3-1-405b-instruct-v1:0",
    "us.meta.llama3-2-11b-instruct-v1:0",
    "us.meta.llama3-2-90b-instruct-v1:0",
    "us.meta.llama3-2-1b-instruct-v1:0",
    "us.meta.llama3-2-3b-instruct-v1:0",
    "us.meta.llama3-3-70b-instruct-v1:0",
    "mistral.mistral-7b-instruct-v0:2",
    "mistral.mixtral-8x7b-instruct-v0:1",
    "mistral.mistral-large-2402-v1:0",
    "mistral.mistral-large-2407-v1:0",
]

```

Latest Bedrock models.
###  BedrockModelName `module-attribute`
```
BedrockModelName =  | LatestBedrockModelNames[](https://ai.pydantic.dev/api/models/bedrock/#pydantic_ai.models.bedrock.LatestBedrockModelNames "LatestBedrockModelNames



      module-attribute
   \(pydantic_ai.models.bedrock.LatestBedrockModelNames\)")

```

Possible Bedrock model names.
Since Bedrock supports a variety of date-stamped models, we explicitly list the latest models but allow any name in the type hints. See
###  BedrockModelSettings
Bases: `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)")`
Settings for Bedrock models.
See
Source code in `pydantic_ai_slim/pydantic_ai/models/bedrock.py`
```
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
```
| ```
class BedrockModelSettings(ModelSettings, total=False):
    """Settings for Bedrock models.

    See [the Bedrock Converse API docs](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html#API_runtime_Converse_RequestSyntax) for a full list.
    See [the boto3 implementation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/converse.html) of the Bedrock Converse API.
    """

    # ALL FIELDS MUST BE `bedrock_` PREFIXED SO YOU CAN MERGE THEM WITH OTHER MODELS.

    bedrock_guardrail_config: GuardrailConfigurationTypeDef
    """Content moderation and safety settings for Bedrock API requests.

    See more about it on <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_GuardrailConfiguration.html>.
    """

    bedrock_performance_configuration: PerformanceConfigurationTypeDef
    """Performance optimization settings for model inference.

    See more about it on <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_PerformanceConfiguration.html>.
    """

    bedrock_request_metadata: dict[str, str]
    """Additional metadata to attach to Bedrock API requests.

    See more about it on <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html#API_runtime_Converse_RequestSyntax>.
    """

    bedrock_additional_model_response_fields_paths: list[str]
    """JSON paths to extract additional fields from model responses.

    See more about it on <https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html>.
    """

    bedrock_prompt_variables: Mapping[str, PromptVariableValuesTypeDef]
    """Variables for substitution into prompt templates.

    See more about it on <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_PromptVariableValues.html>.
    """

    bedrock_additional_model_requests_fields: Mapping[str, Any]
    """Additional model-specific parameters to include in requests.

    See more about it on <https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html>.
    """

    bedrock_cache_tool_definitions: bool
    """Whether to add a cache point after the last tool definition.

    When enabled, the last tool in the `tools` array will include a `cachePoint`, allowing Bedrock to cache tool
    definitions and reduce costs for compatible models.
    See https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html for more information.
    """

    bedrock_cache_instructions: bool
    """Whether to add a cache point after the system prompt blocks.

    When enabled, an extra `cachePoint` is appended to the system prompt so Bedrock can cache system instructions.
    See https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html for more information.
    """

    bedrock_cache_messages: bool
    """Convenience setting to enable caching for the last user message.

    When enabled, this automatically adds a cache point to the last content block
    in the final user message, which is useful for caching conversation history
    or context in multi-turn conversations.

    Note: Uses 1 of Bedrock's 4 available cache points per request. Any additional CachePoint
    markers in messages will be automatically limited to respect the 4-cache-point maximum.
    See https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html for more information.
    """

    bedrock_service_tier: ServiceTierTypeDef
    """Setting for optimizing performance and cost

    See more about it on <https://docs.aws.amazon.com/bedrock/latest/userguide/service-tiers-inference.html>.
    """

```

---|---
####  bedrock_guardrail_config `instance-attribute`
```
bedrock_guardrail_config: GuardrailConfigurationTypeDef

```

Content moderation and safety settings for Bedrock API requests.
See more about it on
####  bedrock_performance_configuration `instance-attribute`
```
bedrock_performance_configuration: (
    PerformanceConfigurationTypeDef
)

```

Performance optimization settings for model inference.
See more about it on
####  bedrock_request_metadata `instance-attribute`
```
bedrock_request_metadata: [, ]

```

Additional metadata to attach to Bedrock API requests.
See more about it on
####  bedrock_additional_model_response_fields_paths `instance-attribute`
```
bedrock_additional_model_response_fields_paths: []

```

JSON paths to extract additional fields from model responses.
See more about it on
####  bedrock_prompt_variables `instance-attribute`
```
bedrock_prompt_variables: [
    , PromptVariableValuesTypeDef
]

```

Variables for substitution into prompt templates.
See more about it on
####  bedrock_additional_model_requests_fields `instance-attribute`
```
bedrock_additional_model_requests_fields: [, ]

```

Additional model-specific parameters to include in requests.
See more about it on
####  bedrock_cache_tool_definitions `instance-attribute`
```
bedrock_cache_tool_definitions:

```

Whether to add a cache point after the last tool definition.
When enabled, the last tool in the `tools` array will include a `cachePoint`, allowing Bedrock to cache tool definitions and reduce costs for compatible models. See https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html for more information.
####  bedrock_cache_instructions `instance-attribute`
```
bedrock_cache_instructions:

```

Whether to add a cache point after the system prompt blocks.
When enabled, an extra `cachePoint` is appended to the system prompt so Bedrock can cache system instructions. See https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html for more information.
####  bedrock_cache_messages `instance-attribute`
```
bedrock_cache_messages:

```

Convenience setting to enable caching for the last user message.
When enabled, this automatically adds a cache point to the last content block in the final user message, which is useful for caching conversation history or context in multi-turn conversations.
Note: Uses 1 of Bedrock's 4 available cache points per request. Any additional CachePoint markers in messages will be automatically limited to respect the 4-cache-point maximum. See https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html for more information.
####  bedrock_service_tier `instance-attribute`
```
bedrock_service_tier: ServiceTierTypeDef

```

Setting for optimizing performance and cost
See more about it on
###  BedrockConverseModel `dataclass`
Bases: `Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)")`
A model that uses the Bedrock Converse API.
Source code in `pydantic_ai_slim/pydantic_ai/models/bedrock.py`
```
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
1020
1021
1022
1023
1024
```
| ```
@dataclass(init=False)
class BedrockConverseModel(Model):
    """A model that uses the Bedrock Converse API."""

    client: BedrockRuntimeClient

    _model_name: BedrockModelName = field(repr=False)
    _provider: Provider[BaseClient] = field(repr=False)

    def __init__(
        self,
        model_name: BedrockModelName,
        *,
        provider: Literal['bedrock', 'gateway'] | Provider[BaseClient] = 'bedrock',
        profile: ModelProfileSpec | None = None,
        settings: ModelSettings | None = None,
    ):
        """Initialize a Bedrock model.

        Args:
            model_name: The name of the model to use.
            model_name: The name of the Bedrock model to use. List of model names available
                [here](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html).
            provider: The provider to use for authentication and API access. Can be either the string
                'bedrock' or an instance of `Provider[BaseClient]`. If not provided, a new provider will be
                created using the other parameters.
            profile: The model profile to use. Defaults to a profile picked by the provider based on the model name.
            settings: Model-specific settings that will be used as defaults for this model.
        """
        self._model_name = model_name

        if isinstance(provider, str):
            provider = infer_provider('gateway/bedrock' if provider == 'gateway' else provider)
        self._provider = provider
        self.client = cast('BedrockRuntimeClient', provider.client)

        super().__init__(settings=settings, profile=profile or provider.model_profile)

    @property
    def base_url(self) -> str:
        return str(self.client.meta.endpoint_url)

    @property
    def model_name(self) -> str:
        """The model name."""
        return self._model_name

    @property
    def system(self) -> str:
        """The model provider."""
        return self._provider.name

    @classmethod
    def supported_builtin_tools(cls) -> frozenset[type[AbstractBuiltinTool]]:
        """The set of builtin tool types this model can handle."""
        return frozenset({CodeExecutionTool})

    def _get_tools(self, model_request_parameters: ModelRequestParameters) -> list[ToolTypeDef]:
        return [self._map_tool_definition(r) for r in model_request_parameters.tool_defs.values()]

    @staticmethod
    def _map_tool_definition(f: ToolDefinition) -> ToolTypeDef:
        tool_spec: ToolSpecificationTypeDef = {'name': f.name, 'inputSchema': {'json': f.parameters_json_schema}}

        if f.description:  # pragma: no branch
            tool_spec['description'] = f.description

        return {'toolSpec': tool_spec}

    async def request(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> ModelResponse:
        model_settings, model_request_parameters = self.prepare_request(
            model_settings,
            model_request_parameters,
        )
        settings = cast(BedrockModelSettings, model_settings or {})
        response = await self._messages_create(messages, False, settings, model_request_parameters)
        model_response = await self._process_response(response)
        return model_response

    async def count_tokens(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> usage.RequestUsage:
        """Count the number of tokens, works with limited models.

        Check the actual supported models on <https://docs.aws.amazon.com/bedrock/latest/userguide/count-tokens.html>
        """
        model_settings, model_request_parameters = self.prepare_request(model_settings, model_request_parameters)
        settings = cast(BedrockModelSettings, model_settings or {})
        system_prompt, bedrock_messages = await self._map_messages(messages, model_request_parameters, settings)
        params: CountTokensRequestTypeDef = {
            'modelId': remove_bedrock_geo_prefix(self.model_name),
            'input': {
                'converse': {
                    'messages': bedrock_messages,
                    'system': system_prompt,
                },
            },
        }
        try:
            response = await anyio.to_thread.run_sync(functools.partial(self.client.count_tokens, **params))
        except ClientError as e:
            status_code = e.response.get('ResponseMetadata', {}).get('HTTPStatusCode')
            if isinstance(status_code, int):
                raise ModelHTTPError(status_code=status_code, model_name=self.model_name, body=e.response) from e
            raise ModelAPIError(model_name=self.model_name, message=str(e)) from e
        return usage.RequestUsage(input_tokens=response['inputTokens'])

    @asynccontextmanager
    async def request_stream(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
        run_context: RunContext[Any] | None = None,
    ) -> AsyncIterator[StreamedResponse]:
        model_settings, model_request_parameters = self.prepare_request(
            model_settings,
            model_request_parameters,
        )
        settings = cast(BedrockModelSettings, model_settings or {})
        response = await self._messages_create(messages, True, settings, model_request_parameters)
        yield BedrockStreamedResponse(
            model_request_parameters=model_request_parameters,
            _model_name=self.model_name,
            _event_stream=response['stream'],
            _provider_name=self._provider.name,
            _provider_url=self.base_url,
            _provider_response_id=response.get('ResponseMetadata', {}).get('RequestId', None),
        )

    async def _process_response(self, response: ConverseResponseTypeDef) -> ModelResponse:
        items: list[ModelResponsePart] = []
        if message := response['output'].get('message'):  # pragma: no branch
            for item in message['content']:
                if reasoning_content := item.get('reasoningContent'):
                    if redacted_content := reasoning_content.get('redactedContent'):
                        items.append(
                            ThinkingPart(
                                id='redacted_content',
                                content='',
                                signature=redacted_content.decode('utf-8'),
                                provider_name=self.system,
                            )
                        )
                    elif reasoning_text := reasoning_content.get('reasoningText'):  # pragma: no branch
                        signature = reasoning_text.get('signature')
                        items.append(
                            ThinkingPart(
                                content=reasoning_text['text'],
                                signature=signature,
                                provider_name=self.system if signature else None,
                            )
                        )
                if text := item.get('text'):
                    items.append(TextPart(content=text))
                elif tool_use := item.get('toolUse'):
                    if tool_use.get('type') == 'server_tool_use':
                        if tool_use['name'] == 'nova_code_interpreter':  # pragma: no branch
                            items.append(
                                BuiltinToolCallPart(
                                    provider_name=self.system,
                                    tool_name=CodeExecutionTool.kind,
                                    args=tool_use['input'],
                                    tool_call_id=tool_use['toolUseId'],
                                )
                            )
                    else:
                        items.append(
                            ToolCallPart(
                                tool_name=tool_use['name'],
                                args=tool_use['input'],
                                tool_call_id=tool_use['toolUseId'],
                            ),
                        )
                elif tool_result := item.get('toolResult'):
                    if tool_result.get('type') == 'nova_code_interpreter_result':  # pragma: no branch
                        items.append(
                            BuiltinToolReturnPart(
                                provider_name=self.system,
                                tool_name=CodeExecutionTool.kind,
                                content=tool_result['content'][0].get('json') if tool_result['content'] else None,
                                tool_call_id=tool_result.get('toolUseId'),
                                provider_details={'status': tool_result['status']} if 'status' in tool_result else {},
                            )
                        )

        input_tokens = response['usage']['inputTokens']
        output_tokens = response['usage']['outputTokens']
        cache_read_tokens = response['usage'].get('cacheReadInputTokens', 0)
        cache_write_tokens = response['usage'].get('cacheWriteInputTokens', 0)
        u = usage.RequestUsage(
            input_tokens=input_tokens + cache_write_tokens + cache_read_tokens,
            output_tokens=output_tokens,
            cache_read_tokens=cache_read_tokens,
            cache_write_tokens=cache_write_tokens,
        )
        response_id = response.get('ResponseMetadata', {}).get('RequestId', None)
        raw_finish_reason = response['stopReason']
        provider_details = {'finish_reason': raw_finish_reason}
        finish_reason = _FINISH_REASON_MAP.get(raw_finish_reason)

        return ModelResponse(
            parts=items,
            usage=u,
            model_name=self.model_name,
            provider_response_id=response_id,
            provider_name=self._provider.name,
            provider_url=self.base_url,
            finish_reason=finish_reason,
            provider_details=provider_details,
        )

    @overload
    async def _messages_create(
        self,
        messages: list[ModelMessage],
        stream: Literal[True],
        model_settings: BedrockModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> ConverseStreamResponseTypeDef:
        pass

    @overload
    async def _messages_create(
        self,
        messages: list[ModelMessage],
        stream: Literal[False],
        model_settings: BedrockModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> ConverseResponseTypeDef:
        pass

    async def _messages_create(
        self,
        messages: list[ModelMessage],
        stream: bool,
        model_settings: BedrockModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> ConverseResponseTypeDef | ConverseStreamResponseTypeDef:
        settings = model_settings or BedrockModelSettings()
        system_prompt, bedrock_messages = await self._map_messages(messages, model_request_parameters, settings)
        inference_config = self._map_inference_config(settings)

        params: ConverseRequestTypeDef = {
            'modelId': self.model_name,
            'messages': bedrock_messages,
            'system': system_prompt,
            'inferenceConfig': inference_config,
        }

        tool_config = self._map_tool_config(model_request_parameters, settings)
