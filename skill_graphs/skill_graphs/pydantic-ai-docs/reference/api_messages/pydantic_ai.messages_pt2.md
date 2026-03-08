    @property
    def identifier(self) -> str:
        """Identifier for the binary content, such as a unique ID.

        This identifier can be provided to the model in a message to allow it to refer to this file in a tool call argument,
        and the tool can look up the file in question by iterating over the message history and finding the matching `BinaryContent`.

        This identifier is only automatically passed to the model when the `BinaryContent` is returned by a tool.
        If you're passing the `BinaryContent` as a user message, it's up to you to include a separate text part with the identifier,
        e.g. "This is file <identifier>:" preceding the `BinaryContent`.

        It's also included in inline-text delimiters for providers that require inlining text documents, so the model can
        distinguish multiple files.
        """
        return self._identifier or _multi_modal_content_identifier(self.data)

    @property
    def data_uri(self) -> str:
        """Convert the `BinaryContent` to a data URI."""
        return f'data:{self.media_type};base64,{self.base64}'

    @property
    def base64(self) -> str:
        """Return the binary data as a base64-encoded string. Default encoding is UTF-8."""
        return base64.b64encode(self.data).decode()

    @property
    def is_audio(self) -> bool:
        """Return `True` if the media type is an audio type."""
        return self.media_type.startswith('audio/')

    @property
    def is_image(self) -> bool:
        """Return `True` if the media type is an image type."""
        return self.media_type.startswith('image/')

    @property
    def is_video(self) -> bool:
        """Return `True` if the media type is a video type."""
        return self.media_type.startswith('video/')

    @property
    def is_document(self) -> bool:
        """Return `True` if the media type is a document type."""
        return self.media_type in _document_format_lookup

    @property
    def format(self) -> str:
        """The file format of the binary content."""
        try:
            if self.is_audio:
                return _audio_format_lookup[self.media_type]
            elif self.is_image:
                return _image_format_lookup[self.media_type]
            elif self.is_video:
                return _video_format_lookup[self.media_type]
            else:
                return _document_format_lookup[self.media_type]
        except KeyError as e:
            raise ValueError(f'Unknown media type: {self.media_type}') from e

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  data `instance-attribute`
```
data:

```

The binary file data.
Use `.base64` to get the base64-encoded string.
####  media_type `instance-attribute`
```
media_type: (
    AudioMediaType
    | ImageMediaType
    | DocumentMediaType
    |
)

```

The media type of the binary data.
####  vendor_metadata `class-attribute` `instance-attribute`
```
vendor_metadata: [, ] | None = None

```

Vendor-specific metadata for the file.
Supported by: - `GoogleModel`: `BinaryContent.vendor_metadata` is used as `video_metadata`: https://ai.google.dev/gemini-api/docs/video-understanding#customize-video-processing - `OpenAIChatModel`, `OpenAIResponsesModel`: `BinaryContent.vendor_metadata['detail']` is used as `detail` setting for images - `XaiModel`: `BinaryContent.vendor_metadata['detail']` is used as `detail` setting for images
####  kind `class-attribute` `instance-attribute`
```
kind: ['binary'] = 'binary'

```

Type identifier, this is available on all parts as a discriminator.
####  narrow_type `staticmethod`
```
narrow_type(
    bc: BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)"),
) -> BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)") | BinaryImage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryImage "BinaryImage \(pydantic_ai.messages.BinaryImage\)")

```

Narrow the type of the `BinaryContent` to `BinaryImage` if it's an image.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
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
```
| ```
@staticmethod
def narrow_type(bc: BinaryContent) -> BinaryContent | BinaryImage:
    """Narrow the type of the `BinaryContent` to `BinaryImage` if it's an image."""
    if bc.is_image:
        return BinaryImage(
            data=bc.data,
            media_type=bc.media_type,
            identifier=bc.identifier,
            vendor_metadata=bc.vendor_metadata,
        )
    else:
        return bc

```

---|---
####  from_data_uri `classmethod`
```
from_data_uri(data_uri: ) -> BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)")

