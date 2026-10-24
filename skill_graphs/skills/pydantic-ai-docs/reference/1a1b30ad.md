
    If not provided, use 1e-6.
    """
    diff_rtol: float
    """The relative tolerance for considering a difference "significant".

    See the description of `diff_atol` for more details about what makes a difference "significant".

    If not provided, use 0.001 if all values are ints, otherwise 0.05.
    """
    diff_increase_style: str
    """The style to apply to diffed values that have a significant increase.

    See the description of `diff_atol` for more details about what makes a difference "significant".

    If not provided, use green for scores and red for metrics. You can also use arbitrary `rich` styles, such as "bold red".
    """
    diff_decrease_style: str
    """The style to apply to diffed values that have significant decrease.

    See the description of `diff_atol` for more details about what makes a difference "significant".

    If not provided, use red for scores and green for metrics. You can also use arbitrary `rich` styles, such as "bold red".
    """

```

---|---
####  value_formatter `instance-attribute`
```
value_formatter:  | [[ | ], ]

```

The logic to use for formatting values.
  * If not provided, format as ints if all values are ints, otherwise at least one decimal place and at least four significant figures.
  * You can also use a custom string format spec, e.g. '{:.3f}'
  * You can also use a custom function, e.g. lambda x: f'{x:.3f}'


####  diff_formatter `instance-attribute`
```
diff_formatter: (

    | [[ | ,  | ],  | None]
    | None
)

```

The logic to use for formatting details about the diff.
The strings produced by the value_formatter will always be included in the reports, but the diff_formatter is used to produce additional text about the difference between the old and new values, such as the absolute or relative difference.
  * If not provided, format as ints if all values are ints, otherwise at least one decimal place and at least four significant figures, and will include the percentage change.
  * You can also use a custom string format spec, e.g. '{:+.3f}'
  * You can also use a custom function, e.g. lambda x: f'{x:+.3f}'. If this function returns None, no extra diff text will be added.
  * You can also use None to never generate extra diff text.


####  diff_atol `instance-attribute`
```
diff_atol:

```

The absolute tolerance for considering a difference "significant".
A difference is "significant" if `abs(new - old) < self.diff_atol + self.diff_rtol * abs(old)`.
If a difference is not significant, it will not have the diff styles applied. Note that we still show both the rendered before and after values in the diff any time they differ, even if the difference is not significant. (If the rendered values are exactly the same, we only show the value once.)
If not provided, use 1e-6.
####  diff_rtol `instance-attribute`
```
diff_rtol:

```

The relative tolerance for considering a difference "significant".
See the description of `diff_atol` for more details about what makes a difference "significant".
If not provided, use 0.001 if all values are ints, otherwise 0.05.
####  diff_increase_style `instance-attribute`
```
diff_increase_style:

```

The style to apply to diffed values that have a significant increase.
See the description of `diff_atol` for more details about what makes a difference "significant".
If not provided, use green for scores and red for metrics. You can also use arbitrary `rich` styles, such as "bold red".
####  diff_decrease_style `instance-attribute`
```
diff_decrease_style:

```

The style to apply to diffed values that have significant decrease.
See the description of `diff_atol` for more details about what makes a difference "significant".
If not provided, use red for scores and green for metrics. You can also use arbitrary `rich` styles, such as "bold red".
###  ReportCaseRenderer `dataclass`
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
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
```
| ```
@dataclass(kw_only=True)
class ReportCaseRenderer:
    include_input: bool
    include_metadata: bool
    include_expected_output: bool
    include_output: bool
    include_scores: bool
    include_labels: bool
    include_metrics: bool
    include_assertions: bool
    include_reasons: bool
    include_durations: bool
    include_total_duration: bool
    include_error_message: bool
    include_error_stacktrace: bool
    include_evaluator_failures: bool

    input_renderer: _ValueRenderer
    metadata_renderer: _ValueRenderer
    output_renderer: _ValueRenderer
    score_renderers: Mapping[str, _NumberRenderer]
    label_renderers: Mapping[str, _ValueRenderer]
    metric_renderers: Mapping[str, _NumberRenderer]
    duration_renderer: _NumberRenderer

    # TODO(DavidM): in v2, change the return type here to RenderableType
    def build_base_table(self, title: str) -> Table:
        """Build and return a Rich Table for the diff output."""
        table = Table(title=title, show_lines=True)
        table.add_column('Case ID', style='bold')
        if self.include_input:
            table.add_column('Inputs', overflow='fold')
        if self.include_metadata:
            table.add_column('Metadata', overflow='fold')
        if self.include_expected_output:
            table.add_column('Expected Output', overflow='fold')
        if self.include_output:
            table.add_column('Outputs', overflow='fold')
        if self.include_scores:
            table.add_column('Scores', overflow='fold')
        if self.include_labels:
            table.add_column('Labels', overflow='fold')
        if self.include_metrics:
            table.add_column('Metrics', overflow='fold')
        if self.include_assertions:
            table.add_column('Assertions', overflow='fold')
        if self.include_evaluator_failures:
            table.add_column('Evaluator Failures', overflow='fold')
        if self.include_durations:
            table.add_column('Durations' if self.include_total_duration else 'Duration', justify='right')
        return table

    # TODO(DavidM): in v2, change the return type here to RenderableType
    def build_failures_table(self, title: str) -> Table:
        """Build and return a Rich Table for the failures output."""
        table = Table(title=title, show_lines=True)
        table.add_column('Case ID', style='bold')
        if self.include_input:
            table.add_column('Inputs', overflow='fold')
        if self.include_metadata:
            table.add_column('Metadata', overflow='fold')
        if self.include_expected_output:
            table.add_column('Expected Output', overflow='fold')
        if self.include_error_message:
            table.add_column('Error Message', overflow='fold')
        if self.include_error_stacktrace:
            table.add_column('Error Stacktrace', overflow='fold')
        return table

    def build_row(self, case: ReportCase) -> list[str]:
        """Build a table row for a single case."""
        row = [case.name]

        if self.include_input:
            row.append(self.input_renderer.render_value(None, case.inputs) or EMPTY_CELL_STR)

        if self.include_metadata:
            row.append(self.metadata_renderer.render_value(None, case.metadata) or EMPTY_CELL_STR)

        if self.include_expected_output:
            row.append(self.output_renderer.render_value(None, case.expected_output) or EMPTY_CELL_STR)

        if self.include_output:
            row.append(self.output_renderer.render_value(None, case.output) or EMPTY_CELL_STR)

        if self.include_scores:
            row.append(self._render_dict({k: v for k, v in case.scores.items()}, self.score_renderers))

        if self.include_labels:
            row.append(self._render_dict({k: v for k, v in case.labels.items()}, self.label_renderers))

        if self.include_metrics:
            row.append(self._render_dict(case.metrics, self.metric_renderers))

        if self.include_assertions:
            row.append(self._render_assertions(list(case.assertions.values())))

        if self.include_evaluator_failures:
            row.append(self._render_evaluator_failures(case.evaluator_failures))

        if self.include_durations:
            row.append(self._render_durations(case))

        return row

    def build_aggregate_row(self, aggregate: ReportCaseAggregate) -> list[str]:
        """Build a table row for an aggregated case."""
        row = [f'[b i]{aggregate.name}[/]']

        if self.include_input:
            row.append(EMPTY_AGGREGATE_CELL_STR)

        if self.include_metadata:
            row.append(EMPTY_AGGREGATE_CELL_STR)

        if self.include_expected_output:
            row.append(EMPTY_AGGREGATE_CELL_STR)

        if self.include_output:
            row.append(EMPTY_AGGREGATE_CELL_STR)

        if self.include_scores:
            row.append(self._render_dict(aggregate.scores, self.score_renderers))

        if self.include_labels:
            row.append(self._render_dict(aggregate.labels, self.label_renderers))

        if self.include_metrics:
            row.append(self._render_dict(aggregate.metrics, self.metric_renderers))

        if self.include_assertions:
            row.append(self._render_aggregate_assertions(aggregate.assertions))

        if self.include_evaluator_failures:
            row.append(EMPTY_AGGREGATE_CELL_STR)

        if self.include_durations:
            row.append(self._render_durations(aggregate))

        return row

    def build_diff_row(
        self,
        new_case: ReportCase,
        baseline: ReportCase,
    ) -> list[str]:
        """Build a table row for a given case ID."""
        assert baseline.name == new_case.name, 'This should only be called for matching case IDs'
        row = [baseline.name]

        if self.include_input:  # pragma: no branch
            input_diff = self.input_renderer.render_diff(None, baseline.inputs, new_case.inputs) or EMPTY_CELL_STR
            row.append(input_diff)

        if self.include_metadata:  # pragma: no branch
            metadata_diff = (
                self.metadata_renderer.render_diff(None, baseline.metadata, new_case.metadata) or EMPTY_CELL_STR
            )
            row.append(metadata_diff)

        if self.include_expected_output:  # pragma: no branch
            expected_output_diff = (
                self.output_renderer.render_diff(None, baseline.expected_output, new_case.expected_output)
                or EMPTY_CELL_STR
            )
            row.append(expected_output_diff)

        if self.include_output:  # pragma: no branch
            output_diff = self.output_renderer.render_diff(None, baseline.output, new_case.output) or EMPTY_CELL_STR
            row.append(output_diff)

        if self.include_scores:  # pragma: no branch
            scores_diff = self._render_dicts_diff(
                {k: v.value for k, v in baseline.scores.items()},
                {k: v.value for k, v in new_case.scores.items()},
                self.score_renderers,
            )
            row.append(scores_diff)

        if self.include_labels:  # pragma: no branch
            labels_diff = self._render_dicts_diff(
                {k: v.value for k, v in baseline.labels.items()},
                {k: v.value for k, v in new_case.labels.items()},
                self.label_renderers,
            )
            row.append(labels_diff)

        if self.include_metrics:  # pragma: no branch
            metrics_diff = self._render_dicts_diff(baseline.metrics, new_case.metrics, self.metric_renderers)
            row.append(metrics_diff)

        if self.include_assertions:  # pragma: no branch
            assertions_diff = self._render_assertions_diff(
                list(baseline.assertions.values()), list(new_case.assertions.values())
            )
            row.append(assertions_diff)

        if self.include_evaluator_failures:  # pragma: no branch
            evaluator_failures_diff = self._render_evaluator_failures_diff(
                baseline.evaluator_failures, new_case.evaluator_failures
            )
            row.append(evaluator_failures_diff)

        if self.include_durations:  # pragma: no branch
            durations_diff = self._render_durations_diff(baseline, new_case)
            row.append(durations_diff)

        return row

    def build_diff_aggregate_row(
        self,
        new: ReportCaseAggregate,
        baseline: ReportCaseAggregate,
    ) -> list[str]:
        """Build a table row for a given case ID."""
        assert baseline.name == new.name, 'This should only be called for aggregates with matching names'
        row = [f'[b i]{baseline.name}[/]']

        if self.include_input:  # pragma: no branch
            row.append(EMPTY_AGGREGATE_CELL_STR)

        if self.include_metadata:  # pragma: no branch
            row.append(EMPTY_AGGREGATE_CELL_STR)

        if self.include_expected_output:  # pragma: no branch
            row.append(EMPTY_AGGREGATE_CELL_STR)

        if self.include_output:  # pragma: no branch
            row.append(EMPTY_AGGREGATE_CELL_STR)

        if self.include_scores:  # pragma: no branch
            scores_diff = self._render_dicts_diff(baseline.scores, new.scores, self.score_renderers)
            row.append(scores_diff)

        if self.include_labels:  # pragma: no branch
            labels_diff = self._render_dicts_diff(baseline.labels, new.labels, self.label_renderers)
            row.append(labels_diff)

        if self.include_metrics:  # pragma: no branch
            metrics_diff = self._render_dicts_diff(baseline.metrics, new.metrics, self.metric_renderers)
            row.append(metrics_diff)

        if self.include_assertions:  # pragma: no branch
            assertions_diff = self._render_aggregate_assertions_diff(baseline.assertions, new.assertions)
            row.append(assertions_diff)

        if self.include_evaluator_failures:  # pragma: no branch
            row.append(EMPTY_AGGREGATE_CELL_STR)

        if self.include_durations:  # pragma: no branch
            durations_diff = self._render_durations_diff(baseline, new)
            row.append(durations_diff)

        return row

    def build_failure_row(self, case: ReportCaseFailure) -> list[str]:
        """Build a table row for a single case failure."""
        row = [case.name]

        if self.include_input:
            row.append(self.input_renderer.render_value(None, case.inputs) or EMPTY_CELL_STR)

        if self.include_metadata:
            row.append(self.metadata_renderer.render_value(None, case.metadata) or EMPTY_CELL_STR)

        if self.include_expected_output:
            row.append(self.output_renderer.render_value(None, case.expected_output) or EMPTY_CELL_STR)

        if self.include_error_message:
            row.append(case.error_message or EMPTY_CELL_STR)

        if self.include_error_stacktrace:
            row.append(case.error_stacktrace or EMPTY_CELL_STR)

        return row

    def _render_durations(self, case: ReportCase | ReportCaseAggregate) -> str:
        """Build the diff string for a duration value."""
        case_durations: dict[str, float] = {'task': case.task_duration}
        if self.include_total_duration:
            case_durations['total'] = case.total_duration
        return self._render_dict(
            case_durations,
            {'task': self.duration_renderer, 'total': self.duration_renderer},
            include_names=self.include_total_duration,
        )

    def _render_durations_diff(
        self,
        base_case: ReportCase | ReportCaseAggregate,
        new_case: ReportCase | ReportCaseAggregate,
    ) -> str:
        """Build the diff string for a duration value."""
        base_case_durations: dict[str, float] = {'task': base_case.task_duration}
        new_case_durations: dict[str, float] = {'task': new_case.task_duration}
        if self.include_total_duration:  # pragma: no branch
            base_case_durations['total'] = base_case.total_duration
            new_case_durations['total'] = new_case.total_duration
        return self._render_dicts_diff(
            base_case_durations,
            new_case_durations,
            {'task': self.duration_renderer, 'total': self.duration_renderer},
            include_names=self.include_total_duration,
        )

    @staticmethod
    def _render_dicts_diff(
        baseline_dict: dict[str, T],
        new_dict: dict[str, T],
        renderers: Mapping[str, _AbstractRenderer[T]],
        *,
        include_names: bool = True,
    ) -> str:
        keys: set[str] = set()
        keys.update(baseline_dict.keys())
        keys.update(new_dict.keys())
        diff_lines: list[str] = []
        for key in sorted(keys):
            old_val = baseline_dict.get(key)
            new_val = new_dict.get(key)
            rendered = renderers[key].render_diff(key if include_names else None, old_val, new_val)
            diff_lines.append(rendered)
        return '\n'.join(diff_lines) if diff_lines else EMPTY_CELL_STR

    def _render_dict(
        self,
        case_dict: Mapping[str, EvaluationResult[T] | T],
        renderers: Mapping[str, _AbstractRenderer[T]],
        *,
        include_names: bool = True,
    ) -> str:
        diff_lines: list[str] = []
        for key, val in case_dict.items():
            value = cast(EvaluationResult[T], val).value if isinstance(val, EvaluationResult) else val
            rendered = renderers[key].render_value(key if include_names else None, value)
            if self.include_reasons and isinstance(val, EvaluationResult) and (reason := val.reason):
                rendered += f'\n  Reason: {reason}\n'
            diff_lines.append(rendered)
        return '\n'.join(diff_lines) if diff_lines else EMPTY_CELL_STR

    def _render_assertions(
        self,
        assertions: list[EvaluationResult[bool]],
    ) -> str:
        if not assertions:
            return EMPTY_CELL_STR
        lines: list[str] = []
        for a in assertions:
            line = '[green]✔[/]' if a.value else '[red]✗[/]'
            if self.include_reasons:
                line = f'{a.name}: {line}\n'
                line = f'{line}  Reason: {a.reason}\n\n' if a.reason else line
            lines.append(line)
        return ''.join(lines)

    @staticmethod
    def _render_aggregate_assertions(
        assertions: float | None,
    ) -> str:
        return (
            default_render_percentage(assertions) + ' [green]✔[/]'
            if assertions is not None
            else EMPTY_AGGREGATE_CELL_STR
        )

    @staticmethod
    def _render_assertions_diff(
        assertions: list[EvaluationResult[bool]], new_assertions: list[EvaluationResult[bool]]
    ) -> str:
        if not assertions and not new_assertions:  # pragma: no cover
            return EMPTY_CELL_STR

        old = ''.join(['[green]✔[/]' if a.value else '[red]✗[/]' for a in assertions])
        new = ''.join(['[green]✔[/]' if a.value else '[red]✗[/]' for a in new_assertions])
        return old if old == new else f'{old} → {new}'

    @staticmethod
    def _render_aggregate_assertions_diff(
        baseline: float | None,
        new: float | None,
    ) -> str:
        if baseline is None and new is None:  # pragma: no cover
            return EMPTY_AGGREGATE_CELL_STR
        rendered_baseline = (
            default_render_percentage(baseline) + ' [green]✔[/]' if baseline is not None else EMPTY_CELL_STR
        )
        rendered_new = default_render_percentage(new) + ' [green]✔[/]' if new is not None else EMPTY_CELL_STR
        return rendered_new if rendered_baseline == rendered_new else f'{rendered_baseline} → {rendered_new}'

    def _render_evaluator_failures(
        self,
        failures: list[EvaluatorFailure],
    ) -> str:
        if not failures:
            return EMPTY_CELL_STR  # pragma: no cover
        lines: list[str] = []
        for failure in failures:
            line = f'[red]{failure.name}[/]'
            if failure.error_message:
                line += f': {failure.error_message}'
            lines.append(line)
        return '\n'.join(lines)

    def _render_evaluator_failures_diff(
        self,
        baseline_failures: list[EvaluatorFailure],
        new_failures: list[EvaluatorFailure],
    ) -> str:
        baseline_str = self._render_evaluator_failures(baseline_failures)
        new_str = self._render_evaluator_failures(new_failures)
        if baseline_str == new_str:
            return baseline_str  # pragma: no cover
        return f'{baseline_str}\n→\n{new_str}'

```

---|---
####  build_base_table
```
build_base_table(title: ) ->

```

Build and return a Rich Table for the diff output.
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
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
```
| ```
def build_base_table(self, title: str) -> Table:
    """Build and return a Rich Table for the diff output."""
    table = Table(title=title, show_lines=True)
    table.add_column('Case ID', style='bold')
    if self.include_input:
        table.add_column('Inputs', overflow='fold')
    if self.include_metadata:
        table.add_column('Metadata', overflow='fold')
    if self.include_expected_output:
        table.add_column('Expected Output', overflow='fold')
    if self.include_output:
        table.add_column('Outputs', overflow='fold')
    if self.include_scores:
        table.add_column('Scores', overflow='fold')
    if self.include_labels:
        table.add_column('Labels', overflow='fold')
    if self.include_metrics:
        table.add_column('Metrics', overflow='fold')
    if self.include_assertions:
        table.add_column('Assertions', overflow='fold')
    if self.include_evaluator_failures:
        table.add_column('Evaluator Failures', overflow='fold')
    if self.include_durations:
        table.add_column('Durations' if self.include_total_duration else 'Duration', justify='right')
    return table

```

---|---
####  build_failures_table
```
build_failures_table(title: ) ->

```

Build and return a Rich Table for the failures output.
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
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
```
| ```
def build_failures_table(self, title: str) -> Table:
    """Build and return a Rich Table for the failures output."""
    table = Table(title=title, show_lines=True)
    table.add_column('Case ID', style='bold')
    if self.include_input:
        table.add_column('Inputs', overflow='fold')
    if self.include_metadata:
        table.add_column('Metadata', overflow='fold')
    if self.include_expected_output:
        table.add_column('Expected Output', overflow='fold')
    if self.include_error_message:
        table.add_column('Error Message', overflow='fold')
    if self.include_error_stacktrace:
        table.add_column('Error Stacktrace', overflow='fold')
    return table

```

---|---
####  build_row
```
build_row(case: ReportCase[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportCase "ReportCase



      dataclass
   \(pydantic_evals.reporting.ReportCase\)")) -> []

```

Build a table row for a single case.
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
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
```
| ```
def build_row(self, case: ReportCase) -> list[str]:
