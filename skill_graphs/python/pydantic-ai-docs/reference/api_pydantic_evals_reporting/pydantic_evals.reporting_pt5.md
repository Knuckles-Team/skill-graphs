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

```

---|---
####  build_aggregate_row
```
build_aggregate_row(
    aggregate: ReportCaseAggregate[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportCaseAggregate "ReportCaseAggregate \(pydantic_evals.reporting.ReportCaseAggregate\)"),
) -> []

```

Build a table row for an aggregated case.
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
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
```
| ```
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

```

---|---
####  build_diff_row
```
build_diff_row(
    new_case: ReportCase[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportCase "ReportCase



      dataclass
   \(pydantic_evals.reporting.ReportCase\)"), baseline: ReportCase[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportCase "ReportCase



      dataclass
   \(pydantic_evals.reporting.ReportCase\)")
) -> []

```

Build a table row for a given case ID.
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
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
```
| ```
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

```

---|---
####  build_diff_aggregate_row
```
build_diff_aggregate_row(
    new: ReportCaseAggregate[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportCaseAggregate "ReportCaseAggregate \(pydantic_evals.reporting.ReportCaseAggregate\)"), baseline: ReportCaseAggregate[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportCaseAggregate "ReportCaseAggregate \(pydantic_evals.reporting.ReportCaseAggregate\)")
) -> []

```

Build a table row for a given case ID.
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
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
```
| ```
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

```

---|---
####  build_failure_row
```
build_failure_row(case: ReportCaseFailure[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.ReportCaseFailure "ReportCaseFailure



      dataclass
   \(pydantic_evals.reporting.ReportCaseFailure\)")) -> []

```

Build a table row for a single case failure.
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
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
```
| ```
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

