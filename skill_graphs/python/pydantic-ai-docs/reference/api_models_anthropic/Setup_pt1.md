## Setup
For details on how to set up authentication with this model, see [model configuration for Anthropic](https://ai.pydantic.dev/models/anthropic/).
###  LatestAnthropicModelNames `module-attribute`
```
LatestAnthropicModelNames = ModelParam

```

Latest Anthropic models.
###  AnthropicModelName `module-attribute`
```
AnthropicModelName =  | LatestAnthropicModelNames[](https://ai.pydantic.dev/api/models/anthropic/#pydantic_ai.models.anthropic.LatestAnthropicModelNames "LatestAnthropicModelNames



      module-attribute
   \(pydantic_ai.models.anthropic.LatestAnthropicModelNames\)")

```

Possible Anthropic model names.
Since Anthropic supports a variety of date-stamped models, we explicitly list the latest models but allow any name in the type hints. See
###  AnthropicModelSettings
Bases: `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)")`
Settings used for an Anthropic model request.
Source code in `pydantic_ai_slim/pydantic_ai/models/anthropic.py`
```
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
```
| ```
class AnthropicModelSettings(ModelSettings, total=False):
    """Settings used for an Anthropic model request."""

    # ALL FIELDS MUST BE `anthropic_` PREFIXED SO YOU CAN MERGE THEM WITH OTHER MODELS.

    anthropic_metadata: BetaMetadataParam
    """An object describing metadata about the request.

    Contains `user_id`, an external identifier for the user who is associated with the request.
    """

    anthropic_thinking: BetaThinkingConfigParam
    """Determine whether the model should generate a thinking block.

    See [the Anthropic docs](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking) for more information.
    """

    anthropic_cache_tool_definitions: bool | Literal['5m', '1h']
    """Whether to add `cache_control` to the last tool definition.

    When enabled, the last tool in the `tools` array will have `cache_control` set,
    allowing Anthropic to cache tool definitions and reduce costs.
    If `True`, uses TTL='5m'. You can also specify '5m' or '1h' directly.
    TTL is automatically omitted for Bedrock, as it does not support explicit TTL.
    See https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching for more information.
    """

    anthropic_cache_instructions: bool | Literal['5m', '1h']
    """Whether to add `cache_control` to the last system prompt block.

    When enabled, the last system prompt will have `cache_control` set,
    allowing Anthropic to cache system instructions and reduce costs.
    If `True`, uses TTL='5m'. You can also specify '5m' or '1h' directly.
    TTL is automatically omitted for Bedrock, as it does not support explicit TTL.
    See https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching for more information.
    """

    anthropic_cache_messages: bool | Literal['5m', '1h']
    """Convenience setting to enable caching for the last user message.

    When enabled, this automatically adds a cache point to the last content block
    in the final user message, which is useful for caching conversation history
    or context in multi-turn conversations.
    If `True`, uses TTL='5m'. You can also specify '5m' or '1h' directly.
    TTL is automatically omitted for Bedrock, as it does not support explicit TTL.

    Note: Uses 1 of Anthropic's 4 available cache points per request. Any additional CachePoint
    markers in messages will be automatically limited to respect the 4-cache-point maximum.
    See https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching for more information.
    """

    anthropic_effort: Literal['low', 'medium', 'high', 'max'] | None
    """The effort level for the model to use when generating a response.

    See [the Anthropic docs](https://docs.anthropic.com/en/docs/build-with-claude/effort) for more information.
    """

    anthropic_container: BetaContainerParams | Literal[False]
    """Container configuration for multi-turn conversations.

    By default, if previous messages contain a container_id (from a prior response),
    it will be reused automatically.

    Set to `False` to force a fresh container (ignore any `container_id` from history).
    Set to a dict (e.g. `{'id': 'container_xxx'}`) to explicitly specify a container.
    """

    anthropic_betas: list[AnthropicBetaParam]
    """List of Anthropic beta features to enable for API requests.

    Each item can be a known beta name (e.g. 'interleaved-thinking-2025-05-14') or a custom string.
    Merged with auto-added betas (e.g. structured-outputs, builtin tools) and any betas from
    extra_headers['anthropic-beta']. See the Anthropic docs for available beta features.
    """

```

---|---
####  anthropic_metadata `instance-attribute`
```
anthropic_metadata: BetaMetadataParam

```

An object describing metadata about the request.
Contains `user_id`, an external identifier for the user who is associated with the request.
####  anthropic_thinking `instance-attribute`
```
anthropic_thinking: BetaThinkingConfigParam

```

Determine whether the model should generate a thinking block.
See
####  anthropic_cache_tool_definitions `instance-attribute`
```
anthropic_cache_tool_definitions:  | ["5m", "1h"]

```

Whether to add `cache_control` to the last tool definition.
When enabled, the last tool in the `tools` array will have `cache_control` set, allowing Anthropic to cache tool definitions and reduce costs. If `True`, uses TTL='5m'. You can also specify '5m' or '1h' directly. TTL is automatically omitted for Bedrock, as it does not support explicit TTL. See https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching for more information.
####  anthropic_cache_instructions `instance-attribute`
```
anthropic_cache_instructions:  | ['5m', '1h']

```

Whether to add `cache_control` to the last system prompt block.
When enabled, the last system prompt will have `cache_control` set, allowing Anthropic to cache system instructions and reduce costs. If `True`, uses TTL='5m'. You can also specify '5m' or '1h' directly. TTL is automatically omitted for Bedrock, as it does not support explicit TTL. See https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching for more information.
####  anthropic_cache_messages `instance-attribute`
```
anthropic_cache_messages:  | ['5m', '1h']

```

Convenience setting to enable caching for the last user message.
When enabled, this automatically adds a cache point to the last content block in the final user message, which is useful for caching conversation history or context in multi-turn conversations. If `True`, uses TTL='5m'. You can also specify '5m' or '1h' directly. TTL is automatically omitted for Bedrock, as it does not support explicit TTL.
Note: Uses 1 of Anthropic's 4 available cache points per request. Any additional CachePoint markers in messages will be automatically limited to respect the 4-cache-point maximum. See https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching for more information.
####  anthropic_effort `instance-attribute`
```
anthropic_effort: (
    ["low", "medium", "high", "max"] | None
)

```

The effort level for the model to use when generating a response.
See
####  anthropic_container `instance-attribute`
```
anthropic_container: BetaContainerParams | [False]

```

Container configuration for multi-turn conversations.
By default, if previous messages contain a container_id (from a prior response), it will be reused automatically.
Set to `False` to force a fresh container (ignore any `container_id` from history). Set to a dict (e.g. `{'id': 'container_xxx'}`) to explicitly specify a container.
####  anthropic_betas `instance-attribute`
```
anthropic_betas: [AnthropicBetaParam]

```

List of Anthropic beta features to enable for API requests.
Each item can be a known beta name (e.g. 'interleaved-thinking-2025-05-14') or a custom string. Merged with auto-added betas (e.g. structured-outputs, builtin tools) and any betas from extra_headers['anthropic-beta']. See the Anthropic docs for available beta features.
###  AnthropicModel `dataclass`
Bases: `Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)")`
A model that uses the Anthropic API.
Internally, this uses the
Apart from `__init__`, all methods are private or match those of the base class.
Source code in `pydantic_ai_slim/pydantic_ai/models/anthropic.py`
```
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
1025
1026
1027
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
```
| ```
@dataclass(init=False)
class AnthropicModel(Model):
    """A model that uses the Anthropic API.

    Internally, this uses the [Anthropic Python client](https://github.com/anthropics/anthropic-sdk-python) to interact with the API.

    Apart from `__init__`, all methods are private or match those of the base class.
    """

    client: AsyncAnthropicClient = field(repr=False)

    _model_name: AnthropicModelName = field(repr=False)
    _provider: Provider[AsyncAnthropicClient] = field(repr=False)

    def __init__(
        self,
        model_name: AnthropicModelName,
        *,
        provider: Literal['anthropic', 'gateway'] | Provider[AsyncAnthropicClient] = 'anthropic',
        profile: ModelProfileSpec | None = None,
        settings: ModelSettings | None = None,
    ):
        """Initialize an Anthropic model.

        Args:
            model_name: The name of the Anthropic model to use. List of model names available
                [here](https://docs.anthropic.com/en/docs/about-claude/models).
            provider: The provider to use for the Anthropic API. Can be either the string 'anthropic' or an
                instance of `Provider[AsyncAnthropicClient]`. Defaults to 'anthropic'.
            profile: The model profile to use. Defaults to a profile picked by the provider based on the model name.
                The default 'anthropic' provider will use the default `..profiles.anthropic.anthropic_model_profile`.
            settings: Default model settings for this model instance.
        """
        self._model_name = model_name

        if isinstance(provider, str):
            provider = infer_provider('gateway/anthropic' if provider == 'gateway' else provider)
        self._provider = provider
        self.client = provider.client

        super().__init__(settings=settings, profile=profile or provider.model_profile)

    @property
    def base_url(self) -> str:
        return str(self.client.base_url)

    @property
    def model_name(self) -> AnthropicModelName:
        """The model name."""
        return self._model_name

    @property
    def system(self) -> str:
        """The model provider."""
        return self._provider.name

    @classmethod
    def supported_builtin_tools(cls) -> frozenset[type[AbstractBuiltinTool]]:
        """The set of builtin tool types this model can handle."""
        return frozenset({WebSearchTool, CodeExecutionTool, WebFetchTool, MemoryTool, MCPServerTool})

    async def request(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> ModelResponse:
        check_allow_model_requests()
        model_settings, model_request_parameters = self.prepare_request(
            model_settings,
            model_request_parameters,
        )
        model_settings = cast(AnthropicModelSettings, model_settings or {})
        try:
            response = await self._messages_create(messages, False, model_settings, model_request_parameters)
            return self._process_response(response)
        except ValueError as e:
            if 'Streaming is required' in str(e):
                # Anthropic SDK requires streaming for high max_tokens; fall back transparently
                # https://github.com/anthropics/anthropic-sdk-python/blob/49d639a671cb0ac30c767e8e1e68fdd5925205d5/src/anthropic/_base_client.py#L726
                stream = await self._messages_create(messages, True, model_settings, model_request_parameters)
                async with stream:
                    streamed_response = await self._process_streamed_response(stream, model_request_parameters)
                    async for _ in streamed_response:
                        pass
                    return streamed_response.get()
            raise  # pragma: no cover

    async def count_tokens(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> usage.RequestUsage:
        model_settings, model_request_parameters = self.prepare_request(
            model_settings,
            model_request_parameters,
        )

        response = await self._messages_count_tokens(
            messages, cast(AnthropicModelSettings, model_settings or {}), model_request_parameters
        )

        return usage.RequestUsage(input_tokens=response.input_tokens)

    @asynccontextmanager
    async def request_stream(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
        run_context: RunContext[Any] | None = None,
    ) -> AsyncIterator[StreamedResponse]:
        check_allow_model_requests()
        model_settings, model_request_parameters = self.prepare_request(
            model_settings,
            model_request_parameters,
        )
        response = await self._messages_create(
            messages, True, cast(AnthropicModelSettings, model_settings or {}), model_request_parameters
        )
        async with response:
            yield await self._process_streamed_response(response, model_request_parameters)

    def prepare_request(
        self, model_settings: ModelSettings | None, model_request_parameters: ModelRequestParameters
    ) -> tuple[ModelSettings | None, ModelRequestParameters]:
        settings = merge_model_settings(self.settings, model_settings)
        if (
            model_request_parameters.output_tools
            and settings
            and (thinking := settings.get('anthropic_thinking'))
            and thinking.get('type') in ('enabled', 'adaptive')
        ):
            if model_request_parameters.output_mode == 'auto':
                output_mode = 'native' if self.profile.supports_json_schema_output else 'prompted'
                model_request_parameters = replace(model_request_parameters, output_mode=output_mode)
            elif (
                model_request_parameters.output_mode == 'tool' and not model_request_parameters.allow_text_output
            ):  # pragma: no branch
                # This would result in `tool_choice=required`, which Anthropic does not support with thinking.
                suggested_output_type = 'NativeOutput' if self.profile.supports_json_schema_output else 'PromptedOutput'
                raise UserError(
                    f'Anthropic does not support thinking and output tools at the same time. Use `output_type={suggested_output_type}(...)` instead.'
                )

        if model_request_parameters.output_mode == 'native':
            assert model_request_parameters.output_object is not None
            if model_request_parameters.output_object.strict is False:
                raise UserError(
                    'Setting `strict=False` on `output_type=NativeOutput(...)` is not allowed for Anthropic models.'
                )
            model_request_parameters = replace(
                model_request_parameters, output_object=replace(model_request_parameters.output_object, strict=True)
            )
        return super().prepare_request(model_settings, model_request_parameters)

    @overload
    async def _messages_create(
        self,
        messages: list[ModelMessage],
        stream: Literal[True],
        model_settings: AnthropicModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> AsyncStream[BetaRawMessageStreamEvent]:
        pass

    @overload
    async def _messages_create(
        self,
        messages: list[ModelMessage],
        stream: Literal[False],
        model_settings: AnthropicModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> BetaMessage:
        pass

    async def _messages_create(
        self,
        messages: list[ModelMessage],
        stream: bool,
        model_settings: AnthropicModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> BetaMessage | AsyncStream[BetaRawMessageStreamEvent]:
        """Calls the Anthropic API to create a message.

        This is the last step before sending the request to the API.
        Most preprocessing has happened in `prepare_request()`.
        """
        tools = self._get_tools(model_request_parameters, model_settings)
        tools, mcp_servers, builtin_tool_betas = self._add_builtin_tools(tools, model_request_parameters)

        tool_choice = self._infer_tool_choice(tools, model_settings, model_request_parameters)

        system_prompt, anthropic_messages = await self._map_message(messages, model_request_parameters, model_settings)
        self._limit_cache_points(system_prompt, anthropic_messages, tools)
        output_config = self._build_output_config(model_request_parameters, model_settings)
        betas, extra_headers = self._get_betas_and_extra_headers(tools, model_request_parameters, model_settings)
        betas.update(builtin_tool_betas)
        container = self._get_container(messages, model_settings)
        try:
            return await self.client.beta.messages.create(
                max_tokens=model_settings.get('max_tokens', 4096),
                system=system_prompt or OMIT,
                messages=anthropic_messages,
                model=self._model_name,
                tools=tools or OMIT,
                tool_choice=tool_choice or OMIT,
                mcp_servers=mcp_servers or OMIT,
                output_config=output_config or OMIT,
                betas=sorted(betas) or OMIT,
                stream=stream,
                thinking=model_settings.get('anthropic_thinking', OMIT),
                stop_sequences=model_settings.get('stop_sequences', OMIT),
                temperature=model_settings.get('temperature', OMIT),
                top_p=model_settings.get('top_p', OMIT),
                timeout=model_settings.get('timeout', NOT_GIVEN),
                metadata=model_settings.get('anthropic_metadata', OMIT),
                container=container or OMIT,
                extra_headers=extra_headers,
                extra_body=model_settings.get('extra_body'),
            )
        except APIStatusError as e:
            if (status_code := e.status_code) >= 400:
                raise ModelHTTPError(status_code=status_code, model_name=self.model_name, body=e.body) from e
            raise ModelAPIError(model_name=self.model_name, message=e.message) from e  # pragma: lax no cover
        except APIConnectionError as e:
            raise ModelAPIError(model_name=self.model_name, message=e.message) from e

    def _get_betas_and_extra_headers(
        self,
        tools: list[BetaToolUnionParam],
        model_request_parameters: ModelRequestParameters,
        model_settings: AnthropicModelSettings,
    ) -> tuple[set[str], dict[str, str]]:
        """Prepare beta features list and extra headers for API request.

        Handles merging custom `anthropic-beta` header from `extra_headers` into betas set
        and ensuring `User-Agent` is set.
        """
        extra_headers = dict(model_settings.get('extra_headers', {}))
        extra_headers.setdefault('User-Agent', get_user_agent())

        betas: set[str] = set()

        has_strict_tools = any(tool.get('strict') for tool in tools)

        if has_strict_tools or model_request_parameters.output_mode == 'native':
            betas.add('structured-outputs-2025-11-13')

        if betas_from_setting := model_settings.get('anthropic_betas'):
            betas.update(str(b) for b in betas_from_setting)

        if beta_header := extra_headers.pop('anthropic-beta', None):
            betas.update({stripped_beta for beta in beta_header.split(',') if (stripped_beta := beta.strip())})

        return betas, extra_headers

    def _get_container(
        self, messages: list[ModelMessage], model_settings: AnthropicModelSettings
    ) -> BetaContainerParams | None:
        """Get container config for the API request."""
        if (container := model_settings.get('anthropic_container')) is not None:
