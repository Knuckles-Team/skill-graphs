Source code in `pydantic_ai_slim/pydantic_ai/result.py`
```
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
```
| ```
async def stream_output(self, *, debounce_by: float | None = 0.1) -> AsyncIterator[OutputDataT]:
    """Stream the output as an async iterable.

    The pydantic validator for structured data will be called in
    [partial mode](https://docs.pydantic.dev/dev/concepts/experimental/#partial-validation)
    on each iteration.

    Args:
        debounce_by: by how much (if at all) to debounce/group the output chunks by. `None` means no debouncing.
            Debouncing is particularly important for long structured outputs to reduce the overhead of
            performing validation as each token is received.

    Returns:
        An async iterable of the response data.
    """
    if self._run_result is not None:
        yield self._run_result.output
        await self._marked_completed()
    elif self._stream_response is not None:
        async for output in self._stream_response.stream_output(debounce_by=debounce_by):
            yield output
        await self._marked_completed(self.response)
    else:
        raise ValueError('No stream response or run result provided')  # pragma: no cover

```

---|---
####  stream_text `async`
```
stream_text(
    *, delta:  = False, debounce_by:  | None = 0.1
) -> []

```

Stream the text result as an async iterable.
Note
Result validators will NOT be called on the text result if `delta=True`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`delta` |  |  if `True`, yield each chunk of text as it is received, if `False` (default), yield the full text up to the current point. |  `False`
`debounce_by` |  |  by how much (if at all) to debounce/group the response chunks by. `None` means no debouncing. Debouncing is particularly important for long structured responses to reduce the overhead of performing validation as each token is received. |  `0.1`
Source code in `pydantic_ai_slim/pydantic_ai/result.py`
```
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
```
| ```
async def stream_text(self, *, delta: bool = False, debounce_by: float | None = 0.1) -> AsyncIterator[str]:
    """Stream the text result as an async iterable.

    !!! note
        Result validators will NOT be called on the text result if `delta=True`.

    Args:
        delta: if `True`, yield each chunk of text as it is received, if `False` (default), yield the full text
            up to the current point.
        debounce_by: by how much (if at all) to debounce/group the response chunks by. `None` means no debouncing.
            Debouncing is particularly important for long structured responses to reduce the overhead of
            performing validation as each token is received.
    """
    if self._run_result is not None:  # pragma: no cover
        # We can't really get here, as `_run_result` is only set in `run_stream` when `CallToolsNode` produces `DeferredToolRequests` output
        # as a result of a tool function raising `CallDeferred` or `ApprovalRequired`.
        # That'll change if we ever support something like `raise EndRun(output: OutputT)` where `OutputT` could be `str`.
        if not isinstance(self._run_result.output, str):
            raise exceptions.UserError('stream_text() can only be used with text responses')
        yield self._run_result.output
        await self._marked_completed()
    elif self._stream_response is not None:
        async for text in self._stream_response.stream_text(delta=delta, debounce_by=debounce_by):
            yield text
        await self._marked_completed(self.response)
    else:
        raise ValueError('No stream response or run result provided')  # pragma: no cover

```

---|---
####  stream_structured `async` `deprecated`
```
stream_structured(
    *, debounce_by:  | None = 0.1
) -> [[ModelResponse[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "ModelResponse



      dataclass
   \(pydantic_ai.messages.ModelResponse\)"), ]]

```

Deprecated
`StreamedRunResult.stream_structured` is deprecated, use `stream_responses` instead.
Source code in `pydantic_ai_slim/pydantic_ai/result.py`
```
493
494
495
496
497
498
```
| ```
@deprecated('`StreamedRunResult.stream_structured` is deprecated, use `stream_responses` instead.')
async def stream_structured(
    self, *, debounce_by: float | None = 0.1
) -> AsyncIterator[tuple[_messages.ModelResponse, bool]]:
    async for msg, last in self.stream_responses(debounce_by=debounce_by):
        yield msg, last

```

---|---
####  stream_responses `async`
```
stream_responses(
    *, debounce_by:  | None = 0.1
) -> [[ModelResponse[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "ModelResponse



      dataclass
   \(pydantic_ai.messages.ModelResponse\)"), ]]

```

Stream the response as an async iterable of Structured LLM Messages.
Parameters:
Name | Type | Description | Default
---|---|---|---
`debounce_by` |  |  by how much (if at all) to debounce/group the response chunks by. `None` means no debouncing. Debouncing is particularly important for long structured responses to reduce the overhead of performing validation as each token is received. |  `0.1`
Returns:
Type | Description
---|---
`ModelResponse[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "ModelResponse



      dataclass
   \(pydantic_ai.messages.ModelResponse\)"), ` |  An async iterable of the structured response message and whether that is the last message.
