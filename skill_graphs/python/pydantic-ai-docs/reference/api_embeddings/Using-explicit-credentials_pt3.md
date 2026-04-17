                'type': 'object',
                'properties': {
                    'input_type': {'type': 'string'},
                    'inputs_count': {'type': 'integer'},
                    'embedding_settings': {'type': 'object'},
                    **(
                        {'inputs': {'type': ['array']}, 'embeddings': {'type': 'array'}}
                        if self.instrumentation_settings.include_content
                        else {}
                    ),
                },
            }
        )

        record_metrics: Callable[[], None] | None = None
        try:
            with self.instrumentation_settings.tracer.start_as_current_span(span_name, attributes=attributes) as span:

                def finish(result: EmbeddingResult):
                    # Prepare metric recording closure first so metrics are recorded
                    # even if the span is not recording.
                    provider_name = attributes[GEN_AI_PROVIDER_NAME_ATTRIBUTE]
                    request_model = attributes[GEN_AI_REQUEST_MODEL_ATTRIBUTE]
                    response_model = result.model_name or request_model
                    price_calculation = None

                    def _record_metrics():
                        token_attributes = {
                            GEN_AI_PROVIDER_NAME_ATTRIBUTE: provider_name,
                            'gen_ai.operation.name': operation,
                            GEN_AI_REQUEST_MODEL_ATTRIBUTE: request_model,
                            'gen_ai.response.model': response_model,
                            'gen_ai.token.type': 'input',
                        }
                        tokens = result.usage.input_tokens or 0
                        if tokens:  # pragma: no branch
                            self.instrumentation_settings.tokens_histogram.record(tokens, token_attributes)
                            if price_calculation is not None:
                                self.instrumentation_settings.cost_histogram.record(
                                    float(getattr(price_calculation, 'input_price', 0.0)),
                                    token_attributes,
                                )

                    nonlocal record_metrics
                    record_metrics = _record_metrics

                    if not span.is_recording():
                        return  # pragma: lax no cover

                    attributes_to_set: dict[str, AttributeValue] = {
                        **result.usage.opentelemetry_attributes(),
                        'gen_ai.response.model': response_model,
                    }

                    try:
                        price_calculation = result.cost()
                    except LookupError:
                        # The cost of this provider/model is unknown, which is common.
                        pass
                    except Exception as e:  # pragma: no cover
                        warnings.warn(
                            f'Failed to get cost from response: {type(e).__name__}: {e}', CostCalculationFailedWarning
                        )
                    else:
                        attributes_to_set['operation.cost'] = float(price_calculation.total_price)

                    embeddings = result.embeddings
                    if embeddings:  # pragma: no branch
                        attributes_to_set['gen_ai.embeddings.dimension.count'] = len(embeddings[0])
                        if self.instrumentation_settings.include_content:
                            attributes['embeddings'] = json.dumps(embeddings)

                    if result.provider_response_id is not None:
                        attributes_to_set['gen_ai.response.id'] = result.provider_response_id

                    span.set_attributes(attributes_to_set)

                yield finish
        finally:
            if record_metrics:  # pragma: no branch
                # Record metrics after the span finishes to avoid duplication.
                record_metrics()

    @staticmethod
    def model_attributes(model: EmbeddingModel) -> dict[str, AttributeValue]:
        attributes: dict[str, AttributeValue] = {
            GEN_AI_PROVIDER_NAME_ATTRIBUTE: model.system,
            GEN_AI_REQUEST_MODEL_ATTRIBUTE: model.model_name,
        }
        if base_url := model.base_url:
            try:
                parsed = urlparse(base_url)
            except Exception:  # pragma: no cover
                pass
            else:
                if parsed.hostname:  # pragma: no branch
                    attributes['server.address'] = parsed.hostname
                if parsed.port:
                    attributes['server.port'] = parsed.port  # pragma: no cover

        return attributes

    @staticmethod
    def serialize_any(value: Any) -> str:
        try:
            return ANY_ADAPTER.dump_python(value, mode='json')
        except Exception:  # pragma: no cover
            try:
                return str(value)
            except Exception as e:
                return f'Unable to serialize: {e}'

```

---|---
####  instrumentation_settings `instance-attribute`
```
instrumentation_settings: InstrumentationSettings[](https://ai.pydantic.dev/api/models/instrumented/#pydantic_ai.models.instrumented.InstrumentationSettings "InstrumentationSettings



      dataclass
   \(pydantic_ai.models.instrumented.InstrumentationSettings\)") = (
    options or InstrumentationSettings[](https://ai.pydantic.dev/api/models/instrumented/#pydantic_ai.models.instrumented.InstrumentationSettings "InstrumentationSettings



      dataclass
   \(pydantic_ai.models.instrumented.InstrumentationSettings\)")()
)

```

Instrumentation settings for this model.
© Pydantic Services Inc. 2024 to present
