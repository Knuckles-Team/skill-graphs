                            ):
                                yield event
                        else:
                            for event in self._parts_manager.handle_text_delta(
                                vendor_part_id=None,
                                content=part.text,
                                provider_name=self.provider_name if provider_details else None,
                                provider_details=provider_details,
                            ):
                                yield event
                    elif part.function_call:
                        maybe_event = self._parts_manager.handle_tool_call_delta(
                            vendor_part_id=uuid4(),
                            tool_name=part.function_call.name,
                            args=part.function_call.args,
                            tool_call_id=part.function_call.id,
                            provider_name=self.provider_name if provider_details else None,
                            provider_details=provider_details,
                        )
                        if maybe_event is not None:  # pragma: no branch
                            yield maybe_event
                    elif part.inline_data is not None:
                        if part.thought:  # pragma: no cover
                            # Per https://ai.google.dev/gemini-api/docs/image-generation#thinking-process:
                            # > The model generates up to two interim images to test composition and logic. The last image within Thinking is also the final rendered image.
                            # We currently don't expose these image thoughts as they can't be represented with `ThinkingPart`
                            continue
                        data = part.inline_data.data
                        mime_type = part.inline_data.mime_type
                        assert data and mime_type, 'Inline data must have data and mime type'
                        content = BinaryContent(data=data, media_type=mime_type)
                        yield self._parts_manager.handle_part(
                            vendor_part_id=uuid4(),
                            part=FilePart(
                                content=BinaryContent.narrow_type(content),
                                provider_name=self.provider_name if provider_details else None,
                                provider_details=provider_details,
                            ),
                        )
                    elif part.executable_code is not None:
                        part_obj = self._handle_executable_code_streaming(part.executable_code)
                        part_obj.provider_details = provider_details
                        yield self._parts_manager.handle_part(vendor_part_id=uuid4(), part=part_obj)
                    elif part.code_execution_result is not None:
                        part = self._map_code_execution_result(part.code_execution_result)
                        part.provider_details = provider_details
                        yield self._parts_manager.handle_part(vendor_part_id=uuid4(), part=part)
                    else:
                        assert part.function_response is not None, f'Unexpected part: {part}'  # pragma: no cover

                # Grounding metadata is attached to the final text chunk, so
                # we emit the `BuiltinToolReturnPart` after the text delta so
                # that the delta is properly added to the same `TextPart` as earlier chunks
                file_search_part = self._handle_file_search_grounding_metadata_streaming(candidate.grounding_metadata)
                if file_search_part is not None:
                    yield self._parts_manager.handle_part(vendor_part_id=uuid4(), part=file_search_part)
        except errors.APIError as e:
            if (status_code := e.code) >= 400:
                raise ModelHTTPError(
                    status_code=status_code,
                    model_name=self._model_name,
                    body=cast(Any, e.details),  # pyright: ignore[reportUnknownMemberType]
                ) from e
            raise ModelAPIError(model_name=self._model_name, message=str(e)) from e

    def _handle_file_search_grounding_metadata_streaming(
        self, grounding_metadata: GroundingMetadata | None
    ) -> BuiltinToolReturnPart | None:
        """Handle file search grounding metadata for streaming responses.

        Returns a BuiltinToolReturnPart if file search results are available in the grounding metadata.
        """
        if not self._file_search_tool_call_id or not grounding_metadata:
            return None

        grounding_chunks = grounding_metadata.grounding_chunks
        retrieved_contexts = _extract_file_search_retrieved_contexts(grounding_chunks)
        if retrieved_contexts:  # pragma: no branch
            part = BuiltinToolReturnPart(
                provider_name=self.provider_name,
                tool_name=FileSearchTool.kind,
                tool_call_id=self._file_search_tool_call_id,
                content=retrieved_contexts,
            )
            self._file_search_tool_call_id = None
            return part
        return None  # pragma: no cover

    def _map_code_execution_result(self, code_execution_result: CodeExecutionResult) -> BuiltinToolReturnPart:
        """Map code execution result to a BuiltinToolReturnPart using instance state."""
        assert self._code_execution_tool_call_id is not None
        return _map_code_execution_result(code_execution_result, self.provider_name, self._code_execution_tool_call_id)

    def _handle_executable_code_streaming(self, executable_code: ExecutableCode) -> ModelResponsePart:
        """Handle executable code for streaming responses.

        Returns a BuiltinToolCallPart for file search or code execution.
        Sets self._code_execution_tool_call_id or self._file_search_tool_call_id as appropriate.
        """
        code = executable_code.code
        has_file_search_tool = any(
            isinstance(tool, FileSearchTool) for tool in self.model_request_parameters.builtin_tools
        )

        if code and has_file_search_tool and (file_search_query := self._extract_file_search_query(code)):
            self._file_search_tool_call_id = _utils.generate_tool_call_id()
            return BuiltinToolCallPart(
                provider_name=self.provider_name,
                tool_name=FileSearchTool.kind,
                tool_call_id=self._file_search_tool_call_id,
                args={'query': file_search_query},
            )

        self._code_execution_tool_call_id = _utils.generate_tool_call_id()
        return _map_executable_code(executable_code, self.provider_name, self._code_execution_tool_call_id)

    def _extract_file_search_query(self, code: str) -> str | None:
        """Extract the query from file_search.query() executable code.

        Handles escaped quotes in the query string.

        Example: 'print(file_search.query(query="what is the capital of France?"))'
        Returns: 'what is the capital of France?'
        """
        match = _FILE_SEARCH_QUERY_PATTERN.search(code)
        if match:
            query = match.group(2)
            query = query.replace('\\\\', '\\').replace('\\"', '"').replace("\\'", "'")
            return query
        return None  # pragma: no cover

    @property
    def model_name(self) -> GoogleModelName:
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
model_name: GoogleModelName[](https://ai.pydantic.dev/api/models/google/#pydantic_ai.models.google.GoogleModelName "GoogleModelName



      module-attribute
   \(pydantic_ai.models.google.GoogleModelName\)")

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