```

---|---
###  EvaluationRenderer `dataclass`
A class for rendering an EvalReport or the diff between two EvalReports.
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
1354
1355
1356
1357
1358
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
1563
1564
1565
1566
1567
1568
1569
1570
1571
1572
1573
1574
1575
1576
1577
1578
1579
1580
1581
1582
1583
1584
1585
1586
1587
1588
1589
1590
1591
1592
1593
1594
1595
1596
1597
1598
1599
1600
1601
1602
1603
1604
1605
1606
1607
1608
1609
1610
```
| ```
@dataclass(kw_only=True)
class EvaluationRenderer:
    """A class for rendering an EvalReport or the diff between two EvalReports."""

    # Columns to include
    include_input: bool
    include_metadata: bool
    include_expected_output: bool
    include_output: bool
    include_durations: bool
    include_total_duration: bool

    # Rows to include
    include_removed_cases: bool
    include_averages: bool

    input_config: RenderValueConfig
    metadata_config: RenderValueConfig
    output_config: RenderValueConfig
    score_configs: dict[str, RenderNumberConfig]
    label_configs: dict[str, RenderValueConfig]
    metric_configs: dict[str, RenderNumberConfig]
    duration_config: RenderNumberConfig

    # Data to include
    include_reasons: bool  # only applies to reports, not to diffs

    include_error_message: bool
    include_error_stacktrace: bool
    include_evaluator_failures: bool

    def include_scores(self, report: EvaluationReport, baseline: EvaluationReport | None = None):
        return any(case.scores for case in self._all_cases(report, baseline))

    def include_labels(self, report: EvaluationReport, baseline: EvaluationReport | None = None):
        return any(case.labels for case in self._all_cases(report, baseline))

    def include_metrics(self, report: EvaluationReport, baseline: EvaluationReport | None = None):
        return any(case.metrics for case in self._all_cases(report, baseline))

    def include_assertions(self, report: EvaluationReport, baseline: EvaluationReport | None = None):
        return any(case.assertions for case in self._all_cases(report, baseline))

    def include_evaluator_failures_column(self, report: EvaluationReport, baseline: EvaluationReport | None = None):
        return self.include_evaluator_failures and any(
            case.evaluator_failures for case in self._all_cases(report, baseline)
        )

    def _all_cases(self, report: EvaluationReport, baseline: EvaluationReport | None) -> list[ReportCase]:
        if not baseline:
            return report.cases
        else:
            return report.cases + self._baseline_cases_to_include(report, baseline)

    def _baseline_cases_to_include(self, report: EvaluationReport, baseline: EvaluationReport) -> list[ReportCase]:
        if self.include_removed_cases:
            return baseline.cases
        report_case_names = {case.name for case in report.cases}
        return [case for case in baseline.cases if case.name in report_case_names]

    def _get_case_renderer(
        self, report: EvaluationReport, baseline: EvaluationReport | None = None
    ) -> ReportCaseRenderer:
        input_renderer = _ValueRenderer.from_config(self.input_config)
        metadata_renderer = _ValueRenderer.from_config(self.metadata_config)
        output_renderer = _ValueRenderer.from_config(self.output_config)
        score_renderers = self._infer_score_renderers(report, baseline)
        label_renderers = self._infer_label_renderers(report, baseline)
        metric_renderers = self._infer_metric_renderers(report, baseline)
        duration_renderer = _NumberRenderer.infer_from_config(
            self.duration_config, 'duration', [x.task_duration for x in self._all_cases(report, baseline)]
        )

        return ReportCaseRenderer(
            include_input=self.include_input,
            include_metadata=self.include_metadata,
            include_expected_output=self.include_expected_output,
            include_output=self.include_output,
            include_scores=self.include_scores(report, baseline),
            include_labels=self.include_labels(report, baseline),
            include_metrics=self.include_metrics(report, baseline),
            include_assertions=self.include_assertions(report, baseline),
            include_reasons=self.include_reasons,
            include_durations=self.include_durations,
            include_total_duration=self.include_total_duration,
            include_error_message=self.include_error_message,
            include_error_stacktrace=self.include_error_stacktrace,
            include_evaluator_failures=self.include_evaluator_failures_column(report, baseline),
            input_renderer=input_renderer,
            metadata_renderer=metadata_renderer,
            output_renderer=output_renderer,
            score_renderers=score_renderers,
            label_renderers=label_renderers,
            metric_renderers=metric_renderers,
            duration_renderer=duration_renderer,
        )

    # TODO(DavidM): in v2, change the return type here to RenderableType
    def build_table(self, report: EvaluationReport, *, with_title: bool = True) -> Table:
        """Build a table for the report.

        Args:
            report: The evaluation report to render
            with_title: Whether to include the title in the table (default True)

        Returns:
            A Rich Table object
        """
        case_renderer = self._get_case_renderer(report)

        title = f'Evaluation Summary: {report.name}' if with_title else ''
        table = case_renderer.build_base_table(title)

        for case in report.cases:
            table.add_row(*case_renderer.build_row(case))

        if self.include_averages:  # pragma: no branch
            average = report.averages()
            if average:  # pragma: no branch
                table.add_row(*case_renderer.build_aggregate_row(average))

        return table

    # TODO(DavidM): in v2, change the return type here to RenderableType
    def build_diff_table(
        self, report: EvaluationReport, baseline: EvaluationReport, *, with_title: bool = True
    ) -> Table:
        """Build a diff table comparing report to baseline.

        Args:
            report: The evaluation report to compare
            baseline: The baseline report to compare against
            with_title: Whether to include the title in the table (default True)

        Returns:
            A Rich Table object
        """
        report_cases = report.cases
        baseline_cases = self._baseline_cases_to_include(report, baseline)

        report_cases_by_id = {case.name: case for case in report_cases}
        baseline_cases_by_id = {case.name: case for case in baseline_cases}

        diff_cases: list[tuple[ReportCase, ReportCase]] = []
        removed_cases: list[ReportCase] = []
        added_cases: list[ReportCase] = []

        for case_id in sorted(set(baseline_cases_by_id.keys()) | set(report_cases_by_id.keys())):
            maybe_baseline_case = baseline_cases_by_id.get(case_id)
            maybe_report_case = report_cases_by_id.get(case_id)
            if maybe_baseline_case and maybe_report_case:
                diff_cases.append((maybe_baseline_case, maybe_report_case))
            elif maybe_baseline_case:
                removed_cases.append(maybe_baseline_case)
            elif maybe_report_case:
                added_cases.append(maybe_report_case)
            else:  # pragma: no cover
                assert False, 'This should be unreachable'

        case_renderer = self._get_case_renderer(report, baseline)
        diff_name = baseline.name if baseline.name == report.name else f'{baseline.name} → {report.name}'

        title = f'Evaluation Diff: {diff_name}' if with_title else ''
        table = case_renderer.build_base_table(title)

        for baseline_case, new_case in diff_cases:
            table.add_row(*case_renderer.build_diff_row(new_case, baseline_case))
        for case in added_cases:
            row = case_renderer.build_row(case)
            row[0] = f'[green]+ Added Case[/]\n{row[0]}'
            table.add_row(*row)
        for case in removed_cases:
            row = case_renderer.build_row(case)
            row[0] = f'[red]- Removed Case[/]\n{row[0]}'
            table.add_row(*row)

        if self.include_averages:  # pragma: no branch
            # Use flat averaging for both sides to keep the diff symmetric.
            # baseline_cases is already filtered to only cases matching the report.
            # Note: for multi-run reports, this differs from build_table which uses two-level
            # aggregation via report.averages(). In practice the results are identical when all
            # runs succeed (equal group sizes), and only diverge with partial failures within a
            # group — a rare edge case. We can revisit if users report confusing behavior.
            report_average = ReportCaseAggregate.average(report_cases) if report_cases else None
            baseline_average = ReportCaseAggregate.average(baseline_cases) if baseline_cases else None
            if report_average and baseline_average:  # pragma: no branch
                table.add_row(*case_renderer.build_diff_aggregate_row(report_average, baseline_average))

        return table

    # TODO(DavidM): in v2, change the return type here to RenderableType
    def build_failures_table(self, report: EvaluationReport) -> Table:
        case_renderer = self._get_case_renderer(report)
        table = case_renderer.build_failures_table('Case Failures')
        for case in report.failures:
            table.add_row(*case_renderer.build_failure_row(case))

        return table

    def _infer_score_renderers(
        self, report: EvaluationReport, baseline: EvaluationReport | None
    ) -> dict[str, _NumberRenderer]:
        all_cases = self._all_cases(report, baseline)

        values_by_name: dict[str, list[float | int]] = {}
        for case in all_cases:
            for k, score in case.scores.items():
                values_by_name.setdefault(k, []).append(score.value)

        all_renderers: dict[str, _NumberRenderer] = {}
        for name, values in values_by_name.items():
            merged_config = _DEFAULT_NUMBER_CONFIG.copy()
            merged_config.update(self.score_configs.get(name, {}))
            all_renderers[name] = _NumberRenderer.infer_from_config(merged_config, 'score', values)
        return all_renderers

    def _infer_label_renderers(
        self, report: EvaluationReport, baseline: EvaluationReport | None
    ) -> dict[str, _ValueRenderer]:
        all_cases = self._all_cases(report, baseline)
        all_names: set[str] = set()
        for case in all_cases:
            for k in case.labels:
                all_names.add(k)

        all_renderers: dict[str, _ValueRenderer] = {}
        for name in all_names:
            merged_config = _DEFAULT_VALUE_CONFIG.copy()
            merged_config.update(self.label_configs.get(name, {}))
            all_renderers[name] = _ValueRenderer.from_config(merged_config)
        return all_renderers

    def _infer_metric_renderers(
        self, report: EvaluationReport, baseline: EvaluationReport | None
    ) -> dict[str, _NumberRenderer]:
        all_cases = self._all_cases(report, baseline)

        values_by_name: dict[str, list[float | int]] = {}
        for case in all_cases:
            for k, v in case.metrics.items():
                values_by_name.setdefault(k, []).append(v)

        all_renderers: dict[str, _NumberRenderer] = {}
        for name, values in values_by_name.items():
            merged_config = _DEFAULT_NUMBER_CONFIG.copy()
            merged_config.update(self.metric_configs.get(name, {}))
            all_renderers[name] = _NumberRenderer.infer_from_config(merged_config, 'metric', values)
        return all_renderers

    def _infer_duration_renderer(
        self, report: EvaluationReport, baseline: EvaluationReport | None
    ) -> _NumberRenderer:  # pragma: no cover
        all_cases = self._all_cases(report, baseline)
        all_durations = [x.task_duration for x in all_cases]
        if self.include_total_duration:
            all_durations += [x.total_duration for x in all_cases]
        return _NumberRenderer.infer_from_config(self.duration_config, 'duration', all_durations)

```

