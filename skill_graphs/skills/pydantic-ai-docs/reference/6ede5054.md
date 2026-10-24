## Setup
For details on how to set up authentication with this model, see [model configuration for OpenAI](https://ai.pydantic.dev/models/openai/).
###  OpenAIModelName `module-attribute`
```
OpenAIModelName =  | AllModels

```

Possible OpenAI model names.
Since OpenAI supports a variety of date-stamped models, we explicitly list the latest models but allow any name in the type hints. See
Using this more broad type for the model name instead of the ChatModel definition allows this model to be used more easily with other model types (ie, Ollama, Deepseek).
###  MCP_SERVER_TOOL_CONNECTOR_URI_SCHEME `module-attribute`
```
MCP_SERVER_TOOL_CONNECTOR_URI_SCHEME: [
    "x-openai-connector"
] = "x-openai-connector"

```

Prefix for OpenAI connector IDs. OpenAI supports either a URL or a connector ID when passing MCP configuration to a model, by using that prefix like `x-openai-connector:<connector-id>` in a URL, you can pass a connector ID to a model.
###  OpenAIChatModelSettings
Bases: `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)")`
Settings used for an OpenAI model request.
Source code in `pydantic_ai_slim/pydantic_ai/models/openai.py`
```
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
```
| ```
class OpenAIChatModelSettings(ModelSettings, total=False):
    """Settings used for an OpenAI model request."""

    # ALL FIELDS MUST BE `openai_` PREFIXED SO YOU CAN MERGE THEM WITH OTHER MODELS.

    openai_reasoning_effort: ReasoningEffort
    """Constrains effort on reasoning for [reasoning models](https://platform.openai.com/docs/guides/reasoning).

    Currently supported values are `low`, `medium`, and `high`. Reducing reasoning effort can
    result in faster responses and fewer tokens used on reasoning in a response.
    """

    openai_logprobs: bool
    """Include log probabilities in the response.

    For Chat models, these will be included in `ModelResponse.provider_details['logprobs']`.
    For Responses models, these will be included in the response output parts `TextPart.provider_details['logprobs']`.
    """

    openai_top_logprobs: int
    """Include log probabilities of the top n tokens in the response."""

    openai_store: bool | None
    """Whether or not to store the output of this request in OpenAI's systems.

    If `False`, OpenAI will not store the request for its own internal review or training.
    See [OpenAI API reference](https://platform.openai.com/docs/api-reference/chat/create#chat-create-store)."""

    openai_user: str
    """A unique identifier representing the end-user, which can help OpenAI monitor and detect abuse.

    See [OpenAI's safety best practices](https://platform.openai.com/docs/guides/safety-best-practices#end-user-ids) for more details.
    """

    openai_service_tier: Literal['auto', 'default', 'flex', 'priority']
    """The service tier to use for the model request.

    Currently supported values are `auto`, `default`, `flex`, and `priority`.
    For more information, see [OpenAI's service tiers documentation](https://platform.openai.com/docs/api-reference/chat/object#chat/object-service_tier).
    """

    openai_prediction: ChatCompletionPredictionContentParam
    """Enables [predictive outputs](https://platform.openai.com/docs/guides/predicted-outputs).

    This feature is currently only supported for some OpenAI models.
    """

    openai_prompt_cache_key: str
    """Used by OpenAI to cache responses for similar requests to optimize your cache hit rates.

    See the [OpenAI Prompt Caching documentation](https://platform.openai.com/docs/guides/prompt-caching#how-it-works) for more information.
    """

    openai_prompt_cache_retention: Literal['in_memory', '24h']
    """The retention policy for the prompt cache. Set to 24h to enable extended prompt caching, which keeps cached prefixes active for longer, up to a maximum of 24 hours.

    See the [OpenAI Prompt Caching documentation](https://platform.openai.com/docs/guides/prompt-caching#how-it-works) for more information.
    """

    openai_continuous_usage_stats: bool
    """When True, enables continuous usage statistics in streaming responses.

    When enabled, the API returns cumulative usage data with each chunk rather than only at the end.
    This setting correctly handles the cumulative nature of these stats by using only the final
    usage values rather than summing all intermediate values.

    See [OpenAI's streaming documentation](https://platform.openai.com/docs/api-reference/chat/create#stream_options) for more information.
    """

```

---|---
####  openai_reasoning_effort `instance-attribute`
```
openai_reasoning_effort: ReasoningEffort

```

Constrains effort on reasoning for
Currently supported values are `low`, `medium`, and `high`. Reducing reasoning effort can result in faster responses and fewer tokens used on reasoning in a response.
####  openai_logprobs `instance-attribute`
```
openai_logprobs:

```

Include log probabilities in the response.
For Chat models, these will be included in `ModelResponse.provider_details['logprobs']`. For Responses models, these will be included in the response output parts `TextPart.provider_details['logprobs']`.
####  openai_top_logprobs `instance-attribute`
```
openai_top_logprobs:

```

Include log probabilities of the top n tokens in the response.
####  openai_store `instance-attribute`
```
openai_store:  | None

```

Whether or not to store the output of this request in OpenAI's systems.
If `False`, OpenAI will not store the request for its own internal review or training. See
####  openai_user `instance-attribute`
```
openai_user:

```

A unique identifier representing the end-user, which can help OpenAI monitor and detect abuse.
See
####  openai_service_tier `instance-attribute`
```
openai_service_tier: [
    "auto", "default", "flex", "priority"
]

```

The service tier to use for the model request.
Currently supported values are `auto`, `default`, `flex`, and `priority`. For more information, see
####  openai_prediction `instance-attribute`
```
openai_prediction: ChatCompletionPredictionContentParam

```

Enables
This feature is currently only supported for some OpenAI models.
####  openai_prompt_cache_key `instance-attribute`
```
openai_prompt_cache_key:

```

Used by OpenAI to cache responses for similar requests to optimize your cache hit rates.
See the
####  openai_prompt_cache_retention `instance-attribute`
```
openai_prompt_cache_retention: ['in_memory', '24h']

```

The retention policy for the prompt cache. Set to 24h to enable extended prompt caching, which keeps cached prefixes active for longer, up to a maximum of 24 hours.
See the
####  openai_continuous_usage_stats `instance-attribute`
```
openai_continuous_usage_stats:

```

When True, enables continuous usage statistics in streaming responses.
When enabled, the API returns cumulative usage data with each chunk rather than only at the end. This setting correctly handles the cumulative nature of these stats by using only the final usage values rather than summing all intermediate values.
See
###  OpenAIModelSettings `deprecated`
Bases: `OpenAIChatModelSettings[](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIChatModelSettings "OpenAIChatModelSettings \(pydantic_ai.models.openai.OpenAIChatModelSettings\)")`
Deprecated
Use `OpenAIChatModelSettings` instead.
Deprecated alias for `OpenAIChatModelSettings`.
Source code in `pydantic_ai_slim/pydantic_ai/models/openai.py`
```
372
373
374
```
| ```
@deprecated('Use `OpenAIChatModelSettings` instead.')
class OpenAIModelSettings(OpenAIChatModelSettings, total=False):
    """Deprecated alias for `OpenAIChatModelSettings`."""

```

---|---
###  OpenAIResponsesModelSettings
Bases: `OpenAIChatModelSettings[](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIChatModelSettings "OpenAIChatModelSettings \(pydantic_ai.models.openai.OpenAIChatModelSettings\)")`
Settings used for an OpenAI Responses model request.
ALL FIELDS MUST BE `openai_` PREFIXED SO YOU CAN MERGE THEM WITH OTHER MODELS.
Source code in `pydantic_ai_slim/pydantic_ai/models/openai.py`
```
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
```
| ```
class OpenAIResponsesModelSettings(OpenAIChatModelSettings, total=False):
    """Settings used for an OpenAI Responses model request.

    ALL FIELDS MUST BE `openai_` PREFIXED SO YOU CAN MERGE THEM WITH OTHER MODELS.
    """

    openai_builtin_tools: Sequence[FileSearchToolParam | WebSearchToolParam | ComputerToolParam]
    """The provided OpenAI built-in tools to use.

    See [OpenAI's built-in tools](https://platform.openai.com/docs/guides/tools?api-mode=responses) for more details.
    """

    openai_reasoning_generate_summary: Literal['detailed', 'concise']
    """Deprecated alias for `openai_reasoning_summary`."""

    openai_reasoning_summary: Literal['detailed', 'concise', 'auto']
    """A summary of the reasoning performed by the model.

    This can be useful for debugging and understanding the model's reasoning process.
    One of `concise`, `detailed`, or `auto`.

    Check the [OpenAI Reasoning documentation](https://platform.openai.com/docs/guides/reasoning?api-mode=responses#reasoning-summaries)
    for more details.
    """

    openai_send_reasoning_ids: bool
    """Whether to send the unique IDs of reasoning, text, and function call parts from the message history to the model. Enabled by default for reasoning models.

    This can result in errors like `"Item 'rs_123' of type 'reasoning' was provided without its required following item."`
    if the message history you're sending does not match exactly what was received from the Responses API in a previous response,
    for example if you're using a [history processor](../../message-history.md#processing-message-history).
    In that case, you'll want to disable this.
    """

    openai_truncation: Literal['disabled', 'auto']
    """The truncation strategy to use for the model response.

    It can be either:
    - `disabled` (default): If a model response will exceed the context window size for a model, the
        request will fail with a 400 error.
    - `auto`: If the context of this response and previous ones exceeds the model's context window size,
        the model will truncate the response to fit the context window by dropping input items in the
        middle of the conversation.
    """

    openai_text_verbosity: Literal['low', 'medium', 'high']
    """Constrains the verbosity of the model's text response.

    Lower values will result in more concise responses, while higher values will
    result in more verbose responses. Currently supported values are `low`,
    `medium`, and `high`.
    """

    openai_previous_response_id: Literal['auto'] | str
    """The ID of a previous response from the model to use as the starting point for a continued conversation.

    When set to `'auto'`, the request automatically uses the most recent
    `provider_response_id` from the message history and omits earlier messages.

    This enables the model to use server-side conversation state and faithfully reference previous reasoning.
    See the [OpenAI Responses API documentation](https://platform.openai.com/docs/guides/reasoning#keeping-reasoning-items-in-context)
    for more information.
    """

    openai_include_code_execution_outputs: bool
    """Whether to include the code execution results in the response.

    Corresponds to the `code_interpreter_call.outputs` value of the `include` parameter in the Responses API.
    """

    openai_include_web_search_sources: bool
    """Whether to include the web search results in the response.

    Corresponds to the `web_search_call.action.sources` value of the `include` parameter in the Responses API.
    """

    openai_include_file_search_results: bool
    """Whether to include the file search results in the response.

    Corresponds to the `file_search_call.results` value of the `include` parameter in the Responses API.
    """

    openai_include_raw_annotations: bool
    """Whether to include the raw annotations in `TextPart.provider_details`.

    When enabled, any annotations (e.g., citations from web search) will be available
    in the `provider_details['annotations']` field of text parts.
    This is opt-in since there may be overlap with native annotation support once
    added via https://github.com/pydantic/pydantic-ai/issues/3126.
    """

```

---|---
####  openai_builtin_tools `instance-attribute`
```
openai_builtin_tools: [
    FileSearchToolParam
    | WebSearchToolParam
    | ComputerToolParam
]

```

The provided OpenAI built-in tools to use.
See
####  openai_reasoning_generate_summary `instance-attribute`
```
openai_reasoning_generate_summary: [
    "detailed", "concise"
]

```

Deprecated alias for `openai_reasoning_summary`.
####  openai_reasoning_summary `instance-attribute`
```
openai_reasoning_summary: [
    "detailed", "concise", "auto"
]

```

A summary of the reasoning performed by the model.
This can be useful for debugging and understanding the model's reasoning process. One of `concise`, `detailed`, or `auto`.
Check the
####  openai_send_reasoning_ids `instance-attribute`
```
openai_send_reasoning_ids:

```

Whether to send the unique IDs of reasoning, text, and function call parts from the message history to the model. Enabled by default for reasoning models.
This can result in errors like `"Item 'rs_123' of type 'reasoning' was provided without its required following item."` if the message history you're sending does not match exactly what was received from the Responses API in a previous response, for example if you're using a [history processor](https://ai.pydantic.dev/message-history/#processing-message-history). In that case, you'll want to disable this.
####  openai_truncation `instance-attribute`
```
openai_truncation: ['disabled', 'auto']

```

The truncation strategy to use for the model response.
It can be either: - `disabled` (default): If a model response will exceed the context window size for a model, the request will fail with a 400 error. - `auto`: If the context of this response and previous ones exceeds the model's context window size, the model will truncate the response to fit the context window by dropping input items in the middle of the conversation.
####  openai_text_verbosity `instance-attribute`
```
openai_text_verbosity: ['low', 'medium', 'high']

```

Constrains the verbosity of the model's text response.
Lower values will result in more concise responses, while higher values will result in more verbose responses. Currently supported values are `low`, `medium`, and `high`.
####  openai_previous_response_id `instance-attribute`
```
openai_previous_response_id: ['auto'] |

```

The ID of a previous response from the model to use as the starting point for a continued conversation.
When set to `'auto'`, the request automatically uses the most recent `provider_response_id` from the message history and omits earlier messages.
This enables the model to use server-side conversation state and faithfully reference previous reasoning. See the
####  openai_include_code_execution_outputs `instance-attribute`
```
openai_include_code_execution_outputs:

```

Whether to include the code execution results in the response.
Corresponds to the `code_interpreter_call.outputs` value of the `include` parameter in the Responses API.
####  openai_include_web_search_sources `instance-attribute`
```
openai_include_web_search_sources:

```

Whether to include the web search results in the response.
Corresponds to the `web_search_call.action.sources` value of the `include` parameter in the Responses API.
####  openai_include_file_search_results `instance-attribute`
```
openai_include_file_search_results:

```

Whether to include the file search results in the response.
Corresponds to the `file_search_call.results` value of the `include` parameter in the Responses API.
####  openai_include_raw_annotations `instance-attribute`
```
openai_include_raw_annotations:

```

Whether to include the raw annotations in `TextPart.provider_details`.
When enabled, any annotations (e.g., citations from web search) will be available in the `provider_details['annotations']` field of text parts. This is opt-in since there may be overlap with native annotation support once added via https://github.com/pydantic/pydantic-ai/issues/3126.
###  OpenAIChatModel `dataclass`
Bases: `Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)")`
A model that uses the OpenAI API.
Internally, this uses the
Apart from `__init__`, all methods are private or match those of the base class.
Source code in `pydantic_ai_slim/pydantic_ai/models/openai.py`
```
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
1312
1313
1314
1315
1316
1317
1318
1319
1320
```
| ```
@dataclass(init=False)
class OpenAIChatModel(Model):
    """A model that uses the OpenAI API.

    Internally, this uses the [OpenAI Python client](https://github.com/openai/openai-python) to interact with the API.

    Apart from `__init__`, all methods are private or match those of the base class.
    """

    client: AsyncOpenAI = field(repr=False)

    _model_name: OpenAIModelName = field(repr=False)
    _provider: Provider[AsyncOpenAI] = field(repr=False)

    @overload
    def __init__(
        self,
        model_name: OpenAIModelName,
        *,
        provider: OpenAIChatCompatibleProvider
        | Literal[
            'openai',
            'openai-chat',
            'gateway',
        ]
        | Provider[AsyncOpenAI] = 'openai',
        profile: ModelProfileSpec | None = None,
        settings: ModelSettings | None = None,
    ) -> None: ...

    @deprecated('Set the `system_prompt_role` in the `OpenAIModelProfile` instead.')
    @overload
    def __init__(
        self,
        model_name: OpenAIModelName,
        *,
        provider: OpenAIChatCompatibleProvider
        | Literal[
            'openai',
            'openai-chat',
            'gateway',
        ]
        | Provider[AsyncOpenAI] = 'openai',
        profile: ModelProfileSpec | None = None,
        system_prompt_role: OpenAISystemPromptRole | None = None,
        settings: ModelSettings | None = None,
    ) -> None: ...

    def __init__(
        self,
        model_name: OpenAIModelName,
        *,
        provider: OpenAIChatCompatibleProvider
        | Literal[
            'openai',
            'openai-chat',
            'gateway',
        ]
        | Provider[AsyncOpenAI] = 'openai',
        profile: ModelProfileSpec | None = None,
        system_prompt_role: OpenAISystemPromptRole | None = None,
        settings: ModelSettings | None = None,
    ):
        """Initialize an OpenAI model.

        Args:
            model_name: The name of the OpenAI model to use. List of model names available
                [here](https://github.com/openai/openai-python/blob/v1.54.3/src/openai/types/chat_model.py#L7)
                (Unfortunately, despite being ask to do so, OpenAI do not provide `.inv` files for their API).
            provider: The provider to use. Defaults to `'openai'`.
            profile: The model profile to use. Defaults to a profile picked by the provider based on the model name.
            system_prompt_role: The role to use for the system prompt message. If not provided, defaults to `'system'`.
                In the future, this may be inferred from the model name.
            settings: Default model settings for this model instance.
        """
        self._model_name = model_name

        if isinstance(provider, str):
            provider = infer_provider('gateway/openai' if provider == 'gateway' else provider)
        self._provider = provider
        self.client = provider.client

        super().__init__(settings=settings, profile=profile or provider.model_profile)

        if system_prompt_role is not None:
            self.profile = OpenAIModelProfile(openai_system_prompt_role=system_prompt_role).update(self.profile)

    @property
    def base_url(self) -> str:
        return str(self.client.base_url)

    @property
    def model_name(self) -> OpenAIModelName:
        """The model name."""
        return self._model_name

    @property
    def system(self) -> str:
        """The model provider."""
        return self._provider.name

    @classmethod
    def supported_builtin_tools(cls) -> frozenset[type[AbstractBuiltinTool]]:
        """Return the set of builtin tool types this model can handle."""
        return frozenset({WebSearchTool})

    @cached_property
    def profile(self) -> ModelProfile:
        """The model profile.

        WebSearchTool is only supported if openai_chat_supports_web_search is True.
        """
