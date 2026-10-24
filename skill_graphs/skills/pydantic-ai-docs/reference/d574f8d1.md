


      dataclass
   \(pydantic_evals.reporting.EvaluationReport\)"),
    baseline: EvaluationReport[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.EvaluationReport "EvaluationReport



      dataclass
   \(pydantic_evals.reporting.EvaluationReport\)"),
    *,
    with_title:  = True
) ->

```

Build a diff table comparing report to baseline.
Parameters:
Name | Type | Description | Default
---|---|---|---
`report` |  `EvaluationReport[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.EvaluationReport "EvaluationReport



      dataclass
   \(pydantic_evals.reporting.EvaluationReport\)")` |  The evaluation report to compare |  _required_
`baseline` |  `EvaluationReport[](https://ai.pydantic.dev/api/pydantic_evals/reporting/#pydantic_evals.reporting.EvaluationReport "EvaluationReport



      dataclass
   \(pydantic_evals.reporting.EvaluationReport\)")` |  The baseline report to compare against |  _required_
`with_title` |  |  Whether to include the title in the table (default True) |  `True`
Returns:
Type | Description
---|---
|  A Rich Table object
Source code in `pydantic_evals/pydantic_evals/reporting/__init__.py`
```
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
```
| ```
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

```

---|---
© Pydantic Services Inc. 2024 to present
