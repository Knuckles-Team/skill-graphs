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
```
| ```
class Model(ABC):
    """Abstract class for a model."""

    _profile: ModelProfileSpec | None = None
    _settings: ModelSettings | None = None

    def __init__(
        self,
        *,
        settings: ModelSettings | None = None,
        profile: ModelProfileSpec | None = None,
    ) -> None:
        """Initialize the model with optional settings and profile.

        Args:
            settings: Model-specific settings that will be used as defaults for this model.
            profile: The model profile to use.
        """
        self._settings = settings
        self._profile = profile

    @property
    def settings(self) -> ModelSettings | None:
        """Get the model settings."""
        return self._settings

    @abstractmethod
    async def request(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> ModelResponse:
        """Make a request to the model.

        This is ultimately called by `pydantic_ai._agent_graph.ModelRequestNode._make_request(...)`.
        """
        raise NotImplementedError()

    async def count_tokens(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> RequestUsage:
        """Make a request to the model for counting tokens."""
        # This method is not required, but you need to implement it if you want to support `UsageLimits.count_tokens_before_request`.
        raise NotImplementedError(f'Token counting ahead of the request is not supported by {self.__class__.__name__}')

    @asynccontextmanager
    async def request_stream(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
        run_context: RunContext[Any] | None = None,
    ) -> AsyncIterator[StreamedResponse]:
        """Make a request to the model and return a streaming response."""
        # This method is not required, but you need to implement it if you want to support streamed responses
        raise NotImplementedError(f'Streamed requests not supported by this {self.__class__.__name__}')
        # yield is required to make this a generator for type checking
        # noinspection PyUnreachableCode
        yield  # pragma: no cover

    def customize_request_parameters(self, model_request_parameters: ModelRequestParameters) -> ModelRequestParameters:
        """Customize the request parameters for the model.

        This method can be overridden by subclasses to modify the request parameters before sending them to the model.
        In particular, this method can be used to make modifications to the generated tool JSON schemas if necessary
        for vendor/model-specific reasons.
        """
        if transformer := self.profile.json_schema_transformer:
            model_request_parameters = replace(
                model_request_parameters,
                function_tools=[_customize_tool_def(transformer, t) for t in model_request_parameters.function_tools],
                output_tools=[_customize_tool_def(transformer, t) for t in model_request_parameters.output_tools],
            )
            if output_object := model_request_parameters.output_object:
                model_request_parameters = replace(
                    model_request_parameters,
                    output_object=_customize_output_object(transformer, output_object),
                )

        return model_request_parameters

    def prepare_request(
        self,
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> tuple[ModelSettings | None, ModelRequestParameters]:
        """Prepare request inputs before they are passed to the provider.

        This merges the given `model_settings` with the model's own `settings` attribute and ensures
        `customize_request_parameters` is applied to the resolved
        [`ModelRequestParameters`][pydantic_ai.models.ModelRequestParameters]. Subclasses can override this method if
        they need to customize the preparation flow further, but most implementations should simply call
        `self.prepare_request(...)` at the start of their `request` (and related) methods.
        """
        model_settings = merge_model_settings(self.settings, model_settings)

        params = self.customize_request_parameters(model_request_parameters)

        if builtin_tools := params.builtin_tools:
            # Deduplicate builtin tools
            params = replace(
                params,
                builtin_tools=list({tool.unique_id: tool for tool in builtin_tools}.values()),
            )

        if params.output_mode == 'auto':
            output_mode = self.profile.default_structured_output_mode
            params = replace(
                params,
                output_mode=output_mode,
                allow_text_output=output_mode in ('native', 'prompted'),
            )

        # Reset irrelevant fields
        if params.output_tools and params.output_mode != 'tool':
            params = replace(params, output_tools=[])
        if params.output_object and params.output_mode not in ('native', 'prompted'):
            params = replace(params, output_object=None)
        if params.prompted_output_template and params.output_mode not in ('prompted', 'native'):
            params = replace(params, prompted_output_template=None)  # pragma: no cover

        # Set default prompted output template
        if (
            params.output_mode == 'prompted'
            or (params.output_mode == 'native' and self.profile.native_output_requires_schema_in_instructions)
        ) and params.prompted_output_template is None:
            params = replace(params, prompted_output_template=self.profile.prompted_output_template)

        # Check if output mode is supported
        if params.output_mode == 'native' and not self.profile.supports_json_schema_output:
            raise UserError('Native structured output is not supported by this model.')
        if params.output_mode == 'tool' and not self.profile.supports_tools:
            raise UserError('Tool output is not supported by this model.')
        if params.allow_image_output and not self.profile.supports_image_output:
            raise UserError('Image output is not supported by this model.')

        # Check if builtin tools are supported
        if params.builtin_tools:
            supported_types = self.profile.supported_builtin_tools
            unsupported = [tool for tool in params.builtin_tools if not isinstance(tool, tuple(supported_types))]
            if unsupported:
                unsupported_names = [type(tool).__name__ for tool in unsupported]
                supported_names = [t.__name__ for t in supported_types]
                raise UserError(
                    f'Builtin tool(s) {unsupported_names} not supported by this model. Supported: {supported_names}'
                )

        return model_settings, params

    @property
    @abstractmethod
    def model_name(self) -> str:
        """The model name."""
        raise NotImplementedError()

    @property
    def model_id(self) -> str:
        """The fully qualified model name in `'provider:model_name'` format."""
        return f'{self.system}:{self.model_name}'

    @property
    def label(self) -> str:
        """Human-friendly display label for the model.

        Handles common patterns:
        - gpt-5 -> GPT 5
        - claude-sonnet-4-5 -> Claude Sonnet 4.5
        - gemini-2.5-pro -> Gemini 2.5 Pro
        - meta-llama/llama-3-70b -> Llama 3 70b (OpenRouter style)
        """
        label = self.model_name
        # Handle OpenRouter-style names with / (e.g., meta-llama/llama-3-70b)
        if '/' in label:
            label = label.split('/')[-1]

        parts = label.split('-')
        result: list[str] = []

        for i, part in enumerate(parts):
            if i == 0 and part.lower() == 'gpt':
                result.append(part.upper())
            elif part.replace('.', '').isdigit():
                if result and result[-1].replace('.', '').isdigit():
                    result[-1] = f'{result[-1]}.{part}'
                else:
                    result.append(part)
            else:
                result.append(part.capitalize())

        return ' '.join(result)

    @classmethod
    def supported_builtin_tools(cls) -> frozenset[type[AbstractBuiltinTool]]:
        """Return the set of builtin tool types this model class can handle.

        Subclasses should override this to reflect their actual capabilities.
        Default is empty set - subclasses must explicitly declare support.
        """
        return frozenset()

    @cached_property
    def profile(self) -> ModelProfile:
        """The model profile.

        We use this to compute the intersection of the profile's supported_builtin_tools
        and the model's implemented tools, ensuring model.profile.supported_builtin_tools
        is the single source of truth for what builtin tools are actually usable.
        """
        _profile = self._profile
        if callable(_profile):
            _profile = _profile(self.model_name)

        if _profile is None:
            _profile = DEFAULT_PROFILE

        # Compute intersection: profile's allowed tools & model's implemented tools
        model_supported = self.__class__.supported_builtin_tools()
        profile_supported = _profile.supported_builtin_tools
        effective_tools = profile_supported & model_supported

        if effective_tools != profile_supported:
            _profile = replace(_profile, supported_builtin_tools=effective_tools)

        return _profile

    @property
    @abstractmethod
    def system(self) -> str:
        """The model provider, ex: openai.

        Use to populate the `gen_ai.system` OpenTelemetry semantic convention attribute,
        so should use well-known values listed in
        https://opentelemetry.io/docs/specs/semconv/attributes-registry/gen-ai/#gen-ai-system
        when applicable.
        """
        raise NotImplementedError()

    @property
    def base_url(self) -> str | None:
        """The base URL for the provider API, if available."""
        return None

    @staticmethod
    def _get_instructions(
        messages: Sequence[ModelMessage], model_request_parameters: ModelRequestParameters | None = None
    ) -> str | None:
        """Get instructions from the first ModelRequest found when iterating messages in reverse.

        In the case that a "mock" request was generated to include a tool-return part for a result tool,
        we want to use the instructions from the second-to-most-recent request (which should correspond to the
        original request that generated the response that resulted in the tool-return part).
        """
        instructions = None

        last_two_requests: list[ModelRequest] = []
        for message in reversed(messages):
            if isinstance(message, ModelRequest):
                last_two_requests.append(message)
                if len(last_two_requests) == 2:
                    break
                if message.instructions is not None:
                    instructions = message.instructions
                    break

        # If we don't have two requests, and we didn't already return instructions, there are definitely not any:
        if instructions is None and len(last_two_requests) == 2:
            most_recent_request = last_two_requests[0]
            second_most_recent_request = last_two_requests[1]

            # If we've gotten this far and the most recent request consists of only tool-return parts or retry-prompt parts,
            # we use the instructions from the second-to-most-recent request. This is necessary because when handling
            # result tools, we generate a "mock" ModelRequest with a tool-return part for it, and that ModelRequest will not
            # have the relevant instructions from the agent.

            # While it's possible that you could have a message history where the most recent request has only tool returns,
            # I believe there is no way to achieve that would _change_ the instructions without manually crafting the most
            # recent message. That might make sense in principle for some usage pattern, but it's enough of an edge case
            # that I think it's not worth worrying about, since you can work around this by inserting another ModelRequest
            # with no parts at all immediately before the request that has the tool calls (that works because we only look
            # at the two most recent ModelRequests here).

            # If you have a use case where this causes pain, please open a GitHub issue and we can discuss alternatives.

            if all(p.part_kind == 'tool-return' or p.part_kind == 'retry-prompt' for p in most_recent_request.parts):
                instructions = second_most_recent_request.instructions

        if model_request_parameters and (output_instructions := model_request_parameters.prompted_output_instructions):
            if instructions:
                instructions = '\n\n'.join([instructions, output_instructions])
            else:
                instructions = output_instructions

        return instructions

```

---|---
####  __init__
```
__init__(
    *,
    settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None,
    profile: ModelProfileSpec | None = None
) -> None

```

Initialize the model with optional settings and profile.
Parameters:
Name | Type | Description | Default
---|---|---|---
`settings` |  `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None` |  Model-specific settings that will be used as defaults for this model. |  `None`
`profile` |  `ModelProfileSpec | None` |  The model profile to use. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/models/__init__.py`
```
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
```
| ```
def __init__(
    self,
    *,
    settings: ModelSettings | None = None,
    profile: ModelProfileSpec | None = None,
) -> None:
    """Initialize the model with optional settings and profile.

    Args:
        settings: Model-specific settings that will be used as defaults for this model.
        profile: The model profile to use.
    """
    self._settings = settings
    self._profile = profile

```

---|---
####  settings `property`
```
settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None

```

Get the model settings.
####  request `abstractmethod` `async`
```
request(
    messages: [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")],
    model_settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None,
    model_request_parameters: ModelRequestParameters[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.ModelRequestParameters "ModelRequestParameters



      dataclass
   \(pydantic_ai.models.ModelRequestParameters\)"),
) -> ModelResponse[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "ModelResponse



      dataclass
   \(pydantic_ai.messages.ModelResponse\)")

```

Make a request to the model.
This is ultimately called by `pydantic_ai._agent_graph.ModelRequestNode._make_request(...)`.
Source code in `pydantic_ai_slim/pydantic_ai/models/__init__.py`
```
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
```
| ```
@abstractmethod
async def request(
    self,
    messages: list[ModelMessage],
    model_settings: ModelSettings | None,
    model_request_parameters: ModelRequestParameters,
) -> ModelResponse:
    """Make a request to the model.

    This is ultimately called by `pydantic_ai._agent_graph.ModelRequestNode._make_request(...)`.
    """
    raise NotImplementedError()

```

---|---
####  count_tokens `async`
```
count_tokens(
    messages: [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")],
    model_settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None,
    model_request_parameters: ModelRequestParameters[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.ModelRequestParameters "ModelRequestParameters



      dataclass
   \(pydantic_ai.models.ModelRequestParameters\)"),
) -> RequestUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RequestUsage "RequestUsage



      dataclass
   \(pydantic_ai.usage.RequestUsage\)")

```

Make a request to the model for counting tokens.
Source code in `pydantic_ai_slim/pydantic_ai/models/__init__.py`
```
685
686
687
688
689
690
691
692
693
```
| ```
async def count_tokens(
    self,
    messages: list[ModelMessage],
    model_settings: ModelSettings | None,
    model_request_parameters: ModelRequestParameters,
) -> RequestUsage:
    """Make a request to the model for counting tokens."""
    # This method is not required, but you need to implement it if you want to support `UsageLimits.count_tokens_before_request`.
    raise NotImplementedError(f'Token counting ahead of the request is not supported by {self.__class__.__name__}')

```

---|---
####  request_stream `async`
```
request_stream(
    messages: [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")],
    model_settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None,
    model_request_parameters: ModelRequestParameters[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.ModelRequestParameters "ModelRequestParameters



      dataclass
   \(pydantic_ai.models.ModelRequestParameters\)"),
    run_context: RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai._run_context.RunContext\)")[] | None = None,
) -> [StreamedResponse[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.StreamedResponse "StreamedResponse



      dataclass
   \(pydantic_ai.models.StreamedResponse\)")]

```

Make a request to the model and return a streaming response.
Source code in `pydantic_ai_slim/pydantic_ai/models/__init__.py`
```
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
```
| ```
@asynccontextmanager
async def request_stream(
    self,
    messages: list[ModelMessage],
    model_settings: ModelSettings | None,
    model_request_parameters: ModelRequestParameters,
    run_context: RunContext[Any] | None = None,
) -> AsyncIterator[StreamedResponse]:
    """Make a request to the model and return a streaming response."""
    # This method is not required, but you need to implement it if you want to support streamed responses
    raise NotImplementedError(f'Streamed requests not supported by this {self.__class__.__name__}')
    # yield is required to make this a generator for type checking
    # noinspection PyUnreachableCode
    yield  # pragma: no cover

```

---|---
####  customize_request_parameters
```
customize_request_parameters(
    model_request_parameters: ModelRequestParameters[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.ModelRequestParameters "ModelRequestParameters



      dataclass
   \(pydantic_ai.models.ModelRequestParameters\)"),
) -> ModelRequestParameters[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.ModelRequestParameters "ModelRequestParameters



      dataclass
   \(pydantic_ai.models.ModelRequestParameters\)")

```

Customize the request parameters for the model.
This method can be overridden by subclasses to modify the request parameters before sending them to the model. In particular, this method can be used to make modifications to the generated tool JSON schemas if necessary for vendor/model-specific reasons.
Source code in `pydantic_ai_slim/pydantic_ai/models/__init__.py`
```
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
```
| ```
def customize_request_parameters(self, model_request_parameters: ModelRequestParameters) -> ModelRequestParameters:
    """Customize the request parameters for the model.

    This method can be overridden by subclasses to modify the request parameters before sending them to the model.
    In particular, this method can be used to make modifications to the generated tool JSON schemas if necessary
    for vendor/model-specific reasons.
    """
    if transformer := self.profile.json_schema_transformer:
        model_request_parameters = replace(
            model_request_parameters,
            function_tools=[_customize_tool_def(transformer, t) for t in model_request_parameters.function_tools],
            output_tools=[_customize_tool_def(transformer, t) for t in model_request_parameters.output_tools],
        )
        if output_object := model_request_parameters.output_object:
            model_request_parameters = replace(
                model_request_parameters,
                output_object=_customize_output_object(transformer, output_object),
            )

    return model_request_parameters

```

---|---
####  prepare_request
```
prepare_request(
    model_settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None,
    model_request_parameters: ModelRequestParameters[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.ModelRequestParameters "ModelRequestParameters



      dataclass
   \(pydantic_ai.models.ModelRequestParameters\)"),
) -> [ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None, ModelRequestParameters[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.ModelRequestParameters "ModelRequestParameters



      dataclass
   \(pydantic_ai.models.ModelRequestParameters\)")]

```

Prepare request inputs before they are passed to the provider.
This merges the given `model_settings` with the model's own `settings` attribute and ensures `customize_request_parameters` is applied to the resolved [`ModelRequestParameters`](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.ModelRequestParameters "ModelRequestParameters



      dataclass
  "). Subclasses can override this method if they need to customize the preparation flow further, but most implementations should simply call `self.prepare_request(...)` at the start of their `request` (and related) methods.
Source code in `pydantic_ai_slim/pydantic_ai/models/__init__.py`
```
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
```
| ```
def prepare_request(
    self,
    model_settings: ModelSettings | None,
    model_request_parameters: ModelRequestParameters,
) -> tuple[ModelSettings | None, ModelRequestParameters]:
    """Prepare request inputs before they are passed to the provider.

    This merges the given `model_settings` with the model's own `settings` attribute and ensures
    `customize_request_parameters` is applied to the resolved
    [`ModelRequestParameters`][pydantic_ai.models.ModelRequestParameters]. Subclasses can override this method if
    they need to customize the preparation flow further, but most implementations should simply call
    `self.prepare_request(...)` at the start of their `request` (and related) methods.
    """
    model_settings = merge_model_settings(self.settings, model_settings)

    params = self.customize_request_parameters(model_request_parameters)

    if builtin_tools := params.builtin_tools:
        # Deduplicate builtin tools
        params = replace(