```

Create a `BinaryContent` from a data URI.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
523
524
525
526
527
528
529
530
```
| ```
@classmethod
def from_data_uri(cls, data_uri: str) -> BinaryContent:
    """Create a `BinaryContent` from a data URI."""
    prefix = 'data:'
    if not data_uri.startswith(prefix):
        raise ValueError('Data URI must start with "data:"')
    media_type, data = data_uri[len(prefix) :].split(';base64,', 1)
    return cls.narrow_type(cls(data=base64.b64decode(data), media_type=media_type))

```

---|---
####  from_path `classmethod`
```
from_path(path: []) -> BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)")

```

Create a `BinaryContent` from a path.
Defaults to 'application/octet-stream' if the media type cannot be inferred.
Raises:
Type | Description
---|---
|  if the file does not exist.
|  if the file cannot be read.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
```
| ```
@classmethod
def from_path(cls, path: PathLike[str]) -> BinaryContent:
    """Create a `BinaryContent` from a path.

    Defaults to 'application/octet-stream' if the media type cannot be inferred.

    Raises:
        FileNotFoundError: if the file does not exist.
        PermissionError: if the file cannot be read.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f'File not found: {path}')
    media_type, _ = _mime_types.guess_type(path)
    if media_type is None:
        media_type = 'application/octet-stream'

    return cls.narrow_type(cls(data=path.read_bytes(), media_type=media_type))

```

---|---
####  identifier `property`
```
identifier:

```

Identifier for the binary content, such as a unique ID.
This identifier can be provided to the model in a message to allow it to refer to this file in a tool call argument, and the tool can look up the file in question by iterating over the message history and finding the matching `BinaryContent`.
This identifier is only automatically passed to the model when the `BinaryContent` is returned by a tool. If you're passing the `BinaryContent` as a user message, it's up to you to include a separate text part with the identifier, e.g. "This is file :" preceding the `BinaryContent`.
It's also included in inline-text delimiters for providers that require inlining text documents, so the model can distinguish multiple files.
####  data_uri `property`
```
data_uri:

```

Convert the `BinaryContent` to a data URI.
####  base64 `property`
```
base64:

```

Return the binary data as a base64-encoded string. Default encoding is UTF-8.
####  is_audio `property`
```
is_audio:

```

Return `True` if the media type is an audio type.
####  is_image `property`
```
is_image:

```

Return `True` if the media type is an image type.
####  is_video `property`
```
is_video:

```

Return `True` if the media type is a video type.
####  is_document `property`
```
is_document:

```

Return `True` if the media type is a document type.
####  format `property`
```
format:

```

The file format of the binary content.
###  BinaryImage
Bases: `BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)")`
Binary content that's guaranteed to be an image.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
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
```
| ```
@pydantic_dataclass(
    repr=False,
    config=pydantic.ConfigDict(
        ser_json_bytes='base64',
        val_json_bytes='base64',
    ),
)
class BinaryImage(BinaryContent):
    """Binary content that's guaranteed to be an image."""

    # `pydantic_dataclass` replaces `__init__` so this method is never used.
    # The signature is kept so that pyright/IDE hints recognize the `identifier` alias for the `_identifier` field.
    def __init__(
        self,
        data: bytes,
        *,
        media_type: ImageMediaType | str,
        identifier: str | None = None,
        vendor_metadata: dict[str, Any] | None = None,
        kind: Literal['binary'] = 'binary',
        # Required for inline-snapshot which expects all dataclass `__init__` methods to take all field names as kwargs.
        _identifier: str | None = None,
    ) -> None: ...  # pragma: no cover

    def __post_init__(self):
        if not self.is_image:
            raise ValueError('`BinaryImage` must have a media type that starts with "image/"')

```

---|---
###  CachePoint `dataclass`
A cache point marker for prompt caching.
Can be inserted into UserPromptPart.content to mark cache boundaries. Models that don't support caching will filter these out.
Supported by:
  * Anthropic
  * Amazon Bedrock (Converse API)

Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
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
```
| ```
@dataclass
class CachePoint:
    """A cache point marker for prompt caching.

    Can be inserted into UserPromptPart.content to mark cache boundaries.
    Models that don't support caching will filter these out.

    Supported by:

    - Anthropic
    - Amazon Bedrock (Converse API)
    """

    kind: Literal['cache-point'] = 'cache-point'
    """Type identifier, this is available on all parts as a discriminator."""

    ttl: Literal['5m', '1h'] = '5m'
    """The cache time-to-live, either "5m" (5 minutes) or "1h" (1 hour).

    Supported by:

    * Anthropic (automatically omitted for Bedrock, as it does not support explicit TTL). See https://docs.claude.com/en/docs/build-with-claude/prompt-caching#1-hour-cache-duration for more information."""

```

