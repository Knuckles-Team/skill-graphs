            raise exceptions.ModelRetry(e.error.message)

    if result.isError:
        message: str | None = None
        if result.content:  # pragma: no branch
            text_parts = [part.text for part in result.content if isinstance(part, mcp_types.TextContent)]
            message = '\n'.join(text_parts)

        raise exceptions.ModelRetry(message or 'MCP tool call failed')

    # Prefer structured content if there are only text parts, which per the docs would contain the JSON-encoded structured content for backward compatibility.
    # See https://github.com/modelcontextprotocol/python-sdk#structured-output
    if (structured := result.structuredContent) and not any(
        not isinstance(part, mcp_types.TextContent) for part in result.content
    ):
        # The MCP SDK wraps primitives and generic types like list in a `result` key, but we want to use the raw value returned by the tool function.
        # See https://github.com/modelcontextprotocol/python-sdk#structured-output
        if isinstance(structured, dict) and len(structured) == 1 and 'result' in structured:
            return structured['result']
        return structured

    mapped = [await self._map_tool_result_part(part) for part in result.content]
    return mapped[0] if len(mapped) == 1 else mapped

```

---|---
####  list_resources `async`
```
list_resources() -> [Resource[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.Resource "Resource



      dataclass
   \(pydantic_ai.mcp.Resource\)")]

```

Retrieve resources that are currently present on the server.
Resources are cached by default, with cache invalidation on: - `notifications/resources/list_changed` notifications from the server - `__aexit__` when the last context exits
Set `cache_resources=False` for servers that change resources without sending notifications.
Raises:
Type | Description
---|---
`MCPError[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.MCPError "MCPError \(pydantic_ai.mcp.MCPError\)")` |  If the server returns an error.
Source code in `pydantic_ai_slim/pydantic_ai/mcp_server.py`
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
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
```
| ```
async def list_resources(self) -> list[Resource]:
    """Retrieve resources that are currently present on the server.

    Resources are cached by default, with cache invalidation on:
    - `notifications/resources/list_changed` notifications from the server
    - `__aexit__` when the last context exits

    Set `cache_resources=False` for servers that change resources without sending notifications.

    Raises:
        MCPError: If the server returns an error.
    """
    if self.cache_resources and self._cached_resources is not None:
        return self._cached_resources

    async with self:
        if not self.capabilities.resources:
            return []
        try:
            result = await self._client.list_resources()
            resources = [Resource.from_mcp_sdk(r) for r in result.resources]
            if self.cache_resources:
                self._cached_resources = resources
            return resources
        except mcp_exceptions.McpError as e:
            raise MCPError.from_mcp_sdk(e) from e

```

---|---
####  list_resource_templates `async`
```
list_resource_templates() -> [ResourceTemplate[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.ResourceTemplate "ResourceTemplate



      dataclass
   \(pydantic_ai.mcp.ResourceTemplate\)")]

```

Retrieve resource templates that are currently present on the server.
Raises:
Type | Description
---|---
`MCPError[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.MCPError "MCPError \(pydantic_ai.mcp.MCPError\)")` |  If the server returns an error.
Source code in `pydantic_ai_slim/pydantic_ai/mcp_server.py`
```
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
```
| ```
async def list_resource_templates(self) -> list[ResourceTemplate]:
    """Retrieve resource templates that are currently present on the server.

    Raises:
        MCPError: If the server returns an error.
    """
    async with self:  # Ensure server is running
        if not self.capabilities.resources:
            return []
        try:
            result = await self._client.list_resource_templates()
        except mcp_exceptions.McpError as e:
            raise MCPError.from_mcp_sdk(e) from e
    return [ResourceTemplate.from_mcp_sdk(t) for t in result.resourceTemplates]

```

---|---
####  read_resource `async`
```
read_resource(
    uri: ,
) ->  | BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)") | [ | BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)")]

```

```
read_resource(
    uri: Resource[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.Resource "Resource



      dataclass
   \(pydantic_ai.mcp.Resource\)"),
) ->  | BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)") | [ | BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)")]

```

```
read_resource(
    uri:  | Resource[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.Resource "Resource



      dataclass
   \(pydantic_ai.mcp.Resource\)"),
) ->  | BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)") | [ | BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)")]

```

Read the contents of a specific resource by URI.
Parameters:
Name | Type | Description | Default
---|---|---|---
`uri` |  `Resource[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.Resource "Resource



      dataclass
   \(pydantic_ai.mcp.Resource\)")` |  The URI of the resource to read, or a Resource object. |  _required_
Returns:
Type | Description
---|---
`BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)") | BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)")]` |  The resource contents. If the resource has a single content item, returns that item directly.
`BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)") | BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)")]` |  If the resource has multiple content items, returns a list of items.
Raises:
Type | Description
---|---
`MCPError[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.MCPError "MCPError \(pydantic_ai.mcp.MCPError\)")` |  If the server returns an error.
Source code in `pydantic_ai_slim/pydantic_ai/mcp_server.py`
```
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
```
| ```
async def read_resource(
    self, uri: str | Resource
) -> str | messages.BinaryContent | list[str | messages.BinaryContent]:
    """Read the contents of a specific resource by URI.

    Args:
        uri: The URI of the resource to read, or a Resource object.

    Returns:
        The resource contents. If the resource has a single content item, returns that item directly.
        If the resource has multiple content items, returns a list of items.

    Raises:
        MCPError: If the server returns an error.
    """
    resource_uri = uri if isinstance(uri, str) else uri.uri
    async with self:  # Ensure server is running
        try:
            result = await self._client.read_resource(AnyUrl(resource_uri))
        except mcp_exceptions.McpError as e:
            raise MCPError.from_mcp_sdk(e) from e

    return (
        self._get_content(result.contents[0])
        if len(result.contents) == 1
        else [self._get_content(resource) for resource in result.contents]
    )

```

---|---
####  __aenter__ `async`
```
__aenter__() ->

```

Enter the MCP server context.
This will initialize the connection to the server. If this server is an [`MCPServerStdio`](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.MCPServerStdio "MCPServerStdio"), the server will first be started as a subprocess.
This is a no-op if the MCP server has already been entered.
Source code in `pydantic_ai_slim/pydantic_ai/mcp_server.py`
```
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
```
| ```
async def __aenter__(self) -> Self:
    """Enter the MCP server context.

    This will initialize the connection to the server.
    If this server is an [`MCPServerStdio`][pydantic_ai.mcp.MCPServerStdio], the server will first be started as a subprocess.

    This is a no-op if the MCP server has already been entered.
    """
    async with self._enter_lock:
        if self._running_count == 0:
            async with AsyncExitStack() as exit_stack:
                self._read_stream, self._write_stream = await exit_stack.enter_async_context(self.client_streams())

                client = ClientSession(
                    read_stream=self._read_stream,
                    write_stream=self._write_stream,
                    sampling_callback=self._sampling_callback if self.allow_sampling else None,
                    elicitation_callback=self.elicitation_callback,
                    logging_callback=self.log_handler,
                    read_timeout_seconds=timedelta(seconds=self.read_timeout),
                    message_handler=self._handle_notification,
                    client_info=self.client_info,
                )
                self._client = await exit_stack.enter_async_context(client)

                with anyio.fail_after(self.timeout):
                    result = await self._client.initialize()
                    self._server_info = result.serverInfo
                    self._server_capabilities = ServerCapabilities.from_mcp_sdk(result.capabilities)
                    self._instructions = result.instructions
                    if log_level := self.log_level:
                        await self._client.set_logging_level(log_level)

                self._exit_stack = exit_stack.pop_all()
        self._running_count += 1
    return self

```

---|---
####  is_running `property`
```
is_running:

```

Check if the MCP server is running.
###  MCPServerStdio
Bases: `MCPServer[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.MCPServer "MCPServer \(pydantic_ai.mcp.MCPServer\)")`
Runs an MCP server in a subprocess and communicates with it over stdin/stdout.
This class implements the stdio transport from the MCP specification. See
Note
Using this class as an async context manager will start the server as a subprocess when entering the context, and stop it when exiting the context.
Example:
```
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio

server = MCPServerStdio(  [](https://ai.pydantic.dev/api/mcp/#__code_72_annotation_1)
    'uv', args=['run', 'mcp-run-python', 'stdio'], timeout=10
)
agent = Agent('openai:gpt-5.2', toolsets=[server])

```

Source code in `pydantic_ai_slim/pydantic_ai/mcp_server.py`
```
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
```
| ```
class MCPServerStdio(MCPServer):
    """Runs an MCP server in a subprocess and communicates with it over stdin/stdout.

    This class implements the stdio transport from the MCP specification.
    See <https://spec.modelcontextprotocol.io/specification/2024-11-05/basic/transports/#stdio> for more information.

    !!! note
        Using this class as an async context manager will start the server as a subprocess when entering the context,
        and stop it when exiting the context.

    Example:
```python {py="3.10"}
    from pydantic_ai import Agent
    from pydantic_ai.mcp import MCPServerStdio

    server = MCPServerStdio(  # (1)!
        'uv', args=['run', 'mcp-run-python', 'stdio'], timeout=10
    )
    agent = Agent('openai:gpt-5.2', toolsets=[server])
```

    1. See [MCP Run Python](https://github.com/pydantic/mcp-run-python) for more information.
    """

    command: str
    """The command to run."""

    args: Sequence[str]
    """The arguments to pass to the command."""

    env: dict[str, str] | None
    """The environment variables the CLI server will have access to.

    By default the subprocess will not inherit any environment variables from the parent process.
    If you want to inherit the environment variables from the parent process, use `env=os.environ`.
    """

    cwd: str | Path | None
    """The working directory to use when spawning the process."""

    # last fields are re-defined from the parent class so they appear as fields
    tool_prefix: str | None
    log_level: mcp_types.LoggingLevel | None
    log_handler: LoggingFnT | None
    timeout: float
    read_timeout: float
    process_tool_call: ProcessToolCallback | None
    allow_sampling: bool
    sampling_model: models.Model | None
    max_retries: int
    elicitation_callback: ElicitationFnT | None = None
    cache_tools: bool
    cache_resources: bool

    def __init__(
        self,
        command: str,
        args: Sequence[str],
        *,
        env: dict[str, str] | None = None,
        cwd: str | Path | None = None,
        tool_prefix: str | None = None,
        log_level: mcp_types.LoggingLevel | None = None,
        log_handler: LoggingFnT | None = None,
        timeout: float = 5,
        read_timeout: float = 5 * 60,
        process_tool_call: ProcessToolCallback | None = None,
        allow_sampling: bool = True,
        sampling_model: models.Model | None = None,
        max_retries: int = 1,
        elicitation_callback: ElicitationFnT | None = None,
        cache_tools: bool = True,
        cache_resources: bool = True,
        id: str | None = None,
        client_info: mcp_types.Implementation | None = None,
    ):
        """Build a new MCP server.

        Args:
            command: The command to run.
            args: The arguments to pass to the command.
            env: The environment variables to set in the subprocess.
            cwd: The working directory to use when spawning the process.
            tool_prefix: A prefix to add to all tools that are registered with the server.
            log_level: The log level to set when connecting to the server, if any.
            log_handler: A handler for logging messages from the server.
            timeout: The timeout in seconds to wait for the client to initialize.
            read_timeout: Maximum time in seconds to wait for new messages before timing out.
            process_tool_call: Hook to customize tool calling and optionally pass extra metadata.
            allow_sampling: Whether to allow MCP sampling through this client.
            sampling_model: The model to use for sampling.
            max_retries: The maximum number of times to retry a tool call.
            elicitation_callback: Callback function to handle elicitation requests from the server.
            cache_tools: Whether to cache the list of tools.
                See [`MCPServer.cache_tools`][pydantic_ai.mcp.MCPServer.cache_tools].
            cache_resources: Whether to cache the list of resources.
                See [`MCPServer.cache_resources`][pydantic_ai.mcp.MCPServer.cache_resources].
            id: An optional unique ID for the MCP server. An MCP server needs to have an ID in order to be used in a durable execution environment like Temporal, in which case the ID will be used to identify the server's activities within the workflow.
            client_info: Information describing the MCP client implementation.
        """
        self.command = command
        self.args = args
        self.env = env
        self.cwd = cwd

        super().__init__(
            tool_prefix,
            log_level,
            log_handler,
            timeout,
            read_timeout,
            process_tool_call,
            allow_sampling,
            sampling_model,
            max_retries,
            elicitation_callback,
            cache_tools,
            cache_resources,
            id=id,
            client_info=client_info,
        )

    @classmethod
    def __get_pydantic_core_schema__(cls, _: Any, __: Any) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            lambda dct: MCPServerStdio(**dct),
            core_schema.typed_dict_schema(
                {
                    'command': core_schema.typed_dict_field(core_schema.str_schema()),
                    'args': core_schema.typed_dict_field(core_schema.list_schema(core_schema.str_schema())),
                    'env': core_schema.typed_dict_field(
                        core_schema.dict_schema(core_schema.str_schema(), core_schema.str_schema()),
                        required=False,
                    ),
                }
            ),
        )

    @asynccontextmanager
    async def client_streams(
        self,
    ) -> AsyncIterator[
        tuple[
            MemoryObjectReceiveStream[SessionMessage | Exception],
            MemoryObjectSendStream[SessionMessage],
        ]
    ]:
        server = StdioServerParameters(command=self.command, args=list(self.args), env=self.env, cwd=self.cwd)
        async with stdio_client(server=server) as (read_stream, write_stream):
            yield read_stream, write_stream

    def __repr__(self) -> str:
        repr_args = [
            f'command={self.command!r}',
            f'args={self.args!r}',
        ]
        if self.id:
            repr_args.append(f'id={self.id!r}')  # pragma: lax no cover
        return f'{self.__class__.__name__}({", ".join(repr_args)})'

    def __eq__(self, value: object, /) -> bool:
        return (
            super().__eq__(value)
            and isinstance(value, MCPServerStdio)
            and self.command == value.command
            and self.args == value.args
            and self.env == value.env
            and self.cwd == value.cwd
        )

```

---|---
####  __init__
```
__init__(
    command: ,
    args: [],
    *,
    env: [, ] | None = None,
    cwd:  |  | None = None,
    tool_prefix:  | None = None,
    log_level: LoggingLevel | None = None,
    log_handler: LoggingFnT | None = None,
    timeout:  = 5,
    read_timeout:  = 5 * 60,
    process_tool_call: ProcessToolCallback[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.ProcessToolCallback "ProcessToolCallback



      module-attribute
   \(pydantic_ai.mcp.ProcessToolCallback\)") | None = None,
    allow_sampling:  = True,
    sampling_model: Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)") | None = None,
    max_retries:  = 1,
    elicitation_callback: ElicitationFnT | None = None,
    cache_tools:  = True,
    cache_resources:  = True,
    id:  | None = None,
    client_info:  | None = None
)

```

Build a new MCP server.
Parameters:
Name | Type | Description | Default
---|---|---|---
`command` |  |  The command to run. |  _required_
`args` |  |  The arguments to pass to the command. |  _required_
`env` |  |  The environment variables to set in the subprocess. |  `None`
`cwd` |  |  The working directory to use when spawning the process. |  `None`
`tool_prefix` |  |  A prefix to add to all tools that are registered with the server. |  `None`
`log_level` |  `LoggingLevel | None` |  The log level to set when connecting to the server, if any. |  `None`
`log_handler` |  `LoggingFnT | None` |  A handler for logging messages from the server. |  `None`
`timeout` |  |  The timeout in seconds to wait for the client to initialize. |  `5`
`read_timeout` |  |  Maximum time in seconds to wait for new messages before timing out. |  `5 * 60`
`process_tool_call` |  `ProcessToolCallback[](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.ProcessToolCallback "ProcessToolCallback



      module-attribute
   \(pydantic_ai.mcp.ProcessToolCallback\)") | None` |  Hook to customize tool calling and optionally pass extra metadata. |  `None`
`allow_sampling` |  |  Whether to allow MCP sampling through this client. |  `True`
`sampling_model` |  `Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)") | None` |  The model to use for sampling. |  `None`
`max_retries` |  |  The maximum number of times to retry a tool call. |  `1`
`elicitation_callback` |  `ElicitationFnT | None` |  Callback function to handle elicitation requests from the server. |  `None`
`cache_tools` |  |  Whether to cache the list of tools. See [`MCPServer.cache_tools`](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.MCPServer.cache_tools "cache_tools



      instance-attribute
  "). |  `True`
`cache_resources` |  |  Whether to cache the list of resources. See [`MCPServer.cache_resources`](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.MCPServer.cache_resources "cache_resources



      instance-attribute
  "). |  `True`
`id` |  |  An optional unique ID for the MCP server. An MCP server needs to have an ID in order to be used in a durable execution environment like Temporal, in which case the ID will be used to identify the server's activities within the workflow. |  `None`
`client_info` |  |  Information describing the MCP client implementation. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/mcp_server.py`
```
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
```
| ```
def __init__(
    self,
    command: str,
    args: Sequence[str],
    *,
    env: dict[str, str] | None = None,
    cwd: str | Path | None = None,
    tool_prefix: str | None = None,
    log_level: mcp_types.LoggingLevel | None = None,
    log_handler: LoggingFnT | None = None,
    timeout: float = 5,
    read_timeout: float = 5 * 60,
    process_tool_call: ProcessToolCallback | None = None,
    allow_sampling: bool = True,
    sampling_model: models.Model | None = None,
    max_retries: int = 1,
    elicitation_callback: ElicitationFnT | None = None,
    cache_tools: bool = True,
    cache_resources: bool = True,
    id: str | None = None,
    client_info: mcp_types.Implementation | None = None,
):
    """Build a new MCP server.

    Args:
        command: The command to run.
        args: The arguments to pass to the command.
        env: The environment variables to set in the subprocess.
        cwd: The working directory to use when spawning the process.
        tool_prefix: A prefix to add to all tools that are registered with the server.
        log_level: The log level to set when connecting to the server, if any.
        log_handler: A handler for logging messages from the server.
        timeout: The timeout in seconds to wait for the client to initialize.
        read_timeout: Maximum time in seconds to wait for new messages before timing out.
        process_tool_call: Hook to customize tool calling and optionally pass extra metadata.
        allow_sampling: Whether to allow MCP sampling through this client.
        sampling_model: The model to use for sampling.
        max_retries: The maximum number of times to retry a tool call.
        elicitation_callback: Callback function to handle elicitation requests from the server.
        cache_tools: Whether to cache the list of tools.
            See [`MCPServer.cache_tools`][pydantic_ai.mcp.MCPServer.cache_tools].
        cache_resources: Whether to cache the list of resources.
            See [`MCPServer.cache_resources`][pydantic_ai.mcp.MCPServer.cache_resources].
        id: An optional unique ID for the MCP server. An MCP server needs to have an ID in order to be used in a durable execution environment like Temporal, in which case the ID will be used to identify the server's activities within the workflow.
        client_info: Information describing the MCP client implementation.
    """
    self.command = command
    self.args = args
    self.env = env
    self.cwd = cwd

    super().__init__(
        tool_prefix,
        log_level,
        log_handler,
        timeout,
        read_timeout,
        process_tool_call,
        allow_sampling,
        sampling_model,
        max_retries,
        elicitation_callback,
        cache_tools,
        cache_resources,
        id=id,
        client_info=client_info,
    )

```

---|---
####  command `instance-attribute`