Source code in `pydantic_ai_slim/pydantic_ai/result.py`
```
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
```
| ```
async def stream_responses(
    self, *, debounce_by: float | None = 0.1
) -> AsyncIterator[tuple[_messages.ModelResponse, bool]]:
    """Stream the response as an async iterable of Structured LLM Messages.

    Args:
        debounce_by: by how much (if at all) to debounce/group the response chunks by. `None` means no debouncing.
            Debouncing is particularly important for long structured responses to reduce the overhead of
            performing validation as each token is received.

    Returns:
        An async iterable of the structured response message and whether that is the last message.
    """
    if self._run_result is not None:
        yield self.response, True
        await self._marked_completed()
    elif self._stream_response is not None:
        # if the message currently has any parts with content, yield before streaming
        async for msg in self._stream_response.stream_responses(debounce_by=debounce_by):
            yield msg, False

        msg = self.response
        yield msg, True

        await self._marked_completed(msg)
    else:
        raise ValueError('No stream response or run result provided')  # pragma: no cover

```

---|---
####  get_output `async`
```
get_output() -> OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")

```

Stream the whole response, validate and return it.
Source code in `pydantic_ai_slim/pydantic_ai/result.py`
```
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
```
| ```
async def get_output(self) -> OutputDataT:
    """Stream the whole response, validate and return it."""
    if self._run_result is not None:
        output = self._run_result.output
        await self._marked_completed()
        return output
    elif self._stream_response is not None:
        output = await self._stream_response.get_output()
        await self._marked_completed(self.response)
        return output
    else:
        raise ValueError('No stream response or run result provided')  # pragma: no cover

```

---|---
####  response `property`
```
response: ModelResponse[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "ModelResponse



      dataclass
   \(pydantic_ai.messages.ModelResponse\)")

```

Return the current state of the response.
####  metadata `property`
```
metadata: [, ] | None

```

Metadata associated with this agent run, if configured.
####  usage
```
usage() -> RunUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RunUsage "RunUsage



      dataclass
   \(pydantic_ai.usage.RunUsage\)")

```

Return the usage of the whole run.
Note
This won't return the full usage until the stream is finished.
Source code in `pydantic_ai_slim/pydantic_ai/result.py`
```
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
```
| ```
def usage(self) -> RunUsage:
    """Return the usage of the whole run.

    !!! note
        This won't return the full usage until the stream is finished.
    """
    if self._run_result is not None:
        return self._run_result.usage()
    elif self._stream_response is not None:
        return self._stream_response.usage()
    else:
        raise ValueError('No stream response or run result provided')  # pragma: no cover

```

---|---
####  timestamp
```
timestamp() ->

```

Get the timestamp of the response.
Source code in `pydantic_ai_slim/pydantic_ai/result.py`
```
576
577
578
579
580
581
582
583
```
| ```
def timestamp(self) -> datetime:
    """Get the timestamp of the response."""
    if self._run_result is not None:
        return self._run_result.timestamp()
    elif self._stream_response is not None:
        return self._stream_response.timestamp()
    else:
        raise ValueError('No stream response or run result provided')  # pragma: no cover

```

---|---
####  run_id `property`
```
run_id:

```

The unique identifier for the agent run.
####  validate_structured_output `async` `deprecated`
```
validate_structured_output(
    message: ModelResponse[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "ModelResponse



      dataclass
   \(pydantic_ai.messages.ModelResponse\)"), *, allow_partial:  = False
) -> OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")

```

Deprecated
`validate_structured_output` is deprecated, use `validate_response_output` instead.
Source code in `pydantic_ai_slim/pydantic_ai/result.py`
```
595
596
597
598
599
```
| ```
@deprecated('`validate_structured_output` is deprecated, use `validate_response_output` instead.')
async def validate_structured_output(
    self, message: _messages.ModelResponse, *, allow_partial: bool = False
) -> OutputDataT:
    return await self.validate_response_output(message, allow_partial=allow_partial)

```

---|---
####  validate_response_output `async`
```
validate_response_output(
    message: ModelResponse[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "ModelResponse



      dataclass
   \(pydantic_ai.messages.ModelResponse\)"), *, allow_partial:  = False
) -> OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")

```

Validate a structured result message.
Source code in `pydantic_ai_slim/pydantic_ai/result.py`
```
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
```
| ```
async def validate_response_output(
    self, message: _messages.ModelResponse, *, allow_partial: bool = False
) -> OutputDataT:
    """Validate a structured result message."""
    if self._run_result is not None:
        return self._run_result.output
    elif self._stream_response is not None:
        return await self._stream_response.validate_response_output(message, allow_partial=allow_partial)
    else:
        raise ValueError('No stream response or run result provided')  # pragma: no cover

```