---|---
####  kind `class-attribute` `instance-attribute`
```
kind: ['cache-point'] = 'cache-point'

```

Type identifier, this is available on all parts as a discriminator.
####  ttl `class-attribute` `instance-attribute`
```
ttl: ['5m', '1h'] = '5m'

```

The cache time-to-live, either "5m" (5 minutes) or "1h" (1 hour).
Supported by:
  * Anthropic (automatically omitted for Bedrock, as it does not support explicit TTL). See https://docs.claude.com/en/docs/build-with-claude/prompt-caching#1-hour-cache-duration for more information.


###  UploadedFileProviderName `module-attribute`
```
UploadedFileProviderName:  = [
    "anthropic",
    "openai",
    "google-gla",
    "google-vertex",
    "bedrock",
    "xai",
]

```

Provider names supported by [`UploadedFile`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.UploadedFile "UploadedFile").
###  UploadedFile
A reference to a file uploaded to a provider's file storage by ID.
This allows referencing files that have been uploaded via provider-specific file APIs rather than providing the file content directly.
Supported by:
  * [`AnthropicModel`](https://ai.pydantic.dev/api/models/anthropic/#pydantic_ai.models.anthropic.AnthropicModel "AnthropicModel



      dataclass
  ")
  * [`OpenAIChatModel`](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIChatModel "OpenAIChatModel



      dataclass
  ")
  * [`OpenAIResponsesModel`](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIResponsesModel "OpenAIResponsesModel



      dataclass
  ")
  * [`BedrockConverseModel`](https://ai.pydantic.dev/api/models/bedrock/#pydantic_ai.models.bedrock.BedrockConverseModel "BedrockConverseModel



      dataclass
  ")
  * [`GoogleModel`](https://ai.pydantic.dev/api/models/google/#pydantic_ai.models.google.GoogleModel "GoogleModel



      dataclass
  ")
  * [`XaiModel`](https://ai.pydantic.dev/api/models/xai/#pydantic_ai.models.xai.XaiModel "XaiModel")

Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
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
784
785
786
787
788
789
790
791
```
| ```
@pydantic_dataclass(repr=False, config=pydantic.ConfigDict(validate_by_name=True))
class UploadedFile:
    """A reference to a file uploaded to a provider's file storage by ID.

    This allows referencing files that have been uploaded via provider-specific file APIs
    rather than providing the file content directly.

    Supported by:

    - [`AnthropicModel`][pydantic_ai.models.anthropic.AnthropicModel]
    - [`OpenAIChatModel`][pydantic_ai.models.openai.OpenAIChatModel]
    - [`OpenAIResponsesModel`][pydantic_ai.models.openai.OpenAIResponsesModel]
    - [`BedrockConverseModel`][pydantic_ai.models.bedrock.BedrockConverseModel]
    - [`GoogleModel`][pydantic_ai.models.google.GoogleModel]
    - [`XaiModel`][pydantic_ai.models.xai.XaiModel]
    """

    file_id: str
    """The provider-specific file identifier."""

    provider_name: UploadedFileProviderName
    """The provider this file belongs to.

    This is required because file IDs are not portable across providers, and using a file ID
    with the wrong provider will always result in an error.

    Tip: Use `model.system` to get the provider name dynamically.
    """

    _: KW_ONLY

    vendor_metadata: dict[str, Any] | None = None
    """Vendor-specific metadata for the file.

    The expected shape of this dictionary depends on the provider:

    Supported by:
    - `GoogleModel`: used as `video_metadata` for video files
    """

    _media_type: Annotated[str | None, pydantic.Field(alias='media_type', default=None, exclude=True)] = field(
        compare=False, default=None
    )

    _identifier: Annotated[str | None, pydantic.Field(alias='identifier', default=None, exclude=True)] = field(
        compare=False, default=None
    )

    kind: Literal['uploaded-file'] = 'uploaded-file'
    """Type identifier, this is available on all parts as a discriminator."""

    # `pydantic_dataclass` replaces `__init__` so this method is never used.
    # The signature is kept so that pyright/IDE hints recognize the `media_type` and `identifier` aliases.
    def __init__(
        self,
        file_id: str,
        provider_name: UploadedFileProviderName,
        *,
        media_type: str | None = None,
        vendor_metadata: dict[str, Any] | None = None,
        identifier: str | None = None,
        kind: Literal['uploaded-file'] = 'uploaded-file',
        # Required for inline-snapshot which expects all dataclass `__init__` methods to take all field names as kwargs.
        _media_type: str | None = None,
        _identifier: str | None = None,
    ) -> None: ...  # pragma: no cover

    @pydantic.computed_field
    @property
    def media_type(self) -> str:
        """Return the media type of the file, inferred from `file_id` if not explicitly provided.

        Note: Inference relies on the file extension in `file_id`.
        For opaque file IDs (e.g., `'file-abc123'`), the media type will default to `'application/octet-stream'`.
        Inference relies on Python's `mimetypes` module, whose results may vary across platforms.

        Required by some providers (e.g., Bedrock) for certain file types.
        """
        if self._media_type is not None:
            return self._media_type
        parsed = urlparse(self.file_id)
        mime_type, _ = _mime_types.guess_type(parsed.path)
        return mime_type or 'application/octet-stream'

    @pydantic.computed_field
    @property
    def identifier(self) -> str:
        """The identifier of the file, such as a unique ID.

        This identifier can be provided to the model in a message to allow it to refer to this file in a tool call argument,
        and the tool can look up the file in question by iterating over the message history and finding the matching `UploadedFile`.

        This identifier is only automatically passed to the model when the `UploadedFile` is returned by a tool.
        If you're passing the `UploadedFile` as a user message, it's up to you to include a separate text part with the identifier,
        e.g. "This is file <identifier>:" preceding the `UploadedFile`.
        """
        return self._identifier or _multi_modal_content_identifier(self.file_id)

    @property
    def format(self) -> str:
        """A general-purpose media-type-to-format mapping.

        Maps media types to format strings (e.g. `'image/png'` -> `'png'`). Covers image, video,
        audio, and document types. Currently used by Bedrock, which requires explicit format strings.
        """
        media_type = self.media_type
        try:
            if media_type.startswith('image/'):
                return _image_format_lookup[media_type]
            elif media_type.startswith('video/'):
                return _video_format_lookup[media_type]
            elif media_type.startswith('audio/'):
                return _audio_format_lookup[media_type]
            else:
                return _document_format_lookup[media_type]
        except KeyError as e:
            raise ValueError(f'Unknown media type: {media_type}') from e

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  file_id `instance-attribute`
```
file_id:

```

The provider-specific file identifier.
####  provider_name `instance-attribute`
```
provider_name: UploadedFileProviderName[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.UploadedFileProviderName "UploadedFileProviderName



      module-attribute
   \(pydantic_ai.messages.UploadedFileProviderName\)")

```

The provider this file belongs to.
This is required because file IDs are not portable across providers, and using a file ID with the wrong provider will always result in an error.
Tip: Use `model.system` to get the provider name dynamically.
####  vendor_metadata `class-attribute` `instance-attribute`
```
vendor_metadata: [, ] | None = None

```

Vendor-specific metadata for the file.
The expected shape of this dictionary depends on the provider:
Supported by: - `GoogleModel`: used as `video_metadata` for video files
####  kind `class-attribute` `instance-attribute`
```
kind: ['uploaded-file'] = 'uploaded-file'

```

Type identifier, this is available on all parts as a discriminator.
####  media_type `property`
```
media_type:

```

Return the media type of the file, inferred from `file_id` if not explicitly provided.
Note: Inference relies on the file extension in `file_id`. For opaque file IDs (e.g., `'file-abc123'`), the media type will default to `'application/octet-stream'`. Inference relies on Python's `mimetypes` module, whose results may vary across platforms.
Required by some providers (e.g., Bedrock) for certain file types.
####  identifier `property`
```
identifier:

```

The identifier of the file, such as a unique ID.
This identifier can be provided to the model in a message to allow it to refer to this file in a tool call argument, and the tool can look up the file in question by iterating over the message history and finding the matching `UploadedFile`.
This identifier is only automatically passed to the model when the `UploadedFile` is returned by a tool. If you're passing the `UploadedFile` as a user message, it's up to you to include a separate text part with the identifier, e.g. "This is file :" preceding the `UploadedFile`.
####  format `property`
```
format:

```

A general-purpose media-type-to-format mapping.
Maps media types to format strings (e.g. `'image/png'` -> `'png'`). Covers image, video, audio, and document types. Currently used by Bedrock, which requires explicit format strings.
###  MULTI_MODAL_CONTENT_TYPES `module-attribute`
```
MULTI_MODAL_CONTENT_TYPES = (
    ImageUrl[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl "ImageUrl \(pydantic_ai.messages.ImageUrl\)"),
    AudioUrl[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AudioUrl "AudioUrl \(pydantic_ai.messages.AudioUrl\)"),
    DocumentUrl[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl "DocumentUrl \(pydantic_ai.messages.DocumentUrl\)"),
    VideoUrl[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.VideoUrl "VideoUrl \(pydantic_ai.messages.VideoUrl\)"),
    BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)"),
    UploadedFile[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.UploadedFile "UploadedFile \(pydantic_ai.messages.UploadedFile\)"),
)

```

Tuple of multi-modal content types for use with isinstance() checks.
###  MultiModalContent `module-attribute`
```
MultiModalContent = [
    ImageUrl[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl "ImageUrl \(pydantic_ai.messages.ImageUrl\)")
    | AudioUrl[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AudioUrl "AudioUrl \(pydantic_ai.messages.AudioUrl\)")
    | DocumentUrl[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl "DocumentUrl \(pydantic_ai.messages.DocumentUrl\)")
    | VideoUrl[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.VideoUrl "VideoUrl \(pydantic_ai.messages.VideoUrl\)")
    | BinaryContent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent "BinaryContent \(pydantic_ai.messages.BinaryContent\)")
    | UploadedFile[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.UploadedFile "UploadedFile \(pydantic_ai.messages.UploadedFile\)"),
    Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("kind"),
]

```

Union of all multi-modal content types with a discriminator for Pydantic validation.
###  ToolReturn `dataclass`
A structured return value for tools that need to provide both a return value and custom content to the model.
This class allows tools to return complex responses that include: - A return value for actual tool return - Custom content (including multi-modal content) to be sent to the model as a UserPromptPart - Optional metadata for application use
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
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
```
| ```
@dataclass(repr=False)
class ToolReturn:
    """A structured return value for tools that need to provide both a return value and custom content to the model.

    This class allows tools to return complex responses that include:
    - A return value for actual tool return
    - Custom content (including multi-modal content) to be sent to the model as a UserPromptPart
    - Optional metadata for application use
    """

    return_value: ToolReturnContent
    """The return value to be used in the tool response."""

    _: KW_ONLY

    content: str | Sequence[UserContent] | None = None
    """The content to be sent to the model as a UserPromptPart."""

    metadata: Any = None
    """Additional data that can be accessed programmatically by the application but is not sent to the LLM."""

    kind: Literal['tool-return'] = 'tool-return'

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  return_value `instance-attribute`
```
return_value: ToolReturnContent

```

The return value to be used in the tool response.
####  content `class-attribute` `instance-attribute`
```
content:  | [UserContent] | None = None

```

The content to be sent to the model as a UserPromptPart.
####  metadata `class-attribute` `instance-attribute`
```
metadata:  = None

```

Additional data that can be accessed programmatically by the application but is not sent to the LLM.
###  UserPromptPart `dataclass`
A user prompt, generally written by the end user.
Content comes from the `user_prompt` parameter of [`Agent.run`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run "run



      async
  "), [`Agent.run_sync`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run_sync "run_sync"), and [`Agent.run_stream`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run_stream "run_stream



      async
  ").
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
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
