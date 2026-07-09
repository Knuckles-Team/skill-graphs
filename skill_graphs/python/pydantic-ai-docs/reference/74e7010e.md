                    _annotations_by_item.setdefault(chunk.item_id, []).append(chunk.annotation)

            elif isinstance(chunk, responses.ResponseTextDeltaEvent):
                for event in self._parts_manager.handle_text_delta(
                    vendor_part_id=chunk.item_id,
                    content=chunk.delta,
                    id=chunk.item_id,
                    provider_name=self.provider_name,
                ):
                    yield event

            elif isinstance(chunk, responses.ResponseTextDoneEvent):
                # Add annotations to provider_details if available
                provider_details: dict[str, Any] = {}
                annotations = _annotations_by_item.get(chunk.item_id)
                if annotations:
                    provider_details['annotations'] = responses_output_text_annotations_ta.dump_python(
                        list(annotations), warnings=False
                    )

                if provider_details:
                    for event in self._parts_manager.handle_text_delta(
                        vendor_part_id=chunk.item_id,
                        content='',
                        provider_name=self.provider_name,
                        provider_details=provider_details,
                    ):
                        yield event

            elif isinstance(chunk, responses.ResponseRefusalDeltaEvent):
                # Accumulate refusal text from deltas as a fallback in case the done event is missing.
                self._has_refusal = True
                self.finish_reason = 'content_filter'
                self._refusal_text += chunk.delta

            elif isinstance(chunk, responses.ResponseRefusalDoneEvent):
                # The done event contains the full refusal text, replacing any accumulated deltas.
                self._has_refusal = True
                self.finish_reason = 'content_filter'
                self._refusal_text = chunk.refusal

            elif isinstance(chunk, responses.ResponseWebSearchCallInProgressEvent):
                pass  # there's nothing we need to do here

            elif isinstance(chunk, responses.ResponseWebSearchCallSearchingEvent):
                pass  # there's nothing we need to do here

            elif isinstance(chunk, responses.ResponseWebSearchCallCompletedEvent):
                pass  # there's nothing we need to do here

            elif isinstance(chunk, responses.ResponseAudioDeltaEvent):  # pragma: lax no cover
                pass  # there's nothing we need to do here

            elif isinstance(chunk, responses.ResponseCodeInterpreterCallCodeDeltaEvent):
                json_args_delta = to_json(chunk.delta).decode()[1:-1]  # Drop the surrounding `"`
                maybe_event = self._parts_manager.handle_tool_call_delta(
                    vendor_part_id=f'{chunk.item_id}-call',
                    args=json_args_delta,
                )
                if maybe_event is not None:  # pragma: no branch
                    yield maybe_event

            elif isinstance(chunk, responses.ResponseCodeInterpreterCallCodeDoneEvent):
                maybe_event = self._parts_manager.handle_tool_call_delta(
                    vendor_part_id=f'{chunk.item_id}-call',
                    args='"}',
                )
                if maybe_event is not None:  # pragma: no branch
                    yield maybe_event

            elif isinstance(chunk, responses.ResponseCodeInterpreterCallCompletedEvent):
                pass  # there's nothing we need to do here

            elif isinstance(chunk, responses.ResponseCodeInterpreterCallInProgressEvent):
                pass  # there's nothing we need to do here

            elif isinstance(chunk, responses.ResponseCodeInterpreterCallInterpretingEvent):
                pass  # there's nothing we need to do here

            elif isinstance(chunk, responses.ResponseImageGenCallCompletedEvent):  # pragma: no cover
                pass  # there's nothing we need to do here

            elif isinstance(chunk, responses.ResponseImageGenCallGeneratingEvent):
                pass  # there's nothing we need to do here

            elif isinstance(chunk, responses.ResponseImageGenCallInProgressEvent):
                pass  # there's nothing we need to do here

            elif isinstance(chunk, responses.ResponseImageGenCallPartialImageEvent):
                # Not present on the type, but present on the actual object.
                # See https://github.com/openai/openai-python/issues/2649
                output_format = getattr(chunk, 'output_format', 'png')
                file_part = FilePart(
                    content=BinaryImage(
                        data=base64.b64decode(chunk.partial_image_b64),
                        media_type=f'image/{output_format}',
                    ),
                    id=chunk.item_id,
                )
                yield self._parts_manager.handle_part(vendor_part_id=f'{chunk.item_id}-file', part=file_part)

            elif isinstance(chunk, responses.ResponseMcpCallArgumentsDoneEvent):
                maybe_event = self._parts_manager.handle_tool_call_delta(
                    vendor_part_id=f'{chunk.item_id}-call',
                    args='}',
                )
                if maybe_event is not None:  # pragma: no branch
                    yield maybe_event

            elif isinstance(chunk, responses.ResponseMcpCallArgumentsDeltaEvent):
                maybe_event = self._parts_manager.handle_tool_call_delta(
                    vendor_part_id=f'{chunk.item_id}-call',
                    args=chunk.delta,
                )
                if maybe_event is not None:  # pragma: no branch
                    yield maybe_event

            elif isinstance(chunk, responses.ResponseMcpListToolsInProgressEvent):
                pass  # there's nothing we need to do here

            elif isinstance(chunk, responses.ResponseMcpListToolsCompletedEvent):
                pass  # there's nothing we need to do here

            elif isinstance(chunk, responses.ResponseMcpListToolsFailedEvent):  # pragma: no cover
                pass  # there's nothing we need to do here

            elif isinstance(chunk, responses.ResponseMcpCallInProgressEvent):
                pass  # there's nothing we need to do here

            elif isinstance(chunk, responses.ResponseMcpCallFailedEvent):  # pragma: no cover
                pass  # there's nothing we need to do here

            elif isinstance(chunk, responses.ResponseMcpCallCompletedEvent):
                pass  # there's nothing we need to do here

            elif isinstance(chunk, responses.ResponseFileSearchCallCompletedEvent):
                pass  # there's nothing we need to do here

            elif isinstance(chunk, responses.ResponseFileSearchCallSearchingEvent):
                pass  # there's nothing we need to do here

            elif isinstance(chunk, responses.ResponseFileSearchCallInProgressEvent):
                pass  # there's nothing we need to do here

            else:  # pragma: no cover
                warnings.warn(
                    f'Handling of this event type is not yet implemented. Please report on our GitHub: {chunk}',
                    UserWarning,
                )

        if self._refusal_text:
            self.provider_details = {**(self.provider_details or {}), 'refusal': self._refusal_text}

    def _map_usage(self, response: responses.Response) -> usage.RequestUsage:
        return _map_usage(response, self._provider_name, self._provider_url, self.model_name)

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
© Pydantic Services Inc. 2024 to present