---|---
###  StreamedRunResultSync `dataclass`
Bases: `AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)"), OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]`
Synchronous wrapper for [`StreamedRunResult`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResult "StreamedRunResult



      dataclass
  ") that only exposes sync methods.
Source code in `pydantic_ai_slim/pydantic_ai/result.py`
```
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
```
| ```
@dataclass(init=False)
class StreamedRunResultSync(Generic[AgentDepsT, OutputDataT]):
    """Synchronous wrapper for [`StreamedRunResult`][pydantic_ai.result.StreamedRunResult] that only exposes sync methods."""

    _streamed_run_result: StreamedRunResult[AgentDepsT, OutputDataT]

    def __init__(self, streamed_run_result: StreamedRunResult[AgentDepsT, OutputDataT]) -> None:
        self._streamed_run_result = streamed_run_result

    def all_messages(self, *, output_tool_return_content: str | None = None) -> list[_messages.ModelMessage]:
        """Return the history of messages.

        Args:
            output_tool_return_content: The return content of the tool call to set in the last message.
                This provides a convenient way to modify the content of the output tool call if you want to continue
                the conversation and want to set the response to the output tool call. If `None`, the last message will
                not be modified.

        Returns:
            List of messages.
        """
        return self._streamed_run_result.all_messages(output_tool_return_content=output_tool_return_content)

    def all_messages_json(self, *, output_tool_return_content: str | None = None) -> bytes:  # pragma: no cover
        """Return all messages from [`all_messages`][pydantic_ai.result.StreamedRunResultSync.all_messages] as JSON bytes.

        Args:
            output_tool_return_content: The return content of the tool call to set in the last message.
                This provides a convenient way to modify the content of the output tool call if you want to continue
                the conversation and want to set the response to the output tool call. If `None`, the last message will
                not be modified.

        Returns:
            JSON bytes representing the messages.
        """
        return self._streamed_run_result.all_messages_json(output_tool_return_content=output_tool_return_content)

    def new_messages(self, *, output_tool_return_content: str | None = None) -> list[_messages.ModelMessage]:
        """Return new messages associated with this run.

        Messages from older runs are excluded.

        Args:
            output_tool_return_content: The return content of the tool call to set in the last message.
                This provides a convenient way to modify the content of the output tool call if you want to continue
                the conversation and want to set the response to the output tool call. If `None`, the last message will
                not be modified.

        Returns:
            List of new messages.
        """
        return self._streamed_run_result.new_messages(output_tool_return_content=output_tool_return_content)

    def new_messages_json(self, *, output_tool_return_content: str | None = None) -> bytes:  # pragma: no cover
        """Return new messages from [`new_messages`][pydantic_ai.result.StreamedRunResultSync.new_messages] as JSON bytes.

        Args:
            output_tool_return_content: The return content of the tool call to set in the last message.
                This provides a convenient way to modify the content of the output tool call if you want to continue
                the conversation and want to set the response to the output tool call. If `None`, the last message will
                not be modified.

        Returns:
            JSON bytes representing the new messages.
        """
        return self._streamed_run_result.new_messages_json(output_tool_return_content=output_tool_return_content)

    def stream_output(self, *, debounce_by: float | None = 0.1) -> Iterator[OutputDataT]:
        """Stream the output as an iterable.

        The pydantic validator for structured data will be called in
        [partial mode](https://docs.pydantic.dev/dev/concepts/experimental/#partial-validation)
        on each iteration.

        Args:
            debounce_by: by how much (if at all) to debounce/group the output chunks by. `None` means no debouncing.
                Debouncing is particularly important for long structured outputs to reduce the overhead of
                performing validation as each token is received.

        Returns:
            An iterable of the response data.
        """
        return _utils.sync_async_iterator(self._streamed_run_result.stream_output(debounce_by=debounce_by))

    def stream_text(self, *, delta: bool = False, debounce_by: float | None = 0.1) -> Iterator[str]:
        """Stream the text result as an iterable.

        !!! note
            Result validators will NOT be called on the text result if `delta=True`.

        Args:
            delta: if `True`, yield each chunk of text as it is received, if `False` (default), yield the full text
                up to the current point.
            debounce_by: by how much (if at all) to debounce/group the response chunks by. `None` means no debouncing.
                Debouncing is particularly important for long structured responses to reduce the overhead of
                performing validation as each token is received.
        """
        return _utils.sync_async_iterator(self._streamed_run_result.stream_text(delta=delta, debounce_by=debounce_by))

    def stream_responses(self, *, debounce_by: float | None = 0.1) -> Iterator[tuple[_messages.ModelResponse, bool]]:
        """Stream the response as an iterable of Structured LLM Messages.

        Args:
            debounce_by: by how much (if at all) to debounce/group the response chunks by. `None` means no debouncing.
                Debouncing is particularly important for long structured responses to reduce the overhead of
                performing validation as each token is received.

        Returns:
            An iterable of the structured response message and whether that is the last message.
        """
        return _utils.sync_async_iterator(self._streamed_run_result.stream_responses(debounce_by=debounce_by))

    def get_output(self) -> OutputDataT:
        """Stream the whole response, validate and return it."""
        return _utils.get_event_loop().run_until_complete(self._streamed_run_result.get_output())

    @property
    def response(self) -> _messages.ModelResponse:
        """Return the current state of the response."""
        return self._streamed_run_result.response

    def usage(self) -> RunUsage:
        """Return the usage of the whole run.

        !!! note
            This won't return the full usage until the stream is finished.
        """
        return self._streamed_run_result.usage()

    def timestamp(self) -> datetime:
        """Get the timestamp of the response."""
        return self._streamed_run_result.timestamp()

    @property
    def run_id(self) -> str:
        """The unique identifier for the agent run."""
        return self._streamed_run_result.run_id

    @property
    def metadata(self) -> dict[str, Any] | None:
        """Metadata associated with this agent run, if configured."""
        return self._streamed_run_result.metadata

    def validate_response_output(self, message: _messages.ModelResponse, *, allow_partial: bool = False) -> OutputDataT:
        """Validate a structured result message."""
        return _utils.get_event_loop().run_until_complete(
            self._streamed_run_result.validate_response_output(message, allow_partial=allow_partial)
        )

    @property
    def is_complete(self) -> bool:
        """Whether the stream has all been received.

        This is set to `True` when one of
        [`stream_output`][pydantic_ai.result.StreamedRunResultSync.stream_output],
        [`stream_text`][pydantic_ai.result.StreamedRunResultSync.stream_text],
        [`stream_responses`][pydantic_ai.result.StreamedRunResultSync.stream_responses] or
        [`get_output`][pydantic_ai.result.StreamedRunResultSync.get_output] completes.
        """
        return self._streamed_run_result.is_complete

```

---|---
####  all_messages
```
all_messages(
    *, output_tool_return_content:  | None = None
) -> [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")]

```

Return the history of messages.
Parameters:
Name | Type | Description | Default
---|---|---|---
`output_tool_return_content` |  |  The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the output tool call if you want to continue the conversation and want to set the response to the output tool call. If `None`, the last message will not be modified. |  `None`
Returns:
Type | Description
---|---
`ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")]` |  List of messages.
Source code in `pydantic_ai_slim/pydantic_ai/result.py`
```
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
```
| ```
def all_messages(self, *, output_tool_return_content: str | None = None) -> list[_messages.ModelMessage]:
    """Return the history of messages.

    Args:
        output_tool_return_content: The return content of the tool call to set in the last message.
            This provides a convenient way to modify the content of the output tool call if you want to continue
            the conversation and want to set the response to the output tool call. If `None`, the last message will
            not be modified.

    Returns:
        List of messages.
    """
    return self._streamed_run_result.all_messages(output_tool_return_content=output_tool_return_content)

```

---|---
####  all_messages_json
```
all_messages_json(
    *, output_tool_return_content:  | None = None
) ->

```

Return all messages from [`all_messages`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResultSync.all_messages "all_messages") as JSON bytes.
Parameters:
Name | Type | Description | Default
---|---|---|---
`output_tool_return_content` |  |  The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the output tool call if you want to continue the conversation and want to set the response to the output tool call. If `None`, the last message will not be modified. |  `None`
Returns:
Type | Description
---|---
|  JSON bytes representing the messages.
Source code in `pydantic_ai_slim/pydantic_ai/result.py`
```
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
```
| ```
def all_messages_json(self, *, output_tool_return_content: str | None = None) -> bytes:  # pragma: no cover
    """Return all messages from [`all_messages`][pydantic_ai.result.StreamedRunResultSync.all_messages] as JSON bytes.

    Args:
        output_tool_return_content: The return content of the tool call to set in the last message.
            This provides a convenient way to modify the content of the output tool call if you want to continue
            the conversation and want to set the response to the output tool call. If `None`, the last message will
            not be modified.

    Returns:
        JSON bytes representing the messages.
    """
    return self._streamed_run_result.all_messages_json(output_tool_return_content=output_tool_return_content)

```

---|---
####  new_messages
```
new_messages(
    *, output_tool_return_content:  | None = None
) -> [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")]

```

Return new messages associated with this run.
Messages from older runs are excluded.
Parameters:
Name | Type | Description | Default
---|---|---|---
`output_tool_return_content` |  |  The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the output tool call if you want to continue the conversation and want to set the response to the output tool call. If `None`, the last message will not be modified. |  `None`
Returns:
Type | Description
---|---
`ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")]` |  List of new messages.
Source code in `pydantic_ai_slim/pydantic_ai/result.py`