---|---
####  build_table
```
build_table(
    report: EvaluationReport[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.EvaluationReport "EvaluationReport



      dataclass
   \(pydantic_evals.reporting.EvaluationReport\)"), *, with_title:  = True
) ->

```

Build a table for the report.
Parameters:
Name | Type | Description | Default
---|---|---|---
`report` |  `EvaluationReport[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.EvaluationReport "EvaluationReport



      dataclass
   \(pydantic_evals.reporting.EvaluationReport\)")` |  The evaluation report to render |  _required_
`with_title` |  |  Whether to include the title in the table (default True) |  `True`
Returns:
Type | Description
---|---
|  A Rich Table object
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
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
```
| ```
def build_table(self, report: EvaluationReport, *, with_title: bool = True) -> Table:
    """Build a table for the report.

    Args:
        report: The evaluation report to render
        with_title: Whether to include the title in the table (default True)

    Returns:
        A Rich Table object
    """
    case_renderer = self._get_case_renderer(report)

    title = f'Evaluation Summary: {report.name}' if with_title else ''
    table = case_renderer.build_base_table(title)

    for case in report.cases:
        table.add_row(*case_renderer.build_row(case))

    if self.include_averages:  # pragma: no branch
        average = report.averages()
        if average:  # pragma: no branch
            table.add_row(*case_renderer.build_aggregate_row(average))

    return table

```

---|---
####  build_diff_table
```
build_diff_table(
    report: EvaluationReport[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.EvaluationReport "EvaluationReport
