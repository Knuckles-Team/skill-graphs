```
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
```
| ```
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

```

---|---
####  new_messages_json
```
new_messages_json(
    *, output_tool_return_content:  | None = None
) ->

```

Return new messages from [`new_messages`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResultSync.new_messages "new_messages") as JSON bytes.
Parameters:
Name | Type | Description | Default
---|---|---|---
`output_tool_return_content` |  |  The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the output tool call if you want to continue the conversation and want to set the response to the output tool call. If `None`, the last message will not be modified. |  `None`
Returns:
Type | Description
---|---
|  JSON bytes representing the new messages.
Source code in `pydantic_ai_slim/pydantic_ai/result.py`
```
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
```
| ```
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

```

---|---
####  stream_output
```
stream_output(
    *, debounce_by:  | None = 0.1
) -> [OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]

```

Stream the output as an iterable.
The pydantic validator for structured data will be called in [partial mode](https://docs.pydantic.dev/dev/concepts/experimental/#partial-validation) on each iteration.
Parameters:
Name | Type | Description | Default
---|---|---|---
`debounce_by` |  |  by how much (if at all) to debounce/group the output chunks by. `None` means no debouncing. Debouncing is particularly important for long structured outputs to reduce the overhead of performing validation as each token is received. |  `0.1`
Returns:
Type | Description
---|---
`OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")]` |  An iterable of the response data.
Source code in `pydantic_ai_slim/pydantic_ai/result.py`
```
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
```
| ```
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

```

---|---
####  stream_text
```
stream_text(
    *, delta:  = False, debounce_by:  | None = 0.1
) -> []

```

Stream the text result as an iterable.
Note
Result validators will NOT be called on the text result if `delta=True`.
Parameters:
Name | Type | Description | Default
---|---|---|---
`delta` |  |  if `True`, yield each chunk of text as it is received, if `False` (default), yield the full text up to the current point. |  `False`
`debounce_by` |  |  by how much (if at all) to debounce/group the response chunks by. `None` means no debouncing. Debouncing is particularly important for long structured responses to reduce the overhead of performing validation as each token is received. |  `0.1`
Source code in `pydantic_ai_slim/pydantic_ai/result.py`
```
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
```
| ```
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

```

---|---
####  stream_responses
```
stream_responses(
    *, debounce_by:  | None = 0.1
) -> [[ModelResponse[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "ModelResponse



      dataclass
   \(pydantic_ai.messages.ModelResponse\)"), ]]

```

Stream the response as an iterable of Structured LLM Messages.
Parameters:
Name | Type | Description | Default
---|---|---|---
`debounce_by` |  |  by how much (if at all) to debounce/group the response chunks by. `None` means no debouncing. Debouncing is particularly important for long structured responses to reduce the overhead of performing validation as each token is received. |  `0.1`
Returns:
Type | Description
---|---
`ModelResponse[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "ModelResponse



      dataclass
   \(pydantic_ai.messages.ModelResponse\)"), ` |  An iterable of the structured response message and whether that is the last message.
Source code in `pydantic_ai_slim/pydantic_ai/result.py`
```
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
```
| ```
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

```

---|---
####  get_output
```
get_output() -> OutputDataT[](https://ai.pydantic.dev/api/output/#pydantic_ai.output.OutputDataT "OutputDataT



      module-attribute
   \(pydantic_ai.output.OutputDataT\)")

```

Stream the whole response, validate and return it.
Source code in `pydantic_ai_slim/pydantic_ai/result.py`
```
736
737
738
```
| ```
def get_output(self) -> OutputDataT:
    """Stream the whole response, validate and return it."""
    return _utils.get_event_loop().run_until_complete(self._streamed_run_result.get_output())

```

---|---
####  response `property`
```
response: ModelResponse[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "ModelResponse



      dataclass
   \(pydantic_ai.messages.ModelResponse\)")

```

Return the current state of the response.
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
745
746
747
748
749
750
751
```
| ```
def usage(self) -> RunUsage:
    """Return the usage of the whole run.

    !!! note
        This won't return the full usage until the stream is finished.
    """
    return self._streamed_run_result.usage()

```

---|---
####  timestamp
```
timestamp() ->

```

Get the timestamp of the response.
Source code in `pydantic_ai_slim/pydantic_ai/result.py`
```
753
754
755
```
| ```
def timestamp(self) -> datetime:
    """Get the timestamp of the response."""
    return self._streamed_run_result.timestamp()

```

---|---
####  run_id `property`
```
run_id:

```

The unique identifier for the agent run.
####  metadata `property`
```
metadata: [, ] | None

```

Metadata associated with this agent run, if configured.
####  validate_response_output
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
767
768
769
770
771
```
| ```
def validate_response_output(self, message: _messages.ModelResponse, *, allow_partial: bool = False) -> OutputDataT:
    """Validate a structured result message."""
    return _utils.get_event_loop().run_until_complete(
        self._streamed_run_result.validate_response_output(message, allow_partial=allow_partial)
    )

```

---|---
####  is_complete `property`
```
is_complete:

```

Whether the stream has all been received.
This is set to `True` when one of [`stream_output`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResultSync.stream_output "stream_output"), [`stream_text`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResultSync.stream_text "stream_text"), [`stream_responses`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResultSync.stream_responses "stream_responses") or [`get_output`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResultSync.get_output "get_output") completes.
© Pydantic Services Inc. 2024 to present
