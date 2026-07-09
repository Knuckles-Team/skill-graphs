                if raw_finish_reason := event.delta.stop_reason:  # pragma: no branch
                    self.provider_details = self.provider_details or {}
                    self.provider_details['finish_reason'] = raw_finish_reason
                    self.finish_reason = _FINISH_REASON_MAP.get(raw_finish_reason)

            elif isinstance(event, BetaRawContentBlockStopEvent):  # pragma: no branch
                if isinstance(current_block, BetaMCPToolUseBlock):
                    maybe_event = self._parts_manager.handle_tool_call_delta(
                        vendor_part_id=event.index,
                        args='}',
                    )
                    if maybe_event is not None:  # pragma: no branch
                        yield maybe_event
                current_block = None
            elif isinstance(event, BetaRawMessageStopEvent):  # pragma: no branch
                current_block = None

    @property
    def model_name(self) -> AnthropicModelName:
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
model_name: AnthropicModelName[](https://ai.pydantic.dev/api/models/anthropic/#pydantic_ai.models.anthropic.AnthropicModelName "AnthropicModelName



      module-attribute
   \(pydantic_ai.models.anthropic.AnthropicModelName\)")

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
