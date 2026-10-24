# `pydantic_ai.messages`
The structure of [`ModelMessage`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
  ") can be shown as a graph:
###  FinishReason `module-attribute`
```
FinishReason:  = [
    "stop", "length", "content_filter", "tool_call", "error"
]

```

Reason the model finished generating the response, normalized to OpenTelemetry values.
###  ForceDownloadMode `module-attribute`
```
ForceDownloadMode:  =  | ["allow-local"]

```

Type for the force_download parameter on FileUrl subclasses.
  * `False`: The URL is sent directly to providers that support it. For providers that don't, the file is downloaded with SSRF protection (blocks private IPs and cloud metadata).
  * `True`: The file is always downloaded with SSRF protection (blocks private IPs and cloud metadata).
  * `'allow-local'`: The file is always downloaded, allowing private IPs but still blocking cloud metadata.


###  ProviderDetailsDelta `module-attribute`
```
ProviderDetailsDelta:  = (
    [, ]
    | [[[, ] | None], [, ]]
    | None
)

```

Type for provider_details input: can be a static dict, a callback to update existing details, or None.
###  SystemPromptPart `dataclass`
A system prompt, generally written by the application developer.
This gives the model context and guidance on how to respond.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
```
| ```
@dataclass(repr=False)
class SystemPromptPart:
    """A system prompt, generally written by the application developer.

    This gives the model context and guidance on how to respond.
    """

    content: str
    """The content of the prompt."""

    _: KW_ONLY

    timestamp: datetime = field(default_factory=_now_utc)
    """The timestamp of the prompt."""

    dynamic_ref: str | None = None
    """The ref of the dynamic system prompt function that generated this part.

    Only set if system prompt is dynamic, see [`system_prompt`][pydantic_ai.agent.Agent.system_prompt] for more information.
    """

    part_kind: Literal['system-prompt'] = 'system-prompt'
    """Part type identifier, this is available on all parts as a discriminator."""

    def otel_event(self, settings: InstrumentationSettings) -> LogRecord:
        return LogRecord(
            attributes={'event.name': 'gen_ai.system.message'},
            body={'role': 'system', **({'content': self.content} if settings.include_content else {})},
        )

    def otel_message_parts(self, settings: InstrumentationSettings) -> list[_otel_messages.MessagePart]:
        return [_otel_messages.TextPart(type='text', **{'content': self.content} if settings.include_content else {})]

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  content `instance-attribute`
```
content:

```

The content of the prompt.
####  timestamp `class-attribute` `instance-attribute`
```
timestamp:  = (default_factory=now_utc)

```

The timestamp of the prompt.
####  dynamic_ref `class-attribute` `instance-attribute`
```
dynamic_ref:  | None = None

```

The ref of the dynamic system prompt function that generated this part.
Only set if system prompt is dynamic, see [`system_prompt`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.system_prompt "system_prompt") for more information.
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: ['system-prompt'] = 'system-prompt'

```

Part type identifier, this is available on all parts as a discriminator.
###  FileUrl
Bases:
Abstract base class for any URL-based file.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
```
| ```
@pydantic_dataclass(repr=False, config=pydantic.ConfigDict(validate_by_name=True))
class FileUrl(ABC):
    """Abstract base class for any URL-based file."""

    url: str
    """The URL of the file."""

    _: KW_ONLY

    force_download: ForceDownloadMode = False
    """Controls whether the file is downloaded and how SSRF protection is applied:

    * If `False`, the URL is sent directly to providers that support it. For providers that don't,
      the file is downloaded with SSRF protection (blocks private IPs and cloud metadata).
    * If `True`, the file is always downloaded with SSRF protection (blocks private IPs and cloud metadata).
    * If `'allow-local'`, the file is always downloaded, allowing private IPs but still blocking cloud metadata.
    """

    vendor_metadata: dict[str, Any] | None = None
    """Vendor-specific metadata for the file.

    Supported by:
    - `GoogleModel`: `VideoUrl.vendor_metadata` is used as `video_metadata`: https://ai.google.dev/gemini-api/docs/video-understanding#customize-video-processing
    - `OpenAIChatModel`, `OpenAIResponsesModel`: `ImageUrl.vendor_metadata['detail']` is used as `detail` setting for images
    - `XaiModel`: `ImageUrl.vendor_metadata['detail']` is used as `detail` setting for images
    """

    _media_type: Annotated[str | None, pydantic.Field(alias='media_type', default=None, exclude=True)] = field(
        compare=False, default=None
    )

    _identifier: Annotated[str | None, pydantic.Field(alias='identifier', default=None, exclude=True)] = field(
        compare=False, default=None
    )

    # `pydantic_dataclass` replaces `__init__` so this method is never used.
    # The signature is kept so that pyright/IDE hints recognize the `media_type` and `identifier` aliases.
    def __init__(
        self,
        url: str,
        *,
        media_type: str | None = None,
        identifier: str | None = None,
        force_download: ForceDownloadMode = False,
        vendor_metadata: dict[str, Any] | None = None,
        # Required for inline-snapshot which expects all dataclass `__init__` methods to take all field names as kwargs.
        _media_type: str | None = None,
        _identifier: str | None = None,
    ) -> None: ...  # pragma: no cover

    @pydantic.computed_field
    @property
    def media_type(self) -> str:
        """Return the media type of the file, based on the URL or the provided `media_type`."""
        return self._media_type or self._infer_media_type()

    @pydantic.computed_field
    @property
    def identifier(self) -> str:
        """The identifier of the file, such as a unique ID.

        This identifier can be provided to the model in a message to allow it to refer to this file in a tool call argument,
        and the tool can look up the file in question by iterating over the message history and finding the matching `FileUrl`.

        This identifier is only automatically passed to the model when the `FileUrl` is returned by a tool.
        If you're passing the `FileUrl` as a user message, it's up to you to include a separate text part with the identifier,
        e.g. "This is file <identifier>:" preceding the `FileUrl`.

        It's also included in inline-text delimiters for providers that require inlining text documents, so the model can
        distinguish multiple files.
        """
        return self._identifier or _multi_modal_content_identifier(self.url)

    @abstractmethod
    def _infer_media_type(self) -> str:
        """Infer the media type of the file based on the URL."""
        raise NotImplementedError

    @property
    @abstractmethod
    def format(self) -> str:
        """The file format."""
        raise NotImplementedError

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  url `instance-attribute`
```
url:

```

The URL of the file.
####  force_download `class-attribute` `instance-attribute`
```
force_download: ForceDownloadMode[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ForceDownloadMode "ForceDownloadMode



      module-attribute
   \(pydantic_ai.messages.ForceDownloadMode\)") = False

```

Controls whether the file is downloaded and how SSRF protection is applied:
  * If `False`, the URL is sent directly to providers that support it. For providers that don't, the file is downloaded with SSRF protection (blocks private IPs and cloud metadata).
  * If `True`, the file is always downloaded with SSRF protection (blocks private IPs and cloud metadata).
  * If `'allow-local'`, the file is always downloaded, allowing private IPs but still blocking cloud metadata.


####  vendor_metadata `class-attribute` `instance-attribute`
```
vendor_metadata: [, ] | None = None

```

Vendor-specific metadata for the file.
Supported by: - `GoogleModel`: `VideoUrl.vendor_metadata` is used as `video_metadata`: https://ai.google.dev/gemini-api/docs/video-understanding#customize-video-processing - `OpenAIChatModel`, `OpenAIResponsesModel`: `ImageUrl.vendor_metadata['detail']` is used as `detail` setting for images - `XaiModel`: `ImageUrl.vendor_metadata['detail']` is used as `detail` setting for images
####  media_type `property`
```
media_type:

```

Return the media type of the file, based on the URL or the provided `media_type`.
####  identifier `property`
```
identifier:

```

The identifier of the file, such as a unique ID.
This identifier can be provided to the model in a message to allow it to refer to this file in a tool call argument, and the tool can look up the file in question by iterating over the message history and finding the matching `FileUrl`.
This identifier is only automatically passed to the model when the `FileUrl` is returned by a tool. If you're passing the `FileUrl` as a user message, it's up to you to include a separate text part with the identifier, e.g. "This is file :" preceding the `FileUrl`.
It's also included in inline-text delimiters for providers that require inlining text documents, so the model can distinguish multiple files.
####  format `abstractmethod` `property`
```
format:

```

The file format.
###  VideoUrl
Bases: `FileUrl[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FileUrl "FileUrl \(pydantic_ai.messages.FileUrl\)")`
A URL to a video.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
```
| ```
@pydantic_dataclass(repr=False, config=pydantic.ConfigDict(validate_by_name=True))
class VideoUrl(FileUrl):
    """A URL to a video."""

    url: str
    """The URL of the video."""

    _: KW_ONLY

    kind: Literal['video-url'] = 'video-url'
    """Type identifier, this is available on all parts as a discriminator."""

    # `pydantic_dataclass` replaces `__init__` so this method is never used.
    # The signature is kept so that pyright/IDE hints recognize the aliases for the `_media_type` and `_identifier` fields.
    def __init__(
        self,
        url: str,
        *,
        media_type: str | None = None,
        identifier: str | None = None,
        force_download: ForceDownloadMode = False,
        vendor_metadata: dict[str, Any] | None = None,
        kind: Literal['video-url'] = 'video-url',
        # Required for inline-snapshot which expects all dataclass `__init__` methods to take all field names as kwargs.
        _media_type: str | None = None,
        _identifier: str | None = None,
    ) -> None: ...  # pragma: no cover

    def _infer_media_type(self) -> str:
        """Return the media type of the video, based on the url."""
        # Assume that YouTube videos are mp4 because there would be no extension
        # to infer from. This should not be a problem, as Gemini disregards media
        # type for YouTube URLs.
        if self.is_youtube:
            return 'video/mp4'

        mime_type, _ = _mime_types.guess_type(self.url)
        if mime_type is None:
            raise ValueError(
                f'Could not infer media type from video URL: {self.url}. Explicitly provide a `media_type` instead.'
            )
        return mime_type

    @property
    def is_youtube(self) -> bool:
        """True if the URL has a YouTube domain."""
        parsed = urlparse(self.url)
        hostname = parsed.hostname
        return hostname in ('youtu.be', 'youtube.com', 'www.youtube.com')

    @property
    def format(self) -> VideoFormat:
        """The file format of the video.

        The choice of supported formats were based on the Bedrock Converse API. Other APIs don't require to use a format.
        """
        return _video_format_lookup[self.media_type]

```

---|---
####  url `instance-attribute`
```
url:

```

The URL of the video.
####  kind `class-attribute` `instance-attribute`
```
kind: ['video-url'] = 'video-url'

```

Type identifier, this is available on all parts as a discriminator.
####  is_youtube `property`
```
is_youtube:

```

True if the URL has a YouTube domain.
####  format `property`
```
format: VideoFormat

```

The file format of the video.
The choice of supported formats were based on the Bedrock Converse API. Other APIs don't require to use a format.
###  AudioUrl
Bases: `FileUrl[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FileUrl "FileUrl \(pydantic_ai.messages.FileUrl\)")`
A URL to an audio file.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
```
| ```
@pydantic_dataclass(repr=False, config=pydantic.ConfigDict(validate_by_name=True))
class AudioUrl(FileUrl):
    """A URL to an audio file."""

    url: str
    """The URL of the audio file."""

    _: KW_ONLY

    kind: Literal['audio-url'] = 'audio-url'
    """Type identifier, this is available on all parts as a discriminator."""

    # `pydantic_dataclass` replaces `__init__` so this method is never used.
    # The signature is kept so that pyright/IDE hints recognize the aliases for the `_media_type` and `_identifier` fields.
    def __init__(
        self,
        url: str,
        *,
        media_type: str | None = None,
        identifier: str | None = None,
        force_download: ForceDownloadMode = False,
        vendor_metadata: dict[str, Any] | None = None,
        kind: Literal['audio-url'] = 'audio-url',
        # Required for inline-snapshot which expects all dataclass `__init__` methods to take all field names as kwargs.
        _media_type: str | None = None,
        _identifier: str | None = None,
    ) -> None: ...  # pragma: no cover

    def _infer_media_type(self) -> str:
        """Return the media type of the audio file, based on the url.

        References:
        - Gemini: https://ai.google.dev/gemini-api/docs/audio#supported-formats
        """
        mime_type, _ = _mime_types.guess_type(self.url)
        if mime_type is None:
            raise ValueError(
                f'Could not infer media type from audio URL: {self.url}. Explicitly provide a `media_type` instead.'
            )
        return mime_type

    @property
    def format(self) -> AudioFormat:
        """The file format of the audio file."""
        return _audio_format_lookup[self.media_type]

```

---|---
####  url `instance-attribute`
```
url:

```

The URL of the audio file.
####  kind `class-attribute` `instance-attribute`
```
kind: ['audio-url'] = 'audio-url'

```

Type identifier, this is available on all parts as a discriminator.
####  format `property`
```
format: AudioFormat

```

The file format of the audio file.
###  ImageUrl
Bases: `FileUrl[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FileUrl "FileUrl \(pydantic_ai.messages.FileUrl\)")`
A URL to an image.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
```
| ```
@pydantic_dataclass(repr=False, config=pydantic.ConfigDict(validate_by_name=True))
class ImageUrl(FileUrl):
    """A URL to an image."""

    url: str
    """The URL of the image."""

    _: KW_ONLY

    kind: Literal['image-url'] = 'image-url'
    """Type identifier, this is available on all parts as a discriminator."""

    # `pydantic_dataclass` replaces `__init__` so this method is never used.
    # The signature is kept so that pyright/IDE hints recognize the aliases for the `_media_type` and `_identifier` fields.
    def __init__(
        self,
        url: str,
        *,
        media_type: str | None = None,
        identifier: str | None = None,
        force_download: ForceDownloadMode = False,
        vendor_metadata: dict[str, Any] | None = None,
        kind: Literal['image-url'] = 'image-url',
        # Required for inline-snapshot which expects all dataclass `__init__` methods to take all field names as kwargs.
        _media_type: str | None = None,
        _identifier: str | None = None,
    ) -> None: ...  # pragma: no cover

    def _infer_media_type(self) -> str:
        """Return the media type of the image, based on the url."""
        mime_type, _ = _mime_types.guess_type(self.url)
        if mime_type is None:
            raise ValueError(
                f'Could not infer media type from image URL: {self.url}. Explicitly provide a `media_type` instead.'
            )
        return mime_type

    @property
    def format(self) -> ImageFormat:
        """The file format of the image.

        The choice of supported formats were based on the Bedrock Converse API. Other APIs don't require to use a format.
        """
        return _image_format_lookup[self.media_type]

```

---|---
####  url `instance-attribute`
```
url:

```

The URL of the image.
####  kind `class-attribute` `instance-attribute`
```
kind: ['image-url'] = 'image-url'

```

Type identifier, this is available on all parts as a discriminator.
####  format `property`
```
format: ImageFormat

```

The file format of the image.
The choice of supported formats were based on the Bedrock Converse API. Other APIs don't require to use a format.
###  DocumentUrl
Bases: `FileUrl[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FileUrl "FileUrl \(pydantic_ai.messages.FileUrl\)")`
The URL of the document.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
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
```
| ```
@pydantic_dataclass(repr=False, config=pydantic.ConfigDict(validate_by_name=True))
class DocumentUrl(FileUrl):
    """The URL of the document."""

    url: str
    """The URL of the document."""

    _: KW_ONLY

    kind: Literal['document-url'] = 'document-url'
    """Type identifier, this is available on all parts as a discriminator."""

    # `pydantic_dataclass` replaces `__init__` so this method is never used.
    # The signature is kept so that pyright/IDE hints recognize the aliases for the `_media_type` and `_identifier` fields.
    def __init__(
        self,
        url: str,
        *,
        media_type: str | None = None,
        identifier: str | None = None,
        force_download: ForceDownloadMode = False,
        vendor_metadata: dict[str, Any] | None = None,
        kind: Literal['document-url'] = 'document-url',
        # Required for inline-snapshot which expects all dataclass `__init__` methods to take all field names as kwargs.
        _media_type: str | None = None,
        _identifier: str | None = None,
    ) -> None: ...  # pragma: no cover

    def _infer_media_type(self) -> str:
        """Return the media type of the document, based on the url."""
        mime_type, _ = _mime_types.guess_type(self.url)
        if mime_type is None:
            raise ValueError(
                f'Could not infer media type from document URL: {self.url}. Explicitly provide a `media_type` instead.'
            )
        return mime_type

    @property
    def format(self) -> DocumentFormat:
        """The file format of the document.

        The choice of supported formats were based on the Bedrock Converse API. Other APIs don't require to use a format.
        """
        media_type = self.media_type
        try:
            return _document_format_lookup[media_type]
        except KeyError as e:
            raise ValueError(f'Unknown document media type: {media_type}') from e

```

---|---
####  url `instance-attribute`
```
url:

```

The URL of the document.
####  kind `class-attribute` `instance-attribute`
```
kind: ['document-url'] = 'document-url'

```

Type identifier, this is available on all parts as a discriminator.
####  format `property`
```
format: DocumentFormat

```

The file format of the document.
The choice of supported formats were based on the Bedrock Converse API. Other APIs don't require to use a format.
###  BinaryContent
Binary content, e.g. an audio or image file.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
459
460
461
462
463
464
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
492
493
494
495
496
497
498
499
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
527
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
550
551
552
553
554
555
556
557
558
559
560
561
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
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
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
```
| ```
@pydantic_dataclass(
    repr=False,
    config=pydantic.ConfigDict(
        ser_json_bytes='base64',
        val_json_bytes='base64',
    ),
)
class BinaryContent:
    """Binary content, e.g. an audio or image file."""

    data: bytes
    """The binary file data.

    Use `.base64` to get the base64-encoded string.
    """

    _: KW_ONLY

    media_type: AudioMediaType | ImageMediaType | DocumentMediaType | str
    """The media type of the binary data."""

    vendor_metadata: dict[str, Any] | None = None
    """Vendor-specific metadata for the file.

    Supported by:
    - `GoogleModel`: `BinaryContent.vendor_metadata` is used as `video_metadata`: https://ai.google.dev/gemini-api/docs/video-understanding#customize-video-processing
    - `OpenAIChatModel`, `OpenAIResponsesModel`: `BinaryContent.vendor_metadata['detail']` is used as `detail` setting for images
    - `XaiModel`: `BinaryContent.vendor_metadata['detail']` is used as `detail` setting for images
    """

    _identifier: Annotated[str | None, pydantic.Field(alias='identifier', default=None, exclude=True)] = field(
        compare=False, default=None
    )

    kind: Literal['binary'] = 'binary'
    """Type identifier, this is available on all parts as a discriminator."""

    # `pydantic_dataclass` replaces `__init__` so this method is never used.
    # The signature is kept so that pyright/IDE hints recognize the `identifier` alias for the `_identifier` field.
    def __init__(
        self,
        data: bytes,
        *,
        media_type: AudioMediaType | ImageMediaType | DocumentMediaType | str,
        identifier: str | None = None,
        vendor_metadata: dict[str, Any] | None = None,
        kind: Literal['binary'] = 'binary',
        # Required for inline-snapshot which expects all dataclass `__init__` methods to take all field names as kwargs.
        _identifier: str | None = None,
    ) -> None: ...  # pragma: no cover

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

    @classmethod
    def from_data_uri(cls, data_uri: str) -> BinaryContent:
        """Create a `BinaryContent` from a data URI."""
        prefix = 'data:'
        if not data_uri.startswith(prefix):
            raise ValueError('Data URI must start with "data:"')
        media_type, data = data_uri[len(prefix) :].split(';base64,', 1)
        return cls.narrow_type(cls(data=base64.b64decode(data), media_type=media_type))

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

    @pydantic.computed_field
